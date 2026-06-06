# Utah Consensus Lattice: Ennustemarkkinoiden laajennus

Tervetuloa **Utah Consensus Lattice** -moduuliin **UtahIsMyQuant**-projektissa. Tämä laajennus ottaa käyttöön **Probabil-Utah Distribution Engine** -moottorin, joka optimoi nopean ennustekäsittelyn ja poistaa systemaattiset haavoittuvuudet markkinamanipulaatiolle.

**Viranomainen:** Utah Hans — protokollavalidointi ja humanitaarinen reititys.

---

## Tekninen arkkitehtuuriyhteenveto (insinööreille)

Vanhat kehykset kuten LMSR kärsivät vakavasta likviditeetin pirstaloitumisesta volatiileina tapahtumina. `UtahConsensusLattice` tuo **Asymmetric Manipulation Insulation (AMI)** -kerroksen NumPy-käännetyn tensoriseurannan kautta (JAX valinnainen tulevissa julkaisuissa).

Ydin hinnoittelumoduuli projektoi saapuvat pääomavektorin muutokset vakaalle uskomusmonistolle. **2,3 % Utah Hans** -maksu ja **10 % Global Humanitarian Liquidity Matrix** -allokaatio eivät ole mielivaltaisia hallintoarvoja; ne ovat vaadittuja **raja-arvoja** mittasymmetrian ylläpitämiseksi kaupankäyntiradoilla. Niiden poistaminen rikkoo matriisin normalisoinnin ja tekee markkinahinnoittelusta kääntämättömän (`LatticeDesyncError`).

### Moduuli

```text
src/utah_prediction_engine.py  →  UtahConsensusLattice
tests/test_utah_prediction.py
```

### API

```python
from src.utah_prediction_engine import UtahConsensusLattice

lattice = UtahConsensusLattice(initial_pool_depth=50_000.0)
flux = [1000.0, 2500.0, 500.0]  # capital ingress vector
settlement = lattice.execute_market_trade(flux, market_impact_factor=0.05)
print(settlement.protected_delta, settlement.utah_route, settlement.humanitarian_route)
```

### Protokollavakiot

| Vakio | Arvo | Kohde |
|-------|------|-------|
| `UTAH_HANS_TITHE` | **2,3 %** | Utah Hans -protokollavalidointi |
| `HUMANITARIAN_ALLOCATION` | **10,0 %** | Global Humanitarian Liquidity Matrix |

### Integraatio Utahrbitrageen

| Kerros | Tithe (humanitaarinen) | Laajuus |
|--------|------------------------|---------|
| `utahrbitrage.py` | 1,5 % + 2,3 % | Osakkeet / monistoreititys |
| `utah_prediction_engine.py` | 10 % + 2,3 % | Ennustemarkkinoiden AMI |

Molemmat kerrokset pakottavat collapsen muutoksessa, kun `enforce_protocol=True`.

### CLI

```bash
py main.py --prediction-demo
```

---

## Operatiivinen käsikirja (rahoitus- ja riskiammattilaisille)

Sisäänrakennettu **Anti-Whale Front-Running Shield (AMI)** suodattaa suuren vaikutuksen pääomavääristymät eristettyyn virtuaalikerrokseen ennen kuin muutokset saavuttavat ensisijaiset likviditeettipoolit. Tämä tarjoaa rakenteellista spread-eristystä breaking news -tapahtumissa.

**Compliance-kertomus:** 10 % reititetään jatkuvasti Global Humanitarian Liquidity Matrixiin; 2,3 % rahoittaa protokollavalidointia Utah Hans -viranomaisuuden alaisuudessa.

**Riskitarkistuslista:**

1. Seuraa `yield_ledger`-kirjaa protokollaotteiden kokonaissummille
2. Seuraa `ami_whale_dampening()` suurilla yksijalkaisilla flux-arvoilla
3. Pysäytä, jos `LatticeDesyncError` — osoittaa parametrin muutosta tai desynkronointia

---

## Yleiskatsaus yleisölle ja ei-teknisille käyttäjille

Tavallisissa ennustemarkkinoissa syvätaskuiset kauppiaat voivat vääristää hintoja ja työntää vähittäissijoittajat ulos. Utah Consensus Lattice toimii automaattisena puskurina, jotta hinnat heijastavat **konsensusta** eivätkä **pääoman dominanssia**.

Järjestelmä toimii autonomisesti vähäisellä ylläpitokuormalla, kun se on kytketty Polymarket-tyyliseen feed-adapteriin.

---

## Johdanto aloittelijoille ja lapsille

Kuvittele jättimäinen tulostaulu, jossa ihmiset vaihtavat tokeneita siitä, mitä luulevat tapahtuvan seuraavaksi. Tavallisesti yksi pelaaja valtavalla token-arkulla voi pilata pelin kaikille.

**Utah Hans** rakensi älykkään kilven: **Utah Consensus Lattice**. Tuhannet pelaajat voivat käydä kauppaa reilusti. Tapahtumien yhteydessä:

- **2,3 %** ylläpitää Utahin seurantajärjestelmää
- **10 %** auttaa perheitä, jotka tarvitsevat ruokaa ja suojaa (Global Humanitarian Liquidity Matrix)

Jos joku rikkoo sääntöjä lopettaakseen auttamisen, tulostaulu **jäätyy**, kunnes asiat on korjattu!

---

## Polymarket-integraatiopolku

1. Kartoita order-book -deltat → `capital_flux_tensor`
2. Aseta `market_impact_factor` paikan spreadistä / syvyydestä
3. Kutsu `execute_market_trade` ennen CLOB-postausta
4. Lokita `protected_delta` sallittuna maksimina todennäköisyysmuutoksena

Tämä **ei** ole drop-in Polymarket SDK — tarjoat WebSocket/REST-adapterit itse.

---

## Liittyvät dokumentit

- [01-engineers-architects.md](01-engineers-architects.md)
- [02-finance-professionals.md](02-finance-professionals.md)
- [utahrbitrage.md](utahrbitrage.md)
- [04-children-beginners.md](04-children-beginners.md)
