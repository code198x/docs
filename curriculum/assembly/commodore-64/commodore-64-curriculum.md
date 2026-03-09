# Commodore 64 Curriculum

**Platform:** Commodore 64
**Killer Feature:** SID sound chip and hardware sprites
**Assembly Games:** 4
**Total Units:** 1,408

---

## Overview

The Commodore 64 curriculum teaches 6510 assembly programming through four complete games. The sequence begins with hardware sprites and the SID chip — the C64's twin defining features — and progresses through raster effects, sprite multiplexing, and demo-scene techniques until learners can produce commercial-quality games.

The C64 offered hardware sprites, three-voice synthesised sound with programmable filters, and a VIC-II chip capable of smooth hardware scrolling and raster interrupts. Professional developers like Factor 5, System 3, and Thalamus pushed these capabilities to extraordinary levels. This curriculum teaches learners to do the same.

By the final game, learners will have skills matching professional C64 developers of the late 1980s and early 1990s.

---

## Assembly Track

### Structure

| Game | Units | Phases | Units/Phase | Role |
|------|-------|--------|-------------|------|
| 1 | 128 | 8 | 16 | Accessible entry — sprites + SID from frame one |
| 2 | 256 | 8 | 32 | Signature technique — scrolling, large sprites, SID atmosphere |
| 3 | 512 | 16 | 32 | Ambitious — run 'n' gun with sprite multiplexing |
| 4 | 512 | 16 | 32 | Capstone — fast loader, demo-scene, professional distribution |
| **Total** | **1,408** | | | |

---

### Game 1: Wave-Based Space Shooter

**Units:** 128 (8 phases)
**Genre:** Wave-based space shooter
**Inspired by:** Katakis, Galaga, Armalyte
**Working title:** TBD

**Concept:** Control a ship, destroy waves of enemies, collect power-ups, fight bosses. The player has something on screen in unit 1, is shooting by unit 3, and has a playable game with SID sound by unit 8. This is the C64 doing what it does best: colourful hardware sprites with a pounding SID soundtrack.

**Skills taught:**
- 6510 fundamentals (registers, addressing modes, zero page)
- VIC-II sprite setup (enable, position, pointers, colour, multicolour mode)
- Sprite-to-sprite and sprite-to-background collision ($D01E, $D01F)
- CIA joystick reading ($DC00)
- Bullet pool management (fixed array, recycling)
- Wave patterns and enemy formations
- Enemy AI (path following, dive attacks, formation breaks)
- Power-up system (weapon upgrades, shields, speed)
- SID sound effects integrated throughout (not bolted on at the end)
- SID basics: voices, waveforms, ADSR, frequency
- Boss encounters with multi-phase patterns
- Score display via custom character set
- Title screen, game-over, high scores
- Raster interrupt introduction (stable playfield, IRQ timing)
- Starfield background (character scrolling)

**Why first:** A wave shooter gets something playable on screen immediately. The C64's hardware sprites mean the learner doesn't need to understand screen memory layout first — enable a sprite, set its position, and it appears. The SID is introduced through satisfying sound effects from the earliest units, not as a theory lesson. By the end, the learner has a complete game that looks and sounds like a real C64 release.

---

### Game 2: Stealth-Puzzle

**Units:** 256 (8 phases × 32 units)
**Genre:** Stealth-puzzle platformer
**Inspired by:** Impossible Mission, Montezuma's Revenge
**Working title:** TBD

**Concept:** Infiltrate a facility. Search rooms, hack terminals, avoid robots, collect puzzle pieces, escape before time runs out. Large multi-screen rooms scroll as the player moves. Robot guards patrol on fixed paths but react when they detect the player. The SID creates an atmosphere of tension — humming machinery, echoing footsteps, the iconic synthesised speech.

**Skills taught:**
- VIC-II hardware scrolling ($D016 fine scroll, $D011 vertical)
- Smooth scrolling with colour RAM synchronisation
- Large scrolling rooms (wider than one screen)
- Raster interrupts for stable scroll and effects
- Large animated sprites (player somersault, robot patrol cycles)
- Room data structures and transitions
- Searchable objects (furniture, terminals) with randomised contents
- Puzzle piece collection and assembly mechanic
- Robot AI (patrol routes, detection radius, pursuit behaviour)
- Lift/elevator mechanics (multi-floor navigation)
- SID speech synthesis (using sampled or synthesised techniques)
- SID atmospheric music (tension, pursuit, discovery themes)
- Timer mechanic with SID countdown audio
- Character set design (room furniture, terminals, decorations)
- Password or checkpoint system
- Multiple difficulty levels affecting robot speed and placement

