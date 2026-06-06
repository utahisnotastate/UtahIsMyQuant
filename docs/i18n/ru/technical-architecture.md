# Техническая архитектура

## Обзор системы

UtahIsMyQuant реализует **замкнутый event-driven стек**:

```text
┌──────────────┐     ┌─────────────────┐     ┌──────────────────┐
│ TickObserver │────▶│  AlphaGenerator │────▶│  RiskSupervisor  │
│  (ingest)    │     │ (logic gates)   │◀────│  (veto / exit)   │
└──────┬───────┘     └────────┬────────┘     └──────────────────┘
       │                      │
       │              ┌───────▼────────┐
       │              │ ManifoldEngine │
       │              │ ShadowTensor   │
       │              └────────────────┘
       │
       ▼
  WebSocket / Replay queue
```

Точки входа:

- `omega_point.py` (`OmegaPoint`) — классический замкнутый цикл  
- `main.py` (`OmniDiscoveryEngine`) — Omni/TAD/symplectic + utah-flux

---

## Справочник модулей

### `manifold_kernel.py` — ManifoldEngine (+ adelic)

**Ответственность:** Извлечение признаков из окон цен.

| Метод | Вход | Выход | Заметки |
|-------|------|-------|---------|
| `calculate_curvature` | `price_vector` | `float` | Среднее abs 2-й разности |
| `manifold_drift` | `price_vector` | `float` | Среднее 3-й разности (ускорение) |
| `differential_entropy` | `price_vector` | `float` | KDE по лог-доходностям |
| `adaptive_quantize` | `price_vector` | `ndarray` | `float64` спокойно / `float32` волатильно |
| `adelic_resonance` | prices, volumes | `float` | Сила кросс-простого резонанса |
| `detect_adelic_void` | prices, volumes | `bool` | Обнаружение вакуума ликвидности |
| `generate_signal` | curvature, entropy, drift, adelic state | `str` | Enum сигнала (вкл. `ADELIC_*`) |

**Чувствительность по умолчанию:** `0.05` (порог кривизны для `REVERSAL_IMMINENT`).

**Приоритет сигналов** (первое совпадение побеждает):

1. `REVERSAL_IMMINENT` — curvature > sensitivity  
2. `DRIFT_ACCELERATING` / `DRIFT_DECELERATING` — |drift| > `drift_sensitivity` (1e-3)  
3. `BREAKOUT_PRIMED` — entropy < 85% от baseline  
4. `HOLD`

---

### `tick_observer.py` — TickObserver

**Ответственность:** Асинхронный приём и fan-out.

| Режим | API | Сценарий |
|-------|-----|----------|
| Sentinel | `listen()` + `process()` / `start_sentinel()` | Live WebSocket |
| Replay | `ingest(payload)` + `process()` | Симуляция |
| Bridge | `listen_queue(external_queue)` | Интеграция с legacy |

**Схема Tick:**

```python
Tick(symbol: str, price: float, volume: float = 0, timestamp_ns: int)
```

**Алиасы payload:** `symbol`/`s`, `price`/`p`, `volume`/`v`.

**Задержка:** `TickObserver.latency_us(tick)` → микросекунды с timestamp тика.

---

### `shadow_tensor.py` — ShadowTensorAudit

**Ответственность:** Обнаружение деградации альфы через зеркалирование inverse-manifold.

- Отражает окно цен: `reflected = 2 * anchor - prices`
- Сравнивает прямой сигнал с inverse-сигналом
- `degradation_score` = доля зеркалирования в скользящем окне
- `alpha_healthy()` если score < `mirror_threshold` (по умолчанию 0.55)

Фоновый поток: `start_background(interval=0.5)`.

---

### `alpha_generator.py` — AlphaGenerator

**Ответственность:** Матрица решений logic-gate + учёт PnL/десятины, с опциональными Omni-хуками (TAD, symplectic, utah-flux).

**Ворота LogicGateMatrix:**

