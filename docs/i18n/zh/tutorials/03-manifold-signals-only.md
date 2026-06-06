# 教程 03：仅流形信号

## 目标

在不使用交易逻辑的情况下使用 **ManifoldEngine**——理解曲率、熵、adelic 信号。

## 配方

见 [../recipes/manifold.md](../recipes/manifold.md)。

## 练习

1. 平坦价格 → 曲率 ≈ 0
2. 冲高后暴跌 → 可能出现 `REVERSAL_IMMINENT`
3. 平坦成交量 + 平坦价格 → 可能出现 `ADELIC_VOID`

```python
import numpy as np
from src.manifold_kernel import ManifoldEngine

engine = ManifoldEngine(sensitivity=0.01)
flat = np.ones(40) * 100
spike = np.concatenate([np.linspace(100, 110, 20), np.linspace(110, 90, 20)])

for name, p in [("flat", flat), ("spike", spike)]:
    c = engine.calculate_curvature(p)
    sig = engine.generate_signal(c)
    print(name, "curvature", c, "signal", sig)
```

## 下一步

[教程 04：逻辑门控与 alpha](04-logic-gates-and-alpha.md)
