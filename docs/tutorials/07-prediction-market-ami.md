# Tutorial 07: Prediction Market AMI

## Goal

Use **Utah Consensus Lattice** for Polymarket-style anti-whale insulation.

## Demo CLI

```bash
py main.py --prediction-demo
```

Compare whale vs retail log lines.

## Recipe

[../recipes/prediction-lattice.md](../recipes/prediction-lattice.md)

## Map to Polymarket (conceptual)

1. Build `capital_flux_tensor` from order-book delta vector  
2. Set `market_impact_factor` from spread / depth  
3. `protected_delta` → max probability shift before posting  
4. Log `yield_ledger` for protocol extraction audit  

Full guide: [../prediction_market_integration.md](../prediction_market_integration.md)

## Next

[Tutorial 08: Live WebSocket feed](08-live-websocket-feed.md)
