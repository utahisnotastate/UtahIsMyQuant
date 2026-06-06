# Миграция: маленький prop shop (3–10 человек) → UtahIsMyQuant

## Вы здесь, если…

- Один квант, один dev, один founder в двух ролях  
- Excel всё ещё где-то участвует  
- «Риск» = размер позиции в голове трейдера  

## Почему это лучший fit

UtahIsMyQuant **компактен**: Python, numpy, asyncio, для v1 не нужен K8s manifest.

| Ресурс | Требование |
|--------|------------|
| Железо | Одна приличная машина или маленький VM |
| Данные | Один WebSocket-фид, за который уже платите |
| Время команды | ~2 недели на replay, ~4 недели на paper |

## Минимальный viable desk

```text
Trader laptop / VPS
  └── py omega_point.py --uri wss://feed --live
  └── logs → ./logs/events.jsonl  (добавьте 20 строк)
  └── broker paper API (подключаете вы)
```

## План по неделям

| Неделя | Результат |
|--------|-----------|
| 1 | `pytest -q` зелёный; replay vendor ticks из CSV → `ingest` |
| 2 | Live sentinel log-only; Slack alert на EXECUTE_* |
| 3 | Paper orders; дневной PnL vs ручная таблица |
| 4 | Go/no-go: макс. 1–2% NAV на `risk_limit` |

## Роли (кто что делает)

| Человек | Задача |
|---------|--------|
| Квант | Настройка `sensitivity`, интерпретация сигналов |
| Dev | WebSocket + адаптер брокера |
| Founder | [Руководство для менеджера](../guides/hedge-fund-manager.md), потолки капитала |

## Что не строить пока

- Кастомные Kubernetes operators  
- 14 рукавов стратегий  
- Замена Bloomberg  

## Сравнение затрат (грубо)

| Статья | Legacy prop spike | UtahIsMyQuant |
|--------|-------------------|---------------|
| MD platform | $2k–30k/мес | Только ваш фид |
| GPU training | $500+/мес | $0 по умолчанию |
| Risk vendor | $5k+/мес | Supervisor в репозитории |

Экономию направьте в **качество данных** и **оплату автору**, если прибыльно: utah@utahcreates.com.

## Подводные камни

- Live до проверки supervisor на устаревших timestamps  
- Один человек в отпуске без runbook `shutdown()`  

## Далее

- [Ежедневный процесс кванта](../guides/quant-daily-workflow.md)
