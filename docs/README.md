# UtahIsMyQuant Documentation

Welcome to the full documentation set. Pick the guide that matches who you are today—not who your LinkedIn says you are.

## Start here

| Audience | Document | What you'll get |
|----------|----------|-----------------|
| **Everyone (donations, overview)** | [Main README](../README.md) | Install, run, support the author |
| **Kids & curious humans** | [For Kids](for-kids.md) | Stories, no jargon |
| **Non-technical users** | [For Everyone](for-everyone.md) | What it does without math trauma |
| **Engineers & quants** | [Technical Architecture](technical-architecture.md) | Modules, data flow, parameters |
| **API users** | [API Reference](api-reference.md) | Classes, methods, return shapes |

## Migration from legacy hedge-fund stacks

Leaving a billion-dollar habit is hard. These playbooks map common old worlds to UtahIsMyQuant:

| Scenario | Guide |
|----------|--------|
| Polling / REST / slow data | [From Polling to Sentinel](migration/from-polling-to-sentinel.md) |
| Backtest-heavy / overfit culture | [From Backtest-Heavy to Real-Time](migration/from-backtest-heavy-to-realtime.md) |
| Black-box ML / LSTM zoo | [From Black-Box ML to Manifold](migration/from-black-box-ml-to-manifold.md) |
| Enterprise risk & compliance stack | [From Enterprise Risk Stack](migration/from-enterprise-risk-stack.md) |
| Small prop shop / lean team | [From Small Prop Shop](migration/from-small-prop-shop.md) |
| **Migration index** | [Migration Overview](migration/README.md) |

## Role-based guides

| Role | Guide |
|------|--------|
| **Quant (daily integration)** | [Quant Daily Workflow](guides/quant-daily-workflow.md) |
| **Hedge fund manager** | [Manager's Guide](guides/hedge-fund-manager.md) |
| **Guides index** | [Guides Overview](guides/README.md) |

## Quick commands

```bash
pip install -r requirements.txt
pytest -q
py omega_point.py                    # demo replay
py omega_point.py --uri wss://... --live
```

## Document map (visual)

```text
                    ┌─────────────────┐
                    │   README.md     │
                    │  (donate + run) │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
   for-kids.md        for-everyone.md    technical-architecture.md
         │                   │                   │
         └───────────────────┴───────────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        migration/*     guides/*      api-reference.md
```

*The manifold does not provide tax, legal, or career advice. It does provide curvature.*
