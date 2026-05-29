# Code Recipes

Minimal copy-paste snippets. Assumes repo root on `PYTHONPATH` (`pytest.ini` sets this).

```python
# At top of scripts run from repo root:
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
```

Or run from repo root: `py your_script.py`

| Recipe | Description |
|--------|-------------|
| [manifold.md](manifold.md) | Curvature, entropy, signals |
| [alpha-gates.md](alpha-gates.md) | Logic gates, decisions |
| [utahrbitrage.md](utahrbitrage.md) | Omega-Point routing |
| [prediction-lattice.md](prediction-lattice.md) | AMI prediction markets |
| [full-tick-handler.md](full-tick-handler.md) | End-to-end tick processing |
