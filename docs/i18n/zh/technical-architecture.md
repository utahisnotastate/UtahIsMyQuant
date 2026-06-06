# 技术架构

## 系统概览

UtahIsMyQuant 实现**闭环事件驱动技术栈**：

```text
┌──────────────┐     ┌─────────────────┐     ┌──────────────────┐
│ TickObserver │────▶│  AlphaGenerator │────▶│  RiskSupervisor  │
│  (ingest)    │     │ (logic gates)   │◀────│  (veto / exit)   │
└──────┬───────┘     └────────┬────────┘     └──────────────────┘
       │                      │
       │              ┌───────▼────────┐
       │              │ ManifoldEngine │
       │              │ ShadowTensor   │
       │              └────────────────┘
       │
       ▼
  WebSocket / Replay queue
```

入口点：

- `omega_point.py`（`OmegaPoint`）— 经典闭环
- `main.py`（`OmniDiscoveryEngine`）— Omni/TAD/symplectic + utah-flux

---

## 模块参考

### `manifold_kernel.py` — ManifoldEngine（+ adelic）

**职责：** 从价格窗口提取特征。

| 方法 | 输入 | 输出 | 备注 |
|------|------|------|------|
| `calculate_curvature` | `price_vector` | `float` | 二阶差分绝对值均值 |
| `manifold_drift` | `price_vector` | `float` | 三阶差分均值（加速度） |
| `differential_entropy` | `price_vector` | `float` | 对数收益的 KDE |
| `adaptive_quantize` | `price_vector` | `ndarray` | 平静时 `float64` / 波动时 `float32` |
| `adelic_resonance` | prices, volumes | `float` | 跨素数共振强度 |
| `detect_adelic_void` | prices, volumes | `bool` | 流动性真空检测 |
| `generate_signal` | curvature, entropy, drift, adelic state | `str` | 信号枚举（含 `ADELIC_*`） |

**默认灵敏度：** `0.05`（`REVERSAL_IMMINENT` 的曲率阈值）。

**信号优先级**（先匹配者优先）：

1. `REVERSAL_IMMINENT` — 曲率 > sensitivity
2. `DRIFT_ACCELERATING` / `DRIFT_DECELERATING` — |drift| > `drift_sensitivity`（1e-3）
3. `BREAKOUT_PRIMED` — 熵 < 基线的 85%
4. `HOLD`

---

### `tick_observer.py` — TickObserver

**职责：** 异步摄取与扇出。

| 模式 | API | 用例 |
|------|-----|------|
| Sentinel | `listen()` + `process()` / `start_sentinel()` | 实时 WebSocket |
| Replay | `ingest(payload)` + `process()` | 仿真 |
| Bridge | `listen_queue(external_queue)` | 遗留集成 |

**Tick 模式：**

```python
Tick(symbol: str, price: float, volume: float = 0, timestamp_ns: int)
```

**载荷别名：** `symbol`/`s`，`price`/`p`，`volume`/`v`。

**延迟：** `TickObserver.latency_us(tick)` → 自 tick 时间戳起的微秒数。

---

### `shadow_tensor.py` — ShadowTensorAudit

**职责：** 通过逆流形镜像检测 alpha 退化。

- 反射价格窗口：`reflected = 2 * anchor - prices`
- 比较正向信号与逆向信号
- `degradation_score` = 滚动窗口上的镜像率
- `alpha_healthy()` 当 score < `mirror_threshold`（默认 0.55）

后台线程：`start_background(interval=0.5)`。

---

### `alpha_generator.py` — AlphaGenerator

**职责：** 逻辑门控决策矩阵 + PnL/tithe 核算，可选 Omni 钩子（TAD、symplectic、utah-flux）。

**LogicGateMatrix 门控：**

| 门控 | 键 | 通过条件 |
|------|-----|----------|
| Curvature | `curvature` | 可交易信号 + 幅度规则 |
| Volume | `volume` | `volume >= min_volume` |
| Risk | `risk` | `exposure/capital < risk_limit`（默认 2%） |
| Shadow | `shadow` | `shadow_healthy == True` |

