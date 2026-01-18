# Sinclair ZX Spectrum Curriculum

**Platform:** Sinclair ZX Spectrum
**Killer Feature:** Attribute colour system
**Games:** 16
**Total Units:** 2,048

---

## Overview

The ZX Spectrum curriculum teaches Z80 assembly programming through 16 complete games. The sequence begins with the attribute system - the Spectrum's defining characteristic that created its distinctive visual style - and progresses through scrolling, enemy AI, isometric projection, and advanced techniques until learners can produce commercial-quality games.

The Spectrum had no hardware sprites, no smooth scrolling, and a single-bit beeper for sound. Every impressive effect was achieved through software and creativity. This curriculum embraces those constraints, teaching learners to make the hardware sing through ingenuity.

By the final game, learners will have skills matching professional Spectrum developers of the late 1980s - equivalent to teams at Ultimate, Ocean, or Codemasters.

---

## Unit Structure

Games scale in unit count based on complexity:

| Games | Units Each | Total | Rationale |
|-------|-----------|-------|-----------|
| 1-8 | 128 | 1,024 | Foundation games - shooter, physics, platformer, exploration, strategy, maze, snake, Tetris |
| 9-10 | 64 | 128 | Foundation - core concepts |
| 11-13 | 128 | 384 | System-heavy - multiple complex systems |
| 14-15 | 128 | 256 | Advanced - new paradigms (isometric, epic action) |
| 16 | 256 | 256 | Capstone - commercial quality |
| **Total** | | **2,048** | |

Each game follows a phase structure (4-16 phases depending on length), with each phase containing 16 units.

---

## Game Sequence

### Game 1: Skyfire
**Units:** 128 (8 phases)
**Concept:** Fixed-screen space shooter. Player ship versus descending enemy waves. Immediate engagement from Unit 1.

**Skills taught:**
- Screen memory layout ($4000-$57FF)
- Attribute memory ($5800-$5AFF)
- INK, PAPER, BRIGHT, FLASH bits
- Keyboard input via ROM routines
- Player sprite drawing and movement
- Projectile spawning and management
- Enemy patterns and waves
- Multiple collision types
- Beeper sound effects (pitch variation)
- Sprite masking techniques
- Increasing difficulty curves
- High score display

**Why first:** A shooter gets something playable on screen immediately. Learners control a ship from Unit 2, shoot from Unit 3. The attribute system is learned through doing, not theory.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-zx-spectrum-skyfire.md`

---

### Game 2: Shatter
**Units:** 128 (8 phases)
**Concept:** Breakout clone polished to commercial quality. Paddle, ball, bricks - with physics that feel right, power-ups, and full audio.

**Skills taught:**
- Sub-cell movement (fixed-point pixel precision)
- Ball physics (velocity, angles, reflection, spin)
- Paddle control and angle influence
- Multiple brick types (hard, unbreakable)
- Power-up systems (extend, multi-ball, laser, catch)
- Custom fonts and graphics (UDG)
- Full beeper audio (music + SFX)
- High scores, difficulty settings, multiplayer
- 20 levels of varied brick patterns

**Why here:** After shooting, physics simulation introduces a fundamentally different movement model. 128 units allows proper exploration of angles, feel, and polish.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-zx-spectrum-shatter.md`

---

### Game 3: Cavern
**Units:** 128 (8 phases)
**Concept:** Single-screen platformer polished to commercial quality. In the Manic Miner tradition - platforms, hazards, collectibles, air supply, and pixel-perfect jumps.

**Skills taught:**
- Gravity and jump physics (velocity, acceleration, variable height)
- Platform collision detection (landing, head bonk, walls)
- Player animation (walk cycle, jump, death)
- Patrolling enemies with simple AI
- Crumbling platforms (timed hazards)
- Moving platforms (horizontal and vertical)
- Conveyor belts and environmental hazards
- Air supply mechanic (time pressure)
- Key collection and locked exits
- Power-ups (speed, invincibility)
- 20 levels with progressive difficulty
- Full beeper audio (music and SFX)

**Why here:** Builds on sub-cell movement from Shatter, applies physics to gravity instead of bouncing. This is the Spectrum's signature genre.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-zx-spectrum-cavern.md`

---

### Game 4: Chambers
**Units:** 128 (8 phases)
**Concept:** Flip-screen top-down exploration polished to commercial quality. Navigate rooms, collect items, avoid enemies, find the exit. In the Atic Atac tradition - the Spectrum's signature exploration genre.

