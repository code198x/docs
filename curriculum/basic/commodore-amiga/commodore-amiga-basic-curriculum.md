# Commodore Amiga BASIC Curriculum

**Platform:** Commodore Amiga
**Languages:** AMOS Professional, Blitz Basic 2
**Tracks:** 2
**Total Games:** 8 (4 AMOS + 4 Blitz)
**Total Units:** 512 (8 × 64)

---

## Overview

The Amiga BASIC curriculum has two tracks: AMOS and Blitz Basic. Both are real game development languages — commercial titles shipped in each — but they represent fundamentally different approaches to the same hardware.

**AMOS** is friendly and immediate. `Bob 1, 100, 100, 1` puts a sprite on screen. `Screen Offset 0, X, 0` scrolls the display. AMOS wraps hardware complexity in accessible commands, making it ideal for learners who want visual results quickly.

**Blitz Basic** is compiled and fast. It produces executables that rival hand-written C. Where AMOS abstracts the hardware, Blitz exposes more of it. Games like Worms and Skidmarks shipped as Blitz Basic — proof that "BASIC" doesn't mean "slow."

The two tracks teach different things: AMOS teaches game design thinking with immediate feedback. Blitz teaches performance-aware programming that bridges toward assembly. Neither is a prerequisite for the other or for the assembly track.

---

## Why Both?

| Factor | AMOS | Blitz Basic |
|--------|------|-------------|
| **Speed** | Interpreted (with compiler option) | Compiled — fast executables |
| **Ease** | Gentler, more forgiving | Steeper, more structured |
| **Hardware access** | Abstracted (BOB, SCREEN commands) | More direct (memory access, custom types) |
| **Culture** | Hobbyist, learning, prototyping | Performance, commercial games |
| **Commercial proof** | Guardian, Scorched Tanks, Ultimate Soccer Manager | Worms, Skidmarks, Super Skidmarks |
| **Bridge to assembly** | Indirect — same concepts, different interface | Direct — similar memory model and performance thinking |

Teaching both shows that there is no single "right" tool — different problems reward different approaches.

---

## Part 1: AMOS Track (4 Games)

### Structure

| Game | Units | Role |
|------|-------|------|
| 1 | 64 | Ricochet — bouncing sprites game (immediate visuals) |
| 2 | 64 | Conduit — pipe-routing puzzle with mouse control |
| 3 | 64 | Sidewinder — scrolling game using screen commands |
| 4 | 64 | TBD — complete game with MOD music |
| **Total** | **256** | |

Each game has 4 phases of 16 units. Each unit is 60-120 minutes. Each game targets under 500 lines of AMOS.

---

### AMOS Game 1: Ricochet

**Units:** 64 (4 phases × 16 units)
**Genre:** Sprite-based action
**Inspired by:** AMOS demo programs, simple arcade games

**Concept:** A game built around moving BOBs — sprites that bounce, collide, and interact. AMOS makes this immediate: `Bob 1, X, Y, Image` puts a sprite on screen. The learner starts with a visual demo (sprites bouncing off screen edges) and turns it into a game by adding rules, scoring, and player control. Catch falling objects, dodge bouncing hazards, or shoot moving targets — the specific game design emerges from the mechanics.

**Skills taught:**
- AMOS environment and editor
- Screen setup (SCREEN OPEN, mode, dimensions)
- BOB display and movement (Bob, Bob Off, X Bob, Y Bob)
- Sprite sheet loading (LOAD, SPRITE$, banks)
- Collision detection (Bob Col, Sprite Col)
- Joystick reading (Joy, Jleft, Jright, Jup, Jdown, Fire)
- Game loop structure (DO...LOOP, WAIT VBL)
- Variables, arrays, conditionals, loops
- Score display (TEXT, LOCATE, PRINT)
- Difficulty progression (speed, spawn rate)
- Title screen and game-over
- WAIT VBL for frame synchronisation

**Why first:** AMOS's strength is immediate visual results. `Bob 1, 100, 100, 1` — there's a sprite. Move it, bounce it, collide it. The game comes together visually from the first unit, and AMOS handles the hardware complexity (bitplane allocation, DMA timing, Blitter cookie-cut) invisibly. The learner focuses on game design, not hardware registers.

---

### AMOS Game 2: Conduit

**Units:** 64 (4 phases × 16 units)
**Genre:** Point-and-click / mouse-driven
**Inspired by:** AMOS utility programs, simple point-and-click games

**Concept:** A game that uses the Amiga's mouse as the primary input — click targets, drag objects, draw paths, select tools. The Amiga was a mouse-first computer; AMOS exposes mouse state directly. The game could be a puzzle (arrange pieces), a strategy game (place defences), or a creative tool turned game (draw shapes that come alive). The mouse changes how the player thinks about interaction.

**Skills taught:**
- Mouse reading (X Mouse, Y Mouse, Mouse Key, Mouse Click)
- Zone detection (ZONE, screen regions)
- Drag-and-drop mechanics (track mouse state, move objects)
- Screen zones and clickable areas
- Cursor graphics (custom mouse pointer via sprite)
- Menu and button design
- AMOS drawing commands (INK, BOX, BAR, CIRCLE, DRAW, PAINT)
- Screen management (multiple screens, screen priority)
- Sound effects via SAM (AMOS speech synthesiser) and SAMPLE PLAY
- State machines (tool selected → action on click → result)
- Undo/redo via state arrays
- File I/O (saving/loading game state)

