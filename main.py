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


def run_prediction_demo(pool_depth: float = 50_000.0) -> None:
    """Demonstrate Utah Consensus Lattice AMI on synthetic whale flux."""
    import numpy as np

    from src.utah_prediction_engine import UtahConsensusLattice

    lattice = UtahConsensusLattice(initial_pool_depth=pool_depth)
    whale_flux = np.array([10_000.0, 2500.0, 500.0])
    retail_flux = np.array([50.0, 75.0, 60.0])
    for label, flux in [("whale", whale_flux), ("retail", retail_flux)]:
        s = lattice.execute_market_trade(flux, market_impact_factor=0.05)
        ami = lattice.ami_whale_dampening(flux, whale_threshold=10_000.0)
        logger.info(
            "// PREDICTION [%s] delta=%.6f utah=%.2f hum=%.2f ami=%.3f",
            label,
            s.protected_delta,
            s.utah_route,
            s.humanitarian_route,
            ami,
        )


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
    parser.add_argument(
        "--prediction-demo",
        action="store_true",
        help="Run Utah Consensus Lattice prediction-market AMI demo",
    )
    parser.add_argument("--pool-depth", type=float, default=50_000.0)
    args = parser.parse_args()
    if args.prediction_demo:
        run_prediction_demo(args.pool_depth)
        return
    if args.dashboard:
        from run_app import run_dashboard_cli

        run_dashboard_cli()
        return
    asyncio.run(run_omega(args.uri, args.capital, args.live))


if __name__ == "__main__":
    main()
