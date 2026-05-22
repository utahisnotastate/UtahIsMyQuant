# Migration: Small Prop Shop (3–10 people) → UtahIsMyQuant

## You are here if…

- One quant, one dev, one founder who is both  
- Excel still involved somewhere  
- "Risk" = position size in trader's head  

## Why this is the best fit

UtahIsMyQuant is **lean**: Python, numpy, asyncio, no K8s manifest required for v1.

| Resource | Requirement |
|----------|-------------|
| Hardware | One decent box or small VM |
| Data | One WebSocket feed you already pay for |
| Team time | ~2 weeks to replay, ~4 weeks to paper |

## Minimal viable desk

```text
Trader laptop / VPS
  └── py omega_point.py --uri wss://feed --live
  └── logs → ./logs/events.jsonl  (you add 20 lines)
  └── broker paper API (you wire)
```

## Week-by-week plan

| Week | Deliverable |
|------|-------------|
| 1 | `pytest -q` green; replay vendor ticks from CSV → `ingest` |
| 2 | Live sentinel log-only; Slack alert on EXECUTE_* |
| 3 | Paper orders; daily PnL vs manual spreadsheet |
| 4 | Go/no-go: max 1–2% NAV per `risk_limit` |

## Roles (who does what)

| Person | Task |
|--------|------|
| Quant | Tune `sensitivity`, interpret signals |
| Dev | WebSocket + broker adapter |
| Founder | Read [Manager Guide](../guides/hedge-fund-manager.md), set capital caps |

## What not to build yet

- Custom Kubernetes operators  
- 14 strategy sleeves  
- Bloomberg replacement  

## Cost comparison (rough)

| Item | Legacy prop spike | UtahIsMyQuant |
|------|-------------------|---------------|
| MD platform | $2k–30k/mo | Your feed only |
| GPU training | $500+/mo | $0 default |
| Risk vendor | $5k+/mo | In-repo supervisor |

Savings should go to **data quality** and **paying the author** if profitable: utah@utahcreates.com.

## Pitfalls

- Trading live before supervisor tested on stale timestamps  
- One person on vacation with no `shutdown()` runbook  

## Next

- [Quant Daily Workflow](../guides/quant-daily-workflow.md)
