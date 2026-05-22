"""
CORE ARCHITECTURE: ALPHA_GENERATOR
Logic: State-space decision matrix with multi-gate topology.
Converts manifold signals into executable trade actions only when all lights are green.
No backtesting. No optimization. Real-time manifold stability only.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any

import numpy as np

from .manifold_kernel import ManifoldEngine
from .risk_supervisor import RiskSupervisor
from .shadow_tensor import ShadowTensorAudit
from .tick_observer import Tick, TickObserver


TITHE_RATE = 0.10
COMMODITY_BASKET = ("FOOD", "WATER")

# Manifold signals that may request capital (Gate 1 candidates)
TRADEABLE_SIGNALS = frozenset(
    {"REVERSAL_IMMINENT", "BREAKOUT_PRIMED", "DRIFT_ACCELERATING"}
)


class Action(StrEnum):
    HOLD = "HOLD"
    WAIT = "WAIT"
    BUY = "BUY"
    SELL = "SELL"
    EXIT = "EXIT"


class ExecuteAction(StrEnum):
    """Manifesto-facing execution verbs."""
    WAIT = "WAIT"
    EXECUTE_BUY = "EXECUTE_BUY"
    EXECUTE_SELL = "EXECUTE_SELL"
    EXECUTE_EXIT = "EXECUTE_EXIT"


@dataclass
class AlphaState:
    symbol: str
    position: str = "FLAT"
    side: Action = Action.HOLD
    exposure: float = 0.0
    cumulative_pnl: float = 0.0
    tithe_accrued: float = 0.0
    last_curvature: float = 0.0
    last_entropy: float = 0.0
    last_drift: float = 0.0
    prices: list[float] = field(default_factory=list)
    volumes: list[float] = field(default_factory=list)


@dataclass(frozen=True)
class AlphaEvent:
    symbol: str
    signal: str
    action: Action
    decision: dict[str, Any]
    curvature: float
    entropy: float
    drift: float
    precision: str
    pnl_delta: float
    tithe_delta: float
    shadow_healthy: bool
    gates_passed: tuple[str, ...]
    gates_failed: tuple[str, ...]
    supervisor_verdict: str = "CLEAR"
    circuit_breaker: bool = False


class LogicGateMatrix:
    """
    Safety guard: sequential sanity checks before capital commitment.
    All gates must pass; first failure short-circuits with WAIT.
    """

    def __init__(
        self,
        risk_limit: float = 0.02,
        min_volume: float = 1.0,
        curvature_sensitivity: float = 0.05,
    ):
        self.risk_limit = risk_limit
        self.min_volume = min_volume
        self.curvature_sensitivity = curvature_sensitivity

    def gate_curvature(self, signal: str, curvature: float) -> bool:
        """Gate 1: Is the manifold curvature / signal regime sufficient?"""
        if signal == "REVERSAL_IMMINENT":
            return curvature >= self.curvature_sensitivity
        return signal in TRADEABLE_SIGNALS

    def gate_volume(self, volume: float) -> bool:
        """Gate 2: Is market participation adequate?"""
        return volume >= self.min_volume

    def gate_risk(self, capital: float, exposure: float) -> bool:
        """Gate 3: Does this trade exceed per-trade risk tolerance?"""
        if capital <= 0:
            return False
        return (exposure / capital) < self.risk_limit

    def gate_shadow(self, shadow_healthy: bool) -> bool:
        """Gate 4: Is alpha free of inverse-manifold mirror degradation?"""
        return shadow_healthy

    def evaluate(
        self,
        signal: str,
        curvature: float,
        volume: float,
        capital: float,
        exposure: float,
        shadow_healthy: bool,
    ) -> tuple[bool, list[str], list[str]]:
        checks: list[tuple[str, bool]] = [
            ("curvature", self.gate_curvature(signal, curvature)),
            ("volume", self.gate_volume(volume)),
            ("risk", self.gate_risk(capital, exposure)),
            ("shadow", self.gate_shadow(shadow_healthy)),
        ]
        passed = [name for name, ok in checks if ok]
        failed = [name for name, ok in checks if not ok]
        return len(failed) == 0, passed, failed


class DecisionMatrix:
    """State-space resolver: signal + drift + position -> intended direction."""

    @staticmethod
    def intended_side(signal: str, drift: float, side: Action) -> Action:
        if signal == "REVERSAL_IMMINENT":
            if side in (Action.BUY, Action.SELL):
                return Action.EXIT
            return Action.SELL if drift >= 0 else Action.BUY
        if signal == "BREAKOUT_PRIMED":
            return Action.BUY if drift >= 0 else Action.SELL
        if signal == "DRIFT_ACCELERATING":
            if side == Action.HOLD:
                return Action.BUY if drift > 0 else Action.SELL
            return side
        if signal == "DRIFT_DECELERATING":
            return Action.EXIT if side in (Action.BUY, Action.SELL) else Action.HOLD
        return Action.HOLD if side == Action.HOLD else side


class AlphaGenerator:
    """
    Executive decision module: manifold intelligence through logic gates,
    then capital-sized execution.
    """

    def __init__(
        self,
        engine: ManifoldEngine | None = None,
        audit: ShadowTensorAudit | None = None,
        gates: LogicGateMatrix | None = None,
        window: int = 64,
        tithe_rate: float = TITHE_RATE,
        risk_limit: float = 0.02,
        capital: float = 100_000.0,
        min_volume: float = 1.0,
        enable_shadow_audit: bool = True,
        supervisor: RiskSupervisor | None = None,
    ):
        self.engine = engine or ManifoldEngine()
        self.supervisor = supervisor
        self.audit = audit or ShadowTensorAudit(engine=self.engine)
        self.gates = gates or LogicGateMatrix(
            risk_limit=risk_limit,
            min_volume=min_volume,
            curvature_sensitivity=self.engine.sensitivity,
        )
        self.risk_limit = risk_limit
        self.capital = capital
        self.window = window
        self.tithe_rate = tithe_rate
        self.enable_shadow_audit = enable_shadow_audit
        self._states: dict[str, AlphaState] = {}
        self._entropy_baselines: dict[str, float] = {}
        if enable_shadow_audit:
            self.audit.start_background(interval=0.5)

    def _state(self, symbol: str) -> AlphaState:
        if symbol not in self._states:
            self._states[symbol] = AlphaState(symbol=symbol)
        return self._states[symbol]

    def attach(self, observer: TickObserver) -> None:
        observer.subscribe(self.on_tick)

    async def on_tick(self, tick: Tick) -> AlphaEvent | None:
        return self.process_tick(tick)

    # --- Manifesto gate API (callable standalone) ---

    def gate_curvature(self, signal: str, curvature: float) -> bool:
        return self.gates.gate_curvature(signal, curvature)

    def gate_risk(self, capital: float, exposure: float) -> bool:
        return self.gates.gate_risk(capital, exposure)

    def gate_volume(self, volume: float) -> bool:
        return self.gates.gate_volume(volume)

    def generate_action(
        self,
        signal: str,
        capital: float,
        exposure: float,
        *,
        curvature: float = 0.0,
        volume: float = 0.0,
        shadow_healthy: bool = True,
        drift: float = 0.0,
        side: Action = Action.HOLD,
    ) -> dict[str, Any]:
        """
        Decision matrix: combine manifold signals with hard-coded risk constraints.
        Returns manifesto-compatible dict (WAIT | EXECUTE_*).
        """
        all_green, passed, failed = self.gates.evaluate(
            signal, curvature, volume, capital, exposure, shadow_healthy
        )

        if not all_green:
            reason = self._wait_reason(failed)
            return {
                "action": ExecuteAction.WAIT.value,
                "reason": reason,
                "gates_passed": passed,
                "gates_failed": failed,
                "timestamp_ns": time.time_ns(),
            }

        intended = DecisionMatrix.intended_side(signal, drift, side)
        if intended == Action.EXIT:
            return {
                "action": ExecuteAction.EXECUTE_EXIT.value,
                "size": exposure,
                "reason": "Deceleration / reversal exit — all gates green.",
                "gates_passed": passed,
                "gates_failed": failed,
                "timestamp_ns": time.time_ns(),
            }
        if intended == Action.SELL:
            return {
                "action": ExecuteAction.EXECUTE_SELL.value,
                "size": capital * self.risk_limit,
                "reason": "Manifold SELL — all gates green.",
                "gates_passed": passed,
                "gates_failed": failed,
                "timestamp_ns": time.time_ns(),
            }
        if intended == Action.BUY:
            return {
                "action": ExecuteAction.EXECUTE_BUY.value,
                "size": capital * self.risk_limit,
                "reason": "Manifold BUY — all gates green.",
                "gates_passed": passed,
                "gates_failed": failed,
                "timestamp_ns": time.time_ns(),
            }

        return {
            "action": ExecuteAction.WAIT.value,
            "reason": "No executable edge after gates.",
            "gates_passed": passed,
            "gates_failed": failed,
            "timestamp_ns": time.time_ns(),
        }

    @staticmethod
    def _wait_reason(failed: list[str]) -> str:
        if "curvature" in failed:
            return "Manifold curvature insufficient."
        if "risk" in failed:
            return "Risk threshold exceeded."
        if "volume" in failed:
            return "Volume below participation threshold."
        if "shadow" in failed:
            return "Shadow tensor audit failed — alpha mirroring detected."
        if "supervisor" in failed:
            return "Risk supervisor veto — Fourth Law boundary active."
        return "Gate check failed."

    @staticmethod
    def decision_to_action(decision: dict[str, Any]) -> Action:
        mapping = {
            ExecuteAction.WAIT.value: Action.WAIT,
            ExecuteAction.EXECUTE_BUY.value: Action.BUY,
            ExecuteAction.EXECUTE_SELL.value: Action.SELL,
            ExecuteAction.EXECUTE_EXIT.value: Action.EXIT,
        }
        return mapping.get(decision["action"], Action.HOLD)

    def process_tick(self, tick: Tick) -> AlphaEvent | None:
        state = self._state(tick.symbol)
        state.prices.append(tick.price)
        state.volumes.append(tick.volume)
        if len(state.prices) > self.window:
            state.prices = state.prices[-self.window :]
            state.volumes = state.volumes[-self.window :]

        if len(state.prices) < 3:
            return None

        vec = np.array(state.prices, dtype=np.float64)
        curvature = self.engine.calculate_curvature(vec)
        entropy = self.engine.differential_entropy(vec)
        drift = self.engine.manifold_drift(vec)
        precision = self.engine.adaptive_dtype(vec).__name__
        avg_volume = float(np.mean(state.volumes[-8:])) if state.volumes else tick.volume

        baseline = self._entropy_baselines.get(tick.symbol, entropy)
        self._entropy_baselines[tick.symbol] = 0.95 * baseline + 0.05 * entropy

        signal = self.engine.generate_signal(
            curvature,
            entropy=entropy,
            entropy_baseline=baseline,
            drift=drift,
        )

        if self.enable_shadow_audit:
            self.audit.record_tick(tick.symbol, vec, signal, baseline)

        shadow_healthy = self.audit.alpha_healthy()

        decision = self.generate_action(
            signal,
            self.capital,
            state.exposure,
            curvature=curvature,
            volume=max(tick.volume, avg_volume),
            shadow_healthy=shadow_healthy,
            drift=drift,
            side=state.side,
        )

        supervisor_tag = "CLEAR"
        circuit = False
        if self.supervisor is not None:
            equity = self.capital + sum(s.cumulative_pnl for s in self._states.values())
            latency_ms = TickObserver.latency_us(tick) / 1000.0
            positions = self._build_positions(tick.symbol, state)
            verdict = self.supervisor.evaluate_tick(
                tick.symbol,
                tick.price,
                equity,
                positions,
                latency_ms,
                returns_std=self._returns_std(state.prices),
            )
            decision = self.supervisor.veto_decision(decision, verdict)
            supervisor_tag = str(decision.get("supervisor", "CLEAR"))
            circuit = verdict.circuit_breaker

        action = self.decision_to_action(decision)
        if action in (Action.BUY, Action.SELL):
            state.exposure = float(decision.get("size", self.capital * self.risk_limit))
        elif action == Action.EXIT:
            state.exposure = 0.0

        state.side = action if action != Action.WAIT else state.side

        pnl_delta, tithe_delta = self._apply_action(state, action, tick.price)
        state.last_curvature = curvature
        state.last_entropy = entropy
        state.last_drift = drift
        state.position = signal if signal != "HOLD" else state.position

        passed = tuple(decision.get("gates_passed", ()))
        failed = tuple(decision.get("gates_failed", ()))

        return AlphaEvent(
            symbol=tick.symbol,
            signal=signal,
            action=action,
            decision=decision,
            curvature=curvature,
            entropy=entropy,
            drift=drift,
            precision=precision,
            pnl_delta=pnl_delta,
            tithe_delta=tithe_delta,
            shadow_healthy=shadow_healthy,
            gates_passed=passed,
            gates_failed=failed,
            supervisor_verdict=supervisor_tag,
            circuit_breaker=circuit,
        )

    def _apply_action(self, state: AlphaState, action: Action, price: float) -> tuple[float, float]:
        """Mark-to-market by action; tithe on gains only."""
        if action in (Action.HOLD, Action.WAIT) or len(state.prices) < 2:
            return 0.0, 0.0

        prev = state.prices[-2]
        move = price - prev
        pnl_delta = 0.0

        if action == Action.BUY:
            pnl_delta = move
        elif action == Action.SELL:
            pnl_delta = -move
        elif action == Action.EXIT:
            if state.position in ("BREAKOUT_PRIMED", "DRIFT_ACCELERATING"):
                pnl_delta = move
            elif state.position in ("REVERSAL_IMMINENT", "DRIFT_DECELERATING"):
                pnl_delta = -move
            state.side = Action.HOLD

        tithe_delta = 0.0
        if pnl_delta > 0:
            tithe_delta = pnl_delta * self.tithe_rate
            state.tithe_accrued += tithe_delta
            pnl_delta -= tithe_delta

        state.cumulative_pnl += pnl_delta
        return pnl_delta, tithe_delta

    def tithe_allocation(self, symbol: str | None = None) -> dict[str, float]:
        """Split accrued tithe across humanitarian commodity basket."""
        total = (
            self._states[symbol].tithe_accrued
            if symbol and symbol in self._states
            else sum(s.tithe_accrued for s in self._states.values())
        )
        per = total / len(COMMODITY_BASKET)
        return {commodity: per for commodity in COMMODITY_BASKET}

    def _build_positions(self, symbol: str, state: AlphaState) -> list[dict[str, Any]]:
        positions: list[dict[str, Any]] = []
        for sym, st in self._states.items():
            if st.exposure <= 0 or not st.prices:
                continue
            side = "long" if st.side == Action.BUY else "short"
            positions.append(
                {
                    "symbol": sym,
                    "entry_price": st.prices[0],
                    "value": st.exposure,
                    "side": side,
                }
            )
        if state.exposure > 0 and state.prices and not any(p["symbol"] == symbol for p in positions):
            positions.append(
                {
                    "symbol": symbol,
                    "entry_price": state.prices[0],
                    "value": state.exposure,
                    "side": "long" if state.side == Action.BUY else "short",
                }
            )
        return positions

    @staticmethod
    def _returns_std(prices: list[float]) -> float:
        if len(prices) < 3:
            return 0.0
        vec = np.array(prices, dtype=np.float64)
        returns = np.diff(np.log(np.maximum(vec, 1e-12)))
        return float(np.std(returns))

    def shutdown(self) -> None:
        self.audit.stop()
        if self.supervisor is not None:
            self.supervisor.stop()
