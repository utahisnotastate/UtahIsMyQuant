# Tekninen arkkitehtuuri

## Järjestelmäyleiskatsaus

UtahIsMyQuant toteuttaa **suljetun silmukan tapahtumapohjaisen pinon**:

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

Käynnistyspisteet:

- `omega_point.py` (`OmegaPoint`) — klassinen suljettu silmukka
- `main.py` (`OmniDiscoveryEngine`) — Omni/TAD/symplectic + utah-flux

---

## Moduuliviite

### `manifold_kernel.py` — ManifoldEngine (+ adelic)

**Vastuu:** Ominaisuuksien poiminta hintaikkunoista.

| Metodi | Syöte | Tulos | Huomiot |
|--------|-------|-------|---------|
| `calculate_curvature` | `price_vector` | `float` | Keskiarvo abs 2. erotus |
| `manifold_drift` | `price_vector` | `float` | Keskiarvo 3. erotus (kiihtyvyys) |
| `differential_entropy` | `price_vector` | `float` | KDE log-tuotoille |
| `adaptive_quantize` | `price_vector` | `ndarray` | `float64` rauhallinen / `float32` epävakaa |
| `adelic_resonance` | prices, volumes | `float` | Ristiin-prime-resonanssin voima |
| `detect_adelic_void` | prices, volumes | `bool` | Likviditeettityhjiön havaitseminen |
| `generate_signal` | curvature, entropy, drift, adelic state | `str` | Signaali-enum (ml. `ADELIC_*`) |

**Oletusherkkyys:** `0.05` (kaarevuuskynnys `REVERSAL_IMMINENT`-signaalille).

**Signaaliprioriteetti** (ensimmäinen osuma voittaa):

1. `REVERSAL_IMMINENT` — curvature > sensitivity
2. `DRIFT_ACCELERATING` / `DRIFT_DECELERATING` — |drift| > `drift_sensitivity` (1e-3)
3. `BREAKOUT_PRIMED` — entropy < 85 % baselinesta
4. `HOLD`

---

### `tick_observer.py` — TickObserver

**Vastuu:** Asynkroninen ingest ja fan-out.

| Tila | API | Käyttötapaus |
|------|-----|--------------|
| Sentinel | `listen()` + `process()` / `start_sentinel()` | Live WebSocket |
| Replay | `ingest(payload)` + `process()` | Simulaatio |
| Bridge | `listen_queue(external_queue)` | Legacy-integraatio |

**Tick-skeema:**

```python
Tick(symbol: str, price: float, volume: float = 0, timestamp_ns: int)
```

**Payload-aliakset:** `symbol`/`s`, `price`/`p`, `volume`/`v`.

**Viive:** `TickObserver.latency_us(tick)` → mikrosekunnit tickin aikaleimasta.

---

### `shadow_tensor.py` — ShadowTensorAudit

**Vastuu:** Alphan heikkenemisen havaitseminen käänteisen moniston peilausella.

- Peilaa hintaikkunan: `reflected = 2 * anchor - prices`
- Vertaa eteenpäin-signaalia vs käänteissignaalia
- `degradation_score` = peilausaste liukuvalla ikkunalla
- `alpha_healthy()` jos score < `mirror_threshold` (oletus 0.55)

Taustasäie: `start_background(interval=0.5)`.

---

### `alpha_generator.py` — AlphaGenerator

**Vastuu:** Logic-gate-päätösmatriisi + PnL/tithe-kirjanpito, valinnaisilla Omni-koukuilla (TAD, symplectic, utah-flux).

**LogicGateMatrix-gateet:**

| Gate | Avain | Läpäisyehdokset |
|------|-------|-----------------|
| Curvature | `curvature` | Kaupattava signaali + magnitudisäännöt |
| Volume | `volume` | `volume >= min_volume` |
| Risk | `risk` | `exposure/capital < risk_limit` (oletus 2 %) |
| Shadow | `shadow` | `shadow_healthy == True` |

**Supervisor-veto gatejen jälkeen** (jos `supervisor` liitetty): voi lisätä `supervisor` → `gates_failed`.

**Toteutusverbit:** `WAIT`, `EXECUTE_BUY`, `EXECUTE_SELL`, `EXECUTE_EXIT`.

**Tithe:** `TITHE_RATE = 0.10` positiivisesta PnL:stä → `FOOD` / `WATER` -purkit `tithe_allocation()`-kautta.

---

### `risk_supervisor.py` — RiskSupervisor

**Vastuu:** Portfolio-tason bodyguard (Fourth Law -raja).

| Kontrolli | Oletus | Vaikutus |
|-----------|--------|----------|
| `max_drawdown` | 5 % | Positiokohtainen `SELL_IMMEDIATE` |
| `max_position_size` | 10 % | Kokonaisaltistuskatto |
| `max_latency_ms` | 200 | Circuit breaker |
| `max_account_drawdown` | 5 % | Tilitason pysäytys |

**Fourth Law:** `fourth_law_boundary(bug, fix)` → pysäytys jos jompikumpi tosi.

**Integraatio:** `evaluate_tick()` → `veto_decision()` muuttaa alpha-päätös-dictiä.

---

## Datavirta (yksi tick)

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
4. AlphaEvent palautetaan subscriberille / OmegaPoint-lokiin
```

---

## Konfiguraatiomatriisi

| Parametri | Sijainti | Tyypillinen alue |
|-----------|----------|------------------|
| `sensitivity` | ManifoldEngine | 0.01–0.10 |
| `entropy_window` | ManifoldEngine | 16–64 |
| `risk_limit` | AlphaGenerator / LogicGateMatrix | 0.01–0.05 |
| `capital` | AlphaGenerator | tilin NAV |
| `min_volume` | LogicGateMatrix | paikkakohtainen |
| `max_drawdown` | RiskSupervisor | 0.02–0.08 |
| `max_position_size` | RiskSupervisor | 0.05–0.25 |
| `max_latency_ms` | RiskSupervisor | 50–500 |

---

## Riippuvuudet

```text
numpy, scipy    — manifold + adelic math
websockets      — live sentinel
asyncio         — stdlib event loop
streamlit       — Omni-Sieve dashboard (optional)
pytest          — test harness
```

---

## Testaus

```bash
pytest -q                           # 62 tests
pytest tests/test_manifold.py -v    # kernel only
pytest tests/test_alpha_gates.py -v # gates only
pytest tests/test_risk_supervisor.py -v
pytest tests/test_omega_point.py -v # integration
```

---

## Laajennuspisteet

1. **Broker adapter** — Tilaa `TickObserver`, lähetä toimeksiannot `AlphaEvent.action`-signaalilla
2. **Custom feed** — Toteuta `ingest()` omalla JSON-skeemallasi (laajenna `from_payload`)
3. **Extra gate** — Peri `LogicGateMatrix.evaluate()` tai kääri `generate_action`
4. **Distress overlay** — Lisää supervisor-syöte ulkoisista Akashic/distress-signaaleista (`data/`)

---

## Turvallisuus ja operointi

- Älä commitoi API-avaimia tai `.env`-tiedostoja tunnistetiedoilla
- Aja live vain paperikaupalla, kunnes veto/stop-käyttäytyminen on validoitu
- Circuit breaker on viivepohjainen proxy, ei pörssitilan feed
- Ei HA/klusterointia — yksiprosessinen asyncio-malli

---

## Liittyvät dokumentit

- [API-viite](api-reference.md)
- [Quantin päivittäinen työnkulku](guides/quant-daily-workflow.md)
- [Siirtymäoppaat](migration/README.md)
