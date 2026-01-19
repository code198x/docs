# Full Game Outline: NES Stellar Barrage (128 Units)

**Game:** Stellar Barrage (Game 1)
**Units:** 128 (8 phases × 16 units)
**Target Quality:** Commercial-grade fixed-screen shooter (1985-86 era)
**Comparable To:** Galaga, Galaxian, Space Invaders

---

## What Makes This "NES"

The NES has:
- **Tile-based PPU** — everything is 8×8 tiles, backgrounds AND sprites
- **64 hardware sprites** — but only 8 per scanline (flickering required)
- **Separate PPU memory** — CPU talks to PPU through registers, not direct access
- **Nametables** — 32×30 tile grid for backgrounds
- **APU sound** — 2 pulse, 1 triangle, 1 noise, 1 sample channel
- **Controller input** — standardised d-pad + A/B/Start/Select

This shooter showcases tile-based thinking. Enemies are sprites. Background is nametable tiles. The 8-sprite limit forces smart flickering. The APU gives distinctive NES sound.

---

## Design Philosophy

- **One concept per unit** — never overwhelming
- **Always playable** — from Unit 2 onwards
- **Debugging inline** — every unit includes "if it doesn't work"
- **PPU understanding central** — tiles, sprites, palettes
- **APU sound throughout** — that NES sound from Unit 4
- **Commercial quality by Unit 128** — a real game

---

## Phase 1: Minimal Playable Game (Units 1-16)

**Goal:** Complete game loop — shoot enemies, score points, die, restart.

| Unit | You Add | Result |
|------|---------|--------|
| 1 | Ship sprite on screen | See your ship |
| 2 | Controller moves ship | **Control something** |
| 3 | A button shoots | Bullet flies up |
| 4 | Laser sound (pulse channel) | Satisfying "pew" |
| 5 | One enemy sprite | Target exists |
| 6 | Bullet hits enemy | **It dies!** |
| 7 | Explosion sound (noise channel) | Feedback |
| 8 | Score display (background tiles) | See your points |
| 9 | Enemies spawn continuously | Challenge |
| 10 | Enemy touches ship | You can die |
| 11 | Game over screen | End state |
| 12 | Start button restarts | **Complete loop** |
| 13 | Title screen | Feels real |
| 14 | Three lives | Forgiveness |
| 15 | Life lost effect/sound | Feedback |
| 16 | Integration + edge cases | Solid foundation |

**NES-Specific Unit 1:**
```asm
; Set up sprite 0 (ship) in OAM
; OAM format: Y, Tile, Attributes, X
lda #$C0            ; Y position
sta $0200
lda #$01            ; Tile index
sta $0201
lda #$00            ; Attributes (palette 0, no flip)
sta $0202
lda #$78            ; X position (centered)
sta $0203

; In NMI, trigger OAM DMA
lda #$02
sta $4014           ; DMA from $0200
```

**If it doesn't work (Unit 1):**
- **Black screen?** Check $2001 (rendering enabled), check $2000 (NMI enabled)
- **No sprite?** Check OAM data at $0200+, check DMA in NMI
- **Wrong position?** Y is first byte, X is fourth (counterintuitive)
- **Wrong colours?** Check palette at $3F10+ (sprite palettes)

**End of Phase 1:** Playable NES shooter.

---

## Phase 2: Enemy Variety (Units 17-32)

**Goal:** Multiple enemy types with distinct sprites and movement.

| Unit | You Add | Result |
|------|---------|--------|
| 17 | Fast enemy (different tile) | Variety begins |
| 18 | Slow enemy (another tile) | Pacing contrast |
| 19 | Zigzag enemy (weaves) | Movement patterns |
| 20 | Different sprite tiles per type | Visual distinction |
| 21 | Different palettes per type | Colour coding |
| 22 | Different point values | Risk/reward |
| 23 | Wave system (8 enemies = wave) | Structure |
| 24 | Wave complete bonus | Incentive |
| 25 | Faster spawning each wave | Difficulty curve |
| 26 | Wave display (background tiles) | Progress visible |
| 27 | Mix of enemy types | Tactical variety |
| 28 | Later waves = harder mix | Escalation |
| 29 | Enemy spawn sound | Audio feedback |
| 30 | Wave start jingle | Punctuation |
| 31 | Brief pause between waves | Breathing room |
| 32 | Integration + balance | Feels fair |

