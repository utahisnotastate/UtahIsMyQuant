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

## Support the author

If this project helps you make money in the real world, please consider sending what you can:

**PayPal: [utah@utahcreates.com](mailto:utah@utahcreates.com)**

The author is broke. Coffee helps documentation stay alive.

---

## Next documents

- **Kids:** [for-kids.md](for-kids.md)
- **Technical:** [technical-architecture.md](technical-architecture.md)
- **Quants:** [guides/quant-daily-workflow.md](guides/quant-daily-workflow.md)
- **Managers:** [guides/hedge-fund-manager.md](guides/hedge-fund-manager.md)
- **Migrating from a fund stack:** [migration/README.md](migration/README.md)
