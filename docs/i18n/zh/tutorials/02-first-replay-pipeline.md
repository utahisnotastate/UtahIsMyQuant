# 教程 02：首个回放流水线

## 目标

在无实时市场数据的情况下运行完整**感知 → 决策 → 保护**循环。

## 代码

保存为 `examples/replay_demo.py` 或运行：

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

## 发生了什么

1. **TickObserver** 摄取 JSON tick
2. **AlphaGenerator** 计算流形特征 + 门控
3. **RiskSupervisor** + symplectic veto 可能阻止交易
4. **OmniDiscoveryEngine** 同步 Utahrbitrage + prediction lattice

## 检查一个事件

```python
e = events[-1]
print(e.decision)       # full decision dict
print(e.supervisor_verdict)
print(e.circuit_breaker)
```

## 下一步

[教程 03：仅流形信号](03-manifold-signals-only.md)
