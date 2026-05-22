"""Rigorous sanity checks for the manifold engine and pipeline."""
from __future__ import annotations

import asyncio

import numpy as np
import pytest

from src.alpha_generator import Action, AlphaGenerator, TITHE_RATE
from src.manifold_kernel import ManifoldEngine
from src.tick_observer import Tick, TickObserver


class TestManifoldEngine:
    def test_curvature_flat_line_is_zero(self):
        engine = ManifoldEngine()
        flat = np.ones(50) * 100.0
        assert engine.calculate_curvature(flat) == pytest.approx(0.0, abs=1e-9)

    def test_curvature_spike_detected(self):
        engine = ManifoldEngine(sensitivity=0.01)
        prices = np.concatenate([np.linspace(100, 110, 30), np.linspace(110, 95, 30)])
        curvature = engine.calculate_curvature(prices)
        assert curvature > engine.sensitivity

    def test_entropy_finite_on_noisy_returns(self):
        engine = ManifoldEngine()
        rng = np.random.default_rng(42)
        prices = 100 * np.exp(np.cumsum(rng.normal(0, 0.002, size=80)))
        entropy = engine.differential_entropy(prices)
        assert np.isfinite(entropy)
        assert entropy != 0.0

    def test_reversal_signal_on_high_curvature(self):
        engine = ManifoldEngine(sensitivity=0.01)
        assert engine.generate_signal(0.5) == "REVERSAL_IMMINENT"

    def test_hold_on_low_curvature(self):
        engine = ManifoldEngine(sensitivity=1.0)
        assert engine.generate_signal(0.001) == "HOLD"

    def test_breakout_primed_on_compressed_entropy(self):
        engine = ManifoldEngine()
        assert (
            engine.generate_signal(0.0, entropy=0.5, entropy_baseline=1.0)
            == "BREAKOUT_PRIMED"
        )


class TestTickObserver:
    @pytest.mark.asyncio
    async def test_emit_dispatches_to_handler(self):
        observer = TickObserver()
        received: list[Tick] = []

        async def handler(tick: Tick) -> None:
            received.append(tick)

        observer.subscribe(handler)
        tick = Tick(symbol="SPY", price=450.25)
        await observer.emit(tick)
        assert len(received) == 1
        assert received[0].symbol == "SPY"

    @pytest.mark.asyncio
    async def test_queue_listener(self):
        observer = TickObserver()
        q: asyncio.Queue[Tick] = asyncio.Queue()
        hits: list[float] = []
        observer.subscribe(lambda t: hits.append(t.price))

        task = observer.start_background(q)
        await q.put(Tick(symbol="QQQ", price=380.0))
        await q.put(Tick(symbol="QQQ", price=381.0))
        await asyncio.sleep(0.05)
        await observer.stop()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert hits == [380.0, 381.0]


class TestAlphaGenerator:
    def test_tithe_on_positive_pnl(self):
        gen = AlphaGenerator(tithe_rate=TITHE_RATE, enable_shadow_audit=False)
        state = gen._state("TEST")
        state.prices = [100.0, 100.0]
        pnl_delta, tithe_delta = gen._apply_action(state, Action.BUY, 101.0)
        assert tithe_delta == pytest.approx(0.1)
        assert pnl_delta == pytest.approx(0.9)
        assert state.tithe_accrued == pytest.approx(0.1)

    def test_tithe_rate_constant(self):
        assert TITHE_RATE == pytest.approx(0.10)

    def test_tithe_allocation_splits_basket(self):
        gen = AlphaGenerator(enable_shadow_audit=False)
        gen._state("X").tithe_accrued = 100.0
        alloc = gen.tithe_allocation("X")
        assert sum(alloc.values()) == pytest.approx(100.0)
        assert set(alloc.keys()) == {"FOOD", "WATER"}