**Skills taught:**
- 4-way top-down movement
- Room data structures and transitions
- Persistent state (collected items stay collected)
- Inventory systems (keys, items, weapons)
- Enemy chase AI with wall awareness
- Multiple enemy types (patrol, chase, ranged)
- Coloured keys and locked doors
- Hazards, traps, and environmental puzzles
- Multi-floor world design
- Full beeper audio (music and SFX)
- High scores, difficulty options, map screen

**Why here:** Multi-room structure and state management prepare learners for more complex AI in following games. 128 units allows full world-building.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-zx-spectrum-chambers.md`

---

### Game 5: Ink War
**Units:** 128 (8 phases)
**Concept:** Territory control strategy game polished to commercial quality. Player vs AI, taking turns to claim 8×8 attribute cells. Control the majority to win. A unique genre that turns the Spectrum's colour limitations into a feature.

**Skills taught:**
- Deep attribute system mastery (attribute = gameplay)
- Turn-based game loop (different paradigm)
- Strategic AI (greedy, minimax, personality)
- Position evaluation and scoring
- Multiple game modes (vs AI, two-player)
- Board size variants (6×6, 8×8, 10×10)
- Tournament and handicap modes
- Undo/replay functionality
- Save/load games
- Tutorial mode
- Statistics and achievements
- Full beeper audio (music and effects)

**Why here:** After 4 action games, learners explore strategic thinking. The attribute system becomes the core mechanic, turning a limitation into innovation.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-zx-spectrum-ink-war.md`

---

### Game 6: Chomp
**Units:** 128 (8 phases)
**Concept:** Pac-Man style maze game polished to commercial quality. Collect dots, avoid ghosts with distinct AI personalities, eat power pills to turn the tables.

**Skills taught:**
- Tile-based maze structure
- Constrained corridor movement (only turn at junctions)
- Four ghost AI personalities (Blinky, Pinky, Inky, Clyde)
- Chase/scatter mode state machines
- Frightened mode with ghost-eating chains
- Power-up state transitions
- Screen wrap-around tunnels
- Speed and difficulty progression
- Bonus fruit per level
- Cruise Elroy (Blinky speed-up)
- Intermission cut-scenes
- Full beeper audio (waka-waka, siren, death)
- High scores, demo mode
- Two-player mode

**Why here:** After strategic Ink War, learners return to real-time action with sophisticated enemy AI. Four distinct ghost behaviours create emergent gameplay.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-zx-spectrum-chomp.md`

---

### Game 7: Slither
**Units:** 128 (8 phases)
**Concept:** Classic snake game polished to commercial quality. Eat food, grow longer, avoid hitting yourself or walls. Teaches the ring buffer data structure.

**Skills taught:**
- Ring buffer for body segment storage
- Grid-based movement system
- Self-collision detection algorithms
- Growing entity management
- Food spawning and placement validation
- Speed progression with length
- Multiple maze layouts
- Level system with targets
- Power-up system (slow-down, ghost, shrink)
- Two-player alternating mode
- AI opponent with difficulty levels
- Wrap-around mode option
- Theme system (visual variants)
- Achievement and statistics tracking
- Beeper sound effects and music
- Demo/attract mode

**Why here:** After maze navigation in Chomp, learners tackle a different grid-based challenge. The ring buffer is a fundamental data structure used throughout game and audio programming.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-zx-spectrum-slither.md`

---

### Game 8: Stack
**Units:** 128 (8 phases)
**Concept:** Classic falling block puzzle polished to commercial quality. Tetris-style piece rotation, stacking, and line clearing with modern features like wall kicks, T-spins, and competitive multiplayer.

**Skills taught:**
- Piece rotation mathematics (4 orientations × 7 pieces)
- Timer-based falling mechanics
- Grid collision detection (can piece fit?)
- Line detection and efficient clearing
- Next piece preview and hold piece
- Ghost piece showing landing position
- Wall kick system (SRS-style)
- T-spin detection and bonus scoring
- Combo and back-to-back systems
- 7-bag randomiser for fair distribution
- Speed progression with level system
- Multiple game modes (Marathon, Sprint, Ultra)
- Two-player competitive with garbage lines
- AI opponent with difficulty levels
- Visual themes and customisation
- Achievement and statistics tracking
- Beeper sound effects
- 128K AY music (optional)
- Replay system
- Demo/attract mode

