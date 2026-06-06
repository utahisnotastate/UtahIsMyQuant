# Siirtymäyleiskatsaus — Hedge-rahaston legacy → UtahIsMyQuant

Tämä indeksi kartoittaa **yleiset institutionaaliset asetelmat** UtahIsMyQuant-arkkitehtuuriin. Jokaisessa oppaassa: mitä jätät taakse, mitä saat, vaiheittainen cutover ja sudenkuopat.

## Valitse skenaariosi

| Jos rahastosi tällä hetkellä… | Lue tämä |
|-------------------------------|----------|
| Pollaa REST-API:ta ajastimella | [Polling → Sentinel](from-polling-to-sentinel.md) |
| Elää Jupyter-backtesteissä | [Backtest-painotteinen → reaaliaika](from-backtest-heavy-to-realtime.md) |
| Ajaa LSTM / läpinäkymätöntä ML-pinoa | [Mustalaatikko-ML → monisto](from-black-box-ml-to-manifold.md) |
| Käyttää yritysriskiä (MSCI, sisäinen RMS) | [Yritysriskipino](from-enterprise-risk-stack.md) |
| On 3–10 hengen prop-kauppa | [Pieni prop-kauppa](from-small-prop-shop.md) |

## Yleiset siirtymäperiaatteet

1. **Rinnakkaisajo ensin** — Lokita UtahIsMyQuant-päätökset legacy-rinnalla; älä vaihda toteutusta ensimmäisenä päivänä.
2. **Paperikauppa toiseksi** — Kytke broker paper API; validoi supervisor-vetot.
3. **Pääoma viimeiseksi** — Pieni live-slice vasta, kun viive ja stop-loss-käyttäytyminen vastaa odotuksia.
4. **Ei backtest-pariteettiteatteria** — Et toista vanhoja Sharpe-käyriä; se on tarkoitus.
5. **Dokumentoi gate-epäonnistumiset** — `AlphaEvent.gates_failed` on audit trailisi.

## Komponenttikartoitus (Rosetta-kivi)

| Legacy-käsite | UtahIsMyQuant-moduuli |
|---------------|----------------------|
| Market data handler (MDH) | `TickObserver` |
| Alpha-malli / signaalipalvelin | `ManifoldEngine` + `AlphaGenerator` |
| Riskimoottori / esikauppatarkistukset | `LogicGateMatrix` + `RiskSupervisor` |
| Mallin seuranta / heikkeneminen | `ShadowTensorAudit` |
| Strategia-isäntä / orkestraattori | `omega_point.py` |
| Kill switch | `RiskSupervisor.circuit_breaker_active` |

## Aikataulumalli (8 viikkoa)

| Viikko | Aktiviteetti |
|--------|--------------|
| 1–2 | Asennus, testit, replay-tickit historiallisesta feed-viennistä |
| 3–4 | WebSocket sentinel kytketty; vain loki-tila |
| 5–6 | Paperitoteutus; säädä `risk_limit`, `max_drawdown` |
| 7 | Johtajan hyväksyntä veto-lokeihin |
| 8 | Rajoitettu live-notional |

## Tuki

Jos siirtyminen säästää pöydällesi oikeaa rahaa: **PayPal [utah@utahcreates.com](mailto:utah@utahcreates.com)** — tekijä on köyhä ja dokumentoi nälkäisenä.