**Why here:** After the shooter's fast action, Impossible Mission demands a completely different tempo: deliberate movement, careful searching, tactical evasion. It teaches hardware scrolling through necessity — rooms are too large for a single screen — and uses the SID for atmosphere rather than action. The speech synthesis ("Stay a while. Stay forever.") is a technical showcase that also serves the game design. The learner emerges understanding scrolling, large sprites, room management, and the SID as a mood instrument.

---

### Game 3: Run 'n' Gun

**Units:** 512 (16 phases × 32 units)
**Genre:** Run 'n' gun
**Inspired by:** Turrican, Mega Turrican, Contra
**Working title:** TBD

**Concept:** A side-scrolling action game with 8-way movement, multiple weapon systems, and massive bosses across five themed worlds. The player runs, jumps, shoots, and grapples through expansive scrolling levels. This is the game that requires everything the C64 can do: smooth 8-directional scrolling, sprite multiplexing to fill the screen with enemies and projectiles, raster effects for visual polish, and a SID soundtrack that drives the action.

**Skills taught:**
- 8-way hardware scrolling (combined horizontal and vertical, $D011/$D016)
- Sprite multiplexing: displaying 16-32+ sprites using raster interrupts
  - Y-sorted sprite allocation
  - Double IRQ for cycle-exact timing
  - Flicker management and priority
  - Crunch bug avoidance
- Level streaming (loading new column/row data during scroll)
- Grappling hook physics (rope simulation, swing momentum)
- Vehicle/transformation sections (different physics model)
- Multiple weapon types with upgrade paths
- Large multi-sprite boss assemblies
- Boss AI with multiple phases and weak points
- Destructible terrain
- Parallax scrolling (multiple scroll speeds via raster splits)
- Advanced SID: multi-speed music, filter sweeps, digi-drum samples
- Memory management (fitting large levels, sprite data, music)
- World map or inter-level transitions
- Checkpoint system within levels
- 5 themed worlds with distinct enemy sets and visual styles

**Why here:** Turrican represents the peak of C64 development — a game that makes the hardware do things it wasn't designed for. Sprite multiplexing is THE C64 technique: the VIC-II supports 8 sprites, but Turrican fills the screen with dozens. This game teaches it not as an isolated trick but as a necessity — the gameplay demands more sprites than the hardware provides, so the learner builds the multiplexer. The 8-way scrolling, grappling physics, and vehicle sections ensure this is genuinely ambitious: a game that would have been sold in shops.

---

### Game 4: Capstone

**Units:** 512 (16 phases × 32 units)
**Genre:** Action-platformer with demo-scene polish (distinct from Games 1-3)
**Inspired by:** Creatures, Mayhem in Monsterland, Last Ninja series
**Working title:** TBD

**Concept:** A polished action game that combines platforming, combat, and visual spectacle across multiple zones. The game itself is a new genre — not a repeat of the run 'n' gun — but the real focus is on the production techniques that separated bedroom coders from commercial studios: custom fast loaders, direct drive programming, demo-scene visual effects, and professional multi-format distribution.

The finished game should look like a Thalamus or System 3 release: custom loading screen, fast loader with music, demo-scene title sequence, and flawless execution.

**Skills taught:**
- All techniques from Games 1-3 at mastery level
- Custom fast loader (replacing slow Kernal routines)
- Direct 1541 drive programming (drive's own 6502, serial protocol)
- IRQ loader (loading data while game runs, music during load)
- Demo-scene effects: FLD (Flexible Line Distance), DYCP (Different Y Character Positions), AGSP, tech-tech, raster bars
- Advanced SID: ring modulation, hard sync, combined waveforms, PWM
- 6581/8580 SID model detection and adaptation
- Loading screen display during tape/disk load
- Custom title sequence with demo-scene effects
- D64 disk image creation and layout
- Tape distribution (TAP format, turbo encoding)
- Dual distribution: same game on D64 and tape
- Multi-load architecture (loading levels from disk during play)
- Memory optimisation (banking, compression, overlays)
- Testing across configurations (PAL/NTSC, 6581/8580, 1541/1571)
- Professional credits, end sequence, and packaging

**Why last:** The capstone proves the learner can ship a product with professional production values. The game itself is ambitious, but the distinctive challenge is everything around the game: making it load fast, look spectacular during loading, adapt to different hardware revisions, and distribute on physical media. The demo-scene effects in the title sequence and transitions are not gratuitous — they demonstrate mastery of VIC-II timing at a level that commands respect.

---

## BASIC Gateway

The C64 BASIC V2 curriculum is maintained separately. See `/docs/curriculum/basic/commodore-64/commodore-64-basic-curriculum.md`.

---

## Changelog

- **v4.0 (2026-03-09):** Major restructure. Reduced from 16 to 4 assembly games. No-repetition rule across primary platforms. Every game inspired by a real commercial release. BASIC gateway restructured as 4 focused games. Previous 16-game curriculum preserved in game outline files for reference.
- **v3.0 (2026-01-18):** Initial 16-game curriculum.
