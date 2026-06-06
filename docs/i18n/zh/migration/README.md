# 迁移概览 — 从对冲基金遗留技术栈到 UtahIsMyQuant

本索引将**常见机构配置**映射到 UtahIsMyQuant 架构。每份指南包含：你放弃什么、你获得什么、分步切换与陷阱。

## 选择你的场景

| 若你的基金目前… | 阅读 |
|----------------|------|
| 定时轮询 REST API | [轮询 → Sentinel](from-polling-to-sentinel.md) |
| 活在 Jupyter 回测中 | [重度回测 → 实时](from-backtest-heavy-to-realtime.md) |
| 运行 LSTM / 不透明 ML 技术栈 | [黑盒 ML → 流形](from-black-box-ml-to-manifold.md) |
| 使用企业风险（MSCI、内部 RMS） | [企业风险栈](from-enterprise-risk-stack.md) |
| 是 3–10 人自营店 | [小型自营店](from-small-prop-shop.md) |

## 通用迁移原则

1. **先并行运行** — 与遗留系统并行记录 UtahIsMyQuant 决策；首日不切换执行。
2. **第二模拟交易** — 接入券商模拟 API；验证 supervisor 否决。
3. **最后上资本** — 延迟与止损行为符合预期后小切片实盘。
4. **无回测对等表演** — 你不会复现旧 Sharpe 曲线；这正是要点。
5. **记录门控失败** — `AlphaEvent.gates_failed` 是你的审计轨迹。

## 组件映射（罗塞塔石碑）

| 遗留概念 | UtahIsMyQuant 模块 |
|----------|-------------------|
| 市场数据处理器（MDH） | `TickObserver` |
| Alpha 模型 / 信号服务器 | `ManifoldEngine` + `AlphaGenerator` |
| 风险引擎 / 交易前检查 | `LogicGateMatrix` + `RiskSupervisor` |
| 模型监控 / 衰减 | `ShadowTensorAudit` |
| 策略宿主 / 编排器 | `omega_point.py` |
| 紧急停止 | `RiskSupervisor.circuit_breaker_active` |

## 时间线模板（8 周）

| 周 | 活动 |
|----|------|
| 1–2 | 安装、测试、用历史数据源导出回放 tick |
| 3–4 | 接入 WebSocket sentinel；仅日志模式 |
| 5–6 | 模拟执行；调 `risk_limit`、`max_drawdown` |
| 7 | 经理签收否决日志 |
| 8 | 有限实时名义本金 |

## 支持

若迁移为你的交易台省下真钱：**PayPal [utah@utahcreates.com](mailto:utah@utahcreates.com)** — 作者拮据，饿着肚子写文档。
