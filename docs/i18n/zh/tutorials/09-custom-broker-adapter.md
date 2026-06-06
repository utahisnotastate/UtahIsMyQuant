# 教程 09：自定义券商适配器

## 目标

将 `AlphaEvent` 转为模拟订单（你实现券商 API）。

## 模式

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

## 接入 observer

```python
from src.tick_observer import TickObserver
from src.alpha_generator import AlphaGenerator

observer = TickObserver()
alpha = AlphaGenerator(enable_shadow_audit=False)
alpha.attach(observer)
observer.subscribe(on_alpha)  # your async handler
```

## 幂等性

Supervisor 可能发出重复 EXIT 信号——按 `(symbol, action, tick_id)` 去重。

## 下一步

[教程 10：Streamlit 仪表盘](10-streamlit-dashboard.md)
