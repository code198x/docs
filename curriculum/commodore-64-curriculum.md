# Commodore 64 Assembly Curriculum

**Platform:** commodore-64
**Phases:** 0-8 (Phase 0 BASIC is the recommended starting point)
**Total Tiers:** 128 (16 per phase, 2^7)
**Lessons Per Tier:** 32 (2^5)
**Total Lessons:** 4,096 (2^12)

## Overview

This curriculum teaches 6510 assembly programming on the Commodore 64 through **spiral learning** and **genre diversity**. Each phase contains 16 complete games spanning different genres. Learners build playable games quickly (by Lesson 15-20 of each tier), then deepen understanding through polish and refinement.

The same genres are revisited across phases at increasing complexity, allowing learners to master techniques progressively while maintaining variety and engagement.

By Phase 8 completion, learners will produce games rivaling the technical sophistication of titles like Turrican II (1991) and Mayhem in Monsterland (1993).

## Curriculum Philosophy

### Spiral Learning
- **First pass:** Quick implementation (Lessons 1-20 = playable game)
- **Second pass:** Understanding and refinement (Lessons 21-32)
- **Later phases:** Same genre, higher complexity, deeper mastery

### Genre Progression
Each genre appears across multiple phases:
- **Phase 1:** Foundation version (1982-1983 quality)
- **Phase 4:** Intermediate version (1985-1987 quality)
- **Phase 8:** Master version (1991-1993 quality)

### Lesson-Level Pacing
- **Lesson 1:** Concept introduction
- **Lessons 2-3:** Interactive demo (move something, see results!)
- **Lessons 15-20:** **PLAYABLE GAME**
- **Lessons 21-32:** Polish, features, deeper understanding

---

## Phase 1: Foundation (1982-1983)

**Commercial Quality Era:** Early arcade ports and simple original games
**Example Games:** Choplifter (1982), Pac-Man (1983), Wizard of Wor (1983)
**Overall Goal:** Build 16 simple single-screen games demonstrating core techniques

### Tier 1: Space Shooter (Lessons 1-32)
**Game:** Single-screen space shooter (player ship vs enemies)
**Playable by:** Lesson 15-20
**Key Techniques:** Basic sprites, movement, shooting, collision, score
**Lessons 1-3:** Hello World → Border color control → Character on screen moving
**Lessons 4-10:** Sprite definition, display, keyboard/joystick input, movement
**Lessons 11-15:** Bullets, enemies, collision detection
**Lessons 16-20:** **PLAYABLE** - Score, lives, game over
**Lessons 21-32:** Sound effects, animation, polish, multiple enemy types

### Tier 2: Maze Chase (Lessons 33-64)
**Game:** Pac-Man style maze game
**Playable by:** Lesson 47-50
**Key Techniques:** Character graphics, maze rendering, AI pathfinding, pellets
**Spiral concepts:** Movement (in maze context), collision (with walls/ghosts), score
**Lessons 33-40:** Character graphics, maze drawing
**Lessons 41-50:** Player movement, pellet collection, **PLAYABLE**
**Lessons 51-64:** Ghost AI, power pellets, lives, polish

### Tier 3: Simple Platformer (Lessons 65-96)
**Game:** Single-screen platform jumper
**Playable by:** Lesson 79-82
**Key Techniques:** Jump physics, gravity, platform collision, enemies
**Spiral concepts:** Sprites, collision (platforms), movement (with physics)
**Lessons 65-72:** Platform rendering, player sprite
**Lessons 73-82:** Jump mechanics, gravity, **PLAYABLE**
**Lessons 83-96:** Enemies, hazards, collectibles, lives

### Tier 4: Breakout (Lessons 97-128)
**Game:** Brick-breaking game
**Playable by:** Lesson 111-114
**Key Techniques:** Ball physics, paddle control, brick destruction, angles
**Spiral concepts:** Collision (ball/brick/paddle), movement (ball trajectory)
**Lessons 97-104:** Paddle, ball, basic physics
**Lessons 105-114:** Brick grid, collision, **PLAYABLE**
**Lessons 115-128:** Power-ups, levels, ball spin, polish

### Tier 5: Fixed Shooter (Lessons 129-160)
**Game:** Space Invaders style (stationary player, waves of enemies)
**Playable by:** Lesson 143-146
**Key Techniques:** Enemy formation, wave patterns, shields, descending enemies
**Spiral concepts:** Shooting (enemy bullets), collision, formation movement
**Lessons 129-136:** Player cannon, enemy grid
**Lessons 137-146:** Enemy movement, shooting, **PLAYABLE**
**Lessons 147-160:** Shields, UFO, wave progression, difficulty

