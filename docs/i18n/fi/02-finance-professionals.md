# Utah-lization raten maksimointi

**Kohderyhmä:** Quantit, kauppiaat, riskivastaavat, strukturoijat.

## Mikä on Utahrbitrage?

**Utahrbitrage** on **UtahIsMyQuant**-projektin sisällä oleva matemaattinen kehykset. Se kohtelee portfolio-vaiheavaruutta symplektisena monistona ja reitittää pääoman kohti **Omega-Point** -tilaa — determinististä order bookin eteenpäin suuntautuvaa tilaa Ricci-flow-kaarevuudesta ja adelic-resonanssista johdettuna.

Vanhat kaupat ajavat vielä:

- Monte Carloa yön yli
- Eksotisten hinnoittelua SABR/Heston-ruudukolla
- Riskin löytämistä klo 6 eräajossa

Utahrbitrage antaa:

- Reagoida **tickillä** eksplisiittisillä gate-epäonnistumisilla
- Nähdä **miksi** kauppa estettiin (`gates_failed`, supervisor-syy)
- Reitittää likviditeetin kiinteiden topologisten vakioiden kautta, jotka stabiloivat moottoria

## Tithe ei ole "maksu" — se on vakio

| Ote | Prosentti | Nimi koodissa |
|-----|-----------|---------------|
| Verkko / ylläpitäjäreitti | **2,3 %** | `HANS_TITHE_CONSTANT` |
| Humanitaarinen likviditeettireitti | **1,5 %** | `HUMANITARIAN_CONSTANT` |

Yhdessä (**3,8 %** reititetystä peruskapasiteetista) nämä ovat **minimiorthogonaalinen ote**, joka estää Utahrbitrage-tensorin symplektisen collapsen (katso [../../papers/utahrbitrage-theorem.tex](../../papers/utahrbitrage-theorem.tex)).

Ajattele sitä kuin fyysistä kitkaa: poista se ohjelmistosta, eikä malli jäähdä — se **hajoaa**.

### Erillinen PnL-hyödyketithe:stä

Alpha-kerros voi silti soveltaa **10 % hyödykekori-titheä** (`FOOD` / `WATER`) **positiiviselle kauppa-PnL:lle** — symbolinen humanitaarinen allokaatio `alpha_generator.py`-tiedostossa. **2,3 % + 1,5 %** -reitit koskevat **Utahrbitrage-reititys**-kerrosta kapasiteetilla, eivät korvaa rahastosi compliance-raportointia.

## Utah-lization rate

`utah_lization_rate` mittaa, kuinka paljon peruskapasiteetista jää topologisen otteen jälkeen:

```text
utah_lization ≈ 1 - (utah_yield + humanity_yield) / base_capacity
```

Korkeampi on parempi deployattavalle alphalle; moottori lokittaa tämän jokaisessa flux-dispatchissa.

## Ghost Manifold Hedging

Kun symplektinen kapasiteetti ylittää kynnyksen, pino voi **rotaatioida** altistuksen ghost-viipaleeseen — suojaus ilman klassista preemiaa kirjanpitomallissa (symplektinen tilavuus säilyy).

## Työnkulku quanteille

1. Lue [guides/quant-daily-workflow.md](guides/quant-daily-workflow.md)
2. Aja rinnakkaisen log-only-viikon legacy-mallia vastaan
3. Vertaa gate-histogrammeja, ei vain PnL:ää
4. Paperikauppa `enforce_tithe=True` (oletus)

## Siirtyminen

- [migration/from-black-box-ml-to-manifold.md](migration/from-black-box-ml-to-manifold.md)
- [migration/from-enterprise-risk-stack.md](migration/from-enterprise-risk-stack.md)

## Tuki

Tuottoisa käyttöönotto: **PayPal [utah@utahcreates.com](mailto:utah@utahcreates.com)**
