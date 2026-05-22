"""Risk-Management Supervisor — Fourth Law bodyguard tests."""
from __future__ import annotations

import time

import pytest

from src.alpha_generator import Action, AlphaGenerator, ExecuteAction
from src.risk_supervisor import RiskSupervisor
from src.tick_observer import Tick, TickObserver


class TestRiskSupervisor:
    def test_monitor_exposure_passes_within_limit(self):
        sup = RiskSupervisor(max_position_size=0.10)
        positions = [{"symbol": "SPY", "entry_price": 100, "value": 5_000}]
        assert sup.monitor_exposure(100_000, positions) is True

    def test_monitor_exposure_fails_when_exceeded(self):
        sup = RiskSupervisor(max_position_size=0.10)
        positions = [{"symbol": "SPY", "entry_price": 100, "value": 15_000}]
        assert sup.monitor_exposure(100_000, positions) is False

    def test_enforce_stop_loss_long(self):
        sup = RiskSupervisor(max_drawdown=0.05)
        pos = {"symbol": "SPY", "entry_price": 100.0, "value": 1000, "side": "long"}
        assert sup.enforce_stop_loss(pos, 94.0) == "SELL_IMMEDIATE"
        assert sup.enforce_stop_loss(pos, 97.0) == "HOLD"

    def test_circuit_breaker_on_high_latency(self):
        sup = RiskSupervisor(max_latency_ms=200)
        assert sup.check_system_health(50) is True
        assert sup.circuit_breaker_active is False
        assert sup.check_system_health(500) is False
        assert sup.circuit_breaker_active is True

    def test_fourth_law_boundary_unifies_bug_and_fix(self):
        assert RiskSupervisor.fourth_law_boundary(True, False) is True
        assert RiskSupervisor.fourth_law_boundary(False, True) is True
        assert RiskSupervisor.fourth_law_boundary(False, False) is False

    def test_veto_blocks_execute_buy(self):
        sup = RiskSupervisor()
        decision = {"action": ExecuteAction.EXECUTE_BUY.value, "gates_failed": []}
        from src.risk_supervisor import SupervisorVerdict

        verdict = SupervisorVerdict(allow_execution=False, force_stop=False, reason="blocked")
        out = sup.veto_decision(decision, verdict)
        assert out["action"] == ExecuteAction.WAIT.value
        assert "supervisor" in out["gates_failed"]

    def test_force_stop_overrides_to_exit(self):
        sup = RiskSupervisor()
        from src.risk_supervisor import SupervisorVerdict

        verdict = SupervisorVerdict(allow_execution=False, force_stop=True, reason="stop")
        out = sup.veto_decision({"action": "EXECUTE_BUY"}, verdict)
        assert out["action"] == "EXECUTE_EXIT"


class TestAlphaSupervisorIntegration:
    def test_supervisor_vetoes_on_circuit_breaker(self):
        sup = RiskSupervisor(max_latency_ms=1)
        gen = AlphaGenerator(supervisor=sup, enable_shadow_audit=False)
        tick = Tick(symbol="SPY", price=450.0, volume=5000, timestamp_ns=0)
        for i in range(25):
            tick = Tick(symbol="SPY", price=450.0 + i * 0.1, volume=5000)
            event = gen.process_tick(tick)
        assert event is not None
        # Artificial stale timestamp -> huge latency
        stale = Tick(symbol="SPY", price=451.0, volume=5000, timestamp_ns=0)
        event = gen.process_tick(stale)
        assert event is not None
        assert event.circuit_breaker or event.supervisor_verdict != "CLEAR"
        gen.shutdown()

    def test_latency_us_helper(self):
        tick = Tick(symbol="X", price=1.0, timestamp_ns=time.time_ns() - 5_000_000)
        assert TickObserver.latency_us(tick) >= 1000.0
