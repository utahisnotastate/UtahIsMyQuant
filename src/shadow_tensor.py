"""
Shadow Tensor Audit — background inverse-model probe for alpha degradation.
Detects when forward signals mirror the inverted manifold (market-impact noise).
"""
from __future__ import annotations

import asyncio
import threading
import time
from collections import deque
from dataclasses import dataclass, field

import numpy as np

from .manifold_kernel import ManifoldEngine


@dataclass
class AuditSnapshot:
    degradation_score: float
    mirror_rate: float
    samples: int
    healthy: bool


class ShadowTensorAudit:
    """Runs inverse manifold checks to flag self-induced / mirrored alpha decay."""

    def __init__(
        self,
        engine: ManifoldEngine | None = None,
        mirror_threshold: float = 0.55,
        window: int = 128,
    ):
        self.engine = engine or ManifoldEngine()
        self.mirror_threshold = mirror_threshold
        self.window = window
        self._records: deque[tuple[str, str, bool]] = deque(maxlen=window)
        self._lock = threading.Lock()
        self._degradation_score = 0.0
        self._running = False
        self._thread: threading.Thread | None = None
        self._async_task: asyncio.Task[None] | None = None

    @property
    def degradation_score(self) -> float:
        with self._lock:
            return self._degradation_score

    def record_tick(
        self,
        symbol: str,
        prices: np.ndarray,
        forward_signal: str,
        entropy_baseline: float,
    ) -> bool:
        """
        Compare forward signal to signal on reflected (inverse) price path.
        Returns True if signals mirror (degradation event).
        """
        if prices.size < 3 or forward_signal == "HOLD":
            return False

        reflected = self._reflect_prices(prices)
        vec = prices.astype(np.float64)
        ref_vec = reflected.astype(np.float64)

        fwd_curv = self.engine.calculate_curvature(vec)
        inv_curv = self.engine.calculate_curvature(ref_vec)
        fwd_ent = self.engine.differential_entropy(vec)
        inv_ent = self.engine.differential_entropy(ref_vec)

        inv_signal = self.engine.generate_signal(
            inv_curv, entropy=inv_ent, entropy_baseline=entropy_baseline
        )
        mirrored = inv_signal == forward_signal and forward_signal != "HOLD"

        with self._lock:
            self._records.append((symbol, forward_signal, mirrored))
            self._recompute_locked()

        return mirrored

    def _reflect_prices(self, prices: np.ndarray) -> np.ndarray:
        """Inverse manifold path: reflect prices around the window midpoint."""
        p = prices.astype(np.float64)
        anchor = (p[0] + p[-1]) / 2.0
        return 2.0 * anchor - p

    def _recompute_locked(self) -> None:
        if not self._records:
            self._degradation_score = 0.0
            return
        mirrors = sum(1 for _, _, m in self._records if m)
        self._degradation_score = mirrors / len(self._records)

    def snapshot(self) -> AuditSnapshot:
        with self._lock:
            samples = len(self._records)
            score = self._degradation_score
            mirror_rate = score
        return AuditSnapshot(
            degradation_score=score,
            mirror_rate=mirror_rate,
            samples=samples,
            healthy=score < self.mirror_threshold,
        )

    def alpha_healthy(self) -> bool:
        return self.snapshot().healthy

    def _audit_loop_sync(self, interval: float) -> None:
        while self._running:
            with self._lock:
                self._recompute_locked()
            time.sleep(interval)

    async def _audit_loop_async(self, interval: float) -> None:
        while self._running:
            with self._lock:
                self._recompute_locked()
            await asyncio.sleep(interval)

    def start_background(self, interval: float = 1.0, *, use_thread: bool = True) -> None:
        if self._running:
            return
        self._running = True
        if use_thread:
            self._thread = threading.Thread(
                target=self._audit_loop_sync,
                args=(interval,),
                daemon=True,
                name="shadow-tensor-audit",
            )
            self._thread.start()
        else:
            self._async_task = asyncio.create_task(self._audit_loop_async(interval))

    def stop(self) -> None:
        self._running = False
        if self._thread is not None:
            self._thread.join(timeout=2.0)
            self._thread = None
        if self._async_task is not None:
            self._async_task.cancel()
            self._async_task = None
