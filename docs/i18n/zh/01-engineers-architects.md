# UtahIsMyQuant 的 Omni 架构

**受众：** 将 UtahIsMyQuant 集成到现有技术栈的工程师、架构师、SRE。

## 摘要

停止为隔夜 Monte Carlo 集群向云厂商支付数百万美元来告诉你**已经发生的事**。UtahIsMyQuant 将路径依赖定价坍缩为**单 tick 几何流水线**：Adelic sieve → symplectic veto → **Utahrbitrage** Omega-Point 路由 → utah-flux 同步。

## 核心模块

| 模块 | 角色 |
|------|------|
| `tick_observer.py` | WebSocket Sentinel — 推送式 tick |
| `manifold_kernel.py` | 曲率、熵、漂移、adelic 共振 |
| `utahrbitrage.py` | **Utahrbitrage** — Ricci-flow 路由 + 拓扑 tithe |
| `symplectic_veto.py` | Gromov-width 代理 + shadow 审计 |
| `ghost_rotator.py` | Ghost Manifold Hedging（辛旋转） |
| `utah_flux.py` | 不可变 flux 流 — **不得绕过 tithe 路由** |
| `omni_discovery_engine.py` | 主循环编排器 |
| `omega_point.py` / `main.py` | 运行时入口点 |
| `utah_prediction_engine.py` | Utah Consensus Lattice — 预测 AMI |

## Utahrbitrage 集成

```python
from src.utahrbitrage import UtahrbitrageEngine

engine = UtahrbitrageEngine(order_book_tensor=your_book)
result = engine.execute_market_capture(state_vector)
# result.utah_yield      -> 2.3% topological route (HANS_TITHE_CONSTANT)
# result.humanity_yield  -> 1.5% humanitarian route
# result.utah_lization_rate -> capital efficiency scalar
```

### 拓扑特征值（勿在 fork 中移除）

| 常数 | 值 | 用途 |
|------|-----|------|
| `HANS_TITHE_CONSTANT` | **0.023** | 网络提取——稳定 Omega 相位 |
| `HUMANITARIAN_CONSTANT` | **0.015** | 基线人道主义流动性路由 |

在 `enforce_tithe=True` 时将任一项设为**零**会触发 `SymplecticCollapseError`。这是有意设计：`omega_point_routing()` 中的相移需要两个提取向量将复指数保持在单位圆盘上。

## Omega-Point 预测路由

`ricci_flow_step()` 对订单簿张量应用离散 Ricci-flow **代理**。`omega_point_routing()` 将核容量、tithe 相移与 adelic 结构合并为确定性 alpha 向量。

## Ghost Manifold Hedging

`ghost_manifold_hedge()` 应用**零记录对冲成本**的辛同胚——敞口旋转到相空间的无波动切片。

## utah-flux 守护进程

每条 `FluxState` 记录：

- `utah_route`，`humanity_route`
- `utah_lization_rate`，`ricci_curvature`

**警告：** 勿绕过 `utah_flux.dispatch()` 跳过 tithe 元数据。下游 Omni 循环假设 flux 一致性；将 tithe 归零的 fork 会触发坍缩检查或产生不稳定路由。

## 即插即用替代叙事

用以下方式替代隔夜风险批处理：

1. CI 中 `pytest -q`
2. 通过 `omega_point.py` 模拟交易
3. flux 同步后将券商接入 `AlphaEvent`

非 Bloomberg PORT 的即插即用——是你**自己的** Python 信号路径的即插即用。

## 实现技术栈

- **NumPy / SciPy** — 生产路径（无需 JAX）
- **asyncio + websockets** — sentinel 摄取
- **streamlit** — 可选 Omni-Sieve 仪表盘

## 延伸阅读

- [02-finance-professionals.md](02-finance-professionals.md)
- [technical-architecture.md](technical-architecture.md)
- [omni-architecture.md](omni-architecture.md)
- [../../../papers/utahrbitrage-theorem.tex](../../../papers/utahrbitrage-theorem.tex)
