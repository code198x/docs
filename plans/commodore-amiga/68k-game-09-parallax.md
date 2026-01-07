# Parallax: 128-Unit Outline

**Game:** 9 of 16 (68000 Assembly)
**Platform:** Commodore Amiga
**Language:** 68000 Assembly
**Units:** 128 (8 phases)
**Concept:** Horizontal parallax shooter - the quintessential Amiga showcase.

---

## Why This Game Ninth?

Parallax introduces the Amiga's signature capability:

1. **Dual playfield mode** - Two independent scroll layers
2. **Multi-speed scrolling** - Parallax depth effect
3. **Hardware scrolling** - Smooth pixel scroll
4. **Copper palette cycling** - Animated colours
5. **MOD replay** - Tracker music

This is what made Amiga games distinctive.

---

## Skills Applied from Previous Games

| Skill | From | Application |
|-------|------|-------------|
| Blitter BOBs | All | Player, enemies |
| Collision | All | Shooting, damage |
| Object pools | Blast Zone | Bullets, enemies |
| Wave systems | Blast Zone | Level progression |
| All fundamentals | Games 1-8 | Core techniques |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Dual playfield | 1 | Two scroll layers |
| Hardware scroll | 2 | BPL scroll registers |
| Copper cycling | 3 | Animated palettes |
| Blitter updates | 4 | Scroll tile refresh |
| MOD replay | 6 | Tracker music |

---

## Phase 1: Dual Playfield Setup (Units 1-16)
*Two independent display layers.*

### Units 1-4: Dual Playfield Concept
- **Unit 1:** Playfield overview - bitplane layers
- **Unit 2:** Dual playfield mode - BPLCON0
- **Unit 3:** Playfield priority - which in front
- **Unit 4:** Separate colours - two palettes

### Units 5-8: Display Setup
- **Unit 5:** Bitplane allocation - 3+3 or 2+2
- **Unit 6:** Playfield pointers - separate sets
- **Unit 7:** Display dimensions - overscan
- **Unit 8:** First dual display - two layers

### Units 9-12: Layer Design
- **Unit 9:** Background layer - distant scenery
- **Unit 10:** Foreground layer - close terrain
- **Unit 11:** Transparency - colour 0
- **Unit 12:** Layer demo - two visible layers

### Units 13-16: Player Setup
- **Unit 13:** Ship sprite - hardware sprite
- **Unit 14:** Ship movement - 8-directional
- **Unit 15:** Ship boundaries - screen limits
- **Unit 16:** Dual playfield demo - ship over layers

**Phase Goal:** Dual playfield with player.

---

## Phase 2: Hardware Scrolling (Units 17-32)
*Smooth parallax movement.*

### Units 17-20: Scroll Registers
- **Unit 17:** BPL1MOD/BPL2MOD - modulos
- **Unit 18:** BPLCON1 - fine scroll
- **Unit 19:** Scroll calculation - coarse + fine
- **Unit 20:** Single layer scroll

### Units 21-24: Parallax Scrolling
- **Unit 21:** Different speeds - layer rates
- **Unit 22:** Background slow - distant
- **Unit 23:** Foreground fast - close
- **Unit 24:** Parallax effect - depth illusion

### Units 25-28: Scroll Management
- **Unit 25:** Scroll position - 16-bit tracking
- **Unit 26:** Wrap around - seamless
- **Unit 27:** Variable speed - player control
- **Unit 28:** Smooth scrolling demo

### Units 29-32: Blitter Tile Updates
- **Unit 29:** Tile columns - new tiles needed
- **Unit 30:** Blitter copy - add new column
- **Unit 31:** Timing - during VBlank
- **Unit 32:** Seamless scrolling - no glitches

**Phase Goal:** Smooth parallax scrolling.

---

## Phase 3: Combat System (Units 33-48)
*Shooting and enemies.*

### Units 33-36: Player Weapons
- **Unit 33:** Bullet sprites - small BOBs
- **Unit 34:** Bullet pool - reuse
- **Unit 35:** Fire rate - cooldown
- **Unit 36:** Bullet movement - with scroll

### Units 37-40: Enemy Waves
- **Unit 37:** Enemy types - multiple designs
- **Unit 38:** Enemy spawning - off-screen
- **Unit 39:** Wave patterns - formations
- **Unit 40:** Enemy movement - various paths

### Units 41-44: Collision
- **Unit 41:** Bullet/enemy - hit detection
- **Unit 42:** Enemy/player - damage
- **Unit 43:** Terrain collision - foreground
- **Unit 44:** Explosion effects - BOBs

### Units 45-48: Copper Palette Cycling
- **Unit 45:** Cycling concept - animated colours
- **Unit 46:** Water effect - flowing
- **Unit 47:** Fire effect - flickering
- **Unit 48:** Background animation

**Phase Goal:** Combat with visual effects.

---

## Phase 4: Power-ups and Bosses (Units 49-64)
*Upgrades and challenges.*

### Units 49-52: Power-up System
- **Unit 49:** Power-up sprites - collectibles
- **Unit 50:** Power-up drops - from enemies
- **Unit 51:** Weapon upgrades - spread, laser
- **Unit 52:** Shield/speed - defensive

