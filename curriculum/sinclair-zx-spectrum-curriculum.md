# Sinclair ZX Spectrum Curriculum

## Overview

This curriculum covers game development for the Sinclair ZX Spectrum across 8 phases of increasing complexity, from basic arcade-style games to sophisticated commercial-quality titles that pushed the hardware to its limits.

**Total Structure:**
- **8 Phases** (2^3) - Technical progression from 1982-style to 1992-style games
- **16 Tiers per Phase** (2^4) - 16 different game genres/types
- **32 Lessons per Tier** (2^5) - Complete game development cycle
- **Total: 4,096 lessons** (2^12)

**Learning Approach:**
- **Spiral Learning:** Teach minimum needed first, deepen understanding later
- **Quick Interaction:** Lessons 2-3 have interactive elements
- **Playable Early:** Lessons 15-20 produce a playable game
- **Polish Phase:** Lessons 21-32 add effects, variety, commercial quality

**ZX Spectrum Technical Context:**
- **CPU:** Zilog Z80 @ 3.5 MHz
- **Graphics:** Software sprites, UDG (User Defined Graphics), attribute-based color
- **Resolution:** 256×192 pixels, 32×24 characters
- **Color System:** 8×8 attribute blocks (ink/paper/bright/flash)
- **Sound:** 1-bit beeper (creative pulse-width modulation)
- **Memory:** 48K standard (16K/128K models exist)
- **Storage:** Cassette tape initially, later +3 disk

---

## Phase 1: Foundation (1982-1983 Era)

**Target Quality:** Early ZX Spectrum games - simple graphics, monochrome or minimal color, basic beeper effects, arcade-inspired gameplay. Think *3D Monster Maze*, *Horace Goes Skiing*, *Manic Miner* (early levels).

**Technical Focus:**
- BASIC programming with machine code routines
- Character graphics and UDG (User Defined Graphics)
- Keyboard input (IN 31, INKEY$)
- Screen manipulation (PRINT AT, PLOT, DRAW)
- Simple beeper sound (BEEP command)
- Attribute management (INK, PAPER, BRIGHT, FLASH)
- Character-based collision detection

**16 Game Genres (Phase 1):**

### Tier 1: Fixed Screen Shooter (Lessons 1-32)
**Game:** Space Invaders-style fixed shooter (player at bottom vs descending enemies)
**Playable by:** Lesson 15-20
**Key Techniques:** UDG sprites, keyboard input, movement, shooting, collision, score
**ZX Specific:** Monochrome graphics to avoid attribute clash, simple beeper shots

### Tier 2: Maze Chase (Lessons 33-64)
**Game:** Pac-Man inspired maze game (collect items, avoid enemies)
**Playable by:** Lesson 48-52
**Key Techniques:** Character-based maze, scrolling text, enemy AI patterns
**ZX Specific:** Pre-drawn maze using graphics characters, attribute-based colors

### Tier 3: Platform Game (Lessons 65-96)
**Game:** Single-screen platformer (jump between platforms, collect items)
**Playable by:** Lesson 80-84
**Key Techniques:** Gravity, jumping, platform collision, ladders
**ZX Specific:** Character-aligned platforms, UDG for player/enemies

### Tier 4: Breakout (Lessons 97-128)
**Game:** Brick-breaking paddle game
**Playable by:** Lesson 112-116
**Key Techniques:** Ball physics, paddle control, brick destruction
**ZX Specific:** PLOT/DRAW for ball, character blocks for bricks

### Tier 5: Horizontal Shooter (Lessons 129-160)
**Game:** Side-scrolling space shooter (fly right, shoot enemies)
**Playable by:** Lesson 144-148
**Key Techniques:** Scrolling starfield, enemy waves, power-ups
**ZX Specific:** Attribute scrolling for background, UDG for sprites

### Tier 6: Snake (Lessons 161-192)
**Game:** Growing snake collecting food
**Playable by:** Lesson 176-180
**Key Techniques:** Dynamic tail growth, self-collision, food spawning
**ZX Specific:** Character-based snake segments, fast PRINT AT rendering

### Tier 7: Vertical Shooter (Lessons 193-224)
**Game:** Top-down vertical scrolling shooter
**Playable by:** Lesson 208-212
**Key Techniques:** Vertical scrolling, formation enemies, boss patterns
**ZX Specific:** Attribute scrolling, synchronized sprite movement

