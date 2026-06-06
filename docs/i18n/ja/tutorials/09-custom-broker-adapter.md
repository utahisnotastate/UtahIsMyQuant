# チュートリアル 09: カスタムブローカーアダプター

## 目標

`AlphaEvent` をペーパー注文に変換する（ブローカー API は自分で実装）。

## パターン

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

## オブザーバーに配線

```python
from src.tick_observer import TickObserver
from src.alpha_generator import AlphaGenerator

observer = TickObserver()
alpha = AlphaGenerator(enable_shadow_audit=False)
alpha.attach(observer)
observer.subscribe(on_alpha)  # your async handler
```

## べき等性

スーパーバイザーは繰り返し EXIT を出しうる — `(symbol, action, tick_id)` で重複排除。

## 次へ

[チュートリアル 10: Streamlit ダッシュボード](10-streamlit-dashboard.md)
