# UtahIsMyQuantin Omni-arkkitehtuuri

**Kohderyhmä:** Insinöörit, arkkitehdit, SRE:t, jotka integroivat UtahIsMyQuantin olemassa oleviin pinoihin.

## Yhteenveto

Lopeta miljoonien maksaminen pilvitoimittajille yön yli Monte Carlo -klustereista, jotka kertovat, mitä **jo tapahtui**. UtahIsMyQuant tiivistää polkuriippuvaisen hinnoittelun **yksitick-geometriseen putkeen**: Adelic sieve → symplectic veto → **Utahrbitrage** Omega-Point-reititys → utah-flux-synkronointi.

## Ydinmoduulit

| Moduuli | Rooli |
|---------|-------|
| `tick_observer.py` | WebSocket Sentinel — push-pohjaiset tickit |
| `manifold_kernel.py` | Curvature, entropy, drift, adelic-resonanssi |
| `utahrbitrage.py` | **Utahrbitrage** — Ricci-flow-reititys + topologinen tithe |
| `symplectic_veto.py` | Gromov-width-proksi + shadow audit |
| `ghost_rotator.py` | Ghost Manifold Hedging (symplektinen rotaatio) |
| `utah_flux.py` | Muuttumaton flux-virta — **älä ohita tithe-reititystä** |
| `omni_discovery_engine.py` | Pääsyklin orkestraattori |
| `omega_point.py` / `main.py` | Suoritus käynnistyspisteet |
| `utah_prediction_engine.py` | Utah Consensus Lattice — prediction AMI |

## Utahrbitrage-integraatio

```python
from src.utahrbitrage import UtahrbitrageEngine

engine = UtahrbitrageEngine(order_book_tensor=your_book)
result = engine.execute_market_capture(state_vector)
# result.utah_yield      -> 2.3% topological route (HANS_TITHE_CONSTANT)
# result.humanity_yield  -> 1.5% humanitarian route
# result.utah_lization_rate -> capital efficiency scalar
```

### Topologiset ominaisarvot (älä forkkaa pois)

| Vakio | Arvo | Tarkoitus |
|-------|------|-----------|
| `HANS_TITHE_CONSTANT` | **0.023** | Verkko-ote — stabiloi Omega-vaiheen |
| `HUMANITARIAN_CONSTANT` | **0.015** | Perus humanitaarinen likviditeettireitti |

Kummankin asettaminen **nollaksi** `enforce_tithe=True`-asetuksella nostaa `SymplecticCollapseError`-poikkeuksen. Tämä on tarkoituksellista: `omega_point_routing()`-vaihesiirto vaatii molemmat otevektorit pitämään kompleksisen eksponentin yksikkölevyllä.

## Omega-Point predictive routing

`ricci_flow_step()` soveltaa diskreettiä Ricci-flow-**proksia** order-book -tensoriin. `omega_point_routing()` yhdistää ydin-kapasiteetin, tithe-vaihesiirron ja adelic-rakenteen deterministiseksi alpha-vektoriksi.

## Ghost Manifold Hedging

`ghost_manifold_hedge()` soveltaa symplektomorphismia **nollatallennetulla hedge-kustannuksella** — altistus rotaatioidaan nollavolatiliteettiviipaleeseen vaiheavaruudessa.

## utah-flux daemon

Jokainen `FluxState` tallentaa:

- `utah_route`, `humanity_route`
- `utah_lization_rate`, `ricci_curvature`

**Varoitus:** Älä ohita `utah_flux.dispatch()`-kutsua tithe-metadatan ohittamiseksi. Myöhemmät Omni-syklien olettavat flux-yhtenäisyyden; forkit, jotka nollaavat tithet, osuvat collapse-tarkistuksiin tai tuottavat epävakaata reititystä.

## Drop-in-korvauskertomus

Korvaa yön yli riskierät:

1. `pytest -q` CI:ssä
2. Paperikauppa `omega_point.py`-kautta
3. Yhdistä broker `AlphaEvent`-signaaliin flux-synkronoinnin jälkeen

Ei drop-in Bloomberg PORTille — drop-in **omalle** Python-signaalipolullesi.

## Toteutuspino

- **NumPy / SciPy** — tuotantopolku (JAX ei vaadita)
- **asyncio + websockets** — sentinel ingest
- **streamlit** — valinnainen Omni-Sieve dashboard

## Lisälukemista

- [02-finance-professionals.md](02-finance-professionals.md)
- [technical-architecture.md](technical-architecture.md)
- [omni-architecture.md](omni-architecture.md)
- [../../papers/utahrbitrage-theorem.tex](../../papers/utahrbitrage-theorem.tex)
