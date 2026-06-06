# Opetusohjelma 04: Logic gateet ja alpha

## Tavoite

Ymmärrä **LogicGateMatrix** ja `generate_action()`-paluuarvot.

## Gateet (kaikkien täytyy läpäistä EXECUTE_*:lle)

| Gate | Epäonnistuu kun… |
|------|------------------|
| curvature | Signaali ei kaupattava tai käännös liian heikko |
| volume | Alle `min_volume` |
| risk | `exposure/capital >= risk_limit` |
| shadow | Shadow tensor epäterve |

## Resepti

[../recipes/alpha-gates.md](../recipes/alpha-gates.md)

## Harjoitus: pakota WAIT

```python
from src.alpha_generator import AlphaGenerator

gen = AlphaGenerator(enable_shadow_audit=False)
# Low volume → volume gate fails
d = gen.generate_action("BREAKOUT_PRIMED", 100_000, 0, curvature=0.1, volume=0.1)
assert d["action"] == "WAIT"
print(d["reason"], d["gates_failed"])
```

## Seuraavaksi

[Opetusohjelma 05: Risk supervisor ja veto](05-risk-supervisor-and-veto.md)
