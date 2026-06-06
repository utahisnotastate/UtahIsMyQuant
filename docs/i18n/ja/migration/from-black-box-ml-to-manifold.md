# 移行: ブラックボックス ML（LSTM 等）→ マニフォールド幾何学

## 該当する場合…

- フィーチャストア + 夜間学習パイプライン
- 説明できないモデル版 `v847`
- GPU 予算の経費項目

## 概念的マッピング

| ML スタック | マニフォールド + Utahrbitrage スタック |
|----------|-------------------------------|
| 隠れ状態 | 価格ウィンドウ（デフォルト64ティック） |
| Attention / レイヤー | 曲率 + エントロピー + ドリフト + adelic 共鳴 |
| 予測ヘッド | `generate_signal()` + `omega_point_routing()` |
| 正則化 | ロジックゲート + shadow tensor + symplectic veto |
| ドリフト検出 | `ShadowTensorAudit` ミラー率 |
| 推論 GPU | CPU NumPy/SciPy（意図的にリーン） |
| 不透明な「手数料」 | **トポロジカル固有値** 2.3% + 1.5%（`utahrbitrage.py`） |

## 最終的に削除するもの

- 日中アルファ用の学習 cron（EOD 分析は別途残してよい）
- サブ秒決定用の巨大フィーチャ DAG
- ハイパーパラメータ探索クラスタ

## 残すもの

- **クリーンなティック** のデータエンジニアリング（もう一層より価値が高い）
- ポートフォリオ会計 / PnL システム
- コンプライアンス報告（外部）

## 切り替え手順

### 1. マニフォールドを並行「モデル B」として実行

並べてログ:

- ML シグナル: `buy_prob=0.73`
- マニフォールド: `signal=BREAKOUT_PRIMED`, `gates_failed=[]`

### 2. 不一致日を比較

ML が取引してマニフォールドが WAIT の日はゲート理由で事後分析。マニフォールドが取引して ML が待つ日はスーパーバイザー結果を確認。

### 3. **遅延クリティカル** パスから先に ML を廃止

遅いスリーブ（日次リバランス）で ML が利益なら残す — ハイブリッドショップでよい。

### 4. 解釈可能性でスタッフを再教育

各 `AlphaEvent` は一文で説明可能:

> 「ブレイクアウト準備、エントロピー圧縮、出来高 OK、リスク OK、shadow 健全 → NAV の2% BUY。」

## 落とし穴

| 落とし穴 | 緩和 |
|---------|------------|
| 「マニフォールドは単純すぎ」 | 単純さは遅延 + 監査可能性 |
| 薄いウィンドウでエントロピー不安定 | `entropy_window` を増やす |
| チームの AUC ノスタルジア | AUC ではなくライブスリッページ調整後 PnL を追跡 |

## コードブリッジ（アンサンブル）

```python
async def ensemble_handler(tick: Tick):
    ml_side = your_ml_model.predict(tick)
    event = alpha.process_tick(tick)
    if ml_side == "BUY" and event.action == Action.BUY:
        await execute(tick, event)
```

## 次へ

- [技術アーキテクチャ](../technical-architecture.md)
