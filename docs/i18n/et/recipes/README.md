# Koodiretseptid

Minimaalsed kopeeri-kleebi lõigud. Eeldab repo juur `PYTHONPATH`-il (`pytest.ini` seab selle).

```python
# At top of scripts run from repo root:
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
```

Või käivita repo juurest: `py your_script.py`

| Retsept | Kirjeldus |
|---------|-----------|
| [manifold.md](manifold.md) | Curvature, entropy, signaalid |
| [alpha-gates.md](alpha-gates.md) | Logic gates, otsused |
| [utahrbitrage.md](utahrbitrage.md) | Omega-Point marsruutimine |
| [prediction-lattice.md](prediction-lattice.md) | AMI ennustusturud |
| [full-tick-handler.md](full-tick-handler.md) | Otsast-lõpuni tik töötlemine |
