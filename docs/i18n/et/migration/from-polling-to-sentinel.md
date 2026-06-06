# Migreerimine: polling / REST → Sentinel (WebSocket)

## Sa oled siin, kui…

- Hinnad saabuvad `requests.get()`, cron-i või 1–5 sekundi polling tsüklite kaudu
- „Reaalajas“ laud tähendab „uuendame aktsiate jaoks piisavalt kiiresti“
- MDH meeskond omab 40 Pythoni skripti, mis kutsuvad sama REST endpointi

## Mis muutub

| Enne | Pärast |
|------|--------|
| Pull intervalliga | Push tikil (`websockets`) |
| Blokeeriv I/O kuumteel | `asyncio` queue eraldab võrgu loogikast |
| Latentsus = poll periood + RTT | Latentsus = ainult töötlemine (vaata `latency_us`) |

## Ülemineku sammud

### 1. Peegelda oma voog formaat

Kaardista vendor JSON → `Tick.from_payload`:

```python
# Vendor: {"ticker": "SPY", "last": 450.12, "size": 100}
tick = Tick.from_payload({
    "symbol": payload["ticker"],
    "price": payload["last"],
    "volume": payload["size"],
})
```

Või laienda `from_payload` oma võtmetega `tick_observer.py`-s.

### 2. Seisa sentinel polling kõrval (nädal 1–2)

```python
observer = TickObserver(uri="wss://vendor/stream")
observer.subscribe(log_only_handler)  # no execution
observer.start_sentinel()
```

Hoia pärand pollerit; võrdle ajatempleid ja viimast hinda.

### 3. Mõõda aeglasest andmest maksu

Logi `TickObserver.latency_us(tick)` tik kohta. Kui p99 > 200ms koormuse all, supervisor tripib kaitseautomaadi — **see on taotluslik**.

### 4. Pensioneeri poller (nädal 3+)

- Suuna tootmisloogika `observer.ingest` või ainult WebSocket kaudu
- Pensioneeri cron jobid; hoia üks partiitöö EOD reconciliatsiooniks

## Lõksud

| Lõks | Parandus |
|------|----------|
| WebSocket reconnect tormid | Wrap `listen()` exponential backoff-iga (sinu adapter) |
| Osalised sõnumid | Valideeri JSON enne `queue.put` |
| Sümboli kaardistuse triiv | Tsentraliseeri symbology tabel |
| asyncio pärand sync rakenduses | Käivita loop eraldi protsessis (OmegaPoint muster) |

## Tagasipöördumise plaan

Hoia poller read-only 30 päeva. Kui sentinel ebaõnnestub, lange poller logidele — mitte vaikne ebaõnnestumine.

## Edasi

- [Backtesti-kultuur → reaalajas](from-backtest-heavy-to-realtime.md)
- [Tehniline arhitektuur](../technical-architecture.md)
