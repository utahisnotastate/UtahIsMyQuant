# レシピ: Utahrbitrage Engine

```python
import numpy as np
from src.utahrbitrage import UtahrbitrageEngine, HANS_TITHE_CONSTANT

engine = UtahrbitrageEngine(order_book_tensor=np.eye(4))
state = engine.build_state_vector(
    prices=np.linspace(450, 451, 20),
    volumes=np.full(20, 5000.0),
    exposure=2000.0,
    momentum=0.5,
)

result = engine.execute_market_capture(state)
print("utah_lization:", result.utah_lization_rate)
print("utah_yield:", result.utah_yield)
print("humanity_yield:", result.humanity_yield)
print("ledger:", engine.liquidity_ledger[-1])

hedge = engine.ghost_manifold_hedge(state, theta=0.1)
print("hedge_cost:", hedge.hedge_cost)
```
