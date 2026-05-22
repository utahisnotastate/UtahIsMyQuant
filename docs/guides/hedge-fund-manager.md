# Hedge Fund Manager Guide — Oversight Without Reading Python

You run capital. You do not need to import scipy. You need **control, narrative, and downside bounds**.

---

## What UtahIsMyQuant gives your fund

| Benefit | Mechanism |
|---------|-----------|
| Faster awareness | WebSocket sentinel vs polling |
| Explainable decisions | Every trade has `reason` + `gates_passed/failed` |
| Intraday survival tools | Stop-loss, exposure cap, circuit breaker |
| Audit trail | `AlphaEvent` logs (when your team wires them) |
| No backtest fantasy | Forces honesty about live behavior |

## What it does NOT give you

- Regulatory compliance package  
- Investor reporting templates  
- Guaranteed returns  
- A reason to fire your risk officer  

---

## Questions to ask your quant team (weekly)

1. **What % of ticks were WAIT?**  
   - Healthy: high WAIT, low EXECUTE  
   - Unhealthy: EXECUTE on every tick (gates too loose)

2. **How many circuit breaker trips this week?**  
   - Zero forever: threshold maybe too loose  
   - Daily: infrastructure problem

3. **Shadow tensor health?**  
   - `degradation_score` trending up → alpha decay / noise trading

4. **Largest single gate failure category?**  
   - Informs whether problem is signal, liquidity, or risk limit

5. **Did we override the system manually?**  
   - More than twice/week → system or discipline failure

---

## Dashboards to request (minimal)

Your team can build these from JSONL logs in a day:

| Panel | Metric |
|-------|--------|
| Signal mix | Count by `signal` type |
| Action mix | BUY / SELL / EXIT / WAIT |
| Gate failures | Stacked bar of `gates_failed` |
| Supervisor | VETO vs FORCE_STOP vs CLEAR |
| Latency | p50/p99 `latency_us` |
| PnL | Cumulative `pnl_delta` (paper then live) |
| Tithe | `tithe_accrued` (if you track ESG narrative) |

---

## Risk appetite alignment

| Your policy | UtahIsMyQuant knob |
|-------------|-------------------|
| Max 2% risk per idea | `risk_limit=0.02` |
| Max 10% book per name | `max_position_size=0.10` |
| 5% stop on positions | `max_drawdown=0.05` |
| Halt on bad data | `max_latency_ms=200` |

**Sign-off document:** One page listing these numbers with effective date. Quants change them weekly = red flag.

---

## Migration sign-off (manager checklist)

- [ ] Parallel log-only week completed  
- [ ] Paper trading week completed  
- [ ] Kill switch drill documented (who calls `reset_circuit_breaker`)  
- [ ] Enterprise RMS still in path (if applicable)  
- [ ] Investor letter updated if strategy narrative changed  
- [ ] Live notional cap written ($X max until review)  

---

## For the "backtest" objection

**Investor / board question:** "Where is the historical Sharpe?"

**Answer you can use:**

> "We operate on real-time geometric stability and explicit gate failures, not historical curve fitting. Paper trading and controlled live phases are our validation. Legacy backtests remain available for slow sleeves but do not drive sub-second decisions."

**Do not say:** "Backtesting is for losers" in investor meetings. Say it in the repo README only.

---

## Organizational placement

```text
CIO / Manager (you)
    └── Head of Quant (owns Manifold + gates)
    └── Head of Risk (owns enterprise RMS + reviews supervisor logs)
    └── CTO (owns WebSocket infra + broker)
    └── Ops (owns kill switch runbook)
```

UtahIsMyQuant sits **between** quant signal and execution—not replacing risk department.

---

## Budget narrative

| Line item | Story |
|-----------|-------|
| Market data | Still required; this stack doesn't replace feed |
| Compute | **Down** vs GPU ML (CPU-first) |
| Vendor risk | **Not removed** for compliance |
| Engineering | **Up** short-term for integration, down long-term vs bespoke MDH |

If savings appear, allocate to **data quality** and **redundancy**, not immediately to leverage.

---

## When to shut it down for the day

Order ops to pull plug if:

1. Circuit breaker tripped + latency not fixed in 15 min  
2. Shadow degradation > threshold for 2 consecutive hours  
3. Manual override dispute between quant and risk  
4. Any log line `FORCE_STOP` cluster on correlated names (liquidity event)  

---

## Supporting the project

If this stack protects your year:

**PayPal: [utah@utahcreates.com](mailto:utah@utahcreates.com)**

The maintainer is broke. Sponsorship keeps documentation honest.

---

## Further reading

- [Migration Overview](../migration/README.md)
- [For Everyone](../for-everyone.md)
- [Quant Daily Workflow](quant-daily-workflow.md)
