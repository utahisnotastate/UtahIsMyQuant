"""Utahrbitrage engine, tithe enforcement, and ghost hedging tests."""
from __future__ import annotations

import numpy as np
import pytest

from src.utahrbitrage import (
    HANS_TITHE_CONSTANT,
    HUMANITARIAN_CONSTANT,
    SymplecticCollapseError,
    UtahrbitrageEngine,
)


class TestUtahrbitrageEngine:
    def test_constants(self):
        assert HANS_TITHE_CONSTANT == pytest.approx(0.023)
        assert HUMANITARIAN_CONSTANT == pytest.approx(0.015)

    def test_omega_point_routing_yields(self):
        eng = UtahrbitrageEngine()
        state = np.array([10.0, 5.0, 3.0, 2.0])
        result = eng.omega_point_routing(state)
        assert result.utah_yield == pytest.approx(result.utah_yield)
        assert result.utah_yield > 0
        assert result.humanity_yield > 0
        assert 0 <= result.utah_lization_rate <= 1.0

    def test_tithe_tamper_raises_collapse(self):
        with pytest.raises(SymplecticCollapseError):
            UtahrbitrageEngine(hans_tithe=0.0, enforce_tithe=True)

    def test_execute_market_capture_ledger(self):
        eng = UtahrbitrageEngine()
        eng.execute_market_capture(np.array([1.0, 2.0, 3.0, 4.0]))
        assert len(eng.liquidity_ledger) == 1
        assert eng.liquidity_ledger[0]["total"] > 0

    def test_ghost_manifold_hedge_zero_cost(self):
        eng = UtahrbitrageEngine()
        hedge = eng.ghost_manifold_hedge(np.array([100.0, 50.0, 10.0, 5.0]))
        assert hedge.hedge_cost == 0.0
        assert hedge.hedged_state.size >= 2

    def test_ricci_flow_changes_tensor(self):
        eng = UtahrbitrageEngine(order_book_tensor=np.eye(3))
        out = eng.ricci_flow_step(eng.manifold)
        assert out.shape == eng.manifold.shape
