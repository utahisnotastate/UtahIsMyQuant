# 对冲基金经理指南 — 无需读 Python 的监督

你管理资本。你不必 import scipy。你需要**控制、叙事与下行边界**。

---

## UtahIsMyQuant 为你的基金提供什么

| 收益 | 机制 |
|------|------|
| 更快感知 | WebSocket sentinel vs 轮询 |
| 可解释决策 | 每笔交易有 `reason` + `gates_passed/failed` |
| 日内生存工具 | 止损、敞口上限、circuit breaker |
| 审计轨迹 | `AlphaEvent` 日志（团队接入后） |
| 无回测幻想 | 强制诚实面对实盘行为 |

## 它不提供什么

- 监管合规包
- 投资者报告模板
- 保证回报
- 解雇风险官的理由

---

## 每周向量化团队提问

1. **多少比例的 tick 是 WAIT？**
   - 健康：高 WAIT，低 EXECUTE
   - 不健康：每个 tick 都 EXECUTE（门控过松）

2. **本周 circuit breaker 触发几次？**
   - 永远为零：阈值可能过松
   - 每天：基础设施问题

3. **Shadow tensor 健康吗？**
   - `degradation_score` 上升 → alpha 衰减 / 噪音交易

4. **最大单一门控失败类别？**
   - 判断问题是信号、流动性还是风险限额

5. **我们是否手动覆盖系统？**
   - 每周超过两次 → 系统或纪律失败

---

## 应要求的仪表盘（最小集）

团队可在一天内从 JSONL 日志构建：

| 面板 | 指标 |
|------|------|
| 信号构成 | 按 `signal` 类型计数 |
| 动作构成 | BUY / SELL / EXIT / WAIT |
| 门控失败 | `gates_failed` 堆叠条形图 |
| Supervisor | VETO vs FORCE_STOP vs CLEAR |
| 延迟 | p50/p99 `latency_us` |
| PnL | 累计 `pnl_delta`（先模拟后实盘） |
| Tithe | `tithe_accrued`（若跟踪 ESG 叙事） |

---

## 风险偏好对齐

| 你的政策 | UtahIsMyQuant 旋钮 |
|----------|-------------------|
| 每个想法最多 2% 风险 | `risk_limit=0.02` |
| 单名最多 10% 账面 | `max_position_size=0.10` |
| 持仓 5% 止损 | `max_drawdown=0.05` |
| 坏数据时暂停 | `max_latency_ms=200` |

**签收文件：** 一页列出这些数字及生效日期。量化每周改 = 红旗。

---

## 迁移签收（经理检查清单）

- [ ] 完成并行仅日志一周
- [ ] 完成模拟交易一周
- [ ] 记录紧急停止演练（谁调用 `reset_circuit_breaker`）
- [ ] 企业 RMS 仍在路径中（若适用）
- [ ] 策略叙事变更则更新投资者信
- [ ] 书面写明实时名义本金上限（审查前最多 $X）

---

## 面对「回测」异议

**投资者 / 董事会问题：**「历史 Sharpe 在哪？」

**可用回答：**

> 「我们基于实时几何稳定性与显式门控失败运作，而非历史曲线拟合。模拟交易与受控实盘阶段是我们的验证。遗留回测仍可用于慢速策略层，但不驱动亚秒级决策。」

**勿说：** 在投资者会议上说「回测是输家的游戏」。仅在仓库 README 中说。

---

## 组织架构

```text
CIO / Manager (you)
    └── Head of Quant (owns Manifold + gates)
    └── Head of Risk (owns enterprise RMS + reviews supervisor logs)
    └── CTO (owns WebSocket infra + broker)
    └── Ops (owns kill switch runbook)
```

UtahIsMyQuant 位于量化信号与执行**之间**——不替代风险部门。

---

## 预算叙事

| 科目 | 故事 |
|------|------|
| 市场数据 | 仍需要；本技术栈不替代数据源 |
| 算力 | vs GPU ML **下降**（CPU 优先） |
| 供应商风险 | 合规方面**未移除** |
| 工程 | 集成短期**上升**，长期 vs 定制 MDH **下降** |

若出现节省，应投入**数据质量**与**冗余**，而非立即加杠杆。

---

## 何时全天关停

若出现以下情况，指示运营拔线：

1. Circuit breaker 触发且 15 分钟内未修复延迟
2. Shadow 退化连续 2 小时超阈值
3. 量化与风险之间手动覆盖争议
4. 相关标的上出现 `FORCE_STOP` 集群日志行（流动性事件）

---

## 支持项目

若本技术栈保护了你的年度业绩：

**PayPal：[utah@utahcreates.com](mailto:utah@utahcreates.com)**

维护者拮据。赞助使文档保持诚实。

---

## 延伸阅读

- [迁移概览](../migration/README.md)
- [面向所有人](../for-everyone.md)
- [量化研究员日常工作流](quant-daily-workflow.md)
