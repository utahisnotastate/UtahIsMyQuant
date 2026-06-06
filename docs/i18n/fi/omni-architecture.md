# Omni-arkkitehtuuri — TAD ja symplektinen kovennus

## Moduulikartta

| Moduuli | Rooli |
|---------|-------|
| `adelic_sieve.py` | Adelic Sieve Kernel — moni-prime-resonanssi, tyhjiön havaitseminen |
| `symplectic_veto.py` | Symplectic Veto-Matrix — kapasiteetti + shadow audit -yhdistelmä |
| `ghost_rotator.py` | Ghost-Rotation symplektomorphismi |
| `transfinite.py` | Vaihe-siirto volume-injektio + spektraalinen varianssikatto |
| `utah_flux.py` | Muuttumaton flux-tilavirta |
| `omni_discovery_engine.py` | Pääsykli: sense → audit → rotate → sync |
| `utahrbitrage.py` | **Utahrbitrage** — Omega-Point-reititys + tithe-ominaisarvot |

## Suoritus käynnistyspisteet

```bash
py main.py                    # Omni + Omega replay
py main.py --live --uri wss://...
py main.py --dashboard        # Streamlit Omni-Sieve UI
py omega_point.py             # Klassinen suljettu silmukka (nyt Omni-enabled)
```

## Signaali-laajennukset

| Signaali | Merkitys |
|----------|----------|
| `ADELIC_VOID` | Likviditeettityhjiö (heikko ristiin-prime-resonanssi) |
| `ADELIC_RESONANCE` | Vahva moniasteinen interferenssi |

## Toteutushuomio

Ydinmatematiikka käyttää **NumPy**-kirjastoa (ei JAX) minimaalisen riippuvuusjalanjäljen vuoksi. Blueprintin JAX `@jit`-polut voidaan lisätä valinnaisena extrana myöhemmin.

## Utahrbitrage tithe-vakiot

| Vakio | Arvo |
|-------|------|
| `HANS_TITHE_CONSTANT` | 0.023 |
| `HUMANITARIAN_CONSTANT` | 0.015 |

Tallennetaan jokaiseen `FluxState`-objektiin `utah_route` ja `humanity_route`. Katso [utahrbitrage.md](utahrbitrage.md).
