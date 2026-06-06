# Pika-aloitus — UtahIsMyQuant 10 minuutissa

## Edellytykset

- Python 3.11+ (3.14 testattu)
- Git

## 1. Kloonaa ja asenna

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

## 2. Varmista

```bash
pytest -q
```

Odotettu tulos: **62 passed** (likimääräinen; tarkka lukumäärä paikallisesti).

## 3. Aja demot (ei oikeaa rahaa)

| Komento | Mitä se tekee |
|---------|----------------|
| `py omega_point.py` | Suljettu silmukka (tickit → alpha → riski) |
| `py main.py` | Omni Discovery + Utahrbitrage synkronointi |
| `py main.py --prediction-demo` | Utah Consensus Lattice AMI -demo |
| `py main.py --dashboard` | Streamlit Omni-Sieve -käyttöliittymä |

## 4. Lue seuraavaksi

| Tavoite | Dokumentti |
|---------|------------|
| Ymmärrä arkkitehtuuri | [technical-architecture.md](technical-architecture.md) |
| Kopioi-liitä-koodi | [tutorials/README.md](tutorials/README.md) |
| API-haku | [api-reference.md](api-reference.md) |
| Siirry vanhasta pinosta | [migration/README.md](migration/README.md) |

## 5. Utahin tukeminen

Jos tästä oli apua: [paying-utah.md](paying-utah.md) — sähköposti [utah@utahcreates.com](mailto:utah@utahcreates.com). Maksu-GUI suunnitteilla.

## 6. Muut kielet

Русский · Eesti · 日本語 · Suomi — erilliset sivut: [languages.md](languages.md)
