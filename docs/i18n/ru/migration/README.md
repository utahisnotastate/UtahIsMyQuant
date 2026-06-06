# Обзор миграции — от legacy хедж-фонда к UtahIsMyQuant

Этот индекс сопоставляет **типичные институциональные установки** с архитектурой UtahIsMyQuant. Каждое руководство включает: что оставляете, что получаете, пошаговый cutover и подводные камни.

## Выберите сценарий

| Если ваш фонд сейчас… | Читайте это |
|-----------------------|-------------|
| Опрашивает REST API по таймеру | [Опрос → Sentinel](from-polling-to-sentinel.md) |
| Живёт в Jupyter-бэктестах | [Бэктесты → реальное время](from-backtest-heavy-to-realtime.md) |
| Гоняет LSTM / непрозрачные ML-стеки | [Чёрный ящик ML → многообразие](from-black-box-ml-to-manifold.md) |
| Использует enterprise risk (MSCI, внутренний RMS) | [Enterprise Risk Stack](from-enterprise-risk-stack.md) |
| Это prop shop на 3–10 человек | [Маленький prop shop](from-small-prop-shop.md) |

## Универсальные принципы миграции

1. **Сначала параллельный запуск** — Логируйте решения UtahIsMyQuant рядом с legacy; не переключайте исполнение в первый день.  
2. **Второй этап — бумажная торговля** — Подключите paper API брокера; проверьте veto supervisor.  
3. **Капитал последним** — Небольшой live-срез после совпадения задержки и stop-loss с ожиданиями.  
4. **Без театра паритета бэктестов** — Старые кривые Sharpe не воспроизведёте; в этом смысл.  
5. **Документируйте сбои ворот** — `AlphaEvent.gates_failed` — ваш аудит-трейл.

## Сопоставление компонентов (Rosetta stone)

| Legacy-концепция | Модуль UtahIsMyQuant |
|------------------|----------------------|
| Market data handler (MDH) | `TickObserver` |
| Alpha model / signal server | `ManifoldEngine` + `AlphaGenerator` |
| Risk engine / pre-trade checks | `LogicGateMatrix` + `RiskSupervisor` |
| Model monitoring / decay | `ShadowTensorAudit` |
| Strategy host / orchestrator | `omega_point.py` |
| Kill switch | `RiskSupervisor.circuit_breaker_active` |

## Шаблон таймлайна (8 недель)

| Неделя | Активность |
|--------|------------|
| 1–2 | Установка, тесты, replay тиков из экспорта исторического фида |
| 3–4 | WebSocket sentinel; режим только лог |
| 5–6 | Бумажное исполнение; настройка `risk_limit`, `max_drawdown` |
| 7 | Подписание менеджером логов veto |
| 8 | Ограниченный live notional |

## Поддержка

Если миграция сэкономила деску реальные деньги: **PayPal [utah@utahcreates.com](mailto:utah@utahcreates.com)** — автор без денег и документирует голодным.
