# Migreerimine: backtesti-kultuur → reaalajas manifold stabiilsus

## Sa oled siin, kui…

- Uurimisjuht mõõdab edu in-sample Sharpe-ga
- Tootmismudel ≠ backtesti mudel (klassika)
- „Re-optimeeri igakuiselt“ on kalendris

## Kultuuriline šokk (taotluslik)

**UtahIsMyQuant ei tarni backtesti raamistikku.**

See pole puuduv funktsionaalsus — see on disaini avaldus:

> Ajaloo sobitamine on ego sobitamine. Kaupleme *olevik* geomeetriaga.

Kvantid vastu seisavad. Juhid küsivad „ühte graafikut 2020-st.“ Valmista vastused:

1. **Shadow tensor** on edasi-modeli tervis, mitte tagasi PnL
2. **Värava ebaõnnestumise logid** on sinu uus uurimisandmestik
3. **Paberkauplemine** on sinu „out of sample“

## Mis asendab backtesti?

| Vana rituaal | Uus rituaal |
|--------------|-------------|
| Walk-forward grid search | Häälesta `sensitivity`, `risk_limit` ainult elaval paberil |
| Sharpe 10 aasta pealt | Jälgi `degradation_score`, kaitseautomaadi trippe |
| Slippage mudel simis | Mõõda `latency_us` + realis slippage paberil |
| Uurimisnotebook → prod | `omega_point.py` on prod skeleton |

## Ülemineku sammud

### Faas A — Varjurežiim (täitmine puudub)

```python
gen = AlphaGenerator(enable_shadow_audit=True)
# Log every AlphaEvent.decision for 2–4 weeks
```

Ehita armatuurlaud: `gates_failed` loendused värava nime järgi.

### Faas B — Paber täitmine

Ühenda maakleri paber API `AlphaEvent.action`-iga ainult kui `supervisor_verdict == "CLEAR"`.

### Faas C — Elav mikro-nominaal

Cap `risk_limit * capital` manifesti väravate järgi.

## Vana mõõdiku kaardistus uuele

| Backtesti mõõdik | Reaalajas proksi |
|------------------|------------------|
| Max drawdown | `RiskSupervisor.account_drawdown()` |
| Hit rate | Positiivsete `pnl_delta` sündmuste suhe |
| Turnover | `EXECUTE_*` loend sessiooni kohta |
| Alfa degradatsioon | `ShadowTensorAudit.degradation_score` |

## Lõksud

- **Pariteedi nõudmine** — Vana strateegia ei kaardistu 1:1 manifold signaalidele
- **Sensitivity üle-häälestamine** ühel volatiilsel nädalal — külmuta parameetrid min 20 sessiooni
- **WAIT ignoreerimine** — Enamik tikke peaks WAIT olema; see on distsipliin

## Juhi jutupunktid

Vaata [Hedge-fondi juhi juhend](../guides/hedge-fund-manager.md#backtesti-vastuväite-jaoks).

## Edasi

- [Must kast ML → manifold](from-black-box-ml-to-manifold.md)