### Tier 6: Collect-Em-Up (Lessons 161-192)
**Game:** Navigate arena collecting items, avoid hazards
**Playable by:** Lesson 175-178
**Key Techniques:** Item spawning, timer, hazard patterns, combo scoring
**Spiral concepts:** Movement, collision, score (with bonuses)
**Lessons 161-168:** Arena, player, basic items
**Lessons 169-178:** Collection, hazards, timer, **PLAYABLE**
**Lessons 179-192:** Multiple item types, combos, difficulty scaling

### Tier 7: Block Puzzle (Lessons 193-224)
**Game:** Falling block puzzle (Columns/Tetris style)
**Playable by:** Lesson 207-210
**Key Techniques:** Grid system, piece rotation, line clearing, drop mechanics
**Spiral concepts:** Character graphics (puzzle pieces), game logic
**Lessons 193-200:** Grid rendering, piece display
**Lessons 201-210:** Piece movement, rotation, stacking, **PLAYABLE**
**Lessons 211-224:** Line clearing, score, speed increase, next piece

### Tier 8: Scrolling Shooter (Lessons 225-256)
**Game:** Horizontal scrolling space shooter
**Playable by:** Lesson 239-242
**Key Techniques:** Basic horizontal scrolling, enemy waves, power-ups
**Spiral concepts:** Shooting, collision, scrolling introduction
**Lessons 225-232:** Scrolling background basics
**Lessons 233-242:** Player, enemies, shooting, **PLAYABLE**
**Lessons 243-256:** Power-ups, parallax hints, boss, polish

### Tier 9: Top-Down Racer (Lessons 257-288)
**Game:** Overhead racing game
**Playable by:** Lesson 271-274
**Key Techniques:** Track rendering, car sprite, steering, lap timing
**Spiral concepts:** Movement (with momentum), scrolling (track), collision (track boundaries)
**Lessons 257-264:** Track tiles, car sprite
**Lessons 265-274:** Steering, momentum, lap counter, **PLAYABLE**
**Lessons 275-288:** Opponents, obstacles, time trial, polish

### Tier 10: Simple Fighting (Lessons 289-320)
**Game:** One-on-one fighting (simple)
**Playable by:** Lesson 303-306
**Key Techniques:** Attack/block states, hit detection, health bars, knockback
**Spiral concepts:** Animation (fighting moves), collision (hit detection)
**Lessons 289-296:** Two fighters, basic movement
**Lessons 297-306:** Punch/kick, blocking, health, **PLAYABLE**
**Lessons 307-320:** Special moves, combos, rounds, KO

### Tier 11: Single-Screen Adventure (Lessons 321-352)
**Game:** Room-based adventure (Zelda-esque single screen)
**Playable by:** Lesson 335-338
**Key Techniques:** Room transitions, inventory, keys/doors, simple combat
**Spiral concepts:** Movement (between rooms), collision (walls/enemies)
**Lessons 321-328:** Room rendering, player, exits
**Lessons 329-338:** Room transitions, enemies, sword, **PLAYABLE**
**Lessons 339-352:** Keys/doors, inventory, items, treasure

### Tier 12: Simple Tactics (Lessons 353-384)
**Game:** Turn-based tactical grid game
**Playable by:** Lesson 367-370
**Key Techniques:** Grid cursor, unit selection, turn-based movement, simple AI
**Spiral concepts:** Grid logic, AI (opponent), game state (turns)
**Lessons 353-360:** Grid map, cursor control
**Lessons 361-370:** Unit selection, movement, turns, **PLAYABLE**
**Lessons 371-384:** Combat, AI opponent, win condition, polish

### Tier 13: Pong-Style Sports (Lessons 385-416)
**Game:** Tennis/Pong with enhancements
**Playable by:** Lesson 399-402
**Key Techniques:** Two-player input, ball spin, score tracking, serve mechanics
**Spiral concepts:** Ball physics (spin), collision (paddle angles), input
**Lessons 385-392:** Paddles, ball, basic physics
**Lessons 393-402:** Two players, scoring, serving, **PLAYABLE**
**Lessons 403-416:** Ball spin, AI opponent, power serves, match system

