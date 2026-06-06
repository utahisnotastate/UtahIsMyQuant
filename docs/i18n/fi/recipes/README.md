# Koodireseptit

Minimaaliset kopioi-liitä-pätkät. Olettaa repon juuren `PYTHONPATH`-polulla (`pytest.ini` asettaa tämän).

```python
# At top of scripts run from repo root:
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
```

Tai aja repon juuresta: `py your_script.py`

| Resepti | Kuvaus |
|---------|--------|
| [manifold.md](manifold.md) | Curvature, entropy, signaalit |
| [alpha-gates.md](alpha-gates.md) | Logic gateet, päätökset |
| [utahrbitrage.md](utahrbitrage.md) | Omega-Point-reititys |
| [prediction-lattice.md](prediction-lattice.md) | AMI ennustemarkkinat |
| [full-tick-handler.md](full-tick-handler.md) | End-to-end tick-käsittely |
