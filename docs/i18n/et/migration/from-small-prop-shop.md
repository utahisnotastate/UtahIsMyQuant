# Migreerimine: väike prop shop (3–10 inimest) → UtahIsMyQuant

## Sa oled siin, kui…

- Üks kvant, üks dev, üks asutaja, kes on mõlemad
- Excel on kuskil ikka kaasas
- „Risk“ = positsiooni suurus kaupleja peas

## Miks see parim sobivus

UtahIsMyQuant on **lean**: Python, numpy, asyncio, v1 jaoks pole K8s manifesti vaja.

| Ressurss | Nõue |
|----------|------|
| Riistvara | Üks korralik masin või väike VM |
| Andmed | Üks WebSocket voog, mille eest juba maksad |
| Meeskonna aeg | ~2 nädalat replay, ~4 nädalat paber |

## Minimaalne elujõuline laud

```text
Trader laptop / VPS
  └── py omega_point.py --uri wss://feed --live
  └── logs → ./logs/events.jsonl  (you add 20 lines)
  └── broker paper API (you wire)
```

## Nädal-nädalalt plaan

| Nädal | Tarnitav |
|-------|----------|
| 1 | `pytest -q` roheline; replay vendor tikid CSV-st → `ingest` |
| 2 | Elav sentinel log-only; Slack alert EXECUTE_* |
| 3 | Paber orderid; päevane PnL vs käsitsi spreadsheet |
| 4 | Go/no-go: max 1–2% NAV `risk_limit` järgi |

## Rollid (kes teeb mida)

| Isik | Ülesanne |
|------|----------|
| Kvant | Häälesta `sensitivity`, interpreta signaale |
| Dev | WebSocket + maakleri adapter |
| Asutaja | Loe [Juhi juhend](../guides/hedge-fund-manager.md), sea kapitali capid |

## Mida veel mitte ehitada

- Kohandatud Kubernetes operatorid
- 14 strateegia varrukaid
- Bloomberg asendus

## Kulude võrdlus (jäme)

| Rida | Pärand prop spike | UtahIsMyQuant |
|------|-------------------|---------------|
| MD platvorm | $2k–30k/kuu | Ainult su voog |
| GPU treenimine | $500+/kuu | $0 vaikimisi |
| Risk vendor | $5k+/kuu | Repo supervisor |

Säästud peaksid minema **andmekvaliteeti** ja **autori tasumisse**, kui kasumlik: utah@utahcreates.com.

## Lõksud

- Elav kauplemine enne supervisor testi aegunud timestampidel
- Üks inimene puhkusel ilma `shutdown()` runbookita

## Edasi

- [Kvanti igapäevane töövoog](../guides/quant-daily-workflow.md)
