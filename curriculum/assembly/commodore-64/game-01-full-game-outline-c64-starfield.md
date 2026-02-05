# Full Game Outline: C64 Starfield (128 Units)

**Game:** Starfield (Game 1)
**Units:** 128 (8 phases × 16 units)
**Target Quality:** Commercial-grade single-screen shooter (1985-86 era)
**Comparable To:** Galaga, Phoenix, Gyruss, Arcadia

---

## Design Philosophy

- **One concept per unit** — never overwhelming
- **Always playable** — from Unit 2 onwards, you can play what you've built
- **Debugging inline** — every unit includes "if it doesn't work"
- **Sound throughout** — not bolted on at the end
- **Commercial quality by Unit 128** — not a tutorial exercise, a real game

---

## Phase 1: Minimal Playable Game (Units 1-16)

**Goal:** Complete game loop — shoot enemies, score points, die, restart.

| Unit | You Add | Result |
|------|---------|--------|
| 1 | Ship sprite on screen | See your ship |
| 2 | Joystick moves ship | **Control something** |
| 3 | Fire button shoots | Bullet flies up |
| 4 | Laser sound effect | Satisfying "pew" |
| 5 | One enemy appears | Target exists |
| 6 | Bullet hits enemy | **It dies!** |
| 7 | Explosion sound | Feedback |
| 8 | Score display | See your points |
| 9 | Enemies spawn continuously | Challenge |
| 10 | Enemy touches ship | You can die |
| 11 | Game over screen | End state |
| 12 | Press fire to restart | **Complete loop** |
| 13 | Title screen | Feels real |
| 14 | Three lives | Forgiveness |
| 15 | Life lost flash/sound | Feedback |
| 16 | Integration + edge cases | Solid foundation |

**End of Phase 1:** Playable shooter. Simple, but complete.

---

## Phase 2: Enemy Variety (Units 17-32)

**Goal:** Multiple enemy types with distinct behaviours.

| Unit | You Add | Result |
|------|---------|--------|
| 17 | Fast enemy (dives straight down) | Variety begins |
| 18 | Slow enemy (drifts down) | Pacing contrast |
| 19 | Zigzag enemy (weaves as it falls) | Movement patterns |
| 20 | Different sprites for each type | Visual distinction |
| 21 | Different colours per type | Instant recognition |
| 22 | Different point values | Risk/reward |
| 23 | Wave system (10 enemies = wave) | Structure |
| 24 | Wave complete bonus | Incentive to clear |
| 25 | Faster spawning each wave | Difficulty curve |
| 26 | Wave number display | Progress visible |
| 27 | Mix of enemy types per wave | Tactical variety |
| 28 | Later waves = harder enemy mix | Escalation |
| 29 | Enemy spawn sound | Audio feedback |
| 30 | Wave start fanfare | Punctuation |
| 31 | Brief pause between waves | Breathing room |
| 32 | Integration + balance tuning | Feels fair |

**End of Phase 2:** Varied, escalating challenge. Waves feel distinct.

---

## Phase 3: Player Abilities (Units 33-48)

**Goal:** Power-ups and upgrades make the player stronger.

| Unit | You Add | Result |
|------|---------|--------|
| 33 | Power-up item drops from enemies | Collectibles exist |
| 34 | Collect power-up = effect | System works |
| 35 | Speed boost power-up | Move faster |
| 36 | Rapid fire power-up | Shoot faster |
| 37 | Power-up collect sound | Satisfying pickup |
| 38 | Power-up visible on HUD | Know what you have |
| 39 | Power-ups are temporary (timer) | Strategic decisions |
| 40 | Timer display or flashing warning | Know when it ends |
| 41 | Double shot power-up (two bullets) | Firepower |
| 42 | Spread shot (three directions) | Screen coverage |
| 43 | Shield power-up (one free hit) | Defensive option |
| 44 | Shield visual (sprite overlay) | See protection |
| 45 | Shield break sound/visual | Dramatic feedback |
| 46 | Power-up spawn frequency tuning | Balance |
| 47 | Power-ups don't spawn on Wave 1 | Earned progression |
| 48 | Integration + balance | Rewarding loop |

