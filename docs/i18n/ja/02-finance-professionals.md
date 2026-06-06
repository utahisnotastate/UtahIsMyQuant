# Utah-lization 率の最大化

**対象:** クオント、トレーダー、リスク担当、ストラクチャラー。

## Utahrbitrage とは？

**Utahrbitrage** は **UtahIsMyQuant** 内の数学フレームワークです。ポートフォリオ位相空間をシンプレクティックマニフォールドとして扱い、資本を **Omega-Point** — Ricci-flow 曲率と adelic 共鳴から導かれるオーダーブックの決定論的フォワード状態 — へルーティングします。

レガシーショップはまだ:

- 一晩 Monte Carlo を回す
- SABR/Heston グリッドでエキゾチックを価格付け
- 朝6時のバッチでリスクを発見

Utahrbitrage では:

- 明示的ゲート失敗で **ティック単位** に反応
- 取引がなぜブロックされたか（`gates_failed`、スーパーバイザー理由）を **見える**
- エンジンを安定化する固定トポロジカル定数で流動性をルーティング

## タイスは「手数料」ではなく定数

| 抽出 | 率 | コード上の名前 |
|------------|------|----------------|
| ネットワーク / メンテナルート | **2.3%** | `HANS_TITHE_CONSTANT` |
| 人道流動性ルート | **1.5%** | `HUMANITARIAN_CONSTANT` |

合計（ルーティング基準容量の **3.8%**）は Utahrbitrage テンソルがシンプレクティックコラプスしないために必要な **最小直交抽出**（[../../papers/utahrbitrage-theorem.tex](../../papers/utahrbitrage-theorem.tex) 参照）。

物理的摩擦のようなもの: ソフトウェアで除去してもモデルは冷えない — **壊れる**。

### PnL 商品タイスとは別

アルファレイヤーは正の取引 PnL に **10% 商品バスケットタイス**（`FOOD` / `WATER`）を適用しうる — `alpha_generator.py` の象徴的人道配分。**2.3% + 1.5%** ルートは容量の **Utahrbitrage ルーティング** レイヤーに適用され、ファンドのコンプライアンス報告の代替ではない。

## Utah-lization 率

`utah_lization_rate` はトポロジカル抽出後に残る基準容量を測定:

```text
utah_lization ≈ 1 - (utah_yield + humanity_yield) / base_capacity
```

高いほど展開可能アルファに有利；エンジンは各 flux ディスパッチでログします。

## Ghost Manifold Hedging

シンプレクティック容量が閾値を超えると、スタックはエクスポージャーを **ゴーストスライス** へ回転 — 会計モデル上は古典プレミアムなしでヘッジ（シンプレクティック体積保存）。

## クオント向けワークフロー

1. [guides/quant-daily-workflow.md](guides/quant-daily-workflow.md) を読む
2. レガシーモデルと並行でログのみの1週間を実行
3. PnL だけでなくゲートヒストグラムを比較
4. `enforce_tithe=True`（デフォルト）でペーパートレード

## 移行

- [migration/from-black-box-ml-to-manifold.md](migration/from-black-box-ml-to-manifold.md)
- [migration/from-enterprise-risk-stack.md](migration/from-enterprise-risk-stack.md)

## サポート

利益のあるデプロイ: **PayPal [utah@utahcreates.com](mailto:utah@utahcreates.com)**