**NES-Specific:**
- Each enemy type uses different CHR tile
- Palette choice (0-3) gives colour variety
- Max 64 sprites total, plan accordingly

**End of Phase 2:** Varied enemies, distinct by sprite and colour.

---

## Phase 3: Player Abilities (Units 33-48)

**Goal:** Power-ups make the player stronger.

| Unit | You Add | Result |
|------|---------|--------|
| 33 | Power-up drops (sprite) | Collectibles exist |
| 34 | Collect power-up = effect | System works |
| 35 | Speed boost | Agility |
| 36 | Rapid fire | Firepower |
| 37 | Power-up sound (triangle) | Satisfying |
| 38 | Power-up flashes (palette cycle) | Visibility |
| 39 | Power-ups are temporary | Strategic |
| 40 | Timer via HUD | Know when it ends |
| 41 | Double shot (two sprites) | Coverage |
| 42 | Spread shot (three directions) | Screen control |
| 43 | Shield (one free hit) | Defensive |
| 44 | Shield sprite overlay | See protection |
| 45 | Shield break effect | Feedback |
| 46 | Power-up frequency tuning | Balance |
| 47 | No power-ups Wave 1 | Earned |
| 48 | Integration + balance | Rewarding |

**NES-Specific:**
- Power-ups are sprites (count against limit)
- Palette cycling for visibility
- Shield = additional sprite layered on player

**End of Phase 3:** Power-ups feel great and add strategy.

---

## Phase 4: Enemies Fight Back (Units 49-64)

**Goal:** Enemies shoot, creating dodge gameplay.

| Unit | You Add | Result |
|------|---------|--------|
| 49 | Enemy bullet (sprite) | Danger |
| 50 | Enemy bullet visible tile | Clear threat |
| 51 | Enemy bullet hits player | Real danger |
| 52 | Enemy fire sound | Warning |
| 53 | Random enemy fires | Unpredictable |
| 54 | Shooter enemy type | Role variety |
| 55 | Shooter worth more | Risk/reward |
| 56 | Multiple enemy bullets | Intensity |
| 57 | Bullet speed varies | Escalation |
| 58 | Aimed shots | Smart enemies |
| 59 | Aimed vs random mix | Variety |
| 60 | Shoot enemy bullets | Skill option |
| 61 | Death = bullets clear | Fair |
| 62 | Bullet density tuning | Balance |
| 63 | Sprite limit management | 8-per-line |
| 64 | Integration + balance | Challenging |

**NES-Specific:**
- Enemy bullets compete for sprite slots
- May need flickering when busy
- Careful sprite Y-sorting to manage scanline limit

**End of Phase 4:** Proper two-way combat. Sprite management matters.

---

## Phase 5: Visual Polish (Units 65-80)

**Goal:** Game looks commercially polished.

| Unit | You Add | Result |
|------|---------|--------|
| 65 | Starfield (background tiles) | Depth |
| 66 | Animated stars (tile swap) | Motion |
| 67 | Multiple star types | Variety |
| 68 | Explosion animation (frames) | Impact |
| 69 | Multi-frame sprite sequence | Drama |
| 70 | Player death animation | Stakes |
| 71 | Screen flash (palette) | Emphasis |
| 72 | Sprite flicker system | Handle overflow |
| 73 | Enemy spawn animation | Polish |
| 74 | Smooth sprite movement | Professional |
| 75 | Custom CHR tiles | Cohesive look |
| 76 | Palette cycling title | Attract |
| 77 | Colour schemes per wave | Visual themes |
| 78 | Score flash on increase | Feedback |
| 79 | Clean nametable layout | Professional |
| 80 | Integration + consistency | Cohesive |

**NES-Specific:**
- Stars are background tiles, not sprites (saves sprite slots)
- Palette cycling via PPU palette updates in vblank
- Sprite flickering = rotate OAM order when >8 on scanline