### Tier 8: Adventure (Lessons 225-256)
**Game:** Text adventure with simple graphics
**Playable by:** Lesson 240-244
**Key Techniques:** Parser, inventory, room descriptions, conditional logic
**ZX Specific:** Split screen (text below, image above), tape save/load

### Tier 9: Racing (Lessons 257-288)
**Game:** Top-down racing game (avoid obstacles, reach finish)
**Playable by:** Lesson 272-276
**Key Techniques:** Road scrolling, steering, speed control, obstacles
**ZX Specific:** Repeating road patterns, character-based graphics

### Tier 10: Pong (Lessons 289-320)
**Game:** Classic two-paddle ball game
**Playable by:** Lesson 304-308
**Key Techniques:** Two-player input, ball physics, score tracking
**ZX Specific:** PLOT/DRAW for ball and paddles, beeper scoring sound

### Tier 11: Target Shooter (Lessons 321-352)
**Game:** Shooting gallery (moving targets, score multiplier)
**Playable by:** Lesson 336-340
**Key Techniques:** Moving target patterns, timing, accuracy scoring
**ZX Specific:** Crosshair using PLOT, UDG targets

### Tier 12: Block Puzzle (Lessons 353-384)
**Game:** Falling block puzzle (Tetris-style)
**Playable by:** Lesson 368-372
**Key Techniques:** Rotation, line clearing, gravity, game speed
**ZX Specific:** Character block graphics, fast playfield rendering

### Tier 13: Frogger Clone (Lessons 385-416)
**Game:** Road crossing game (avoid cars, cross river)
**Playable by:** Lesson 400-404
**Key Techniques:** Multiple scrolling lanes, timing-based gameplay
**ZX Specific:** Character scrolling for traffic lanes

### Tier 14: Lunar Lander (Lessons 417-448)
**Game:** Physics-based landing game (thrust, gravity, fuel)
**Playable by:** Lesson 432-436
**Key Techniques:** Thrust physics, fuel management, landing detection
**ZX Specific:** Vector graphics using DRAW, simple terrain

### Tier 15: Bomber (Lessons 449-480)
**Game:** Drop bombs on targets below (side-view bomber)
**Playable by:** Lesson 464-468
**Key Techniques:** Dropping projectiles, building destruction, altitude
**ZX Specific:** Scrolling landscape using character graphics

### Tier 16: Submarine Game (Lessons 481-512)
**Game:** Side-view submarine game (torpedoes, depth charges)
**Playable by:** Lesson 496-500
**Key Techniques:** Depth control, sonar detection, torpedo physics
**ZX Specific:** Layered attribute colors for water depth

---

## Phase 2: Enhancement (1983-1984 Era)

**Target Quality:** Improved ZX Spectrum games - better color management, smoother animation, multi-screen gameplay, machine code speed-up. Think *Jetpac*, *Sabre Wulf*, *Chuckie Egg*.

**Technical Focus:**
- Hybrid BASIC/machine code for speed
- Software sprite routines (XOR drawing)
- Screen buffering techniques
- Optimized attribute management
- Multi-screen level design
- Simple music routines
- Refined collision detection

**Genre Mix:**
- **Enhanced from Phase 1:** Fixed Screen Shooter, Horizontal Shooter, Platform Game, Vertical Shooter, Racing, Target Shooter, Frogger Clone
- **Evolved:** Maze Chase → Multi-Screen Maze Explorer
- **New for Phase 2:** Collect-Em-Up, Jetpack Game
- **Dropped:** Breakout, Pong, Snake, Block Puzzle, Lunar Lander, Bomber, Submarine Game

### Tier 1: Fixed Screen Shooter - Enhanced (Lessons 1-32)
Multiple enemy types, power-ups, animated explosions, color cycling effects

### Tier 2: Multi-Screen Maze Explorer (Lessons 33-64)
**Evolution of Maze Chase:** Multiple connected screens, keys/doors, enemy spawning

### Tier 3: Platform Game - Enhanced (Lessons 65-96)
Multi-screen scrolling, moving platforms, enemy patterns, lives system

### Tier 4: Collect-Em-Up (Lessons 97-128)
**New Genre:** Jetpac-style collect items and build objective (machine code sprites)

### Tier 5: Horizontal Shooter - Enhanced (Lessons 129-160)
Parallax scrolling, ground targets, weapon variety, end-of-level boss

### Tier 6: Jetpack Game (Lessons 161-192)
**New Genre:** Thrust/gravity with fuel, collect items, avoid obstacles

