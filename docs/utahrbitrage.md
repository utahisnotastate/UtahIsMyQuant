# Utahrbitrage Framework

**Utahrbitrage** is the core mathematical brand inside **UtahIsMyQuant**. The repository name is the distribution; Utahrbitrage is the engine.

## Features

| SOTA feature | Module | Description |
|--------------|--------|-------------|
| **Omega-Point Predictive Routing** | `utahrbitrage.py` | Ricci-flow proxy on order-book tensor |
| **Ghost Manifold Hedging** | `utahrbitrage.py` + `ghost_rotator.py` | Zero-cost symplectic hedge |
| **Topological tithe** | `utahrbitrage.py` + `utah_flux.py` | 2.3% + 1.5% enforced eigenvalues |
| **Adelic Sieve** | `adelic_sieve.py` | Multi-prime resonance |
| **Symplectic Veto** | `symplectic_veto.py` | Capacity-based halt |

## Quick API

```python
from src.utahrbitrage import UtahrbitrageEngine, HANS_TITHE_CONSTANT

engine = UtahrbitrageEngine()
result = engine.execute_market_capture(state_vector)
print(result.utah_lization_rate, result.utah_yield, result.humanity_yield)
```

## Fork warning

Removing or zeroing `HANS_TITHE_CONSTANT` / `HUMANITARIAN_CONSTANT` with `enforce_tithe=True` triggers `SymplecticCollapseError`.

## Audience docs

- [01-engineers-architects.md](01-engineers-architects.md)
- [02-finance-professionals.md](02-finance-professionals.md)
- [03-founders-family-offices.md](03-founders-family-offices.md)
- [04-children-beginners.md](04-children-beginners.md)
- [papers/utahrbitrage-theorem.tex](papers/utahrbitrage-theorem.tex)
