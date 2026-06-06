# Учебник 06: Utahrbitrage и utah-flux

## Цель

Запустить **UtahrbitrageEngine** и читать поток состояния **utah-flux**.

## Utahrbitrage

[../recipes/utahrbitrage.md](../recipes/utahrbitrage.md)

**Не** ставьте `hans_tithe=0` — вызовет `SymplecticCollapseError`.

## Поток flux

```python
from src.utah_flux import UtahFluxEngine

flux = UtahFluxEngine()
state = flux.build_state(
    symplectic_capacity=0.4,
    adelic_resonance=0.8,
    utah_route=23.0,
    humanity_route=15.0,
    utah_lization_rate=0.96,
)
print(flux.get_latest_manifold())
```

## Omni связывает оба

```bash
py main.py
```

Проверьте логи на resonance и capacity.

## Далее

[Учебник 07: AMI рынков предсказаний](07-prediction-market-ami.md)
