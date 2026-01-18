# Full Game Outline: ZX Spectrum Skyfire (128 Units)

**Game:** Skyfire (Game 1)
**Units:** 128 (8 phases × 16 units)
**Target Quality:** Commercial-grade fixed-screen shooter (1984-85 era)
**Comparable To:** Arcadia, Spectipede, Alien Swarm

---

## What Makes This "Spectrum"

The ZX Spectrum has:
- **No hardware sprites** — everything is software-rendered
- **Attribute colour system** — 8×8 cells, one foreground + background per cell
- **Colour clash** — design WITH it, not against it
- **Beeper sound** — one channel, creative tricks required
- **No joystick standard** — keyboard is primary (Kempston optional)

This shooter embraces these constraints. Enemies are attribute-coloured blocks. The player ship works within colour cells. Sound is punchy beeper effects. The result is unmistakably Spectrum.

---

## Design Philosophy

- **One concept per unit** — never overwhelming
- **Always playable** — from Unit 2 onwards
- **Debugging inline** — every unit includes "if it doesn't work"
- **Attribute system central** — colour IS the game's visual identity
- **Beeper sound throughout** — not silent until late game
- **Commercial quality by Unit 128** — a real game

---

## Phase 1: Minimal Playable Game (Units 1-16)

**Goal:** Complete game loop — shoot enemies, score points, die, restart.

| Unit | You Add | Result |
|------|---------|--------|
| 1 | Ship on screen (attribute block) | See your ship (coloured cell) |
| 2 | Keyboard moves ship (QAOP) | **Control something** |
| 3 | Fire button shoots (SPACE/M) | Bullet flies up |
| 4 | Laser sound (beeper) | Satisfying "pzzt" |
| 5 | One enemy appears | Target exists |
| 6 | Bullet hits enemy | **It dies!** |
| 7 | Explosion sound (beeper) | Feedback |
| 8 | Score display | See your points |
| 9 | Enemies spawn continuously | Challenge |
| 10 | Enemy touches ship | You can die |
| 11 | Game over screen | End state |
| 12 | Press key to restart | **Complete loop** |
| 13 | Title screen | Feels real |
| 14 | Three lives | Forgiveness |
| 15 | Life lost flash/sound | Feedback |
| 16 | Integration + edge cases | Solid foundation |

**Spectrum-Specific Unit 1:**
```asm
; Ship is a coloured attribute cell
; Bright cyan on black = %01000101
ld a,%01000101
ld (ship_attr_addr),a

; Fill the cell's pixels so colour shows
ld hl,ship_screen_addr
ld b,8
ship_fill:
    ld (hl),$ff
    inc h
    djnz ship_fill
```

**If it doesn't work (Unit 1):**
- **No colour?** Check attribute address ($5800+) vs screen address ($4000+)
- **Wrong position?** Screen layout is weird — use lookup table
- **Colour clash?** Ship crossed cell boundary — keep within 8×8

**End of Phase 1:** Playable shooter with Spectrum character.

---

## Phase 2: Enemy Variety (Units 17-32)

**Goal:** Multiple enemy types, distinct by colour and movement.

| Unit | You Add | Result |
|------|---------|--------|
| 17 | Fast enemy (red, dives) | Variety begins |
| 18 | Slow enemy (green, drifts) | Pacing contrast |
| 19 | Zigzag enemy (yellow, weaves) | Movement patterns |
| 20 | Colour = enemy type | Instant recognition |
| 21 | Different point values | Risk/reward |
| 22 | Wave system (8 enemies = wave) | Structure |
| 23 | Wave complete bonus | Incentive to clear |
| 24 | Faster spawning each wave | Difficulty curve |
| 25 | Wave number display | Progress visible |
| 26 | Mix of enemy types per wave | Tactical variety |
| 27 | Later waves = harder mix | Escalation |
| 28 | Enemy spawn sound | Audio feedback |
| 29 | Wave start sound | Punctuation |
| 30 | Brief pause between waves | Breathing room |
| 31 | BRIGHT attribute for tough enemies | Visual hierarchy |
| 32 | Integration + balance | Feels fair |

**Spectrum-Specific:**
- Enemy type shown through INK colour (no sprite changes needed)
- BRIGHT bit indicates elite/tough enemies
- Colour clash managed by keeping enemies in separate rows

**End of Phase 2:** Varied enemies, each instantly recognisable by colour.

---

