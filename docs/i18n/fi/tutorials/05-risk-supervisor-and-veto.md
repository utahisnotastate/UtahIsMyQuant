# Opetusohjelma 05: Risk Supervisor ja veto

## Tavoite

Laukaise **circuit breaker**, symplectic veto ja ymmärrä `FORCE_STOP` / `GHOST_ROTATION`.

## Circuit breaker (viive)

```python
from src.risk_supervisor import RiskSupervisor

sup = RiskSupervisor(max_latency_ms=1)
assert sup.check_system_health(500) is False
assert sup.circuit_breaker_active
```

## Symplectic + vanhentunut tick (integraatio)

Prosessoi tickit `timestamp_ns=0` vanhalla tickillä — supervisorin pitäisi vetää veto tai laukaista circuit breaker. Katso `tests/test_risk_supervisor.py`.

## Fourth Law

Sekä `bug` että `fix` pysäyttävät — sama raja:

```python
RiskSupervisor.fourth_law_boundary(True, False)  # True
```

## Seuraavaksi

[Opetusohjelma 06: Utahrbitrage ja utah-flux](06-utahrbitrage-and-flux.md)