### Tier 7: Vertical Shooter - Enhanced (Lessons 193-224)
Ground installations, bonus stages, complex bullet patterns

### Tier 8: Adventure - Enhanced (Lessons 225-256)
Animated graphics, simple parser, inventory management, multiple locations

### Tier 9: Racing - Enhanced (Lessons 257-288)
Opponent cars, checkpoints, multiple tracks, speed boosts

### Tier 10: Target Shooter - Enhanced (Lessons 289-320)
Moving backgrounds, combo scoring, different weapon types

### Tier 11: Frogger Clone - Enhanced (Lessons 321-352)
Multiple levels, varied obstacles, bonus timers, log/turtle patterns

### Tier 12: Run 'n' Gun (Lessons 353-384)
**New Genre:** Walking shooter with multi-directional shooting (Commando-style)

### Tier 13: Climbing Game (Lessons 385-416)
**New Genre:** Climb to top avoiding obstacles (Donkey Kong-style)

### Tier 14: Defence Game (Lessons 417-448)
**New Genre:** Defend base from waves of attackers

### Tier 15: Flip-Screen Platform (Lessons 449-480)
**New Genre:** Manic Miner-style screen-by-screen platformer with hazards

### Tier 16: Maze Builder (Lessons 481-512)
**New Genre:** Player builds/modifies maze while playing (Amidar-style)

---

## Phase 3: Sophistication (1985-1986 Era)

**Target Quality:** "Golden Era" ZX Spectrum games - advanced graphics, isometric projection, complex gameplay, iconic titles. Think *Knight Lore*, *Skool Daze*, *R-Type* (Spectrum port).

**Technical Focus:**
- Pure machine code for performance
- Isometric 3D graphics
- Advanced sprite rendering
- Screen-splitting techniques
- AY sound chip (128K models)
- Complex enemy AI
- Save/load game states

**Genre Mix:**
- **Core Genres:** Fixed Screen Shooter, Horizontal Shooter, Platform Game, Vertical Shooter, Racing, Run 'n' Gun
- **Evolved:** Multi-Screen Maze → Isometric Adventure, Flip-Screen Platform → Isometric Platformer
- **New for Phase 3:** Isometric Action-Adventure, Beat 'Em Up, Diagonal Shooter, Arcade Sports
- **Dropped:** Collect-Em-Up, Jetpack Game, Target Shooter, Frogger Clone, Climbing Game, Defence Game, Maze Builder, Adventure (text-based)

### Tier 1: Fixed Screen Shooter - Advanced (Lessons 1-32)
Screen rotation effects, complex wave patterns, shield mechanics

### Tier 2: Isometric Adventure (Lessons 33-64)
**Evolution:** Knight Lore-style object interaction, puzzle-solving, flip-screen exploration

### Tier 3: Isometric Platformer (Lessons 65-96)
**Evolution:** 3D movement, perspective jumping, layered sprites

### Tier 4: Isometric Action-Adventure (Lessons 97-128)
**New Genre:** Combat + puzzles in isometric view (Head Over Heels-style)

### Tier 5: Horizontal Shooter - Advanced (Lessons 129-160)
R-Type quality: detailed sprites, complex patterns, charge weapons

### Tier 6: Run 'n' Gun - Advanced (Lessons 161-192)
Multi-directional scrolling, destructible environments, grenades

### Tier 7: Vertical Shooter - Advanced (Lessons 193-224)
1942-style with loops, formations, ground/air targets

### Tier 8: Beat 'Em Up (Lessons 225-256)
**New Genre:** Side-scrolling fighting (Renegade-style), multiple enemies

### Tier 9: Racing - Advanced (Lessons 257-288)
3D perspective racing (Out Run-style), track variety

### Tier 10: Diagonal Shooter (Lessons 289-320)
**New Genre:** Zaxxon-style angled perspective shooter

### Tier 11: Platform Game - Advanced (Lessons 321-352)
Rick Dangerous-style with inventory, traps, shooting

### Tier 12: Arcade Sports (Lessons 353-384)
**New Genre:** Football/soccer with tactics and controls

### Tier 13: Space Combat (Lessons 385-416)
**New Genre:** Elite-style 3D space trading/combat (simplified)

### Tier 14: Stealth Platformer (Lessons 417-448)
**New Genre:** Avoid detection, shadows, line-of-sight

### Tier 15: Tactical Action (Lessons 449-480)
**New Genre:** Strategic combat with unit control

### Tier 16: Vector Shooter (Lessons 481-512)
**New Genre:** Asteroids-style with vector graphics using DRAW

