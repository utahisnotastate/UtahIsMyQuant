# UtahIsMyQuant — ドキュメント（日本語）

ようこそ。完全なドキュメントセットです。今日のあなたに合ったガイドを選んでください — LinkedIn の肩書きではなく。

## はじめに

| 対象 | ドキュメント | 得られるもの |
|------|----------------|--------------|
| **初めての方（10分）** | [クイックスタート](quickstart.md) | インストール、テスト、最初のデモ |
| **チュートリアルとレシピ** | [tutorials/README.md](tutorials/README.md) | ステップバイステップ + コピペ用コード |
| **Utah への支払い** | [paying-utah.md](paying-utah.md) | Utah へメール；GUI アプリは計画中 |
| **全体概要** | [project-overview.md](project-overview.md) | インストール、実行、法的注意事項 |
| **言語（別ページ）** | [languages.md](languages.md) | Русский · Eesti · English |
| **用語集** | [GLOSSARY.md](GLOSSARY.md) | 用語と略語 |
| **子どもと好奇心旺盛な方** | [子ども向け](for-kids.md) | 物語形式、専門用語なし |
| **非技術者向け** | [みんなのための説明](for-everyone.md) | 数学トラウマなしで何ができるか |
| **エンジニアとクオント** | [技術アーキテクチャ](technical-architecture.md) | モジュール、データフロー、パラメータ |
| **API 利用者** | [API リファレンス](api-reference.md) | クラス、メソッド、戻り値の形 |
| **Omni / TAD / Symplectic** | [Omni アーキテクチャ](omni-architecture.md) | Adelic sieve、veto-matrix、flux |
| **Utahrbitrage フレームワーク** | [Utahrbitrage](utahrbitrage.md) | Omega-Point ルーティング、タイス定数、ゴーストヘッジ |
| **予測市場（Polymarket 風）** | [予測市場統合](prediction_market_integration.md) | Utah Consensus Lattice + AMI |

## Golden Master ガイド（役割別）

| # | 対象 | ドキュメント |
|---|------|----------------|
| 01 | エンジニアとアーキテクト | [01-engineers-architects.md](01-engineers-architects.md) |
| 02 | 金融プロフェッショナルとクオント | [02-finance-professionals.md](02-finance-professionals.md) |
| 03 | 創業者とファミリーオフィス | [03-founders-family-offices.md](03-founders-family-offices.md) |
| 04 | 子どもと初心者 | [04-children-beginners.md](04-children-beginners.md) |

**基礎証明（LaTeX）:** [../../papers/utahrbitrage-theorem.tex](../../papers/utahrbitrage-theorem.tex)

## レガシーヘッジファンドスタックからの移行

古い習慣を捨てるのは大変です。よくある旧環境を UtahIsMyQuant にマッピングするプレイブック:

| シナリオ | ガイド |
|----------|--------|
| ポーリング / REST / 遅いデータ | [ポーリングから Sentinel へ](migration/from-polling-to-sentinel.md) |
| バックテスト偏重 / 過剰適合文化 | [バックテスト偏重からリアルタイムへ](migration/from-backtest-heavy-to-realtime.md) |
| ブラックボックス ML / LSTM 群 | [ブラックボックス ML からマニフォールドへ](migration/from-black-box-ml-to-manifold.md) |
| エンタープライズリスクとコンプライアンス | [エンタープライズリスクスタックから](migration/from-enterprise-risk-stack.md) |
| 小規模プロップショップ / リーンなチーム | [小規模プロップショップから](migration/from-small-prop-shop.md) |
| **移行インデックス** | [移行概要](migration/README.md) |

## 役割別ガイド

| 役割 | ガイド |
|------|--------|
| **クオント（日次統合）** | [クオント日次ワークフロー](guides/quant-daily-workflow.md) |
| **ヘッジファンドマネージャー** | [マネージャーガイド](guides/hedge-fund-manager.md) |
| **ガイドインデックス** | [ガイド概要](guides/README.md) |

## クイックコマンド

```bash
pip install -r requirements.txt
pytest -q
py examples/replay_demo.py           # 最小リプレイ
py omega_point.py                    # フル omega リプレイ
py main.py                           # Omni + Utahrbitrage
py main.py --prediction-demo         # 予測 AMI
py main.py --dashboard               # Streamlit UI
py omega_point.py --uri wss://... --live
```

## チュートリアル（学習パス）

| # | チュートリアル |
|---|----------------|
| 01 | [インストールと検証](tutorials/01-install-and-verify.md) |
| 02 | [最初のリプレイパイプライン](tutorials/02-first-replay-pipeline.md) |
| 03–10 | [全文インデックス](tutorials/README.md) |

## コードレシピ

[recipes/README.md](recipes/README.md) — マニフォールド、アルファ、Utahrbitrage、予測ラティスのコピペ用スニペット。

## ドキュメントマップ（視覚）

```text
                    ┌─────────────────┐
                    │ project-overview│
                    │  (支援 + 実行)  │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
   for-kids.md        for-everyone.md    technical-architecture.md
         │                   │                   │
         └───────────────────┴───────────────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        migration/*     guides/*      api-reference.md
```

## Utah への支払い

本番でスタックが役立った場合は **[utah@utahcreates.com](mailto:utah@utahcreates.com)** へメール。詳細: [paying-utah.md](paying-utah.md)。支払い管理用デスクトップ GUI は計画中です。

## 他の言語

| 言語 | ハブ |
|------|------|
| English | [../../README.md](../../README.md) |
| Русский | [../ru/README.md](../ru/README.md) |
| Eesti | [../et/README.md](../et/README.md) |
| Suomi | [../fi/README.md](../fi/README.md) |
| 简体中文 | [../zh/README.md](../zh/README.md) |

一覧: [languages.md](languages.md)

*マニフォールドは税務・法務・キャリアアドバイスは提供しません。曲率は提供します。*