### Tier 14: Run 'n' Gun (Lessons 417-448)
**Game:** Side-scrolling action (Contra-lite)
**Playable by:** Lesson 431-434
**Key Techniques:** Horizontal scrolling + shooting, ground/air enemies, 8-way aim
**Spiral concepts:** Scrolling, shooting (8 directions), platforming
**Lessons 417-424:** Scrolling level, player running/jumping
**Lessons 425-434:** Shooting 8 directions, enemies, **PLAYABLE**
**Lessons 435-448:** Power weapons, enemy variety, hazards, boss

### Tier 15: Stealth Infiltration (Lessons 449-480)
**Game:** Avoid guards, reach exit (Impossible Mission style)
**Playable by:** Lesson 463-466
**Key Techniques:** Guard AI (vision cones), sneaking, alarm system, timing
**Spiral concepts:** AI (patrol patterns), collision (detection), game state (alarms)
**Lessons 449-456:** Room, player, basic guard
**Lessons 457-466:** Guard patrol, detection, alarm, exit, **PLAYABLE**
**Lessons 467-480:** Multiple guards, vision cones, items, timer

### Tier 16: Vertical Shmup (Lessons 481-512)
**Game:** Vertical scrolling shooter
**Playable by:** Lesson 495-498
**Key Techniques:** Vertical scrolling, enemy patterns from top, ground targets
**Spiral concepts:** Scrolling (vertical), shooting, enemy waves
**Lessons 481-488:** Vertical scrolling background
**Lessons 489-498:** Player, enemies from top, shooting, **PLAYABLE**
**Lessons 499-512:** Ground targets, power-ups, formations, boss

---

## Phase 2: Movement (1983-1984)

**Commercial Quality Era:** Smooth scrolling games emerge
**Example Games:** International Soccer (1983), Beach-Head (1983), Blue Max (1983)
**Overall Goal:** 16 games demonstrating scrolling, sprite multiplexing, and animation

### Phase 2 Genre Mix
**Continuing from Phase 1 (enhanced):**
- Tier 1: Space Shooter → Smooth horizontal scrolling
- Tier 2: Platformer → Multi-directional scrolling
- Tier 3: Vertical Shmup → Smooth vertical scrolling
- Tier 4: Run 'n' Gun → Enhanced scrolling + shooting
- Tier 5: Single-Screen Adventure → Multi-screen scrolling world
- Tier 6: Top-Down Racer → Smooth track scrolling
- Tier 7: Scrolling Shooter → Enhanced with parallax hints

**Evolved genres (replacing simpler ones):**
- Tier 8: Multi-Screen Maze → Replaces Pac-Man style
- Tier 9: Advanced Breakout → Multi-ball, complex physics
- Tier 10: Formation Shooter → Replaces Fixed Shooter with scrolling

**New genres for this era:**
- Tier 11: Football/Soccer → Sports with scrolling playfield
- Tier 12: Flick-Screen Adventure → Room-to-room exploration
- Tier 13: Multi-Directional Shooter → Defender/Scramble style
- Tier 14: Boulder Dash Clone → Dig/puzzle mechanics
- Tier 15: Advanced Fighting → Two-player scrolling arena
- Tier 16: Shoot-Em-Up with Levels → Progressive difficulty, boss fights

**Dropped genres:** Simple Pong-style (peaked), Fixed Shooter (evolved into scrolling), Collect-Em-Up (mechanics absorbed into other genres), Block Puzzle (not scrolling-focused)

**New techniques:** Character set manipulation, smooth hardware scrolling (H/V), sprite multiplexing (16+ sprites), tile maps, background music, advanced animation

---

## Phase 3: Sophistication (1984-1985)

**Commercial Quality Era:** Isometric games, advanced arcade conversions
**Example Games:** Impossible Mission (1984), Ghostbusters (1984), Paradroid (1985)
**Overall Goal:** 16 games with isometric graphics, advanced raster effects, complex AI

### Phase 3 Genre Mix
**Continuing (advanced):**
- Tier 1: Space Shooter → Advanced scrolling, raster effects
- Tier 2: Platformer → Sophisticated physics, large levels
- Tier 3: Vertical Shmup → Advanced enemy patterns, power-ups
- Tier 4: Run 'n' Gun → Enhanced weapons, complex levels

**Isometric variants (new perspective):**
- Tier 5: Isometric Adventure → Knight Lore/Head Over Heels style
- Tier 6: Isometric Tactics → Strategic grid-based combat
- Tier 7: Isometric Platformer → 3D perspective jumping puzzles
- Tier 8: Isometric Shooter → Zaxxon-style perspective

