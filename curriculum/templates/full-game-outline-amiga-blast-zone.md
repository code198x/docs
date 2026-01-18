# Full Game Outline: Amiga Blast Zone (128 Units)

**Game:** Blast Zone (Game 1)
**Units:** 128 (8 phases × 16 units)
**Target Quality:** Commercial-grade fixed-screen shooter (1987-88 era)
**Comparable To:** Xenon, Menace, Blood Money (single-screen sections)

---

## What Makes This "Amiga"

The Amiga has:
- **Custom chipset** — Agnus, Denise, Paula working in concert
- **Hardware sprites** — 8 sprites, 16 pixels wide, can be multiplexed
- **Blitter Objects (BOBs)** — software sprites of any size via Blitter
- **Copper** — display list coprocessor for mid-frame effects
- **Bitplane graphics** — planar format, not chunky pixels
- **Paula audio** — 4 channels of 8-bit sampled sound
- **Joystick input** — analogue ports with fire buttons

This shooter showcases the chipset symphony. Player is a hardware sprite. Enemies are BOBs (Blitter Objects). Copper creates gradient backgrounds. Paula plays sampled explosions. The result is unmistakably Amiga.

---

## Design Philosophy

- **One concept per unit** — never overwhelming
- **Always playable** — from Unit 2 onwards
- **Debugging inline** — every unit includes "if it doesn't work"
- **Chipset harmony** — Blitter, Copper, Paula all used from early on
- **Sampled sound throughout** — that Amiga audio quality
- **Commercial quality by Unit 128** — a real game

---

## Phase 1: Minimal Playable Game (Units 1-16)

**Goal:** Complete game loop — shoot enemies, score points, die, restart.

| Unit | You Add | Result |
|------|---------|--------|
| 1 | Ship sprite on screen | See your ship |
| 2 | Joystick moves ship | **Control something** |
| 3 | Fire button shoots | Bullet flies up |
| 4 | Laser sample plays | Satisfying "pew" |
| 5 | One enemy (BOB) | Target exists |
| 6 | Bullet hits enemy | **It dies!** |
| 7 | Explosion sample | Feedback |
| 8 | Score display (Blitter text) | See your points |
| 9 | Enemies spawn continuously | Challenge |
| 10 | Enemy touches ship | You can die |
| 11 | Game over screen | End state |
| 12 | Fire button restarts | **Complete loop** |
| 13 | Title screen | Feels real |
| 14 | Three lives | Forgiveness |
| 15 | Life lost effect/sample | Feedback |
| 16 | Integration + edge cases | Solid foundation |

**Amiga-Specific Unit 1:**
```asm
; Set up hardware sprite 0 (player ship)
; Sprite data must be in chip RAM

    ; Point sprite 0 to data
    move.l  #ship_sprite,$dff120    ; SPR0PT

    ; Sprite data format:
    ; Word 0: VSTART + HSTART high bits
    ; Word 1: VSTOP + control bits
    ; Then pairs of words for each line (2 bitplanes)

ship_sprite:
    dc.w    $6050       ; Y=96, X=80
    dc.w    $7800       ; Y stop=120
    dc.w    %0001100000011000, %0000000000000000  ; Line 1
    dc.w    %0011110000111100, %0000000000000000  ; Line 2
    ; ... etc for 24 lines
    dc.w    0,0         ; End of sprite
```

**If it doesn't work (Unit 1):**
- **Black screen?** Check DMACON — sprites need $8020, display needs $8100+
- **No sprite?** Sprite data not in chip RAM, or SPRxPT not set
- **Wrong position?** Sprite header encodes position (tricky format)
- **Wrong colours?** Set COLOR17-19 for sprite 0 palette

**End of Phase 1:** Playable Amiga shooter.

---

## Phase 2: Enemy Variety (Units 17-32)

**Goal:** Multiple enemy types as BOBs with different graphics.

| Unit | You Add | Result |
|------|---------|--------|
| 17 | Fast enemy (different BOB) | Variety |
| 18 | Slow enemy (another BOB) | Contrast |
| 19 | Zigzag enemy (weaves) | Patterns |
| 20 | Different BOB graphics per type | Distinction |
| 21 | Different colours per type | Colour coding |
| 22 | Different point values | Risk/reward |
| 23 | Wave system | Structure |
| 24 | Wave complete bonus | Incentive |
| 25 | Faster spawning | Difficulty |
| 26 | Wave display | Progress |
| 27 | Mix of types | Variety |
| 28 | Harder mix later | Escalation |
| 29 | Enemy spawn sample | Audio |
| 30 | Wave start jingle | Punctuation |
| 31 | Pause between waves | Breathing |
| 32 | Integration + balance | Fair |

