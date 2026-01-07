# Sinclair ZX Spectrum Curriculum

**Platform:** Sinclair ZX Spectrum
**Killer Feature:** Attribute colour system
**Games:** 16
**Total Units:** 1,536

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
| 1-10 | 64 | 640 | Foundation - core concepts |
| 11-13 | 128 | 384 | System-heavy - multiple complex systems |
| 14-15 | 128 | 256 | Advanced - new paradigms (isometric, epic action) |
| 16 | 256 | 256 | Capstone - commercial quality |

Each game follows a phase structure (4-16 phases depending on length), with each phase containing 16 units.

---

## Game Sequence

### Game 1: Ink War
**Units:** 64 (4 phases)
**Concept:** Territory control game where the attribute system *is* the gameplay. Player vs AI, taking turns to claim 8×8 attribute cells. Control the majority to win.

**Skills taught:**
- Screen memory layout ($4000-$57FF)
- Attribute memory ($5800-$5AFF)
- INK, PAPER, BRIGHT, FLASH bits
- Keyboard input via ROM routines
- Game state management
- Simple AI decision-making
- Turn-based game loop
- Colour clash awareness

**Why first:** The attribute system is what made Spectrum games look distinctly Spectrum. Starting here teaches the core constraint that shapes everything else.

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-01-ink-war.md`

---

### Game 2: Shatter
**Units:** 64 (4 phases)
**Concept:** Breakout clone with polish focus. Paddle, ball, bricks - with custom font, smooth animation, and audio feedback.

**Skills taught:**
- Custom font design and installation
- Smooth sub-cell movement (pixel precision)
- Frame-based timing and delta movement
- Collision detection (walls, paddle, bricks)
- Bounce angles and reflection physics
- Brick destruction with visual effects
- Beeper sound design
- Power-up systems
- Level progression

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-02-shatter.md`

---

### Game 3: Skyfire
**Units:** 64 (4 phases)
**Concept:** Fixed-screen space shooter. Player ship versus descending enemy waves.

**Skills taught:**
- Player sprite drawing and movement
- Projectile spawning and management
- Enemy patterns and waves
- Multiple collision types
- Beeper sound effects (pitch variation)
- Sprite masking techniques
- Increasing difficulty curves
- High score display

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-03-skyfire.md`

---

### Game 4: Cavern
**Units:** 64 (4 phases)
**Concept:** Single-screen platformer in the Manic Miner tradition. Platforms, hazards, collectibles.

**Skills taught:**
- Gravity and falling physics
- Jump physics (velocity, arc, landing)
- Platform collision detection
- Player animation (walk cycle, jump frame)
- Hazards and enemies (crumbling floors, patrolling enemies)
- Level completion logic
- Air supply mechanic
- Multiple levels

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-04-cavern.md`

---

### Game 5: Chambers
**Units:** 64 (4 phases)
**Concept:** Flip-screen top-down exploration. Navigate rooms, collect items, avoid enemies. Atic Atac territory.

**Skills taught:**
- 4-way movement
- Room data structures
- Screen transitions (flip-screen)
- Persistent state across rooms
- Simple inventory (keys, items)
- Enemies with chase behaviour
- Multiple room types
- Locked doors and key colours

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-05-chambers.md`

---

### Game 6: Chomp
**Units:** 64 (4 phases)
**Concept:** Pac-Man style maze game. Collect dots, avoid ghosts, eat power pills to turn the tables.

**Skills taught:**
- Tile-based maze structure
- Constrained corridor movement
- Enemy AI with personality (scatter, chase modes)
- Power-ups that change game state
- Wrap-around screen edges
- Levels and speed progression
- Ghost respawn mechanics
- Bonus fruit spawning

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-06-chomp.md`

---

### Game 7: Slither
**Units:** 64 (4 phases)
**Concept:** Snake game. Eat food, grow longer, don't hit yourself.

**Skills taught:**
- Grid-based movement
- Growing entity management (linked list concepts)
- Self-collision detection
- Food spawning
- Increasing difficulty through length
- Tight game loop optimisation
- Obstacle mazes
- Speed progression

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-07-slither.md`

---

### Game 8: Stack
**Units:** 64 (4 phases)
**Concept:** Falling blocks puzzle. Tetris-style piece rotation, stacking, and line clearing.

**Skills taught:**
- Piece rotation (4 orientations per piece)
- Falling on a timer
- Grid collision (can piece fit?)
- Line detection and clearing
- Next piece preview
- Speed increases over time
- Scoring with combos
- Wall kick mechanics

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-08-stack.md`

---

### Game 9: Blitz
**Units:** 64 (4 phases)
**Concept:** Side-scrolling shooter. Horizontal scroll, shoot enemies, navigate terrain.

**Skills taught:**
- Software horizontal scrolling
- Tile map level data
- Player in scrolling playfield
- Terrain collision
- Enemies tied to scroll position
- Multiple stage sections
- Optimised screen shifting
- Background/foreground layers

**Why here:** The Spectrum has no hardware scrolling - this is all software, shifting bytes. A fundamental skill for larger games.

**Detailed outline:** `/docs/plans/sinclair-zx-spectrum/game-09-blitz.md`

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

## Sinclair BASIC Track (Optional)

For learners wanting a different approach, an optional Sinclair BASIC track is available. BASIC is better suited to certain game types - particularly text adventures where string handling matters more than speed.

### BASIC Game 1: Caverns of Dorath
**Units:** 8
**Concept:** Text adventure. Explore caverns, solve puzzles, find treasure. Parser-based interaction.

**Skills taught:**
- Sinclair BASIC fundamentals
- String handling and INPUT$
- IF/THEN logic
- Arrays for room and inventory data
- PRINT and CLS for display
- Game state management

### BASIC Game 2: Mindbreaker
**Units:** 8
**Concept:** Mastermind-style code breaker. Deduce the hidden code through logic and clues.

**Skills taught:**
- Array manipulation
- Logic and deduction algorithms
- Feedback systems
- Game loop in BASIC
- Difficulty progression
- Why assembly matters for speed

The BASIC track is optional. Learners can start directly at Game 1 (Ink War) with no BASIC knowledge required.

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

## Future Expansion Tracks

After completing the core curriculum, optional expansion tracks are available:

- **ZX Spectrum Next:** Hardware sprites, copper, DMA, enhanced graphics
- **128K Deep Dive:** Advanced AY programming, full bank usage
- **Modern Tooling:** VS Code workflows, automated testing

See `/docs/plans/future-expansion-tracks.md` for details.

---

## Version History

- **3.0 (2025-01-07):** Expanded to 1,536 units. Games 1-10 at 64 units, Games 11-15 at 128 units, Game 16 at 256 units. Added tape loading, 128K support, distribution skills.
- **2.0 (2025-11-26):** Complete rewrite. Replaced phases/tiers/lessons with games model.
- **1.0 (2025-01-15):** Original 4,096-lesson curriculum.
