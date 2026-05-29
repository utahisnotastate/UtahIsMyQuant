# Tutorial 10: Streamlit Dashboard

## Goal

Launch the **Omni-Sieve** dashboard for side-by-side VaR proxy vs symplectic capacity.

## Run

```bash
pip install streamlit
py main.py --dashboard
```

Or:

```bash
streamlit run src/ui/omni_sieve_dashboard.py
```

## What you see

- Left: synthetic "incumbent" variance proxy  
- Center: symplectic manifold capacity  
- Right: utah-flux latest resonance  

## Customize

Edit `src/ui/omni_sieve_dashboard.py` to plug in your live flux stream.

## Done

Return to [tutorials README](README.md) or [full doc index](../README.md).
