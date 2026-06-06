# Õpetus 05: Risk Supervisor ja veto

## Eesmärk

Käivita **kaitseautomaat**, symplectic veto ja mõista `FORCE_STOP` / `GHOST_ROTATION`.

## Kaitseautomaat (latentsus)

```python
from src.risk_supervisor import RiskSupervisor

sup = RiskSupervisor(max_latency_ms=1)
assert sup.check_system_health(500) is False
assert sup.circuit_breaker_active
```

## Symplectic + aegunud tik (integratsioon)

Töötle tikke `timestamp_ns=0` vanal tikil — supervisor peaks veto tegema või kaitseautomaadi tripima. Vaata `tests/test_risk_supervisor.py`.

## Fourth Law

`bug` ja `fix` mõlemad peatavad — sama piir:

```python
RiskSupervisor.fourth_law_boundary(True, False)  # True
```

## Edasi

[Õpetus 06: Utahrbitrage ja utah-flux](06-utahrbitrage-and-flux.md)
