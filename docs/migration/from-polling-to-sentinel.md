# Migration: Polling / REST → Sentinel (WebSocket)

## You are here if…

- Prices arrive via `requests.get()`, cron, or 1–5 second polling loops  
- "Real-time" desk means "we refresh fast enough for equities"  
- MDH team owns 40 Python scripts that call the same REST endpoint  

## What changes

| Before | After |
|--------|-------|
| Pull on interval | Push on tick (`websockets`) |
| Blocking I/O in hot path | `asyncio` queue decouples network from logic |
| Latency = poll period + RTT | Latency = processing only (see `latency_us`) |

## Cutover steps

### 1. Mirror your feed format

Map vendor JSON to `Tick.from_payload`:

```python
# Vendor: {"ticker": "SPY", "last": 450.12, "size": 100}
tick = Tick.from_payload({
    "symbol": payload["ticker"],
    "price": payload["last"],
    "volume": payload["size"],
})
```

Or extend `from_payload` with your keys in `tick_observer.py`.

### 2. Stand up sentinel beside polling (week 1–2)

```python
observer = TickObserver(uri="wss://vendor/stream")
observer.subscribe(log_only_handler)  # no execution
observer.start_sentinel()
```

Keep legacy poller running; compare timestamps and last price.

### 3. Measure the slow-data tax

Log `TickObserver.latency_us(tick)` per tick. If p99 > 200ms under load, supervisor will trip circuit breaker—**that's intentional**.

### 4. Decommission poller (week 3+)

- Route production logic through `observer.ingest` or WebSocket only  
- Retire cron jobs; keep one batch job for EOD reconciliation only  

## Pitfalls

| Pitfall | Fix |
|---------|-----|
| WebSocket reconnect storms | Wrap `listen()` with exponential backoff (your adapter) |
| Partial messages | Validate JSON before `queue.put` |
| Symbol mapping drift | Centralize symbology table |
| asyncio in legacy sync app | Run loop in dedicated process (OmegaPoint pattern) |

## Rollback plan

Keep poller read-only for 30 days. If sentinel fails, fall back to poller logs—not silent failure.

## Next

- [Backtest-Heavy → Real-Time](from-backtest-heavy-to-realtime.md)
- [Technical Architecture](../technical-architecture.md)
