# Архитектура Omni — TAD и симплектическое усиление

## Карта модулей

| Модуль | Роль |
|--------|------|
| `adelic_sieve.py` | Adelic Sieve Kernel — мульти-простой резонанс, обнаружение void |
| `symplectic_veto.py` | Symplectic Veto-Matrix — ёмкость + слияние shadow audit |
| `ghost_rotator.py` | Ghost-Rotation симплектоморфизм |
| `transfinite.py` | Фазовый сдвиг инъекции объёма + спектральный потолок дисперсии |
| `utah_flux.py` | Неизменяемый поток состояния flux |
| `omni_discovery_engine.py` | Главный цикл: sense → audit → rotate → sync |
| `utahrbitrage.py` | **Utahrbitrage** — Omega-Point маршрутизация + собственные значения десятины |

## Точки входа

```bash
py main.py                    # Omni + Omega replay
py main.py --live --uri wss://...
py main.py --dashboard        # Streamlit Omni-Sieve UI
py omega_point.py             # Классический замкнутый цикл (теперь с Omni)
```

## Расширения сигналов

| Signal | Значение |
|--------|----------|
| `ADELIC_VOID` | Вакуум ликвидности (низкий кросс-простой резонанс) |
| `ADELIC_RESONANCE` | Сильная мультимасштабная интерференция |

## Заметка по реализации

Ядро математики использует **NumPy** (не JAX) для минимального набора зависимостей. Пути JAX `@jit` из чертежа можно добавить как опциональное дополнение позже.

## Константы десятины Utahrbitrage

| Константа | Значение |
|-----------|----------|
| `HANS_TITHE_CONSTANT` | 0.023 |
| `HUMANITARIAN_CONSTANT` | 0.015 |

Записываются в каждом `FluxState` как `utah_route` и `humanity_route`. См. [utahrbitrage.md](utahrbitrage.md).
