# Õpetus 02: Esimene replay toru

## Eesmärk

Käivita täielik **sense → decide → protect** tsükkel ilma elava turuandmeta.

## Kood

Salvesta `examples/replay_demo.py`-na või käivita:

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

## Mis juhtus

1. **TickObserver** ingestis JSON tikid
2. **AlphaGenerator** arvutas manifold tunnused + väravad
3. **RiskSupervisor** + symplectic veto võivad tehinguid blokeerida
4. **OmniDiscoveryEngine** sünkis Utahrbitrage + prediction lattice

## Uuri üht sündmust

```python
e = events[-1]
print(e.decision)       # full decision dict
print(e.supervisor_verdict)
print(e.circuit_breaker)
```

## Edasi

[Õpetus 03: Ainult manifold signaalid](03-manifold-signals-only.md)
