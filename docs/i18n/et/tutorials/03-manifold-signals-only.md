# Õpetus 03: Ainult manifold signaalid

## Eesmärk

Kasuta **ManifoldEngine** ilma kauplemisloogikata — mõista curvature, entropy, adelic signaale.

## Retsept

Vaata [../recipes/manifold.md](../recipes/manifold.md).

## Harjutus

1. Lamedad hinnad → curvature ≈ 0
2. Spike siis crash → tõenäoliselt `REVERSAL_IMMINENT`
3. Lame maht + lamedad hinnad → võimalik `ADELIC_VOID`

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

## Edasi

[Õpetus 04: Loogikaväravad ja alfa](04-logic-gates-and-alpha.md)
