# Hedge-fondi juhi juhend — järelevalve ilma Pythoni lugemiseta

Sa juhid kapitali. Sa ei pea scipy importima. Sul on vaja **kontrolli, narratiivi ja allapoole piire**.

---

## Mida UtahIsMyQuant su fondile annab

| Kasu | Mehhanism |
|------|-----------|
| Kiirem teadlikkus | WebSocket sentinel vs polling |
| Seletatavad otsused | Igal tehingul `reason` + `gates_passed/failed` |
| Intraday ellujäämisvahendid | Stop-loss, exposure cap, kaitseautomaat |
| Auditirada | `AlphaEvent` logid (kui meeskond ühendab) |
| Backtesti fantaasia puudub | Sunnib ausust elava käitumise kohta |

## Mida see EI anna

- Regulatiivse vastavuse paketti
- Investorite aruande mallid
- Garanteeritud tootlust
- Põhjust riskiametniku vallandamiseks

---

## Küsimused kvant meeskonnale (iganädalane)

1. **Mis % tikke oli WAIT?**
   - Tervislik: kõrge WAIT, madal EXECUTE
   - Ebatervislik: EXECUTE igal tikil (väravad liiga laiad)

2. **Mitu kaitseautomaadi trippi sel nädalal?**
   - Null igavesti: läve võib olla liiga lai
   - Iga päev: infrastruktuuri probleem

3. **Shadow tensor tervis?**
   - `degradation_score` trendib üles → alfa decay / müra kauplemine

4. **Suurim üksik värava ebaõnnestumise kategooria?**
   - Informeerib, kas probleem on signaal, likviidsus või riski limiit

5. **Kas üle kirjutasime süsteemi käsitsi?**
   - Rohkem kui kaks korda nädalas → süsteemi või distsipliini ebaõnnestumine

---

## Armaturelauad, mida küsida (minimaalne)

Meeskond saab need JSONL logidest päevaga:

| Paneel | Mõõdik |
|--------|--------|
| Signaali mix | Loend `signal` tüübi järgi |
| Action mix | BUY / SELL / EXIT / WAIT |
| Värava ebaõnnestumised | `gates_failed` virnajoon |
| Supervisor | VETO vs FORCE_STOP vs CLEAR |
| Latentsus | p50/p99 `latency_us` |
| PnL | Kumulatiivne `pnl_delta` (paber siis elav) |
| Tithe | `tithe_accrued` (kui jälgitakse ESG narratiivi) |

---

## Riskiisu joondamine

| Sinu poliitika | UtahIsMyQuant nupp |
|----------------|-------------------|
| Max 2% risk idee kohta | `risk_limit=0.02` |
| Max 10% raamat nime kohta | `max_position_size=0.10` |
| 5% stop positsioonidel | `max_drawdown=0.05` |
| Peatus halbade andmete korral | `max_latency_ms=200` |

**Allkirjastamise dokument:** Üks leht nende numbritega kehtivuskuupäevaga. Kvantid muudavad iganädalaselt = punane lipp.

---

## Migreerimise allkirjastamine (juhi kontrollnimekiri)

- [ ] Paralleelne log-only nädal lõpetatud
- [ ] Paberkauplemise nädal lõpetatud
- [ ] Kill switch drill dokumenteeritud (kes kutsub `reset_circuit_breaker`)
- [ ] Enterprise RMS ikka teel (kui kohaldatav)
- [ ] Investorite kiri uuendatud, kui strateegia narratiiv muutus
- [ ] Elav nominaal cap kirjas ($X max kuni ülevaatus)

---

## Backtesti vastuväite jaoks

**Investori / nõukogu küsimus:** „Kus on ajalooline Sharpe?“

**Vastus, mida saad kasutada:**

> „Operatsioonid põhinevad reaalajas geomeetrilisel stabiilsusel ja selgetel värava ebaõnnestumistel, mitte ajaloolisel curve fittingul. Paberkauplemine ja kontrollitud elavad faasid on meie valideerimine. Pärand backtestid jäävad aeglastele varrukatele, aga ei juhi sub-sekundi otsuseid.“

**Ära ütle:** „Backtesting on kaotajatele“ investorite koosolekul. Ütle seda ainult repo README-s.

---

## Organisatsiooniline paigutus

```text
CIO / Manager (sina)
    └── Head of Quant (owns Manifold + gates)
    └── Head of Risk (owns enterprise RMS + reviews supervisor logs)
    └── CTO (owns WebSocket infra + broker)
    └── Ops (owns kill switch runbook)
```

UtahIsMyQuant istub **vahel** kvant signaali ja täitmise — ei asenda riskiosakonda.

---

## Eelarve narratiiv

| Rida | Lugu |
|------|------|
| Turuandmed | Ikka vajalik; see virn ei asenda voogu |
| Compute | **Alla** vs GPU ML (CPU-first) |
| Vendor risk | **Ei eemaldu** vastavuse jaoks |
| Engineering | **Üles** lühiajaliselt integratsiooniks, **alla** pikaajaliselt vs bespoke MDH |

Kui säästud ilmnevad, suuna **andmekvaliteeti** ja **redundantsi**, mitte kohe finantsvõimendusse.

---

## Millal päevaks välja lülitada

Käsi opsil tõmmata pistik, kui:

1. Kaitseautomaat trip + latentsus pole 15 min parandatud
2. Shadow degradatsioon > läve 2 järjestikust tundi
3. Käsitsi override vaidlus quanti ja riski vahel
4. Logirida `FORCE_STOP` klaster korreleeritud nimedel (likviidsussündmus)

---

## Projekti toetamine

Kui see virn kaitseb su aastat:

**PayPal: [utah@utahcreates.com](mailto:utah@utahcreates.com)**

Maintainer on vaene. Sponsorship hoiab dokumentatsiooni ausana.

---

## Edasi lugemiseks

- [Migreerimise ülevaade](../migration/README.md)
- [Kõigile](../for-everyone.md)
- [Kvanti igapäevane töövoog](quant-daily-workflow.md)
