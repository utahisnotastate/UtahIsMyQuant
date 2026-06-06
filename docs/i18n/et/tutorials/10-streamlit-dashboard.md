# Õpetus 10: Streamlit armatuurlaud

## Eesmärk

Käivita **Omni-Sieve** armatuurlaud VaR proksi vs symplectic võimsuse kõrvuti vaatamiseks.

## Käivita

```bash
pip install streamlit
py main.py --dashboard
```

Või:

```bash
streamlit run src/ui/omni_sieve_dashboard.py
```

## Mida näed

- Vasakul: sünteetiline „incumbent“ variantsi proksi
- Keskel: symplectic manifold võimsus
- Paremal: utah-flux viimane resonants

## Kohanda

Muuda `src/ui/omni_sieve_dashboard.py`, et ühendada elav flux voog.

## Valmis

Naase [õpetuste README](README.md) juurde või [täisindeks](../README.md).
