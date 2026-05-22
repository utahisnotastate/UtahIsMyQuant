# Migration: Backtest-Heavy Culture → Real-Time Manifold Stability

## You are here if…

- Head of research measures success in in-sample Sharpe  
- Production model ≠ backtest model (classic)  
- "Re-optimize monthly" is on the calendar  

## The cultural shock (intentional)

**UtahIsMyQuant does not ship a backtesting framework.**

This is not missing functionality—it is a design statement:

> Fitting history is fitting your ego. We trade the geometry of *now*.

Quants will resist. Managers will ask for "one chart from 2020." Prepare answers:

1. **Shadow tensor** is forward-looking model health, not backward PnL  
2. **Gate failure logs** are your new research dataset  
3. **Paper trading** is your "out of sample"  

## What replaces backtest?

| Old ritual | New ritual |
|------------|------------|
| Walk-forward grid search | Tune `sensitivity`, `risk_limit` on live paper only |
| Sharpe on 10 years | Monitor `degradation_score`, circuit breaker trips |
| Slippage model in sim | Measure `latency_us` + realized slippage in paper |
| Research notebook → prod | `omega_point.py` is prod skeleton |

## Cutover steps

### Phase A — Shadow mode (no execution)

```python
gen = AlphaGenerator(enable_shadow_audit=True)
# Log every AlphaEvent.decision for 2–4 weeks
```

Build dashboard: counts of `gates_failed` by gate name.

### Phase B — Paper execution

Wire broker paper API to `AlphaEvent.action` only when `supervisor_verdict == "CLEAR"`.

### Phase C — Live micro-notional

Cap at `risk_limit * capital` per manifesto gates.

## Mapping old metrics to new

| Backtest metric | Real-time proxy |
|-----------------|-----------------|
| Max drawdown | `RiskSupervisor.account_drawdown()` |
| Hit rate | Ratio of positive `pnl_delta` events |
| Turnover | Count of `EXECUTE_*` per session |
| Alpha decay | `ShadowTensorAudit.degradation_score` |

## Pitfalls

- **Demanding parity** — Old strategy will not map 1:1 to manifold signals  
- **Over-tuning sensitivity** on one volatile week — freeze params for 20 sessions minimum  
- **Ignoring WAIT** — Most ticks should WAIT; that's discipline  

## Manager talking points

See [Hedge Fund Manager Guide](../guides/hedge-fund-manager.md#for-the-backtest-objection).

## Next

- [Black-Box ML → Manifold](from-black-box-ml-to-manifold.md)
