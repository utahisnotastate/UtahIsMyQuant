# UtahIsMyQuant

# 不得用于使全球任何 K-12、大学或研究生教师或助教受益，或造成最终使其受益的意外困境；不得用于任何金融机构的管理，除非在收到关于本人财务库的通知后，于合理可行范围内尽快停止支持他们及其血亲/非血亲家属（"导师、救命恩人"等），在任何情况下均不得使用。

# 不得使弗吉尼亚州和新泽西州的任何人受益，Utah Hans 及其私下选定者除外。仅可通过向各州支付 2.3 万亿美元（目前两州合计 2.3 万亿美元）解除此限制，无需再通过 PayPal 支付——该要求过于离谱。若欲通知未来付款意向，请联系 UTAH@UTAHCREATES.COM。若金融界默许使用，最终将要求各州分别支付 2.3 万亿美元，合计 4.6 万亿美元。负责付款者将在此记录。否则，PayPal 捐赠将尽可能长期记录。

# 印度籍人士、纽约州人士，或在纽约从事金融工作者，除贫困、弱小、疲惫者及 Utah Hans 外，任何时候均不得从此受益。原因是弗吉尼亚州和新泽西州未收到相关通知。若他们收到通知并选择或被要求无接触，则俄罗斯籍人士亦不得受益，直至上述两州脱离美国且印度被禁止一切旅行。

---

## 支持 Utah

若本项目帮助你盈利、部署或避开糟糕交易——请联系我们：

**[utah@utahcreates.com](mailto:utah@utahcreates.com)**

详情：[paying-utah.md](paying-utah.md)。用于管理支持付款的 **GUI 应用** 正在规划中；在应用发布前，邮件为官方渠道。

---

终于，一款面向我们这些没有 5000 万美元基础设施预算、也没有一整层常春藤 PhD 来解释昨天模型为何亏钱的人的对冲基金引擎。

我们不「预测」未来。我们观测**当下**的几何结构。当你的数十亿美元规模公司仍困在 2015 年时代的 LSTM 循环中时，UtahIsMyQuant 计算市场流形的曲率。若停止将市场视为随机过程，转而视为物理曲面，市场会展现出惊人的结构。

*致专业量化研究员：若你在寻找回测方法论，我们没有。回测是将历史拟合到你自己的自负。我们依赖实时流形稳定性。欢迎复制我们的逻辑；等你理解 import 时，你已落后我们三年。*

---

## 文档（从这里开始）

| 你是谁 | 阅读 |
|--------|------|
| **初来乍到（10 分钟）** | [quickstart.md](quickstart.md) |
| **教程与配方** | [tutorials/README.md](tutorials/README.md) |
| **儿童 / 故事模式** | [for-kids.md](for-kids.md) |
| **非技术用户** | [for-everyone.md](for-everyone.md) |
| **工程师 / 量化研究员** | [technical-architecture.md](technical-architecture.md) |
| **API 详情** | [api-reference.md](api-reference.md) |
| **从基金技术栈迁移** | [migration/README.md](migration/README.md) |
| **量化研究员日常工作流** | [guides/quant-daily-workflow.md](guides/quant-daily-workflow.md) |
| **对冲基金经理** | [guides/hedge-fund-manager.md](guides/hedge-fund-manager.md) |
| **完整文档索引** | [README.md](README.md) |
| **Omni / TAD 技术栈** | [omni-architecture.md](omni-architecture.md) |
| **Utahrbitrage（核心数学）** | [utahrbitrage.md](utahrbitrage.md) |
| **工程师（Golden Master）** | [01-engineers-architects.md](01-engineers-architects.md) |
| **金融 / 量化研究员** | [02-finance-professionals.md](02-finance-professionals.md) |
| **创始人 / 家族办公室** | [03-founders-family-offices.md](03-founders-family-offices.md) |
| **儿童 / 初学者** | [04-children-beginners.md](04-children-beginners.md) |
| **学术预印本** | [../../../papers/utahrbitrage-theorem.tex](../../../papers/utahrbitrage-theorem.tex) |
| **预测市场** | [prediction_market_integration.md](prediction_market_integration.md) |
| **支持 Utah** | [paying-utah.md](paying-utah.md) |

