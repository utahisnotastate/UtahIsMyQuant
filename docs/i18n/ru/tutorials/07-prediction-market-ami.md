# Учебник 07: AMI рынков предсказаний

## Цель

Использовать **Utah Consensus Lattice** для anti-whale изоляции в стиле Polymarket.

## Demo CLI

```bash
py main.py --prediction-demo
```

Сравните строки лога whale vs retail.

## Рецепт

[../recipes/prediction-lattice.md](../recipes/prediction-lattice.md)

## Сопоставление с Polymarket (концептуально)

1. Построить `capital_flux_tensor` из вектора дельт стакана  
2. Задать `market_impact_factor` из спреда / глубины  
3. `protected_delta` → максимальный сдвиг вероятности перед постингом  
4. Логировать `yield_ledger` для аудита извлечения протокола  

Полное руководство: [../prediction_market_integration.md](../prediction_market_integration.md)

## Далее

[Учебник 08: Live WebSocket-фид](08-live-websocket-feed.md)
