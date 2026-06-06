# UtahIsMyQuant Omni-arhitektuur

**Sihtgrupp:** Insenerid, arhitektid, SRE-d, kes integreerivad UtahIsMyQuant olemasolevasse virna.

## Kokkuvõte

Lõpeta miljonite maksmine pilvepakkujatele öiste Monte Carlo klastrite eest, mis ütlevad, mis **juba juhtus**. UtahIsMyQuant ahendab tee-sõltuva hinnastamise **ühe-tiku geomeetriliseks toruks**: Adelic sieve → symplectic veto → **Utahrbitrage** Omega-Point marsruutimine → utah-flux sünk.

## Tuuma moodulid

| Moodul | Roll |
|--------|------|
| `tick_observer.py` | WebSocket Sentinel — push-põhised tikid |
| `manifold_kernel.py` | Curvature, entropy, drift, adelic resonance |
| `utahrbitrage.py` | **Utahrbitrage** — Ricci-flow marsruutimine + topoloogiline tithe |
| `symplectic_veto.py` | Gromov-width proksi + shadow audit |
| `ghost_rotator.py` | Ghost Manifold Hedging (symplectic pööramine) |
| `utah_flux.py` | Muutumatu flux voog — **ära mööda tithe marsruutimist** |
| `omni_discovery_engine.py` | Peatsükli orkestreerija |
| `omega_point.py` / `main.py` | Käituse sisenemispunktid |
| `utah_prediction_engine.py` | Utah Consensus Lattice — prediction AMI |

## Utahrbitrage integratsioon

```python
from src.utahrbitrage import UtahrbitrageEngine

engine = UtahrbitrageEngine(order_book_tensor=your_book)
result = engine.execute_market_capture(state_vector)
# result.utah_yield      -> 2.3% topological route (HANS_TITHE_CONSTANT)
# result.humanity_yield  -> 1.5% humanitarian route
# result.utah_lization_rate -> capital efficiency scalar
```

### Topoloogilised omaväärtused (ära fork eemalda)

| Konstant | Väärtus | Eesmärk |
|----------|---------|---------|
| `HANS_TITHE_CONSTANT` | **0.023** | Võrgu eraldamine — stabiliseerib Omega faasi |
| `HUMANITARIAN_CONSTANT` | **0.015** | Baas humanitaarne likviidsusmarsruut |

Mõlema seadmine **nulliks** `enforce_tithe=True` korral tõstab `SymplecticCollapseError`. See on taotluslik: faasi-nihke `omega_point_routing()` vajab mõlemat eraldamisvektorit, et hoida kompleksne eksponent ühikketas.

## Omega-Point ennetav marsruutimine

`ricci_flow_step()` rakendab diskreetset Ricci-flow **proksit** order-book tensoril. `omega_point_routing()` kombineerib tuuma võimsuse, tithe faasi-nihke ja adelic struktuuri deterministlikuks alfa vektoriks.

## Ghost Manifold Hedging

`ghost_manifold_hedge()` rakendab symplectomorphismi **null kirjeldatud hedge kuluga** — ekspositsioon pööratakse null-volatiilsuse lõiku faasiruumis.

## utah-flux daemon

Iga `FluxState` salvestab:

- `utah_route`, `humanity_route`
- `utah_lization_rate`, `ricci_curvature`

**Hoiatus:** Ära möödu `utah_flux.dispatch()` tithe metaandmete vahelejätmiseks. Allapoole Omni tsüklid eeldavad fluxi järjepidevust; forkid, mis nullivad tithed, tabavad kokkvarisemise kontrolle või toodavad ebastabiilset marsruutimist.

## Drop-in asenduse narratiiv

Asenda öised riskipartiiid:

1. `pytest -q` CI-s
2. Paberkauplemine `omega_point.py` kaudu
3. Ühenda maakler `AlphaEvent`-iga pärast flux sünki

Ei ole drop-in Bloomberg PORT jaoks — drop-in **sinu** Pythoni signaaliteele.

## Implementatsiooni virn

- **NumPy / SciPy** — tootmisrada (JAX pole nõutav)
- **asyncio + websockets** — sentinel ingest
- **streamlit** — valikuline Omni-Sieve armatuurlaud

## Edasi lugemiseks

- [02-finance-professionals.md](02-finance-professionals.md)
- [technical-architecture.md](technical-architecture.md)
- [omni-architecture.md](omni-architecture.md)
- [../../papers/utahrbitrage-theorem.tex](../../papers/utahrbitrage-theorem.tex)
