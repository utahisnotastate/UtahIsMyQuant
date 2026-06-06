# 移行: 小規模プロップショップ（3–10人）→ UtahIsMyQuant

## 該当する場合…

- クオント1人、開発1人、創業者が両方
- どこかに Excel がまだ残っている
- 「リスク」= トレーダーの頭の中のポジションサイズ

## なぜ最適なフィットか

UtahIsMyQuant は **リーン**: Python、numpy、asyncio、v1 に K8s マニフェスト不要。

| リソース | 要件 |
|----------|-------------|
| ハードウェア |  decent な1台または小さな VM |
| データ | 既に払っている WebSocket フィード1本 |
| チーム時間 | リプレイ約2週、ペーパー約4週 |

## 最小実行デスク

```text
Trader laptop / VPS
  └── py omega_point.py --uri wss://feed --live
  └── logs → ./logs/events.jsonl  (you add 20 lines)
  └── broker paper API (you wire)
```

## 週ごとの計画

| 週 | 成果物 |
|------|-------------|
| 1 | `pytest -q` 緑；CSV からベンダーティックをリプレイ → `ingest` |
| 2 | ライブ sentinel ログのみ；EXECUTE_* で Slack アラート |
| 3 | ペーパー注文；日次 PnL vs 手動スプレッドシート |
| 4 | Go/no-go: `risk_limit` あたり最大 NAV の1–2% |

## 役割（誰が何をするか）

| 人 | タスク |
|--------|------|
| クオント | `sensitivity` 調整、シグナル解釈 |
| 開発 | WebSocket + ブローカーアダプター |
| 創業者 | [マネージャーガイド](../guides/hedge-fund-manager.md) を読み、資本上限を設定 |

## まだ作らないもの

- カスタム Kubernetes オペレータ
- 14戦略スリーブ
- Bloomberg 置き換え

## コスト比較（概算）

| 項目 | レガシープロップ急増 | UtahIsMyQuant |
|------|-------------------|---------------|
| MD プラットフォーム | $2k–30k/月 | フィードのみ |
| GPU 学習 | $500+/月 | デフォルト $0 |
| リスクベンダー | $5k+/月 | リポジトリ内スーパーバイザー |

節約は **データ品質** と利益があれば **作者への支払い**（utah@utahcreates.com）へ。

## 落とし穴

- 古いタイムスタンプでスーパーバイザーをテストせずライブ取引
- 休暇中1人で `shutdown()` 手順書なし

## 次へ

- [クオント日次ワークフロー](../guides/quant-daily-workflow.md)
