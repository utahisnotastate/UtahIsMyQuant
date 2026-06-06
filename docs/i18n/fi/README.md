# UtahIsMyQuant — dokumentaatio

Tervetuloa koko dokumentaatioon. Valitse opas, joka vastaa sitä, kuka olet tänään — ei sitä, mitä LinkedIn sanoo.

## Aloita tästä

| Kohderyhmä | Dokumentti | Mitä saat |
|------------|------------|-----------|
| **Uudet käyttäjät (10 min)** | [Pika-aloitus](quickstart.md) | Asennus, testit, ensimmäinen demo |
| **Opetusohjelmat ja reseptit** | [tutorials/README.md](tutorials/README.md) | Vaiheittain + kopioi-liitä-koodi |
| **Utahin tukeminen** | [paying-utah.md](paying-utah.md) | Sähköposti Utahille; GUI suunnitteilla |
| **Yleiskatsaus (asennus, ajo)** | [project-overview.md](project-overview.md) | Asennus, ajaminen, huomautukset |
| **Kielet (erilliset sivut)** | [languages.md](languages.md) | Русский · Eesti · 日本語 · Suomi |
| **Sanasto** | [GLOSSARY.md](GLOSSARY.md) | Termit ja lyhenteet |
| **Lapset ja uteliaat** | [Lapsille](for-kids.md) | Tarinoita, ei jargonia |
| **Ei-tekniset käyttäjät** | [Kaikille](for-everyone.md) | Mitä se tekee ilman matemaattista trauma |
| **Insinöörit ja quantit** | [Tekninen arkkitehtuuri](technical-architecture.md) | Moduulit, datavirta, parametrit |
| **API-käyttäjät** | [API-viite](api-reference.md) | Luokat, metodit, paluuarvot |
| **Omni / TAD / Symplectic** | [Omni-arkkitehtuuri](omni-architecture.md) | Adelic-sieve, veto-matrix, flux |
| **Utahrbitrage-kehykset** | [Utahrbitrage](utahrbitrage.md) | Omega-Point-reititys, tithe-vakiot, ghost hedge |
| **Ennustemarkkinat (Polymarket-tyyli)** | [Ennustemarkkinaintegraatio](prediction_market_integration.md) | Utah Consensus Lattice + AMI |

## Golden Master -oppaat (roolin mukaan)

| # | Kohderyhmä | Dokumentti |
|---|------------|------------|
| 01 | Insinöörit ja arkkitehdit | [01-engineers-architects.md](01-engineers-architects.md) |
| 02 | Rahoitusalan ammattilaiset ja quantit | [02-finance-professionals.md](02-finance-professionals.md) |
| 03 | Perustajat ja perhetoimistot | [03-founders-family-offices.md](03-founders-family-offices.md) |
| 04 | Lapset ja aloittelijat | [04-children-beginners.md](04-children-beginners.md) |

**Perustodistus (LaTeX):** [../../papers/utahrbitrage-theorem.tex](../../papers/utahrbitrage-theorem.tex)

## Siirtyminen vanhoista hedge-rahastopinoista

Miljardien dollarien tottumuksesta luopuminen on vaikeaa. Nämä pelikirjat kartoittavat yleiset vanhat maailmat UtahIsMyQuant-arkkitehtuuriin:

| Skenaario | Opas |
|-----------|------|
| Polling / REST / hidas data | [Pollingista Sentineliin](migration/from-polling-to-sentinel.md) |
| Backtest-painotteinen / overfit-kulttuuri | [Backtestistä reaaliaikaan](migration/from-backtest-heavy-to-realtime.md) |
| Mustalaatikko-ML / LSTM-zoo | [Mustalaatikko-ML:stä monistoon](migration/from-black-box-ml-to-manifold.md) |
| Yritystason riski- ja compliance-pino | [Yritysriskipinosta](migration/from-enterprise-risk-stack.md) |
| Pieni prop-kauppa / lean-tiimi | [Pienestä prop-kaupasta](migration/from-small-prop-shop.md) |
| **Siirtymäindeksi** | [Siirtymäyleiskatsaus](migration/README.md) |

## Roolipohjaiset oppaat

| Rooli | Opas |
|-------|------|
| **Quant (päivittäinen integraatio)** | [Quantin päivittäinen työnkulku](guides/quant-daily-workflow.md) |
| **Hedge-rahaston johtaja** | [Johtajan opas](guides/hedge-fund-manager.md) |
| **Oppaiden indeksi** | [Oppaiden yleiskatsaus](guides/README.md) |

## Pikakomennot

```bash
pip install -r requirements.txt
pytest -q
py examples/replay_demo.py           # minimaalinen replay
py omega_point.py                    # täysi omega-replay
py main.py                           # Omni + Utahrbitrage
py main.py --prediction-demo         # prediction AMI
py main.py --dashboard               # Streamlit UI
py omega_point.py --uri wss://... --live
```

## Opetusohjelmat (oppimispolku)

| # | Opetusohjelma |
|---|---------------|
| 01 | [Asennus ja varmistus](tutorials/01-install-and-verify.md) |
| 02 | [Ensimmäinen replay-putki](tutorials/02-first-replay-pipeline.md) |
| 03–10 | [Koko indeksi](tutorials/README.md) |

## Koodireseptit

[recipes/README.md](recipes/README.md) — kopioi-liitä-pätkät monistolle, alphalle, Utahrbitragelle, prediction lattice -kerrokselle.

## Dokumenttikartta (visuaalinen)

```text
                    ┌─────────────────┐
                    │ project-overview│
                    │  (tuki + ajo)   │
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

## Utahin tukeminen

Jos pino auttoi tuotannossa, lähetä sähköpostia **[utah@utahcreates.com](mailto:utah@utahcreates.com)**. Lisätiedot: [paying-utah.md](paying-utah.md). Työpöytä-GUI maksujen hallintaan on suunnitteilla.

## Käännökset

| Kieli | Keskus |
|-------|--------|
| English | [../../README.md](../../README.md) |
| Русский | [../ru/README.md](../ru/README.md) |
| Eesti | [../et/README.md](../et/README.md) |
| 日本語 | [../ja/README.md](../ja/README.md) |
| 简体中文 | [../zh/README.md](../zh/README.md) |
| **Suomi** | [README.md](README.md) |

Koko indeksi: [languages.md](languages.md).

*Monisto ei anna vero-, oikeus- eikä uraneuvontaa. Se antaa kaarevuutta.*
