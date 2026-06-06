# Omni arhitektuur — TAD ja Symplectic tugevdamine

## Moodulite kaart

| Moodul | Roll |
|--------|------|
| `adelic_sieve.py` | Adelic Sieve Kernel — multi-prime resonants, void tuvastus |
| `symplectic_veto.py` | Symplectic Veto-Matrix — võimsus + shadow audit merge |
| `ghost_rotator.py` | Ghost-Rotation symplectomorphism |
| `transfinite.py` | Faasi-nihke ruumala süst + spektraalne variantsi cap |
| `utah_flux.py` | Muutumatu flux olekuvoog |
| `omni_discovery_engine.py` | Peatsükkel: sense → audit → rotate → sync |
| `utahrbitrage.py` | **Utahrbitrage** — Omega-Point marsruutimine + tithe omaväärtused |

## Käituse sisenemispunktid

```bash
py main.py                    # Omni + Omega replay
py main.py --live --uri wss://...
py main.py --dashboard        # Streamlit Omni-Sieve UI
py omega_point.py             # Klassikaline suletud tsükkel (nüüd Omni-enabled)
```

## Signaali laiendused

| Signaal | Tähendus |
|---------|----------|
| `ADELIC_VOID` | Likviidsuse vaakum (madal rist-prime resonants) |
| `ADELIC_RESONANCE` | Tugev mitmemastaabi interferents |

## Implementatsiooni märkus

Tuuma matemaatika kasutab **NumPy** (mitte JAX) minimaalse sõltuvusjalajälje jaoks. JAX `@jit` rajad blueprintist võib hiljem lisada valikulise extrana.

## Utahrbitrage tithe konstandid

| Konstant | Väärtus |
|----------|---------|
| `HANS_TITHE_CONSTANT` | 0.023 |
| `HUMANITARIAN_CONSTANT` | 0.015 |

Salvestatakse igal `FluxState`-il `utah_route` ja `humanity_route`. Vaata [utahrbitrage.md](utahrbitrage.md).