**End of Phase 3:** Player has agency. Choices matter. Getting power-ups feels great.

---

## Phase 4: Enemies Fight Back (Units 49-64)

**Goal:** Enemies shoot, creating dodge gameplay.

| Unit | You Add | Result |
|------|---------|--------|
| 49 | Enemy bullet (one at a time) | Danger from above |
| 50 | Enemy bullet sprite | Visible threat |
| 51 | Enemy bullet hits player | Real danger |
| 52 | Enemy fire sound | Audio warning |
| 53 | Random enemy fires | Unpredictable |
| 54 | Firing enemy type (dedicated shooter) | Role variety |
| 55 | Shooter enemy visual distinction | See the threat |
| 56 | Shooter enemy worth more points | Risk/reward |
| 57 | Multiple enemy bullets | Intensity |
| 58 | Bullet speed varies by wave | Escalation |
| 59 | Aimed shots (towards player) | Smart enemies |
| 60 | Aimed vs random mix | Variety |
| 61 | Player bullet destroys enemy bullet | Skill option |
| 62 | Player death = bullets cleared | Fair restart |
| 63 | Bullet density tuning | Not overwhelming |
| 64 | Integration + difficulty balance | Challenging but fair |

**End of Phase 4:** Proper two-way combat. Dodging matters. Tension exists.

---

## Phase 5: Visual Polish (Units 65-80)

**Goal:** Game looks commercially polished.

| Unit | You Add | Result |
|------|---------|--------|
| 65 | Starfield background (characters) | Depth |
| 66 | Multiple star speeds (parallax) | Motion |
| 67 | Star colours (dim = far, bright = near) | Depth cues |
| 68 | Explosion animation (4 frames) | Impact |
| 69 | Explosion sprite sequence | Visual drama |
| 70 | Player death explosion (bigger) | Stakes |
| 71 | Screen flash on player death | Emphasis |
| 72 | Screen shake on explosions | Game feel |
| 73 | Enemy spawn animation (fade in) | Polish |
| 74 | Multicolour sprites (ship detail) | Quality |
| 75 | Multicolour enemies | Visual upgrade |
| 76 | Colour cycling on title | Attract mode |
| 77 | Border colour effects | C64 flair |
| 78 | Score colours (white, yellow on high) | Feedback |
| 79 | Smooth sprite movement (subpixel) | Professional feel |
| 80 | Integration + visual consistency | Cohesive look |

**End of Phase 5:** Looks like a real game. Screenshots would sell it.

---

## Phase 6: Audio Polish (Units 81-96)

**Goal:** Full SID soundtrack and rich sound design.

| Unit | You Add | Result |
|------|---------|--------|
| 81 | Title screen music (simple loop) | Atmosphere |
| 82 | Music uses two SID voices | Richer sound |
| 83 | Music stops when game starts | Clean transition |
| 84 | Game over jingle | Punctuation |
| 85 | High score jingle (new record) | Celebration |
| 86 | Wave complete jingle | Achievement |
| 87 | Varied explosion sounds (pitch) | Richness |
| 88 | Low health warning beep | Tension |
| 89 | Power-up collected jingles (per type) | Distinction |
| 90 | Boss warning siren (prep for Phase 7) | Drama |
| 91 | Enemy dive sound (fast enemy) | Audio cues |
| 92 | Shield active hum | Status feedback |
| 93 | Volume balance (music vs SFX) | Professional mix |
| 94 | Filter sweeps on explosions | SID character |
| 95 | Sound doesn't cut out (voice allocation) | Robust |
| 96 | Integration + audio balance | Sounds great |

**End of Phase 6:** Audio matches visuals in quality. SID sings.

---

## Phase 7: Boss Battles (Units 97-112)

**Goal:** Epic boss fights punctuate the experience.

