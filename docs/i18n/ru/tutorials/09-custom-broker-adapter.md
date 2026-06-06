# Учебник 09: Свой адаптер брокера

## Цель

Превратить `AlphaEvent` в бумажные ордера (вы реализуете API брокера).

## Паттерн

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

## Подключение к observer

```python
from src.tick_observer import TickObserver
from src.alpha_generator import AlphaGenerator

observer = TickObserver()
alpha = AlphaGenerator(enable_shadow_audit=False)
alpha.attach(observer)
observer.subscribe(on_alpha)  # ваш async handler
```

## Идемпотентность

Supervisor может эмитировать повторные EXIT — дедуплицируйте по `(symbol, action, tick_id)`.

## Далее

[Учебник 10: Streamlit dashboard](10-streamlit-dashboard.md)