**End of Phase 5:** Looks like a real NES game.

---

## Phase 6: Audio Polish (Units 81-96)

**Goal:** Full APU soundtrack.

| Unit | You Add | Result |
|------|---------|--------|
| 81 | Title music (pulse + triangle) | Atmosphere |
| 82 | Two-voice melody | Richer |
| 83 | Music stops on start | Transition |
| 84 | Game over jingle | Punctuation |
| 85 | High score jingle | Celebration |
| 86 | Wave complete jingle | Achievement |
| 87 | Varied explosion (noise pitch) | Richness |
| 88 | Low lives warning | Tension |
| 89 | Power-up jingles | Distinction |
| 90 | Boss warning | Drama |
| 91 | Enemy dive sound | Cues |
| 92 | Shield sound | Feedback |
| 93 | Sound engine (basic) | Organisation |
| 94 | Music during gameplay | Atmosphere |
| 95 | SFX over music | Priority |
| 96 | Integration + balance | Sounds great |

**NES-Specific:**
- Pulse 1 + 2 for melody/harmony
- Triangle for bass
- Noise for percussion/explosions
- SFX typically steal pulse 2 or noise

**End of Phase 6:** That distinctive NES sound throughout.

---

## Phase 7: Boss Battles (Units 97-112)

**Goal:** Epic boss fights using multiple sprites.

| Unit | You Add | Result |
|------|---------|--------|
| 97 | Boss every 5 waves | Structure |
| 98 | Boss = multi-sprite (2×2) | Large enemy |
| 99 | Boss movement pattern | Behaviour |
| 100 | Boss health bar (tiles) | Progress |
| 101 | Boss takes hits | Endurance |
| 102 | Boss hit flash | Feedback |
| 103 | Boss shoots (spread) | Danger |
| 104 | Boss phases | Escalation |
| 105 | Phase 2 faster | Drama |
| 106 | Boss death (big explosion) | Payoff |
| 107 | Boss bonus points | Reward |
| 108 | Boss defeat jingle | Celebration |
| 109 | Second boss type | Variety |
| 110 | Different pattern | Fresh |
| 111 | Boss warning | Prep |
| 112 | Integration + balance | Fair |

**NES-Specific:**
- Boss made of 4+ sprites (8×8 each)
- Careful Y-positioning to avoid scanline overflow
- Metasprite handling (multiple sprites as one object)

**End of Phase 7:** Boss fights are highlights.

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
| 123 | NTSC/PAL timing | Platform |
| 124 | Continue option | Forgiveness |
| 125 | Ending screen | Completion |
| 126 | Credits | Professional |
| 127 | Final balance + bugs | Release ready |
| 128 | **Complete game** | Ship it! |

**End of Phase 8:** A game worthy of 1986 NES release.

---

## NES-Specific Debugging (Throughout)

**Black Screen Issues:**
- $2001 not set (rendering off)
- $2000 NMI not enabled
- PPU warmup not waited (need 2 vblanks)
- Wrong palette (all black)

**Sprite Issues:**
- OAM DMA not happening in NMI
- Y position off-screen (>$EF hides sprite)
- Tile index wrong (check CHR bank)
- More than 8 on scanline (need flickering)

**Scroll Issues:**
- $2005 not reset after $2006 writes
- Writing to PPU outside vblank (glitches)

**Controller Issues:**
- Strobe sequence wrong ($4016 write 1, then 0)
- Reading wrong number of times
- Checking wrong bit for button

---

## Quality Comparison

| Aspect | Phase 1 (Unit 16) | Phase 8 (Unit 128) |
|--------|-------------------|---------------------|
| Enemies | One type | 4+ types, patterns, aimed |
| Player | Move + shoot | Power-ups, shield, spread |
| Bosses | None | Two types with phases |
| Visuals | Basic sprites | Animation, effects, polish |
| Audio | Pew + boom | Full APU music, varied SFX |
| Modes | Single play | Two-player, difficulty, attract |
| Polish | Functional | High scores, initials, ending |

---

**Version:** 1.0
**Last Updated:** 2026-01-17
