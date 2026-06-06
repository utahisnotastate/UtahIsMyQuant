# Siirtyminen: Polling / REST → Sentinel (WebSocket)

## Olet tässä, jos…

- Hinnat saapuvat `requests.get()`-kutsulla, cronilla tai 1–5 sekunnin polling-silmukoilla
- "Reaaliaikainen" pöytä tarkoittaa "päivitämme tarpeeksi nopeasti osakkeille"
- MDH-tiimi omistaa 40 Python-skriptiä, jotka kutsuvat samaa REST-päätettä

## Mitä muuttuu

| Ennen | Jälkeen |
|-------|---------|
| Pull väliajoin | Push tickillä (`websockets`) |
| Blokkaava I/O hot pathissa | `asyncio`-jono erottaa verkon logiikasta |
| Viive = poll-jakso + RTT | Viive = vain prosessointi (katso `latency_us`) |

## Cutover-vaiheet

### 1. Peilaa feed-muotosi

Kartoita vendor JSON → `Tick.from_payload`:

```python
# Vendor: {"ticker": "SPY", "last": 450.12, "size": 100}
tick = Tick.from_payload({
    "symbol": payload["ticker"],
    "price": payload["last"],
    "volume": payload["size"],
})
```

Tai laajenna `from_payload` omilla avaimillasi `tick_observer.py`-tiedostossa.

### 2. Pystytä sentinel pollingin rinnalle (viikko 1–2)

```python
observer = TickObserver(uri="wss://vendor/stream")
observer.subscribe(log_only_handler)  # no execution
observer.start_sentinel()
```

Pidä legacy-poller käynnissä; vertaa aikaleimoja ja viimeistä hintaa.

### 3. Mittaa hitaan datan vero

Lokita `TickObserver.latency_us(tick)` per tick. Jos p99 > 200ms kuormalla, supervisor laukaisee circuit breakerin — **tarkoituksella**.

### 4. Poista poller käytöstä (viikko 3+)

- Reititä tuotantologiikan `observer.ingest`- tai WebSocket-only-polun kautta
- Poista cron-työt; pidä yksi erätyö vain EOD-täsmäytykseen

## Sudenkuopat

| Sudenkuoppa | Korjaus |
|-------------|---------|
| WebSocket-uudelleenyhdistämismyrskyt | Kääri `listen()` eksponentiaalisella backoffilla (adapterisi) |
| Osittaiset viestit | Validoi JSON ennen `queue.put` |
| Symbolikartoitus drift | Keskitä symbologiatabeli |
| asyncio legacy-synk-sovelluksessa | Aja loop erillisessä prosessissa (OmegaPoint-malli) |

## Rollback-suunnitelma

Pidä poller read-only 30 päivää. Jos sentinel kaatuu, fallback poller-lokeihin — ei hiljaista epäonnistumista.

## Seuraavaksi

- [Backtest-painotteinen → reaaliaika](from-backtest-heavy-to-realtime.md)
- [Tekninen arkkitehtuuri](../technical-architecture.md)