### Units 53-56: Weapon Types
- **Unit 53:** Standard shot - single bullet
- **Unit 54:** Spread shot - triple
- **Unit 55:** Laser - continuous beam
- **Unit 56:** Missile - homing

### Units 57-60: Mid-Boss
- **Unit 57:** Mid-boss design - large BOB
- **Unit 58:** Mid-boss patterns - attacks
- **Unit 59:** Mid-boss health - multi-hit
- **Unit 60:** Mid-boss defeat - explosion

### Units 61-64: End Boss
- **Unit 61:** Boss design - screen-filling
- **Unit 62:** Boss phases - multiple patterns
- **Unit 63:** Boss weak points - targeting
- **Unit 64:** Boss defeat - level complete

**Phase Goal:** Power-ups and bosses.

---

## Phase 5: Level Design (Units 65-80)
*Complete stages.*

### Units 65-68: Level Structure
- **Unit 65:** Level data - tile maps
- **Unit 66:** Level length - scroll distance
- **Unit 67:** Enemy placement - triggers
- **Unit 68:** Level pacing - difficulty curve

### Units 69-72: Stage 1
- **Unit 69:** Stage 1 theme - space/planet
- **Unit 70:** Stage 1 enemies - wave design
- **Unit 71:** Stage 1 boss
- **Unit 72:** Stage 1 complete

### Units 73-76: Stage 2
- **Unit 73:** Stage 2 theme - different environment
- **Unit 74:** Stage 2 enemies - new types
- **Unit 75:** Stage 2 hazards - terrain
- **Unit 76:** Stage 2 boss

### Units 77-80: Stage 3
- **Unit 77:** Stage 3 theme - final approach
- **Unit 78:** Stage 3 difficulty - hardest
- **Unit 79:** Stage 3 boss - final
- **Unit 80:** Victory sequence

**Phase Goal:** Three complete stages.

---

## Phase 6: MOD Audio (Units 81-96)
*Tracker music system.*

### Units 81-84: MOD Format
- **Unit 81:** MOD overview - pattern-based
- **Unit 82:** Sample data - instruments
- **Unit 83:** Pattern data - notes
- **Unit 84:** Module structure - songs

### Units 85-88: MOD Replay
- **Unit 85:** Replay routine - timing
- **Unit 86:** Sample playback - Paula channels
- **Unit 87:** Pattern reading - note handling
- **Unit 88:** Effects - volume, pitch

### Units 89-92: Game Integration
- **Unit 89:** Music loading - from disk
- **Unit 90:** Music switching - per level
- **Unit 91:** Music/SFX balance - channel allocation
- **Unit 92:** Dynamic music - intensity

### Units 93-96: Sound Effects
- **Unit 93:** Prioritised SFX - over music
- **Unit 94:** Channel stealing - temporary
- **Unit 95:** Effect variety - many sounds
- **Unit 96:** Audio polish

**Phase Goal:** Full MOD soundtrack.

---

## Phase 7: Polish (Units 97-112)
*Presentation and features.*

### Units 97-100: Title Screen
- **Unit 97:** Title graphics - logo
- **Unit 98:** Title animation - effects
- **Unit 99:** Menu system - options
- **Unit 100:** Title music

### Units 101-104: HUD
- **Unit 101:** Score display - top
- **Unit 102:** Lives display - ships
- **Unit 103:** Weapon indicator - current
- **Unit 104:** Boss health bar

### Units 105-108: Intermissions
- **Unit 105:** Level intro - stage name
- **Unit 106:** Level complete - stats
- **Unit 107:** Game over - continue?
- **Unit 108:** Attract mode - demo

### Units 109-112: Extra Features
- **Unit 109:** Difficulty settings
- **Unit 110:** Two-player option
- **Unit 111:** High score saving
- **Unit 112:** Options screen

**Phase Goal:** Polished presentation.

---

## Phase 8: Release (Units 113-128)
*Testing and distribution.*

### Units 113-116: Balance
- **Unit 113:** Difficulty tuning
- **Unit 114:** Weapon balance
- **Unit 115:** Boss balance
- **Unit 116:** Scoring balance

### Units 117-120: Testing
- **Unit 117:** Full playthrough
- **Unit 118:** Edge cases
- **Unit 119:** Performance testing
- **Unit 120:** Memory usage

### Units 121-124: Optimisation
- **Unit 121:** Blitter optimisation
- **Unit 122:** Scroll optimisation
- **Unit 123:** Collision optimisation
- **Unit 124:** Overall tuning

### Units 125-128: Release
- **Unit 125:** Credits screen
- **Unit 126:** Documentation
- **Unit 127:** Final testing
- **Unit 128:** Release build - ADF

**Phase Goal:** Complete shooter.

---

## Summary

**Parallax** showcases the Amiga's signature capabilities.

### Technical Specifications

- **Display:** Dual playfield, 320×256
- **Scroll:** Multi-speed hardware parallax
- **Player:** Hardware sprite, 8-directional
- **Weapons:** 4 types with upgrades
- **Enemies:** Multiple types, formations
- **Bosses:** Mid-boss and end boss per stage
- **Stages:** 3 complete levels
- **Audio:** Full MOD soundtrack + SFX
- **Distribution:** Bootable ADF

### Skills for Next Game

- Dual playfield mastery
- Hardware scrolling
- MOD replay integration
- Complex level design
- Boss pattern systems