## Phase 3: Player Abilities (Units 33-48)

**Goal:** Power-ups make the player stronger.

| Unit | You Add | Result |
|------|---------|--------|
| 33 | Power-up drops from enemies | Collectibles exist |
| 34 | Collect power-up = effect | System works |
| 35 | Speed boost (move faster) | Agility |
| 36 | Rapid fire (shoot faster) | Firepower |
| 37 | Power-up collect sound | Satisfying pickup |
| 38 | Power-up flashes (FLASH attribute) | Visibility |
| 39 | Power-ups are temporary | Strategic decisions |
| 40 | Timer shown via border colour | Know when it ends |
| 41 | Double shot (two bullets) | Coverage |
| 42 | Wide shot (three directions) | Screen control |
| 43 | Shield (one free hit) | Defensive option |
| 44 | Shield shown via BRIGHT | See protection |
| 45 | Shield break effect | Dramatic feedback |
| 46 | Power-up frequency tuning | Balance |
| 47 | No power-ups Wave 1 | Earned progression |
| 48 | Integration + balance | Rewarding loop |

**Spectrum-Specific:**
- FLASH attribute makes power-ups visible
- Border colour indicates active power-up
- Shield = BRIGHT attribute on ship

**End of Phase 3:** Power-ups feel great, add strategy.

---

## Phase 4: Enemies Fight Back (Units 49-64)

**Goal:** Enemies shoot, creating dodge gameplay.

| Unit | You Add | Result |
|------|---------|--------|
| 49 | Enemy bullet (one at a time) | Danger from above |
| 50 | Enemy bullet visible | Clear threat |
| 51 | Enemy bullet hits player | Real danger |
| 52 | Enemy fire sound | Audio warning |
| 53 | Random enemy fires | Unpredictable |
| 54 | Shooter enemy type (cyan) | Role variety |
| 55 | Shooter worth more points | Risk/reward |
| 56 | Multiple enemy bullets | Intensity |
| 57 | Bullet speed varies by wave | Escalation |
| 58 | Aimed shots (toward player) | Smart enemies |
| 59 | Aimed vs random mix | Variety |
| 60 | Shoot enemy bullets | Skill option |
| 61 | Player death = bullets clear | Fair restart |
| 62 | Bullet density tuning | Not overwhelming |
| 63 | Colour clash bullet fix | Bullets stay visible |
| 64 | Integration + balance | Challenging but fair |

**Spectrum-Specific:**
- Enemy bullets = different INK from enemies (avoid clash)
- Careful attribute management when bullets cross enemy cells
- Border flash on near miss

**End of Phase 4:** Proper two-way combat. Dodging matters.

---

## Phase 5: Visual Polish (Units 65-80)

**Goal:** Game looks commercially polished (within Spectrum limits).

| Unit | You Add | Result |
|------|---------|--------|
| 65 | Starfield background (pixels) | Depth |
| 66 | Multiple star speeds | Parallax effect |
| 67 | Stars don't colour clash | Technical care |
| 68 | Explosion animation (attribute flash) | Impact |
| 69 | Multi-frame explosion | Visual drama |
| 70 | Player death sequence | Stakes |
| 71 | Border flash on events | Spectrum flair |
| 72 | Screen shake (scroll offset) | Game feel |
| 73 | Enemy spawn animation | Polish |
| 74 | Smooth movement (pixel-level) | Professional feel |
| 75 | Custom font for text | Cohesive look |
| 76 | Colour cycling title | Attract mode |
| 77 | Attribute colour schemes | Visual themes |
| 78 | Score highlight on increase | Feedback |
| 79 | Clean attribute layout | No accidental clash |
| 80 | Integration + visual consistency | Cohesive look |

**Spectrum-Specific:**
- Stars are pixels in PAPER area (no clash)
- Explosions cycle through colours rapidly
- Border colour is a key feedback channel

**End of Phase 5:** Looks like a real Spectrum game. Distinctive style.

---

## Phase 6: Audio Polish (Units 81-96)

**Goal:** Rich beeper sound design.

