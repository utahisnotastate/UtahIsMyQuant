"""
Omega Point — closed-loop UtahIsMyQuant execution.
Sense (TickObserver) → Decide (AlphaGenerator) → Protect (RiskSupervisor).

Fourth Law: bug and fix share the same execution boundary; the supervisor
acts on both identically and instantaneously.
"""
from __future__ import annotations

import argparse
import asyncio
import logging
from typing import Any

import numpy as np

from src.alpha_generator import AlphaEvent, AlphaGenerator
from src.risk_supervisor import RiskSupervisor
from src.tick_observer import Tick, TickObserver

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("omega_point")


class OmegaPoint:
    """ZEO protocol closed-loop orchestrator."""

    def __init__(
        self,
        uri: str | None = None,
        capital: float = 100_000.0,
        enable_live: bool = False,
    ):
        self.observer = TickObserver(uri=uri)
        self.alpha = AlphaGenerator(capital=capital, enable_shadow_audit=True)
        self.supervisor = RiskSupervisor()
        self.alpha.supervisor = self.supervisor
        self.supervisor.start_background()
        self.alpha.attach(self.observer)
        self._events: list[AlphaEvent] = []
        self.enable_live = enable_live

    def _positions_from_alpha(self) -> list[dict[str, Any]]:
        positions: list[dict[str, Any]] = []
        for symbol, state in self.alpha._states.items():
            if state.exposure <= 0 or not state.prices:
                continue
            entry = state.prices[0]
            side = "long" if state.side.value in ("BUY",) else "short"
            positions.append(
                {
                    "symbol": symbol,
                    "entry_price": entry,
                    "value": state.exposure,
                    "side": side,
                }
            )
        return positions

    async def on_tick_guarded(self, tick: Tick) -> AlphaEvent | None:
        """Observer handler: alpha decides, supervisor protects."""
        event = await self.alpha.on_tick(tick)
        if event is None:
            return None
        self._events.append(event)
        if event.decision.get("supervisor") == "FORCE_STOP":
            logger.error("// OMEGA: Forced exit %s — %s", tick.symbol, event.decision.get("reason"))
        elif event.decision.get("action") == "WAIT" and "supervisor" in str(
            event.decision.get("gates_failed", ())
        ):
            logger.warning("// OMEGA: Supervisor veto — %s", event.decision.get("reason"))
        return event

    async def run_replay(self, ticks: list[dict[str, Any]]) -> list[AlphaEvent]:
        """Simulated tick stream for integration without live WebSocket."""
        self.observer.unsubscribe(self.alpha.on_tick)
        self.observer.subscribe(self.on_tick_guarded)
        self.observer._running = True
        self.observer._process_task = asyncio.create_task(self.observer.process())
        for raw in ticks:
            await self.observer.ingest(raw)
        await self.observer.queue.join()
        await self.observer.stop()
        return list(self._events)

    async def run_live(self) -> None:
        if not self.observer.uri:
            raise ValueError("Live mode requires --uri wss://...")
        self.observer.unsubscribe(self.alpha.on_tick)
        self.observer.subscribe(self.on_tick_guarded)
        self.observer.start_sentinel()
        try:
            await asyncio.Future()
        except asyncio.CancelledError:
            pass
        finally:
            await self.observer.stop()

    def shutdown(self) -> None:
        self.alpha.shutdown()
        self.supervisor.stop()


def _demo_ticks() -> list[dict[str, Any]]:
    rng = np.random.default_rng(7)
    base = 450.0
    out: list[dict[str, Any]] = []
    for i in range(40):
        base += float(rng.normal(0, 0.3))
        out.append({"symbol": "SPY", "price": base, "volume": 5000 + i * 10})
    return out


async def _main_async(args: argparse.Namespace) -> None:
    omega = OmegaPoint(uri=args.uri, capital=args.capital, enable_live=args.live)
    try:
        if args.live:
            await omega.run_live()
        else:
            events = await omega.run_replay(_demo_ticks())
            logger.info("// OMEGA COMPLETE: %d events, circuit=%s", len(events), omega.supervisor.circuit_breaker_active)
    finally:
        omega.shutdown()


def main() -> None:
    parser = argparse.ArgumentParser(description="UtahIsMyQuant Omega Point executor")
    parser.add_argument("--uri", default=None, help="WebSocket tick feed URI")
    parser.add_argument("--capital", type=float, default=100_000.0)
    parser.add_argument("--live", action="store_true", help="Run live WebSocket sentinel")
    args = parser.parse_args()
    asyncio.run(_main_async(args))


if __name__ == "__main__":
    main()
