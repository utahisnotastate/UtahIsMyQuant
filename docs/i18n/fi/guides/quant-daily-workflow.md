# Quantin päivittäinen työnkulku — UtahIsMyQuant arkeen

Näin käytät UtahIsMyQuantia **jokaisena kauppapäivänä** ilman, että siitä tulee toinen hylätty repo kannettavallasi.

---

## Aamu (ennen markkinoita, 30–45 min)

### 1. Terveystarkistus

```powershell
cd UtahIsMyQuant
.venv\Scripts\activate
pytest -q
```

Jos punainen: **älä käy kauppaa**. Korjaa testit ensin — ne suojelevat matematiikkaa, jonka lopetit ymmärtämästä kuusi kuukautta sitten.

### 2. Tarkista yön lokit

Etsi eilisen lokeista:

| Kuvio | Toimenpide |
|-------|------------|
| `CIRCUIT BREAKER TRIPPED` | Tarkista feed-viive / VPS-verkko |
| `gates_failed': ['shadow']` | Alpha peilaa kohinaa — pienennä kokoa tai tauota |
| `FORCE_STOP` | Jokaisen symbolin jälkikäynti |
| Enimmäkseen `WAIT` | Normaalia. Epäilyttävää, jos 100 % EXECUTE |

### 3. Aseta päivän parametrit (kirjoita ylös)

```python
engine = ManifoldEngine(sensitivity=0.05)  # do not change mid-session
gen = AlphaGenerator(
    capital=YOUR_NAV,
    risk_limit=0.02,
    min_volume=YOUR_VENUE_MIN,
    supervisor=RiskSupervisor(max_latency_ms=200),
)
```

**Sääntö:** Enintään yksi parametrimuutos viikossa livessä. Muuten backtestaat oikealla rahalla.

### 4. Käynnistä sentinel (vain loki ensimmäiset 15 min)

```python
# omega_point.py or your wrapper
omega = OmegaPoint(uri=os.environ["WSS_URI"], capital=NAV)
# First 15 min: patch execute() to log-only
```

Varmista `latency_us` p99 < 200ms.

---

## Markkina-aika (jatkuva)

### Tapahtumasilmukan mentaalimalli

```text
tick → manifold features → gates → supervisor → your broker adapter
```

### Sinun tehtäväsi EI ole ohittaa

Jos ohitat yli 2× viikossa, järjestelmä on väärin konfiguroitu — korjaa parametrit, älä tee sankarikauppoja.

### Pikadiagnostiikka

```python
event = gen.process_tick(tick)
if event:
    print(event.signal, event.action, event.gates_failed, event.supervisor_verdict)
```

### Lounastarkistus (5 min)

- Tilin drawdown vs `max_account_drawdown`
- Jokin symboli jumissa altistuksessa, kun action on WAIT (synk-bugi?)
- Tithe-kertymä (`tithe_allocation()`) — vain sanity

---

## Iltapäivä (sulku)

### 1. Flatten-politiikka

Päätä pöydän sääntö:

- **Auto EXIT** `DRIFT_DECELERATING`-signaalilla (jo bias)
- Kovaa flat T-15 minuuttia — broker-cronisi, ei UtahIsMyQuant

### 2. Vie `AlphaEvent`-loki

Append-only JSONL suositeltu:

```python
import json
with open("logs/session.jsonl", "a") as f:
    f.write(json.dumps(event.__dict__, default=str) + "\n")
```

### 3. Sammuta siististi

```python
omega.shutdown()  # stops shadow thread + supervisor thread
```

---

## Viikoittain (tutkimus ilman backtest-teatteria)

| Päivä | Tehtävä |
|-------|---------|
| Ma | Tarkista gate-epäonnistumishistogrammi |
| Ke | Paperitestaa yksi parametrin muutos |
| Pe | Kirjoita 3 lauseen jälkikäynti huonoimmasta kaupasta |

**Sallittu tutkimus:**

- Viivejakaumakuviot
- Peilausaste vs toteutunut slippage
- Volume-gate-kalibrointi

**Kielletty tutkimus:**

- "Vielä yksi backtest vuodelta 2019" live-muutoksen perustelemiseksi tänään

---

## Broker-kytkentä (malli)

```python
async def guarded_execute(tick: Tick, event: AlphaEvent):
    if event.action not in (Action.BUY, Action.SELL, Action.EXIT):
        return
    if event.circuit_breaker:
        return
    await broker.send(symbol=tick.symbol, side=event.action.value, qty=size_from(event))
```

Pidä **idempotentit** order ID:t. Supervisor voi pakottaa toistuvia EXIT-yrityksiä volatiileilla tickeillä — deduplikoi omalla puolellasi.

---

## Integraatio "normaaliin quant-elämään"

| Aktiviteetti | UtahIsMyQuant-rooli |
|--------------|---------------------|
| Aamututkimus | Vaikuttaa `min_volume`-arvoon, ei harkittavaan ohitukseen |
| Makrokalenteri | Manuaalinen tauko: kutsu `supervisor.reset_circuit_breaker()` vain kun olet itse pysäyttänyt uudet entryt |
| Slack-hälytykset | Kytke `EXECUTE_*` ja `FORCE_STOP` |
| Jupyter-tutkimus | Offline replay `ingest`-kautta, ei sekoitettuna live-silmukkaan |
| Viikonloppu-ML-harjoitus | Erillinen putki; älä yhdistä painoja monistoon |

---

## Kun häviät rahaa

1. Hae `gates_failed` kyseiselle kaupalle
2. Tarkista, laukesiko supervisor-veto ja ohititko sen
3. Jos kaikki gateet vihreinä ja silti häviö: **normaalia**
4. Älä nosta `risk_limit`-arvoa samana päivänä

---

## Kun ansaitset rahaa

Lähetä tekijälle jotain, jos voit: **PayPal utah@utahcreates.com** — köyhä ylläpitäjärahasto.

---

## Pikaopas

```bash
pytest -q
py omega_point.py
py omega_point.py --uri $env:WSS_URI --live
```

Dokumentit: [API-viite](../api-reference.md) | [Tekninen arkkitehtuuri](../technical-architecture.md)
