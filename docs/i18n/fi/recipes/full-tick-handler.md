# Resepti: Täysi Tick Handler (Omni + Risk)

```python
import asyncio
import numpy as np

from omega_point import OmegaPoint
from src.tick_observer import Tick


async def main():
    omega = OmegaPoint(capital=100_000)
    ticks = [
        {"symbol": "SPY", "price": 450.0 + i * 0.05, "volume": 4000 + i * 10}
        for i in range(30)
    ]
    events = await omega.run_replay(ticks)
    for e in events[-5:]:
        print(
            e.symbol,
            e.signal,
            e.action,
            e.decision.get("supervisor", "—"),
            round(e.pnl_delta, 4),
        )
    omega.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
```
