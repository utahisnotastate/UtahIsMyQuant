"""Example: probe manifold signals — py examples/manifold_probe.py"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.manifold_kernel import ManifoldEngine


def main() -> None:
    engine = ManifoldEngine(sensitivity=0.01)
    spike = np.concatenate([np.linspace(100, 110, 20), np.linspace(110, 90, 20)])
    c = engine.calculate_curvature(spike)
    ent = engine.differential_entropy(spike)
    sig = engine.generate_signal(c, entropy=ent, entropy_baseline=1.0)
    print(f"curvature={c:.4f} entropy={ent:.4f} signal={sig}")


if __name__ == "__main__":
    main()