---

## Phase 4: Commercial Quality (1987-1988 Era)

**Target Quality:** Commercial-grade games with polished gameplay, advanced techniques, loader screens, full soundtracks. Think *Renegade III*, *Operation Wolf*, *Rainbow Islands*.

**Technical Focus:**
- Optimized machine code rendering
- Double buffering
- Advanced color mixing
- Multi-channel beeper music
- Interrupt-driven routines
- Compression techniques
- Custom loaders

**Genre Mix:**
- **Core Genres:** Horizontal Shooter, Platform Game, Vertical Shooter, Run 'n' Gun, Racing, Beat 'Em Up
- **Continued:** Isometric Adventure, Isometric Action-Adventure, Arcade Sports
- **New for Phase 4:** Light Gun Shooter, Puzzle-Platformer, Action RPG
- **Dropped:** Fixed Screen Shooter, Isometric Platformer, Diagonal Shooter, Space Combat, Stealth Platformer, Tactical Action, Vector Shooter

### Tier 1: Horizontal Shooter - Commercial (Lessons 1-32)
Multiple weapon systems, mid-level checkpoints, cinematic presentation

### Tier 2: Isometric Adventure - Advanced (Lessons 33-64)
Complex puzzles, character switching, environmental interaction

### Tier 3: Isometric Action-Adventure - Advanced (Lessons 65-96)
Boss fights, inventory puzzles, multiple playable characters

### Tier 4: Light Gun Shooter (Lessons 97-128)
**New Genre:** Operation Wolf-style gallery shooter, ammo management

### Tier 5: Platform Game - Commercial (Lessons 129-160)
Rainbow Islands quality: screen scrolling, varied mechanics per level

### Tier 6: Run 'n' Gun - Commercial (Lessons 161-192)
Vehicles, multiple routes, destructible scenery

### Tier 7: Vertical Shooter - Commercial (Lessons 193-224)
Polished bullet patterns, scoring chains, dramatic bosses

### Tier 8: Beat 'Em Up - Advanced (Lessons 225-256)
Weapons, grab moves, multiple attack types, co-op elements

### Tier 9: Racing - Commercial (Lessons 257-288)
Track editor, opponent AI, weather effects, damage system

### Tier 10: Puzzle-Platformer (Lessons 289-320)
**New Genre:** Platform mechanics with logic puzzles (Sokoban elements)

### Tier 11: Action RPG (Lessons 321-352)
**New Genre:** Real-time combat with stats, inventory, quests

### Tier 12: Arcade Sports - Advanced (Lessons 353-384)
Multiple sports modes, season/tournament structure

### Tier 13: Maze Exploration (Lessons 385-416)
Complex multi-level maze with mapping, teleporters

### Tier 14: Artillery Game (Lessons 417-448)
Scorched Earth-style angle/power shooting with destructible terrain

### Tier 15: Side-View Combat (Lessons 449-480)
One-on-one fighting with special moves

### Tier 16: Tower Defense (Lessons 481-512)
Place defenders to stop waves of enemies

---

## Phase 5: Mastery (1988-1989 Era)

**Target Quality:** Pushing hardware limits with advanced techniques. Think *Last Ninja 2*, *New Zealand Story*, *Turrican*.

**Technical Focus:**
- Multi-color sprites (careful attribute management)
- Hardware scrolling tricks
- Sample playback (digitized sound)
- Memory banking (128K)
- Advanced physics engines
- Particle systems
- Dynamic difficulty

**Genre Mix:**
- **All-Phase Core:** Horizontal Shooter, Platform Game, Vertical Shooter, Run 'n' Gun, Racing
- **Continued:** Beat 'Em Up, Isometric Action-Adventure, Action RPG, Arcade Sports
- **New for Phase 5:** Metroidvania, Combat Flight Sim, Cinematic Platformer
- **Dropped:** Isometric Adventure, Light Gun Shooter, Puzzle-Platformer, Maze Exploration, Artillery Game, Side-View Combat, Tower Defense

### Tier 1: Horizontal Shooter - Master (Lessons 1-32)
R-Type quality with organic enemies, multiple phases per level

### Tier 2: Isometric Action-Adventure - Master (Lessons 33-64)
Batman-style with gadgets, cinematic sequences, complex combat

### Tier 3: Metroidvania (Lessons 65-96)
**New Genre:** Connected world, ability-gating, backtracking

### Tier 4: Platform Game - Master (Lessons 97-128)
New Zealand Story quality: varied mechanics, creative power-ups

