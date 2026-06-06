# Utah-lization rate maksimeerimine

**Sihtgrupp:** Kvantid, kauplejad, riskiametnikud, struktureerijad.

## Mis on Utahrbitrage?

**Utahrbitrage** on matemaatiline raamistik **UtahIsMyQuant** sees. See käsitleb portfelli faasiruumi symplectic mitmekordse hulgani ja marsruudib kapitali **Omega-Point** poole — deterministlik edasi-olek order bookist, mis tuleneb Ricci-flow kõverusest ja adelic resonantsist.

Pärand poed teevad ikka:

- Monte Carlo öösel
- Eksootikute hinnastamine SABR/Heston ruudustikega
- Riski avastamine kell 6 hommikul partiitööna

Utahrbitrage võimaldab:

- Reageerida **tikil** selgete värava ebaõnnestumistega
- Näha **miks** tehing blokeeriti (`gates_failed`, supervisor reason)
- Marsruutida likviidsust fikseeritud topoloogiliste konstantide kaudu, mis stabiliseerivad mootorit

## Tithe ei ole „tasu“ — see on konstant

| Eraldamine | Määr | Nimi koodis |
|------------|------|-------------|
| Võrgu / maintainer marsruut | **2,3%** | `HANS_TITHE_CONSTANT` |
| Humanitaarne likviidsusmarsruut | **1,5%** | `HUMANITARIAN_CONSTANT` |

Koos (**3,8%** marsruuditud baasvõimsusest) on need **minimaalne ortogonaalne eraldamine**, mis hoiab Utahrbitrage tensorit symplectic kokkvarisemisest (vaata [../../papers/utahrbitrage-theorem.tex](../../papers/utahrbitrage-theorem.tex)).

Mõtle füüsilise hõõrdumisena: eemalda see tarkvaras ja mudel ei jahuta — see **puruneb**.

### Eraldi PnL kauba tithest

Alfa kiht võib endiselt rakendada **10% kaubakorvi tithet** (`FOOD` / `WATER`) **positiivse tehingu PnL** pealt — sümboolne humanitaarne jaotus `alpha_generator.py`-s. **2,3% + 1,5%** marsruudid kehtivad **Utahrbitrage marsruutimise** kihil võimsuse pealt, mitte fondi vastavusaruande asendajana.

## Utah-lization rate

`utah_lization_rate` mõõdab, kui palju baasvõimsust jääb pärast topoloogilist eraldamist:

```text
utah_lization ≈ 1 - (utah_yield + humanity_yield) / base_capacity
```

Kõrgem on parem deployable alfa jaoks; mootor logib seda igal flux dispatchil.

## Ghost Manifold Hedging

Kui symplectic võimsus ületab läve, võib virn **pöörata** ekspositsiooni ghost lõiku — hedge ilma klassikalise preemiumita arvestusmudelis (symplectic ruumala säilib).

## Töövoog kvantidele

1. Loe [guides/quant-daily-workflow.md](guides/quant-daily-workflow.md)
2. Käivita paralleelne log-only nädal vs pärand mudel
3. Võrdle värava histogramme, mitte ainult PnL
4. Paberkauplemine `enforce_tithe=True` (vaikimisi)

## Migreerimine

- [migration/from-black-box-ml-to-manifold.md](migration/from-black-box-ml-to-manifold.md)
- [migration/from-enterprise-risk-stack.md](migration/from-enterprise-risk-stack.md)

## Toetus

Kasumlik deploy: **PayPal [utah@utahcreates.com](mailto:utah@utahcreates.com)**
