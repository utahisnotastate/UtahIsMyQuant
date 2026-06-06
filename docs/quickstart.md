# Quickstart — UtahIsMyQuant in 10 Minutes

## Prerequisites

- Python 3.11+ (3.14 tested)
- Git

## 1. Clone and install

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

## 2. Verify

```bash
pytest -q
```

Expected: **62 passed** (approximate; run locally for exact count).

## 3. Run demos (no real money)

| Command | What it does |
|---------|----------------|
| `py omega_point.py` | Closed-loop replay (ticks → alpha → risk) |
| `py main.py` | Omni Discovery + Utahrbitrage sync |
| `py main.py --prediction-demo` | Utah Consensus Lattice AMI demo |
| `py main.py --dashboard` | Streamlit Omni-Sieve UI |

## 4. Read next

| Goal | Doc |
|------|-----|
| Understand architecture | [technical-architecture.md](technical-architecture.md) |
| Copy-paste code | [tutorials/README.md](tutorials/README.md) |
| API lookup | [api-reference.md](api-reference.md) |
| Migrate from legacy stack | [migration/README.md](migration/README.md) |

## 5. Paying Utah

If this helped you: [paying-utah.md](paying-utah.md) — email [utah@utahcreates.com](mailto:utah@utahcreates.com). Payment GUI app planned.

## 6. Other languages

Русский · Eesti · Suomi · 日本語 · 简体中文 — separate pages: [languages.md](languages.md)