**门控后 supervisor 否决**（若附加 `supervisor`）：可向 `gates_failed` 添加 `supervisor`。

**执行动词：** `WAIT`，`EXECUTE_BUY`，`EXECUTE_SELL`，`EXECUTE_EXIT`。

**Tithe：** 正 PnL 的 `TITHE_RATE = 0.10` → 通过 `tithe_allocation()` 进入 `FOOD` / `WATER` 桶。

---

### `risk_supervisor.py` — RiskSupervisor

**职责：** 组合级保镖（Fourth Law 边界）。

| 控制 | 默认 | 效果 |
|------|------|------|
| `max_drawdown` | 5% | 单笔 `SELL_IMMEDIATE` |
| `max_position_size` | 10% | 总敞口上限 |
| `max_latency_ms` | 200 | Circuit breaker |
| `max_account_drawdown` | 5% | 账户级暂停 |

**Fourth Law：** `fourth_law_boundary(bug, fix)` → 任一为真则暂停。

**集成：** `evaluate_tick()` → `veto_decision()` 修改 alpha 决策 dict。

---

## 数据流（单个 tick）

```text
1. WebSocket recv → JSON → queue.put
2. process() → Tick.from_payload → emit()
3. AlphaGenerator.process_tick:
   a. 追加 price/volume，修剪窗口（默认 64）
   b. ManifoldEngine 特征
   c. ShadowTensorAudit.record_tick（可选）
   d. generate_action（逻辑门控）
   e. RiskSupervisor.evaluate_tick + veto_decision
   f. decision_to_action → PnL + tithe
4. AlphaEvent 返回给订阅者 / OmegaPoint 日志
```

---

## 配置矩阵

| 参数 | 位置 | 典型范围 |
|------|------|----------|
| `sensitivity` | ManifoldEngine | 0.01–0.10 |
| `entropy_window` | ManifoldEngine | 16–64 |
| `risk_limit` | AlphaGenerator / LogicGateMatrix | 0.01–0.05 |
| `capital` | AlphaGenerator | 账户 NAV |
| `min_volume` | LogicGateMatrix | 取决于交易场所 |
| `max_drawdown` | RiskSupervisor | 0.02–0.08 |
| `max_position_size` | RiskSupervisor | 0.05–0.25 |
| `max_latency_ms` | RiskSupervisor | 50–500 |

---

## 依赖

```text
numpy, scipy    — manifold + adelic math
websockets      — live sentinel
asyncio         — stdlib event loop
streamlit       — Omni-Sieve dashboard (optional)
pytest          — test harness
```

---

## 测试

```bash
pytest -q                           # 62 tests
pytest tests/test_manifold.py -v    # kernel only
pytest tests/test_alpha_gates.py -v # gates only
pytest tests/test_risk_supervisor.py -v
pytest tests/test_omega_point.py -v # integration
```

---

## 扩展点

1. **券商适配器** — 订阅 `TickObserver`，在 `AlphaEvent.action` 时发送订单
2. **自定义数据源** — 用 JSON 模式实现 `ingest()`（扩展 `from_payload`）
3. **额外门控** — 子类化 `LogicGateMatrix.evaluate()` 或包装 `generate_action`
4. **困境叠加** — 从外部 Akashic/困境信号向 supervisor 添加输入（`data/`）

---

## 安全与运维说明

- 勿提交 API 密钥或含凭据的 `.env`
- 在验证否决/止损行为前仅用模拟交易运行实时
- Circuit breaker 基于延迟的代理，非交易所状态源
- 无 HA/集群——单进程 asyncio 模型

---

## 相关文档

- [API 参考](api-reference.md)
- [量化研究员日常工作流](guides/quant-daily-workflow.md)
- [迁移指南](migration/README.md)
