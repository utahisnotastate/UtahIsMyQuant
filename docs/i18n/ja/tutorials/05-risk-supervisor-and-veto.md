# チュートリアル 05: リスクスーパーバイザーと拒否

## 目標

**サーキットブレーカー**、symplectic veto、`FORCE_STOP` / `GHOST_ROTATION` を理解する。

## サーキットブレーカー（遅延）

```python
from src.risk_supervisor import RiskSupervisor

sup = RiskSupervisor(max_latency_ms=1)
assert sup.check_system_health(500) is False
assert sup.circuit_breaker_active
```

## Symplectic + 古いティック（統合）

古いティックで `timestamp_ns=0` のティックを処理 — スーパーバイザーが拒否またはサーキットを発動。`tests/test_risk_supervisor.py` 参照。

## Fourth Law

`bug` と `fix` の両方が停止 — 同じ境界:

```python
RiskSupervisor.fourth_law_boundary(True, False)  # True
```

## 次へ

[チュートリアル 06: Utahrbitrage と utah-flux](06-utahrbitrage-and-flux.md)