| Unit | You Add | Result |
|------|---------|--------|
| 81 | Title screen music (beeper tune) | Atmosphere |
| 82 | Simple melody loop | Recognisable |
| 83 | Music stops on game start | Clean transition |
| 84 | Game over jingle | Punctuation |
| 85 | High score jingle | Celebration |
| 86 | Wave complete jingle | Achievement |
| 87 | Varied explosion pitches | Richness |
| 88 | Low lives warning beep | Tension |
| 89 | Different power-up sounds | Distinction |
| 90 | Boss warning sound | Drama |
| 91 | Enemy dive sound | Audio cues |
| 92 | Shield hit sound | Status feedback |
| 93 | Beeper engine (multi-voice trick) | Advanced |
| 94 | In-game beat/pulse | Rhythm |
| 95 | Sound priority system | No cutoff |
| 96 | Integration + audio polish | Sounds great |

**Spectrum-Specific:**
- All sound through 1-bit beeper
- Multi-voice tricks via rapid alternation
- In-game sound must be quick (halts gameplay briefly)

**End of Phase 6:** Impressive beeper sound. Punchy and characterful.

---

## Phase 7: Boss Battles (Units 97-112)

**Goal:** Epic boss fights using attribute system creatively.

| Unit | You Add | Result |
|------|---------|--------|
| 97 | Boss appears every 5 waves | Structure |
| 98 | Boss is multi-cell (4×2 attributes) | Impressive size |
| 99 | Boss movement pattern | Behaviour |
| 100 | Boss health bar | Visible progress |
| 101 | Boss takes multiple hits | Endurance |
| 102 | Boss hit flash (BRIGHT toggle) | Feedback |
| 103 | Boss shoots (spread pattern) | Danger |
| 104 | Boss phases (colour change at 50%) | Escalation |
| 105 | Phase 2 = faster/angrier | Drama |
| 106 | Boss death explosion (BIG) | Payoff |
| 107 | Boss defeat bonus | Reward |
| 108 | Boss defeat jingle | Celebration |
| 109 | Second boss type (wave 10) | Variety |
| 110 | Second boss different pattern | Fresh challenge |
| 111 | Boss warning (border) | Preparation |
| 112 | Integration + boss balance | Fair fights |

**Spectrum-Specific:**
- Bosses made of multiple attribute cells (largest "sprites")
- Colour changes indicate damage state
- FLASH attribute during vulnerability

**End of Phase 7:** Boss fights are memorable highlights.

---

## Phase 8: Final Polish (Units 113-128)

**Goal:** Commercial release quality.

| Unit | You Add | Result |
|------|---------|--------|
| 113 | High score table (top 5) | Competition |
| 114 | Initials entry | Ownership |
| 115 | High scores on title | Bragging |
| 116 | Attract mode (demo) | Shop display |
| 117 | Two-player alternating | Multiplayer |
| 118 | Score comparison | Competition |
| 119 | Difficulty select | Accessibility |
| 120 | Difficulty affects gameplay | Real difference |
| 121 | Extra life at 10,000 | Reward skill |
| 122 | Extra life celebration | Feedback |
| 123 | Kempston joystick support | Accessibility |
| 124 | Sinclair joystick support | More options |
| 125 | PAL timing polish | Platform correct |
| 126 | Loading screen (if tape) | Professional |
| 127 | Final balance + bugs | Release ready |
| 128 | **Complete game** | Ship it! |

**End of Phase 8:** A game worthy of 1985 software house release.

---

## Spectrum-Specific Debugging (Throughout)

**Colour Clash Issues:**
- If colours bleed: Check objects stay within attribute cell boundaries
- If objects disappear: They're same colour as background
- If background corrupts: You're writing to wrong attribute address

**Screen Address Issues:**
- Screen layout is non-linear (thirds interleaved)
- Use lookup table for Y→address conversion
- `inc h` moves down within character row, not to next pixel row

**Beeper Issues:**
- If sound affects gameplay: Keep sounds SHORT
- If no sound: Check border I/O port ($FE)
- If sound wrong pitch: Check loop timing

**Keyboard Issues:**
- Keys are active LOW (0 = pressed)
- Each half-row is separate port
- Multiple keys = AND the results

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 8 (Unit 128) |
|--------|-------------------|---------------------|
| Enemies | One type, falls down | 4+ types, patterns, aimed shots |
| Player | Move + shoot | Power-ups, shield, spread shot |
| Bosses | None | Two types with phases |
| Visuals | Attribute blocks | Smooth animation, explosions, parallax |
| Audio | Pew + boom | Full beeper music, varied SFX |
| Modes | Single play | Two-player, difficulty select, attract |
| Polish | Functional | Kempston support, high scores, initials |

---

**Version:** 1.0
**Last Updated:** 2026-01-17
