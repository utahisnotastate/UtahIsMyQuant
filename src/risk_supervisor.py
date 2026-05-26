"""
CORE ARCHITECTURE: RISK_MANAGEMENT_SUPERVISOR
Physics: Entropic Thresholding (Fourth Law boundary)
Purpose: Protect account equity via real-time position monitoring
and emergency circuit-breaking.
"""
from __future__ import annotations

import logging
import threading
import time
from dataclasses import dataclass
from typing import Any

import numpy as np

from .symplectic_veto import SymplecticVetoMatrix

logger = logging.getLogger(__name__)


@dataclass
class Position:
    symbol: str
    entry_price: float
    value: float
    quantity: float = 1.0
    side: str = "long"

    def to_dict(self) -> dict[str, Any]:
        return {
            "symbol": self.symbol,
            "entry_price": self.entry_price,
            "value": self.value,
            "quantity": self.quantity,
            "side": self.side,
        }


@dataclass(frozen=True)
class SupervisorVerdict:
    """Fourth Law boundary: bug and fix are the same halt state at execution."""

    allow_execution: bool
    force_stop: bool
    reason: str = ""
    circuit_breaker: bool = False
    force_ghost_rotation: bool = False
    symplectic_capacity: float = 0.0
    adelic_capacity: float = 0.0


