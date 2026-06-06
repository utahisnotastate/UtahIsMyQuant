# UtahIsMyQuant — dokumentatsioon

Tere tulemast täielikku dokumentatsioonikogusse. Vali juhend, mis sobib sinuga **täna** — mitte see, mida LinkedIn ütleb.

## Alusta siit

| Sihtgrupp | Dokument | Mida saad |
|-----------|----------|-----------|
| **Uued kasutajad (10 min)** | [Kiire algus](quickstart.md) | Paigaldus, testid, esimene demo |
| **Õpetused ja retseptid** | [tutorials/README.md](tutorials/README.md) | Samm-sammult + kopeeritav kood |
| **Utah tasumine** | [paying-utah.md](paying-utah.md) | Kirjuta Utahile; GUI rakendus tulekul |
| **Ülevaade (kõigile)** | [Projekti ülevaade](project-overview.md) | Paigaldus, käivitamine, märkused |
| **Keeled (eraldi lehed)** | [languages.md](languages.md) | English · Русский · Suomi · 日本語 |
| **Sõnastik** | [GLOSSARY.md](GLOSSARY.md) | Terminid ja lühendid |
| **Lapsed ja uudishimulikud** | [Lastele](for-kids.md) | Lood, ilma žargoonita |
| **Mitte-tehniline** | [Kõigile](for-everyone.md) | Mida see teeb, ilma matemaatilise traumata |
| **Insenerid ja kvantid** | [Tehniline arhitektuur](technical-architecture.md) | Moodulid, andmevoog, parameetrid |
| **API kasutajad** | [API viide](api-reference.md) | Klassid, meetodid, tagastuskujud |
| **Omni / TAD / Symplectic** | [Omni arhitektuur](omni-architecture.md) | Adelic sieve, veto-matrix, flux |
| **Utahrbitrage raamistik** | [Utahrbitrage](utahrbitrage.md) | Omega-Point marsruutimine, tithe konstandid, ghost hedge |
| **Ennustusturud (Polymarket-stiil)** | [Ennustusturu integratsioon](prediction_market_integration.md) | Utah Consensus Lattice + AMI |

## Golden Master juhendid (rolli järgi)

| # | Sihtgrupp | Dokument |
|---|-----------|----------|
| 01 | Insenerid ja arhitektid | [01-engineers-architects.md](01-engineers-architects.md) |
| 02 | Finantsprofessionaalid ja kvantid | [02-finance-professionals.md](02-finance-professionals.md) |
| 03 | Asutajad ja perekontorid | [03-founders-family-offices.md](03-founders-family-offices.md) |
| 04 | Lapsed ja algajad | [04-children-beginners.md](04-children-beginners.md) |

**Alus tõestus (LaTeX):** [../../papers/utahrbitrage-theorem.tex](../../papers/utahrbitrage-theorem.tex)

## Migreerimine pärand-hedge-fondi virnast

Miljardidollariline harjumus on raske maha jätta. Need juhendid kaardistavad tavalised vanad maailmad UtahIsMyQuantile:

| Stsenaarium | Juhend |
|-------------|--------|
| Polling / REST / aeglane andmevoog | [Pollingust Sentinelini](migration/from-polling-to-sentinel.md) |
| Backtesti-kultuur / ülesobitamine | [Backtestist reaalajasse](migration/from-backtest-heavy-to-realtime.md) |
| Must kast ML / LSTM zoo | [Mustast kastist mitmekordse hulgani](migration/from-black-box-ml-to-manifold.md) |
| Ettevõtte riski- ja vastavusvirn | [Ettevõtte riskivirnast](migration/from-enterprise-risk-stack.md) |
| Väike prop shop / väike meeskond | [Väikesest prop shopist](migration/from-small-prop-shop.md) |
| **Migreerimise indeks** | [Migreerimise ülevaade](migration/README.md) |

## Rollipõhised juhendid

| Roll | Juhend |
|------|--------|
| **Kvant (igapäevane integratsioon)** | [Kvanti igapäevane töövoog](guides/quant-daily-workflow.md) |
| **Hedge-fondi juht** | [Juhi juhend](guides/hedge-fund-manager.md) |
| **Juhendite indeks** | [Juhendite ülevaade](guides/README.md) |

## Kiired käsud

```bash
pip install -r requirements.txt
pytest -q
py examples/replay_demo.py           # minimaalne replay
py omega_point.py                    # täielik omega replay
py main.py                           # Omni + Utahrbitrage
py main.py --prediction-demo         # prediction AMI
py main.py --dashboard               # Streamlit UI
py omega_point.py --uri wss://... --live
```

## Õpetused (õpitee)

| # | Õpetus |
|---|--------|
| 01 | [Paigaldus ja kontroll](tutorials/01-install-and-verify.md) |
| 02 | [Esimene replay toru](tutorials/02-first-replay-pipeline.md) |
| 03–10 | [Täisindeks](tutorials/README.md) |

## Koodiretseptid

[recipes/README.md](recipes/README.md) — kopeeritavad lõigud mitmekordse, alfa, Utahrbitrage ja ennustusvõrgustiku jaoks.

## Dokumendi kaart (visuaalne)

```text
                    ┌─────────────────┐
                    │   README.md     │
                    │  (toetus + käiv)│
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
   for-kids.md        for-everyone.md    technical-architecture.md
         │                   │                   │
         └───────────────────┴───────────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        migration/*     guides/*      api-reference.md
```

## Utah tasumine

Kui virn aitas sind tootmises, kirjuta **[utah@utahcreates.com](mailto:utah@utahcreates.com)**. Üksikasjad: [paying-utah.md](paying-utah.md). Lauaarvuti GUI maksete haldamiseks on plaanis.

## Tõlked

| Keel | Keskus |
|------|--------|
| English | [../../README.md](../../README.md) |
| Русский | [../ru/README.md](../ru/README.md) |
| Suomi | [../fi/README.md](../fi/README.md) |
| 日本語 | [../ja/README.md](../ja/README.md) |

Täisindeks: [languages.md](languages.md).

*Mitmekord ei anna maksu-, õigus- ega karjäärinõu. Kõverust ta siiski annab.*
