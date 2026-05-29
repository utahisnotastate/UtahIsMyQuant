# Tutorial 01: Install and Verify

## Goal

Clone UtahIsMyQuant, install dependencies, and confirm all tests pass.

## Steps

### 1. Clone

```bash
git clone https://github.com/utahisnotastate/UtahIsMyQuant.git
cd UtahIsMyQuant
```

### 2. Virtual environment

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run tests

```bash
pytest -q
```

### 4. Explore layout

```text
src/           Core engines
tests/         62+ unit tests
omega_point.py Closed-loop runner
main.py        Omni + prediction demos
docs/          All documentation
examples/      Runnable example scripts
```

### 5. First demo

```bash
py omega_point.py
```

You should see log lines ending with `// OMEGA COMPLETE`.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `python` not found | Use `py` on Windows |
| `websockets` import error | `pip install -r requirements.txt` |
| Tests hang | Ensure no zombie Python; `pytest -q --maxfail=1` |

## Next

[Tutorial 02: First replay pipeline](02-first-replay-pipeline.md)
