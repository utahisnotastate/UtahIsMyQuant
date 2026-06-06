# コードレシピ

最小のコピペ用スニペット。リポジトリルートが `PYTHONPATH` にある前提（`pytest.ini` が設定）。

```python
# At top of scripts run from repo root:
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
```

またはリポジトリルートから: `py your_script.py`

| レシピ | 説明 |
|--------|-------------|
| [manifold.md](manifold.md) | 曲率、エントロピー、シグナル |
| [alpha-gates.md](alpha-gates.md) | ロジックゲート、決定 |
| [utahrbitrage.md](utahrbitrage.md) | Omega-Point ルーティング |
| [prediction-lattice.md](prediction-lattice.md) | AMI 予測市場 |
| [full-tick-handler.md](full-tick-handler.md) | エンドツーエンドティック処理 |
