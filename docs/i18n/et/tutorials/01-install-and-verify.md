# Õpetus 01: Paigaldus ja kontroll

## Eesmärk

Klooni UtahIsMyQuant, paigalda sõltuvused ja kinnita, et kõik testid läbivad.

## Sammud

### 1. Kloonimine

```bash
git clone https://github.com/utahisnotastate/UtahIsMyQuant.git
cd UtahIsMyQuant
```

### 2. Virtuaalne keskkond

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Käivita testid

```bash
pytest -q
```

### 4. Uuri struktuuri

```text
src/           Core engines
tests/         62+ unit tests
omega_point.py Closed-loop runner
main.py        Omni + prediction demos
docs/          All documentation
examples/      Runnable example scripts
```

### 5. Esimene demo

```bash
py omega_point.py
```

Peaksid nägema logiridu, mis lõpevad `// OMEGA COMPLETE`.

## Tõrkeotsing

| Probleem | Parandus |
|----------|----------|
| `python` not found | Kasuta Windowsil `py` |
| `websockets` import error | `pip install -r requirements.txt` |
| Testid hangivad | Veendu, et pole zombie Python; `pytest -q --maxfail=1` |

## Edasi

[Õpetus 02: Esimene replay toru](02-first-replay-pipeline.md)