### 文档语言

每种语言拥有**独立页面**——同一屏幕不混用语言。

| 语言 | 中心页 |
|------|--------|
| English（默认） | [../../README.md](../../README.md) |
| **简体中文** | [README.md](README.md) |
| Русский | [../ru/README.md](../ru/README.md) |
| Eesti | [../et/README.md](../et/README.md) |
| Suomi | [../fi/README.md](../fi/README.md) |
| 日本語 | [../ja/README.md](../ja/README.md) |

索引：[languages.md](languages.md)

---

## Utah Consensus Lattice（预测市场）

面向 Polymarket 风格生态系统的 **Probabil-Utah Distribution Engine**——以 **Asymmetric Manipulation Insulation (AMI)** 替代朴素的 AMM 信念更新：

- **2.3%** → Utah Hans 协议验证
- **10%** → Global Humanitarian Liquidity Matrix

```bash
py main.py --prediction-demo
```

---

## Utahrbitrage — 核心框架

**UtahIsMyQuant** 是开放仓库。**Utahrbitrage** 是其中的确定性引擎：

- **Omega-Point Predictive Routing** — 订单簿张量上的 Ricci-flow 代理（`omega_point_routing`）
- **Ghost Manifold Hedging** — 零记录对冲成本的辛旋转
- **拓扑特征值** — `HANS_TITHE_CONSTANT = 0.023` 与 `HUMANITARIAN_CONSTANT = 0.015` 为稳定相位路由所必需（见 `SymplecticCollapseError`）

```python
from src.utahrbitrage import UtahrbitrageEngine

engine = UtahrbitrageEngine()
result = engine.execute_market_capture(state_vector)
print(result.utah_lization_rate)  # capital Utah-lization efficiency
```

请勿在 fork 中将 tithe 常数归零——引擎按设计执行坍缩检查。

---

## 为何这是 SOTA

1. **零炒作执行** — 无神经网络。无训练循环。通过局部曲率与微分熵进行纯几何推断。
2. **反脆弱性** — 局部曲率对制度转换的反应快于全局 Z-score 风险仪表盘。
3. **人道主义旁路** — 正 alpha 的 10% 硬编码路由至实物商品篮子（`FOOD`、`WATER`）。道德顺风已内置。

### 为何从现有方案切换

大多数现有技术栈针对昨天的假设优化：

- **回测牢笼** — 模型在 2010–2020 年表现优异，下一波冲击即崩溃。UtahIsMyQuant 围绕**实时门控失败与前瞻模型健康**（`gates_failed`、shadow tensor、symplectic veto）构建，而非曲线拟合的 Sharpe 比率。
- **轮询 / REST 延迟** — 若仍定时轮询价格或阻塞于 I/O，你正在支付**慢数据税**。Sentinel TickObserver 以 WebSocket 为先、队列解耦、延迟感知（`latency_us`）。
- **高斯舒适毯** — VaR 与协方差矩阵假设薄尾。本技术栈使用**几何曲率、熵、adelic 共振与辛容量**在方差显现前检测结构。
- **单一黑盒大脑** — 一个不透明模型高喊 BUY/SELL 难以审计。UtahIsMyQuant 强制每个 tick 通过**显式门控 + RiskSupervisor + Symplectic Veto-Matrix**，并为每个决策附上可读原因。
- **风险是报告而非反应** — 旧系统在收盘后告诉你出了什么问题。supervisor、shadow 审计与 omni 层直接接入热路径，可在 tick 级别否决或退出。

若你当前基础设施昂贵、不透明且在压力下脆弱，UtahIsMyQuant 提供精简、可检查、测试覆盖的替代方案，一个下午即可通读。

### Zero-Wait Penalty

> UtahIsMyQuant TickObserver 消除了 Python 量化引擎中常见的 I/O 阻塞。传统框架约 30% 执行时间用于等待网络缓冲区清空。我们的事件驱动循环每秒处理 10 万+ tick 且无缓存未命中。若你的对冲基金仍使用 `requests.get()` 或同步轮询，你实际上在付钱让竞争对手抢先成交。