**Why here:** The falling blocks puzzle teaches rotation mathematics, grid algorithms, and polished game feel. Different from snake's ring buffer, this focuses on piece manipulation and clearing mechanics.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-zx-spectrum-stack.md`

---

### Game 9: Blitz
**Units:** 256 (16 phases)
**Concept:** Side-scrolling shooter on hardware with NO scroll support. Master THE hardest Spectrum technique: software pixel scrolling. Shift every byte, manage contended memory timing, and build a complete R-Type style shooter.

**Skills taught:**
- Software horizontal scrolling (character and pixel-level)
- Stack-based scroll tricks for maximum speed
- Unrolled and self-modifying scroll routines
- Contended memory timing management
- Attribute clash handling during scroll
- Tile map level streaming
- Parallax pseudo-layers via colour tricks
- Player and enemies in scrolling playfield
- Complex bullet patterns and enemy AI
- Five complete levels with distinct themes
- Five epic boss battles
- Weapon upgrade system with multiple types
- 128K AY sound enhancements
- Multiple game modes (Normal, Boss Rush, Endless)
- Two-player alternating mode
- Comprehensive optimisation techniques

**Why expanded:** Software scrolling is THE hardest Spectrum technique. Games like R-Type achieved legendary status for smooth scrolling on hardware with no scroll support. 256 units allows mastery of this platform-defining challenge.

**Detailed outline:** `/docs/curriculum/templates/full-game-outline-zx-spectrum-blitz.md`

---

### Game 10: Exodus
**Units:** 64 (4 phases)
**Concept:** Scrolling platformer. Cavern's mechanics in a larger, scrolling world.

**Skills taught:**
- Horizontal scrolling with platformer physics
- Camera following player
- Large level data structures
- Scrolling collision detection
- Enemies in scrolling world
- Checkpoints and progression
- Scrolling optimisation techniques
- Level streaming basics

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-10-exodus.md`

---

### Game 11: Redline
**Units:** 128 (8 phases)
**Concept:** Full vertical scrolling racer. Championship mode, multiple tracks, opponent AI, weather effects.

**Skills taught:**
- Vertical software scrolling
- Speed variation (accelerate, brake)
- Road rendering with curves
- Opponent AI with overtaking
- Collision at speed
- Track variety (city, country, night)
- Championship progression
- Weather effects (rain affects handling)
- **Tape loading basics** (standard loader)
- **TAP file creation**
- Pit stops and damage

**Why 128 units:** Full racing game with championships, multiple tracks, and opponent AI requires extensive content and systems.

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-11-redline.md`

---

### Game 12: Recoil
**Units:** 128 (8 phases)
**Concept:** Run 'n' gun action. Contra-style platforming with multi-directional shooting, multiple weapons, epic bosses.

**Skills taught:**
- Combining platformer and shooter mechanics
- Multi-directional firing (8-way)
- Shooting while moving/jumping
- Enemies that shoot back
- Weapon power-ups and switching
- Boss encounters with patterns
- Multiple stages with themes
- Two-player cooperative mode
- Continues and checkpoints
- Spread, laser, and homing weapons

**Why 128 units:** Combines two genres (platformer + shooter) with weapon variety and boss design.

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-12-recoil.md`

---

### Game 13: Knuckle Brawl
**Units:** 128 (8 phases)
**Concept:** Side-scrolling beat 'em up. Walk right, punch enemies, fight bosses. Streets of Rage/Final Fight territory.

**Skills taught:**
- Depth sorting (Y-axis layering)
- Melee combat mechanics (punches, kicks, throws)
- Combo systems
- Multiple enemy management
- Health and damage systems
- Walking "into" the screen (pseudo-3D)
- Stage progression
- Multiple playable characters
- Weapon pickups
- Boss encounters

**Why 128 units:** Depth sorting is complex, combat needs proper feel, multiple characters need balancing.

**Why here:** Depth sorting is the bridge to isometric. This game introduces layered drawing order.

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-13-knuckle-brawl.md`

---

### Game 14: Strafe
**Units:** 128 (8 phases)
**Concept:** Full vertical scrolling shooter. 1942-style planes, formations, weapons, bosses. 7+ stages.

