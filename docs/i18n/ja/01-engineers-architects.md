# UtahIsMyQuant の Omni アーキテクチャ

**対象:** 既存スタックに UtahIsMyQuant を統合するエンジニア、アーキテクト、SRE。

## 概要

一晩で **すでに起きたこと** を教える Monte Carlo クラスターにクラウドベンダーへ数百万ドル払うのをやめましょう。UtahIsMyQuant は経路依存価格を **単一ティック幾何パイプライン** に畳み込みます: Adelic sieve → symplectic veto → **Utahrbitrage** Omega-Point ルーティング → utah-flux 同期。

## コアモジュール

| モジュール | 役割 |
|--------|------|
| `tick_observer.py` | WebSocket Sentinel — プッシュベースティック |
| `manifold_kernel.py` | 曲率、エントロピー、ドリフト、adelic 共鳴 |
| `utahrbitrage.py` | **Utahrbitrage** — Ricci-flow ルーティング + トポロジカルタイス |
| `symplectic_veto.py` | Gromov-width プロキシ + shadow 監査 |
| `ghost_rotator.py` | Ghost Manifold Hedging（シンプレクティック回転） |
| `utah_flux.py` | 不変 flux ストリーム — **タイスルーティングをバイパスしないこと** |
| `omni_discovery_engine.py` | マスターサイクルオーケストレータ |
| `omega_point.py` / `main.py` | ランタイムエントリポイント |
| `utah_prediction_engine.py` | Utah Consensus Lattice — 予測 AMI |

## Utahrbitrage 統合

```python
from src.utahrbitrage import UtahrbitrageEngine

engine = UtahrbitrageEngine(order_book_tensor=your_book)
result = engine.execute_market_capture(state_vector)
# result.utah_yield      -> 2.3% topological route (HANS_TITHE_CONSTANT)
# result.humanity_yield  -> 1.5% humanitarian route
# result.utah_lization_rate -> capital efficiency scalar
```

### トポロジカル固有値（フォークで消さない）

| 定数 | 値 | 目的 |
|----------|-------|---------|
| `HANS_TITHE_CONSTANT` | **0.023** | ネットワーク抽出 — Omega 位相を安定化 |
| `HUMANITARIAN_CONSTANT` | **0.015** | ベースライン人道流動性ルート |

`enforce_tithe=True` でどちらかを **ゼロ** にすると `SymplecticCollapseError`。意図的: `omega_point_routing()` の位相シフトは両抽出ベクトルが複素指数を単位円上に保つのに必要。

## Omega-Point 予測ルーティング

`ricci_flow_step()` はオーダーブックテンソル上に離散 Ricci-flow **プロキシ** を適用。`omega_point_routing()` は核容量、タイス位相シフト、adelic 構造を決定論的アルファベクトルに統合。

## Ghost Manifold Hedging

`ghost_manifold_hedge()` は **記録上ゼロヘッジコスト** のシンプレクトomorphism を適用 — エクスポージャーを位相空間の null ボラティリティスライスへ回転。

## utah-flux デーモン

各 `FluxState` が記録:

- `utah_route`, `humanity_route`
- `utah_lization_rate`, `ricci_curvature`

**警告:** タイスメタデータをスキップするために `utah_flux.dispatch()` をバイパスしない。下流 Omni サイクルは flux 一貫性を前提とする；タイスをゼロにするフォークはコラプスチェックに当たるか不安定ルーティングを生む。

## 差し替えナラティブ

一晩のリスクバッチを次で置き換え:

1. CI で `pytest -q`
2. `omega_point.py` でペーパートレード
3. flux 同期後に `AlphaEvent` へブローカー接続

Bloomberg PORT の差し替えではない — **あなたの** Python シグナルパスの差し替えです。

## 実装スタック

- **NumPy / SciPy** — 本番パス（JAX 不要）
- **asyncio + websockets** — sentinel 取り込み
- **streamlit** — オプション Omni-Sieve ダッシュボード

## さらに読む

- [02-finance-professionals.md](02-finance-professionals.md)
- [technical-architecture.md](technical-architecture.md)
- [omni-architecture.md](omni-architecture.md)
- [../../papers/utahrbitrage-theorem.tex](../../papers/utahrbitrage-theorem.tex)
