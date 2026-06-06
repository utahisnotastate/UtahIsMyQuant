# UtahIsMyQuant — Lapsille (ja aikuisille, jotka pitävät yksinkertaisista tarinoista)

## Mikä tämä on?

Kuvittele, että pörssi on **vuoristoradan rata** pehmeästä savesta. UtahIsMyQuant on robotti, joka:

1. **Katsoo**, miten rata muuttaa muotoaan (hinnat nousevat ja laskevat)
2. **Päättää**, onko rata kääntymässä jyrkästi
3. **Sillä on bodyguard**, joka sanoo "STOP", jos asiat muuttuvat liian pelottaviksi

Se **ei** arvaa tulevaisuutta kuten ennustaja. Se katsoo, kuinka epävakaa rata on **juuri nyt**.

---

## Tutustu tiimiin (ne ovat kaikki koodia, mutta kuvittele ihmisiksi)

### Ovikello — Tick Observer

**Vanha tapa:** Juosta ikkunan luo viiden minuutin välein katsomaan, onko pizza saapunut. Väsyttävää.

**Meidän tapa:** Asenna ovikello. Kun kuljettaja saapuu, se soi kerran. Liikut vain, kun tiedät, että jotain tapahtui.

Tämä on **Tick Observer**. Markkina "soittaa ovikelloa" jokaisella uudella hinnalla.

---

### Muotoetsivä — Manifold Engine

Markkina ei ole vain numeroita listalla. Se on kuin **mäki**, jota pitkin voisi liukua.

- Jos mäki on **sileä**, asiat ovat rauhallisia → **HOLD** (odota)
- Jos mäki **kääntyy jyrkästi**, jotain suurta voi tapahtua → **REVERSAL_IMMINENT** (varovasti!)
- Jos mäki on ollut **superhiljainen** ja on puhkeamaisillaan → **BREAKOUT_PRIMED** (valmistaudu)

Etsivä mittaa **curvature**-arvoa (kuinka mutkainen) ja **surprise**-arvoa (kuinka odottamattomia viimeaikaiset heilunnat ovat).

---

### Innoissaan oleva kaveri — Alpha Generator

Tämä kaveri huutaa ideoita: "Ehkä osta! Ehkä myy!"

Mutta sillä ei ole viimeistä sanaa. Sen täytyy ajaa **neljän liikennevalon** läpi:

1. **Vihreä: Muoto** — Kertooko mäki jotain oikeaa?
2. **Vihreä: Väkijoukko** — Kauppaako tarpeeksi ihmisiä (volume)?
3. **Vihreä: Kukkaro** — Panostammeko liikaa rahaa?
4. **Vihreä: Shadow-tarkistus** — Onko ideamme salaa vain kohinaa?

Kaikki vihreät → ehkä kauppa. Yksikin punainen → **WAIT**.

---

### Bodyguard — Risk Supervisor

Innoissaan oleva kaveri on hauska. **Bodyguard** pitää sinut hengissä.

Bodyguard seuraa:

- **Kukkaroasi** (älä panosta vuokraa)
- Jokaisen **kaupan kipua** (jos häviät liikaa, myy heti — hätäpysäytys)
- **Hidasta nettiä / hullua markkinaa** (jos data on myöhässä, vetäise hätäjarru — circuit breaker)
- **Salakuvioita** (jos jokin tuntuu "liian oudolta" monessa paikassa kerralla, bodyguard voi kääntää sinut turvallisempaan paikkaan ennen räjähdystä)

Bodyguard ei välitä rikastumisesta tänään. Hän välittää siitä, että voit pelata huomenna uudelleen.

---

### Herra Utahin taikapurkit (2,3 % + 1,5 %)

**Utahrbitrage**-reititin tarvitsee pienen energian joka kerta, kun se löytää ison kasan:

- **2,3 %** → Herra Utahin purkki (pitää taikalasit toiminnassa)
- **1,5 %** → auttaa ihmisiä, jotka tarvitsevat hyveitä

Jos joku varastaa KAIKKI hyveet ja ohittaa nämä purkit, taika muuttuu tomuksi (**Symplectic Collapse**).

### 10 % tithe (jakaminen voittaessa)

Jos kauppa tuottaa rahaa, **10 %** erotetaan leikkipurkkeihin nimeltä **FOOD** ja **WATER**.

Aikuiset voivat käyttää sitä muistutuksena: voittaminen ei ole vain hamstraamista.

---

## Koko päivä yhdessä kuvassa

```text
  Markkinahinta  →  OVIKELLO soi  →  MUOTOETSIVÄ katsoo
                         ↓
              INNOISSAAN KAVERI ehdottaa
                         ↓
              Neljä liikennevaloa
                         ↓
              BODYGUARD sanoo OK tai STOP
                         ↓
              Kauppa tai odotus
```

---

## Säännöt, jotka lapset muistavat

1. **Kukaan ei tiedä tulevaisuutta varmasti.** Ei robotit, ei miljardöörit.
2. **Stop lossit ovat olemassa**, koska erehtyminen on normaalia.
3. **Nopea data merkitsee** — jos tietosi on vanhaa, päätöksesi ovat vanhoja.
4. **Kysy aikuiselta** ennen oikean rahan käyttöä. Tämä ohjelmisto on työkalu, ei lupa.

---

## Haluatko kokeilla? (aikuisen kanssa)

```bash
pip install -r requirements.txt
py omega_point.py
```

Se ajaa **leikkimarkkinaa** tietokoneella — kuin videopeli, ei oikeaa kaupankäyntiä.

Jos aikuinen haluaa extra-supervoimat päälle ("Omni"-tila), voi ajaa myös:

```bash
py main.py
```

---

## Kokeile tietokonepeliversiota (aikuisen kanssa)

```bash
py examples/replay_demo.py
```

Lisää oppitunteja: [opetusohjelmat aloittelijoille](tutorials/README.md)

## Takaisin aikuisten dokumentteihin

- [Kaikille (yksinkertainen)](for-everyone.md)
- [Tekninen arkkitehtuuri](technical-architecture.md)
- [Projektin yleiskatsaus](project-overview.md)