**Skills taught:**
- Vertical scrolling (optimised)
- Formation enemy patterns
- Bullet hell patterns
- Power-up collection and weapon variety
- Boss encounters (multi-phase)
- Score chaining mechanics
- Multiple ship types
- **128K detection and AY sound**
- **Bank switching basics**
- Two-player simultaneous mode

**Why 128 units:** Full shooter with 7 stages, multiple weapons, bosses, and 128K support.

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-14-strafe.md`

---

### Game 15: Bastion
**Units:** 128 (8 phases)
**Concept:** Isometric exploration game. Knight Lore territory - the prestige Spectrum technique.

**Skills taught:**
- Isometric projection mathematics
- 3D coordinate systems
- Depth sorting (painter's algorithm)
- Movement in isometric space
- Collision in 3D
- Attribute clash management in isometric view
- Room-based world structure
- Object interaction
- Puzzle mechanics (push blocks, switches)
- 64+ rooms across multiple zones

**Why 128 units:** Isometric is a completely different paradigm requiring new mathematics, rendering, and collision approaches.

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-15-bastion.md`

---

### Game 16: Spectral Legacy
**Units:** 256 (16 phases)
**Concept:** Action-adventure epic. The capstone project combining everything learnt into a commercial-quality game.

**Skills taught:**
- All previous techniques at mastery level
- Large world design (100+ screens)
- Multiple gameplay mechanics integrated
- Story and progression elements
- Full save system
- **Turbo tape loader**
- **128K full support** (AY music, extra RAM)
- **+3 disk support** (optional)
- **TZX file creation** with loading screen
- Professional presentation
- Polish and game feel

**Why 256 units:** The capstone integrates all 15 previous games' skills plus professional distribution and 128K features.