**Evolved genres:**
- Tier 9: Advanced Racing → 3D perspective (Pole Position style)
- Tier 10: Complex Fighting → IK-style multi-move combat
- Tier 11: Multi-Directional Shooter → Uridium/Iridis Alpha style

**New genres for this era:**
- Tier 12: Arcade Conversion Showcase → Authentic ports
- Tier 13: Paradroid-Style → Room exploration, droid transfer
- Tier 14: Ghosts 'n Goblins Clone → Difficult arcade platformer
- Tier 15: Elite-Lite → Simple 3D space trading
- Tier 16: Complex Puzzle Game → Sokoban/Boulderdash advanced

**Dropped genres:** Multi-Screen Maze (evolved into isometric), Simple Adventure (now isometric), Boulder Dash (absorbed into puzzle), Formation Shooter (mechanics in other shooters)

**New techniques:** Isometric projection, advanced IRQ programming, sprite multiplexing mastery (20+), pixel-perfect collision, data compression, SID filters

---

## Phase 4: Mastery Begins (1985-1987)

**Commercial Quality Era:** Polished commercial titles, multi-load epics
**Example Games:** The Last Ninja (1987), Uridium (1986), International Karate (1985)
**Overall Goal:** 16 games with multi-directional scrolling, advanced audio, multi-level structure

### Phase 4 Genre Mix
**Core genres (approaching commercial quality):**
- Tier 1: Horizontal Shooter → Parallax scrolling, Uridium-quality
- Tier 2: Platformer → Large scrolling worlds, The Last Ninja-quality
- Tier 3: Vertical Shmup → Complex patterns, boss battles
- Tier 4: Beat 'Em Up (new) → Side-scrolling brawler, multi-enemies
- Tier 5: Isometric Adventure → Multi-load, large world
- Tier 6: Racing → Advanced 3D perspective, opponents

**Polished variants:**
- Tier 7: Fighting Game → International Karate-quality
- Tier 8: Run 'n' Gun → Parallax, advanced weapons
- Tier 9: Isometric Platformer → Complex puzzles, large levels
- Tier 10: Multi-Directional Shooter → 8-way scrolling mastery

**New commercial-era genres:**
- Tier 11: Sports Simulation → Football/Tennis with depth
- Tier 12: Action RPG → Zelda-style with stats/inventory
- Tier 13: Advanced Tactics → Turn-based with complex systems
- Tier 14: Flight Simulator (simple) → 3D perspective flight
- Tier 15: Metroidvania-Lite → Exploration, power-up gating
- Tier 16: Arcade Perfect Port → Commercial-quality conversion

**Dropped genres:** Arcade Conversion Showcase (now perfected), Elite-Lite (too simple), Paradroid-style (mechanics integrated), Ghosts 'n Goblins (now general advanced platformer)

**New techniques:** Diagonal/8-way scrolling, parallax basics, charset animation, disk I/O, fast loaders, advanced sprite combinations, complex animation, multi-load structure

---

## Phase 5: Technical Excellence (1987-1988)

**Commercial Quality Era:** Peak of 8-bit design
**Example Games:** The Last Ninja 2 (1988), R-Type (1988), IK+ (1988)
**Overall Goal:** 16 games with advanced raster effects, multi-layer parallax, sophisticated AI

### Phase 5 Genre Mix
**Core genres (technical showcase):**
- Tier 1: Horizontal Shooter → R-Type-quality, multi-layer parallax
- Tier 2: Platformer → Advanced physics, polished animation
- Tier 3: Vertical Shmup → Bullet patterns, advanced effects
- Tier 4: Beat 'Em Up → Multiple enemies, advanced combat
- Tier 5: Fighting Game → IK+-quality, smooth animation
- Tier 6: Run 'n' Gun → Advanced scrolling, weapon systems

**Advanced variants:**
- Tier 7: Isometric Adventure → Massive world, sophisticated systems
- Tier 8: Action RPG → Deep stats, large world, save system
- Tier 9: Racing → Realistic physics, opponents
- Tier 10: Sports Simulation → Advanced AI, realistic gameplay

**Technical showcases:**
- Tier 11: Metroidvania → Large interconnected world
- Tier 12: Multi-Directional Shooter → Bullet hell, raster effects
- Tier 13: Advanced Tactics → Complex AI, large battles
- Tier 14: Pinball Simulation → Realistic physics, multiple tables
- Tier 15: Artillery Game → Scorched Earth/Worms-style destructible terrain
- Tier 16: Tower Defense → Strategic unit placement, wave management

**Dropped genres:** Flight Simulator (limited evolution), Isometric Tactics (evolved into Action RPG), Isometric Shooter (mechanics in other shooters)

