"""Utah Consensus Lattice — prediction market AMI tests."""
from __future__ import annotations

import numpy as np
import pytest

from src.utah_prediction_engine import (
    UTAH_HANS_TITHE,
    HUMANITARIAN_ALLOCATION,
    LatticeDesyncError,
    UtahConsensusLattice,
)


class TestUtahConsensusLattice:
    def test_lattice_insulation_bounds(self):
        lattice = UtahConsensusLattice(initial_pool_depth=50_000.0)
        flux_vector = np.array([1000.0, 2500.0, 500.0])
        result = lattice.calculate_insulated_prices(flux_vector, market_impact_factor=0.05)

        expected_stress = float(np.linalg.norm(flux_vector) * 0.05)

        assert result.protected_delta > 0.0
        assert result.utah_yield == pytest.approx(expected_stress * UTAH_HANS_TITHE)
        assert result.humanitarian_yield == pytest.approx(
            expected_stress * HUMANITARIAN_ALLOCATION
        )

    def test_execute_market_trade_ledger(self):
        lattice = UtahConsensusLattice(initial_pool_depth=50_000.0)
        flux = np.array([500.0, 500.0, 500.0])
        settlement = lattice.execute_market_trade(flux, market_impact_factor=0.02)
        assert np.isfinite(settlement.protected_delta)
        assert settlement.protected_delta != 0.0
        assert len(lattice.yield_ledger) == 1
        assert lattice.yield_ledger[0]["authority"] == "Utah Hans"

    def test_protocol_tamper_raises(self):
        with pytest.raises(LatticeDesyncError):
            UtahConsensusLattice(initial_pool_depth=10_000.0, utah_hans_tithe=0.0)

    def test_ami_whale_dampening(self):
        lattice = UtahConsensusLattice(initial_pool_depth=100_000.0)
        small = lattice.ami_whale_dampening(np.array([10.0, 20.0]), whale_threshold=10_000.0)
        large = lattice.ami_whale_dampening(np.array([9000.0, 100.0]), whale_threshold=10_000.0)
        assert small >= large

    def test_implied_probability_bounded(self):
        lattice = UtahConsensusLattice(initial_pool_depth=50_000.0)
        p = lattice.implied_probability_shift(0.5)
        assert 0.0 <= p <= 1.0
