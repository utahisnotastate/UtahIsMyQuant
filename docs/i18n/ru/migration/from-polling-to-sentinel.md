# Миграция: опрос / REST → Sentinel (WebSocket)

## Вы здесь, если…

- Цены приходят через `requests.get()`, cron или циклы опроса 1–5 секунд  
- «Real-time» на деске значит «достаточно быстро для акций»  
- Команда MDH владеет 40 Python-скриптами к одному REST endpoint  

## Что меняется

| Было | Стало |
|------|-------|
| Pull по интервалу | Push на тик (`websockets`) |
| Блокирующий I/O в hot path | `asyncio` queue отделяет сеть от логики |
| Задержка = период опроса + RTT | Задержка = только обработка (см. `latency_us`) |

## Шаги cutover

### 1. Зеркалировать формат фида

Сопоставить vendor JSON с `Tick.from_payload`:

```python
# Vendor: {"ticker": "SPY", "last": 450.12, "size": 100}
tick = Tick.from_payload({
    "symbol": payload["ticker"],
    "price": payload["last"],
    "volume": payload["size"],
})
```

Или расширить `from_payload` своими ключами в `tick_observer.py`.

### 2. Поднять sentinel рядом с опросом (неделя 1–2)

```python
observer = TickObserver(uri="wss://vendor/stream")
observer.subscribe(log_only_handler)  # без исполнения
observer.start_sentinel()
```

Держите legacy poller; сравнивайте timestamps и последнюю цену.

### 3. Измерить налог на медленные данные

Логируйте `TickObserver.latency_us(tick)` на тик. Если p99 > 200ms под нагрузкой, supervisor сработает circuit breaker — **это намеренно**.

### 4. Вывести poller из эксплуатации (неделя 3+)

- Продакшен-логика только через `observer.ingest` или WebSocket  
- Убрать cron; оставить один batch job только для EOD-сверки  

## Подводные камни

| Камень | Исправление |
|--------|-------------|
| Штормы переподключения WebSocket | Обёртка `listen()` с exponential backoff (ваш адаптер) |
| Частичные сообщения | Валидация JSON до `queue.put` |
| Дрейф символов | Централизованная таблица символов |
| asyncio в legacy sync app | Цикл в отдельном процессе (паттерн OmegaPoint) |

## План отката

Держите poller read-only 30 дней. При падении sentinel — откат к логам poller, не тихий сбой.

## Далее

- [Бэктесты → реальное время](from-backtest-heavy-to-realtime.md)
- [Техническая архитектура](../technical-architecture.md)
