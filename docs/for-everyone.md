# UtahIsMyQuant — For Everyone (No PhD Required)

## The one-sentence version

**UtahIsMyQuant** is a free, open toolkit that watches live market prices, looks for geometric "stress" in how prices move, decides whether to trade, and uses a strict safety system to limit damage when things go wrong.

It is **not** a get-rich-quick button. It is **not** financial advice. It is software you can study, run, and adapt—with your eyes open.

---

## What problem does it solve?

Big hedge funds spend fortunes on:

- Slow data pipelines (checking prices on a timer instead of instant updates)
- Over-complicated AI that "fits the past" beautifully and fails in the present
- Risk tools that arrive too late

UtahIsMyQuant is the opposite philosophy:

| Old habit | UtahIsMyQuant approach |
|-----------|------------------------|
| Predict the future from history | Observe the **geometry of now** |
| Months of backtesting | **Real-time** stability checks |
| One black-box says BUY | **Multiple gates** must agree |
| Risk as a quarterly report | Risk as a **bodyguard running every tick** |
| Gaussian comfort zone | **Curvature + entropy + multi-scale resonance + symplectic checks** |

---

## The four parts (plain English)

### 1. Tick Observer — "The doorbell"

Gets price updates as they happen (WebSocket push), not on a slow schedule.

**Why you should care:** In fast markets, stale data is expensive.

### 2. Manifold Engine — "The shape reader"

Treats recent prices like a surface and measures:

- **Curvature** — Is the market bending sharply? (regime change risk)
- **Surprise (entropy)** — Has randomness collapsed before a move?
- **Drift** — Is acceleration building?

**Why you should care:** You're not waiting for a single magic indicator—you're reading structure.

### 3. Alpha Generator — "The decision desk"

Turns shape readings into actions: wait, buy, sell, or exit—but only after **logic gates** pass (shape, volume, per-trade risk, shadow audit).

**Why you should care:** Fewer impulsive trades; every decision has a written reason.

### 4. Risk Supervisor — "The bodyguard"

Monitors total exposure, per-trade drawdown, and system latency. Can **veto** trades or **force exits**. Trips a **circuit breaker** if data is too slow (volatile conditions).

**Why you should care:** Survival first. Profits second.

---

## Who is this for?

| You are… | Good fit? |
|----------|-----------|
| A developer learning quant systems | ✅ Excellent learning project |
| A retail trader with coding skills | ⚠️ Possible—wire your own broker, test heavily |
| A hedge fund replacing Bloomberg | ❌ Not a drop-in replacement |
| Someone with zero coding | ⚠️ Read first; partner with a developer |
| A kid | ✅ Read [For Kids](for-kids.md) with a parent |

---

## What it does NOT do

- **No built-in broker** — You connect your own data feed and execution
- **No guaranteed profits** — Markets hurt people who believe guarantees
- **No backtesting suite** — By design (see [migration guide](migration/from-backtest-heavy-to-realtime.md))
- **No tax/legal compliance pack** — Your jurisdiction is your problem

---

## Getting started (safe path)

1. **Install** (Windows example):
   ```powershell
   cd UtahIsMyQuant
   py -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run tests** (sanity check):
   ```powershell
   pytest -q
   ```

3. **Run demo** (fake ticks, no real money):
   ```powershell
   py omega_point.py
   ```

4. **Only then** consider live data (`--uri wss://...`) and paper trading.

---

## Why you might switch from what you use today

You don't have to hate your current tools to see their limits:

- If your strategy only looks good in backtests, not live, you have a **story**, not a system. UtahIsMyQuant shows you exactly **which gate** blocked a trade, so you can debug reality instead of overfitting charts.
- If your data arrives in slow batches, your decisions are already old. Here, the doorbell (TickObserver) gives you **push-based updates**, so the engine reacts to the present, not to a stale snapshot.
- If your risk view is a PDF once a week, you're flying blind intraday. The supervisor and omni layer are designed to say **\"no\" in real time**, not after the loss.

If none of that sounds familiar, keep your stack. If it does, UtahIsMyQuant is a small, readable codebase you can actually reason about—and turn off—when you need to.

---

## Glossary (friendly)

| Term | Meaning |
|------|---------|
| **Tick** | One price update (symbol, price, volume, time) |
| **Manifold** | Fancy word for "treat prices like a shape, not a list" |
| **Gate** | A yes/no safety check before trading |
| **Circuit breaker** | Emergency pause when conditions are unsafe |
| **Tithe** | 10% of positive PnL earmarked for FOOD/WATER buckets (symbolic allocation in code) |
| **Shadow tensor** | Checks if your signal is mirroring noise |

---

## Paying Utah

If this project helps you in the real world, reach out: [paying-utah.md](paying-utah.md).

**Email:** [utah@utahcreates.com](mailto:utah@utahcreates.com). A GUI app to manage support payments is coming later.

---

## Utahrbitrage (the brand inside the box)

**UtahIsMyQuant** is the repo you clone. **Utahrbitrage** is the engine name for Omega-Point routing and the 2.3% / 1.5% topological routes. Details: [utahrbitrage.md](utahrbitrage.md).

---

## Tutorials for hands-on learning

- [Quickstart](quickstart.md) — 10 minutes  
- [Tutorial 02: First replay](tutorials/02-first-replay-pipeline.md)  
- [All tutorials](tutorials/README.md)  

## Next documents

- **Kids:** [for-kids.md](for-kids.md) · [04-children-beginners.md](04-children-beginners.md)
- **Technical:** [technical-architecture.md](technical-architecture.md)
- **Quants:** [guides/quant-daily-workflow.md](guides/quant-daily-workflow.md)
- **Managers:** [guides/hedge-fund-manager.md](guides/hedge-fund-manager.md)
- **Migrating from a fund stack:** [migration/README.md](migration/README.md)
