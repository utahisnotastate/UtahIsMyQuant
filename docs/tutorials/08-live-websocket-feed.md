# Tutorial 08: Live WebSocket Feed

## Goal

Connect a real `wss://` tick feed to the Sentinel observer.

## Prerequisites

- WebSocket URL from your data vendor  
- `websockets` installed  

## Run

```bash
py omega_point.py --uri wss://YOUR_FEED_URL --live
```

Or:

```bash
py main.py --uri wss://YOUR_FEED_URL --live
```

## Normalize your JSON

Extend `Tick.from_payload` if needed:

```python
# src/tick_observer.py — add keys your vendor uses
tick = Tick.from_payload({
    "symbol": payload["ticker"],
    "price": payload["last"],
    "volume": payload["size"],
})
```

## Safety

1. **Paper trade only** until veto behavior validated  
2. Log all `EXECUTE_*` to file  
3. Set `max_latency_ms` appropriate for your network  

## Next

[Tutorial 09: Custom broker adapter](09-custom-broker-adapter.md)
