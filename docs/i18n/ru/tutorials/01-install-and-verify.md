# Учебник 01: Установка и проверка

## Цель

Клонировать UtahIsMyQuant, установить зависимости и подтвердить, что все тесты проходят.

## Шаги

### 1. Клонирование

```bash
git clone https://github.com/utahisnotastate/UtahIsMyQuant.git
cd UtahIsMyQuant
```

### 2. Виртуальное окружение

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Запуск тестов

```bash
pytest -q
```

### 4. Изучить структуру

```text
src/           Ядро движков
tests/         62+ unit tests
omega_point.py Замкнутый цикл runner
main.py        Omni + prediction demos
docs/          Вся документация
examples/      Запускаемые примеры
```

### 5. Первое демо

```bash
py omega_point.py
```

В логах должны быть строки, заканчивающиеся на `// OMEGA COMPLETE`.

## Устранение неполадок

| Проблема | Решение |
|----------|---------|
| `python` не найден | На Windows используйте `py` |
| Ошибка импорта `websockets` | `pip install -r requirements.txt` |
| Тесты зависают | Убедитесь, что нет zombie Python; `pytest -q --maxfail=1` |

## Далее

[Учебник 02: Первый replay-пайплайн](02-first-replay-pipeline.md)
