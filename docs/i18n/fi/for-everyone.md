# UtahIsMyQuant — Kaikille (ei tarvita tohtorin tutkintoa)

## Yksi lause

**UtahIsMyQuant** on ilmainen, avoin työkalupakki, joka seuraa markkinahintoja reaaliajassa, etsii geometristä "stressiä" hintaliikkeessä, päättää kaupankäynnistä ja käyttää tiukkaa turvajärjestelmää vahinkojen rajoittamiseen, kun asiat menevät pieleen.

Se **ei** ole pikaisesti rikastumisen nappi. Se **ei** ole sijoitusneuvontaa. Se on ohjelmisto, jota voit tutkia, ajaa ja muokata — silmät auki.

---

## Mitä ongelmaa se ratkaisee?

Suuret hedge-rahastot käyttävät omaisuuksia:

- Hitaisiin dataputkiin (hintojen tarkistus ajastimella eikä välittömiä päivityksiä)
- Liian monimutkaiseen tekoälyyn, joka "sopii menneisyyteen" kauniisti ja epäonnistuu nykyhetkessä
- Riskityökaluihin, jotka saapuvat liian myöhään

UtahIsMyQuant on vastakkainen filosofia:

| Vanha tapa | UtahIsMyQuant-lähestymistapa |
|------------|------------------------------|
| Ennusta tulevaisuus historiasta | Havainnoi **nykyhetken geometriaa** |
| Kuukausia backtestausta | **Reaaliaikaiset** vakaustarkistukset |
| Yksi mustalaatikko sanoo BUY | **Useiden gatejen** täytyy olla samaa mieltä |
| Riski neljännesvuosiraporttina | Riski **bodyguardina jokaisella tickillä** |
| Gaussin mukavuusvyöhyke | **Curvature + entropy + moniasteinen resonanssi + symplektiset tarkistukset** |

---

## Neljä osaa (selkokielellä)

### 1. Tick Observer — "Ovikello"

Saa hintapäivitykset heti (WebSocket push), ei hitaalla aikataululla.

**Miksi se merkitsee:** Nopeilla markkinoilla vanhentunut data on kallista.

### 2. Manifold Engine — "Muodonlukija"

Kohtelee viimeaikaisia hintoja pintana ja mittaa:

- **Curvature** — Taipuuko markkina jyrkästi? (rejimivaihdon riski)
- **Surprise (entropy)** — Onko satunnaisuus tiivistynyt ennen liikettä?
- **Drift** — Rakentuuko kiihtyvyys?

**Miksi se merkitsee:** Et odota yhtä taikaindikaattoria — luet rakennetta.

### 3. Alpha Generator — "Päätöspöytä"

Muuttaa muotolukemat toiminnaksi: odota, osta, myy tai poistu — mutta vain **logic gatejen** jälkeen (muoto, volume, kauppariski, shadow audit).

**Miksi se merkitsee:** Vähemmän impulsiivisia kauppoja; jokaisella päätöksellä on kirjattu syy.

### 4. Risk Supervisor — "Bodyguard"

Seuraa kokonaisaltistusta, kauppakohtaista drawdownia ja järjestelmän viivettä. Voi **vetää veton** kaupoille tai **pakottaa poistumisen**. Laukaisee **circuit breakerin**, jos data on liian hidasta (epävakaat olosuhteet).

**Miksi se merkitsee:** Selviytyminen ensin. Voitot toiseksi.

---

## Kenelle tämä on?

| Olet… | Sopii? |
|-------|--------|
| Kehittäjä, joka opettelee quant-järjestelmiä | ✅ Erinomainen oppimisprojekti |
| Yksityissijoittaja koodaustaidoilla | ⚠️ Mahdollista — yhdistä oma broker, testaa paljon |
| Hedge-rahasto, joka korvaa Bloombergin | ❌ Ei suora korvike |
| Joku ilman koodaustaitoja | ⚠️ Lue ensin; kumppanuus kehittäjän kanssa |
| Lapsi | ✅ Lue [Lapsille](for-kids.md) vanhemman kanssa |

---

## Mitä se EI tee

