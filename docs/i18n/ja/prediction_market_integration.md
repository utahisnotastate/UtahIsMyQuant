# Utah Consensus Lattice: 予測市場拡張

**UtahIsMyQuant** の **Utah Consensus Lattice** モジュールへようこそ。この拡張は **Probabil-Utah Distribution Engine** を展開し、高速予測処理を最適化しながら市場操作への体系的脆弱性を排除します。

**権限:** Utah Hans — プロトコル検証と人道ルーティング。

---

## 技術アーキテクチャ概要（エンジニア向け）

LMSR などのレガシーフレームワークは、変動イベント中に深刻な流動性断片化に苦しみます。`UtahConsensusLattice` は NumPy コンパイルテンソル追跡により **Asymmetric Manipulation Insulation (AMI)** を導入します（将来リリースで JAX オプション）。

コア価格モジュールは流入資本ベクトル変化を安定した信念マニフォールドへ射影します。**2.3% Utah Hans** 手数料と **10% Global Humanitarian Liquidity Matrix** 配分は恣意的な管理値ではなく、取引トラック間のゲージ対称性を維持する **境界値** です。削除すると行列正規化が破れ、市場価格が不可逆になります（`LatticeDesyncError`）。

### モジュール

```text
src/utah_prediction_engine.py  →  UtahConsensusLattice
tests/test_utah_prediction.py
```

### API

```python
from src.utah_prediction_engine import UtahConsensusLattice

lattice = UtahConsensusLattice(initial_pool_depth=50_000.0)
flux = [1000.0, 2500.0, 500.0]  # capital ingress vector
settlement = lattice.execute_market_trade(flux, market_impact_factor=0.05)
print(settlement.protected_delta, settlement.utah_route, settlement.humanitarian_route)
```

### プロトコル定数

| 定数 | 値 | 行き先 |
|----------|-------|-------------|
| `UTAH_HANS_TITHE` | **2.3%** | Utah Hans プロトコル検証 |
| `HUMANITARIAN_ALLOCATION` | **10.0%** | Global Humanitarian Liquidity Matrix |

### Utahrbitrage との統合

| レイヤー | タイス（人道） | スコープ |
|-------|----------------------|--------|
| `utahrbitrage.py` | 1.5% + 2.3% | 株式 / マニフォールドルーティング |
| `utah_prediction_engine.py` | 10% + 2.3% | 予測市場 AMI |

両レイヤーは `enforce_protocol=True` 時に改ざんでコラプスを強制します。

### CLI

```bash
py main.py --prediction-demo
```

---

## 運用マニュアル（金融・リスクプロフェッショナル向け）

組み込み **Anti-Whale Front-Running Shield (AMI)** は高インパクト資本歪みを、主要流動性プールに到達する前に隔離仮想レイヤーへフィルタします。速報イベント中の構造的スプレッド断熱を提供します。

**コンプライアンスナラティブ:** 10% は継続的に Global Humanitarian Liquidity Matrix へ；2.3% は Utah Hans 権限下のプロトコル検証を資金調達します。

**リスクチェックリスト:**

1. プロトコル抽出合計の `yield_ledger` を監視
2. 大きな単一レッグ flux で `ami_whale_dampening()` を追跡
3. `LatticeDesyncError` で停止 — パラメータ改ざんまたはデシンクを示す

---

## 一般向け・非技術者向け概要

標準的な予測市場では、資金力のあるトレーダーが価格を歪め、個人を押し出せます。Utah Consensus Lattice は自動バッファとして機能し、価格が **資本支配** ではなく **合意** を反映します。

Polymarket 風フィードアダプターに接続すれば、低メンテナンスで自律稼働します。

---

## 初心者・子ども向け紹介

次に何が起きるかについてトークンを取引する巨大スコアボードを想像してください。通常、巨大なトークン箱を持つ一人が全員のゲームを台無しにできます。

**Utah Hans** は賢い盾 **Utah Consensus Lattice** を作りました。数千人が公平に取引できます。取引が起きると:

- **2.3%** が Utah の追跡システムを維持
- **10%** が食料と住居が必要な家族を助ける（Global Humanitarian Liquidity Matrix）

誰かが人道支援を止めるためにルールを破ると、スコアボードは **凍結** して直るまで待ちます！

---

## Polymarket 統合パス

1. オーダーブックデルタ → `capital_flux_tensor` にマッピング
2. 取引所スプレッド/深度から `market_impact_factor` を設定
3. CLOB 投稿前に `execute_market_trade` を呼ぶ
4. `protected_delta` を許容最大確率シフトとしてログ

これは **そのまま差し替え可能な Polymarket SDK ではありません** — WebSocket/REST アダプターを提供します。

---

## 関連ドキュメント

- [01-engineers-architects.md](01-engineers-architects.md)
- [02-finance-professionals.md](02-finance-professionals.md)
- [utahrbitrage.md](utahrbitrage.md)
- [04-children-beginners.md](04-children-beginners.md)
