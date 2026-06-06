# Siirtyminen: Pieni prop-kauppa (3–10 hlö) → UtahIsMyQuant

## Olet tässä, jos…

- Yksi quant, yksi dev, yksi perustaja molempina
- Excel mukana jossain
- "Riski" = position koko kauppiaan päässä

## Miksi tämä on paras sopivuus

UtahIsMyQuant on **lean**: Python, numpy, asyncio, ei K8s-manifestia v1:een.

| Resurssi | Vaatimus |
|----------|----------|
| Laitteisto | Yksi kunnollinen kone tai pieni VM |
| Data | Yksi WebSocket-feed, josta jo maksat |
| Tiimin aika | ~2 viikkoa replay, ~4 viikkoa paperi |

## Minimaalinen työpöytä

```text
Trader laptop / VPS
  └── py omega_point.py --uri wss://feed --live
  └── logs → ./logs/events.jsonl  (you add 20 lines)
  └── broker paper API (you wire)
```

## Viikko viikolta -suunnitelma

| Viikko | Toimitettava |
|--------|--------------|
| 1 | `pytest -q` vihreinä; replay vendor-tickit CSV:stä → `ingest` |
| 2 | Live sentinel vain loki; Slack-hälytys EXECUTE_* |
| 3 | Paperiorderit; päivittäinen PnL vs manuaalinen taulukko |
| 4 | Go/no-go: max 1–2 % NAV per `risk_limit` |

## Roolit (kuka tekee mitä)

| Henkilö | Tehtävä |
|---------|---------|
| Quant | Säädä `sensitivity`, tulkitse signaalit |
| Dev | WebSocket + broker adapter |
| Perustaja | Lue [Johtajan opas](../guides/hedge-fund-manager.md), aseta pääomakatot |

## Mitä älä rakenna vielä

- Custom Kubernetes -operaattorit
- 14 strategiahihnaa
- Bloomberg-korvike

## Kustannusvertailu (karkea)

| Kohde | Legacy prop spike | UtahIsMyQuant |
|-------|-------------------|---------------|
| MD-alusta | $2k–30k/kk | Vain feedisi |
| GPU-harjoitus | $500+/kk | $0 oletus |
| Riskivendor | $5k+/kk | Repossa supervisor |

Säästöt → **datan laatuun** ja **tekijän maksamiseen**, jos tuottoisa: utah@utahcreates.com.

## Sudenkuopat

- Live-kauppa ennen supervisorin testausta vanhentuneilla aikaleimoilla
- Yksi henkilö lomalla ilman `shutdown()`-runbookia

## Seuraavaksi

- [Quantin päivittäinen työnkulku](../guides/quant-daily-workflow.md)
