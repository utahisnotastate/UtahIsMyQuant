# UtahIsMyQuant Documentation

Welcome to the full documentation set. Pick the guide that matches who you are today—not who your LinkedIn says you are.

## Start here

| Audience | Document | What you'll get |
|----------|----------|-----------------|
| **New users (10 min)** | [Quickstart](quickstart.md) | Install, test, first demo |
| **Tutorials & recipes** | [tutorials/README.md](tutorials/README.md) | Step-by-step + copy-paste code |
| **Paying Utah** | [paying-utah.md](paying-utah.md) | Email Utah; GUI app planned |
| **Everyone (overview)** | [Main README](../README.md) | Install, run, legal notices |
| **Languages (separate pages)** | [languages.md](languages.md) | Русский · Eesti · Suomi · 日本語 |
| **Glossary** | [GLOSSARY.md](GLOSSARY.md) | Terms and acronyms |
| **Kids & curious humans** | [For Kids](for-kids.md) | Stories, no jargon |
| **Non-technical users** | [For Everyone](for-everyone.md) | What it does without math trauma |
| **Engineers & quants** | [Technical Architecture](technical-architecture.md) | Modules, data flow, parameters |
| **API users** | [API Reference](api-reference.md) | Classes, methods, return shapes |
| **Omni / TAD / Symplectic** | [Omni Architecture](omni-architecture.md) | Adelic sieve, veto-matrix, flux |
| **Utahrbitrage framework** | [Utahrbitrage](utahrbitrage.md) | Omega-Point routing, tithe constants, ghost hedge |
| **Prediction markets (Polymarket-style)** | [Prediction Market Integration](prediction_market_integration.md) | Utah Consensus Lattice + AMI |

## Golden Master guides (by role)

| # | Audience | Document |
|---|----------|----------|
| 01 | Engineers & architects | [01-engineers-architects.md](01-engineers-architects.md) |
| 02 | Finance professionals & quants | [02-finance-professionals.md](02-finance-professionals.md) |
| 03 | Founders & family offices | [03-founders-family-offices.md](03-founders-family-offices.md) |
| 04 | Children & beginners | [04-children-beginners.md](04-children-beginners.md) |

**Foundational proof (LaTeX):** [papers/utahrbitrage-theorem.tex](papers/utahrbitrage-theorem.tex)

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
py examples/replay_demo.py           # minimal replay
py omega_point.py                    # full omega replay
py main.py                           # Omni + Utahrbitrage
py main.py --prediction-demo         # prediction AMI
py main.py --dashboard               # Streamlit UI
py omega_point.py --uri wss://... --live
```

## Tutorials (learning path)

| # | Tutorial |
|---|----------|
| 01 | [Install and verify](tutorials/01-install-and-verify.md) |
| 02 | [First replay pipeline](tutorials/02-first-replay-pipeline.md) |
| 03–10 | [Full index](tutorials/README.md) |

## Code recipes

[recipes/README.md](recipes/README.md) — copy-paste snippets for manifold, alpha, Utahrbitrage, prediction lattice.

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

## Paying Utah

If the stack helped you in production, email **[utah@utahcreates.com](mailto:utah@utahcreates.com)**. Details: [paying-utah.md](paying-utah.md). A desktop GUI for managing payments is planned.

## Translations (full trees, separate pages)

| Language | Hub |
|----------|-----|
| Русский | [i18n/ru/README.md](i18n/ru/README.md) |
| Eesti | [i18n/et/README.md](i18n/et/README.md) |
| Suomi | [i18n/fi/README.md](i18n/fi/README.md) |
| 日本語 | [i18n/ja/README.md](i18n/ja/README.md) |

Each locale mirrors this entire doc set. Full index: [languages.md](languages.md).

*The manifold does not provide tax, legal, or career advice. It does provide curvature.*
