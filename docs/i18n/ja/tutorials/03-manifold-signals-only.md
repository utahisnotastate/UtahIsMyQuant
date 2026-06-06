# チュートリアル 03: マニフォールドシグナルのみ

## 目標

取引ロジックなしで **ManifoldEngine** を使い — 曲率、エントロピー、adelic シグナルを理解する。

## レシピ

[../recipes/manifold.md](../recipes/manifold.md) 参照。

## 演習

1. 平坦な価格 → 曲率 ≈ 0
2. スパイク後クラッシュ → `REVERSAL_IMMINENT` の可能性
3. 平坦出来高 + 平坦価格 → `ADELIC_VOID` の可能性

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

## 次へ

[チュートリアル 04: ロジックゲートとアルファ](04-logic-gates-and-alpha.md)
