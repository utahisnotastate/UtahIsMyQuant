# UtahIsMyQuant — kõigile (ilma doktorikraadita)

## Ühe lausega

**UtahIsMyQuant** on tasuta avatud tööriistakomplekt: jälgib reaalajas turuhindu, otsib geomeetrilist „pinget“ hinnaliikumises, otsustab kas kaubelda, ja kasutab ranget turvasüsteemi kahju piiramiseks.

See **ei ole** „rikastu kiiresti“ nupp. See **ei ole** finantsnõuanne. See on tarkvara, mida saad uurida, käivitada ja kohandada — silmad lahti.

---

## Millist probleemi see lahendab?

Suured hedge-fondid kulutavad miljoneid:

- Aeglasele andmevoogule (hindade kontrollimine taimeri järgi, mitte kohe)
- Ülekeerukale tehisintellektile, mis sobib suurepäraselt minevikku, aga murdub olevikus
- Riskitööriistadele, mis jõuavad liiga hilja

UtahIsMyQuant filosoofia on vastupidine:

| Vana harjumus | UtahIsMyQuant lähenemine |
|---------------|--------------------------|
| Ennusta tulevikku ajaloost | Jälgi **olevikku geomeetriat** |
| Kuudepikkused backtestid | **Reaalajas** stabiilsuskontrollid |
| Üks must kast ütleb BUY | **Mitu väravat** peavad nõustuma |
| Risk kvartaliaruandena | Risk **ihukaitsjana igal tikil** |
| Gaussi mugavustsoon | **Kõverus + entroopia + mitmemastaabi resonants + symplectic kontrollid** |

---

## Neli osa (lihtsas keeles)

### 1. Tick Observer — „uksekell“

Saab hinnauuendusi kohe (WebSocket push), mitte aeglasel graafikul.

**Miks see oluline on:** Kiiretes turgudes on aegunud andmed kallid.

### 2. Manifold Engine — „kuju lugeja“

Käsitleb hiljutisi hindu pinnana ja mõõdab:

- **Curvature** — Kas turg paindub järsult? (režiimimuutuse risk)
- **Surprise (entropy)** — Kas juhuslikkus on enne liikumist kokku varisenud?
- **Drift** — Kas kiirendus koguneb?

**Miks see oluline on:** Sa ei oota üht maagilist indikaatorit — sa loed struktuuri.

### 3. Alpha Generator — „otsuslaud“

Muudab kuju näidud tegevusteks: oota, osta, müü, välju — ainult pärast **loogikaväravate** läbimist (kuju, maht, tehingu risk, varjuaudit).

**Miks see oluline on:** Vähem impulsiivseid tehinguid; igal otsusel on kirjalik põhjus.

### 4. Risk Supervisor — „ihukaitsja“

Jälgib kogu riski, tehingu kahjumit ja süsteemi latentsust. Saab **keelata** tehingu või **sundväljuda**. Lülitab **kaitseautomaadi**, kui andmed on liiga aeglased (volatiilsed tingimused).

**Miks see oluline on:** Esmalt ellujäämine. Siis kasum.

---

## Kellele see sobib?

| Sa oled… | Sobib? |
|----------|--------|
| Arendaja, kes õpib kvant-süsteeme | ✅ Suurepärane õppeprojekt |
| Jaemüügikaupleja koodiga | ⚠️ Võimalik — oma maakler, palju teste |
| Hedge-fond Bloomberg asemel | ❌ Ei ole otse asendus |
| Ilma programmeerimiseta | ⚠️ Loe esmalt; leia arendaja |
| Laps | ✅ Loe [Lastele](for-kids.md) koos vanemaga |

---

## Mida see EI tee

- **Pole sisseehitatud maaklerit** — ühendad oma andmevoo ja täitmise
- **Pole garanteeritud kasumit** — turud teevad haiget neile, kes usuvad garantiisse
- **Pole backtesti komplekti** — taotluslikult (vaata [migreerimisjuhendit](migration/from-backtest-heavy-to-realtime.md))
- **Pole maksu-/õiguslikku paketti** — sinu jurisdiktsioon on sinu asi

---

## Turvaline algus

1. **Paigaldus** (Windowsi näide):
   ```powershell
   cd UtahIsMyQuant
   py -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Testid** (sanity check):
   ```powershell
   pytest -q
   ```

3. **Demo** (võlts tikid, mitte päris raha):
   ```powershell
   py omega_point.py
   ```

4. **Alles siis** kaalu elavaid andmeid (`--uri wss://...`) ja paberkauplemist.

---

## Miks vahetada praeguse vastu

Sa ei pea vihkama oma praeguseid tööriistu, et näha nende piire:

- Kui strateegia näeb hea välja ainult backtestides, mitte elus, on sul **lugu**, mitte süsteem. UtahIsMyQuant näitab täpselt **milline värav** tehingu blokeeris, et saaksid debugida reaalsust, mitte ülesobitada graafikuid.
- Kui andmed saabuvad aeglastes partiides, on su otsused juba vanad. Siin annab uksekell (TickObserver) **push-põhised uuendused**, et mootor reageeriks olevikule, mitte aegunud hetktõmmisele.
- Kui su riskivaade on PDF kord nädalas, lennad päeva jooksul pimeduses. Supervisor ja omni kiht on loodud ütlema **„ei“ reaalajas**, mitte pärast kaotust.

Kui see kõik tundub võõras, hoia oma virn. Kui mitte, on UtahIsMyQuant väike, loetav koodibaas, millest saad aru saada — ja vajadusel välja lülitada.

---

## Sõnastik (sõbralik)

| Termin | Tähendus |
|--------|----------|
| **Tick** | Üks hinnauuendus (sümbol, hind, maht, aeg) |
| **Manifold** | Kõnekas sõna: „käsitle hindu kujuna, mitte nimekirjana“ |
| **Gate** | Jah/ei turvakontroll enne kauplemist |
| **Circuit breaker** | Häda-paus ohtlike tingimuste korral |
| **Tithe** | 10% positiivsest PnL-st FOOD/WATER ämbritele (sümboolne jaotus koodis) |
| **Shadow tensor** | Kontrollib, kas signaal peegeldab müra |

---

## Utah tasumine

Kui see projekt aitab sind päris maailmas, võta ühendust: [paying-utah.md](paying-utah.md).

**E-post:** [utah@utahcreates.com](mailto:utah@utahcreates.com). GUI rakendus toetuste haldamiseks tuleb hiljem.

---

## Utahrbitrage (bränd kastis sees)

**UtahIsMyQuant** on hoidla, mida kloonid. **Utahrbitrage** on mootori nimi Omega-Point marsruutimisele ja 2,3% / 1,5% topoloogilistele marsruutidele. Üksikasjad: [utahrbitrage.md](utahrbitrage.md).

---

## Õpetused praktiliseks õppimiseks

- [Kiire algus](quickstart.md) — 10 minutit
- [Õpetus 02: Esimene replay](tutorials/02-first-replay-pipeline.md)
- [Kõik õpetused](tutorials/README.md)

## Järgmised dokumendid

- **Lapsed:** [for-kids.md](for-kids.md) · [04-children-beginners.md](04-children-beginners.md)
- **Tehniline:** [technical-architecture.md](technical-architecture.md)
- **Kvantid:** [guides/quant-daily-workflow.md](guides/quant-daily-workflow.md)
- **Juhid:** [guides/hedge-fund-manager.md](guides/hedge-fund-manager.md)
- **Migreerimine fondi virnast:** [migration/README.md](migration/README.md)