- **Ei sisäänrakennettua brokeria** — Yhdistät oman datafeedin ja toteutuksen
- **Ei taattuja voittoja** — Markkinat satuttavat niitä, jotka uskovat takuisiin
- **Ei backtest-pakettia** — Tarkoituksella (katso [siirtymäopas](migration/from-backtest-heavy-to-realtime.md))
- **Ei vero-/oikeuscompliance-pakettia** — Oma lainkäyttöalueesi on sinun ongelmasi

---

## Aloitus (turvallinen polku)

1. **Asenna** (Windows-esimerkki):
   ```powershell
   cd UtahIsMyQuant
   py -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Aja testit** (terveystarkistus):
   ```powershell
   pytest -q
   ```

3. **Aja demo** (vale-tickit, ei oikeaa rahaa):
   ```powershell
   py omega_point.py
   ```

4. **Vasta sitten** harkitse live-dataa (`--uri wss://...`) ja paperikaupankäyntiä.

---

## Miksi vaihtaa nykyisestä?

Sinun ei tarvitse vihata nykyisiä työkalujasi nähdäksesi niiden rajat:

- Jos strategiasi näyttää hyvältä vain backtesteissä, sinulla on **tarina**, ei järjestelmä. UtahIsMyQuant näyttää tarkalleen **mikä gate** esti kaupan, jotta voit debugata todellisuutta etkä overfittaa kaavioita.
- Jos data saapuu hitaissa erissä, päätöksesi ovat jo vanhoja. Täällä ovikello (TickObserver) antaa **push-päivityksiä**, joten moottori reagoi nykyhetkeen, ei vanhentuneeseen tilannekuvaan.
- Jos riskinäkymäsi on PDF kerran viikossa, lennät sokeana päivän sisällä. Supervisor ja omni-kerros on suunniteltu sanomaan **"ei" reaaliajassa**, ei tappion jälkeen.

Jos mikään näistä ei kuulosta tutulta, pidä nykyinen pino. Jos kuulostaa, UtahIsMyQuant on pieni, luettava koodipohja, josta voit oikeasti päättellä — ja sammuttaa tarvittaessa.

---

## Sanasto (ystävällinen)

| Termi | Merkitys |
|-------|----------|
| **Tick** | Yksi hintapäivitys (symbol, price, volume, time) |
| **Manifold** | Hieno sana sille, että hintoja kohdellaan muotona, ei listana |
| **Gate** | Kyllä/ei-turvatarkistus ennen kauppaa |
| **Circuit breaker** | Hätätauko, kun olosuhteet ovat turvattomat |
| **Tithe** | 10 % positiivisesta PnL:stä FOOD/WATER-purkkeihin (symbolinen allokaatio koodissa) |
| **Shadow tensor** | Tarkistaa, heijastaako signaalisi kohinaa |

---

## Utahin tukeminen

Jos projekti auttaa oikeassa maailmassa, ota yhteyttä: [paying-utah.md](paying-utah.md).

**Sähköposti:** [utah@utahcreates.com](mailto:utah@utahcreates.com). GUI-sovellus tukemaksujen hallintaan tulee myöhemmin.

---

## Utahrbitrage (brändi laatikon sisällä)

**UtahIsMyQuant** on kloonaamasi repo. **Utahrbitrage** on moottorin nimi Omega-Point-reititykselle ja 2,3 % / 1,5 % topologisille reiteille. Lisätiedot: [utahrbitrage.md](utahrbitrage.md).

---

## Opetusohjelmat käytännön oppimiseen

- [Pika-aloitus](quickstart.md) — 10 minuuttia
- [Opetusohjelma 02: Ensimmäinen replay](tutorials/02-first-replay-pipeline.md)
- [Kaikki opetusohjelmat](tutorials/README.md)

## Seuraavat dokumentit

- **Lapset:** [for-kids.md](for-kids.md) · [04-children-beginners.md](04-children-beginners.md)
- **Tekninen:** [technical-architecture.md](technical-architecture.md)
- **Quantit:** [guides/quant-daily-workflow.md](guides/quant-daily-workflow.md)
- **Johtajat:** [guides/hedge-fund-manager.md](guides/hedge-fund-manager.md)
- **Siirtyminen rahastopinosta:** [migration/README.md](migration/README.md)