**New techniques:** Multi-layer parallax (3+ layers), advanced raster splits, 40+ sprite multiplexing, optimized IRQ handlers, decompression, advanced physics, boss systems, custom fast loaders

---

## Phase 6: Innovation (1988-1990)

**Commercial Quality Era:** Technical showcases pushing hardware limits
**Example Games:** Creatures (1990), Retrograde (1989), Last Ninja 3 (1991)
**Overall Goal:** 16 games with software sprites, advanced memory, innovative mechanics

### Phase 6 Genre Mix
**Core genres (innovative techniques):**
- Tier 1: Horizontal Shooter → Software sprites, screen-sized bosses
- Tier 2: Platformer → Innovative mechanics, Creatures-quality
- Tier 3: Vertical Shmup → Procedural levels, dynamic difficulty
- Tier 4: Beat 'Em Up → Large sprites, complex moves
- Tier 5: Metroidvania → Non-linear, multiple endings
- Tier 6: Action RPG → Complex systems, procedural elements

**Innovative hybrids:**
- Tier 7: Puzzle Platformer → Portal-like mechanics
- Tier 8: Roguelike Shooter → Permadeath, procedural generation
- Tier 9: Strategy RPG → Turn-based tactics + character progression
- Tier 10: Simulation Game → Deep systems, emergent gameplay

**Technical innovation:**
- Tier 11: Fighting Game → Advanced combos, special moves
- Tier 12: Racing → Weather effects, dynamic tracks
- Tier 13: Run 'n' Gun → Massive sprites, set pieces
- Tier 14: Multi-Directional Shooter → Innovative control schemes
- Tier 15: God Game → Populous-style terrain manipulation, indirect control
- Tier 16: Construction/Management → Theme Park/Railroad Tycoon-style building

**Dropped genres:** Pinball (limited further evolution), Sports Simulation (mechanics perfected), Advanced Tactics (now Strategy RPG), Hybrid Genre (all are hybrids now)

**New techniques:** Software sprite blitting, large boss characters, memory pools, copper-like effects, procedural generation, save systems, dynamic difficulty

---

## Phase 7: Near-Perfection (1990-1991)

**Commercial Quality Era:** "Impossible" technical achievements
**Example Games:** Turrican (1990), Rick Dangerous 2 (1990), SWIV (1991)
**Overall Goal:** 16 games with massive worlds, polished animation, cinematic quality

### Phase 7 Genre Mix
**Core genres (near-perfection):**
- Tier 1: Horizontal Shooter → Turrican-quality, massive levels
- Tier 2: Platformer → Full-screen parallax, cinematic
- Tier 3: Vertical Shmup → Advanced patterns, visual spectacle
- Tier 4: Beat 'Em Up → Streets of Rage-quality depth
- Tier 5: Metroidvania → Massive interconnected world
- Tier 6: Action RPG → Deep systems, long campaign

**Polished commercial quality:**
- Tier 7: Fighting Game → Tournament-quality balance
- Tier 8: Run 'n' Gun → Contra/Metal Slug-inspired
- Tier 9: Racing → Realistic simulation, career mode
- Tier 10: Strategy RPG → Epic campaign, many units

**Cinematic experiences:**
- Tier 11: Story-Driven Platformer → Cutscenes, narrative
- Tier 12: Multi-Directional Shooter → SWIV-quality polish
- Tier 13: Puzzle Adventure → Atmospheric, environmental storytelling
- Tier 14: Roguelike → Deep systems, replayability
- Tier 15: Sandbox Game → Open-ended gameplay
- Tier 16: Stealth-Action → Metal Gear-style infiltration, detection mechanics

**Dropped genres:** Puzzle Platformer (mechanics in Story-Driven), Roguelike Shooter (now Roguelike), Simulation (elements in other games)

**New techniques:** Full-screen parallax (8 directions), large map streaming, 60fps elements, screen-sized bosses, cinematic sequences, particle systems, weapon variety, environmental interaction

---

## Phase 8: Ultimate Achievement (1991-1993)

**Commercial Quality Era:** The absolute pinnacle of C64 development
**Example Games:** Turrican II (1991), Mayhem in Monsterland (1993), Creatures 2 (1992)
**Overall Goal:** 16 commercial-quality games rivaling the best C64 releases

