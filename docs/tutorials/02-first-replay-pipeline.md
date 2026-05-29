# Tutorial 02: First Replay Pipeline

## Goal

Run the full **sense → decide → protect** loop without live market data.

## Code

Save as `examples/replay_demo.py` or run:

```bash
py examples/replay_demo.py
```

```python
import asyncio
from omega_point import OmegaPoint

async def main():
    omega = OmegaPoint(capital=100_000)
    ticks = [
        {"symbol": "SPY", "price": 450.0 + i * 0.1, "volume": 5000}
        for i in range(25)
    ]
    events = await omega.run_replay(ticks)
    print(f"Processed {len(events)} alpha events")
    if events:
        last = events[-1]
        print("Last:", last.signal, last.action, last.gates_failed)
    omega.shutdown()

asyncio.run(main())
```

## What happened

1. **TickObserver** ingested JSON ticks  
2. **AlphaGenerator** computed manifold features + gates  
3. **RiskSupervisor** + symplectic veto may block trades  
4. **OmniDiscoveryEngine** synced Utahrbitrage + prediction lattice  

## Inspect one event

```python
e = events[-1]
print(e.decision)       # full decision dict
print(e.supervisor_verdict)
print(e.circuit_breaker)
```

## Next

[Tutorial 03: Manifold signals only](03-manifold-signals-only.md)