**Amiga-Specific:**
- Enemies are BOBs (any size, drawn by Blitter)
- Blitter cookie-cut for transparency
- BOBs restore background when moving

**End of Phase 2:** Varied enemies, impressive BOB graphics.

---

## Phase 3: Player Abilities (Units 33-48)

**Goal:** Power-ups with Amiga audiovisual flair.

| Unit | You Add | Result |
|------|---------|--------|
| 33 | Power-up drops (BOB) | Collectibles |
| 34 | Collect = effect | System works |
| 35 | Speed boost | Agility |
| 36 | Rapid fire | Firepower |
| 37 | Power-up sample | Satisfying |
| 38 | Copper colour cycle on pickup | Visual flair |
| 39 | Temporary power-ups | Strategic |
| 40 | Timer via Copper bar | Visibility |
| 41 | Double shot | Coverage |
| 42 | Spread shot | Control |
| 43 | Shield | Defence |
| 44 | Shield = sprite overlay | Visible |
| 45 | Shield break effect | Dramatic |
| 46 | Frequency tuning | Balance |
| 47 | No power-ups Wave 1 | Earned |
| 48 | Integration + balance | Rewarding |

**Amiga-Specific:**
- Power-up = BOB with colour cycling via Copper
- Shield = additional hardware sprite attached to player
- Copper bar shows remaining time

**End of Phase 3:** Power-ups with Amiga polish.

---

## Phase 4: Enemies Fight Back (Units 49-64)

**Goal:** Enemies shoot, Blitter handles many objects.

| Unit | You Add | Result |
|------|---------|--------|
| 49 | Enemy bullet (BOB) | Danger |
| 50 | Bullet graphics | Visible |
| 51 | Bullet hits player | Real danger |
| 52 | Enemy fire sample | Warning |
| 53 | Random firing | Unpredictable |
| 54 | Shooter enemy type | Roles |
| 55 | Shooter worth more | Risk/reward |
| 56 | Multiple bullets | Intensity |
| 57 | Speed varies | Escalation |
| 58 | Aimed shots | Smart |
| 59 | Aimed vs random | Variety |
| 60 | Shoot bullets | Skill |
| 61 | Death = clear | Fair |
| 62 | Density tuning | Balance |
| 63 | Blitter queue management | Performance |
| 64 | Integration + balance | Challenging |

**Amiga-Specific:**
- Many BOBs = Blitter busy, need to manage
- Wait for Blitter between operations
- Prioritise visible objects

**End of Phase 4:** Intense combat, Blitter handles the load.

---

## Phase 5: Visual Polish (Units 65-80)

**Goal:** Showcase Amiga graphics capabilities.

| Unit | You Add | Result |
|------|---------|--------|
| 65 | Copper gradient background | Depth |
| 66 | Animated gradient | Motion |
| 67 | Starfield (separate layer) | Parallax |
| 68 | Explosion animation (BOB) | Impact |
| 69 | Multi-frame explosion | Drama |
| 70 | Player death sequence | Stakes |
| 71 | Screen flash (Copper) | Emphasis |
| 72 | Screen shake | Game feel |
| 73 | Enemy spawn effect | Polish |
| 74 | Smooth movement (subpixel) | Professional |
| 75 | 32-colour graphics | Rich palette |
| 76 | Copper colour bars (title) | Classic Amiga |
| 77 | Palette themes per wave | Visual variety |
| 78 | Score effect | Feedback |
| 79 | Clean display composition | Professional |
| 80 | Integration + consistency | Cohesive |

**Amiga-Specific:**
- Copper gradients = classic Amiga look
- 32 colours on screen (5 bitplanes)
- Copper can change palette mid-screen

**End of Phase 5:** Looks like a commercial Amiga game.

---

## Phase 6: Audio Polish (Units 81-96)

**Goal:** Full Paula soundtrack with samples.

| Unit | You Add | Result |
|------|---------|--------|
| 81 | Title music (MOD) | Atmosphere |
| 82 | 4-channel tracker tune | Rich sound |
| 83 | Music fades on start | Transition |
| 84 | Game over tune | Punctuation |
| 85 | High score tune | Celebration |
| 86 | Wave complete jingle | Achievement |
| 87 | Varied explosion samples | Richness |
| 88 | Low lives warning | Tension |
| 89 | Power-up jingles | Distinction |
| 90 | Boss warning sample | Drama |
| 91 | Enemy dive sound | Cues |
| 92 | Shield sound | Feedback |
| 93 | MOD player integration | System |
| 94 | In-game music | Atmosphere |
| 95 | SFX channel stealing | Priority |
| 96 | Integration + mix | Sounds great |

