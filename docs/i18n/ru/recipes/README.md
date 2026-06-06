# Рецепты кода

Минимальные фрагменты для копирования. Предполагается корень репозитория в `PYTHONPATH` (`pytest.ini` задаёт это).

```python
# В начале скриптов из корня репозитория:
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
```

Или запускайте из корня репозитория: `py your_script.py`

| Рецепт | Описание |
|--------|----------|
| [manifold.md](manifold.md) | Кривизна, энтропия, сигналы |
| [alpha-gates.md](alpha-gates.md) | Логические ворота, решения |
| [utahrbitrage.md](utahrbitrage.md) | Omega-Point маршрутизация |
| [prediction-lattice.md](prediction-lattice.md) | AMI рынков предсказаний |
| [full-tick-handler.md](full-tick-handler.md) | Сквозная обработка тика |
