# Omni アーキテクチャ — TAD と Symplectic 強化

## モジュールマップ

| モジュール | 役割 |
|--------|------|
| `adelic_sieve.py` | Adelic Sieve Kernel — マルチプライム共鳴、void 検出 |
| `symplectic_veto.py` | Symplectic Veto-Matrix — 容量 + shadow 監査マージ |
| `ghost_rotator.py` | Ghost-Rotation シンプレクトomorphism |
| `transfinite.py` | 位相シフト出来高注入 + スペクトル分散上限 |
| `utah_flux.py` | 不変 flux 状態ストリーム |
| `omni_discovery_engine.py` | マスターサイクル: sense → audit → rotate → sync |
| `utahrbitrage.py` | **Utahrbitrage** — Omega-Point ルーティング + タイス固有値 |

## 実行エントリポイント

```bash
py main.py                    # Omni + Omega replay
py main.py --live --uri wss://...
py main.py --dashboard        # Streamlit Omni-Sieve UI
py omega_point.py             # クラシック閉ループ（Omni 有効）
```

## シグナル拡張

| シグナル | 意味 |
|--------|---------|
| `ADELIC_VOID` | 流動性真空（低いクロスプライム共鳴） |
| `ADELIC_RESONANCE` | 強いマルチスケール干渉 |

## 実装メモ

コア数学は **NumPy**（JAX 不要）で最小依存。ブループリントの JAX `@jit` パスは将来オプション追加可能。

## Utahrbitrage タイス定数

| 定数 | 値 |
|----------|-------|
| `HANS_TITHE_CONSTANT` | 0.023 |
| `HUMANITARIAN_CONSTANT` | 0.015 |

各 `FluxState` に `utah_route` と `humanity_route` として記録。[utahrbitrage.md](utahrbitrage.md) 参照。
