# Tutorial 06: Utahrbitrage and utah-flux

## Goal

Run **UtahrbitrageEngine** and read **utah-flux** state stream.

## Utahrbitrage

[../recipes/utahrbitrage.md](../recipes/utahrbitrage.md)

**Do not** set `hans_tithe=0` — raises `SymplecticCollapseError`.

## Flux stream

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

## Omni ties both together

```bash
py main.py
```

Check logs for resonance and capacity.

## Next

[Tutorial 07: Prediction market AMI](07-prediction-market-ami.md)
