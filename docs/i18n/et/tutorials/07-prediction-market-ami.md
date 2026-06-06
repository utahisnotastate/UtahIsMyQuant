# Õpetus 07: Ennustusturu AMI

## Eesmärk

Kasuta **Utah Consensus Lattice** Polymarket-stiilis vaalakaitse jaoks.

## Demo CLI

```bash
py main.py --prediction-demo
```

Võrdle vaala vs jaemüüja logiridu.

## Retsept

[../recipes/prediction-lattice.md](../recipes/prediction-lattice.md)

## Kaardista Polymarketile (kontseptuaalselt)

1. Ehita `capital_flux_tensor` order-book delta vektorist
2. Sea `market_impact_factor` spread / depth järgi
3. `protected_delta` → max tõenäosuse nihe enne postitamist
4. Logi `yield_ledger` protokolli eraldamise auditiks

Täielik juhend: [../prediction_market_integration.md](../prediction_market_integration.md)

## Edasi

[Õpetus 08: Elav WebSocket voog](08-live-websocket-feed.md)
