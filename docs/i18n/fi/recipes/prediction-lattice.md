# Resepti: Utah Consensus Lattice (Ennustemarkkinat)

```python
import numpy as np
from src.utah_prediction_engine import UtahConsensusLattice

lattice = UtahConsensusLattice(initial_pool_depth=50_000.0)

# Retail-sized flux
retail = np.array([50.0, 75.0, 60.0])
s_retail = lattice.execute_market_trade(retail, market_impact_factor=0.05)

# Whale-sized flux
whale = np.array([10_000.0, 2500.0, 500.0])
s_whale = lattice.execute_market_trade(whale, market_impact_factor=0.05)

print("retail delta:", s_retail.protected_delta, "ami:", lattice.ami_whale_dampening(retail, 10_000))
print("whale delta:", s_whale.protected_delta, "ami:", lattice.ami_whale_dampening(whale, 10_000))
print("protocol ledger:", lattice.yield_ledger[-1])
```
