# チュートリアル 06: Utahrbitrage と utah-flux

## 目標

**UtahrbitrageEngine** を実行し **utah-flux** 状態ストリームを読む。

## Utahrbitrage

[../recipes/utahrbitrage.md](../recipes/utahrbitrage.md)

**`hans_tithe=0` にしない** — `SymplecticCollapseError` が発生する。

## Flux ストリーム

```python
from src.utah_flux import UtahFluxEngine

flux = UtahFluxEngine()
state = flux.build_state(
    symplectic_capacity=0.4,
    adelic_resonance=0.8,
    utah_route=23.0,
    humanity_route=15.0,
    utah_lization_rate=0.96,
)
print(flux.get_latest_manifold())
```

## Omni が両方を結ぶ

```bash
py main.py
```

共鳴と容量のログを確認。

## 次へ

[チュートリアル 07: 予測市場 AMI](07-prediction-market-ami.md)
