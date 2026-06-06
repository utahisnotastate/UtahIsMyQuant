# Õpetus 09: Kohandatud maakleri adapter

## Eesmärk

Muuda `AlphaEvent` paberorderiteks (sa implementeerid maakleri API).

## Muster

```python
from src.alpha_generator import Action

async def on_alpha(event):
    if event.circuit_breaker:
        return
    if event.action not in (Action.BUY, Action.SELL, Action.EXIT):
        return
    if event.decision.get("supervisor") in ("VETO", "FORCE_STOP", "GHOST_ROTATION"):
        return
    size = event.decision.get("size", 0)
    # await broker.place_order(symbol=event.symbol, side=event.action.value, qty=size)
    print("PAPER ORDER", event.symbol, event.action, size)
```

## Ühenda observeriga

```python
from src.tick_observer import TickObserver
from src.alpha_generator import AlphaGenerator

observer = TickObserver()
alpha = AlphaGenerator(enable_shadow_audit=False)
alpha.attach(observer)
observer.subscribe(on_alpha)  # your async handler
```

## Idempotentsus

Supervisor võib emitida korduvaid EXIT signaale — dedupe `(symbol, action, tick_id)` järgi.

## Edasi

[Õpetus 10: Streamlit armatuurlaud](10-streamlit-dashboard.md)
