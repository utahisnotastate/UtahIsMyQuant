# Tutorial 03: Manifold Signals Only

## Goal

Use **ManifoldEngine** without trading logic — understand curvature, entropy, adelic signals.

## Recipe

See [../recipes/manifold.md](../recipes/manifold.md).

## Exercise

1. Flat prices → curvature ≈ 0  
2. Spike then crash → `REVERSAL_IMMINENT` likely  
3. Flat volume + flat prices → `ADELIC_VOID` possible  

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

## Next

[Tutorial 04: Logic gates and alpha](04-logic-gates-and-alpha.md)