| Gate | Ключ | Условие прохождения |
|------|------|---------------------|
| Curvature | `curvature` | Торгуемый сигнал + правила величины |
| Volume | `volume` | `volume >= min_volume` |
| Risk | `risk` | `exposure/capital < risk_limit` (по умолчанию 2%) |
| Shadow | `shadow` | `shadow_healthy == True` |

**Veto supervisor после ворот** (если `supervisor` подключён): может добавить `supervisor` в `gates_failed`.

**Глаголы исполнения:** `WAIT`, `EXECUTE_BUY`, `EXECUTE_SELL`, `EXECUTE_EXIT`.

**Десятина:** `TITHE_RATE = 0.10` с положительного PnL → корзины `FOOD` / `WATER` через `tithe_allocation()`.

---

### `risk_supervisor.py` — RiskSupervisor

**Ответственность:** Телохранитель на уровне портфеля (граница Fourth Law).

| Контроль | По умолчанию | Эффект |
|----------|--------------|--------|
| `max_drawdown` | 5% | `SELL_IMMEDIATE` на позицию |
| `max_position_size` | 10% | Потолок общей экспозиции |
| `max_latency_ms` | 200 | Circuit breaker |
| `max_account_drawdown` | 5% | Остановка на уровне счёта |

**Fourth Law:** `fourth_law_boundary(bug, fix)` → остановка если любое true.

**Интеграция:** `evaluate_tick()` → `veto_decision()` изменяет словарь решения alpha.

---

## Поток данных (один тик)

```text
1. WebSocket recv → JSON → queue.put
2. process() → Tick.from_payload → emit()
3. AlphaGenerator.process_tick:
   a. Добавить price/volume, обрезать окно (по умолчанию 64)
   b. Признаки ManifoldEngine
   c. ShadowTensorAudit.record_tick (опционально)
   d. generate_action (logic gates)
   e. RiskSupervisor.evaluate_tick + veto_decision
   f. decision_to_action → PnL + tithe
4. AlphaEvent возвращается подписчику / логу OmegaPoint
```

---

## Матрица конфигурации

| Параметр | Расположение | Типичный диапазон |
|----------|--------------|-------------------|
| `sensitivity` | ManifoldEngine | 0.01–0.10 |
| `entropy_window` | ManifoldEngine | 16–64 |
| `risk_limit` | AlphaGenerator / LogicGateMatrix | 0.01–0.05 |
| `capital` | AlphaGenerator | NAV счёта |
| `min_volume` | LogicGateMatrix | Зависит от площадки |
| `max_drawdown` | RiskSupervisor | 0.02–0.08 |
| `max_position_size` | RiskSupervisor | 0.05–0.25 |
| `max_latency_ms` | RiskSupervisor | 50–500 |

---

## Зависимости

```text
numpy, scipy    — manifold + adelic math
websockets      — live sentinel
asyncio         — stdlib event loop
streamlit       — Omni-Sieve dashboard (опционально)
pytest          — test harness
```

---

## Тестирование

```bash
pytest -q                           # 62 tests
pytest tests/test_manifold.py -v    # kernel only
pytest tests/test_alpha_gates.py -v # gates only
pytest tests/test_risk_supervisor.py -v
pytest tests/test_omega_point.py -v # integration
```

---

## Точки расширения

1. **Адаптер брокера** — Подписка на `TickObserver`, отправка ордеров по `AlphaEvent.action`
2. **Свой фид** — Реализовать `ingest()` со своей JSON-схемой (расширить `from_payload`)
3. **Дополнительное ворота** — Подкласс `LogicGateMatrix.evaluate()` или обёртка `generate_action`
4. **Distress overlay** — Внешний вход supervisor из Akashic/distress (`data/`)

---

## Безопасность и эксплуатация

- Не коммитьте API-ключи или `.env` с учётными данными  
- Live только с бумажной торговлей, пока не проверено поведение veto/stop  
- Circuit breaker — прокси по задержке, не фид статуса биржи  
- Нет HA/кластеризации — однопроцессная модель asyncio  

---

## Связанные документы

- [Справочник API](api-reference.md)
- [Ежедневный процесс кванта](guides/quant-daily-workflow.md)
- [Руководства по миграции](migration/README.md)
