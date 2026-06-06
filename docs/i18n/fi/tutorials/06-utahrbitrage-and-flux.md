# Opetusohjelma 06: Utahrbitrage ja utah-flux

## Tavoite

Aja **UtahrbitrageEngine** ja lue **utah-flux**-tilavirta.

## Utahrbitrage

[../recipes/utahrbitrage.md](../recipes/utahrbitrage.md)

**Älä** aseta `hans_tithe=0` — nostaa `SymplecticCollapseError`-poikkeuksen.

## Flux-virta

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

## Omni yhdistää molemmat

```bash
py main.py
```

Tarkista lokit resonanssille ja kapasiteetille.

## Seuraavaksi

[Opetusohjelma 07: Ennustemarkkinoiden AMI](07-prediction-market-ami.md)
