# 教程 07：预测市场 AMI

## 目标

将 **Utah Consensus Lattice** 用于 Polymarket 风格反巨鲸绝缘。

## 演示 CLI

```bash
py main.py --prediction-demo
```

比较巨鲸与散户日志行。

## 配方

[../recipes/prediction-lattice.md](../recipes/prediction-lattice.md)

## 映射到 Polymarket（概念）

1. 从订单簿 delta 向量构建 `capital_flux_tensor`
2. 根据价差/深度设置 `market_impact_factor`
3. `protected_delta` → 发布前允许的最大概率偏移
4. 记录 `yield_ledger` 用于协议提取审计

完整指南：[../prediction_market_integration.md](../prediction_market_integration.md)

## 下一步

[教程 08：实时 WebSocket 数据源](08-live-websocket-feed.md)
