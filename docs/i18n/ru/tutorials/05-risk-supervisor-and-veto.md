# Учебник 05: Risk supervisor и veto

## Цель

Вызвать **circuit breaker**, symplectic veto и понять `FORCE_STOP` / `GHOST_ROTATION`.

## Circuit breaker (задержка)

```python
from src.risk_supervisor import RiskSupervisor

sup = RiskSupervisor(max_latency_ms=1)
assert sup.check_system_health(500) is False
assert sup.circuit_breaker_active
```

## Symplectic + устаревший тик (интеграция)

Обработайте тики с `timestamp_ns=0` на старом тике — supervisor должен наложить veto или сработать circuit breaker. См. `tests/test_risk_supervisor.py`.

## Fourth Law

`bug` и `fix` оба останавливают — та же граница:

```python
RiskSupervisor.fourth_law_boundary(True, False)  # True
```

## Далее

[Учебник 06: Utahrbitrage и utah-flux](06-utahrbitrage-and-flux.md)
