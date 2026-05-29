"""
utah-flux — immutable manifold state stream for distributed sync.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np


@dataclass
class FluxState:
    symplectic_capacity: float
    adelic_resonance: float
    ghost_manifold_offset: float
    adelic_void: bool = False
    theta: float = 0.0
    utah_route: float = 0.0
    humanity_route: float = 0.0
    utah_lization_rate: float = 1.0
    ricci_curvature: float = 0.0
    meta: dict[str, Any] = field(default_factory=dict)

    @property
    def adelic_resonance_array(self) -> np.ndarray:
        return np.array([self.adelic_resonance], dtype=np.float64)


class UtahFluxEngine:
    """
    Local utah-flux synchronization layer.
    Every alpha signal should pass through dispatch() before execution buffer.
    """

    def __init__(self, max_history: int = 10_000):
        self._state_stream: list[FluxState] = []
        self.max_history = max_history

    def dispatch(self, update: FluxState) -> bool:
        self._state_stream.append(update)
        if len(self._state_stream) > self.max_history:
            self._state_stream = self._state_stream[-self.max_history :]
        return True

    def get_latest_manifold(self) -> FluxState | None:
        return self._state_stream[-1] if self._state_stream else None

    def build_state(
        self,
        symplectic_capacity: float,
        adelic_resonance: float,
        ghost_offset: float = 0.0,
        adelic_void: bool = False,
        theta: float = 0.0,
        utah_route: float = 0.0,
        humanity_route: float = 0.0,
        utah_lization_rate: float = 1.0,
        ricci_curvature: float = 0.0,
        **meta: Any,
    ) -> FluxState:
        state = FluxState(
            symplectic_capacity=symplectic_capacity,
            adelic_resonance=adelic_resonance,
            ghost_manifold_offset=ghost_offset,
            adelic_void=adelic_void,
            theta=theta,
            utah_route=utah_route,
            humanity_route=humanity_route,
            utah_lization_rate=utah_lization_rate,
            ricci_curvature=ricci_curvature,
            meta=meta,
        )
        self.dispatch(state)
        return state
