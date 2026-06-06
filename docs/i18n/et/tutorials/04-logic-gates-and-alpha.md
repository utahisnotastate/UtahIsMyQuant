# Õpetus 04: Loogikaväravad ja alfa

## Eesmärk

Mõista **LogicGateMatrix** ja `generate_action()` tagastusväärtusi.

## Väravad (kõik peavad läbima EXECUTE_* jaoks)

| Värav | Ebaõnnestub, kui… |
|-------|-------------------|
| curvature | Signaal pole kaubeldav või pööre liiga nõrk |
| volume | Allpool `min_volume` |
| risk | `exposure/capital >= risk_limit` |
| shadow | Shadow tensor ebatervislik |

## Retsept

[../recipes/alpha-gates.md](../recipes/alpha-gates.md)

## Harjutus: sunni WAIT

```python
from src.alpha_generator import AlphaGenerator

gen = AlphaGenerator(enable_shadow_audit=False)
# Low volume → volume gate fails
d = gen.generate_action("BREAKOUT_PRIMED", 100_000, 0, curvature=0.1, volume=0.1)
assert d["action"] == "WAIT"
print(d["reason"], d["gates_failed"])
```

## Edasi

[Õpetus 05: Risk supervisor ja veto](05-risk-supervisor-and-veto.md)
