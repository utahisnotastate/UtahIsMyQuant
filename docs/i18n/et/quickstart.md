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
| `py main.py --dashboard` | Streamlit kasutajaliides |

## 4. Edasi lugemiseks

| Eesmärk | Dokument |
|---------|----------|
| Ülevaade lihtsas keeles | [for-everyone.md](for-everyone.md) |
| Autori toetus | [paying-utah.md](paying-utah.md) |
| Arhitektuur | [../../technical-architecture.md](../../technical-architecture.md) **(English)** |
| API | [../../api-reference.md](../../api-reference.md) **(English)** |

## 5. Navigeerimine

- [Eesti keskus](README.md)
- [Kõik keeled](../../languages.md) **(English)**
