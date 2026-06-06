# 迁移：重度回测文化 → 实时流形稳定性

## 你属于这里若…

- 研究负责人以样本内 Sharpe 衡量成功
- 生产模型 ≠ 回测模型（经典问题）
- 日历上有「每月重新优化」

## 文化冲击（有意设计）

**UtahIsMyQuant 不提供回测框架。**

这不是缺失功能——是设计声明：

> 拟合历史就是拟合你的自负。我们交易*当下*的几何。

量化研究员会抵触。经理会要求「2020 年的一张图」。准备回答：

1. **Shadow tensor** 是前瞻模型健康，非向后 PnL
2. **门控失败日志** 是你的新研究数据集
3. **模拟交易** 是你的「样本外」

## 回测的替代

| 旧仪式 | 新仪式 |
|--------|--------|
| 滚动前向网格搜索 | 仅在实盘模拟上调 `sensitivity`、`risk_limit` |
| 10 年 Sharpe | 监视 `degradation_score`、circuit breaker 触发 |
| 仿真中的滑点模型 | 测量 `latency_us` + 模拟中实际滑点 |
| 研究笔记本 → 生产 | `omega_point.py` 是生产骨架 |

## 切换步骤

### 阶段 A — 影子模式（无执行）

```python
gen = AlphaGenerator(enable_shadow_audit=True)
# Log every AlphaEvent.decision for 2–4 weeks
```

构建仪表盘：按门控名统计 `gates_failed`。

### 阶段 B — 模拟执行

仅当 `supervisor_verdict == "CLEAR"` 时将券商模拟 API 接入 `AlphaEvent.action`。

### 阶段 C — 实时微名义本金

按宣言门控上限为 `risk_limit * capital`。

## 旧指标到新指标的映射

| 回测指标 | 实时代理 |
|----------|----------|
| 最大回撤 | `RiskSupervisor.account_drawdown()` |
| 命中率 | 正 `pnl_delta` 事件比率 |
| 换手率 | 每 session `EXECUTE_*` 计数 |
| Alpha 衰减 | `ShadowTensorAudit.degradation_score` |

## 陷阱

- **要求对等** — 旧策略不会 1:1 映射到流形信号
- **在一周波动上过度调 sensitivity** — 至少冻结 20 个 session
- **忽视 WAIT** — 大多数 tick 应 WAIT；这是纪律

## 经理谈话要点

见 [对冲基金经理指南](../guides/hedge-fund-manager.md) 中「面对回测异议」一节。

## 下一步

- [黑盒 ML → 流形](from-black-box-ml-to-manifold.md)