| Unit | You Add | Result |
|------|---------|--------|
| 97 | Boss appears every 5 waves | Structure |
| 98 | Boss sprite (large, multicolour) | Impressive |
| 99 | Boss movement pattern | Behaviour |
| 100 | Boss health bar | Visible progress |
| 101 | Boss takes multiple hits | Endurance fight |
| 102 | Boss hit flash | Feedback |
| 103 | Boss shoots (spread pattern) | Danger |
| 104 | Boss phases (changes at 50% health) | Escalation |
| 105 | Phase 2 = faster/angrier | Drama |
| 106 | Boss death explosion (big!) | Payoff |
| 107 | Boss defeat bonus points | Reward |
| 108 | Boss defeat fanfare | Celebration |
| 109 | Second boss type (wave 10) | Variety |
| 110 | Second boss different pattern | Fresh challenge |
| 111 | Boss warning before spawn | Preparation |
| 112 | Integration + boss balance | Fair fights |

**End of Phase 7:** Boss fights are highlights. Players remember them.

---

## Phase 8: Final Polish (Units 113-128)

**Goal:** Commercial release quality. Complete package.

| Unit | You Add | Result |
|------|---------|--------|
| 113 | High score table (top 5) | Competition |
| 114 | Initials entry for high score | Ownership |
| 115 | High scores shown on title | Bragging |
| 116 | Attract mode (demo plays itself) | Shop display |
| 117 | Two-player alternating mode | Multiplayer |
| 118 | Two-player score comparison | Competition |
| 119 | Difficulty select (easy/normal/hard) | Accessibility |
| 120 | Difficulty affects spawn rate + bullets | Real difference |
| 121 | Extra life at 10,000 points | Reward skill |
| 122 | Extra life sound/visual | Celebration |
| 123 | Game speed tuning (PAL/NTSC) | Platform correct |
| 124 | Continue option (Wave restart) | Forgiveness |
| 125 | Ending screen (after Wave 30?) | Completion |
| 126 | Credits screen | Professional |
| 127 | Final balance + bug fixes | Release ready |
| 128 | **Complete game** | Ship it! |

**End of Phase 8:** A game you could put on tape and sell in 1985.

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 8 (Unit 128) |
|--------|-------------------|---------------------|
| Enemies | One type, fall down | 4+ types, patterns, aimed shots |
| Player | Move + shoot | Power-ups, shield, spread shot |
| Combat | One-way | Two-way, bullet hell lite |
| Bosses | None | Two boss types, phases |
| Visuals | Basic sprites | Multicolour, parallax, explosions |
| Audio | Pew + boom | Full music, varied SFX, filter effects |
| Modes | Single play | Two-player, difficulty select |
| Polish | Functional | Attract mode, high score table, initials |

---

## Debugging Throughout

Every unit includes inline debugging. Examples:

**Unit 2 (joystick):**
> If ship doesn't move: Check `$dc00` (joystick 2) not `$dc01`. Check bits are inverted (0 = pressed).

**Unit 6 (collision):**
> If bullets pass through: Check distance calculation. Common error: comparing X to Y by mistake.

**Unit 74 (multicolour sprites):**
> If colours wrong: Multicolour uses `$d025`/`$d026` for shared colours. Check `$d01c` bit set for that sprite.

**Unit 101 (boss health):**
> If boss dies instantly: Check health is decremented, not set to zero. Check hit detection isn't firing multiple times per frame.

No separate debugging units. Every unit teaches what can break and how to fix it.

---

## Time Investment

128 units × 60-90 minutes = 128-192 hours

At 1 hour/day: ~4-6 months
At 2 hours/day: ~2-3 months
At weekends only (4 hours): ~8-12 months

This is a serious undertaking that produces a serious game.

---

## What Makes It Commercial Quality

By Unit 128, the game has:

1. **Depth** — Multiple enemy types, boss fights, power-ups
2. **Polish** — Smooth animation, parallax, explosions
3. **Audio** — Music, varied SFX, SID character
4. **Replayability** — High scores, difficulty settings, two-player
5. **Presentation** — Title, attract mode, credits
6. **Balance** — Tuned difficulty curve, fair challenge

This isn't "baby's first shooter." It's a real game that happens to teach you everything about C64 development along the way.

---

**Version:** 1.0
**Last Updated:** 2026-01-17
