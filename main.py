"""
UtahIsMyQuant — Omni Discovery entry point.
Binds Adelic Sieve, Symplectic Veto-Matrix, Ghost-Rotator, and utah-flux.
"""
from __future__ import annotations

import argparse
import asyncio
import logging

from omega_point import OmegaPoint
from src.omni_discovery_engine import OmniDiscoveryEngine

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("main")


async def run_omega(uri: str | None, capital: float, live: bool) -> None:
    omni = OmniDiscoveryEngine()
    omega = OmegaPoint(uri=uri, capital=capital, enable_live=live)
    omega.alpha.omni = omni
    try:
        if live:
            await omega.run_live()
        else:
            from omega_point import _demo_ticks

            events = await omega.run_replay(_demo_ticks())
            flux = omni.flux.get_latest_manifold()
            logger.info(
                "// OMNI SYNC: events=%d resonance=%.4f capacity=%s",
                len(events),
                flux.adelic_resonance if flux else 0,
                f"{flux.symplectic_capacity:.4f}" if flux else "n/a",
            )
    finally:
        omega.shutdown()


def main() -> None:
    parser = argparse.ArgumentParser(description="UtahIsMyQuant Omni Discovery")
    parser.add_argument("--uri", default=None, help="WebSocket tick URI")
    parser.add_argument("--capital", type=float, default=100_000.0)
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--dashboard", action="store_true", help="Launch Streamlit Omni-Sieve UI")
    args = parser.parse_args()
    if args.dashboard:
        from run_app import run_dashboard_cli

        run_dashboard_cli()
        return
    asyncio.run(run_omega(args.uri, args.capital, args.live))


if __name__ == "__main__":
    main()
