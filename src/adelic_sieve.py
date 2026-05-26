"""
Adelic Sieve Frequency Engine — non-Archimedean multi-scale resonance detection.
Maps price/volume series across prime-power valuations to find structural interference.
"""
from __future__ import annotations

import numpy as np

DEFAULT_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)


class AdelicSieveKernel:
    """Projects market data into local p-adic components and computes cross-scale resonance."""

    def __init__(self, primes: list[int] | tuple[int, ...] | None = None):
        self.primes = np.array(primes or DEFAULT_PRIMES, dtype=np.int64)

    def apply_sieve(self, market_data: np.ndarray) -> np.ndarray:
        """
        Stack of p-adic valuations per prime.
        Shape: (n_primes, n_samples) aligned to input length.
        """
        data = np.asarray(market_data, dtype=np.float64).ravel()
        if data.size == 0:
            return np.zeros((len(self.primes), 0))
        safe = np.maximum(np.abs(data), 1e-12)
        log_safe = np.log(safe)
        out = np.zeros((len(self.primes), data.size), dtype=np.float64)
        for i, p in enumerate(self.primes):
            out[i] = log_safe / np.log(float(p))
        return out

    def compute_resonance(self, sieve_stack: np.ndarray) -> np.ndarray:
        """Adelic cross-power spectral density — mean across prime scales."""
        if sieve_stack.size == 0:
            return np.array([], dtype=np.float64)
        return np.mean(sieve_stack, axis=0)

    def adelic_cross_power(self, prices: np.ndarray, volumes: np.ndarray | None = None) -> float:
        """Scalar resonance strength for gate / flux synchronization."""
        price_sieve = self.apply_sieve(prices)
        res = self.compute_resonance(price_sieve)
        if volumes is not None and volumes.size == prices.size:
            vol_sieve = self.apply_sieve(volumes)
            vol_res = self.compute_resonance(vol_sieve)
            combined = 0.6 * res + 0.4 * vol_res
            return float(np.std(combined)) if combined.size else 0.0
        return float(np.std(res)) if res.size else 0.0

    def detect_adelic_void(
        self,
        prices: np.ndarray,
        volumes: np.ndarray | None = None,
        void_threshold: float = 0.15,
    ) -> bool:
        """
        Adelic void — liquidity vacuum where institutional interference collapses.
        Low cross-scale variance after sieve → void (pre-move liquidity dry-up).
        """
        resonance = self.adelic_cross_power(prices, volumes)
        return resonance < void_threshold

    def poisson_prime_gap_density(self, n_gaps: int = 32) -> float:
        """
        Spectral variance cap proxy: dispersion of first n_gaps prime gaps.
        Used for zero-point drift calibration (surveillance-noise matching).
        """
        if len(self.primes) < 2:
            return 0.0
        gaps = np.diff(self.primes.astype(np.float64))
        use = gaps[: min(n_gaps, gaps.size)]
        return float(np.var(use)) if use.size else 0.0

    def optimal_phase_theta(self, resonance: float, gap_density: float) -> float:
        """Phase-shift angle for Ghost-Rotation from adelic + spectral state."""
        return float(np.arctan(resonance * (1.0 + gap_density)) * 0.1)
