# 教程 04：逻辑门控与 Alpha

## 目标

理解 **LogicGateMatrix** 与 `generate_action()` 返回值。

## 门控（EXECUTE_* 须全部通过）

| 门控 | 失败当… |
|------|---------|
| curvature | 信号不可交易或反转过弱 |
| volume | 低于 `min_volume` |
| risk | `exposure/capital >= risk_limit` |
| shadow | Shadow tensor 不健康 |

## 配方

[../recipes/alpha-gates.md](../recipes/alpha-gates.md)

## 练习：强制 WAIT

```python
from src.alpha_generator import AlphaGenerator

gen = AlphaGenerator(enable_shadow_audit=False)
# Low volume → volume gate fails
d = gen.generate_action("BREAKOUT_PRIMED", 100_000, 0, curvature=0.1, volume=0.1)
assert d["action"] == "WAIT"
print(d["reason"], d["gates_failed"])
```

## 下一步

[教程 05：风险 supervisor 与否决](05-risk-supervisor-and-veto.md)
