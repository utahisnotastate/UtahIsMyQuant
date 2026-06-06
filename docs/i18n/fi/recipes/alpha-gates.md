# Resepti: Alpha Generator ja Logic Gateet

```python
from src.alpha_generator import AlphaGenerator, ExecuteAction
from src.tick_observer import Tick

gen = AlphaGenerator(enable_shadow_audit=False, enable_transfinite=False)

decision = gen.generate_action(
    "REVERSAL_IMMINENT",
    capital=100_000,
    exposure=0,
    curvature=0.12,
    volume=5000,
    shadow_healthy=True,
    drift=-0.01,
)

print(decision["action"], decision.get("reason"))
print("gates_failed:", decision.get("gates_failed", []))

# Process a tick stream
for price in [450.0, 450.5, 451.0, 450.2, 449.8, 449.0]:
    event = gen.process_tick(Tick(symbol="SPY", price=price, volume=3000))
    if event:
        print(event.signal, event.action, event.gates_failed)
```
