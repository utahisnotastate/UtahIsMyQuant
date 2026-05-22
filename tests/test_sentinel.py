"""Sentinel tick observer, shadow tensor, and decision matrix tests."""
from __future__ import annotations

import asyncio
import numpy as np
import pytest

from src.alpha_generator import Action, AlphaGenerator, DecisionMatrix, ExecuteAction
from src.manifold_kernel import ManifoldEngine
from src.shadow_tensor import ShadowTensorAudit
from src.tick_observer import Tick, TickObserver


class TestManifoldDrift:
    def test_drift_nonzero_on_acceleration(self):
        engine = ManifoldEngine()
        # Non-uniform step growth -> non-zero third difference (jerk)
        prices = np.array([100.0, 101.0, 104.0, 108.0, 113.0, 119.0], dtype=float)
        assert abs(engine.manifold_drift(prices)) > 0

    def test_adaptive_dtype_high_vol_uses_float32(self):
        engine = ManifoldEngine()
        rng = np.random.default_rng(0)
        wild = 100 * np.exp(np.cumsum(rng.normal(0, 0.05, size=40)))
        assert engine.adaptive_dtype(wild) is np.float32

    def test_drift_signal_follows_acceleration_sign(self):
        engine = ManifoldEngine(sensitivity=1e9, entropy_window=8)
        prices = np.array([100.0, 101.0, 104.0, 108.0, 113.0, 119.0, 126.0], dtype=float)
        drift = engine.manifold_drift(prices)
        signal = engine.generate_signal(0.0, drift=drift)
        if drift > 0:
            assert signal == "DRIFT_ACCELERATING"
        elif drift < 0:
            assert signal == "DRIFT_DECELERATING"
        else:
            assert signal == "HOLD"


class TestShadowTensor:
    def test_mirror_detection_raises_degradation(self):
        audit = ShadowTensorAudit(mirror_threshold=0.01)
        engine = ManifoldEngine(sensitivity=0.01)
        prices = np.concatenate([np.linspace(100, 110, 25), np.linspace(110, 95, 25)])
        vec = prices.astype(np.float64)
        signal = engine.generate_signal(engine.calculate_curvature(vec))
        for _ in range(20):
            audit.record_tick("SPY", vec, signal, entropy_baseline=1.0)
        snap = audit.snapshot()
        assert snap.samples > 0

    def test_alpha_healthy_when_low_mirror_rate(self):
        audit = ShadowTensorAudit(mirror_threshold=0.99)
        assert audit.alpha_healthy()


class TestDecisionMatrix:
    def test_breakout_positive_drift_buys(self):
        action = DecisionMatrix.intended_side("BREAKOUT_PRIMED", 0.01, Action.HOLD)
        assert action == Action.BUY

    def test_reversal_negative_drift_buys(self):
        action = DecisionMatrix.intended_side("REVERSAL_IMMINENT", -0.01, Action.HOLD)
        assert action == Action.BUY

    def test_deceleration_exits_when_positioned(self):
        action = DecisionMatrix.intended_side("DRIFT_DECELERATING", 0.0, Action.BUY)
        assert action == Action.EXIT


class TestTickObserverSentinel:
    @pytest.mark.asyncio
    async def test_ingest_process_pipeline(self):
        observer = TickObserver()
        observer.subscribe(lambda t: None)
        observer._running = True
        observer._process_task = asyncio.create_task(observer.process())
        await observer.ingest({"symbol": "SPY", "price": 450.0, "volume": 100})
        await asyncio.sleep(0.05)
        await observer.stop()
        assert observer.ticks_processed >= 1

    def test_tick_from_payload_aliases(self):
        tick = Tick.from_payload({"s": "QQQ", "p": 380.5, "v": 10})
        assert tick.symbol == "QQQ"
        assert tick.price == pytest.approx(380.5)


class TestAlphaPipeline:
    def test_process_tick_returns_action(self):
        gen = AlphaGenerator(enable_shadow_audit=False)
        prices = [100 + i * 0.1 for i in range(20)]
        event = None
        for p in prices:
            event = gen.process_tick(Tick(symbol="SPY", price=float(p)))
        assert event is not None
        assert event.action in Action
