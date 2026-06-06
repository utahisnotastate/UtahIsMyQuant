# Kvanti igapäevane töövoog — UtahIsMyQuant igapäevasesse ellu

Nii kasutad UtahIsMyQuant **iga kauplemispäeva** ilma, et see muutuks järjekordseks hüljatud repoks sülearvutis.

---

## Hommik (enne turgu, 30–45 min)

### 1. Tervisekontroll

```powershell
cd UtahIsMyQuant
.venv\Scripts\activate
pytest -q
```

Kui punane: **ära kauple**. Paranda testid esmalt — need valvavad matemaatikat, mida sa kuus tagasi enam ei mõista.

### 2. Vaata üle öised logid

Otsi eilsetest logidest:

| Mustri | Tegevus |
|--------|---------|
| `CIRCUIT BREAKER TRIPPED` | Kontrolli voog latentsust / VPS võrku |
| `gates_failed': ['shadow']` | Alfa peegeldab müra — vähenda suurust või pausi |
| `FORCE_STOP` | Post-mortem iga sümboli kohta |
| Enamasti `WAIT` | Normaalne. Kahtlane, kui 100% EXECUTE |

### 3. Sea tänased parameetrid (kirjuta üles)

```python
engine = ManifoldEngine(sensitivity=0.05)  # do not change mid-session
gen = AlphaGenerator(
    capital=YOUR_NAV,
    risk_limit=0.02,
    min_volume=YOUR_VENUE_MIN,
    supervisor=RiskSupervisor(max_latency_ms=200),
)
```

**Reegel:** Maksimaalselt üks parameetri muudatus nädalas elus. Muidu backtestid sa päris rahaga.

### 4. Käivita sentinel (esimesed 15 min log-only)

```python
# omega_point.py or your wrapper
omega = OmegaPoint(uri=os.environ["WSS_URI"], capital=NAV)
# First 15 min: patch execute() to log-only
```

Kinnita `latency_us` p99 < 200ms.

---

## Turuaeg (pidev)

### Sündmustsükli vaimne mudel

```text
tick → manifold features → gates → supervisor → your broker adapter
```

### Sinu töö EI ole üle kirjutada

Kui üle kirjutad rohkem kui 2× nädalas, on süsteem valesti seadistatud — paranda parameetreid, ära hero-trade.

### Kiire diagnostika lõik

```python
event = gen.process_tick(tick)
if event:
    print(event.signal, event.action, event.gates_failed, event.supervisor_verdict)
```

### Lõunakontroll (5 min)

- Konto drawdown vs `max_account_drawdown`
- Kas sümbol kinni ekspositsioonis, aga action WAIT (sync bug?)
- Tithe accrual (`tithe_allocation()`) — ainult sanity

---

## Pärastlõuna (lõpetamine)

### 1. Flatten poliitika

Otsusta laua reegel:

- **Auto EXIT** `DRIFT_DECELERATING` korral (juba kallutatud)
- Hard flat T-15 minutit — sinu maakleri cron, mitte UtahIsMyQuant

### 2. Ekspordi `AlphaEvent` log

Append-only JSONL soovitatud:

```python
import json
with open("logs/session.jsonl", "a") as f:
    f.write(json.dumps(event.__dict__, default=str) + "\n")
```

### 3. Sulge puhtalt

```python
omega.shutdown()  # stops shadow thread + supervisor thread
```

---

## Iganädalane (uurimus ilma backtesti teatruta)

| Päev | Ülesanne |
|------|----------|
| E | Vaata värava ebaõnnestumise histogrammi |
| K | Paber-testi üks parameetri muudatus |
| R | Kirjuta 3-lause post-mortem halvimale tehingule |

**Lubatud uurimus:**

- Latentsuse jaotuse graafikud
- Mirror rate vs realis slippage
- Volume gate kalibreerimine

**Keelatud uurimus:**

- „Veel üks backtest 2019 peal“ elava muuduse õigustamiseks täna

---

## Maakleri ühendamine (muster)

```python
async def guarded_execute(tick: Tick, event: AlphaEvent):
    if event.action not in (Action.BUY, Action.SELL, Action.EXIT):
        return
    if event.circuit_breaker:
        return
    await broker.send(symbol=tick.symbol, side=event.action.value, qty=size_from(event))
```

Hoia **idempotentsed** order ID-d. Supervisor võib sundida korduvaid EXIT katseid volatiilsetel tikidel — dedupe sinu poolel.

---

## Integratsioon „tavalise kvant eluga“

| Tegevus | UtahIsMyQuant roll |
|---------|-------------------|
| Hommikune uurimus | Informeerib `min_volume`, mitte diskretion override |
| Makro kalender | Käsitsi paus: kutsu `supervisor.reset_circuit_breaker()` ainult pärast uute entryde peatamist |
| Slack alertid | Hook `EXECUTE_*` ja `FORCE_STOP` |
| Jupyter uurimus | Offline replay `ingest` kaudu, mitte segatud elava tsükliga |
| Nädalavahetuse ML treenimine | Eraldi toru; ära merge kaalusid manifoldi |

---

## Kui kaotad raha

1. Tõmba `gates_failed` selle tehingu jaoks
2. Kontrolli, kas supervisor veto käivitus ja sa ignoreerisid
3. Kui kõik väravad rohelised ja ikka kaotasid: **normaalne**
4. Ära tõsta `risk_limit` samal päeval

---

## Kui teenid raha

Saada autorile midagi, kui saad: **PayPal utah@utahcreates.com** — vaene maintainer fond.

---

## Špargalka

```bash
pytest -q
py omega_point.py
py omega_point.py --uri $env:WSS_URI --live
```

Dokumendid: [API viide](../api-reference.md) | [Tehniline arhitektuur](../technical-architecture.md)
