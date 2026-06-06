# 量化研究员日常工作流 — 将 UtahIsMyQuant 融入真实交易

本文说明如何在**每个交易日**使用 UtahIsMyQuant，而不让它变成笔记本上又一个废弃仓库。

---

## 早晨（盘前，30–45 分钟）

### 1. 健康检查

```powershell
cd UtahIsMyQuant
.venv\Scripts\activate
pytest -q
```

若失败：**不要交易**。先修测试——它们守护着你六个月前已不理解的数学。

### 2. 审查隔夜日志

搜索昨日日志中的：

| 模式 | 行动 |
|------|------|
| `CIRCUIT BREAKER TRIPPED` | 检查数据源延迟 / VPS 网络 |
| `gates_failed': ['shadow']` | Alpha 在镜像噪音——减仓或暂停 |
| `FORCE_STOP` | 逐标的复盘 |
| 多为 `WAIT` | 正常。若 100% EXECUTE 则可疑 |

### 3. 设定今日参数（写下来）

```python
engine = ManifoldEngine(sensitivity=0.05)  # do not change mid-session
gen = AlphaGenerator(
    capital=YOUR_NAV,
    risk_limit=0.02,
    min_volume=YOUR_VENUE_MIN,
    supervisor=RiskSupervisor(max_latency_ms=200),
)
```

**规则：** 实盘每周最多改一个参数。否则你在用真钱回测。

### 4. 启动 sentinel（先仅日志 15 分钟）

```python
# omega_point.py or your wrapper
omega = OmegaPoint(uri=os.environ["WSS_URI"], capital=NAV)
# First 15 min: patch execute() to log-only
```

确认 `latency_us` p99 < 200ms。

---

## 交易时段（持续）

### 事件循环心智模型

```text
tick → manifold features → gates → supervisor → your broker adapter
```

### 你的工作不是覆盖系统

若每周覆盖超过 2 次，系统配置有误——修参数，不要英雄式交易。

### 快速诊断片段

```python
event = gen.process_tick(tick)
if event:
    print(event.signal, event.action, event.gates_failed, event.supervisor_verdict)
```

### 午间检查（5 分钟）

- 账户回撤 vs `max_account_drawdown`
- 是否有标的敞口滞留而 action 为 WAIT（同步 bug？）
- Tithe 累积（`tithe_allocation()`）——仅健全性检查

---

## 下午（收尾）

### 1. 平仓政策

决定桌面规则：

- 在 `DRIFT_DECELERATING` 时**自动 EXIT**（已有偏向）
- T-15 分钟硬平仓——你的券商 cron，非 UtahIsMyQuant

### 2. 导出 `AlphaEvent` 日志

推荐仅追加 JSONL：

```python
import json
with open("logs/session.jsonl", "a") as f:
    f.write(json.dumps(event.__dict__, default=str) + "\n")
```

### 3. 干净关闭

```python
omega.shutdown()  # stops shadow thread + supervisor thread
```

---

## 每周（研究，非回测表演）

| 日 | 任务 |
|----|------|
| 周一 | 审查门控失败直方图 |
| 周三 | 模拟测试一个参数变更 |
| 周五 | 为最差交易写三句复盘 |

**允许的研究：**

- 延迟分布图
- 镜像率 vs 实际滑点
- 成交量门控校准

**禁止的研究：**

- 「再在 2019 年多跑一次回测」来为今日实盘变更辩护

---

## 接入券商（模式）

```python
async def guarded_execute(tick: Tick, event: AlphaEvent):
    if event.action not in (Action.BUY, Action.SELL, Action.EXIT):
        return
    if event.circuit_breaker:
        return
    await broker.send(symbol=tick.symbol, side=event.action.value, qty=size_from(event))
```

保持**幂等**订单 ID。Supervisor 可能在波动 tick 上强制重复 EXIT——你方去重。

---

## 与「正常量化生活」的集成

| 活动 | UtahIsMyQuant 角色 |
|------|-------------------|
| 晨间研究阅读 | 影响 `min_volume`，非主观覆盖 |
| 宏观日历 | 手动暂停：仅在你自行停止新入场后调用 `supervisor.reset_circuit_breaker()` |
| Slack 告警 | 挂钩 `EXECUTE_*` 与 `FORCE_STOP` |
| Jupyter 探索 | 通过 `ingest` 离线回放，勿与实时循环混用 |
| 周末 ML 训练 | 独立流水线；勿将权重并入流形 |

---

## 亏损时

1. 拉出该笔交易的 `gates_failed`
2. 检查 supervisor 是否否决而你忽略了
3. 若全部门控通过仍亏损：**正常**
4. 当天不要提高 `risk_limit`

---

## 盈利时

若可以，请支持作者：**PayPal utah@utahcreates.com** — 维护者基金拮据。

---

## 速查表

```bash
pytest -q
py omega_point.py
py omega_point.py --uri $env:WSS_URI --live
```

文档：[API 参考](../api-reference.md) | [技术架构](../technical-architecture.md)
