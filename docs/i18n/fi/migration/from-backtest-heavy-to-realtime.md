# Siirtyminen: Backtest-painotteinen kulttuuri → reaaliaikainen monistovakaus

## Olet tässä, jos…

- Tutkimusjohtaja mittaa menestystä in-sample Sharpe:lla
- Tuotantomalli ≠ backtest-malli (klassinen)
- "Uudelleenoptimoi kuukausittain" on kalenterissa

## Kulttuurisokki (tarkoituksella)

**UtahIsMyQuant ei toimita backtest-kehykset.**

Tämä ei ole puuttuva toiminnallisuus — se on design-lausunto:

> Historian sovittaminen on egon sovittamista. Käymme kauppaa *nykyhetken* geometrialla.

Quantit vastustavat. Johtajat pyytävät "yhden kaavion vuodelta 2020." Valmistaudu vastauksiin:

1. **Shadow tensor** on eteenpäin suuntautuva malliterveys, ei taaksepäin PnL
2. **Gate-epäonnistumislokit** ovat uusi tutkimusdatasi
3. **Paperikauppa** on "out of sample" -si

## Mitä korvaa backtestin?

| Vanha rituaali | Uusi rituaali |
|----------------|---------------|
| Walk-forward grid search | Säädä `sensitivity`, `risk_limit` vain live-paperilla |
| Sharpe 10 vuodella | Seuraa `degradation_score`, circuit breaker -laukaisuja |
| Slippage-malli simulaatiossa | Mittaa `latency_us` + toteutunut slippage paperilla |
| Tutkimusnotebook → prod | `omega_point.py` on prod-luuranko |

## Cutover-vaiheet

### Vaihe A — Shadow-tila (ei toteutusta)

```python
gen = AlphaGenerator(enable_shadow_audit=True)
# Log every AlphaEvent.decision for 2–4 weeks
```

Rakenna dashboard: `gates_failed` -määrät gate-nimen mukaan.

### Vaihe B — Paperitoteutus

Kytke broker paper API `AlphaEvent.action`-signaaliin vain kun `supervisor_verdict == "CLEAR"`.

### Vaihe C — Live micro-notional

Rajoita `risk_limit * capital` manifestin gatejen mukaan.

## Vanhojen metriikoiden kartoitus uusiin

| Backtest-metriikka | Reaaliaikainen proxy |
|--------------------|------------------------|
| Max drawdown | `RiskSupervisor.account_drawdown()` |
| Hit rate | Positiivisten `pnl_delta`-tapahtumien suhde |
| Turnover | `EXECUTE_*` -määrä per sessio |
| Alpha decay | `ShadowTensorAudit.degradation_score` |

## Sudenkuopat

- **Pariteettivaatimus** — Vanha strategia ei mappaudu 1:1 monistosignaaleihin
- **Over-tuning sensitivity** yhdellä volatiililla viikolla — jäädytä parametrit vähintään 20 sessioksi
- **WAIT:n sivuuttaminen** — Useimpien tickien pitäisi olla WAIT; se on kurinalaisuutta

## Johtajan puhepisteet

Katso [Hedge-rahaston johtajan opas](../guides/hedge-fund-manager.md) — osio "Backtest"-vastaväite.

## Seuraavaksi

- [Mustalaatikko-ML → monisto](from-black-box-ml-to-manifold.md)
