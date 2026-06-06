# Opetusohjelma 02: Ensimmäinen replay-putki

## Tavoite

Aja täysi **sense → decide → protect** -silmukka ilman live-markkinadataa.

## Koodi

Tallenna `examples/replay_demo.py`-tiedostoon tai aja:

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

## Mitä tapahtui

1. **TickObserver** ingestoi JSON-tickit
2. **AlphaGenerator** laski monisto-ominaisuudet + gateet
3. **RiskSupervisor** + symplectic veto voi estää kauppoja
4. **OmniDiscoveryEngine** synkronoi Utahrbitragen + prediction latticen

## Tarkastele yhtä tapahtumaa

```python
e = events[-1]
print(e.decision)       # full decision dict
print(e.supervisor_verdict)
print(e.circuit_breaker)
```

## Seuraavaksi

[Opetusohjelma 03: Vain monistosignaalit](03-manifold-signals-only.md)
