"""Phase 2: logic-gate decision matrix tests."""
from __future__ import annotations

import pytest

from src.alpha_generator import (
    Action,
    AlphaGenerator,
    ExecuteAction,
    LogicGateMatrix,
)


class TestLogicGates:
    def test_gate_curvature_reversal_requires_magnitude(self):
        gates = LogicGateMatrix(curvature_sensitivity=0.05)
        assert gates.gate_curvature("REVERSAL_IMMINENT", 0.10) is True
        assert gates.gate_curvature("REVERSAL_IMMINENT", 0.01) is False

    def test_gate_curvature_breakout_passes(self):
        gates = LogicGateMatrix()
        assert gates.gate_curvature("BREAKOUT_PRIMED", 0.0) is True

    def test_gate_risk_blocks_overexposure(self):
        gates = LogicGateMatrix(risk_limit=0.02)
        assert gates.gate_risk(100_000, 1_000) is True
        assert gates.gate_risk(100_000, 5_000) is False

    def test_gate_volume_blocks_thin_ticks(self):
        gates = LogicGateMatrix(min_volume=100)
        assert gates.gate_volume(500) is True
        assert gates.gate_volume(10) is False


class TestGenerateAction:
    def test_wait_when_curvature_gate_fails(self):
        gen = AlphaGenerator(enable_shadow_audit=False)
        out = gen.generate_action(
            "HOLD",
            capital=100_000,
            exposure=0,
            curvature=0.0,
            volume=1000,
        )
        assert out["action"] == ExecuteAction.WAIT.value
        assert "curvature" in out["gates_failed"]

    def test_execute_buy_when_all_gates_green(self):
        gen = AlphaGenerator(enable_shadow_audit=False, risk_limit=0.02)
        out = gen.generate_action(
            "REVERSAL_IMMINENT",
            capital=100_000,
            exposure=0,
            curvature=0.10,
            volume=5000,
            drift=-0.01,
        )
        assert out["action"] == ExecuteAction.EXECUTE_BUY.value
        assert out["size"] == pytest.approx(2000.0)

    def test_wait_when_risk_exceeded(self):
        gen = AlphaGenerator(enable_shadow_audit=False)
        out = gen.generate_action(
            "REVERSAL_IMMINENT",
            capital=100_000,
            exposure=10_000,
            curvature=0.10,
            volume=5000,
        )
        assert out["action"] == ExecuteAction.WAIT.value
        assert "risk" in out["gates_failed"]

    def test_shadow_failure_blocks_execution(self):
        gen = AlphaGenerator(enable_shadow_audit=False)
        out = gen.generate_action(
            "BREAKOUT_PRIMED",
            capital=100_000,
            exposure=0,
            curvature=0.10,
            volume=5000,
            shadow_healthy=False,
            drift=0.01,
        )
        assert out["action"] == ExecuteAction.WAIT.value
        assert "shadow" in out["gates_failed"]


class TestDecisionToAction:
    def test_maps_execute_buy(self):
        assert (
            AlphaGenerator.decision_to_action({"action": ExecuteAction.EXECUTE_BUY.value})
            == Action.BUY
        )
