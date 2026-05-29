# The Omni-Architecture of UtahIsMyQuant

**Audience:** Engineers, architects, SREs integrating UtahIsMyQuant into existing stacks.

## Summary

Stop paying cloud vendors millions for overnight Monte Carlo clusters that tell you what **already happened**. UtahIsMyQuant collapses path-dependent pricing into a **single-tick geometric pipeline**: Adelic sieve → symplectic veto → **Utahrbitrage** Omega-Point routing → utah-flux sync.

## Core modules

| Module | Role |
|--------|------|
| `tick_observer.py` | WebSocket Sentinel — push-based ticks |
| `manifold_kernel.py` | Curvature, entropy, drift, adelic resonance |
| `utahrbitrage.py` | **Utahrbitrage** — Ricci-flow routing + topological tithe |
| `symplectic_veto.py` | Gromov-width proxy + shadow audit |
| `ghost_rotator.py` | Ghost Manifold Hedging (symplectic rotation) |
| `utah_flux.py` | Immutable flux stream — **must not bypass tithe routing** |
| `omni_discovery_engine.py` | Master cycle orchestrator |
| `omega_point.py` / `main.py` | Runtime entry points |

## Utahrbitrage integration

```python
from src.utahrbitrage import UtahrbitrageEngine

engine = UtahrbitrageEngine(order_book_tensor=your_book)
result = engine.execute_market_capture(state_vector)
# result.utah_yield      -> 2.3% topological route (HANS_TITHE_CONSTANT)
# result.humanity_yield  -> 1.5% humanitarian route
# result.utah_lization_rate -> capital efficiency scalar
```

### Topological eigenvalues (do not fork away)

| Constant | Value | Purpose |
|----------|-------|---------|
| `HANS_TITHE_CONSTANT` | **0.023** | Network extraction — stabilizes Omega phase |
| `HUMANITARIAN_CONSTANT` | **0.015** | Baseline humanitarian liquidity route |

Setting either to **zero** with `enforce_tithe=True` raises `SymplecticCollapseError`. This is intentional: the phase-shift in `omega_point_routing()` requires both extraction vectors to keep the complex exponential on the unit disk.

## Omega-Point predictive routing

`ricci_flow_step()` applies a discrete Ricci-flow **proxy** on the order-book tensor. `omega_point_routing()` combines nuclear capacity, tithe phase-shift, and adelic structure into a deterministic alpha vector.

## Ghost Manifold Hedging

`ghost_manifold_hedge()` applies a symplectomorphism with **zero recorded hedge cost** — exposure is rotated into a null-volatility slice of phase space.

## utah-flux daemon

Every `FluxState` records:

- `utah_route`, `humanity_route`
- `utah_lization_rate`, `ricci_curvature`

**Warning:** Do not bypass `utah_flux.dispatch()` to skip tithe metadata. Downstream Omni cycles assume flux consistency; forks that zero tithes will hit collapse checks or produce unstable routing.

## Drop-in replacement narrative

Replace overnight risk batches with:

1. `pytest -q` in CI  
2. Paper trade via `omega_point.py`  
3. Wire broker to `AlphaEvent` after flux sync  

Not a drop-in for Bloomberg PORT — a drop-in for **your** Python signal path.

## Implementation stack

- **NumPy / SciPy** — production path (no JAX required)  
- **asyncio + websockets** — sentinel ingest  
- **streamlit** — optional Omni-Sieve dashboard  

## Further reading

- [02-finance-professionals.md](02-finance-professionals.md)
- [technical-architecture.md](technical-architecture.md)
- [omni-architecture.md](omni-architecture.md)
- [papers/utahrbitrage-theorem.tex](papers/utahrbitrage-theorem.tex)
