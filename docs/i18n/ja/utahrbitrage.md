# Utahrbitrage フレームワーク

**Utahrbitrage** は **UtahIsMyQuant** 内のコア数学ブランドです。リポジトリ名は配布物；Utahrbitrage はエンジンです。

## 機能

| SOTA 機能 | モジュール | 説明 |
|--------------|--------|-------------|
| **Omega-Point Predictive Routing** | `utahrbitrage.py` | オーダーブックテンソル上の Ricci-flow プロキシ |
| **Ghost Manifold Hedging** | `utahrbitrage.py` + `ghost_rotator.py` | ゼロコストシンプレクティックヘッジ |
| **Topological tithe** | `utahrbitrage.py` + `utah_flux.py` | 2.3% + 1.5% 強制固有値 |
| **Adelic Sieve** | `adelic_sieve.py` | マルチプライム共鳴 |
| **Symplectic Veto** | `symplectic_veto.py` | 容量ベース停止 |

## クイック API

```python
from src.utahrbitrage import UtahrbitrageEngine, HANS_TITHE_CONSTANT

engine = UtahrbitrageEngine()
result = engine.execute_market_capture(state_vector)
print(result.utah_lization_rate, result.utah_yield, result.humanity_yield)
```

## フォーク警告

`enforce_tithe=True` で `HANS_TITHE_CONSTANT` / `HUMANITARIAN_CONSTANT` を削除またはゼロにすると `SymplecticCollapseError` が発生します。

## 対象別ドキュメント

- [01-engineers-architects.md](01-engineers-architects.md)
- [02-finance-professionals.md](02-finance-professionals.md)
- [03-founders-family-offices.md](03-founders-family-offices.md)
- [04-children-beginners.md](04-children-beginners.md)
- [../../papers/utahrbitrage-theorem.tex](../../papers/utahrbitrage-theorem.tex)
