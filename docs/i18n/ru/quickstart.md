# Быстрый старт — UtahIsMyQuant за 10 минут

## Что нужно

- Python 3.11+ (проверено на 3.14)
- Git

## 1. Клонирование и установка

```powershell
git clone https://github.com/utahisnotastate/UtahIsMyQuant.git
cd UtahIsMyQuant
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Проверка

```bash
pytest -q
```

Ожидается: **62 passed** (точное число — у вас локально).

## 3. Демо (без реальных денег)

| Команда | Назначение |
|---------|------------|
| `py omega_point.py` | Замкнутый цикл replay (тики → alpha → риск) |
| `py main.py` | Omni Discovery + Utahrbitrage sync |
| `py main.py --prediction-demo` | Демо Utah Consensus Lattice AMI |
| `py main.py --dashboard` | Интерфейс Streamlit Omni-Sieve |

## 4. Дальше читать

| Цель | Документ |
|------|----------|
| Понять архитектуру | [technical-architecture.md](technical-architecture.md) |
| Готовый код | [tutorials/README.md](tutorials/README.md) |
| Справочник API | [api-reference.md](api-reference.md) |
| Миграция со старого стека | [migration/README.md](migration/README.md) |

## 5. Оплата Utah

Если проект помог: [paying-utah.md](paying-utah.md) — напишите на [utah@utahcreates.com](mailto:utah@utahcreates.com). GUI для платежей в планах.

## 6. Другие языки

English · Eesti · Suomi · 日本語 — отдельные страницы: [languages.md](languages.md)
