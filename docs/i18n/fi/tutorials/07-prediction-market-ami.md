# Opetusohjelma 07: Ennustemarkkinoiden AMI

## Tavoite

Käytä **Utah Consensus Lattice** -kerrosta Polymarket-tyyliseen valasvastukseen.

## Demo CLI

```bash
py main.py --prediction-demo
```

Vertaa valas- vs vähittäislogirivejä.

## Resepti

[../recipes/prediction-lattice.md](../recipes/prediction-lattice.md)

## Kartoitus Polymarketiin (käsitteellinen)

1. Rakenna `capital_flux_tensor` order-book -deltavektorista
2. Aseta `market_impact_factor` spreadistä / syvyydestä
3. `protected_delta` → max todennäköisyysmuutos ennen postausta
4. Lokita `yield_ledger` protokollaotteen auditointiin

Täysi opas: [../prediction_market_integration.md](../prediction_market_integration.md)

## Seuraavaksi

[Opetusohjelma 08: Live WebSocket-feed](08-live-websocket-feed.md)
