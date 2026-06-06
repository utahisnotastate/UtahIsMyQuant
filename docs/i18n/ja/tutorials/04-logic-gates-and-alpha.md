# チュートリアル 04: ロジックゲートとアルファ

## 目標

**LogicGateMatrix** と `generate_action()` の戻り値を理解する。

## ゲート（EXECUTE_* には全て合格が必要）

| ゲート | 失敗条件… |
|------|-------------|
| curvature | シグナルが取引不可、または反転が弱すぎる |
| volume | `min_volume` 未満 |
| risk | `exposure/capital >= risk_limit` |
| shadow | Shadow tensor が不健全 |

## レシピ

[../recipes/alpha-gates.md](../recipes/alpha-gates.md)

## 演習: WAIT を強制

```python
from src.alpha_generator import AlphaGenerator

gen = AlphaGenerator(enable_shadow_audit=False)
# Low volume → volume gate fails
d = gen.generate_action("BREAKOUT_PRIMED", 100_000, 0, curvature=0.1, volume=0.1)
assert d["action"] == "WAIT"
print(d["reason"], d["gates_failed"])
```

## 次へ

[チュートリアル 05: リスクスーパーバイザーと拒否](05-risk-supervisor-and-veto.md)
