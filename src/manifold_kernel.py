"""
CORE ARCHITECTURE: UtahIsMyQuant Manifold Engine
Logic: Market state as a surface curvature + adelic sieve resonance.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import gaussian_kde

from .adelic_sieve import AdelicSieveKernel


class ManifoldEngine:
    def __init__(
        self,
        sensitivity: float = 0.05,
        entropy_window: int = 32,
        adelic: AdelicSieveKernel | None = None,
    ):
        self.sensitivity = sensitivity
        self.entropy_window = max(entropy_window, 8)
        self.adelic = adelic or AdelicSieveKernel()

    def adelic_resonance(
        self,
        price_vector: np.ndarray,
        volume_vector: np.ndarray | None = None,
    ) -> float:
        """Cross-prime adelic resonance strength."""
        return self.adelic.adelic_cross_power(price_vector, volume_vector)

    def detect_adelic_void(
        self,
        price_vector: np.ndarray,
        volume_vector: np.ndarray | None = None,
    ) -> bool:
        """Liquidity vacuum detection via adelic interference collapse."""
        return self.adelic.detect_adelic_void(price_vector, volume_vector)

    def calculate_curvature(self, price_vector: np.ndarray) -> float:
        """
        Calculates the local curvature of the price-action manifold.
        High curvature = High probability of regime shift.
        """
        if price_vector.size < 3:
            return 0.0
        q = self.adaptive_quantize(price_vector)
        delta = np.diff(q, n=2)
        return float(np.mean(np.abs(delta)))

    def manifold_drift(self, price_vector: np.ndarray) -> float:
        """
        Look-ahead manifold drift: acceleration of price (third difference).
        Detects the rate of curvature change, not price level alone.
        """
        if price_vector.size < 4:
            return 0.0
        q = self.adaptive_quantize(price_vector)
        jerk = np.diff(q, n=3)
        return float(np.mean(jerk))

    def adaptive_quantize(self, price_vector: np.ndarray) -> np.ndarray:
        """
        Adaptive quantization: precision scales inversely with volatility.
        Narrow spreads -> float64; high-vol spikes -> float32 to save cycles.
        """
        p = price_vector.astype(np.float64)
        if p.size < 2:
            return p
        vol = float(np.std(np.diff(np.log(np.maximum(p, 1e-12)))))
        dtype = np.float64 if vol < 0.002 else np.float32
        return p.astype(dtype)

    def adaptive_dtype(self, price_vector: np.ndarray) -> type[np.floating]:
        q = self.adaptive_quantize(price_vector)
        return type(q.dtype.type())

    def differential_entropy(self, price_vector: np.ndarray) -> float:
        """
        Estimates differential entropy of recent returns — market "surprise."
        Local minima in surprise often precede directional moves.
        """
        if price_vector.size < 3:
            return 0.0
        q = self.adaptive_quantize(price_vector)
        returns = np.diff(np.log(np.maximum(q.astype(np.float64), 1e-12)))
        window = returns[-self.entropy_window :]
        if window.size < 4 or np.std(window) < 1e-12:
            return 0.0
        kde = gaussian_kde(window)
        samples = kde.resample(len(window) * 4)[0]
        density = np.maximum(kde(samples), 1e-12)
        return float(-np.mean(np.log(density)))

    def surprise_gradient(self, price_vector: np.ndarray) -> float:
        """Rate of change in surprise; negative = surprise compressing."""
        if price_vector.size < self.entropy_window + 4:
            return 0.0
        mid = price_vector.size // 2
        h0 = self.differential_entropy(price_vector[:mid])
        h1 = self.differential_entropy(price_vector[mid:])
        return h1 - h0

    def generate_signal(
        self,
        curvature: float,
        entropy: float | None = None,
        entropy_baseline: float | None = None,
        drift: float | None = None,
        drift_sensitivity: float = 0.001,
        adelic_void: bool = False,
        adelic_resonance: float | None = None,
        resonance_threshold: float = 1.0,
    ) -> str:
        """Determines position based on curvature, surprise, acceleration, and adelic state."""
        if adelic_void:
            return "ADELIC_VOID"
        if adelic_resonance is not None and adelic_resonance > resonance_threshold:
            return "ADELIC_RESONANCE"
        if curvature > self.sensitivity:
            return "REVERSAL_IMMINENT"
        if drift is not None and abs(drift) > drift_sensitivity:
            if drift > 0:
                return "DRIFT_ACCELERATING"
            return "DRIFT_DECELERATING"
        if entropy is not None and entropy_baseline is not None:
            if entropy < entropy_baseline * 0.85:
                return "BREAKOUT_PRIMED"
        return "HOLD"
