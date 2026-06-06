# 代码配方

最小可复制粘贴片段。假设仓库根目录在 `PYTHONPATH` 上（`pytest.ini` 已设置）。

```python
# At top of scripts run from repo root:
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
```

或从仓库根运行：`py your_script.py`

| 配方 | 说明 |
|------|------|
| [manifold.md](manifold.md) | 曲率、熵、信号 |
| [alpha-gates.md](alpha-gates.md) | 逻辑门控、决策 |
| [utahrbitrage.md](utahrbitrage.md) | Omega-Point 路由 |
| [prediction-lattice.md](prediction-lattice.md) | AMI 预测市场 |
| [full-tick-handler.md](full-tick-handler.md) | 端到端 tick 处理 |
