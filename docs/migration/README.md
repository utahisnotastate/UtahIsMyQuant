# Migration Overview — From Hedge Fund Legacy to UtahIsMyQuant

This index maps **common institutional setups** to the UtahIsMyQuant architecture. Each guide includes: what you leave behind, what you gain, step-by-step cutover, and pitfalls.

## Choose your scenario

| If your fund currently… | Read this |
|-------------------------|-----------|
| Polls REST APIs on a timer | [Polling → Sentinel](from-polling-to-sentinel.md) |
| Lives in Jupyter backtests | [Backtest-Heavy → Real-Time](from-backtest-heavy-to-realtime.md) |
| Runs LSTM / opaque ML stacks | [Black-Box ML → Manifold](from-black-box-ml-to-manifold.md) |
| Uses enterprise risk (MSCI, internal RMS) | [Enterprise Risk Stack](from-enterprise-risk-stack.md) |
| Is a 3–10 person prop shop | [Small Prop Shop](from-small-prop-shop.md) |

## Universal migration principles

1. **Parallel run first** — Log UtahIsMyQuant decisions alongside legacy; do not switch execution day one.  
2. **Paper trade second** — Wire broker paper API; validate supervisor vetoes.  
3. **Capital last** — Small live slice after latency and stop-loss behavior match expectations.  
4. **No backtest parity theater** — You will not reproduce old Sharpe curves; that's the point.  
5. **Document gate failures** — `AlphaEvent.gates_failed` is your audit trail.

## Component mapping (Rosetta stone)

| Legacy concept | UtahIsMyQuant module |
|----------------|----------------------|
| Market data handler (MDH) | `TickObserver` |
| Alpha model / signal server | `ManifoldEngine` + `AlphaGenerator` |
| Risk engine / pre-trade checks | `LogicGateMatrix` + `RiskSupervisor` |
| Model monitoring / decay | `ShadowTensorAudit` |
| Strategy host / orchestrator | `omega_point.py` |
| Kill switch | `RiskSupervisor.circuit_breaker_active` |

## Timeline template (8 weeks)

| Week | Activity |
|------|----------|
| 1–2 | Install, tests, replay ticks from your historical feed export |
| 3–4 | WebSocket sentinel wired; log-only mode |
| 5–6 | Paper execution; tune `risk_limit`, `max_drawdown` |
| 7 | Manager sign-off on veto logs |
| 8 | Limited live notional |

## Support

If migration saves your desk real money: **PayPal [utah@utahcreates.com](mailto:utah@utahcreates.com)** — the author is broke and documents while hungry.
