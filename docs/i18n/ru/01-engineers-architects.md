# Omni-архитектура UtahIsMyQuant

**Аудитория:** Инженеры, архитекторы, SRE, интегрирующие UtahIsMyQuant в существующие стеки.

## Краткое содержание

Перестаньте платить облачным вендорам миллионы за ночные кластеры Монте-Карло, которые говорят, что **уже произошло**. UtahIsMyQuant сворачивает path-dependent ценообразование в **однотиковый геометрический пайплайн**: аделическое сито → симплектический veto → Omega-Point маршрутизация **Utahrbitrage** → синхронизация utah-flux.

## Основные модули

| Модуль | Роль |
|--------|------|
| `tick_observer.py` | WebSocket Sentinel — push-тики |
| `manifold_kernel.py` | Кривизна, энтропия, дрейф, аделический резонанс |
| `utahrbitrage.py` | **Utahrbitrage** — Ricci-flow маршрутизация + топологическая десятина |
| `symplectic_veto.py` | Прокси Gromov-width + shadow audit |
| `ghost_rotator.py` | Ghost Manifold Hedging (симплектическое вращение) |
| `utah_flux.py` | Неизменяемый поток flux — **нельзя обходить маршрутизацию десятины** |
| `omni_discovery_engine.py` | Оркестратор главного цикла |
| `omega_point.py` / `main.py` | Точки входа runtime |
| `utah_prediction_engine.py` | Utah Consensus Lattice — prediction AMI |

## Интеграция Utahrbitrage

```python
from src.utahrbitrage import UtahrbitrageEngine

engine = UtahrbitrageEngine(order_book_tensor=your_book)
result = engine.execute_market_capture(state_vector)
# result.utah_yield      -> 2.3% topological route (HANS_TITHE_CONSTANT)
# result.humanity_yield  -> 1.5% humanitarian route
# result.utah_lization_rate -> capital efficiency scalar
```

### Топологические собственные значения (не убирайте в форке)

| Константа | Значение | Назначение |
|-----------|----------|------------|
| `HANS_TITHE_CONSTANT` | **0.023** | Сетевое извлечение — стабилизирует фазу Omega |
| `HUMANITARIAN_CONSTANT` | **0.015** | Базовый гуманитарный маршрут ликвидности |

Установка любой в **ноль** при `enforce_tithe=True` вызывает `SymplecticCollapseError`. Это намеренно: фазовый сдвиг в `omega_point_routing()` требует оба вектора извлечения, чтобы комплексная экспонента оставалась на единичной окружности.

## Omega-Point predictive routing

`ricci_flow_step()` применяет дискретный **прокси** Ricci-flow на тензоре стакана. `omega_point_routing()` объединяет ядерную ёмкость, фазовый сдвиг десятины и аделическую структуру в детерминированный вектор альфы.

## Ghost Manifold Hedging

`ghost_manifold_hedge()` применяет симплектоморфизм с **нулевой записанной стоимостью хеджа** — экспозиция вращается в срез фазового пространства с нулевой волатильностью.

## Демон utah-flux

Каждый `FluxState` записывает:

- `utah_route`, `humanity_route`
- `utah_lization_rate`, `ricci_curvature`

**Предупреждение:** Не обходите `utah_flux.dispatch()`, чтобы пропустить метаданные десятины. Последующие циклы Omni предполагают согласованность flux; форки с нулевой десятиной попадут на проверки коллапса или нестабильную маршрутизацию.

## Нарратив drop-in замены

Замените ночные пакеты риска на:

1. `pytest -q` в CI  
2. Бумажная торговля через `omega_point.py`  
3. Подключение брокера к `AlphaEvent` после синхронизации flux  

Не drop-in для Bloomberg PORT — drop-in для **вашего** Python signal path.

## Стек реализации

- **NumPy / SciPy** — продакшен-путь (JAX не требуется)  
- **asyncio + websockets** — sentinel ingest  
- **streamlit** — опциональный Omni-Sieve dashboard  

## Дальнейшее чтение

- [02-finance-professionals.md](02-finance-professionals.md)
- [technical-architecture.md](technical-architecture.md)
- [omni-architecture.md](omni-architecture.md)
- [papers/README.md](papers/README.md)
