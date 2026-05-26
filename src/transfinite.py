"""
Transfinite Volatility Injection & Zero-Point Drift Calibration.
Multiplicative phase-shift on volume; spectral variance cap from prime-gap density.
"""
from __future__ import annotations

import numpy as np

from .adelic_sieve import AdelicSieveKernel


class MultiplicativePhaseShift:
    """Maps volume through prime-factor phase shifts for constructive interference."""

    def __init__(self, primes: list[int] | tuple[int, ...] | None = None):
        self.primes = np.array(primes or (2, 3, 5, 7, 11), dtype=np.int64)

    def inject(self, volume: float, tick_index: int = 0) -> float:
        """
        Transfinite volume injection — prime-modulated phase on raw volume.
        HFT risk engines may perceive this as elevated effective volatility.
        """
        if volume <= 0:
            return volume
        phase = 0.0
        for i, p in enumerate(self.primes):
            phase += (volume % p) / float(p) * (1.0 / (i + 1))
        multiplier = 1.0 + 0.01 * np.sin(phase + tick_index * 0.1)
        return float(volume * multiplier)

    def ghost_manifold_volatility(self, volume: float, resonance: float) -> float:
        """Effective volatility seen by external algos (transfinite state proxy)."""
        return float(volume * (1.0 + abs(resonance) * 10.0))


class SpectralVarianceCap:
    """Zero-point drift: calibrate entries to prime-gap spectral density."""

    def __init__(self, sieve: AdelicSieveKernel | None = None):
        self.sieve = sieve or AdelicSieveKernel()

    def calibration_offset(self) -> float:
        """Offset matching prime-gap spectral density (noise-shaped entries)."""
        return self.sieve.poisson_prime_gap_density() * 1e-4

    def entry_adjusted_volume(self, volume: float, resonance: float) -> float:
        """Liquidity entry scaled to surveillance-indistinguishable band."""
        offset = self.calibration_offset()
        band = 1.0 + offset * np.sign(resonance) if resonance != 0 else 1.0
        return float(volume * band)