class RiskSupervisor:
    """
    Bodyguard protocol: monitors exposure, per-position drawdown, and system latency.
    Runs optionally on a background thread; vetoes AlphaGenerator when unsafe.
    """

    def __init__(
        self,
        max_drawdown: float = 0.05,
        max_position_size: float = 0.10,
        max_latency_ms: float = 200.0,
        max_account_drawdown: float = 0.05,
        monitor_interval: float = 0.25,
        symplectic: SymplecticVetoMatrix | None = None,
        enable_symplectic: bool = True,
    ):
        self.symplectic = symplectic or SymplecticVetoMatrix()
        self.enable_symplectic = enable_symplectic
        self.max_drawdown = max_drawdown
        self.max_position_size = max_position_size
        self.max_latency_ms = max_latency_ms
        self.max_account_drawdown = max_account_drawdown
        self.monitor_interval = monitor_interval
        self.circuit_breaker_active = False
        self._active_positions: list[dict[str, Any]] = []
        self._account_equity = 100_000.0
        self._peak_equity = 100_000.0
        self._last_latency_ms = 0.0
        self._halt_new_entries = False
        self._lock = threading.Lock()
        self._running = False
        self._thread: threading.Thread | None = None

    @property
    def account_equity(self) -> float:
        with self._lock:
            return self._account_equity

    @property
    def halt_new_entries(self) -> bool:
        with self._lock:
            return self._halt_new_entries or self.circuit_breaker_active

    def set_account_equity(self, equity: float) -> None:
        with self._lock:
            self._account_equity = equity
            self._peak_equity = max(self._peak_equity, equity)

    def update_positions(self, positions: list[dict[str, Any]] | list[Position]) -> None:
        with self._lock:
            self._active_positions = [
                p.to_dict() if isinstance(p, Position) else p for p in positions
            ]

    def update_latency(self, latency_ms: float) -> None:
        with self._lock:
            self._last_latency_ms = latency_ms

    @staticmethod
    def fourth_law_boundary(bug_detected: bool, fix_triggered: bool) -> bool:
        """
        Fourth Law: failing trade (bug) and stop-loss (fix) are identical at the boundary.
        Either state halts new execution.
        """
        return bug_detected or fix_triggered

    def monitor_exposure(self, account_equity: float, active_positions: list[dict[str, Any]]) -> bool:
        """Checks if total exposure exceeds risk limits."""
        if account_equity <= 0:
            return False
        total_exposure = sum(float(pos.get("value", 0)) for pos in active_positions)
        if (total_exposure / account_equity) > self.max_position_size:
            logger.warning("// RISK ALERT: TOTAL EXPOSURE LIMIT EXCEEDED.")
            return False
        return True

    def enforce_stop_loss(self, position: dict[str, Any], current_price: float) -> str:
        """Monitors individual position drawdown."""
        entry = float(position.get("entry_price", 0))
        if entry <= 0:
            return "HOLD"
        side = str(position.get("side", "long")).lower()
        if side == "short":
            drawdown = (current_price - entry) / entry
        else:
            drawdown = (entry - current_price) / entry
        if drawdown > self.max_drawdown:
            symbol = position.get("symbol", "?")
            logger.error("// EXECUTE EMERGENCY STOP LOSS: %s", symbol)
            return "SELL_IMMEDIATE"
        return "HOLD"

    def check_system_health(self, latency_ms: float) -> bool:
        """
        Circuit breaker: latency spike implies volatile plenum — halt until stable.
        """
        if latency_ms > self.max_latency_ms:
            self.circuit_breaker_active = True
            logger.critical("// CIRCUIT BREAKER TRIPPED: LATENCY HIGH.")
            return False
        self.circuit_breaker_active = False
        return True

    def account_drawdown(self) -> float:
        with self._lock:
            if self._peak_equity <= 0:
                return 0.0
            return max(0.0, (self._peak_equity - self._account_equity) / self._peak_equity)

    def entropic_volatility_threshold(self, returns_std: float, baseline: float = 0.002) -> bool:
        """Entropic threshold: True if market surprise exceeds calm baseline."""
        return returns_std > baseline * 3.0

    def evaluate_symplectic(
        self,
        prices: np.ndarray,
        volumes: np.ndarray | None,
        signal: str,
        entropy_baseline: float,
        adelic_resonance: float,
    ) -> SupervisorVerdict | None:
        """Symplectic Veto-Matrix pass (merged shadow audit)."""
        if not self.enable_symplectic:
            return None
        sv = self.symplectic.evaluate(
            np.asarray(prices, dtype=np.float64),
            volumes,
            signal,
            entropy_baseline,
            adelic_resonance,
        )
        if sv.veto:
            return SupervisorVerdict(
                allow_execution=False,
                force_stop=sv.force_ghost_rotation,
                force_ghost_rotation=sv.force_ghost_rotation,
                reason=sv.reason,
                symplectic_capacity=sv.symplectic_capacity,
                adelic_capacity=sv.adelic_capacity,
            )
        return None

    def evaluate_tick(
        self,
        symbol: str,
        current_price: float,
        account_equity: float,
        active_positions: list[dict[str, Any]],
        latency_ms: float,
        returns_std: float = 0.0,
        prices: np.ndarray | None = None,
        volumes: np.ndarray | None = None,
        signal: str = "HOLD",
        entropy_baseline: float = 1.0,
        adelic_resonance: float = 0.0,
    ) -> SupervisorVerdict:
        """
        Full supervisor pass for one tick. Called before alpha execution commits capital.
        """
        self.update_latency(latency_ms)
        self.set_account_equity(account_equity)
        self.update_positions(active_positions)

        if prices is not None:
            sym = self.evaluate_symplectic(
                prices, volumes, signal, entropy_baseline, adelic_resonance
            )
            if sym is not None:
                return sym

        if not self.check_system_health(latency_ms):
            self._halt_new_entries = True
            return SupervisorVerdict(
                allow_execution=False,
                force_stop=False,
                reason="Circuit breaker: latency exceeds plenum stability.",
                circuit_breaker=True,
            )

        if self.account_drawdown() > self.max_account_drawdown:
            self._halt_new_entries = True
            return SupervisorVerdict(
                allow_execution=False,
                force_stop=True,
                reason="Account drawdown exceeds Fourth Law boundary.",
            )

        if returns_std > 0 and self.entropic_volatility_threshold(returns_std):
            logger.warning("// RISK ALERT: Entropic volatility spike — halting new entries.")
            self._halt_new_entries = True
            return SupervisorVerdict(
                allow_execution=False,
                force_stop=False,
                reason="Entropic threshold exceeded — market acting crazy.",
            )

        if not self.monitor_exposure(account_equity, active_positions):
            return SupervisorVerdict(
                allow_execution=False,
                force_stop=False,
                reason="Total exposure limit exceeded.",
            )

        for pos in active_positions:
            if pos.get("symbol") == symbol:
                stop = self.enforce_stop_loss(pos, current_price)
                if stop == "SELL_IMMEDIATE":
                    bug = self.fourth_law_boundary(bug_detected=True, fix_triggered=True)
                    if bug:
                        self._halt_new_entries = True
                    return SupervisorVerdict(
                        allow_execution=False,
                        force_stop=True,
                        reason=f"Emergency stop loss: {symbol}",
                    )

        self._halt_new_entries = False
        return SupervisorVerdict(allow_execution=True, force_stop=False)

    def veto_decision(self, decision: dict[str, Any], verdict: SupervisorVerdict) -> dict[str, Any]:
        """Override alpha decision when supervisor blocks or forces exit."""
        if verdict.force_stop or verdict.force_ghost_rotation:
            tag = "GHOST_ROTATION" if verdict.force_ghost_rotation else "FORCE_STOP"
            return {
                **decision,
                "action": "EXECUTE_EXIT",
                "reason": verdict.reason,
                "supervisor": tag,
                "symplectic_capacity": verdict.symplectic_capacity,
                "gates_failed": list(decision.get("gates_failed", [])) + ["supervisor"],
            }
        if not verdict.allow_execution:
            execute_actions = {"EXECUTE_BUY", "EXECUTE_SELL"}
            if decision.get("action") in execute_actions:
                return {
                    **decision,
                    "action": "WAIT",
                    "reason": verdict.reason,
                    "supervisor": "VETO",
                    "gates_failed": list(decision.get("gates_failed", [])) + ["supervisor"],
                }
        return {**decision, "supervisor": "CLEAR"}

    def _monitor_loop(self) -> None:
        while self._running:
            with self._lock:
                equity = self._account_equity
                positions = list(self._active_positions)
                latency = self._last_latency_ms
            self.check_system_health(latency)
            self.monitor_exposure(equity, positions)
            if self.account_drawdown() > self.max_account_drawdown:
                self._halt_new_entries = True
            time.sleep(self.monitor_interval)

    def start_background(self) -> None:
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(
            target=self._monitor_loop,
            daemon=True,
            name="risk-supervisor",
        )
        self._thread.start()

    def stop(self) -> None:
        self._running = False
        if self._thread is not None:
            self._thread.join(timeout=2.0)
            self._thread = None

    def reset_circuit_breaker(self) -> None:
        self.circuit_breaker_active = False
        self._halt_new_entries = False
        logger.info("// CIRCUIT BREAKER RESET: Plenum stable.")
