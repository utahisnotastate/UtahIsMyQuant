# Migreerimine: must kast ML (LSTM jne) → manifold geomeetria

## Sa oled siin, kui…

- Feature store + öine treenimise toru
- Mudeli versioon `v847`, mida keegi ei oska seletada
- GPU eelarve rida

## Kontseptuaalne kaardistus

| ML virn | Manifold + Utahrbitrage virn |
|---------|------------------------------|
| Hidden state | Hinnakena (vaikimisi 64 tikki) |
| Attention / kihid | Curvature + entropy + drift + adelic resonance |
| Prediction head | `generate_signal()` + `omega_point_routing()` |
| Regulariseerimine | Logic gates + shadow tensor + symplectic veto |
| Drift tuvastus | `ShadowTensorAudit` mirror rate |
| Inference GPU | CPU NumPy/SciPy (taotluslikult lean) |
| Läbipaistmatud „tasud“ | **Topoloogilised omaväärtused** 2,3% + 1,5% (`utahrbitrage.py`) |

## Mida kustutad (lõpuks)

- Treenimise cron jobid intraday alfa jaoks (hoia EOD analüütika eraldi, kui vaja)
- Massiivne feature DAG sub-sekundi otsustele
- Hüperparameetrite otsingu klastrid

## Mida hoiad

- Andmetehnika **puhtate tikide** jaoks (väärtuslikum kui uus kiht)
- Portfelli arvestus / PnL süsteemid
- Vastavusaruanded (väline)

## Ülemineku sammud

### 1. Käivita manifold paralleelselt „Model B“-na

Logi kõrvuti:

- ML signaal: `buy_prob=0.73`
- Manifold: `signal=BREAKOUT_PRIMED`, `gates_failed=[]`

### 2. Võrdle erimeelsuse päevi

Kui ML kaupleb ja manifold WAIT, tee post-mortem värava põhjustega. Kui manifold kaupleb ja ML ootab, kontrolli supervisor tulemust.

### 3. Pensioneeri ML **latentsuskriitiliste** radade jaoks esmalt

Hoia ML aeglastele varrukatele (päevane rebalance), kui kasumlik — hübrid poed on OK.

### 4. Koolita meeskond interpretability-le

Iga `AlphaEvent` peab olema seletatav ühes lauses:

> „Breakout primed, entropy compressed, volume OK, risk OK, shadow healthy → BUY 2% NAV.“

## Lõksud

| Lõks | Leevendus |
|------|-----------|
| „Manifold on liiga lihtne“ | Lihtsus on latentsus + auditeeritavus |
| Entropy ebastabiilne õhukestel akendel | Suurenda `entropy_window` |
| Meeskonna nostalgia AUC jaoks | Jälgi elavat slippage-korrigeeritud PnL, mitte AUC |

## Koodisild (ensemble)

```python
async def ensemble_handler(tick: Tick):
    ml_side = your_ml_model.predict(tick)
    event = alpha.process_tick(tick)
    if ml_side == "BUY" and event.action == Action.BUY:
        await execute(tick, event)
```

## Edasi

- [Tehniline arhitektuur](../technical-architecture.md)
