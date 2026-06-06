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

---

## Neli osa (lihtsas keeles)

### 1. Tick Observer — „uksekell“

Saab hinnauuendusi kohe (WebSocket), mitte graafiku järgi.

### 2. Manifold Engine — „kuju lugeja“

Vaatab hindu pinnana: **kõverus**, **entroopia (üllatus)**, **triiv**.

### 3. Alpha Generator — „otsuslaud“

Muudab näidud tegevusteks: oota, osta, müü, välju — ainult pärast **loogikaväravate** läbimist.

### 4. Risk Supervisor — „ihukaitsja“

Jälgib kogu riski, kahjumit ja andmeviivitust. Saab **keelata** tehingu või **sundväljuda**. Lülitab **kaitseautomaadi**, kui andmed on liiga aeglased.

---

## Kellele see sobib?

| Sa oled… | Sobib? |
|----------|--------|
| Arendaja, kes õpib kvant-süsteeme | ✅ Suurepärane õppeprojekt |
| Jaemüügikaupleja koodiga | ⚠️ Võimalik — oma maakler, palju teste |
| Hedge-fond Bloomberg asemel | ❌ Ei ole otse asendus |
| Ilma programmeerimiseta | ⚠️ Loe esmalt; leia arendaja |
| Laps | ✅ [Lastele](for-kids.md) koos vanemaga |

---

## Mida see EI tee

- **Pole sisseehitatud maaklerit** — ühendad oma andmevoo ja täitmise
- **Pole garanteeritud kasumit**
- **Pole backtesti komplekti** — taotluslikult
- **Pole maksu-/õiguslikku paketti** — sinu jurisdiktsioon on sinu asi

---

## Turvaline algus

```powershell
cd UtahIsMyQuant
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -q
py omega_point.py
```

Alles siis — elavad andmed (`--uri wss://...`) ja paberkauplemine.

---

## Toeta autorit

[Utah tasumine](paying-utah.md) — kirjuta [utah@utahcreates.com](mailto:utah@utahcreates.com). Maksete haldamise GUI tuleb hiljem.

---

## Edasi

- [Kiire algus](quickstart.md)
- [Lastele](for-kids.md)
- [Eesti keskus](README.md)
- Tehniline arhitektuur: [../../technical-architecture.md](../../technical-architecture.md) **(English)**
