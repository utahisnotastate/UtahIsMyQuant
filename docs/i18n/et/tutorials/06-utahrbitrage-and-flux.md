# Õpetus 06: Utahrbitrage ja utah-flux

## Eesmärk

Käivita **UtahrbitrageEngine** ja loe **utah-flux** olekuvoogu.

## Utahrbitrage

[../recipes/utahrbitrage.md](../recipes/utahrbitrage.md)

**Ära** sea `hans_tithe=0` — tõstab `SymplecticCollapseError`.

## Flux voog

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

## Omni seob mõlemad

```bash
py main.py
```

Kontrolli logisid resonantsi ja võimsuse jaoks.

## Edasi

[Õpetus 07: Ennustusturu AMI](07-prediction-market-ami.md)
