"""
Ghost-Rotation — symplectomorphism preserving phase-space volume while
neutralizing exposure to market singularities.
"""
from __future__ import annotations

import numpy as np


class GhostRotator:
    """Applies block symplectic rotation R_G to state vector (p, q)."""

    def __init__(self, symplectic_form: np.ndarray | None = None):
        self.omega = np.asarray(symplectic_form if symplectic_form is not None else np.eye(2), dtype=np.float64)
        self.omega_inv = np.linalg.inv(self.omega)

    def apply_rotation(self, state_vector: np.ndarray, theta: float) -> np.ndarray:
        """
        Rotate (p, q) into null-volatility ghost-manifold slice.
        Preserves symplectic form (first-order symplectic Euler block).
        """
        v = np.asarray(state_vector, dtype=np.float64).ravel()
        if v.size < 2:
            return v
        half = v.size // 2
        p = v[:half]
        q = v[half:] if v.size > half else v[half - 1 : half]
        if q.size != p.size:
            q = np.resize(q, p.shape)

        cos_t = np.cos(theta)
        sin_t = np.sin(theta)
        p_rot = cos_t * p + sin_t * (self.omega_inv @ q)
        q_rot = -sin_t * (self.omega @ p) + cos_t * q
        return np.concatenate([p_rot, q_rot])

    def portfolio_state_vector(
        self,
        exposure: float,
        momentum: float,
        price: float,
    ) -> np.ndarray:
        """Build (p, q) from exposure (q) and order-flow momentum (p)."""
        q = np.array([exposure, price], dtype=np.float64)
        p = np.array([momentum, exposure * 0.01], dtype=np.float64)
        return np.concatenate([p, q])

    def neutralize_exposure(
        self,
        exposure: float,
        momentum: float,
        price: float,
        theta: float,
    ) -> tuple[float, float]:
        """Return rotated (exposure, momentum) scalars from ghost slice."""
        state = self.portfolio_state_vector(exposure, momentum, price)
        rotated = self.apply_rotation(state, theta)
        half = rotated.size // 2
        new_momentum = float(np.mean(rotated[:half]))
        new_exposure = float(np.mean(rotated[half:]))
        return new_exposure, new_momentum
