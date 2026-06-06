# チュートリアル 02: 最初のリプレイパイプライン

## 目標

ライブ市場データなしで **sense → decide → protect** の全ループを実行する。

## コード

`examples/replay_demo.py` として保存するか実行:

```bash
py examples/replay_demo.py
```

```python
import asyncio
from omega_point import OmegaPoint

async def main():
    omega = OmegaPoint(capital=100_000)
    ticks = [
        {"symbol": "SPY", "price": 450.0 + i * 0.1, "volume": 5000}
        for i in range(25)
    ]
    events = await omega.run_replay(ticks)
    print(f"Processed {len(events)} alpha events")
    if events:
        last = events[-1]
        print("Last:", last.signal, last.action, last.gates_failed)
    omega.shutdown()

asyncio.run(main())
```

## 何が起きたか

1. **TickObserver** が JSON ティックを取り込んだ
2. **AlphaGenerator** がマニフォールド特徴量 + ゲートを計算
3. **RiskSupervisor** + symplectic veto が取引をブロックしうる
4. **OmniDiscoveryEngine** が Utahrbitrage + 予測ラティスを同期

## 1イベントを検査

```python
e = events[-1]
print(e.decision)       # full decision dict
print(e.supervisor_verdict)
print(e.circuit_breaker)
```

## 次へ

[チュートリアル 03: マニフォールドシグナルのみ](03-manifold-signals-only.md)
