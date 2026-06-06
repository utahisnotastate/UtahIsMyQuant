# Kiire algus — UtahIsMyQuant 10 minutiga

## Eeldused

- Python 3.11+ (testitud 3.14-ga)
- Git

## 1. Kloonimine ja paigaldus

```powershell
git clone https://github.com/utahisnotastate/UtahIsMyQuant.git
cd UtahIsMyQuant
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Kontroll

```bash
pytest -q
```

Oodatav: **62 passed** (täpne arv kohalikult).

## 3. Demod (ilma päris rahata)

| Käsk | Mida teeb |
|------|-----------|
| `py omega_point.py` | Suletud tsükkel: tikid → alfa → risk |
| `py main.py` | Omni Discovery + Utahrbitrage |
| `py main.py --prediction-demo` | Utah Consensus Lattice (AMI) |
| `py main.py --dashboard` | Streamlit Omni-Sieve kasutajaliides |

## 4. Edasi lugemiseks

| Eesmärk | Dokument |
|---------|----------|
| Arhitektuuri mõistmine | [technical-architecture.md](technical-architecture.md) |
| Kopeeritav kood | [tutorials/README.md](tutorials/README.md) |
| API otsing | [api-reference.md](api-reference.md) |
| Migreerimine pärandvirnast | [migration/README.md](migration/README.md) |

## 5. Utah tasumine

Kui see aitas: [paying-utah.md](paying-utah.md) — kirjuta [utah@utahcreates.com](mailto:utah@utahcreates.com). Maksete GUI rakendus on plaanis.

## 6. Teised keeled

English · Русский · Suomi · 日本語 — eraldi lehed: [languages.md](languages.md)
