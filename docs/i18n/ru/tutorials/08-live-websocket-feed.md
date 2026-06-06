# Учебник 08: Live WebSocket-фид

## Цель

Подключить реальный `wss://` tick feed к Sentinel observer.

## Предварительные условия

- WebSocket URL от вашего data vendor  
- Установлен `websockets`  

## Запуск

```bash
py omega_point.py --uri wss://YOUR_FEED_URL --live
```

Или:

```bash
py main.py --uri wss://YOUR_FEED_URL --live
```

## Нормализация JSON

При необходимости расширьте `Tick.from_payload`:

```python
# src/tick_observer.py — добавьте ключи вашего vendor
tick = Tick.from_payload({
    "symbol": payload["ticker"],
    "price": payload["last"],
    "volume": payload["size"],
})
```

## Безопасность

1. **Только бумажная торговля**, пока не проверено поведение veto  
2. Логировать все `EXECUTE_*` в файл  
3. Задать `max_latency_ms` под вашу сеть  

## Далее

[Учебник 09: Свой адаптер брокера](09-custom-broker-adapter.md)
