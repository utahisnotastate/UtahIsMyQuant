# Quant Daily Workflow — Integrating UtahIsMyQuant Into Real Life

This is how you use UtahIsMyQuant **every trading day** without letting it become another abandoned repo on your laptop.

---

## Morning (pre-market, 30–45 min)

### 1. Health check

```powershell
cd UtahIsMyQuant
.venv\Scripts\activate
pytest -q
```

If red: **do not trade**. Fix tests first—they guard math you stopped understanding six months ago.

### 2. Review overnight logs

Search yesterday's logs for:

| Pattern | Action |
|---------|--------|
| `CIRCUIT BREAKER TRIPPED` | Check feed latency / VPS network |
| `gates_failed': ['shadow']` | Alpha mirroring noise—reduce size or pause |
| `FORCE_STOP` | Post-mortem each symbol |
| Mostly `WAIT` | Normal. Suspicious if 100% EXECUTE |

### 3. Set today's parameters (write them down)

```python
engine = ManifoldEngine(sensitivity=0.05)  # do not change mid-session
gen = AlphaGenerator(
    capital=YOUR_NAV,
    risk_limit=0.02,
    min_volume=YOUR_VENUE_MIN,
    supervisor=RiskSupervisor(max_latency_ms=200),
)
```

**Rule:** One parameter change per week maximum in live. Otherwise you are backtesting with real money.

### 4. Start sentinel (log-only first 15 min)

```python
# omega_point.py or your wrapper
omega = OmegaPoint(uri=os.environ["WSS_URI"], capital=NAV)
# First 15 min: patch execute() to log-only
```

Confirm `latency_us` p99 < 200ms.

---

## Market hours (continuous)

### Event loop mental model

```text
tick → manifold features → gates → supervisor → your broker adapter
```

### Your job is NOT to override

If you override more than 2× per week, the system is misconfigured—fix params, don't hero-trade.

### Quick diagnostic snippet

```python
event = gen.process_tick(tick)
if event:
    print(event.signal, event.action, event.gates_failed, event.supervisor_verdict)
```

### Lunch check (5 min)

- Account drawdown vs `max_account_drawdown`  
- Any symbol stuck in exposure while action is WAIT (sync bug?)  
- Tithe accrual (`tithe_allocation()`)—sanity only  

---

## Afternoon (wind-down)

### 1. Flatten policy

Decide desk rule:

- **Auto EXIT** on `DRIFT_DECELERATING` (already biased)  
- Hard flat at T-15 minutes—your broker cron, not UtahIsMyQuant  

### 2. Export `AlphaEvent` log

Append-only JSONL recommended:

```python
import json
with open("logs/session.jsonl", "a") as f:
    f.write(json.dumps(event.__dict__, default=str) + "\n")
```

### 3. Shutdown cleanly

```python
omega.shutdown()  # stops shadow thread + supervisor thread
```

---

## Weekly (research without backtest theater)

| Day | Task |
|-----|------|
| Mon | Review gate failure histogram |
| Wed | Paper-test one param change |
| Fri | Write 3-sentence post-mortem for worst trade |

**Allowed research:**

- Latency distribution plots  
- Mirror rate vs realized slippage  
- Volume gate calibration  

**Forbidden research:**

- "Just one more backtest on 2019" to justify live change today  

---

## Wiring your broker (pattern)

```python
async def guarded_execute(tick: Tick, event: AlphaEvent):
    if event.action not in (Action.BUY, Action.SELL, Action.EXIT):
        return
    if event.circuit_breaker:
        return
    await broker.send(symbol=tick.symbol, side=event.action.value, qty=size_from(event))
```

Keep **idempotent** order IDs. Supervisor may force duplicate EXIT attempts on volatile ticks—dedupe on your side.

---

## Integration with "normal quant life"

| Activity | UtahIsMyQuant role |
|----------|-------------------|
| Morning research read | Informs `min_volume`, not discretionary override |
| Macro calendar | Manual pause: call `supervisor.reset_circuit_breaker()` only after you halt new entries yourself |
| Slack alerts | Hook `EXECUTE_*` and `FORCE_STOP` |
| Jupyter exploration | Offline replay via `ingest`, never mixed with live loop |
| Weekend ML training | Separate pipeline; don't merge weights into manifold |

---

## When you lose money

1. Pull `gates_failed` for that trade  
2. Check if supervisor veto fired and you ignored it  
3. If all gates green and still lost: **normal**  
4. Do not raise `risk_limit` the same day  

---

## When you make money

Send the author something if you can: **PayPal utah@utahcreates.com** — broke maintainer fund.

---

## Cheat sheet

```bash
pytest -q
py omega_point.py
py omega_point.py --uri $env:WSS_URI --live
```

Docs: [API Reference](../api-reference.md) | [Technical Architecture](../technical-architecture.md)
