# Учебник 03: Только сигналы manifold

## Цель

Использовать **ManifoldEngine** без торговой логики — понять кривизну, энтропию, adelic-сигналы.

## Рецепт

См. [../recipes/manifold.md](../recipes/manifold.md).

## Упражнение

1. Плоские цены → curvature ≈ 0  
2. Спайк затем обвал → вероятен `REVERSAL_IMMINENT`  
3. Плоский объём + плоские цены → возможен `ADELIC_VOID`  

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

## Далее

[Учебник 04: Логические ворота и alpha](04-logic-gates-and-alpha.md)
