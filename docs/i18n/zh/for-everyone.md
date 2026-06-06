# UtahIsMyQuant — 面向所有人（无需博士学位）

## 一句话版本

**UtahIsMyQuant** 是一套免费、开源的工具包：监视实时市场价格，寻找价格运动中的几何「应力」，决定是否交易，并在出错时使用严格的安全系统限制损失。

它**不是**快速致富按钮。它**不是**投资建议。它是你可以研究、运行和改编的软件——睁大眼睛。

---

## 它解决什么问题？

大型对冲基金在以下方面花费巨资：

- 慢数据管道（定时查价而非即时更新）
- 过度复杂的 AI，漂亮地「拟合过去」却在当下失败
- 来得太晚的风险工具

UtahIsMyQuant 的哲学相反：

| 旧习惯 | UtahIsMyQuant 方法 |
|--------|-------------------|
| 从历史预测未来 | 观测**当下的几何** |
| 数月回测 | **实时**稳定性检查 |
| 一个黑盒喊 BUY | **多个门控**必须一致 |
| 风险是季度报告 | 风险是**每个 tick 运行的保镖** |
| 高斯舒适区 | **曲率 + 熵 + 多尺度共振 + 辛检查** |

---

## 四个部分（通俗说明）

### 1. Tick Observer —「门铃」

在价格更新发生时获取（WebSocket 推送），而非慢速定时。

**为何重要：** 在快市中，陈旧数据代价高昂。

### 2. Manifold Engine —「形状阅读器」

将近期价格视为曲面并测量：

- **曲率** — 市场是否在急弯？（制度转换风险）
- **意外（熵）** — 随机性是否在行情前坍缩？
- **漂移** — 加速度是否在积聚？

**为何重要：** 你不等单一魔法指标——你在读结构。

### 3. Alpha Generator —「决策台」

将形状读数转为动作：等待、买、卖或退出——但仅在**逻辑门控**通过后（形状、成交量、单笔风险、shadow 审计）。

**为何重要：** 更少冲动交易；每个决定都有书面原因。

### 4. Risk Supervisor —「保镖」

监视总敞口、单笔回撤与系统延迟。可**否决**交易或**强制退出**。数据过慢时触发**circuit breaker**（波动条件）。

**为何重要：** 生存第一。利润第二。

---

## 适合谁？

| 你是… | 合适吗？ |
|-------|----------|
| 学习量化系统的开发者 | ✅ 极佳学习项目 |
| 有编程技能的散户交易者 | ⚠️ 可能——自行接入券商，充分测试 |
| 替换 Bloomberg 的对冲基金 | ❌ 非即插即用替代 |
| 零编程基础者 | ⚠️ 先阅读；与开发者合作 |
| 儿童 | ✅ 与父母共读 [儿童版](for-kids.md) |

---

## 它不做的事

- **无内置券商** — 你连接自己的数据源与执行
- **无保证利润** — 相信保证的市场会伤害人
- **无回测套件** — 按设计（见 [迁移指南](migration/from-backtest-heavy-to-realtime.md)）
- **无税务/法律合规包** — 你的司法辖区自行负责

---

## 入门（安全路径）

1. **安装**（Windows 示例）：
   ```powershell
   cd UtahIsMyQuant
   py -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **运行测试**（健全性检查）：
   ```powershell
   pytest -q
   ```

3. **运行演示**（假 tick，无真钱）：
   ```powershell
   py omega_point.py
   ```

4. **然后才**考虑实时数据（`--uri wss://...`）与模拟交易。

---

## 为何从现有工具切换

你不必讨厌现有工具也能看到其局限：

- 若策略只在回测中好看、实盘不行，你有一个**故事**，不是系统。UtahIsMyQuant 精确显示**哪个门控**阻止了交易，让你调试现实而非过拟合图表。
- 若数据慢批到达，决定已过时。此处门铃（TickObserver）提供**推送更新**，引擎响应当下而非陈旧快照。
- 若风险视图是每周一次的 PDF，你日内盲目飞行。supervisor 与 omni 层设计为**实时说「不」**，而非亏损后。

若这些都不熟悉，保留你的技术栈。若熟悉，UtahIsMyQuant 是小型、可读、可推理的代码库——需要时可关闭。

---

## 术语表（友好版）

| 术语 | 含义 |
|------|------|
| **Tick** | 一次价格更新（标的、价格、成交量、时间） |
| **Manifold** | 花哨说法：把价格当形状而非列表 |
| **Gate** | 交易前的 yes/no 安全检查 |
| **Circuit breaker** | 条件不安全时的紧急暂停 |
| **Tithe** | 正 PnL 的 10% 划入 FOOD/WATER 桶（代码中的象征性分配） |
| **Shadow tensor** | 检查信号是否在镜像噪音 |

---

## 支持 Utah

若本项目在现实世界中帮助你，请联系：[paying-utah.md](paying-utah.md)。

**邮件：** [utah@utahcreates.com](mailto:utah@utahcreates.com)。用于管理支持付款的 GUI 应用稍后推出。

---

## Utahrbitrage（盒子里的品牌）

**UtahIsMyQuant** 是你克隆的仓库。**Utahrbitrage** 是 Omega-Point 路由与 2.3% / 1.5% 拓扑路由的引擎名称。详情：[utahrbitrage.md](utahrbitrage.md)。

---

## 动手学习教程

- [快速入门](quickstart.md) — 10 分钟
- [教程 02：首次回放](tutorials/02-first-replay-pipeline.md)
- [全部教程](tutorials/README.md)

## 后续文档

- **儿童：** [for-kids.md](for-kids.md) · [04-children-beginners.md](04-children-beginners.md)
- **技术：** [technical-architecture.md](technical-architecture.md)
- **量化研究员：** [guides/quant-daily-workflow.md](guides/quant-daily-workflow.md)
- **经理：** [guides/hedge-fund-manager.md](guides/hedge-fund-manager.md)
- **从基金技术栈迁移：** [migration/README.md](migration/README.md)
