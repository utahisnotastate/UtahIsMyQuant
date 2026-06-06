# Ежедневный рабочий процесс кванта — интеграция UtahIsMyQuant в реальную жизнь

Как использовать UtahIsMyQuant **каждый торговый день**, не превращая его в ещё один заброшенный репозиторий на ноутбуке.

---

## Утро (до рынка, 30–45 мин)

### 1. Проверка здоровья

```powershell
cd UtahIsMyQuant
.venv\Scripts\activate
pytest -q
```

Если красное: **не торговать**. Сначала исправьте тесты — они охраняют математику, которую вы перестали понимать полгода назад.

### 2. Обзор ночных логов

Ищите в логах вчера:

| Паттерн | Действие |
|---------|----------|
| `CIRCUIT BREAKER TRIPPED` | Проверить задержку фида / сеть VPS |
| `gates_failed': ['shadow']` | Альфа зеркалит шум — уменьшить размер или пауза |
| `FORCE_STOP` | Post-mortem по каждому символу |
| В основном `WAIT` | Нормально. Подозрительно, если 100% EXECUTE |

### 3. Задать параметры на сегодня (записать)

```python
engine = ManifoldEngine(sensitivity=0.05)  # не менять в сессии
gen = AlphaGenerator(
    capital=YOUR_NAV,
    risk_limit=0.02,
    min_volume=YOUR_VENUE_MIN,
    supervisor=RiskSupervisor(max_latency_ms=200),
)
```

**Правило:** Максимум одно изменение параметра в неделю в live. Иначе вы бэктестите на реальных деньгах.

### 4. Запустить sentinel (первые 15 мин только лог)

```python
# omega_point.py или ваша обёртка
omega = OmegaPoint(uri=os.environ["WSS_URI"], capital=NAV)
# Первые 15 мин: patch execute() в log-only
```

Подтвердить p99 `latency_us` < 200ms.

---

## Часы рынка (непрерывно)

### Ментальная модель event loop

```text
tick → manifold features → gates → supervisor → ваш адаптер брокера
```

### Ваша работа — НЕ перебивать

Если перебиваете чаще 2× в неделю — система настроена неверно; чините параметры, не геройствуйте.

### Быстрый диагностический фрагмент

```python
event = gen.process_tick(tick)
if event:
    print(event.signal, event.action, event.gates_failed, event.supervisor_verdict)
```

### Обеденная проверка (5 мин)

- Просадка счёта vs `max_account_drawdown`  
- Символ застрял в экспозиции при action WAIT (баг синхронизации?)  
- Начисление десятины (`tithe_allocation()`) — только sanity  

---

## После обеда (сворачивание)

### 1. Политика закрытия

Правило деска:

- **Авто EXIT** на `DRIFT_DECELERATING` (уже заложено)  
- Жёсткое закрытие за T-15 минут — cron брокера, не UtahIsMyQuant  

### 2. Экспорт лога `AlphaEvent`

Рекомендуется append-only JSONL:

```python
import json
with open("logs/session.jsonl", "a") as f:
    f.write(json.dumps(event.__dict__, default=str) + "\n")
```

### 3. Чистое завершение

```python
omega.shutdown()  # останавливает shadow thread + supervisor thread
```

---

## Еженедельно (исследования без театра бэктестов)

| День | Задача |
|------|--------|
| Пн | Гистограмма сбоев ворот |
| Ср | Бумажный тест одного изменения параметра |
| Пт | Post-mortem из 3 предложений для худшей сделки |

**Разрешённые исследования:**

- Графики распределения задержки  
- Mirror rate vs реализованный slippage  
- Калибровка volume gate  

**Запрещённые исследования:**

- «Ещё один бэктест на 2019» чтобы оправдать live-изменение сегодня  

---

## Подключение брокера (паттерн)

```python
async def guarded_execute(tick: Tick, event: AlphaEvent):
    if event.action not in (Action.BUY, Action.SELL, Action.EXIT):
        return
    if event.circuit_breaker:
        return
    await broker.send(symbol=tick.symbol, side=event.action.value, qty=size_from(event))
```

Держите **идемпотентные** order ID. Supervisor может форсировать повторные EXIT на волатильных тиках — дедуплицируйте на своей стороне.

---

## Интеграция с «обычной жизнью кванта»

| Активность | Роль UtahIsMyQuant |
|------------|-------------------|
| Утреннее чтение research | Влияет на `min_volume`, не на дискреционный override |
| Макро-календарь | Ручная пауза: `supervisor.reset_circuit_breaker()` только после самостоятельной остановки новых входов |
| Slack-алерты | Хук на `EXECUTE_*` и `FORCE_STOP` |
| Jupyter-исследования | Offline replay через `ingest`, никогда в live loop |
| Weekend ML training | Отдельный пайплайн; не сливать веса в manifold |

---

## Когда теряете деньги

1. Вытянуть `gates_failed` для той сделки  
2. Проверить, сработал ли veto supervisor и вы его проигнорировали  
3. Если все ворота зелёные и всё равно убыток: **нормально**  
4. Не поднимать `risk_limit` в тот же день  

---

## Когда зарабатываете

Отправьте автору что-нибудь, если можете: **PayPal utah@utahcreates.com** — фонд broke maintainer.

---

## Шпаргалка

```bash
pytest -q
py omega_point.py
py omega_point.py --uri $env:WSS_URI --live
```

Документы: [Справочник API](../api-reference.md) | [Техническая архитектура](../technical-architecture.md)
