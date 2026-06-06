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
| やさしい概要 | [for-everyone.md](for-everyone.md) |
| 作者への支援 | [paying-utah.md](paying-utah.md) |
| アーキテクチャ | [../../technical-architecture.md](../../technical-architecture.md) **(English)** |
| API | [../../api-reference.md](../../api-reference.md) **(English)** |

## 5. ナビゲーション

- [日本語ハブ](README.md)
- [言語一覧](../../languages.md) **(English)**
