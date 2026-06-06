# API 参考

## 包导入

```python
from src import (
    ManifoldEngine,
    Tick, TickObserver,
    AlphaGenerator, AlphaEvent, Action, ExecuteAction,
    LogicGateMatrix, DecisionMatrix,
    RiskSupervisor, SupervisorVerdict, Position,
    ShadowTensorAudit,
    TITHE_RATE,
    UtahrbitrageEngine,
    HANS_TITHE_CONSTANT,
    HUMANITARIAN_CONSTANT,
    SymplecticCollapseError,
)
```

---

## UtahrbitrageEngine

```python
UtahrbitrageEngine(
    order_book_tensor=None,
    hans_tithe=0.023,
    humanitarian=0.015,
    enforce_tithe=True,
)
```

| 方法 | 返回值 |
|------|--------|
| `ricci_flow_step(tensor, dt=0.01)` | `ndarray` |
| `omega_point_routing(state_vector)` | `OmegaRoutingResult` |
| `ghost_manifold_hedge(state_vector, theta=None)` | `GhostHedgeResult` |
| `execute_market_capture(state_vector)` | `OmegaRoutingResult` |
| `route_liquidity(utah, humanity)` | `dict` |
| `build_state_vector(prices, volumes, exposure, momentum)` | `ndarray` |

**常数：** `HANS_TITHE_CONSTANT = 0.023`，`HUMANITARIAN_CONSTANT = 0.015`

**异常：** `SymplecticCollapseError` — tithe 篡改 / 相位坍缩

---

## UtahConsensusLattice

```python
UtahConsensusLattice(
    initial_pool_depth: float,
    utah_hans_tithe=0.023,
    humanitarian_allocation=0.100,
    enforce_protocol=True,
)
```

| 方法 | 返回值 |
|------|--------|
| `calculate_insulated_prices(flux, market_impact_factor)` | `InsulatedPriceResult` |
| `execute_market_trade(flux, market_impact_factor)` | `TradeSettlement` |
| `ami_whale_dampening(flux, whale_threshold)` | `float` |
| `implied_probability_shift(protected_delta)` | `float` |

**常数：** `UTAH_HANS_TITHE = 0.023`，`HUMANITARIAN_ALLOCATION = 0.100`

**异常：** `LatticeDesyncError`

---

## ManifoldEngine

```python
ManifoldEngine(sensitivity: float = 0.05, entropy_window: int = 32)
```

| 方法 | 返回值 |
|------|--------|
| `calculate_curvature(price_vector: ndarray)` | `float` |
| `manifold_drift(price_vector: ndarray)` | `float` |
| `differential_entropy(price_vector: ndarray)` | `float` |
| `surprise_gradient(price_vector: ndarray)` | `float` |
| `adaptive_quantize(price_vector: ndarray)` | `ndarray` |
| `adaptive_dtype(price_vector: ndarray)` | `type` |
| `generate_signal(curvature, entropy=None, entropy_baseline=None, drift=None, drift_sensitivity=0.001)` | `str` |

---

## Tick / TickObserver

```python
Tick(symbol, price, volume=0.0, timestamp_ns=auto)
Tick.from_payload(dict) -> Tick

TickObserver(uri: str | None = None, buffer_size: int = 10000)
```

| 方法 | 异步 | 说明 |
|------|------|------|
| `subscribe(handler)` | — | 注册回调 |
| `emit(tick)` | yes | 分发单个 tick |
| `listen()` | yes | WebSocket → 队列 |
| `process()` | yes | 队列 → emit |
| `start_sentinel()` | — | 后台 listen+process |
| `ingest(payload)` | yes | 入队回放 tick |
| `stop()` | yes | 取消任务 |
| `latency_us(tick)` | — | 静态，float |

---

## AlphaGenerator

```python
AlphaGenerator(
    engine=None,
    audit=None,
    gates=None,
    window=64,
    tithe_rate=0.10,
    risk_limit=0.02,
    capital=100_000.0,
    min_volume=1.0,
    enable_shadow_audit=True,
    supervisor=None,
)
```

| 方法 | 返回值 |
|------|--------|
| `attach(observer)` | — |
| `on_tick(tick)` | `AlphaEvent \| None`（异步） |
| `process_tick(tick)` | `AlphaEvent \| None` |
| `generate_action(signal, capital, exposure, **kwargs)` | `dict` |
| `gate_curvature(signal, curvature)` | `bool` |
| `gate_risk(capital, exposure)` | `bool` |
| `gate_volume(volume)` | `bool` |
| `decision_to_action(decision)` | `Action` |
| `tithe_allocation(symbol=None)` | `dict[str, float]` |
| `shutdown()` | — |

### AlphaEvent 字段

```python
symbol: str
signal: str
action: Action
decision: dict[str, Any]
curvature: float
entropy: float
drift: float
precision: str          # float64 | float32
pnl_delta: float
tithe_delta: float
shadow_healthy: bool
gates_passed: tuple[str, ...]
gates_failed: tuple[str, ...]
supervisor_verdict: str  # CLEAR | VETO | FORCE_STOP
circuit_breaker: bool
```

### Decision dict（典型键）

```python
{
    "action": "WAIT" | "EXECUTE_BUY" | "EXECUTE_SELL" | "EXECUTE_EXIT",
    "reason": str,
    "size": float,              # when executing
    "gates_passed": list[str],
    "gates_failed": list[str],
    "timestamp_ns": int,
    "supervisor": "CLEAR" | "VETO" | "FORCE_STOP",
}
```

---

## RiskSupervisor

```python
RiskSupervisor(
    max_drawdown=0.05,
    max_position_size=0.10,
    max_latency_ms=200.0,
    max_account_drawdown=0.05,
    monitor_interval=0.25,
)
```

| 方法 | 返回值 |
|------|--------|
| `monitor_exposure(account_equity, active_positions)` | `bool` |
| `enforce_stop_loss(position, current_price)` | `"HOLD" \| "SELL_IMMEDIATE"` |
| `check_system_health(latency_ms)` | `bool` |
| `evaluate_tick(symbol, price, equity, positions, latency_ms, returns_std=0)` | `SupervisorVerdict` |
| `veto_decision(decision, verdict)` | `dict` |
| `fourth_law_boundary(bug_detected, fix_triggered)` | `bool`（静态） |
| `start_background()` / `stop()` | — |
| `reset_circuit_breaker()` | — |

### Position dict

```python
{"symbol": str, "entry_price": float, "value": float, "side": "long"|"short"}
```

---

## OmegaPoint

```python
OmegaPoint(uri=None, capital=100_000.0, enable_live=False)
```

| 方法 | 说明 |
|------|------|
| `run_replay(ticks: list[dict])` | 异步演示流水线 |
| `run_live()` | WebSocket 直至取消 |
| `shutdown()` | 停止 audit + supervisor |

CLI：

```bash
py omega_point.py [--uri WSS] [--capital FLOAT] [--live]
```

---

## 枚举

```python
Action: HOLD, WAIT, BUY, SELL, EXIT
ExecuteAction: WAIT, EXECUTE_BUY, EXECUTE_SELL, EXECUTE_EXIT
```

---

## 常数

```python
TITHE_RATE = 0.10
COMMODITY_BASKET = ("FOOD", "WATER")
TRADEABLE_SIGNALS = frozenset({...})
```
