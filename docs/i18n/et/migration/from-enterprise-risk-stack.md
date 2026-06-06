# Migreerimine: ettevõtte riskivirn → UtahIsMyQuant Supervisor

## Sa oled siin, kui…

- Eelkaubelduse vastavus vendor RMS kaudu (limiidid, fat finger, restricted lists)
- Intraday risk eraldi Java teenuses
- Kill switch kuulub operatsioonidele, mitte kvant koodile

## Mida UtahIsMyQuant EI ole

- Asendus **regulatiivsele** vastavusele (restricted securities, wash sales jne)
- Sertifitseeritud **VaR** mootor
- Audit tarkvara SEC eksamite jaoks

## Mida see ON

- **Madala latentsuse taktikaline ihukaitsja** tik vooga joondatud
- **Fourth Law** ühtne peatus vea (kahjum) ja paranduse (stop) korral
- **Kaitseautomaat** andme plenumil (latentsuse proksi)

## Kihiline riskimudel (soovitatud)

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

**Reegel:** Enterprise RMS võidab konfliktil. Supervisor võidab sub-sekundi tikil.

## Kontrollide kaardistus

| Enterprise RMS | RiskSupervisor |
|----------------|----------------|
| Gross exposure limit | `monitor_exposure` + `max_position_size` |
| Stop loss / trailing | `enforce_stop_loss` |
| Strateegia kill switch | `circuit_breaker_active` |
| Mudeli override | `veto_decision` → WAIT |
| Stress stsenaarium | Pole sisseehitatud — hoia vendori tööriist |

## Integratsiooni muster

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

## Ülemineku kontrollnimekiri

- [ ] Dokumenteeri dual approval: ops kill switch + `reset_circuit_breaker()` ACL
- [ ] Kaardista position dict formaat → `RiskSupervisor.update_positions`
- [ ] Alert `// CIRCUIT BREAKER TRIPPED` log real (SIEM)
- [ ] Igakuine drill: sunni kõrge latentsus → kontrolli null uut orderit

## Lõksud

- Enterprise RMS eemaldamine, sest „supervisor piisab“ — **ära tee**
- `gates_failed=supervisor` ignoreerimine vastavus arhiivis

## Edasi

- [Juhi juhend](../guides/hedge-fund-manager.md)