**Why last:** The curriculum ends with learners demonstrating full command of the machine. "Spectral" nods to the Spectrum; "Legacy" is what they've built.

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-16-spectral-legacy.md`

---

## Sinclair BASIC Gateway (Optional)

For learners wanting a gentler introduction before assembly, an optional Sinclair BASIC curriculum is available. This 512-unit track (8 games × 64 units) teaches programming fundamentals through complete games before tackling Z80.

**Games:** Guess Quest, Pixel Rain, Paddle Battle, Dungeon Explorer, Snake Spectrum, Asteroid Dodge, Pattern Match, Platform Jump

**Skills taught:**
- Sinclair BASIC fundamentals (PRINT, INPUT, IF/THEN/ELSE)
- Graphics commands (PLOT, DRAW, CIRCLE)
- User-Defined Graphics (UDGs)
- Real-time input with INKEY$
- Arrays and game state
- BASIC's limits - why assembly is needed

The BASIC gateway is optional. Learners can start directly at Game 1 (Ink War) with no BASIC knowledge required. The gateway exists for those who prefer building foundational programming concepts before diving into assembly.

See `/docs/curriculum/sinclair-zx-spectrum-basic-curriculum.md` for full details.

---

## Skill Progression

| Games | Focus | Era Equivalent |
|-------|-------|----------------|
| 1-6 | Single-screen fundamentals | 1982-1984 |
| 7-8 | Grid-based and puzzle games | 1983-1985 |
| 9-10 | Scrolling introduction | 1984-1986 |
| 11-13 | Complex multi-system games | 1986-1988 |
| 14-15 | Advanced paradigms | 1988-1990 |
| 16 | Commercial quality | 1990-1993 |

By Game 16, learners produce work comparable to late-era commercial releases like Midnight Resistance (1990), Navy Moves (1988), and Head Over Heels (1987).

---

## Distribution Skills Progression

| Game | Skills Introduced |
|------|------------------|
| 11 (Redline) | Standard tape loading, TAP file creation |
| 14 (Strafe) | 128K detection, AY sound, bank switching |
| 16 (Spectral Legacy) | Turbo loader, full 128K, TZX with loading screen, +3 disk |

---

## 128K Support

Later games introduce 128K Spectrum features:

| Feature | Introduced |
|---------|-----------|
| 128K detection | Game 14 (Strafe) |
| AY-3-8912 sound | Game 14 (Strafe) |
| Bank switching | Game 14 (Strafe) |
| Full 128K game | Game 16 (Spectral Legacy) |

Games 1-13 target 48K compatibility. Games 14+ include 128K enhancements with 48K fallback.

---

## Platform Context

**Hardware:**
- **CPU:** Zilog Z80 @ 3.5 MHz
- **RAM:** 48K (16K on early models, 128K on later)
- **Display:** 256×192 pixels, 32×24 attribute cells
- **Colours:** 8 colours, each with normal/bright variant (15 total + black)
- **Sound:** 1-bit beeper (128K models add AY-3-8912 chip)
- **Storage:** Cassette tape (+3 models have disk)

**The Attribute System:**
The Spectrum's display divides the screen into 8×8 pixel cells. Each cell has one attribute byte controlling:
- INK (foreground colour, 3 bits)
- PAPER (background colour, 3 bits)
- BRIGHT (intensity, 1 bit)
- FLASH (alternating, 1 bit)

This creates the infamous "colour clash" when differently-coloured objects overlap within an 8×8 cell. Managing this constraint is central to Spectrum development.

**No Hardware Sprites:**
Unlike the C64, the Spectrum has no hardware sprites. All moving graphics are software-rendered, making efficient drawing routines essential.

**No Hardware Scrolling:**
Smooth scrolling requires shifting screen memory in software - an expensive operation that defined what was possible on the platform.

---

## Optional Enhancement Versions

Select games have optional enhanced versions for expanded hardware. Not every game warrants enhancement - these target games where the additional capabilities meaningfully improve the experience.

### 128K Enhancements

For games that benefit from AY sound and extra RAM:

| Game | Enhancement Focus |
|------|-------------------|
| TBD | AY soundtrack, extra levels |

128K enhancements add AY music, sound effects, and potentially additional content using banked RAM. These are period-authentic enhancements (128K released 1985).

### ZX Spectrum Next Enhancements

For games that benefit from modern hardware capabilities:

| Game | Units | Enhancement Focus |
|------|-------|-------------------|
| 9-16 (select) | 32-128 | Hardware sprites, copper, 256 colours, Z80N |

Next enhancements follow the Amiga AGA model - separate versions that showcase the enhanced hardware while the main game remains 48K compatible.

**Structure (when implemented):**
- Games 9-14 Next: 32 units each
- Game 15 Next: 64 units
- Game 16 Next: 128 units

See `/docs/plans/future-expansion-tracks.md` for full details.

---

## Version History

- **3.11 (2026-01-18):** Expanded Game 9 (Blitz) to 256 units with software scrolling mastery. Total now 2,240 units.
- **3.10 (2026-01-18):** Expanded Game 8 (Stack) to 128 units with T-spins, competitive multiplayer, and modern puzzle features. Total now 2,048 units.
- **3.9 (2026-01-18):** Expanded Game 7 (Slither) to 128 units with ring buffer data structure and AI opponent. Total now 1,984 units.
- **3.8 (2026-01-18):** Expanded Game 6 (Chomp) to 128 units with four distinct ghost AI personalities. Total now 1,920 units.
- **3.7 (2026-01-18):** Expanded Game 5 (Ink War) to 128 units with minimax AI and strategy polish. Total now 1,856 units.
- **3.6 (2026-01-18):** Expanded Game 4 (Chambers) to 128 units with full Atic Atac-style exploration. Total now 1,792 units.
- **3.5 (2026-01-18):** Expanded Game 3 (Cavern) to 128 units with full Manic Miner-style platformer features. Total now 1,728 units.
- **3.4 (2026-01-18):** Expanded Game 2 (Shatter) to 128 units for full physics polish. Total now 1,664 units.
- **3.3 (2026-01-18):** Reordered games per skill tree analysis. Shatter now Game 2 (sub-cell physics). Cavern now Game 3 (platforming). Ink War moved to Game 5 (requires strategic AI experience). See `/docs/curriculum/SKILL-TREES.md`.
- **3.2 (2026-01-18):** Restructured Game 1. Skyfire (shooter) now first game at 128 units for immediate engagement. Total now 1,600 units.
- **3.1 (2026-01-07):** Added optional enhancement versions section (128K and Next). Updated BASIC gateway reference to 512-unit curriculum.
- **3.0 (2025-01-07):** Expanded to 1,536 units. Games 1-10 at 64 units, Games 11-15 at 128 units, Game 16 at 256 units. Added tape loading, 128K support, distribution skills.
- **2.0 (2025-11-26):** Complete rewrite. Replaced phases/tiers/lessons with games model.
- **1.0 (2025-01-15):** Original 4,096-lesson curriculum.
