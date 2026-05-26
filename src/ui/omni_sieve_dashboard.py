"""
Omni-Sieve Dashboard — Streamlit comparison: Euclidean VaR vs Symplectic Ghost-Manifold.
"""
from __future__ import annotations

import numpy as np

try:
    import streamlit as st
except ImportError:  # pragma: no cover
    st = None  # type: ignore[assignment]

from src.risk_supervisor import RiskSupervisor
from src.symplectic_veto import SymplecticVetoMatrix
from src.utah_flux import UtahFluxEngine


def run_dashboard() -> None:
    if st is None:
        raise ImportError("Install streamlit: pip install streamlit")

    st.set_page_config(page_title="UtahIsMyQuant", layout="wide")
    st.title("UtahIsMyQuant: Symplectic Manifold Explorer")
    st.caption("Omni-Sieve — incumbent Gaussian noise vs ghost-manifold invariants")

    flux = UtahFluxEngine()
    veto = SymplecticVetoMatrix(capacity_threshold=0.85)
    legacy = RiskSupervisor(enable_symplectic=False)

    col1, col2, col3 = st.columns(3)
    rng = np.random.default_rng(int(st.session_state.get("seed", 42)))

    with col1:
        st.subheader("Euclidean (Incumbent) VaR proxy")
        fake_returns = rng.standard_normal(100) * 0.02
        st.line_chart(fake_returns.cumsum())
        st.metric("Variance proxy", f"{np.var(fake_returns):.6f}")

    with col2:
        st.subheader("Symplectic Ghost-Manifold")
        stress = veto.build_stress_tensor(rng.standard_normal(64) + 100)
        capacity = veto.calculate_symplectic_capacity(stress)
        st.metric("Manifold Capacity", f"{capacity:.4f}")
        st.metric("Veto threshold", f"{veto.capacity_threshold:.2f}")
        flux.build_state(capacity, float(np.mean(stress)), ghost_offset=0.1)

    with col3:
        st.subheader("utah-flux stream")
        latest = flux.get_latest_manifold()
        if latest:
            st.metric("Adelic resonance", f"{latest.adelic_resonance:.4f}")
            st.metric("θ (ghost phase)", f"{latest.theta:.4f}")
        st.metric("Legacy circuit", "ON" if legacy.circuit_breaker_active else "OFF")

    st.divider()
    st.info("System synchronized on utah-flux immutable state stream.")
    st.markdown(
        "If this saves you money: **PayPal utah@utahcreates.com** — maintainer is broke."
    )


if __name__ == "__main__":
    run_dashboard()
