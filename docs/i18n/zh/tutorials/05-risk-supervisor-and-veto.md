# 教程 05：风险 Supervisor 与否决

## 目标

触发 **circuit breaker**、symplectic veto，理解 `FORCE_STOP` / `GHOST_ROTATION`。

## Circuit breaker（延迟）

```python
from src.risk_supervisor import RiskSupervisor

sup = RiskSupervisor(max_latency_ms=1)
assert sup.check_system_health(500) is False
assert sup.circuit_breaker_active
```

## Symplectic + 陈旧 tick（集成）

在旧 tick 上用 `timestamp_ns=0` 处理 tick——supervisor 应否决或触发 circuit。见 `tests/test_risk_supervisor.py`。

## Fourth Law

`bug` 与 `fix` 均暂停——同一边界：

```python
RiskSupervisor.fourth_law_boundary(True, False)  # True
```

## 下一步

[教程 06：Utahrbitrage 与 utah-flux](06-utahrbitrage-and-flux.md)
