# Siirtyminen: Yritysriskipino → UtahIsMyQuant Supervisor

## Olet tässä, jos…

- Esikauppa-compliance vendor RMS:llä (rajat, fat finger, restricted lists)
- Päivänsisäinen riski erillisessä Java-palvelussa
- Kill switch opsin hallussa, ei quant-koodissa

## Mitä UtahIsMyQuant EI ole

- Korvike **sääntely**-compliancelle (restricted securities, wash sales jne.)
- Sertifioitu **VaR**-moottori
- Audit-ohjelmisto SEC-tutkimuksille

## Mitä se ON

- **Matalan viiveen taktinen bodyguard** tick-virran mukana
- **Fourth Law** yhdistetty pysäytys bugiin (tappio) ja fixiin (stop)
- **Circuit breaker** dataplenumilla (viiveproxy)

## Kerroksittainen riskimalli (suositeltu)

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

**Sääntö:** Enterprise RMS voittaa konfliktissa. Supervisor voittaa subsekuntitwitchissä.

## Kontrollien kartoitus

| Enterprise RMS | RiskSupervisor |
|----------------|----------------|
| Gross exposure limit | `monitor_exposure` + `max_position_size` |
| Stop loss / trailing | `enforce_stop_loss` |
| Strategy kill switch | `circuit_breaker_active` |
| Model override | `veto_decision` → WAIT |
| Stress scenario | Ei sisäänrakennettu — pidä vendor-työkalu |

## Integraatiomalli

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

## Cutover-tarkistuslista

- [ ] Dokumentoi kaksinkertainen hyväksyntä: ops kill switch + `reset_circuit_breaker()` ACL
- [ ] Kartoita position dict -muoto → `RiskSupervisor.update_positions`
- [ ] Hälytys `// CIRCUIT BREAKER TRIPPED` -lokiriville (SIEM)
- [ ] Kuukausittainen harjoitus: pakota korkea viive → varmista nolla uutta orderia

## Sudenkuopat

- Enterprise RMS:n poistaminen, koska "supervisor riittää" — **älä tee**
- `gates_failed=supervisor` sivuuttaminen compliance-arkistossa

## Seuraavaksi

- [Johtajan opas](../guides/hedge-fund-manager.md)
