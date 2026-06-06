# Opetusohjelma 03: Vain monistosignaalit

## Tavoite

Käytä **ManifoldEngine**-moottoria ilman kauppalogiikkaa — ymmärrä curvature, entropy ja adelic-signaalit.

## Resepti

Katso [../recipes/manifold.md](../recipes/manifold.md).

## Harjoitus

1. Tasaiset hinnat → curvature ≈ 0
2. Piikki sitten romahdus → todennäköisesti `REVERSAL_IMMINENT`
3. Tasainen volume + tasaiset hinnat → mahdollinen `ADELIC_VOID`

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

## Seuraavaksi

[Opetusohjelma 04: Logic gateet ja alpha](04-logic-gates-and-alpha.md)