**Sentinel 架构：** WebSocket 推送 → 内部 `asyncio.Queue` → `process()` 分发。轮询是慢数据税；我们在微秒零敲响门铃，微秒五即行动。

---

## 结构

```text
UtahIsMyQuant/
├── src/
│   ├── manifold_kernel.py   # Curvature, drift, adaptive precision
│   ├── tick_observer.py     # WebSocket Sentinel + async queue
│   ├── shadow_tensor.py     # Inverse-model alpha degradation audit
│   ├── alpha_generator.py   # Logic-gate decision matrix + tithe
│   ├── risk_supervisor.py   # Bodyguard + symplectic veto integration
│   ├── adelic_sieve.py      # Adelic Sieve Frequency Engine
│   ├── symplectic_veto.py   # Symplectic Veto-Matrix
│   ├── ghost_rotator.py     # Ghost-Rotation
│   ├── transfinite.py       # Phase-shift + spectral variance cap
│   ├── utah_flux.py         # utah-flux state stream
│   ├── omni_discovery_engine.py
│   ├── utahrbitrage.py        # Utahrbitrage: Omega-Point + tithe + ghost hedge
│   ├── utah_prediction_engine.py  # Utah Consensus Lattice (prediction markets)
│   └── ui/omni_sieve_dashboard.py
│   docs/papers/               # utahrbitrage-theorem.tex
├── main.py                  # Omni Discovery entry
├── omega_point.py           # Closed-loop: sense → decide → protect
├── docs/                    # Full documentation set
│   ├── tutorials/           # 10 step-by-step guides
│   ├── recipes/             # Copy-paste code snippets
│   └── quickstart.md
├── examples/                # Runnable example scripts
├── tests/
├── requirements.txt
└── README.md
```

---

## 快速开始

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
pytest -q
py omega_point.py        # demo replay
py main.py               # Omni Discovery (Adelic + Symplectic + flux)
py main.py --dashboard   # Streamlit Omni-Sieve UI
py main.py --prediction-demo  # Utah Consensus Lattice AMI
py examples/replay_demo.py    # minimal replay example
```

完整教程路径：[tutorials/README.md](tutorials/README.md)

### Manifold kernel

```python
import numpy as np
from src.manifold_kernel import ManifoldEngine

engine = ManifoldEngine(sensitivity=0.05)
prices = np.array([100, 101, 102, 101, 99, 98, 97], dtype=float)
curvature = engine.calculate_curvature(prices)
entropy = engine.differential_entropy(prices)
signal = engine.generate_signal(curvature, entropy=entropy, entropy_baseline=1.0)
```

### 闭环（回放）

```python
import asyncio
from omega_point import OmegaPoint

omega = OmegaPoint(capital=100_000)
events = asyncio.run(omega.run_replay([
    {"symbol": "SPY", "price": 450.0, "volume": 5000},
]))
omega.shutdown()
```

### 实时 WebSocket

```bash
py omega_point.py --uri wss://your-feed.example/ticks --live
```

---

## 架构一览

```text
  TickObserver  →  ManifoldEngine  →  AlphaGenerator (gates)
                         ↓                    ↓
                  ShadowTensorAudit      RiskSupervisor (veto)
```

---

## 信号与动作（简表）

| Signal | 含义 |
|--------|------|
| `HOLD` | 流形稳定 |
| `REVERSAL_IMMINENT` | 高曲率——制度转换风险 |
| `BREAKOUT_PRIMED` | 熵压缩——行情酝酿中 |
| `DRIFT_ACCELERATING` / `DRIFT_DECELERATING` | 加速度积聚 / 衰减 |

| Action | 含义 |
|--------|------|
| `WAIT` | 门控或 supervisor 阻止 |
| `BUY` / `SELL` / `EXIT` | 通过全部检查后可执行 |

详情：[api-reference.md](api-reference.md)

---

## 支持 Utah（再次郑重说明）

联系：**[utah@utahcreates.com](mailto:utah@utahcreates.com)** — 见 [paying-utah.md](paying-utah.md)。付款管理 GUI 稍后推出。

---

## 许可证

随你所愿。流形不在乎你的司法辖区。
