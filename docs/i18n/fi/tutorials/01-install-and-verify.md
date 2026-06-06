# Opetusohjelma 01: Asennus ja varmistus

## Tavoite

Kloonaa UtahIsMyQuant, asenna riippuvuudet ja varmista, että kaikki testit menevät läpi.

## Vaiheet

### 1. Kloonaa

```bash
git clone https://github.com/utahisnotastate/UtahIsMyQuant.git
cd UtahIsMyQuant
```

### 2. Virtuaaliympäristö

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Aja testit

```bash
pytest -q
```

### 4. Tutustu rakenteeseen

```text
src/           Ydinmoottorit
tests/         62+ yksikkötestiä
omega_point.py Suljettu silmukka -runner
main.py        Omni + prediction -demot
docs/          Kaikki dokumentaatio
examples/      Ajettavat esimerkkiskriptit
```

### 5. Ensimmäinen demo

```bash
py omega_point.py
```

Pitäisi näkyä lokirivejä, jotka päättyvät `// OMEGA COMPLETE`.

## Vianmääritys

| Ongelma | Korjaus |
|---------|---------|
| `python` ei löydy | Käytä Windowsilla `py` |
| `websockets` import error | `pip install -r requirements.txt` |
| Testit jumissa | Varmista ettei zombi-Pythonia; `pytest -q --maxfail=1` |

## Seuraavaksi

[Opetusohjelma 02: Ensimmäinen replay-putki](02-first-replay-pipeline.md)
