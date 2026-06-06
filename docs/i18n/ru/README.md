# Документация UtahIsMyQuant

Добро пожаловать в полный набор документации. Выберите руководство, которое соответствует тому, кто вы сегодня — а не тому, что написано в LinkedIn.

## С чего начать

| Аудитория | Документ | Что вы получите |
|-----------|----------|-----------------|
| **Новые пользователи (10 мин)** | [Быстрый старт](quickstart.md) | Установка, тесты, первое демо |
| **Учебники и рецепты** | [tutorials/README.md](tutorials/README.md) | Пошаговые инструкции и готовый код |
| **Оплата Utah** | [paying-utah.md](paying-utah.md) | Напишите Utah; GUI-приложение в планах |
| **Обзор проекта** | [project-overview.md](project-overview.md) | Установка, запуск, юридические оговорки |
| **Языки (отдельные страницы)** | [languages.md](languages.md) | English · Eesti · Suomi · 日本語 |
| **Глоссарий** | [GLOSSARY.md](GLOSSARY.md) | Термины и аббревиатуры |
| **Дети и любопытные** | [Для детей](for-kids.md) | Истории без жаргона |
| **Нетехнические пользователи** | [Для всех](for-everyone.md) | Что делает система — без математической травмы |
| **Инженеры и кванты** | [Техническая архитектура](technical-architecture.md) | Модули, поток данных, параметры |
| **Пользователи API** | [Справочник API](api-reference.md) | Классы, методы, форматы возврата |
| **Omni / TAD / Symplectic** | [Архитектура Omni](omni-architecture.md) | Аделическая сито, veto-matrix, flux |
| **Фреймворк Utahrbitrage** | [Utahrbitrage](utahrbitrage.md) | Omega-Point маршрутизация, константы десятины, ghost hedge |
| **Рынки предсказаний (Polymarket-style)** | [Интеграция рынков предсказаний](prediction_market_integration.md) | Utah Consensus Lattice + AMI |

## Golden Master — руководства по ролям

| № | Аудитория | Документ |
|---|-----------|----------|
| 01 | Инженеры и архитекторы | [01-engineers-architects.md](01-engineers-architects.md) |
| 02 | Финансисты и кванты | [02-finance-professionals.md](02-finance-professionals.md) |
| 03 | Основатели и family offices | [03-founders-family-offices.md](03-founders-family-offices.md) |
| 04 | Дети и начинающие | [04-children-beginners.md](04-children-beginners.md) |

**Фундаментальное доказательство (LaTeX):** [papers/README.md](papers/README.md)

## Миграция со старых стеков хедж-фондов

Уйти от привычки в миллиард долларов — непросто. Эти плейбуки сопоставляют типичные старые миры с UtahIsMyQuant:

| Сценарий | Руководство |
|----------|-------------|
| Опрос / REST / медленные данные | [От опроса к Sentinel](migration/from-polling-to-sentinel.md) |
| Культура бэктестов / переобучение | [От бэктестов к реальному времени](migration/from-backtest-heavy-to-realtime.md) |
| Чёрный ящик ML / зоопарк LSTM | [От чёрного ящика ML к многообразию](migration/from-black-box-ml-to-manifold.md) |
| Корпоративный риск и комплаенс | [От корпоративного риск-стека](migration/from-enterprise-risk-stack.md) |
| Маленький prop shop / lean-команда | [От маленького prop shop](migration/from-small-prop-shop.md) |
| **Индекс миграции** | [Обзор миграции](migration/README.md) |

## Руководства по ролям

| Роль | Руководство |
|------|-------------|
| **Квант (ежедневная интеграция)** | [Ежедневный рабочий процесс кванта](guides/quant-daily-workflow.md) |
| **Управляющий хедж-фондом** | [Руководство для менеджера](guides/hedge-fund-manager.md) |
| **Индекс руководств** | [Обзор руководств](guides/README.md) |

## Быстрые команды

```bash
pip install -r requirements.txt
pytest -q
py examples/replay_demo.py           # минимальный replay
py omega_point.py                    # полный omega replay
py main.py                           # Omni + Utahrbitrage
py main.py --prediction-demo         # prediction AMI
py main.py --dashboard               # Streamlit UI
py omega_point.py --uri wss://... --live
```

## Учебники (путь обучения)

| № | Учебник |
|---|---------|
| 01 | [Установка и проверка](tutorials/01-install-and-verify.md) |
| 02 | [Первый replay-пайплайн](tutorials/02-first-replay-pipeline.md) |
| 03–10 | [Полный индекс](tutorials/README.md) |

## Рецепты кода

[recipes/README.md](recipes/README.md) — готовые фрагменты для manifold, alpha, Utahrbitrage, prediction lattice.

## Карта документов (схема)

```text
                    ┌─────────────────┐
                    │   README.md     │
                    │  (оплата + запуск)│
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
   for-kids.md        for-everyone.md    technical-architecture.md
         │                   │                   │
         └───────────────────┴───────────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        migration/*     guides/*      api-reference.md
```

## Оплата Utah

Если стек помог вам в продакшене, напишите на **[utah@utahcreates.com](mailto:utah@utahcreates.com)**. Подробности: [paying-utah.md](paying-utah.md). Планируется настольное GUI для управления платежами.

## Переводы

| Язык | Хаб |
|------|-----|
| English | [../../README.md](../../README.md) |
| Eesti | [../et/README.md](../et/README.md) |
| Suomi | [../fi/README.md](../fi/README.md) |
| 日本語 | [../ja/README.md](../ja/README.md) |
| 简体中文 | [../zh/README.md](../zh/README.md) |

Полный индекс: [languages.md](languages.md).

*Многообразие не даёт налоговых, юридических или карьерных советов. Зато даёт кривизну.*