### Phase 8 Genre Mix
**Pinnacle genres:**
- Tier 1: Horizontal Shooter → Turrican II-quality perfection
- Tier 2: Platformer → Mayhem in Monsterland-quality mastery
- Tier 3: Vertical Shmup → Bullet hell perfection
- Tier 4: Beat 'Em Up → Commercial release quality
- Tier 5: Metroidvania → Full AAA-scale adventure
- Tier 6: Action RPG → Deep, replayable, polished

**Commercial releases:**
- Tier 7: Fighting Game → Tournament-grade balance
- Tier 8: Run 'n' Gun → Commercial perfection
- Tier 9: Racing → Realistic, polished, complete
- Tier 10: Strategy RPG → Epic scope, professional quality

**Ultimate showcases:**
- Tier 11: Story-Driven Epic → Cinematic, narrative-rich
- Tier 12: Multi-Directional Shooter → Technical perfection
- Tier 13: Roguelike → Endless replayability, depth
- Tier 14: Sandbox → Open-ended, emergent gameplay
- Tier 15: Stealth-Action → Perfect infiltration mechanics, MGS-quality
- Tier 16: 4X Strategy Lite → Civilization-inspired expand/explore/exploit/exterminate

**Modern techniques:** FLD, VSP, advanced demo tricks, cycle-perfect code, ultimate optimization, all techniques at mastery

**Dropped genres:** Puzzle Adventure (evolved into Story-Driven Epic), God Game (mechanics in Sandbox), Construction/Management (mechanics in Sandbox)

**New techniques:** Full-screen parallax at full speed, 50+ sprite multiplexing optimally, sophisticated physics, professional animation, cinematic presentation, complete audio, modern optimization, all techniques combined

---

## Genre Roadmap Across Phases

### Horizontal Shooter (Space Shooter) - ALL PHASES
- **Phase 1:** Single-screen, basic enemies, simple shooting
- **Phase 2:** Smooth horizontal scrolling, sprite multiplexing
- **Phase 3:** Advanced scrolling, raster effects, better enemies
- **Phase 4:** Parallax scrolling, Uridium-quality, bosses
- **Phase 5:** R-Type-quality, multi-layer parallax, advanced patterns
- **Phase 6:** Software sprites, screen-sized bosses, innovation
- **Phase 7:** Turrican-quality, massive levels, cinematic
- **Phase 8:** Turrican II-quality perfection, commercial mastery

### Platformer - ALL PHASES
- **Phase 1:** Single-screen jumping, simple physics
- **Phase 2:** Multi-directional scrolling levels
- **Phase 3:** Sophisticated physics, large levels
- **Phase 4:** The Last Ninja-quality, large scrolling worlds
- **Phase 5:** Advanced physics, polished animation
- **Phase 6:** Creatures-quality, innovative mechanics
- **Phase 7:** Full-screen parallax, cinematic quality
- **Phase 8:** Mayhem in Monsterland-quality mastery

### Vertical Shmup - ALL PHASES
- **Phase 1:** Basic vertical scrolling shooter
- **Phase 2:** Smooth scrolling, better enemies
- **Phase 3:** Advanced enemy patterns, power-ups
- **Phase 4:** Complex patterns, boss battles
- **Phase 5:** Bullet patterns, advanced effects
- **Phase 6:** Procedural levels, dynamic difficulty
- **Phase 7:** Advanced patterns, visual spectacle
- **Phase 8:** Bullet hell perfection

### Run 'n' Gun - Phases 1-8
- **Phase 1:** Side-scrolling action, basic shooting
- **Phase 2:** Enhanced scrolling, 8-way aim
- **Phase 3:** Enhanced weapons, complex levels
- **Phase 4:** Parallax, advanced weapons
- **Phase 5:** Advanced scrolling, weapon systems
- **Phase 6:** Massive sprites, set pieces
- **Phase 7:** Contra-inspired quality
- **Phase 8:** Commercial perfection

### Maze Chase → Isometric Adventure
- **Phase 1:** Pac-Man style maze game
- **Phase 2:** Multi-screen maze exploration
- **Phase 3+:** **EVOLVED** into Isometric Adventure (Phases 3-8)

### Simple Platformer → Beat 'Em Up
- **Phase 1:** Single-screen platform jumper
- **Phase 2:** Multi-screen scrolling
- **Phase 3:** Advanced platforming
- **Phase 4+:** **NEW GENRE** Beat 'Em Up emerges (Phases 4-8)

### Breakout - Phases 1-2 ONLY
- **Phase 1:** Basic brick-breaking
- **Phase 2:** Advanced multi-ball physics
- **Phase 3+:** **DROPPED** (mechanics absorbed into other games)

