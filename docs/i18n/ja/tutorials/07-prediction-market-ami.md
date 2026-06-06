# チュートリアル 07: 予測市場 AMI

## 目標

Polymarket 風の反クジラ断熱に **Utah Consensus Lattice** を使う。

## デモ CLI

```bash
py main.py --prediction-demo
```

クジラ vs 個人のログ行を比較。

## レシピ

[../recipes/prediction-lattice.md](../recipes/prediction-lattice.md)

## Polymarket へのマッピング（概念）

1. オーダーブックデルタから `capital_flux_tensor` を構築
2. スプレッド/深度から `market_impact_factor` を設定
3. `protected_delta` → 投稿前の最大確率シフト
4. プロトコル抽出監査用に `yield_ledger` をログ

フルガイド: [../prediction_market_integration.md](../prediction_market_integration.md)

## 次へ

[チュートリアル 08: ライブ WebSocket フィード](08-live-websocket-feed.md)
