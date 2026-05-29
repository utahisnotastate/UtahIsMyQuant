# Tutorial 05: Risk Supervisor and Veto

## Goal

Trigger **circuit breaker**, symplectic veto, and understand `FORCE_STOP` / `GHOST_ROTATION`.

## Circuit breaker (latency)

```python
from src.risk_supervisor import RiskSupervisor

sup = RiskSupervisor(max_latency_ms=1)
assert sup.check_system_health(500) is False
assert sup.circuit_breaker_active
```

## Symplectic + stale tick (integration)

Process ticks with `timestamp_ns=0` on an old tick — supervisor should veto or trip circuit. See `tests/test_risk_supervisor.py`.

## Fourth Law

`bug` and `fix` both halt — same boundary:

```python
RiskSupervisor.fourth_law_boundary(True, False)  # True
```

## Next

[Tutorial 06: Utahrbitrage and utah-flux](06-utahrbitrage-and-flux.md)
