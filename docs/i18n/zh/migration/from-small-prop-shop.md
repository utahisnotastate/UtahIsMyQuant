# 迁移：小型自营店（3–10 人）→ UtahIsMyQuant

## 你属于这里若…

- 一个量化、一个开发、一个身兼两职的创始人
- 某处仍用 Excel
- 「风险」= 交易员脑中的仓位大小

## 为何这是最佳匹配

UtahIsMyQuant **精简**：Python、numpy、asyncio，v1 无需 K8s 清单。

| 资源 | 需求 |
|------|------|
| 硬件 | 一台像样的机器或小 VM |
| 数据 | 你已付费的一个 WebSocket 数据源 |
| 团队时间 | 约 2 周回放，约 4 周模拟 |

## 最小可行交易台

```text
Trader laptop / VPS
  └── py omega_point.py --uri wss://feed --live
  └── logs → ./logs/events.jsonl  (you add 20 lines)
  └── broker paper API (you wire)
```

## 逐周计划

| 周 | 交付物 |
|----|--------|
| 1 | `pytest -q` 通过；CSV 供应商 tick → `ingest` 回放 |
| 2 | 实时 sentinel 仅日志；EXECUTE_* Slack 告警 |
| 3 | 模拟订单；日 PnL vs 手动电子表 |
| 4 | 去/留：每 `risk_limit` 最多 1–2% NAV |

## 角色（谁做什么）

| 人 | 任务 |
|----|------|
| 量化 | 调 `sensitivity`，解读信号 |
| 开发 | WebSocket + 券商适配器 |
| 创始人 | 读 [经理指南](../guides/hedge-fund-manager.md)，设定资本上限 |

## 暂勿构建

- 定制 Kubernetes operator
- 14 个策略分支
- Bloomberg 替代

## 成本对比（粗略）

| 项目 | 传统自营峰值 | UtahIsMyQuant |
|------|-------------|---------------|
| MD 平台 | $2k–30k/月 | 仅你的数据源 |
| GPU 训练 | $500+/月 | 默认 $0 |
| 风险供应商 | $5k+/月 | 仓库内 supervisor |

节省应投入**数据质量**与**若盈利则支持作者**：utah@utahcreates.com。

## 陷阱

- 在陈旧时间戳上测试 supervisor 前即实盘
- 一人休假无 `shutdown()` 运行手册

## 下一步

- [量化研究员日常工作流](../guides/quant-daily-workflow.md)
