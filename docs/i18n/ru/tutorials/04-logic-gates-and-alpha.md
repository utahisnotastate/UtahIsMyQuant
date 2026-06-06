# Учебник 04: Логические ворота и alpha

## Цель

Понять **LogicGateMatrix** и возвращаемые значения `generate_action()`.

## Ворота (все должны пройти для EXECUTE_*)

| Gate | Сбой когда… |
|------|-------------|
| curvature | Сигнал не торгуемый или разворот слишком слабый |
| volume | Ниже `min_volume` |
| risk | `exposure/capital >= risk_limit` |
| shadow | Shadow tensor нездоров |

## Рецепт

[../recipes/alpha-gates.md](../recipes/alpha-gates.md)

## Упражнение: принудительный WAIT

```python
from src.alpha_generator import AlphaGenerator

gen = AlphaGenerator(enable_shadow_audit=False)
# Низкий объём → volume gate fails
d = gen.generate_action("BREAKOUT_PRIMED", 100_000, 0, curvature=0.1, volume=0.1)
assert d["action"] == "WAIT"
print(d["reason"], d["gates_failed"])
```

## Далее

[Учебник 05: Risk supervisor и veto](05-risk-supervisor-and-veto.md)
