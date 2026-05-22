"""Omega Point closed-loop integration tests."""
from __future__ import annotations

import asyncio

import pytest

from omega_point import OmegaPoint


@pytest.mark.asyncio
async def test_omega_replay_produces_events():
    omega = OmegaPoint(capital=100_000)
    ticks = [{"symbol": "SPY", "price": 450.0 + i * 0.05, "volume": 3000} for i in range(25)]
    events = await omega.run_replay(ticks)
    omega.shutdown()
    assert len(events) >= 1
    assert events[-1].symbol == "SPY"
