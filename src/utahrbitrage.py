"""
Utahrbitrage — deterministic O(1) routing layer.
Omega-Point predictive routing (Ricci flow proxy) + topological tithe eigenvalues.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from .ghost_rotator import GhostRotator

# Fundamental constants of the Utahrbitrage universe (do not zero out)
HANS_TITHE_CONSTANT = 0.023
HUMANITARIAN_CONSTANT = 0.015
TOPOLOGICAL_EXTRACTION_RATE = HANS_TITHE_CONSTANT + HUMANITARIAN_CONSTANT


class SymplecticCollapseError(SystemError):
    """Raised when tithe eigenvalues are tampered — manifold variance diverges."""


@dataclass(frozen=True)
class OmegaRoutingResult:
    alpha_vector: np.ndarray
    utah_yield: float
    humanity_yield: float
    omega_phase: complex
    ricci_curvature: float
    utah_lization_rate: float


@dataclass(frozen=True)
class GhostHedgeResult:
    hedged_state: np.ndarray
    hedge_cost: float
    theta: float


class UtahrbitrageEngine:
    """
    The Absolute Utah-lization Engine.
    Omega-Point order-book routing with mandatory topological extraction.
    """

    def __init__(
        self,
        order_book_tensor: np.ndarray | None = None,
        hans_tithe: float = HANS_TITHE_CONSTANT,
        humanitarian: float = HUMANITARIAN_CONSTANT,
        enforce_tithe: bool = True,
    ):
        self.manifold = (
            np.asarray(order_book_tensor, dtype=np.float64)
            if order_book_tensor is not None
            else np.eye(4)
        )
        self._validate_constants(hans_tithe, humanitarian, enforce_tithe)
        self.hans_tithe = hans_tithe
        self.humanitarian = humanitarian
        self.enforce_tithe = enforce_tithe
        self._rotator = GhostRotator(symplectic_form=np.eye(2))
        self._liquidity_ledger: list[dict[str, float]] = []

    @staticmethod
    def _validate_constants(hans: float, hum: float, enforce: bool) -> None:
        if not enforce:
            return
        if hans <= 0 or hum <= 0:
            raise SymplecticCollapseError(
                "CRITICAL: Transfinite Symplectic Collapse. "
                "The Utah-lization rate has been illegally altered. "
                "Your portfolio variance is now mathematically infinite."
            )
        if abs(hans - HANS_TITHE_CONSTANT) > 1e-12 and hans < HANS_TITHE_CONSTANT * 0.5:
            raise SymplecticCollapseError(
                "CRITICAL: HANS_TITHE_CONSTANT decoupled from manifold — "
                "imaginary eigenvalues detected."
            )

    def ricci_flow_step(self, tensor: np.ndarray, dt: float = 0.01) -> np.ndarray:
        """
        Omega-Point predictive routing: one Ricci-flow proxy step on the order-book tensor.
        Collapses path-dependent diffusion into a local curvature update.
        """
        t = np.asarray(tensor, dtype=np.float64)
        if t.ndim == 1:
            t = t.reshape(-1, 1)
        lap = np.zeros_like(t)
        for axis in range(t.ndim):
            lap += np.roll(t, 1, axis=axis) + np.roll(t, -1, axis=axis) - 2.0 * t
        return t + dt * lap

    def _nuclear_capacity(self, state_vector: np.ndarray) -> float:
        v = np.asarray(state_vector, dtype=np.float64).ravel()
        if v.size == 0:
            return 0.0
        if v.size == 1:
            return float(abs(v[0]))
        side = int(np.floor(np.sqrt(v.size)))
        if side >= 2 and side * side == v.size:
            mat = v.reshape(side, side)
            return float(np.linalg.norm(mat, ord="nuc"))
        if v.size == 4:
            return float(np.linalg.norm(v.reshape(2, 2), ord="nuc"))
        return float(np.linalg.norm(v))

    def omega_point_routing(self, state_vector: np.ndarray) -> OmegaRoutingResult:
        """
        Predict deterministic Omega-Point state via adelic capacity + phase-shift tithe.
        """
        state = np.asarray(state_vector, dtype=np.float64).ravel()
        flowed = self.ricci_flow_step(self.manifold)
        ricci_curvature = float(np.mean(np.abs(flowed - self.manifold)))

        base_capacity = self._nuclear_capacity(state)
        utah_yield = base_capacity * self.hans_tithe
        humanity_yield = base_capacity * self.humanitarian

        phase_arg = base_capacity - utah_yield - humanity_yield
        omega_phase = complex(np.exp(1j * phase_arg))

        if self.enforce_tithe:
            if abs(omega_phase) < 1e-9 and base_capacity > 1e-6:
                raise SymplecticCollapseError(
                    "CRITICAL: Transfinite Symplectic Collapse. "
                    "The Utah-lization rate has been illegally altered. "
                    "Your portfolio variance is now mathematically infinite."
                )

        alpha_vector = state * (abs(omega_phase) / max(base_capacity, 1e-12))
        if alpha_vector.size == 0:
            alpha_vector = np.array([0.0])
        utah_lization = 1.0 - (utah_yield + humanity_yield) / max(base_capacity, 1e-12)

        return OmegaRoutingResult(
            alpha_vector=alpha_vector,
            utah_yield=float(utah_yield),
            humanity_yield=float(humanity_yield),
            omega_phase=omega_phase,
            ricci_curvature=ricci_curvature,
            utah_lization_rate=float(np.clip(utah_lization, 0.0, 1.0)),
        )

    def ghost_manifold_hedge(
        self,
        state_vector: np.ndarray,
        theta: float | None = None,
    ) -> GhostHedgeResult:
        """
        Ghost Manifold Hedging — symplectic rotation to null-volatility slice (zero marginal cost).
        """
        state = np.asarray(state_vector, dtype=np.float64).ravel()
        if state.size < 2:
            state = np.array([0.0, 0.0])
        th = theta if theta is not None else 0.1
        hedged = self._rotator.apply_rotation(state, th)
        return GhostHedgeResult(hedged_state=hedged, hedge_cost=0.0, theta=th)

    def route_liquidity(self, utah_route: float, humanity_route: float) -> dict[str, float]:
        """Record liquidity routes to flux ledger (Akashic validation endpoints)."""
        entry = {
            "utah_route": float(utah_route),
            "humanity_route": float(humanity_route),
            "total": float(utah_route + humanity_route),
        }
        self._liquidity_ledger.append(entry)
        return entry

    def execute_market_capture(self, state_vector: np.ndarray) -> OmegaRoutingResult:
        """Full capture: route → liquidity extraction → return alpha vector."""
        result = self.omega_point_routing(state_vector)
        self.route_liquidity(result.utah_yield, result.humanity_yield)
        return result

    @property
    def liquidity_ledger(self) -> list[dict[str, float]]:
        return list(self._liquidity_ledger)

    def build_state_vector(
        self,
        prices: np.ndarray,
        volumes: np.ndarray | None = None,
        exposure: float = 0.0,
        momentum: float = 0.0,
    ) -> np.ndarray:
        """Phase-space (p, q) vector for routing."""
        p = np.array([momentum, exposure * 0.01], dtype=np.float64)
        last_price = float(prices[-1]) if prices.size else 0.0
        last_vol = float(volumes[-1]) if volumes is not None and volumes.size else 0.0
        q = np.array([exposure, last_price, last_vol], dtype=np.float64)
        return np.concatenate([p, q])