### Tier 5: Combat Flight Sim (Lessons 129-160)
**New Genre:** 3D cockpit view, missile combat, tactical missions

### Tier 6: Run 'n' Gun - Master (Lessons 161-192)
Turrican-style exploration + shooting, huge levels

### Tier 7: Vertical Shooter - Master (Lessons 193-224)
Advanced bullet patterns, scoring systems, rank difficulty

### Tier 8: Beat 'Em Up - Master (Lessons 225-256)
Last Ninja quality: isometric fighting, environmental combat

### Tier 9: Racing - Master (Lessons 257-288)
Full 3D racing with pit stops, damage modeling

### Tier 10: Cinematic Platformer (Lessons 289-320)
**New Genre:** Prince of Persia-style animation, careful movement

### Tier 11: Action RPG - Advanced (Lessons 321-352)
Zelda-style overworld, dungeons, item progression

### Tier 12: Arcade Sports - Master (Lessons 353-384)
Full team management, realistic physics, multiple play modes

### Tier 13: Puzzle Action (Lessons 385-416)
Real-time puzzle solving under pressure

### Tier 14: Experimental Shooter (Lessons 417-448)
Unique mechanics (gravity, time manipulation, perspective shifts)

### Tier 15: Exploration Adventure (Lessons 449-480)
Open-world exploration with environmental storytelling

### Tier 16: Roguelike (Lessons 481-512)
**New Genre:** Procedural dungeons, permadeath, ASCII graphics

---

## Phase 6: Innovation (1989-1990 Era)

**Target Quality:** Genre-defining games with unique mechanics. Think *Pang*, *Fantasy World Dizzy*, *Chase H.Q.*.

**Technical Focus:**
- Multi-load streaming
- Advanced compression
- Screen effects (raster bars, copper effects)
- Physics-based gameplay
- Procedural generation
- Complex state machines

**Genre Mix:**
- **All-Phase Core:** Horizontal Shooter, Platform Game, Vertical Shooter, Run 'n' Gun, Racing
- **Continued:** Beat 'Em Up, Metroidvania, Action RPG, Roguelike
- **New for Phase 6:** Physics Puzzle, Open-World Adventure, Arcade Collection
- **Dropped:** Isometric Action-Adventure, Combat Flight Sim, Cinematic Platformer, Arcade Sports, Puzzle Action, Experimental Shooter, Exploration Adventure

### Tier 1: Horizontal Shooter - Ultimate (Lessons 1-32)
Genre-defining quality, memorable bosses, innovative weapons

### Tier 2: Metroidvania - Advanced (Lessons 33-64)
Interconnected world map, sequence breaking possibilities

### Tier 3: Platform Game - Ultimate (Lessons 65-96)
Dizzy-style adventure-platformer with inventory puzzles

### Tier 4: Physics Puzzle (Lessons 97-128)
**New Genre:** Lemmings/Pang-style physics-based challenges

### Tier 5: Run 'n' Gun - Ultimate (Lessons 129-160)
Metal Slug-style detailed sprites, vehicle sections

### Tier 6: Racing - Ultimate (Lessons 161-192)
Chase H.Q.-style cinematic racing with narrative

### Tier 7: Vertical Shooter - Ultimate (Lessons 193-224)
Genre-defining bullet patterns, sophisticated scoring

### Tier 8: Beat 'Em Up - Ultimate (Lessons 225-256)
Streets of Rage quality, weapon variety, combo system

### Tier 9: Open-World Adventure (Lessons 257-288)
**New Genre:** Non-linear exploration, quest system, day/night

### Tier 10: Action RPG - Master (Lessons 289-320)
Full equipment system, magic, multiple quests

### Tier 11: Roguelike - Advanced (Lessons 321-352)
Classes, magic items, complex dungeons

### Tier 12: Experimental Platform (Lessons 353-384)
Unique movement mechanics (grappling, magnetism, etc.)

### Tier 13: Narrative Adventure (Lessons 385-416)
Story-driven with cutscenes, character development

### Tier 14: Arcade Collection (Lessons 417-448)
**New Genre:** Multiple mini-games with shared progression

### Tier 15: Strategy Action (Lessons 449-480)
Real-time tactics with resource management

### Tier 16: Survival Game (Lessons 481-512)
Resource gathering, crafting, environmental threats

---

## Phase 7: Perfection (1990-1991 Era)

