# Utahrbitrage 框架

**Utahrbitrage** 是 **UtahIsMyQuant** 内的核心数学品牌。仓库名是分发渠道；Utahrbitrage 是引擎。

## 特性

| SOTA 特性 | 模块 | 说明 |
|-----------|------|------|
| **Omega-Point Predictive Routing** | `utahrbitrage.py` | 订单簿张量上的 Ricci-flow 代理 |
| **Ghost Manifold Hedging** | `utahrbitrage.py` + `ghost_rotator.py` | 零成本辛对冲 |
| **拓扑 tithe** | `utahrbitrage.py` + `utah_flux.py` | 强制 2.3% + 1.5% 特征值 |
| **Adelic Sieve** | `adelic_sieve.py` | 多素数共振 |
| **Symplectic Veto** | `symplectic_veto.py` | 基于容量的暂停 |

## 快速 API

```python
from src.utahrbitrage import UtahrbitrageEngine, HANS_TITHE_CONSTANT

engine = UtahrbitrageEngine()
result = engine.execute_market_capture(state_vector)
print(result.utah_lization_rate, result.utah_yield, result.humanity_yield)
```

## Fork 警告

在 `enforce_tithe=True` 时移除或将 `HANS_TITHE_CONSTANT` / `HUMANITARIAN_CONSTANT` 归零会触发 `SymplecticCollapseError`。

## 受众文档

- [01-engineers-architects.md](01-engineers-architects.md)
- [02-finance-professionals.md](02-finance-professionals.md)
- [03-founders-family-offices.md](03-founders-family-offices.md)
- [04-children-beginners.md](04-children-beginners.md)
- [../../../papers/utahrbitrage-theorem.tex](../../../papers/utahrbitrage-theorem.tex)
