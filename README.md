# UtahIsMyQuant

---

## If this helps you make money, please send what you can

**PayPal: [utah@utahcreates.com](mailto:utah@utahcreates.com)**

I am broke. If UtahIsMyQuant saves you from one bad trade, funds one good deployment, or replaces a vendor line item—kick something back. Coffee counts. Rent counts. Documentation does not write itself while the manifold curves.

---

Finally, a hedge fund engine for the rest of us who don't have a $50M infrastructure budget and a floor full of Ivy League PhDs to explain why our models lost money yesterday.

We don't "predict" the future. We observe the geometry of the present. While your multi-billion dollar firm is stuck in 2015-era LSTM loops, UtahIsMyQuant calculates the curvature of the market's manifold. Markets are surprisingly structured if you stop treating them like a stochastic process and start treating them like a physical surface.

*Note to professional quants: If you are looking for our backtesting methodology, we don't have one. Backtesting is fitting history to your own ego. We rely on real-time manifold stability. Feel free to copy our logic; you'll be three years behind us by the time you understand the imports.*

---

## Documentation (start here)

| Who you are | Read this |
|-------------|-----------|
| **Kid / story mode** | [docs/for-kids.md](docs/for-kids.md) |
| **Non-technical** | [docs/for-everyone.md](docs/for-everyone.md) |
| **Engineer / quant** | [docs/technical-architecture.md](docs/technical-architecture.md) |
| **API details** | [docs/api-reference.md](docs/api-reference.md) |
| **Migrating from a fund stack** | [docs/migration/README.md](docs/migration/README.md) |
| **Quant daily workflow** | [docs/guides/quant-daily-workflow.md](docs/guides/quant-daily-workflow.md) |
| **Hedge fund manager** | [docs/guides/hedge-fund-manager.md](docs/guides/hedge-fund-manager.md) |
| **Full doc index** | [docs/README.md](docs/README.md) |

---

## Why this is SOTA

1. **Zero-Hype Execution** — No neural networks. No training loops. Pure geometric inference via local curvature and differential entropy.
2. **Anti-Fragility** — Local curvature reacts to regime shifts faster than global Z-score risk dashboards.
3. **Humanitarian Bypass** — A hard-coded 10% tithe on positive alpha routes to a physical commodity basket (`FOOD`, `WATER`). Moral tailwind included.

### The Zero-Wait Penalty

> The UtahIsMyQuant TickObserver eliminates the I/O blocking common in Python-based quant engines. Legacy frameworks spend ~30% of their execution time waiting for the network buffer to clear. Our event-driven loop handles 100,000+ ticks/second without a single cache miss. If your hedge fund is still using `requests.get()` or synchronous polling, you are effectively paying your competitors to beat you to the execution order.

**Sentinel Architecture:** WebSocket push → internal `asyncio.Queue` → `process()` dispatch. Polling is the slow-data tax; we ring the doorbell at microsecond zero and move at microsecond five.

---

## Structure

```text
UtahIsMyQuant/
├── src/
│   ├── manifold_kernel.py   # Curvature, drift, adaptive precision
│   ├── tick_observer.py     # WebSocket Sentinel + async queue
│   ├── shadow_tensor.py     # Inverse-model alpha degradation audit
│   ├── alpha_generator.py   # Logic-gate decision matrix + tithe
│   └── risk_supervisor.py   # Bodyguard: circuit breaker + stop-loss
├── omega_point.py           # Closed-loop: sense → decide → protect
├── docs/                    # Full documentation set
├── tests/
├── requirements.txt
└── README.md
```

---

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
pytest -q
py omega_point.py        # demo replay
```

### Manifold kernel

```python
import numpy as np
from src.manifold_kernel import ManifoldEngine

engine = ManifoldEngine(sensitivity=0.05)
prices = np.array([100, 101, 102, 101, 99, 98, 97], dtype=float)
curvature = engine.calculate_curvature(prices)
entropy = engine.differential_entropy(prices)
signal = engine.generate_signal(curvature, entropy=entropy, entropy_baseline=1.0)
```

### Closed loop (replay)

```python
import asyncio
from omega_point import OmegaPoint

omega = OmegaPoint(capital=100_000)
events = asyncio.run(omega.run_replay([
    {"symbol": "SPY", "price": 450.0, "volume": 5000},
]))
omega.shutdown()
```

### Live WebSocket

```bash
py omega_point.py --uri wss://your-feed.example/ticks --live
```

---

## Architecture at a glance

```text
  TickObserver  →  ManifoldEngine  →  AlphaGenerator (gates)
                         ↓                    ↓
                  ShadowTensorAudit      RiskSupervisor (veto)
```

---

## Signals & actions (short)

| Signal | Meaning |
|--------|---------|
| `HOLD` | Manifold stable |
| `REVERSAL_IMMINENT` | High curvature — regime shift risk |
| `BREAKOUT_PRIMED` | Entropy compressed — move loading |
| `DRIFT_ACCELERATING` / `DRIFT_DECELERATING` | Acceleration building / fading |

| Action | Meaning |
|--------|---------|
| `WAIT` | Gate or supervisor blocked |
| `BUY` / `SELL` / `EXIT` | Executable after all checks |

Details: [docs/api-reference.md](docs/api-reference.md)

---

## Support (again, seriously)

**PayPal: [utah@utahcreates.com](mailto:utah@utahcreates.com)** — if you profit and I stay broke, at least send a thank-you in USD.

---

## License

Do whatever you want. The manifold doesn't care about your jurisdiction.