**Why here:** The Amiga has a mouse — use it. Most home computers of the era were joystick-first; the Amiga's mouse changes what kinds of games are natural. After the joystick-driven action of Game 1, a mouse-driven game teaches a completely different interaction model. AMOS's zone detection and drawing commands make this accessible; the assembly track's equivalent would require significant Intuition library work.

---

### AMOS Game 3: Sidewinder

**Units:** 64 (4 phases × 16 units)
**Genre:** Side-scrolling action
**Inspired by:** Simple Amiga platformers and shooters

**Concept:** A side-scrolling game where the background moves and enemies appear from the right. The player navigates, avoids, or shoots. AMOS's SCREEN OFFSET command provides hardware scrolling — the same scroll registers the assembly track programs directly. The learner sees the relationship between AMOS commands and hardware behaviour: `Screen Offset 0, X, 0` writes to BPLxPT and BPLCON1.

**Skills taught:**
- Hardware scrolling via SCREEN OFFSET
- Tile-based background design
- Level data in arrays (tile map, enemy spawn points)
- Enemy spawning and despawning (off-screen management)
- Background and foreground layers (dual playfield via AMOS DUAL)
- Parallax scrolling (multiple screen offsets at different speeds)
- Camera and viewport concepts
- Combining scrolling with BOB sprites
- Level streaming (updating tile data as the view moves)
- AMOS music playback (TRACK LOAD, TRACK PLAY for MOD files)
- Sound effects mixed with music (SAMPLE PLAY on specific channels)
- Performance awareness (when AMOS starts to struggle)

**Why here:** Scrolling reveals the Amiga's hardware architecture. SCREEN OFFSET isn't a software trick — it's telling Agnus where to start reading bitplane data. The learner sees the connection between AMOS commands and hardware registers, which makes the assembly track's direct register programming feel like a natural progression. Parallax via dual playfield is the same technique that Shadow of the Beast uses — AMOS just wraps it in friendlier syntax.

---

### AMOS Game 4: TBD

**Units:** 64 (4 phases × 16 units)
**Genre:** Complete polished game
**Inspired by:** Commercial AMOS games (Guardian, Scorched Tanks)

**Concept:** A complete, polished game combining all previous skills with MOD music playback. Multiple screens (title, options, game, high scores, credits), sample sound effects mixed with music, difficulty progression, and a professional presentation. The game should feel like something you'd find on an Amiga Power coverdisk — not a demo, a real game.

**Skills taught:**
- MOD music playback (TRACK LOAD, TRACK PLAY, TRACK STOP)
- Sound effect mixing (allocating channels between music and SFX)
- Multiple game screens (title, options, game, scores)
- Screen transitions (fades, wipes via palette manipulation)
- High score table with name entry and persistence
- Difficulty settings and game options
- AMOS compiler (creating standalone executables)
- Disk-based distribution (creating bootable ADF)
- Professional presentation (attract mode, credits)
- Performance profiling (where AMOS hits its ceiling)
- What assembly would do differently (and faster)

**Why last:** The AMOS track's peak. The game demonstrates everything AMOS can do — and honestly shows where it struggles. MOD music playback and sound mixing are effortless (AMOS handles Paula DMA); real-time action with many BOBs starts to stutter. The compiled executable runs from a bootable ADF, just like the assembly track's output. The learner has a complete game to show for the track, and a clear understanding of why the assembly track exists.

---

## Part 2: Blitz Basic Track (4 Games)

### Structure

| Game | Units | Role |
|------|-------|------|
| 1 | 64 | Flashpoint — fast action game (compiled speed) |
| 2 | 64 | Gridlock — structured game with data modelling |
| 3 | 64 | Craterfall — pushing hardware with compiled code |
| 4 | 64 | TBD — full production game |
| **Total** | **256** | |

Each game has 4 phases of 16 units. Each unit is 60-120 minutes. Each game targets under 500 lines of Blitz Basic.

---

### Blitz Game 1: Flashpoint

**Units:** 64 (4 phases × 16 units)
**Genre:** Fast-paced arcade action
**Inspired by:** Simple Blitz demos, arcade shooters

**Concept:** A fast-paced action game that demonstrates compiled Blitz speed from the start. Where AMOS Game 1 was about getting sprites on screen easily, this game is about getting them on screen fast. Many objects, smooth movement, responsive controls. The compiled executable runs noticeably faster than equivalent AMOS code — same hardware, different tool, different result.

**Skills taught:**
- Blitz Basic environment and compiler
- Bitmap and shape loading (LoadBitmap, LoadShape)
- Display setup (BitMap, Slice, Show)
- Shape blitting (Blit, BBlit — Blitter-based drawing)
- Input handling (Joyb, Joyx, Joyy for joystick)
- Game loop with VWait (vertical blank synchronisation)
- Variables and basic control flow
- Compiled vs. interpreted: measurable speed difference
- Object management (arrays of positions, velocities)
- Collision detection (ShapeHit, pixel-based)
- Score and display management
- Frame-rate-aware design (consistent speed on different Amigas)

