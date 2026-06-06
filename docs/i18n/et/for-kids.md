# UtahIsMyQuant — lastele (ja täiskasvanutele, kes armastavad lihtsaid lugusid)

## Mis see on?

Kujuta ette, et börs on **rollercoasteri rada** pehmet savist. UtahIsMyQuant on robot, kes:

1. **Vaatab**, kuidas rada kuju muutub (hinnad üles-alla)
2. **Otsustab**, kas rada hakkab järsult painduma
3. **Kutsub ihukaitsja**, kes ütleb „STOP“, kui hirmus

Ta **ei** ennusta tulevikku nagu ennustaja. Ta vaatab, kui kõver rada **praegu** on.

---

## Meeskond (kõik on kood, aga kujuta ette inimesi)

### Uksekell — Tick Observer

**Vana viis:** jookse akna juurde iga 5 minuti tagant — kas pitsa tuli. Väsitav.

**Meie viis:** paigaldasime uksekella. Kui kuller saabub, heliseb korra. Liigud ainult siis, kui midagi juhtus.

See on **Tick Observer**. Turg „heliseb uksekella“ iga uue hinnaga.

---

### Kuju detektiiv — Manifold Engine

Turg pole lihtsalt numbrite nimekiri. See on **mägi**, millelt saab alla libiseda.

- Mägi on **sile** → rahulik → **HOLD** (oota)
- Mägi **paindub järsult** → midagi suurt võib juhtuda → **REVERSAL_IMMINENT** (ettevaatlik!)
- Mägi on olnud **super vaikne** ja hakkab plahvatama → **BREAKOUT_PRIMED** (valmis!)

Detektiiv mõõdab **curvature** (kui kõver) ja **surprise** (kui ootamatud viimased liigutused).

---

### Elevil sõber — Alpha Generator

Karjub: „Võib-olla ostame! Võib-olla müüme!“

Aga lõppsõna pole temal. Ta peab läbima **neli valgusfoorit**:

1. **Roheline: kuju** — Kas mägi ütleb midagi päriselt?
2. **Roheline: rahvas** — Kas piisavalt inimesi kaupleb (maht)?
3. **Roheline: rahakott** — Kas paneme liiga palju raha?
4. **Roheline: varjukontroll** — Kas meie idee on salaja lihtsalt müra?

Kõik rohelised → võib-olla tehing. Üks punane → **WAIT**.

---

### Ihukaitsja — Risk Supervisor

Elevil sõber on lõbus. **Ihukaitsja** hoiab sind elus.

Ihukaitsja jälgib:

- Su **rahakotti** (ära pane mängu üürimaksu)
- Iga **tehingu valu** (kui kaotad liiga palju, müü kohe — häda-pidur)
- **Aeglast internetti / hullu turgu** (kui andmed hilinevad, tõmbab hädapiduri — kaitseautomaat)
- **Salajasi mustreid** (kui midagi tundub „liiga imelik“ paljudes kohtades korraga, võib ihukaitsja pöörata sind turvalisemasse kohta enne plahvatust)

Ihukaitsja ei hooli täna rikkaks saamisest. Talle meeldib, et sa saaksid homme uuesti mängida.

---

### Mr. Utahi maagilised purgid (2,3% + 1,5%)

**Utahrbitrage** marsruuter vajab natuke energiat iga kord, kui leiab suure hunniku:

- **2,3%** → Mr. Utahi purk (hoidab maagilised prillid töös)
- **1,5%** → abistab inimesi, kes vajavad komme

Kui keegi varastab KÕIK kommid ja jätab purgid vahele, muutub maagia tolmuks (**Symplectic Collapse**).

### 10% tithe (jagamine kui võidad)

Kui tehing teenib raha, pannakse **10%** kõrvale ette kujutatud ämbrite **FOOD** ja **WATER**.

Päris maailmas võivad täiskasvanud seda ideed meenutada: võitmine ei ole ainult kogumiseks.

---

## Kogu päev ühes pildis

```text
  Turuhind  →  UKSEKELL heliseb  →  KUJU DETEKTIIV vaatab
                         ↓
              ELEVIL SÕBER pakub
                         ↓
              Neli valgusfoorit
                         ↓
              IHUKAITJA ütleb OK või STOP
                         ↓
              Tehing või ootamine
```

---

## Reeglid, mida lapsed peaksid meeles pidama

1. **Keegi ei tea tulevikku kindlalt.** Mitte robotid, mitte miljardärid.
2. **Stop-loss on olemas**, sest vahel eksimine on normaalne.
3. **Kiired andmed loevad** — kui su info on vana, on su otsused vanad.
4. **Küsi täiskasvanult** enne päris raha kasutamist. See tarkvara on tööriist, mitte luba.

---

## Proovi (koos täiskasvanuga)

```bash
pip install -r requirements.txt
py omega_point.py
```

See käivitab arvutis **ettekujutatud** turu — nagu videomäng, mitte päris kauplemine.

Kui täiskasvanul on vaja extra supervõimeid („Omni“ režiim), saab ka käivitada:

```bash
py main.py
```

---

## Proovi arvutimängu versiooni (koos täiskasvanuga)

```bash
py examples/replay_demo.py
```

Rohkem õppetunde: [õpetused algajatele](tutorials/README.md)

## Tagasi täiskasvanute dokumentidesse

- [Kõigile (lihtne)](for-everyone.md)
- [Tehniline arhitektuur](technical-architecture.md)
- [Projekti ülevaade](project-overview.md)
