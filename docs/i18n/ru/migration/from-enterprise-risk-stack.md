# Миграция: enterprise risk stack → RiskSupervisor UtahIsMyQuant

## Вы здесь, если…

- Pre-trade compliance через vendor RMS (лимиты, fat finger, restricted lists)  
- Intraday risk на отдельном Java-сервисе  
- Kill switch у operations, не у quant-кода  

## Чем UtahIsMyQuant НЕ является

- Не замена **регуляторного** комплаенса (restricted securities, wash sales и т.д.)  
- Не сертифицированный движок **VaR**  
- Не аудит-софт для SEC examinations  

## Чем он ЯВЛЯЕТСЯ

- **Тактический телохранитель** с низкой задержкой, согласованный с потоком тиков  
- **Fourth Law** — единая остановка при bug (убыток) и fix (стоп)  
- **Circuit breaker** на plenum данных (прокси задержки)  

## Слоистая модель риска (рекомендуется)

```text
┌─────────────────────────────────────┐
│  Enterprise RMS (vendor) — ОБЯЗАТЕЛЕН │
├─────────────────────────────────────┤
│  UtahIsMyQuant RiskSupervisor        │
├─────────────────────────────────────┤
│  AlphaGenerator LogicGateMatrix      │
├─────────────────────────────────────┤
│  Execution algos / broker            │
└─────────────────────────────────────┘
```

**Правило:** Enterprise RMS побеждает при конфликте. Supervisor побеждает на sub-second twitch.

## Сопоставление контролей

| Enterprise RMS | RiskSupervisor |
|----------------|----------------|
| Лимит gross exposure | `monitor_exposure` + `max_position_size` |
| Stop loss / trailing | `enforce_stop_loss` |
| Strategy kill switch | `circuit_breaker_active` |
| Model override | `veto_decision` → WAIT |
| Stress scenario | Не встроено — оставить vendor tool |

## Паттерн интеграции

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

## Чеклист cutover

- [ ] Задокументировать двойное одобрение: ops kill switch + ACL `reset_circuit_breaker()`  
- [ ] Сопоставить формат position dict с `RiskSupervisor.update_positions`  
- [ ] Алерт на строку лога `// CIRCUIT BREAKER TRIPPED` (SIEM)  
- [ ] Ежемесячный drill: форсировать высокую задержку → проверить ноль новых ордеров  

## Подводные камни

- Убрать enterprise RMS, потому что «supervisor достаточно» — **нельзя**  
- Игнорировать `gates_failed=supervisor` в архиве комплаенса  

## Далее

- [Руководство для менеджера](../guides/hedge-fund-manager.md)