### Fighting Game - Phases 2-8
- **Phase 2:** Two-player fighting introduced
- **Phase 3:** IK-style multi-move combat
- **Phase 4:** International Karate-quality
- **Phase 5:** IK+-quality, smooth animation
- **Phase 6:** Advanced combos, special moves
- **Phase 7:** Tournament-quality balance
- **Phase 8:** Tournament-grade perfection

### Adventure (Single/Multi-Screen) → Metroidvania
- **Phase 1:** Single-screen room-based
- **Phase 2:** Scrolling multi-screen world
- **Phase 3+:** **EVOLVED** into Isometric (Phase 3-4)
- **Phase 4:** Action RPG emerges
- **Phase 5+:** **EVOLVED** into Metroidvania (Phases 5-8)

### Racing - Phases 1-8
- **Phase 1:** Top-down simple racing
- **Phase 2:** Smooth track scrolling
- **Phase 3:** 3D perspective (Pole Position-style)
- **Phase 4:** Advanced 3D, opponents
- **Phase 5:** Realistic physics, opponents
- **Phase 6:** Weather effects, dynamic tracks
- **Phase 7:** Realistic simulation, career mode
- **Phase 8:** Polished, complete racing experience

### Tactics → Strategy RPG
- **Phase 1:** Simple turn-based grid
- **Phase 2:** Enhanced tactics
- **Phase 3:** Isometric tactical combat
- **Phase 4:** Advanced tactics, complex systems
- **Phase 5+:** **EVOLVED** into Strategy RPG (Phases 6-8)

### Pong-Style Sports - Phases 1-2 ONLY
- **Phase 1:** Tennis/Pong with enhancements
- **Phase 2:** **EVOLVED** into Football/Soccer
- **Phase 3+:** **DROPPED** (evolved into Sports Simulation in Phases 4-5)

### Fixed Shooter - Phase 1 ONLY
- **Phase 1:** Space Invaders-style
- **Phase 2+:** **EVOLVED** into Formation/Scrolling Shooters

### Collect-Em-Up - Phase 1 ONLY
- **Phase 1:** Navigate arena, collect items
- **Phase 2+:** **DROPPED** (mechanics absorbed into other genres)

### Block Puzzle - Phase 1 ONLY
- **Phase 1:** Falling block puzzle (Tetris/Columns-style)
- **Phase 2+:** **DROPPED** (not scrolling-focused)

### Stealth Infiltration - Phases 1-3
- **Phase 1:** Impossible Mission-style
- **Phase 2-3:** Enhanced stealth mechanics
- **Phase 4+:** **MECHANICS INTEGRATED** into other genres

### Isometric Games - Phases 3-7
- **Phase 3:** Isometric Adventure, Tactics, Platformer, Shooter introduced
- **Phase 4:** Isometric Adventure, Platformer enhanced
- **Phase 5:** Isometric Adventure reaches peak
- **Phase 6:** Some mechanics absorbed into hybrids
- **Phase 7:** Isometric elements in other genres
- **Phase 8:** Fully integrated techniques

### New Genres Emerging Mid-Curriculum
- **Phase 4:** Action RPG, Metroidvania-Lite, Beat 'Em Up
- **Phase 5:** Metroidvania (full), Pinball Simulation
- **Phase 6:** Roguelike, Puzzle Platformer, Strategy RPG
- **Phase 7:** Story-Driven Platformer, Sandbox, Puzzle Adventure
- **Phase 8:** Stealth-Action, 4X Strategy Lite

---

## Integration with Vault and Pattern Library

### The Vault: Contextual Links

Lessons should link to Vault entries when mentioning:

**People:** Programmers, musicians, artists, designers
- *Example:* "...similar to Martin Galway's approach in Comic Bakery..."
- *Link to:* `/vault/people/martin-galway`

**Companies:** Studios, publishers, hardware manufacturers
- *Example:* "...techniques pioneered by Psygnosis..."
- *Link to:* `/vault/companies/psygnosis`

**Games:** Specific titles used as examples
- *Example:* "...as seen in Mayhem in Monsterland..."
- *Link to:* `/vault/games/mayhem-in-monsterland`

**Techniques:** Programming methods and approaches
- *Example:* "...using sprite multiplexing to display..."
- *Link to:* `/vault/techniques/c64-sprite-multiplexing`

**Hardware:** Chips and components being programmed
- *Example:* "...the VIC-II chip's sprite registers..."
- *Link to:* `/vault/hardware/vic-ii`

