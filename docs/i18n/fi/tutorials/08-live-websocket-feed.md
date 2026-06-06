# Opetusohjelma 08: Live WebSocket-feed

## Tavoite

Kytke oikea `wss://` tick-feed Sentinel-observeriin.

## Edellytykset

- WebSocket-URL datalähteeltäsi
- `websockets` asennettuna

## Aja

```bash
py omega_point.py --uri wss://YOUR_FEED_URL --live
```

Tai:

```bash
py main.py --uri wss://YOUR_FEED_URL --live
```

## Normalisoi JSON

Laajenna `Tick.from_payload` tarvittaessa:

```python
# src/tick_observer.py — add keys your vendor uses
tick = Tick.from_payload({
    "symbol": payload["ticker"],
    "price": payload["last"],
    "volume": payload["size"],
})
```

## Turvallisuus

1. **Vain paperikauppa**, kunnes veto-käyttäytyminen validoitu
2. Lokita kaikki `EXECUTE_*` tiedostoon
3. Aseta `max_latency_ms` verkkoosi sopivaksi

## Seuraavaksi

[Opetusohjelma 09: Custom broker adapter](09-custom-broker-adapter.md)
