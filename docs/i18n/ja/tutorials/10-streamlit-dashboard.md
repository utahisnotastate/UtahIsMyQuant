# チュートリアル 10: Streamlit ダッシュボード

## 目標

VaR プロキシと symplectic 容量を並べた **Omni-Sieve** ダッシュボードを起動する。

## 実行

```bash
pip install streamlit
py main.py --dashboard
```

または:

```bash
streamlit run src/ui/omni_sieve_dashboard.py
```

## 表示内容

- 左: 合成「既存」分散プロキシ
- 中央: symplectic マニフォールド容量
- 右: utah-flux 最新共鳴

## カスタマイズ

`src/ui/omni_sieve_dashboard.py` を編集してライブ flux ストリームを接続。

## 完了

[チュートリアル README](README.md) または [全文インデックス](../README.md) へ戻る。
