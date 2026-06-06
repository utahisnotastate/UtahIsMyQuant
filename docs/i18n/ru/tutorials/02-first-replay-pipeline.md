# Учебник 02: Первый replay-пайплайн

## Цель

Запустить полный цикл **sense → decide → protect** без live-рыночных данных.

## Код

Сохраните как `examples/replay_demo.py` или запустите:

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

## Что произошло

1. **TickObserver** принял JSON-тики  
2. **AlphaGenerator** вычислил признаки manifold + ворота  
3. **RiskSupervisor** + symplectic veto могли заблокировать сделки  
4. **OmniDiscoveryEngine** синхронизировал Utahrbitrage + prediction lattice  

## Изучить одно событие

```python
e = events[-1]
print(e.decision)       # full decision dict
print(e.supervisor_verdict)
print(e.circuit_breaker)
```

## Далее

[Учебник 03: Только сигналы manifold](03-manifold-signals-only.md)
