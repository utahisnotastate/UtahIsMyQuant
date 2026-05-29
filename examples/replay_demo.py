"""Example: OmegaPoint replay demo — run from repo root: py examples/replay_demo.py"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from omega_point import OmegaPoint


async def main() -> None:
    omega = OmegaPoint(capital=100_000)
    ticks = [
        {"symbol": "SPY", "price": 450.0 + i * 0.1, "volume": 5000 + i * 10}
        for i in range(25)
    ]
    events = await omega.run_replay(ticks)
    print(f"// REPLAY: {len(events)} events")
    if events:
        e = events[-1]
        print(f"// LAST: signal={e.signal} action={e.action} gates={e.gates_failed}")
    omega.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
