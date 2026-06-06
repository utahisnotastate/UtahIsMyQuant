# 教程 06：Utahrbitrage 与 utah-flux

## 目标

运行 **UtahrbitrageEngine** 并读取 **utah-flux** 状态流。

## Utahrbitrage

[../recipes/utahrbitrage.md](../recipes/utahrbitrage.md)

**勿** 设置 `hans_tithe=0`——会触发 `SymplecticCollapseError`。

## Flux 流

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

## Omni 将两者串联

```bash
py main.py
```

检查日志中的共振与容量。

## 下一步

[教程 07：预测市场 AMI](07-prediction-market-ami.md)