**Target Quality:** Best-of-platform showcase games. Think *Robocop*, *Navy Moves*, *Dynamite Düx*.

**Technical Focus:**
- Maximum optimization
- Multi-sprite engines
- Advanced music drivers
- Parallax backgrounds
- Screen transitions
- Cut-scene systems

**Genre Mix:**
- **All-Phase Core:** Horizontal Shooter, Platform Game, Vertical Shooter, Run 'n' Gun, Racing
- **Continued:** Beat 'Em Up, Metroidvania, Action RPG, Roguelike, Open-World Adventure
- **New for Phase 7:** None (perfecting existing genres)
- **Dropped:** Physics Puzzle, Arcade Collection, Experimental Platform, Narrative Adventure, Strategy Action, Survival Game

### Tier 1: Horizontal Shooter - Perfected (Lessons 1-32)
Absolute technical showcase, memorable throughout

### Tier 2: Metroidvania - Perfected (Lessons 33-64)
Symphony of the Night-level interconnection (scaled to ZX)

### Tier 3: Platform Game - Perfected (Lessons 65-96)
Genre-defining platforming with perfect controls

### Tier 4: Run 'n' Gun - Perfected (Lessons 97-128)
Ultimate overhead/side-view shooter hybrid

### Tier 5: Racing - Perfected (Lessons 129-160)
Outrun-quality with branching paths

### Tier 6: Vertical Shooter - Perfected (Lessons 161-192)
Perfect bullet patterns, scoring depth

### Tier 7: Beat 'Em Up - Perfected (Lessons 193-224)
Final Fight quality, depth of combat

### Tier 8: Action RPG - Perfected (Lessons 225-256)
Full adventure with deep systems

### Tier 9: Roguelike - Master (Lessons 257-288)
Complex systems, replay value, emergent gameplay

### Tier 10: Open-World Adventure - Advanced (Lessons 289-320)
Living world, NPC schedules, dynamic events

### Tier 11: Puzzle-Shooter Hybrid (Lessons 321-352)
Innovative blend of genres

### Tier 12: Boss Rush (Lessons 353-384)
Pure boss battle game with pattern mastery

### Tier 13: Time Attack Platformer (Lessons 385-416)
Speed-running focus, tight controls

### Tier 14: Precision Shooter (Lessons 417-448)
One-hit-kill gameplay requiring perfect play

### Tier 15: Adventure-Shooter (Lessons 449-480)
Story-driven shooting with RPG elements

### Tier 16: Experimental Genre Blend (Lessons 481-512)
Unique combination not seen before

---

## Phase 8: Legacy (1991-1992 Era)

**Target Quality:** Final generation pushing absolute limits. Think late-era commercial releases that defined what was possible.

**Technical Focus:**
- Every optimization known
- Custom rendering engines
- Advanced compression
- Sample-based music
- Multi-part epics
- Professional production values

**Genre Mix:**
- **All-Phase Core:** Horizontal Shooter, Platform Game, Vertical Shooter, Run 'n' Gun, Racing
- **Continued:** Beat 'Em Up, Metroidvania, Action RPG, Roguelike, Open-World Adventure
- **Capstone Games:** Genre-defining masterworks

### Tier 1: Horizontal Shooter - Legacy (Lessons 1-32)
Ultimate showcase of the genre

### Tier 2: Metroidvania - Legacy (Lessons 33-64)
Defining example of exploration-platformer

### Tier 3: Platform Game - Legacy (Lessons 65-96)
Perfect platforming mechanics and design

### Tier 4: Run 'n' Gun - Legacy (Lessons 97-128)
Genre masterclass

### Tier 5: Racing - Legacy (Lessons 129-160)
Ultimate racing experience on the platform

### Tier 6: Vertical Shooter - Legacy (Lessons 161-192)
Shmup perfection

### Tier 7: Beat 'Em Up - Legacy (Lessons 193-224)
Fighting game excellence

### Tier 8: Action RPG - Legacy (Lessons 225-256)
Epic adventure with all systems mastered

### Tier 9: Roguelike - Legacy (Lessons 257-288)
Ultimate procedural dungeon crawler

### Tier 10: Open-World Adventure - Legacy (Lessons 289-320)
Living breathing game world

### Tier 11: Magnum Opus Project 1 (Lessons 321-352)
Student's choice - any genre, commercial quality

### Tier 12: Magnum Opus Project 2 (Lessons 353-384)
Student's choice - push technical boundaries

### Tier 13: Magnum Opus Project 3 (Lessons 385-416)
Student's choice - innovative mechanics

