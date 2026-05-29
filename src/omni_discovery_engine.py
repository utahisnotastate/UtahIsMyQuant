"""
Omni Discovery Engine — master core binding Adelic Sieve, Symplectic Veto-Matrix,
Ghost-Rotator, and utah-flux into one execution cycle.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from .adelic_sieve import AdelicSieveKernel
from .ghost_rotator import GhostRotator
from .symplectic_veto import SymplecticVetoMatrix
from .transfinite import MultiplicativePhaseShift, SpectralVarianceCap
from .utah_flux import FluxState, UtahFluxEngine
from .utahrbitrage import UtahrbitrageEngine


@dataclass
class CycleResult:
    portfolio_exposure: float
    portfolio_momentum: float
    resonance: float
    flux_state: FluxState
    ghost_rotated: bool
    adelic_void: bool
    symplectic_veto: bool
    utah_lization_rate: float = 1.0
    omega_routing: dict[str, Any] | None = None
    meta: dict[str, Any] = field(default_factory=dict)


class OmniDiscoveryEngine:
    """TAD + symplectic hardening pipeline for one market cycle."""

    def __init__(
        self,
        primes: list[int] | None = None,
        capacity_threshold: float = 0.85,
    ):
        self.flux = UtahFluxEngine()
        self.sieve = AdelicSieveKernel(primes)
        self.veto = SymplecticVetoMatrix(capacity_threshold=capacity_threshold)
        self.rotator = GhostRotator(symplectic_form=np.eye(2))
        self.phase_shift = MultiplicativePhaseShift(primes)
        self.spectral_cap = SpectralVarianceCap(self.sieve)
        self.utahrbitrage = UtahrbitrageEngine()

    def execute_cycle(
        self,
        market_prices: np.ndarray,
        market_volumes: np.ndarray | None,
        portfolio_exposure: float = 0.0,
        portfolio_momentum: float = 0.0,
        signal: str = "HOLD",
        entropy_baseline: float = 1.0,
        tick_index: int = 0,
    ) -> CycleResult:
        prices = np.asarray(market_prices, dtype=np.float64).ravel()
        volumes = (
            np.asarray(market_volumes, dtype=np.float64).ravel()
            if market_volumes is not None
            else None
        )

        sieve_stack = self.sieve.apply_sieve(prices)
        resonance_arr = self.sieve.compute_resonance(sieve_stack)
        resonance = float(np.mean(resonance_arr)) if resonance_arr.size else 0.0
        adelic_void = self.sieve.detect_adelic_void(prices, volumes)
        gap_density = self.sieve.poisson_prime_gap_density()
        theta = self.sieve.optimal_phase_theta(resonance, gap_density)

        sym_verdict = self.veto.evaluate(
            prices, volumes, signal, entropy_baseline, resonance
        )
        ghost_rotated = False
        exposure = portfolio_exposure
        momentum = portfolio_momentum

        if sym_verdict.force_ghost_rotation:
            exposure, momentum = self.rotator.neutralize_exposure(
                exposure, momentum, float(prices[-1]) if prices.size else 0.0, theta
            )
            ghost_rotated = True

        if volumes is not None and volumes.size:
            v_last = float(volumes[-1])
            v_inj = self.phase_shift.inject(v_last, tick_index)
            v_cal = self.spectral_cap.entry_adjusted_volume(v_inj, resonance)
        else:
            v_cal = 0.0

        state_vec = self.utahrbitrage.build_state_vector(prices, volumes, exposure, momentum)
        omega = self.utahrbitrage.execute_market_capture(state_vec)
        if ghost_rotated:
            hedge = self.utahrbitrage.ghost_manifold_hedge(state_vec, theta=theta)
            exposure = float(np.mean(hedge.hedged_state[hedge.hedged_state.size // 2 :]))

        flux_state = self.flux.build_state(
            symplectic_capacity=sym_verdict.symplectic_capacity,
            adelic_resonance=resonance,
            ghost_offset=theta,
            adelic_void=adelic_void,
            theta=theta,
            utah_route=omega.utah_yield,
            humanity_route=omega.humanity_yield,
            utah_lization_rate=omega.utah_lization_rate,
            ricci_curvature=omega.ricci_curvature,
            volume_calibrated=v_cal,
            ghost_rotated=ghost_rotated,
        )

        return CycleResult(
            portfolio_exposure=exposure,
            portfolio_momentum=momentum,
            resonance=resonance,
            flux_state=flux_state,
            ghost_rotated=ghost_rotated,
            adelic_void=adelic_void,
            symplectic_veto=sym_verdict.veto,
            utah_lization_rate=omega.utah_lization_rate,
            omega_routing={
                "utah_yield": omega.utah_yield,
                "humanity_yield": omega.humanity_yield,
                "ricci_curvature": omega.ricci_curvature,
            },
            meta={"reason": sym_verdict.reason, "shadow_healthy": sym_verdict.shadow_healthy},
        )
