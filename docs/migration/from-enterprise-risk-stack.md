# Migration: Enterprise Risk Stack → UtahIsMyQuant Supervisor

## You are here if…

- Pre-trade compliance via vendor RMS (limits, fat finger, restricted lists)  
- Intraday risk on separate Java service  
- Kill switch owned by operations, not quant code  

## What UtahIsMyQuant is NOT

- Not a replacement for **regulatory** compliance (restricted securities, wash sales, etc.)  
- Not a certified **VaR** engine  
- Not audit software for SEC examinations  

## What it IS

- **Low-latency tactical bodyguard** aligned with tick stream  
- **Fourth Law** unified halt on bug (loss) and fix (stop)  
- **Circuit breaker** on data plenum (latency proxy)  

## Layered risk model (recommended)

```text
┌─────────────────────────────────────┐
│  Enterprise RMS (vendor) — MUST keep │
├─────────────────────────────────────┤
│  UtahIsMyQuant RiskSupervisor        │
├─────────────────────────────────────┤
│  AlphaGenerator LogicGateMatrix      │
├─────────────────────────────────────┤
│  Execution algos / broker            │
└─────────────────────────────────────┘
```

**Rule:** Enterprise RMS wins on conflict. Supervisor wins on sub-second twitch.

## Mapping controls

| Enterprise RMS | RiskSupervisor |
|----------------|----------------|
| Gross exposure limit | `monitor_exposure` + `max_position_size` |
| Stop loss / trailing | `enforce_stop_loss` |
| Strategy kill switch | `circuit_breaker_active` |
| Model override | `veto_decision` → WAIT |
| Stress scenario | Not built-in — keep vendor tool |

## Integration pattern

```python
def pre_send_order(event: AlphaEvent, enterprise_ok: bool) -> bool:
    if not enterprise_ok:
        return False
    if event.circuit_breaker:
        return False
    if event.supervisor_verdict in ("VETO", "FORCE_STOP"):
        return False
    return event.decision["action"].startswith("EXECUTE_")
```

## Cutover checklist

- [ ] Document dual approval: ops kill switch + `reset_circuit_breaker()` ACL  
- [ ] Map position dict format to `RiskSupervisor.update_positions`  
- [ ] Alert on `// CIRCUIT BREAKER TRIPPED` log line (SIEM)  
- [ ] Monthly drill: force high latency → verify zero new orders  

## Pitfalls

- Removing enterprise RMS because "supervisor is enough" — **do not**  
- Ignoring `gates_failed=supervisor` in compliance archive  

## Next

- [Manager Guide](../guides/hedge-fund-manager.md)
