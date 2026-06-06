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
| `py omega_point.py` | Замкнутый цикл: тики → альфа → риск |
| `py main.py` | Omni Discovery + Utahrbitrage |
| `py main.py --prediction-demo` | Utah Consensus Lattice (AMI) |
| `py main.py --dashboard` | Интерфейс Streamlit |

## 4. Дальше читать

| Цель | Документ |
|------|----------|
| Обзор без жаргона | [for-everyone.md](for-everyone.md) |
| Поддержка автора | [paying-utah.md](paying-utah.md) |
| Архитектура | [../../technical-architecture.md](../../technical-architecture.md) **(English)** |
| API | [../../api-reference.md](../../api-reference.md) **(English)** |

## 5. Навигация

- [Главная русская страница](README.md)
- [Все языки](../../languages.md) **(English)**
