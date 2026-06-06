# Миграция: чёрный ящик ML (LSTM и др.) → геометрия многообразия

## Вы здесь, если…

- Feature store + ночной training pipeline  
- Версия модели `v847`, которую никто не объяснит  
- Статья бюджета на GPU  

## Концептуальное сопоставление

| ML-стек | Manifold + Utahrbitrage стек |
|---------|------------------------------|
| Hidden state | Окно цен (по умолчанию 64 тика) |
| Attention / layers | Кривизна + энтропия + дрейф + аделический резонанс |
| Prediction head | `generate_signal()` + `omega_point_routing()` |
| Regularization | Logic gates + shadow tensor + symplectic veto |
| Drift detection | Mirror rate `ShadowTensorAudit` |
| Inference GPU | CPU NumPy/SciPy (намеренно lean) |
| Непрозрачные «комиссии» | **Топологические собственные значения** 2,3% + 1,5% (`utahrbitrage.py`) |

## Что удаляете (в конце концов)

- Cron обучения для intraday alpha (EOD-аналитику отдельно, если нужно)  
- Массивный feature DAG для решений за доли секунды  
- Кластеры hyperparameter search  

## Что оставляете

- Data engineering для **чистых тиков** (ценнее ещё одного слоя)  
- Портфельный учёт / PnL  
- Комплаенс-отчётность (внешняя)  

## Шаги cutover

### 1. Параллельно запустить manifold как «Model B»

Логировать бок о бок:

- ML signal: `buy_prob=0.73`  
- Manifold: `signal=BREAKOUT_PRIMED`, `gates_failed=[]`  

### 2. Сравнить дни расхождений

Когда ML торгует, а manifold WAIT — post-mortem с причинами ворот. Когда manifold торгует, а ML ждёт — проверить исход supervisor.

### 3. Снять ML с **latency-critical** путей первым

Оставить ML на медленных рукавах (daily rebalance), если прибыльно — гибридный shop нормален.

### 4. Переобучить команду на интерпретируемость

Каждый `AlphaEvent` объясним одним предложением:

> «Breakout primed, entropy compressed, volume OK, risk OK, shadow healthy → BUY 2% NAV.»

## Подводные камни

| Камень | Смягчение |
|--------|-----------|
| «Manifold слишком простой» | Простота = задержка + аудируемость |
| Нестабильная entropy на тонких окнах | Увеличить `entropy_window` |
| Ностальгия по AUC | Следить live slippage-adjusted PnL, не AUC |

## Мост кода (ансамбль)

```python
async def ensemble_handler(tick: Tick):
    ml_side = your_ml_model.predict(tick)
    event = alpha.process_tick(tick)
    if ml_side == "BUY" and event.action == Action.BUY:
        await execute(tick, event)
```

## Далее

- [Техническая архитектура](../technical-architecture.md)