**Why first:** Blitz's selling point is speed. The first game should demonstrate that immediately — more objects, smoother movement, faster response than AMOS could manage. The learner sees the same hardware producing different results depending on the tool. The compiler changes what's possible.

---

### Blitz Game 2: Gridlock

**Units:** 64 (4 phases × 16 units)
**Genre:** Strategy or simulation
**Inspired by:** Management games, structured Blitz programs

**Concept:** A game that benefits from structured data — custom types (NEWTYPE) for game entities, linked lists for dynamic collections, structured game state. A tower defence, a simple management game, or a unit-based tactics game. The gameplay is less about reflexes and more about systems interacting. Blitz's custom types make this natural where AMOS would need parallel arrays.

**Skills taught:**
- NEWTYPE for custom data structures (entity, projectile, wave)
- Linked lists and dynamic allocation
- Structured program design (procedures, local variables)
- Entity-component thinking (position, velocity, health, state per object)
- Pathfinding basics (grid-based, A* introduction)
- Mouse input (MouseX, MouseY, MouseButton)
- UI rendering (menus, buttons, info panels)
- Game state machines (setup → play → pause → game-over)
- File I/O for save/load
- Sound via Blitz audio commands
- Separation of game logic from rendering

**Why here:** Blitz's custom types (NEWTYPE/End NEWTYPE) enable structured programming that AMOS can't match. This game teaches data modelling — thinking about entities as structures with properties and behaviours. The approach is closer to how professional C and assembly games organise their data, making Blitz a genuine bridge to systems-level thinking.

---

### Blitz Game 3: Craterfall

**Units:** 64 (4 phases × 16 units)
**Genre:** Performance-intensive action (many objects, particles, scrolling)
**Inspired by:** Worms, Skidmarks — games that pushed Blitz to its limits

**Concept:** A game designed to stress the hardware: many simultaneous objects, particle effects, scrolling backgrounds, real-time physics. A destruction game (terrain deformation like Worms), a racing game (many cars, track scrolling), or a swarm game (hundreds of entities). The compiled Blitz code handles workloads that would crush AMOS.

**Skills taught:**
- Bitmap manipulation (direct pixel access, terrain modification)
- Particle systems (spawn, update, expire — hundreds of objects)
- Optimised Blitter usage (QBlit, direct Blitter access)
- Double buffering (draw to back buffer, swap)
- Scrolling with bitmap manipulation
- Physics simulation (gravity, bounce, friction)
- Performance profiling and optimisation
- Memory management (pre-allocation, object pools)
- Copper effects via Blitz copper commands
- Advanced collision (bitmap overlap, per-pixel)
- Terrain deformation (modifying the playfield bitmap — Worms technique)
- Why this works compiled but wouldn't interpreted

**Why here:** This is where Blitz proves its commercial pedigree. Worms was written in Blitz Basic — terrain deformation, physics, particles, AI, all running smoothly. This game teaches the same techniques: bitmap manipulation for destructible terrain, physics for projectiles, particle effects for explosions. The learner sees Blitz operating at a level that rivals hand-written assembly for many workloads.

---

### Blitz Game 4: TBD

**Units:** 64 (4 phases × 16 units)
**Genre:** Complete polished game
**Inspired by:** Commercial Blitz releases (Worms, Skidmarks, Super Stardust)

**Concept:** A complete, polished game at commercial quality. Multiple game modes, MOD music, sound effects, save/load, options screen, attract mode. The compiled executable boots from ADF and runs on any Amiga. The game should feel like a coverdisk release — something a magazine would be proud to include. This is the Blitz track's proof that BASIC can produce professional results.

**Skills taught:**
- MOD music integration (module loading, channel allocation)
- Sound effect management (priority, channel stealing)
- Multiple game modes (campaign, versus, time trial)
- Configuration and options (persistent settings)
- Standalone executable creation
- Bootable ADF creation
- System-friendly startup/shutdown (OS takeover and restore)
- Attract mode and demo replay
- Credits and professional presentation
- Testing across Amiga models (A500, A1200 — chip/fast RAM differences)
- Distribution considerations (ADF, WHDLoad, hard disk install)
- What assembly would add (and when it's not needed)

**Why last:** The Blitz track's capstone demonstrates that "BASIC" is not a limitation — it's a choice. The compiled executable is indistinguishable from a C or assembly program to the end user. The learner has produced a game that boots from disk, plays music, handles input, and looks professional. The assembly track remains available for those who want deeper hardware control, but Blitz proves it's not always necessary.

---

## Changelog

- **v4.0 (2026-03-09):** Major restructure. Reduced from 8 to 4 games per track. Standardised to 64 units per game. AMOS and Blitz tracks maintained as distinct curricula. Each game targets under 500 lines. Previous 8-game curriculum preserved in game outline files for reference.
- **v3.0 (2026-01-18):** Initial 8-game AMOS + 8-game Blitz curriculum.
