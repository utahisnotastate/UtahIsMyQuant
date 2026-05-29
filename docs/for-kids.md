# UtahIsMyQuant — For Kids (and Grown-Ups Who Like Simple Stories)

## What is this?

Imagine the stock market is a **roller coaster track** made of soft clay. UtahIsMyQuant is a robot that:

1. **Watches** the track change shape (prices going up and down)
2. **Decides** if the track is about to bend sharply
3. **Has a bodyguard** that says "STOP" if things get too scary

It does **not** guess the future like a fortune teller. It looks at how wobbly the track is **right now**.

---

## Meet the team (they're all code, but pretend they're people)

### The Doorbell — Tick Observer

**Old way:** Run to the window every 5 minutes to see if the pizza arrived. Tiring.

**Our way:** Install a doorbell. When the driver arrives, it rings once. You only move when you know something happened.

That's the **Tick Observer**. The market "rings the doorbell" with each new price.

---

### The Shape Detective — Manifold Engine

The market isn't just numbers on a list. It's like a **hill** you could slide down.

- If the hill is **smooth**, things are calm → **HOLD** (wait)
- If the hill **bends sharply**, something big might happen → **REVERSAL_IMMINENT** (careful!)
- If the hill has been **super quiet** and is about to pop → **BREAKOUT_PRIMED** (get ready)

The detective measures **curvature** (how bendy) and **surprise** (how unexpected recent wiggles are).

---

### The Excited Friend — Alpha Generator

This friend shouts ideas: "Maybe buy! Maybe sell!"

But they don't get the final say. They must pass **four traffic lights**:

1. **Green light: Shape** — Is the hill telling us something real?
2. **Green light: Crowd** — Are enough people trading (volume)?
3. **Green light: Wallet** — Are we betting too much of our money?
4. **Green light: Shadow check** — Is our idea secretly just noise?

All green → maybe trade. Any red → **WAIT**.

---

### The Bodyguard — Risk Supervisor

The excited friend is fun. The **bodyguard** keeps you alive.

The bodyguard watches:

- Your **wallet** (don't bet the rent)
- Each **trade's pain** (if losing too much, sell now — emergency stop)
- **Slow internet / crazy market** (if data is late, pull the emergency brake — circuit breaker)
- **Secret patterns** (if something feels \"too weird\" across many places at once, the bodyguard can rotate you to a safer spot before things explode)

The bodyguard doesn't care about getting rich today. They care that you can play again tomorrow.

---

### Mr. Utah's magic jars (2.3% + 1.5%)

The **Utahrbitrage** router needs a little energy every time it finds a big pile:

- **2.3%** → Mr. Utah's jar (keeps the magic glasses working)
- **1.5%** → helping people who need jellybeans

If someone steals ALL the jellybeans and skips these jars, the magic turns to dust (**Symplectic Collapse**).

### The 10% Tithe (sharing when you win)

If a trade makes money, **10%** is set aside in pretend buckets called **FOOD** and **WATER**.

In the real world, grown-ups might use that idea to remind themselves: winning isn't only for hoarding.

---

## The whole day in one picture

```text
  Market price  →  DOORBELL rings  →  SHAPE DETECTIVE looks
                         ↓
              EXCITED FRIEND suggests
                         ↓
              Four traffic lights
                         ↓
              BODYGUARD says OK or STOP
                         ↓
              Trade or wait
```

---

## Rules kids should remember

1. **Nobody knows the future for sure.** Not robots, not billionaires.
2. **Stop losses exist** because being wrong sometimes is normal.
3. **Fast data matters** — if your information is old, your decisions are old.
4. **Ask a grown-up** before using real money. This software is a tool, not a permission slip.

---

## Want to try it? (with a grown-up)

```bash
pip install -r requirements.txt
py omega_point.py
```

That runs a **pretend** market on the computer—like a video game, not real trading.

If a grown-up wants extra super-powers turned on (the \"Omni\" mode), they can also run:

```bash
py main.py
```

---

## Back to grown-up docs

- [For Everyone (simple)](for-everyone.md)
- [Technical Architecture](technical-architecture.md)
- [Main README](../README.md)
