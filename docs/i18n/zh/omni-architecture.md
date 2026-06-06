# Omni 架构 — TAD 与 Symplectic 加固

## 模块地图

| 模块 | 角色 |
|------|------|
| `adelic_sieve.py` | Adelic Sieve Kernel — 多素数共振、真空检测 |
| `symplectic_veto.py` | Symplectic Veto-Matrix — 容量 + shadow 审计合并 |
| `ghost_rotator.py` | Ghost-Rotation 辛同胚 |
| `transfinite.py` | 相移成交量注入 + 谱方差上限 |
| `utah_flux.py` | 不可变 flux 状态流 |
| `omni_discovery_engine.py` | 主循环：感知 → 审计 → 旋转 → 同步 |
| `utahrbitrage.py` | **Utahrbitrage** — Omega-Point 路由 + tithe 特征值 |

## 执行入口点

```bash
py main.py                    # Omni + Omega replay
py main.py --live --uri wss://...
py main.py --dashboard        # Streamlit Omni-Sieve UI
py omega_point.py             # Classic closed loop (now Omni-enabled)
```

## 信号扩展

| Signal | 含义 |
|--------|------|
| `ADELIC_VOID` | 流动性真空（低跨素数共振） |
| `ADELIC_RESONANCE` | 强多尺度干涉 |

## 实现说明

核心数学使用 **NumPy**（非 JAX）以保持最小依赖。蓝图中的 JAX `@jit` 路径可作为可选扩展稍后添加。

## Utahrbitrage tithe 常数

| 常数 | 值 |
|------|-----|
| `HANS_TITHE_CONSTANT` | 0.023 |
| `HUMANITARIAN_CONSTANT` | 0.015 |

每条 `FluxState` 记录 `utah_route` 与 `humanity_route`。见 [utahrbitrage.md](utahrbitrage.md)。
