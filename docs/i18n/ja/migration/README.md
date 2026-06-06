# 移行概要 — ヘッジファンドレガシーから UtahIsMyQuant へ

**一般的な機関セットアップ** を UtahIsMyQuant アーキテクチャにマッピングするインデックス。各ガイド: 捨てるもの、得るもの、段階的切り替え、落とし穴。

## シナリオを選ぶ

| ファンドが現在… | 読むもの |
|-------------------------|-----------|
| タイマーで REST API をポーリング | [ポーリング → Sentinel](from-polling-to-sentinel.md) |
| Jupyter バックテスト中心 | [バックテスト偏重 → リアルタイム](from-backtest-heavy-to-realtime.md) |
| LSTM / 不透明 ML スタック | [ブラックボックス ML → マニフォールド](from-black-box-ml-to-manifold.md) |
| エンタープライズリスク（MSCI、内部 RMS） | [エンタープライズリスクスタック](from-enterprise-risk-stack.md) |
| 3–10人のプロップショップ | [小規模プロップショップ](from-small-prop-shop.md) |

## 共通移行原則

1. **まず並行実行** — UtahIsMyQuant 決定をレガシーと並べてログ；初日から執行切替しない。
2. **次にペーパートレード** — ブローカーペーパー API を配線；スーパーバイザー拒否を検証。
3. **最後に資本** — 遅延とストップロス挙動が期待通りの後、小さなライブスライス。
4. **バックテスト整合の芝居なし** — 旧 Sharpe 曲線は再現しない；それが要点。
5. **ゲート失敗を文書化** — `AlphaEvent.gates_failed` が監査証跡。

## コンポーネント対応（ロゼッタストーン）

| レガシー概念 | UtahIsMyQuant モジュール |
|----------------|----------------------|
| マーケットデータハンドラ（MDH） | `TickObserver` |
| アルファモデル / シグナルサーバー | `ManifoldEngine` + `AlphaGenerator` |
| リスクエンジン / 取引前チェック | `LogicGateMatrix` + `RiskSupervisor` |
| モデル監視 / 劣化 | `ShadowTensorAudit` |
| 戦略ホスト / オーケストレータ | `omega_point.py` |
| キルスイッチ | `RiskSupervisor.circuit_breaker_active` |

## タイムラインテンプレート（8週）

| 週 | 活動 |
|------|----------|
| 1–2 | インストール、テスト、履歴フィードエクスポートからリプレイティック |
| 3–4 | WebSocket sentinel 配線；ログのみモード |
| 5–6 | ペーパー執行；`risk_limit`, `max_drawdown` 調整 |
| 7 | マネージャーが拒否ログでサインオフ |
| 8 | 限定ライブノーショナル |

## サポート

移行がデスクに実金を救ったら: **PayPal [utah@utahcreates.com](mailto:utah@utahcreates.com)** — 作者は破産寸前で空腹のまま文書を書いている。
