# Migration: Black-Box ML (LSTM, etc.) → Manifold Geometry

## You are here if…

- Feature store + nightly training pipeline  
- Model version `v847` nobody can explain  
- GPU budget line item  

## Conceptual mapping

| ML stack | Manifold stack |
|----------|----------------|
| Hidden state | Price window (default 64 ticks) |
| Attention / layers | Curvature + entropy + drift |
| Prediction head | `generate_signal()` |
| Regularization | Logic gates + shadow tensor |
| Drift detection | `ShadowTensorAudit` mirror rate |
| Inference GPU | CPU numpy/scipy (intentionally lean) |

## What you delete (eventually)

- Training cron jobs for intraday alpha (keep EOD analytics separately if needed)  
- Massive feature DAG for sub-second decisions  
- Hyperparameter search clusters  

## What you keep

- Data engineering for **clean ticks** (more valuable than another layer)  
- Portfolio accounting / PnL systems  
- Compliance reporting (external)  

## Cutover steps

### 1. Run manifold in parallel as "Model B"

Log side-by-side:

- ML signal: `buy_prob=0.73`  
- Manifold: `signal=BREAKOUT_PRIMED`, `gates_failed=[]`  

### 2. Compare disagreement days

When ML trades and manifold WAITs, post-mortem with gate reasons. When manifold trades and ML waits, check supervisor outcome.

### 3. Retire ML for **latency-critical** paths first

Keep ML for slow sleeves (daily rebalance) if profitable—hybrid shop is fine.

### 4. Retrain staff on interpretability

Every `AlphaEvent` must be explainable in one sentence:

> "Breakout primed, entropy compressed, volume OK, risk OK, shadow healthy → BUY 2% NAV."

## Pitfalls

| Pitfall | Mitigation |
|---------|------------|
| "Manifold is too simple" | Simplicity is latency + auditability |
| Entropy unstable on thin windows | Increase `entropy_window` |
| Team nostalgia for AUC | Track live slippage-adjusted PnL, not AUC |

## Code bridge (ensemble)

```python
async def ensemble_handler(tick: Tick):
    ml_side = your_ml_model.predict(tick)
    event = alpha.process_tick(tick)
    if ml_side == "BUY" and event.action == Action.BUY:
        await execute(tick, event)
```

## Next

- [Technical Architecture](../technical-architecture.md)
