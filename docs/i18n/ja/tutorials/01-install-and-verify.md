# チュートリアル 01: インストールと検証

## 目標

UtahIsMyQuant をクローンし、依存関係をインストールし、全テストが通ることを確認する。

## 手順

### 1. クローン

```bash
git clone https://github.com/utahisnotastate/UtahIsMyQuant.git
cd UtahIsMyQuant
```

### 2. 仮想環境

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. テスト実行

```bash
pytest -q
```

### 4. 構成を探索

```text
src/           Core engines
tests/         62+ unit tests
omega_point.py Closed-loop runner
main.py        Omni + prediction demos
docs/          All documentation
examples/      Runnable example scripts
```

### 5. 最初のデモ

```bash
py omega_point.py
```

`// OMEGA COMPLETE` で終わるログ行が見えるはず。

## トラブルシューティング

| 問題 | 対処 |
|-------|-----|
| `python` が見つからない | Windows では `py` を使う |
| `websockets` インポートエラー | `pip install -r requirements.txt` |
| テストがハング | ゾンビ Python がないか確認；`pytest -q --maxfail=1` |

## 次へ

[チュートリアル 02: 最初のリプレイパイプライン](02-first-replay-pipeline.md)
