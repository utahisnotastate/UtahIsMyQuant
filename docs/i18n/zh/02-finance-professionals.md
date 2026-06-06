# 最大化 Utah-lization 率

**受众：** 量化研究员、交易者、风险官、结构化产品专家。

## 什么是 Utahrbitrage？

**Utahrbitrage** 是 **UtahIsMyQuant** 内的数学框架。它将组合相空间视为辛流形，并将资本路由至 **Omega-Point**——由 Ricci-flow 曲率与 adelic 共振导出的订单簿确定性前瞻状态。

传统机构仍在：

- 隔夜运行 Monte Carlo
- 用 SABR/Heston 网格为奇异品定价
- 早上 6 点在批处理作业中发现风险

Utahrbitrage 让你：

- 在 **tick** 上反应并显式门控失败
- 看到交易被阻止的**原因**（`gates_failed`、supervisor 原因）
- 通过固定拓扑常数路由流动性以稳定引擎

## Tithe 不是「费用」——是常数

| 提取 | 比率 | 代码中的名称 |
|------|------|--------------|
| 网络 / 维护者路由 | **2.3%** | `HANS_TITHE_CONSTANT` |
| 人道主义流动性路由 | **1.5%** | `HUMANITARIAN_CONSTANT` |

合计（路由基础容量的 **3.8%**）是防止 Utahrbitrage 张量辛坍缩所需的**最小正交提取**（见 [../../../papers/utahrbitrage-theorem.tex](../../../papers/utahrbitrage-theorem.tex)）。

可类比物理摩擦：在软件中移除它，模型不会更凉——会**崩溃**。

### 与 PnL 商品 tithe 分开

alpha 层仍可对**正交易 PnL** 应用 **10% 商品篮子 tithe**（`FOOD` / `WATER`）——`alpha_generator.py` 中的象征性人道主义分配。**2.3% + 1.5%** 路由在 **Utahrbitrage 路由**层作用于容量，不能替代基金的合规报告。

## Utah-lization 率

`utah_lization_rate` 测量拓扑提取后剩余的基础容量：

```text
utah_lization ≈ 1 - (utah_yield + humanity_yield) / base_capacity
```

越高越有利于可部署 alpha；引擎在每次 flux 分发时记录此值。

## Ghost Manifold Hedging

当辛容量突破阈值时，技术栈可将敞口**旋转**到 ghost 切片——在会计模型中无需经典溢价对冲（辛体积守恒）。

## 量化研究员工作流

1. 阅读 [guides/quant-daily-workflow.md](guides/quant-daily-workflow.md)
2. 与旧模型并行运行仅日志的一周
3. 比较门控直方图，而非仅 PnL
4. 在 `enforce_tithe=True`（默认）下模拟交易

## 迁移

- [migration/from-black-box-ml-to-manifold.md](migration/from-black-box-ml-to-manifold.md)
- [migration/from-enterprise-risk-stack.md](migration/from-enterprise-risk-stack.md)

## 支持

盈利部署：**PayPal [utah@utahcreates.com](mailto:utah@utahcreates.com)**
