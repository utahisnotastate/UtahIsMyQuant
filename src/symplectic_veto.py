"""
Symplectic Veto-Matrix — Hamiltonian capacity supervisor (Gromov-width proxy).
Unifies structural risk with shadow-tensor alpha health.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .shadow_tensor import ShadowTensorAudit


@dataclass(frozen=True)
class SymplecticVerdict:
    veto: bool
    force_ghost_rotation: bool
    symplectic_capacity: float
    adelic_capacity: float
    shadow_healthy: bool
    reason: str = ""


class SymplecticVetoMatrix:
    """
    Replaces VaR-style thinking with symplectic capacity + adelic capacity bounds.
    Merged audit path: shadow tensor + stress-energy eigenvalues.
    """

    def __init__(
        self,
        capacity_threshold: float = 0.85,
        adelic_capacity_max: float = 2.5,
        audit: ShadowTensorAudit | None = None,
    ):
        self.capacity_threshold = capacity_threshold
        self.adelic_capacity_max = adelic_capacity_max
        self.audit = audit or ShadowTensorAudit()

    def build_stress_tensor(self, prices: np.ndarray, volumes: np.ndarray | None = None) -> np.ndarray:
        """2x2 stress-energy tensor from returns and optional volume stress."""
        p = np.asarray(prices, dtype=np.float64).ravel()
        if p.size < 2:
            return np.eye(2)
        rets = np.diff(np.log(np.maximum(p, 1e-12)))
        vol_stress = 0.0
        if volumes is not None and volumes.size >= 2:
            v = np.asarray(volumes, dtype=np.float64).ravel()[-len(rets) :]
            vol_stress = float(np.std(v)) if v.size else 0.0
        var_r = float(np.var(rets)) if rets.size else 1e-8
        cov = float(np.cov(rets, np.arange(rets.size))[-1, 0]) if rets.size > 1 else 0.0
        return np.array(
            [[var_r, cov], [cov, var_r + vol_stress]],
            dtype=np.float64,
        )

    def calculate_symplectic_capacity(self, stress_tensor: np.ndarray) -> float:
        """Gromov-width proxy: minimum |eigenvalue| of stress tensor."""
        eigenvalues = np.linalg.eigvals(stress_tensor)
        return float(np.min(np.abs(eigenvalues)))

    def calculate_adelic_capacity(self, adelic_resonance: float) -> float:
        """Adelic capacity — scaled resonance energy in sieve space."""
        return float(abs(adelic_resonance))

    def veto_check(self, stress_tensor: np.ndarray) -> bool:
        """Hard-reset trigger when symplectic capacity exceeds threshold."""
        return self.calculate_symplectic_capacity(stress_tensor) > self.capacity_threshold

    def evaluate(
        self,
        prices: np.ndarray,
        volumes: np.ndarray | None,
        signal: str,
        entropy_baseline: float,
        adelic_resonance: float,
    ) -> SymplecticVerdict:
        stress = self.build_stress_tensor(prices, volumes)
        sym_cap = self.calculate_symplectic_capacity(stress)
        adelic_cap = self.calculate_adelic_capacity(adelic_resonance)

        vec = np.asarray(prices, dtype=np.float64)
        self.audit.record_tick("SYM", vec, signal, entropy_baseline)
        shadow_ok = self.audit.alpha_healthy()

        squeeze = sym_cap > self.capacity_threshold
        adelic_collapse = adelic_cap > self.adelic_capacity_max
        force_ghost = squeeze or adelic_collapse

        if not shadow_ok:
            return SymplecticVerdict(
                veto=True,
                force_ghost_rotation=True,
                symplectic_capacity=sym_cap,
                adelic_capacity=adelic_cap,
                shadow_healthy=False,
                reason="Shadow tensor mirror — symplectic veto.",
            )
        if force_ghost:
            return SymplecticVerdict(
                veto=True,
                force_ghost_rotation=True,
                symplectic_capacity=sym_cap,
                adelic_capacity=adelic_cap,
                shadow_healthy=shadow_ok,
                reason="Symplectic squeeze or adelic collapse — ghost rotation required.",
            )
        return SymplecticVerdict(
            veto=False,
            force_ghost_rotation=False,
            symplectic_capacity=sym_cap,
            adelic_capacity=adelic_cap,
            shadow_healthy=shadow_ok,
        )
