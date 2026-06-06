# UtahIsMyQuant — 文档

欢迎阅读完整文档集。请选择与**今天的你**相匹配的指南——而非 LinkedIn 上的你。

## 从这里开始

| 受众 | 文档 | 你将获得 |
|------|------|----------|
| **新用户（10 分钟）** | [快速入门](quickstart.md) | 安装、测试、首次演示 |
| **教程与配方** | [tutorials/README.md](tutorials/README.md) | 分步指南 + 可复制粘贴代码 |
| **支持 Utah** | [paying-utah.md](paying-utah.md) | 邮件联系 Utah；GUI 应用规划中 |
| **概览（安装、运行）** | [project-overview.md](project-overview.md) | 安装、运行、法律声明 |
| **语言（独立页面）** | [languages.md](languages.md) | English · Русский · Eesti · Suomi · 日本語 · 简体中文 |
| **术语表** | [GLOSSARY.md](GLOSSARY.md) | 术语与缩写 |
| **儿童与好奇者** | [儿童版](for-kids.md) | 故事化讲解，无行话 |
| **非技术用户** | [面向所有人](for-everyone.md) | 无需数学背景即可理解 |
| **工程师与量化研究员** | [技术架构](technical-architecture.md) | 模块、数据流、参数 |
| **API 用户** | [API 参考](api-reference.md) | 类、方法、返回值结构 |
| **Omni / TAD / Symplectic** | [Omni 架构](omni-architecture.md) | Adelic sieve、veto-matrix、flux |
| **Utahrbitrage 框架** | [Utahrbitrage](utahrbitrage.md) | Omega-Point 路由、tithe 常数、ghost hedge |
| **预测市场（Polymarket 风格）** | [预测市场集成](prediction_market_integration.md) | Utah Consensus Lattice + AMI |

## Golden Master 指南（按角色）

| # | 受众 | 文档 |
|---|------|------|
| 01 | 工程师与架构师 | [01-engineers-architects.md](01-engineers-architects.md) |
| 02 | 金融专业人士与量化研究员 | [02-finance-professionals.md](02-finance-professionals.md) |
| 03 | 创始人与家族办公室 | [03-founders-family-offices.md](03-founders-family-offices.md) |
| 04 | 儿童与初学者 | [04-children-beginners.md](04-children-beginners.md) |

**基础证明（LaTeX）：** [../../../papers/utahrbitrage-theorem.tex](../../../papers/utahrbitrage-theorem.tex)

## 从传统对冲基金技术栈迁移

摆脱数十亿美元规模的习惯并不容易。以下手册将常见旧体系映射到 UtahIsMyQuant 架构：

| 场景 | 指南 |
|------|------|
| 轮询 / REST / 慢速数据 | [从轮询到 Sentinel](migration/from-polling-to-sentinel.md) |
| 回测为主 / 过拟合文化 | [从重度回测到实时](migration/from-backtest-heavy-to-realtime.md) |
| 黑盒 ML / LSTM 动物园 | [从黑盒 ML 到流形](migration/from-black-box-ml-to-manifold.md) |
| 企业级风险与合规栈 | [从企业风险栈](migration/from-enterprise-risk-stack.md) |
| 小型自营店 / 精益团队 | [从小型自营店](migration/from-small-prop-shop.md) |
| **迁移索引** | [迁移概览](migration/README.md) |

## 基于角色的指南

| 角色 | 指南 |
|------|------|
| **量化研究员（日常集成）** | [量化研究员日常工作流](guides/quant-daily-workflow.md) |
| **对冲基金经理** | [经理指南](guides/hedge-fund-manager.md) |
| **指南索引** | [指南概览](guides/README.md) |

## 快捷命令

```bash
pip install -r requirements.txt
pytest -q
py examples/replay_demo.py           # minimal replay
py omega_point.py                    # full omega replay
py main.py                           # Omni + Utahrbitrage
py main.py --prediction-demo         # prediction AMI
py main.py --dashboard               # Streamlit UI
py omega_point.py --uri wss://... --live
```

## 教程（学习路径）

| # | 教程 |
|---|------|
| 01 | [安装与验证](tutorials/01-install-and-verify.md) |
| 02 | [首个回放流水线](tutorials/02-first-replay-pipeline.md) |
| 03–10 | [完整索引](tutorials/README.md) |

## 代码配方

[recipes/README.md](recipes/README.md) — 流形、alpha、Utahrbitrage、prediction lattice 的可复制粘贴片段。

## 文档地图（可视化）

```text
                    ┌─────────────────┐
                    │ project-overview│
                    │  (支持 + 运行)  │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
   for-kids.md        for-everyone.md    technical-architecture.md
         │                   │                   │
         └───────────────────┴───────────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        migration/*     guides/*      api-reference.md
```

## 支持 Utah

若本技术栈在生产中对你有所帮助，请发送邮件至 **[utah@utahcreates.com](mailto:utah@utahcreates.com)**。详情见 [paying-utah.md](paying-utah.md)。用于管理付款的桌面 GUI 应用正在规划中。

## 翻译

| 语言 | 中心页 |
|------|--------|
| English | [../../README.md](../../README.md) |
| **简体中文** | [README.md](README.md) |
| Русский | [../ru/README.md](../ru/README.md) |
| Eesti | [../et/README.md](../et/README.md) |
| Suomi | [../fi/README.md](../fi/README.md) |
| 日本語 | [../ja/README.md](../ja/README.md) |

完整索引：[languages.md](languages.md)。

*流形不提供税务、法律或职业建议。它提供曲率。*
