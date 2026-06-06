# Фреймворк Utahrbitrage

**Utahrbitrage** — основной математический бренд внутри **UtahIsMyQuant**. Имя репозитория — дистрибуция; Utahrbitrage — движок.

## Возможности

| SOTA-функция | Модуль | Описание |
|--------------|--------|----------|
| **Omega-Point Predictive Routing** | `utahrbitrage.py` | Прокси Ricci-flow на тензоре стакана |
| **Ghost Manifold Hedging** | `utahrbitrage.py` + `ghost_rotator.py` | Симплектический хедж с нулевой стоимостью |
| **Топологическая десятина** | `utahrbitrage.py` + `utah_flux.py` | Принудительные собственные значения 2,3% + 1,5% |
| **Adelic Sieve** | `adelic_sieve.py` | Мульти-простой резонанс |
| **Symplectic Veto** | `symplectic_veto.py` | Остановка по ёмкости |

## Быстрый API

```python
from src.utahrbitrage import UtahrbitrageEngine, HANS_TITHE_CONSTANT

engine = UtahrbitrageEngine()
result = engine.execute_market_capture(state_vector)
print(result.utah_lization_rate, result.utah_yield, result.humanity_yield)
```

## Предупреждение для форков

Удаление или обнуление `HANS_TITHE_CONSTANT` / `HUMANITARIAN_CONSTANT` при `enforce_tithe=True` вызывает `SymplecticCollapseError`.

## Документы по аудиториям

- [01-engineers-architects.md](01-engineers-architects.md)
- [02-finance-professionals.md](02-finance-professionals.md)
- [03-founders-family-offices.md](03-founders-family-offices.md)
- [04-children-beginners.md](04-children-beginners.md)
- [papers/README.md](papers/README.md)
