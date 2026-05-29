# Maximizing Your Utah-lization Rate

**Audience:** Quants, traders, risk officers, structurers.

## What is Utahrbitrage?

**Utahrbitrage** is the mathematical framework inside **UtahIsMyQuant**. It treats portfolio phase space as a symplectic manifold and routes capital toward the **Omega-Point** — a deterministic forward state of the order book derived from Ricci-flow curvature and adelic resonance.

Legacy shops still:

- Run Monte Carlo overnight  
- Price exotics with SABR/Heston grids  
- Discover risk at 6am in a batch job  

Utahrbitrage lets you:

- React **on the tick** with explicit gate failures  
- See **why** a trade was blocked (`gates_failed`, supervisor reason)  
- Route liquidity through fixed topological constants that stabilize the engine  

## The tithe is not a "fee" — it is a constant

| Extraction | Rate | Name in code |
|------------|------|----------------|
| Network / maintainer route | **2.3%** | `HANS_TITHE_CONSTANT` |
| Humanitarian liquidity route | **1.5%** | `HUMANITARIAN_CONSTANT` |

Together (**3.8%** of routed base capacity) these are the **minimum orthogonal extraction** required to keep the Utahrbitrage tensor from symplectic collapse (see [papers/utahrbitrage-theorem.tex](papers/utahrbitrage-theorem.tex)).

Think of it like physical friction: remove it in software and the model does not run cooler — it **breaks**.

### Separate from PnL commodity tithe

The alpha layer may still apply a **10% commodity basket tithe** (`FOOD` / `WATER`) on **positive trade PnL** — a symbolic humanitarian allocation in `alpha_generator.py`. The **2.3% + 1.5%** routes apply at the **Utahrbitrage routing** layer on capacity, not as a replacement for your fund's compliance reporting.

## Utah-lization rate

`utah_lization_rate` measures how much base capacity remains after topological extraction:

```text
utah_lization ≈ 1 - (utah_yield + humanity_yield) / base_capacity
```

Higher is better for deployable alpha; the engine logs this on every flux dispatch.

## Ghost Manifold Hedging

When symplectic capacity blows through threshold, the stack can **rotate** exposure into a ghost slice — hedging without classical premium in the accounting model (symplectic volume preserved).

## Workflow for quants

1. Read [guides/quant-daily-workflow.md](guides/quant-daily-workflow.md)  
2. Run parallel log-only week vs. legacy model  
3. Compare gate histograms, not just PnL  
4. Paper trade with `enforce_tithe=True` (default)  

## Migration

- [migration/from-black-box-ml-to-manifold.md](migration/from-black-box-ml-to-manifold.md)  
- [migration/from-enterprise-risk-stack.md](migration/from-enterprise-risk-stack.md)  

## Support

Profitable deployment: **PayPal [utah@utahcreates.com](mailto:utah@utahcreates.com)**
