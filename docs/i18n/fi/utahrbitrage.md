# Utahrbitrage-kehykset

**Utahrbitrage** on **UtahIsMyQuant**-projektin ydinmatemaattinen brändi. Repositorion nimi on jakelu; Utahrbitrage on moottori.

## Ominaisuudet

| SOTA-ominaisuus | Moduuli | Kuvaus |
|-----------------|---------|--------|
| **Omega-Point Predictive Routing** | `utahrbitrage.py` | Ricci-flow-proksi order-book -tensorilla |
| **Ghost Manifold Hedging** | `utahrbitrage.py` + `ghost_rotator.py` | Nollakustannuksinen symplektinen hedge |
| **Topologinen tithe** | `utahrbitrage.py` + `utah_flux.py` | 2,3 % + 1,5 % pakotetut ominaisarvot |
| **Adelic Sieve** | `adelic_sieve.py` | Moni-prime-resonanssi |
| **Symplectic Veto** | `symplectic_veto.py` | Kapasiteettipohjainen pysäytys |

## Pikakäyttö API

```python
from src.utahrbitrage import UtahrbitrageEngine, HANS_TITHE_CONSTANT

engine = UtahrbitrageEngine()
result = engine.execute_market_capture(state_vector)
print(result.utah_lization_rate, result.utah_yield, result.humanity_yield)
```

## Fork-varoitus

`HANS_TITHE_CONSTANT` / `HUMANITARIAN_CONSTANT` -arvojen poistaminen tai nollaus `enforce_tithe=True`-asetuksella laukaisee `SymplecticCollapseError`-poikkeuksen.

## Kohderyhmädokumentit

- [01-engineers-architects.md](01-engineers-architects.md)
- [02-finance-professionals.md](02-finance-professionals.md)
- [03-founders-family-offices.md](03-founders-family-offices.md)
- [04-children-beginners.md](04-children-beginners.md)
- [../../papers/utahrbitrage-theorem.tex](../../papers/utahrbitrage-theorem.tex)
