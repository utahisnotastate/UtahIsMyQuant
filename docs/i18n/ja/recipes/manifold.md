# レシピ: Manifold Engine

```python
import numpy as np
from src.manifold_kernel import ManifoldEngine

engine = ManifoldEngine(sensitivity=0.05)
prices = np.array([100, 101, 102, 101, 99, 98, 97, 96], dtype=float)
volumes = np.full_like(prices, 5000.0)

curvature = engine.calculate_curvature(prices)
entropy = engine.differential_entropy(prices)
drift = engine.manifold_drift(prices)
resonance = engine.adelic_resonance(prices, volumes)
void = engine.detect_adelic_void(prices, volumes)

signal = engine.generate_signal(
    curvature,
    entropy=entropy,
    entropy_baseline=1.0,
    drift=drift,
    adelic_void=void,
    adelic_resonance=resonance,
)

print(curvature, entropy, drift, resonance, void, signal)
```
