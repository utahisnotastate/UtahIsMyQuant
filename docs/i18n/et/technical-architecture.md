# Tehniline arhitektuur

## Süsteemi ülevaade

UtahIsMyQuant rakendab **suletud tsükli sündmuspõhist virna**:

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

Sisenemispunktid:

- `omega_point.py` (`OmegaPoint`) — klassikaline suletud tsükkel
- `main.py` (`OmniDiscoveryEngine`) — Omni/TAD/symplectic + utah-flux

---

## Moodulite viide

### `manifold_kernel.py` — ManifoldEngine (+ adelic)

**Vastutus:** Tunnuste eraldamine hinnakenadest.

| Meetod | Sisend | Väljund | Märkused |
|--------|--------|---------|----------|
| `calculate_curvature` | `price_vector` | `float` | Keskmine abs 2. erinevus |
| `manifold_drift` | `price_vector` | `float` | Keskmine 3. erinevus (kiirendus) |
| `differential_entropy` | `price_vector` | `float` | KDE log-tootlustel |
| `adaptive_quantize` | `price_vector` | `ndarray` | `float64` rahulik / `float32` volatiilne |
| `adelic_resonance` | prices, volumes | `float` | Rist-prime resonantsi tugevus |
| `detect_adelic_void` | prices, volumes | `bool` | Likviidsuse vaakumi tuvastus |
| `generate_signal` | curvature, entropy, drift, adelic state | `str` | Signaali enum (sh `ADELIC_*`) |

**Vaikimisi tundlikkus:** `0.05` (kõveruse lävi `REVERSAL_IMMINENT` jaoks).

**Signaali prioriteet** (esimene vaste võidab):

1. `REVERSAL_IMMINENT` — curvature > sensitivity
2. `DRIFT_ACCELERATING` / `DRIFT_DECELERATING` — |drift| > `drift_sensitivity` (1e-3)
3. `BREAKOUT_PRIMED` — entropy < 85% baseline
4. `HOLD`

---

### `tick_observer.py` — TickObserver

**Vastutus:** Asünkroonne ingest ja fan-out.

| Režiim | API | Kasutus |
|--------|-----|---------|
| Sentinel | `listen()` + `process()` / `start_sentinel()` | Elav WebSocket |
| Replay | `ingest(payload)` + `process()` | Simulatsioon |
| Bridge | `listen_queue(external_queue)` | Pärand integratsioon |

**Tiku skeem:**

```python
Tick(symbol: str, price: float, volume: float = 0, timestamp_ns: int)
```

**Payload aliased:** `symbol`/`s`, `price`/`p`, `volume`/`v`.

**Latentsus:** `TickObserver.latency_us(tick)` → mikrosekundid tiku ajatempli järgi.

---

### `shadow_tensor.py` — ShadowTensorAudit

**Vastutus:** Alfa degradatsiooni tuvastus inverse-manifold peegeldamise kaudu.

- Peegeldab hinnakena: `reflected = 2 * anchor - prices`
- Võrdleb edasi-signaali vs inverse-signaali
- `degradation_score` = peegeldusmäär libisevas aknas
- `alpha_healthy()` kui skoor < `mirror_threshold` (vaikimisi 0.55)

Taustalõim: `start_background(interval=0.5)`.

---

### `alpha_generator.py` — AlphaGenerator

**Vastutus:** Loogikaväravate otsusmaatriks + PnL/tithe arvestus, valikuliste Omni hookidega (TAD, symplectic, utah-flux).

**LogicGateMatrix väravad:**

| Värav | Võti | Läbimise tingimus |
|-------|------|-------------------|
| Curvature | `curvature` | Kaubeldav signaal + magnituudi reeglid |
| Volume | `volume` | `volume >= min_volume` |
| Risk | `risk` | `exposure/capital < risk_limit` (vaikimisi 2%) |
| Shadow | `shadow` | `shadow_healthy == True` |

**Post-gate supervisor veto** (kui `supervisor` ühendatud): võib lisada `supervisor` `gates_failed`-i.

**Execute verbid:** `WAIT`, `EXECUTE_BUY`, `EXECUTE_SELL`, `EXECUTE_EXIT`.

**Tithe:** `TITHE_RATE = 0.10` positiivse PnL pealt → `FOOD` / `WATER` ämbrid `tithe_allocation()` kaudu.

---

### `risk_supervisor.py` — RiskSupervisor

**Vastutus:** Portfelli-taseme ihukaitsja (Fourth Law piir).

| Kontroll | Vaikimisi | Mõju |
|----------|-----------|------|
| `max_drawdown` | 5% | Positsiooni `SELL_IMMEDIATE` |
| `max_position_size` | 10% | Kogu ekspositsiooni cap |
| `max_latency_ms` | 200 | Kaitseautomaat |
| `max_account_drawdown` | 5% | Konto-taseme peatus |

**Fourth Law:** `fourth_law_boundary(bug, fix)` → peatus, kui kumbki tõene.

**Integratsioon:** `evaluate_tick()` → `veto_decision()` mutates alpha decision dict.

---

## Andmevoog (üks tik)

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

## Konfiguratsiooni maatriks

| Parameeter | Asukoht | Tüüpiline vahemik |
|------------|---------|-------------------|
| `sensitivity` | ManifoldEngine | 0.01–0.10 |
| `entropy_window` | ManifoldEngine | 16–64 |
| `risk_limit` | AlphaGenerator / LogicGateMatrix | 0.01–0.05 |
| `capital` | AlphaGenerator | konto NAV |
| `min_volume` | LogicGateMatrix | venue-sõltuv |
| `max_drawdown` | RiskSupervisor | 0.02–0.08 |
| `max_position_size` | RiskSupervisor | 0.05–0.25 |
| `max_latency_ms` | RiskSupervisor | 50–500 |

---

## Sõltuvused

```text
numpy, scipy    — manifold + adelic math
websockets      — live sentinel
asyncio         — stdlib event loop
streamlit       — Omni-Sieve dashboard (optional)
pytest          — test harness
```

---

## Testimine

```bash
pytest -q                           # 62 tests
pytest tests/test_manifold.py -v    # kernel only
pytest tests/test_alpha_gates.py -v # gates only
pytest tests/test_risk_supervisor.py -v
pytest tests/test_omega_point.py -v # integration
```

---

## Laienduspunktid

1. **Maakleri adapter** — Telli `TickObserver`, saada orderid `AlphaEvent.action` pealt
2. **Kohandatud voog** — Rakenda `ingest()` oma JSON skeemiga (laienda `from_payload`)
3. **Extra värav** — Alaklassi `LogicGateMatrix.evaluate()` või wrap `generate_action`
4. **Distress overlay** — Lisa supervisor sisend välisest Akashic/distress signaalidest (`data/`)

---

## Turvalisus ja operatsioonid

- Ära commiti API võtmeid ega `.env` credentiaale
- Käivita elav ainult paberkauplemisega, kuni veto/stop käitumine on valideeritud
- Kaitseautomaat on latentsuse-põhine proksi, mitte börsi staatuse voog
- HA/klastrit pole — ühe-protsessi asyncio mudel

---

## Seotud dokumendid

- [API viide](api-reference.md)
- [Kvanti igapäevane töövoog](guides/quant-daily-workflow.md)
- [Migreerimisjuhendid](migration/README.md)
