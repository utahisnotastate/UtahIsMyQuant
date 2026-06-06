# Migreerimise ülevaade — hedge-fondi pärandist UtahIsMyQuantile

See indeks kaardistab **tavalised institutsionaalsed seadistused** UtahIsMyQuant arhitektuurile. Iga juhend sisaldab: mida jätad maha, mida saad, samm-sammult üleminekut ja lõksud.

## Vali oma stsenaarium

| Kui su fond praegu… | Loe seda |
|---------------------|----------|
| Küsib REST API-sid taimeriga | [Polling → Sentinel](from-polling-to-sentinel.md) |
| Elab Jupyter backtestides | [Backtesti-kultuur → reaalajas](from-backtest-heavy-to-realtime.md) |
| Käivitab LSTM / läbipaistmatuid ML virnasid | [Must kast ML → manifold](from-black-box-ml-to-manifold.md) |
| Kasutab ettevõtte riski (MSCI, sisemine RMS) | [Ettevõtte riskivirn](from-enterprise-risk-stack.md) |
| On 3–10 inimese prop shop | [Väike prop shop](from-small-prop-shop.md) |

## Universaalsed migreerimise põhimõtted

1. **Paralleelkäivitus esmalt** — Logi UtahIsMyQuant otsuseid pärand kõrval; ära vaheta täitmist esimesel päeval.
2. **Paberkauplemine teisena** — Ühenda maakleri paber API; valideeri supervisor veto-d.
3. **Kapital viimasena** — Väike elav lõik pärast latentsuse ja stop-loss käitumise vastavust ootustele.
4. **Backtesti pariteedi teater puudub** — Sa ei taasta vanu Sharpe kõveraid; see ongi mõte.
5. **Dokumenteeri värava ebaõnnestumised** — `AlphaEvent.gates_failed` on sinu auditirada.

## Komponentide kaardistus (Rosetta kivi)

| Pärand mõiste | UtahIsMyQuant moodul |
|---------------|----------------------|
| Turuandmete handler (MDH) | `TickObserver` |
| Alfa mudel / signaaliserver | `ManifoldEngine` + `AlphaGenerator` |
| Riskimootor / eelkaubelduse kontrollid | `LogicGateMatrix` + `RiskSupervisor` |
| Mudeli jälgimine / degradatsioon | `ShadowTensorAudit` |
| Strateegia host / orkestreerija | `omega_point.py` |
| Kill switch | `RiskSupervisor.circuit_breaker_active` |

## Ajakava mall (8 nädalat)

| Nädal | Tegevus |
|-------|---------|
| 1–2 | Paigaldus, testid, replay tikid ajaloo voog ekspordist |
| 3–4 | WebSocket sentinel ühendatud; log-only režiim |
| 5–6 | Paber täitmine; häälesta `risk_limit`, `max_drawdown` |
| 7 | Juhi allkiri veto logidele |
| 8 | Piiratud elav nominaal |

## Toetus

Kui migreerimine säästab laual päris raha: **PayPal [utah@utahcreates.com](mailto:utah@utahcreates.com)** — autor on vaene ja dokumenteerib näljase peaga.