**Amiga-Specific:**
- MOD format music (ProTracker compatible)
- 4 channels = music + sound effects together
- Channel stealing for SFX during music
- 8-bit samples = quality audio

**End of Phase 6:** That distinctive Amiga sound.

---

## Phase 7: Boss Battles (Units 97-112)

**Goal:** Epic bosses using large BOBs.

| Unit | You Add | Result |
|------|---------|--------|
| 97 | Boss every 5 waves | Structure |
| 98 | Boss = large BOB (64×64) | Impressive |
| 99 | Boss movement | Behaviour |
| 100 | Boss health (Copper bar) | Progress |
| 101 | Boss takes hits | Endurance |
| 102 | Boss hit flash | Feedback |
| 103 | Boss shoots (spread) | Danger |
| 104 | Boss phases | Escalation |
| 105 | Phase 2 = faster | Drama |
| 106 | Boss death (big!) | Payoff |
| 107 | Boss bonus | Reward |
| 108 | Boss jingle | Celebration |
| 109 | Second boss type | Variety |
| 110 | Different pattern | Fresh |
| 111 | Boss warning | Prep |
| 112 | Integration + balance | Fair |

**Amiga-Specific:**
- Boss = large BOB (Blitter handles any size)
- Copper bar for health is smooth and colourful
- Large explosions with multiple samples

**End of Phase 7:** Impressive boss encounters.

---

## Phase 8: Final Polish (Units 113-128)

**Goal:** Commercial release quality.

| Unit | You Add | Result |
|------|---------|--------|
| 113 | High score table | Competition |
| 114 | Initials entry | Ownership |
| 115 | Scores on title | Bragging |
| 116 | Attract mode | Display |
| 117 | Two-player alternating | Multiplayer |
| 118 | Score comparison | Competition |
| 119 | Difficulty select | Accessibility |
| 120 | Difficulty matters | Real difference |
| 121 | Extra life at 10,000 | Reward |
| 122 | Extra life fanfare | Feedback |
| 123 | PAL/NTSC handling | Platform |
| 124 | Continue option | Forgiveness |
| 125 | ADF disk creation | Distribution |
| 126 | Bootable disk | Professional |
| 127 | Final balance + bugs | Release ready |
| 128 | **Complete game** | Ship it! |

**End of Phase 8:** A game worthy of Amiga PD libraries or budget release.

---

## Amiga-Specific Debugging (Throughout)

**Black Screen / No Display:**
- DMACON not set ($dff096) — need $8380 minimum for display
- Copper not started (COP1LC + COPJMP1)
- Copper list in fast RAM (must be chip RAM!)
- Copper list not terminated ($ffff,$fffe)

**Sprites Not Visible:**
- DMACON sprite bits not set ($8020)
- Sprite data not in chip RAM
- Sprite position encoded wrong (header format)
- Sprite colours not set ($dff1a2+)

**BOBs Corrupt / Glitchy:**
- Not waiting for Blitter (check BLTBUSY)
- Wrong minterm for cookie-cut
- Not restoring background
- Source/dest not in chip RAM

**No Sound:**
- Audio DMA not enabled ($dff096)
- Volume zero ($dff0a8)
- Sample not in chip RAM
- Period too low or too high

**Crashes (Guru Meditation):**
- Address error (odd address for word/long)
- Illegal instruction
- Stack overflow
- Writing to protected memory

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 8 (Unit 128) |
|--------|-------------------|---------------------|
| Enemies | One BOB type | 4+ types, patterns, aimed |
| Player | Sprite, move + shoot | Power-ups, shield, spread |
| Bosses | None | Two types, large BOBs |
| Visuals | Basic display | Copper gradients, 32 colours, effects |
| Audio | Samples | Full MOD music, varied SFX |
| Modes | Single play | Two-player, difficulty, attract |
| Polish | Functional | Bootable ADF, high scores, ending |

---

## The Amiga Difference

Where other platforms have constraints, the Amiga has abundance:
- **More colours** — 32 on screen vs 16 (C64) or 4 (Spectrum)
- **Bigger sprites** — BOBs can be any size
- **Better sound** — 4-channel sampled audio
- **Copper magic** — mid-screen palette changes, effects

The challenge is using this power tastefully, not just showing off.

---

**Version:** 1.0
**Last Updated:** 2026-01-17
