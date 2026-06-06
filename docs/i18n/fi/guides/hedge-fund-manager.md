# Hedge-rahaston johtajan opas — valvonta ilman Pythonin lukemista

Hallinnoit pääomaa. Sinun ei tarvitse importata scipyä. Tarvitset **kontrollin, kertomuksen ja alarajan**.

---

## Mitä UtahIsMyQuant antaa rahastollesi

| Hyöty | Mekanismi |
|-------|-----------|
| Nopeampi tietoisuus | WebSocket sentinel vs polling |
| Selitettävät päätökset | Jokaisella kaupalla on `reason` + `gates_passed/failed` |
| Päivänsisäiset selviytymisvälineet | Stop-loss, altistuskatto, circuit breaker |
| Audit trail | `AlphaEvent`-lokit (kun tiimi kytkee ne) |
| Ei backtest-fantasiaa | Pakottaa rehellisyyteen live-käyttäytymisestä |

## Mitä se EI anna

- Sääntelycompliance-pakettia
- Sijoittajraportointimallipohjia
- Taattuja tuottoja
- Syytä erottaa riskivastaavasi

---

## Kysymykset quant-tiimillesi (viikoittain)

1. **Kuinka suuri osa tickeistä oli WAIT?**
   - Terve: paljon WAIT, vähän EXECUTE
   - Epäterve: EXECUTE jokaisella tickillä (gateet liian löysät)

2. **Montako circuit breaker -laukaisua tällä viikolla?**
   - Nolla ikuisesti: kynnys ehkä liian löysä
   - Päivittäin: infrastruktuuriongelma

3. **Shadow tensor -terveys?**
   - `degradation_score` nousee → alpha heikkenee / kohinakauppa

4. **Suurin yksittäinen gate-epäonnistumiskategoria?**
   - Kertoo, onko ongelma signaalissa, likviditeetissä vai riskirajassa

5. **Ohitimmeko järjestelmän manuaalisesti?**
   - Yli kaksi kertaa/viikko → järjestelmä- tai kurinalaisuusongelma

---

## Pyydettävät dashboardit (minimi)

Tiimisi voi rakentaa nämä JSONL-lokeista päivässä:

| Paneeli | Metriikka |
|---------|-----------|
| Signaalimix | Määrä `signal`-tyypin mukaan |
| Toimintomix | BUY / SELL / EXIT / WAIT |
| Gate-epäonnistumiset | Pinottu palkki `gates_failed` |
| Supervisor | VETO vs FORCE_STOP vs CLEAR |
| Viive | p50/p99 `latency_us` |
| PnL | Kumulatiivinen `pnl_delta` (paperi sitten live) |
| Tithe | `tithe_accrued` (jos seuraat ESG-kertomusta) |

---

## Riski-inclinaatio linjassa

| Politiikkasi | UtahIsMyQuant-säätö |
|--------------|---------------------|
| Max 2 % riski per idea | `risk_limit=0.02` |
| Max 10 % kirja per nimi | `max_position_size=0.10` |
| 5 % stop positioissa | `max_drawdown=0.05` |
| Pysäytys huonolla datalla | `max_latency_ms=200` |

**Hyväksyntädokumentti:** Yksi sivu näillä luvuilla voimaantulopäivällä. Quantit muuttavat viikoittain = punainen lippu.

---

## Siirtymän hyväksyntä (johtajan tarkistuslista)

- [ ] Rinnakkaisen log-only-viikon suoritus valmis
- [ ] Paperikauppaviikko valmis
- [ ] Kill switch -harjoitus dokumentoitu (kuka kutsuu `reset_circuit_breaker`)
- [ ] Enterprise RMS edelleen polussa (jos sovellettavissa)
- [ ] Sijoittajakirje päivitetty, jos strategiakertomus muuttui
- [ ] Live-notional-katto kirjattu ($X max kunnes uudelleenarvio)

---

## "Backtest"-vastaväite

**Sijoittaja / hallituksen kysymys:** "Missä historiallinen Sharpe?"

**Vastaus, jota voit käyttää:**

> "Toimimme reaaliaikaisen geometrisen vakauden ja eksplisiittisten gate-epäonnistumisten pohjalta, emme historiallisen curve fittingin. Paperikauppa ja kontrolloidut live-vaiheet ovat validointimme. Legacy-backtestit ovat edelleen saatavilla hitaille hihoille, mutta eivät ohjaa subsekuntipäätöksiä."

**Älä sano:** "Backtesting on häviäjille" sijoittajatapaamisissa. Sano se vain repon README:ssa.

---

## Organisaatiopaikka

```text
CIO / Manager (you)
    └── Head of Quant (owns Manifold + gates)
    └── Head of Risk (owns enterprise RMS + reviews supervisor logs)
    └── CTO (owns WebSocket infra + broker)
    └── Ops (owns kill switch runbook)
```

UtahIsMyQuant istuu **quant-signaalin ja toteutuksen välissä** — ei korvaa riskiosastoa.

---

## Budjettikertomus

| Rivierä | Tarina |
|---------|--------|
| Markkinadata | Edelleen vaaditaan; pino ei korvaa feediä |
| Laskenta | **Alas** vs GPU-ML (CPU-first) |
| Toimittajariski | **Ei poistettu** compliancen osalta |
| Insinöörityö | **Ylös** lyhyellä aikavälillä integraatiosta, alas pitkällä vs räätälöity MDH |

Jos säästöjä ilmestyy, kohdista **datan laatuun** ja **redundanssiin**, ei heti vipuun.

---

## Milloin sammuttaa päivän ajaksi

Käskä ops vetää plugi, jos:

1. Circuit breaker lauennut + viivettä ei korjattu 15 minuutissa
2. Shadow degradation > kynnys 2 tuntia peräkkäin
3. Manuaalisen ohituksen kiista quantin ja riskin välillä
4. Mikä tahansa `FORCE_STOP`-klusteri korreloituneilla nimillä (likviditeettitapahtuma)

---

## Projektin tukeminen

Jos pino suojelee vuottasi:

**PayPal: [utah@utahcreates.com](mailto:utah@utahcreates.com)**

Ylläpitäjä on köyhä. Sponsorointi pitää dokumentaation rehellisenä.

---

## Lisälukemista

- [Siirtymäyleiskatsaus](../migration/README.md)
- [Kaikille](../for-everyone.md)
- [Quantin päivittäinen työnkulku](quant-daily-workflow.md)
