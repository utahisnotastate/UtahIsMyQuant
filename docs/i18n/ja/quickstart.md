# クイックスタート — UtahIsMyQuant を 10 分で

## 前提条件

- Python 3.11 以上（3.14 で動作確認済み）
- Git

## 1. クローンとインストール

```powershell
git clone https://github.com/utahisnotastate/UtahIsMyQuant.git
cd UtahIsMyQuant
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. 動作確認

```bash
pytest -q
```

期待値: **62 passed**（正確な数はローカルで確認）。

## 3. デモ（実資金なし）

| コマンド | 内容 |
|----------|------|
| `py omega_point.py` | 閉ループ: ティック → アルファ → リスク |
| `py main.py` | Omni Discovery + Utahrbitrage |
| `py main.py --prediction-demo` | Utah Consensus Lattice (AMI) |
| `py main.py --dashboard` | Streamlit UI |

## 4. 次に読むもの

| 目的 | ドキュメント |
|------|----------------|
| アーキテクチャを理解 | [technical-architecture.md](technical-architecture.md) |
| コピペ用コード | [tutorials/README.md](tutorials/README.md) |
| API 参照 | [api-reference.md](api-reference.md) |
| レガシースタックから移行 | [migration/README.md](migration/README.md) |

## 5. Utah への支払い

役立った場合: [paying-utah.md](paying-utah.md) — [utah@utahcreates.com](mailto:utah@utahcreates.com) へメール。支払い GUI アプリは計画中。

## 6. 他の言語

Русский · Eesti · English — 別ページ: [languages.md](languages.md)
