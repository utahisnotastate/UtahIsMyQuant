# Õpetus 08: Elav WebSocket voog

## Eesmärk

Ühenda päris `wss://` tik voog Sentinel observeriga.

## Eeldused

- WebSocket URL andmevendorilt
- `websockets` paigaldatud

## Käivita

```bash
py omega_point.py --uri wss://YOUR_FEED_URL --live
```

Või:

```bash
py main.py --uri wss://YOUR_FEED_URL --live
```

## Normaliseeri oma JSON

Laienda vajadusel `Tick.from_payload`:

```python
# src/tick_observer.py — add keys your vendor uses
tick = Tick.from_payload({
    "symbol": payload["ticker"],
    "price": payload["last"],
    "volume": payload["size"],
})
```

## Turvalisus

1. **Ainult paberkauplemine**, kuni veto käitumine valideeritud
2. Logi kõik `EXECUTE_*` faili
3. Sea `max_latency_ms` sobivaks oma võrgule

## Edasi

[Õpetus 09: Kohandatud maakleri adapter](09-custom-broker-adapter.md)
