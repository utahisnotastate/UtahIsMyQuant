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

**Vana viis:** jooksta akna juurde iga 5 minuti tagant — kas pitsa tuli.

**Meie viis:** paigaldasime uksekella. Kui kuller saabub, heliseb. Liigud ainult siis, kui midagi juhtus.

### Kuju detektiiv — Manifold Engine

Turg pole lihtsalt numbrite nimekiri. See on **mägi**, millelt saab alla libiseda.

- Mägi on **sile** → rahulik → **HOLD**
- Mägi **paindub järsult** → midagi suurt võib juhtuda → **REVERSAL_IMMINENT**
- Oli **väga vaikne**, varsti plahvatus → **BREAKOUT_PRIMED**

### Elevil sõber — Alpha Generator

Karjub: „Võib-olla ostame! Võib-olla müüme!“

Aga lõppsõna pole temal. Neli **valgusfoorit**:

1. Mäe kuju
2. Kas piisavalt inimesi kaupleb (maht)
3. Kas paneme liiga palju raha
4. Varjutest — kas see on müra

Kõik rohelised → võib-olla tehing. Üks punane → **WAIT**.

### Ihukaitsja — Risk Supervisor

Jälgib rahakotti, tehingu valu, aeglast internetti. Saab lülitada **hädapiduri**.

### Utahi purgid (2,3% + 1,5%)

**Utahrbitrage** marsruuter paneb natuke energiat Utahi ja abivajajate pankadesse. Kui varastada kõik ja purgid vahele jätta — maagia laguneb (**Symplectic Collapse**).

---

## Proovi (koos täiskasvanuga)

```bash
pip install -r requirements.txt
py examples/replay_demo.py
```

See on **arvutimäng**, mitte päris raha.

---

## Tagasi dokumentidesse

- [Kõigile](for-everyone.md)
- [Kiire algus](quickstart.md)
- [Eesti keskus](README.md)
