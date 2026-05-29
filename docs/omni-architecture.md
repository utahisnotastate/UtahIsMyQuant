# Omni Architecture — TAD & Symplectic Hardening

## Module map

| Module | Role |
|--------|------|
| `adelic_sieve.py` | Adelic Sieve Kernel — multi-prime resonance, void detection |
| `symplectic_veto.py` | Symplectic Veto-Matrix — capacity + shadow audit merge |
| `ghost_rotator.py` | Ghost-Rotation symplectomorphism |
| `transfinite.py` | Phase-shift volume injection + spectral variance cap |
| `utah_flux.py` | Immutable flux state stream |
| `omni_discovery_engine.py` | Master cycle: sense → audit → rotate → sync |
| `utahrbitrage.py` | **Utahrbitrage** — Omega-Point routing + tithe eigenvalues |

## Execution entry points

```bash
py main.py                    # Omni + Omega replay
py main.py --live --uri wss://...
py main.py --dashboard        # Streamlit Omni-Sieve UI
py omega_point.py             # Classic closed loop (now Omni-enabled)
```

## Signal extensions

| Signal | Meaning |
|--------|---------|
| `ADELIC_VOID` | Liquidity vacuum (low cross-prime resonance) |
| `ADELIC_RESONANCE` | Strong multi-scale interference |

## Implementation note

Core math uses **NumPy** (not JAX) for a minimal dependency footprint. JAX `@jit` paths from the blueprint can be added as an optional extra later.

## Utahrbitrage tithe constants

| Constant | Value |
|----------|-------|
| `HANS_TITHE_CONSTANT` | 0.023 |
| `HUMANITARIAN_CONSTANT` | 0.015 |

Recorded on every `FluxState` as `utah_route` and `humanity_route`. See [utahrbitrage.md](utahrbitrage.md).
