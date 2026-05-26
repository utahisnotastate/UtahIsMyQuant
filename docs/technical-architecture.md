# Technical Architecture

## System overview

UtahIsMyQuant implements a **closed-loop event-driven stack**:

```text
┌──────────────┐     ┌─────────────────┐     ┌──────────────────┐
│ TickObserver │────▶│  AlphaGenerator │────▶│  RiskSupervisor  │
│  (ingest)    │     │ (logic gates)   │◀────│  (veto / exit)   │
└──────┬───────┘     └────────┬────────┘     └──────────────────┘
       │                      │
       │              ┌───────▼────────┐
       │              │ ManifoldEngine │
       │              │ ShadowTensor   │
       │              └────────────────┘
       │
       ▼
  WebSocket / Replay queue
```

Entry points:

- `omega_point.py` (`OmegaPoint`) — classic closed loop  
- `main.py` (`OmniDiscoveryEngine`) — Omni/TAD/symplectic + utah-flux

---

## Module reference

### `manifold_kernel.py` — ManifoldEngine (+ adelic)

**Responsibility:** Feature extraction from price windows.

| Method | Input | Output | Notes |
|--------|-------|--------|-------|
| `calculate_curvature` | `price_vector` | `float` | Mean abs 2nd difference |
| `manifold_drift` | `price_vector` | `float` | Mean 3rd difference (acceleration) |
| `differential_entropy` | `price_vector` | `float` | KDE on log-returns |
| `adaptive_quantize` | `price_vector` | `ndarray` | `float64` calm / `float32` volatile |
| `adelic_resonance` | prices, volumes | `float` | Cross-prime resonance strength |
| `detect_adelic_void` | prices, volumes | `bool` | Liquidity vacuum detection |
| `generate_signal` | curvature, entropy, drift, adelic state | `str` | Signal enum (incl. `ADELIC_*`) |

**Default sensitivity:** `0.05` (curvature threshold for `REVERSAL_IMMINENT`).

**Signal priority** (first match wins):

1. `REVERSAL_IMMINENT` — curvature > sensitivity  
2. `DRIFT_ACCELERATING` / `DRIFT_DECELERATING` — |drift| > `drift_sensitivity` (1e-3)  
3. `BREAKOUT_PRIMED` — entropy < 85% of baseline  
4. `HOLD`

---

### `tick_observer.py` — TickObserver

**Responsibility:** Async ingestion and fan-out.

| Mode | API | Use case |
|------|-----|----------|
| Sentinel | `listen()` + `process()` / `start_sentinel()` | Live WebSocket |
| Replay | `ingest(payload)` + `process()` | Simulation |
| Bridge | `listen_queue(external_queue)` | Legacy integration |

**Tick schema:**

```python
Tick(symbol: str, price: float, volume: float = 0, timestamp_ns: int)
```

**Payload aliases:** `symbol`/`s`, `price`/`p`, `volume`/`v`.

**Latency:** `TickObserver.latency_us(tick)` → microseconds since tick timestamp.

---

### `shadow_tensor.py` — ShadowTensorAudit

**Responsibility:** Detect alpha degradation via inverse-manifold mirroring.

- Reflects price window: `reflected = 2 * anchor - prices`
- Compares forward signal vs inverse signal
- `degradation_score` = mirror rate over rolling window
- `alpha_healthy()` if score < `mirror_threshold` (default 0.55)

Background thread: `start_background(interval=0.5)`.

---

### `alpha_generator.py` — AlphaGenerator

**Responsibility:** Logic-gate decision matrix + PnL/tithe accounting, with optional Omni hooks (TAD, symplectic, utah-flux).

**LogicGateMatrix gates:**

| Gate | Key | Pass condition |
|------|-----|----------------|
| Curvature | `curvature` | Tradeable signal + magnitude rules |
| Volume | `volume` | `volume >= min_volume` |
| Risk | `risk` | `exposure/capital < risk_limit` (default 2%) |
| Shadow | `shadow` | `shadow_healthy == True` |

**Post-gate supervisor veto** (if `supervisor` attached): may add `supervisor` to `gates_failed`.

**Execute verbs:** `WAIT`, `EXECUTE_BUY`, `EXECUTE_SELL`, `EXECUTE_EXIT`.

**Tithe:** `TITHE_RATE = 0.10` on positive PnL → `FOOD` / `WATER` buckets via `tithe_allocation()`.

---

### `risk_supervisor.py` — RiskSupervisor

**Responsibility:** Portfolio-level bodyguard (Fourth Law boundary).

| Control | Default | Effect |
|---------|---------|--------|
| `max_drawdown` | 5% | Per-position `SELL_IMMEDIATE` |
| `max_position_size` | 10% | Total exposure cap |
| `max_latency_ms` | 200 | Circuit breaker |
| `max_account_drawdown` | 5% | Account-level halt |

**Fourth Law:** `fourth_law_boundary(bug, fix)` → halt if either true.

**Integration:** `evaluate_tick()` → `veto_decision()` mutates alpha decision dict.

---

## Data flow (single tick)

```text
1. WebSocket recv → JSON → queue.put
2. process() → Tick.from_payload → emit()
3. AlphaGenerator.process_tick:
   a. Append price/volume, trim window (default 64)
   b. ManifoldEngine features
   c. ShadowTensorAudit.record_tick (optional)
   d. generate_action (logic gates)
   e. RiskSupervisor.evaluate_tick + veto_decision
   f. decision_to_action → PnL + tithe
4. AlphaEvent returned to subscriber / OmegaPoint log
```

---

## Configuration matrix

| Parameter | Location | Typical range |
|-----------|----------|---------------|
| `sensitivity` | ManifoldEngine | 0.01–0.10 |
| `entropy_window` | ManifoldEngine | 16–64 |
| `risk_limit` | AlphaGenerator / LogicGateMatrix | 0.01–0.05 |
| `capital` | AlphaGenerator | account NAV |
| `min_volume` | LogicGateMatrix | venue-dependent |
| `max_drawdown` | RiskSupervisor | 0.02–0.08 |
| `max_position_size` | RiskSupervisor | 0.05–0.25 |
| `max_latency_ms` | RiskSupervisor | 50–500 |

---

## Dependencies

```text
numpy, scipy    — manifold + adelic math
websockets      — live sentinel
asyncio         — stdlib event loop
streamlit       — Omni-Sieve dashboard (optional)
pytest          — test harness
```

---

## Testing

```bash
pytest -q                           # 51 tests
pytest tests/test_manifold.py -v    # kernel only
pytest tests/test_alpha_gates.py -v # gates only
pytest tests/test_risk_supervisor.py -v
pytest tests/test_omega_point.py -v # integration
```

---

## Extension points

1. **Broker adapter** — Subscribe to `TickObserver`, send orders on `AlphaEvent.action`
2. **Custom feed** — Implement `ingest()` with your JSON schema (extend `from_payload`)
3. **Extra gate** — Subclass `LogicGateMatrix.evaluate()` or wrap `generate_action`
4. **Distress overlay** — Add supervisor input from external Akashic/distress signals (`data/`)

---

## Security & operations notes

- Do not commit API keys or `.env` with credentials  
- Run live only with paper trading until veto/stop behavior is validated  
- Circuit breaker is latency-based proxy, not a exchange-status feed  
- No HA/clustering — single-process asyncio model  

---

## Related docs

- [API Reference](api-reference.md)
- [Quant Daily Workflow](guides/quant-daily-workflow.md)
- [Migration guides](migration/README.md)