### Tier 14: Magnum Opus Project 4 (Lessons 417-448)
Student's choice - artistic vision

### Tier 15: Portfolio Showcase (Lessons 449-480)
Compilation of best work with professional presentation

### Tier 16: Commercial Release Preparation (Lessons 481-512)
Marketing, distribution, preservation for modern platforms

---

## Genre Lifecycle Roadmap

### All-Phase Genres (Phases 1-8)
These genres appear in all 8 phases with increasing sophistication:

1. **Horizontal Shooter** - Space shooters → R-Type quality → Genre-defining
2. **Platform Game** - Simple jumpers → Multi-screen → Metroidvania-adjacent
3. **Vertical Shooter** - Basic shmups → Bullet patterns → Genre perfection
4. **Run 'n' Gun** - Walking shooters → Destructible environments → Ultimate action
5. **Racing** - Top-down → 3D perspective → Outrun quality

### Evolving Genres

#### Maze Chase → Multi-Screen Maze → Isometric Adventure
- **Phase 1:** Pac-Man style single-screen maze
- **Phase 2:** Multi-screen connected maze with keys/doors
- **Phase 3-4:** Isometric adventure (Knight Lore style)
- **Phase 5+:** Absorbed into Isometric Action-Adventure

#### Adventure → Metroidvania
- **Phase 1:** Text adventure with simple graphics
- **Phase 2:** Enhanced graphics, simple parser
- **Phase 3:** Dropped (text-based)
- **Phase 5+:** Reborn as Metroidvania (connected world exploration)

#### Flip-Screen Platform → Isometric Platformer
- **Phase 2:** Manic Miner-style screen-by-screen
- **Phase 3:** Isometric perspective platforming
- **Phase 4+:** Merged into main platformer genre

### Phase-Limited Genres

#### Phase 1-2 Only
- **Breakout:** Brick-breaking (foundational, not carried forward)
- **Pong:** Two-player ball game (teaching tool only)
- **Snake:** Growing tail game (too simple for later phases)
- **Block Puzzle:** Falling blocks (evolved into puzzle-platformer)
- **Lunar Lander:** Physics lander (mechanics absorbed into other genres)
- **Bomber:** Drop bombs game (mechanics used in other shooters)
- **Submarine Game:** Underwater combat (mechanics evolved)

#### Phase 1 Only
- **Target Shooter:** Shooting gallery (too simple, mechanics reused)

#### Phase 2-3 Only
- **Collect-Em-Up:** Jetpac-style collection (mechanics absorbed)
- **Jetpack Game:** Thrust gameplay (evolved into other genres)
- **Frogger Clone:** Road crossing (too specific)
- **Climbing Game:** Vertical climbing (merged into platformers)
- **Defence Game:** Base defense (evolved into Tower Defense briefly)
- **Maze Builder:** Dynamic maze modification (too niche)

#### Phase 3 Only
- **Diagonal Shooter:** Zaxxon-style perspective (mechanics absorbed)
- **Space Combat:** Elite-lite (too ambitious for continued focus)
- **Stealth Platformer:** Shadow mechanics (absorbed into Action RPG)
- **Tactical Action:** Unit control (brief experiment)
- **Vector Shooter:** Asteroids-style (aesthetic choice, not sustained)

### Emerging Genres by Phase

#### Phase 2 Introductions
- **Collect-Em-Up:** Jetpac-inspired gameplay
- **Jetpack Game:** Thrust/gravity mechanics
- **Run 'n' Gun:** Walking shooter (Commando) - **CONTINUES TO PHASE 8**
- **Climbing Game:** Donkey Kong-style
- **Defence Game:** Protect the base
- **Flip-Screen Platform:** Manic Miner-style
- **Maze Builder:** Dynamic maze gameplay

#### Phase 3 Introductions
- **Isometric Adventure:** Knight Lore-style - **CONTINUES TO PHASE 4**
- **Isometric Platformer:** 3D perspective platforming
- **Isometric Action-Adventure:** Combat + puzzles - **CONTINUES TO PHASE 5**
- **Beat 'Em Up:** Side-scrolling fighting - **CONTINUES TO PHASE 8**
- **Diagonal Shooter:** Zaxxon perspective
- **Arcade Sports:** Football/soccer - **CONTINUES TO PHASE 4**
- **Space Combat:** Elite-style trading
- **Stealth Platformer:** Detection mechanics
- **Tactical Action:** Strategic unit control
- **Vector Shooter:** Wire-frame graphics

