# Tutorial 04: Logic Gates and Alpha

## Goal

Understand **LogicGateMatrix** and `generate_action()` return values.

## Gates (all must pass for EXECUTE_*)

| Gate | Fails when… |
|------|-------------|
| curvature | Signal not tradeable or reversal too weak |
| volume | Below `min_volume` |
| risk | `exposure/capital >= risk_limit` |
| shadow | Shadow tensor unhealthy |

## Recipe

[../recipes/alpha-gates.md](../recipes/alpha-gates.md)

## Exercise: force WAIT

```python
from src.alpha_generator import AlphaGenerator

gen = AlphaGenerator(enable_shadow_audit=False)
# Low volume → volume gate fails
d = gen.generate_action("BREAKOUT_PRIMED", 100_000, 0, curvature=0.1, volume=0.1)
assert d["action"] == "WAIT"
print(d["reason"], d["gates_failed"])
```

## Next

[Tutorial 05: Risk supervisor and veto](05-risk-supervisor-and-veto.md)