**Cultural Context:** Movies, music, events for era context
- *Example:* "...this game was released the same year as Aliens..."
- *Link to:* `/vault/movies/aliens-1986`

### The Pattern Library: Reference Implementations

Lessons teach concepts step-by-step, then reference Pattern Library for production-ready code:

**Pattern Introduction:**
When a pattern is first taught, the lesson should:
1. Teach the concept and build it up incrementally
2. Show a working example in the lesson
3. Reference the Pattern Library entry for the complete, production-ready version

*Example at end of lesson:*
```markdown
## Further Practice

For a complete, production-ready implementation with additional optimizations,
see [Pattern: Sprite Multiplexing (Basic)](/patterns/c64/rendering/sprite-multiplexing-basic).
```

**Pattern Evolution:**
As patterns evolve across phases, reference the appropriate version:
- Phase 2: [Pattern: Sprite Multiplexing (Basic)](/patterns/c64/rendering/sprite-multiplexing-basic)
- Phase 3: [Pattern: Sprite Multiplexing (Sorted)](/patterns/c64/rendering/sprite-multiplexing-sorted)
- Phase 5: [Pattern: Sprite Multiplexing (Advanced)](/patterns/c64/rendering/sprite-multiplexing-advanced)

**Pattern Categories for C64:**
- **Rendering:** Sprites, scrolling, raster effects, character graphics
- **Input:** Joystick, keyboard, multi-key detection
- **Audio:** SID music, sound effects, mixing
- **Physics:** Collision detection, gravity, projectiles
- **AI:** Enemy behavior, pathfinding
- **Framework:** Raster interrupts, game loops, state machines
- **Optimization:** Unrolled loops, lookup tables, cycle counting

### Integration Example

**Lesson excerpt:**
```markdown
In this lesson, we're implementing sprite multiplexing to display more than
8 sprites on screen. The VIC-II chip only supports 8 hardware sprites, but
by using raster interrupts we can reuse them multiple times per frame.

[...lesson content teaching the concept step by step...]

This technique was pioneered in games like Uridium and became standard by
the late 1980s. Mayhem in Monsterland uses advanced multiplexing to display
50+ sprites with minimal flickering.

## Further Reading

**Pattern Library:**
- [Sprite Multiplexing (Basic)](/patterns/c64/rendering/sprite-multiplexing-basic)
- [Raster Interrupts](/patterns/c64/framework/raster-interrupts)

**Vault:**
- [Sprite Multiplexing Technique](/vault/techniques/c64-sprite-multiplexing)
- [VIC-II Chip](/vault/hardware/vic-ii)
- [Mayhem in Monsterland](/vault/games/mayhem-in-monsterland)
- [Andrew Braybrook](/vault/people/andrew-braybrook) (Uridium creator)
```

---

## Curriculum Notes

### Powers of 2 Structure
- **Phases:** 8 (2^3)
- **Tiers per phase:** 16 (2^4)
- **Lessons per tier:** 32 (2^5)
- **Total tiers:** 128 (2^7)
- **Total lessons:** 4,096 (2^12)

### Spiral Learning Benefits
- **Immediate gratification:** Playable game by Lesson 15-20
- **Progressive mastery:** Same concepts revisited at higher complexity
- **Reduced cognitive load:** Learn minimum needed, deepen later
- **Maintained engagement:** Genre variety prevents boredom

### Genre Diversity
16 genres per phase ensure:
- Different game mechanics explored
- Varied technical challenges
- Learner finds preferred genres
- Completed games show breadth

### Assessment
- **Per Tier:** Working playable game (self-assessment)
- **Per Phase:** 16 complete games portfolio
- **Full Curriculum:** 128 games demonstrating commercial-quality mastery

### Time Estimates
- **Tier completion:** 16-32 hours (32 lessons, varies by learner)
- **Phase completion:** 256-512 hours (16 tiers)
- **Full curriculum:** 2,048-4,096 hours (8 phases)

### Prerequisites
- **Phase 1:** Basic understanding of hexadecimal, binary, programming concepts helpful but not required
- **Phases 2-8:** Completion of previous phase (or equivalent experience)

### Resources Required
- VICE emulator (x64sc)
- ACME assembler or ca65
- Text editor
- C64 reference documentation
- Example game ROM files for study

### Metadata Tags (Future)
Each lesson/game will be tagged with:
- Genre
- Platform (commodore-64)
- CPU (6510)
- Era (e.g., 1982-1983)
- Techniques (e.g., sprites, scrolling, IRQ)
- Difficulty level
