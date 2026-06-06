# Opetusohjelma 10: Streamlit-dashboard

## Tavoite

Käynnistä **Omni-Sieve** -dashboard VaR-proxyn ja symplektisen kapasiteetin rinnakkain.

## Aja

```bash
pip install streamlit
py main.py --dashboard
```

Tai:

```bash
streamlit run src/ui/omni_sieve_dashboard.py
```

## Mitä näet

- Vasen: synteettinen "incumbent" varianssiproxy
- Keskellä: symplektinen monistokapasiteetti
- Oikea: utah-flux viimeisin resonanssi

## Mukauta

Muokkaa `src/ui/omni_sieve_dashboard.py` liittääksesi live flux -virran.

## Valmis

Palaa [opetusohjelmaindeksiin](README.md) tai [täyteen dokumentaatioindeksiin](../README.md).