#### Phase 4 Introductions
- **Light Gun Shooter:** Operation Wolf-style
- **Puzzle-Platformer:** Logic + jumping
- **Action RPG:** Real-time RPG combat - **CONTINUES TO PHASE 8**

#### Phase 5 Introductions
- **Metroidvania:** Connected world exploration - **CONTINUES TO PHASE 8**
- **Combat Flight Sim:** 3D cockpit combat
- **Cinematic Platformer:** Prince of Persia-style
- **Roguelike:** Procedural dungeons - **CONTINUES TO PHASE 8**

#### Phase 6 Introductions
- **Physics Puzzle:** Lemmings/Pang-style
- **Open-World Adventure:** Non-linear exploration - **CONTINUES TO PHASE 8**
- **Arcade Collection:** Multi mini-games

### Genre Count by Phase
- **Phase 1:** 16 genres (foundation)
- **Phase 2:** 16 genres (8 enhanced, 2 evolved, 6 new, 8 dropped)
- **Phase 3:** 16 genres (6 core, 2 evolved, 8 new, 8 dropped)
- **Phase 4:** 16 genres (6 core, 3 continued, 3 new, 7 dropped)
- **Phase 5:** 16 genres (5 core, 4 continued, 3 new, 7 dropped)
- **Phase 6:** 16 genres (5 core, 4 continued, 3 new, 7 dropped)
- **Phase 7:** 16 genres (5 core, 5 continued, 0 new, 6 dropped)
- **Phase 8:** 16 genres (5 core, 5 continued, 6 capstone)

---

## ZX Spectrum-Specific Technical Notes

### Attribute Clash
The ZX Spectrum's color system assigns a single color attribute (ink, paper, bright, flash) to each 8×8 pixel block. This creates "attribute clash" when sprites overlap these boundaries.

**Mitigation Strategies by Phase:**
- **Phase 1-2:** Monochrome sprites, careful positioning
- **Phase 3-4:** Pre-shifted sprite masks, strategic color choice
- **Phase 5-8:** Multi-color sprite routines, attribute-friendly designs

### Software Sprites
Unlike C64's hardware sprites, ZX Spectrum requires all sprite rendering in software.

**Evolution:**
- **Phase 1:** Character-based sprites using UDG
- **Phase 2:** XOR drawing for fast movement
- **Phase 3:** Masked sprites with background preservation
- **Phase 4-5:** Optimized machine code blitting
- **Phase 6-8:** Multi-color sprites with attribute management

### Sound Capabilities
The 48K Spectrum has only a 1-bit beeper, while 128K models add the AY-3-8912 sound chip.

**Progression:**
- **Phase 1:** Simple BEEP commands
- **Phase 2:** Pulse-width modulation effects
- **Phase 3:** Multi-channel beeper music engines
- **Phase 4:** AY chip music (128K) or advanced beeper
- **Phase 5-8:** Sample playback, complex music drivers

### Memory Management
- **48K Model:** Careful memory optimization, overlays
- **128K Model:** Memory banking for larger games, better sound

---

## Assessment & Progression

**Within Each Tier (32 Lessons):**
- Lessons 1-10: Core mechanics implementation
- Lessons 11-15: Game loop, basic playability
- Lessons 16-20: **Playable milestone** - fully functional game
- Lessons 21-32: Polish, effects, content variety

**Between Tiers:**
- Complete playable game from previous tier
- Demonstrate understanding of key techniques
- Create one variation/mod showing creativity

**Between Phases:**
- Portfolio of 16 playable games (one from each tier)
- Technical showcase demonstrating phase-appropriate quality
- Self-assessment of readiness for next complexity level

---

## Historical Context & Authenticity

Each phase maps to actual ZX Spectrum development eras:

- **Phase 1 (1982-1983):** Launch era, learning the hardware
- **Phase 2 (1983-1984):** Improved techniques, commercial viability
- **Phase 3 (1985-1986):** Golden age, isometric revolution
- **Phase 4 (1987-1988):** Commercial maturity
- **Phase 5 (1988-1989):** Technical mastery
- **Phase 6 (1989-1990):** Genre innovation
- **Phase 7 (1990-1991):** Platform perfection
- **Phase 8 (1991-1992):** Legacy titles

Games teach not just programming, but the historical evolution of game development on this iconic platform.

---

*This curriculum represents 4,096 lessons of progressive ZX Spectrum game development education, from first programs to commercial-quality games.*
