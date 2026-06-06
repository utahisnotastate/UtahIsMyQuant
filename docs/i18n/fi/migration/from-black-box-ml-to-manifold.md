# Siirtyminen: Mustalaatikko-ML (LSTM jne.) → monistogeometria

## Olet tässä, jos…

- Feature store + yön yli harjoitusputki
- Malliversio `v847`, jota kukaan ei selitä
- GPU-budjetin rivierä

## Käsitteellinen kartoitus

| ML-pino | Monisto + Utahrbitrage-pino |
|---------|----------------------------|
| Hidden state | Hintaikkuna (oletus 64 tickiä) |
| Attention / layers | Curvature + entropy + drift + adelic-resonanssi |
| Prediction head | `generate_signal()` + `omega_point_routing()` |
| Regularisointi | Logic gateet + shadow tensor + symplectic veto |
| Drift detection | `ShadowTensorAudit` peilausaste |
| Inference GPU | CPU NumPy/SciPy (tarkoituksella lean) |
| Läpinäkymättömät "maksut" | **Topologiset ominaisarvot** 2,3 % + 1,5 % (`utahrbitrage.py`) |

## Mitä poistat (loppujen lopuksi)

- Harjoituscron-työt intraday-alphalle (pidä EOD-analytiikka erikseen tarvittaessa)
- Massiivinen feature DAG subsekuntipäätöksille
- Hyperparametrihaku-klusterit

## Mitä pidät

- Data engineering **puhtaille tickeille** (arvokkaampaa kuin uusi kerros)
- Portfolio-kirjanpito / PnL-järjestelmät
- Compliance-raportointi (ulkoinen)

## Cutover-vaiheet

### 1. Aja monisto rinnalla "Malli B"

Lokita rinnakkain:

- ML-signaali: `buy_prob=0.73`
- Monisto: `signal=BREAKOUT_PRIMED`, `gates_failed=[]`

### 2. Vertaa erimielispäiviä

Kun ML käy kauppaa ja monisto WAIT, jälkikäynti gate-syillä. Kun monisto käy kauppaa ja ML odottaa, tarkista supervisor-tulos.

### 3. Poista ML **viivekriittisiltä** poluilta ensin

Pidä ML hitailla hihoilla (päivittäinen rebalance), jos tuottoisa — hybridikauppa on ok.

### 4. Kouluta henkilöstö tulkittavuuteen

Jokainen `AlphaEvent` selitettävä yhdellä lauseella:

> "Breakout primed, entropy compressed, volume OK, risk OK, shadow healthy → BUY 2% NAV."

## Sudenkuopat

| Sudenkuoppa | Lieventäminen |
|-------------|---------------|
| "Monisto on liian yksinkertainen" | Yksinkertaisuus = viive + auditointi |
| Entropia epävakaa ohuilla ikkunoilla | Nosta `entropy_window` |
| Tiimin nostalgia AUC:lle | Seuraa live slippage-adjusted PnL, ei AUC |

## Koodisilta (ensemble)

```python
async def ensemble_handler(tick: Tick):
    ml_side = your_ml_model.predict(tick)
    event = alpha.process_tick(tick)
    if ml_side == "BUY" and event.action == Action.BUY:
        await execute(tick, event)
```

## Seuraavaksi

- [Tekninen arkkitehtuuri](../technical-architecture.md)
