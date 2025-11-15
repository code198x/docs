# Commodore Amiga Curriculum

## Overview

This curriculum covers game development for the Commodore Amiga across 8 phases of increasing complexity, from foundational 68000 assembly games through sophisticated commercial-quality titles that showcased the platform's legendary capabilities.

**Total Structure:**
- **8 Phases** (2^3) - Technical progression from 1985-style to 1994-style games
- **16 Tiers per Phase** (2^4) - 16 different game genres/types
- **32 Lessons per Tier** (2^5) - Complete game development cycle
- **Total: 4,096 lessons** (2^12)

**Learning Approach:**
- **Spiral Learning:** Teach minimum needed first, deepen understanding later
- **Quick Interaction:** Lessons 2-3 have interactive elements
- **Playable Early:** Lessons 15-20 produce a playable game
- **Polish Phase:** Lessons 21-32 add effects, variety, commercial quality

**Amiga Technical Context:**
- **CPU:** Motorola 68000 @ 7.16 MHz (16/32-bit architecture)
- **Graphics:** OCS/ECS/AGA chipset with hardware sprites, blitter, copper
- **Resolution:** Multiple modes (320×256 low-res to 640×512 high-res interlaced)
- **Colors:** 4096 color palette, up to 64 on-screen (HAM mode: 4096 simultaneously)
- **Sound:** Paula (4 channels, 8-bit PCM samples, stereo)
- **Sprites:** 8 hardware sprites (16-pixel wide), reusable via multiplexing
- **Blitter:** Hardware acceleration for graphics operations
- **Copper:** Co-processor for display list manipulation
- **Memory:** 512KB standard (expandable to 9MB on OCS/ECS, 2MB chip RAM on AGA)
- **Storage:** 3.5" floppy disk (880KB), hard drives common

---

## Phase 1: Foundation (1985-1986 Era)

**Target Quality:** Early Amiga games - learning 68000 assembly and custom chipset basics. Think early *Defender of the Crown*, *Marble Madness*, simple arcade ports.

**Technical Focus:**
- 68000 assembly fundamentals
- Hardware sprite setup and control
- Playfield initialization
- Copper list basics
- Simple collision detection
- Paula sound basics (simple samples)
- Joystick/keyboard input via CIA
- Blitter line drawing and fills

**16 Game Genres (Phase 1):**

### Tier 1: Space Shooter (Lessons 1-32)
**Game:** Single-screen space shooter (player ship vs enemies)
**Playable by:** Lesson 15-20
**Key Techniques:** Hardware sprites, joystick input, movement, shooting, collision
**Amiga Specific:** Sprite DMA setup, simple copper list, 4-channel shot sounds

### Tier 2: Breakout (Lessons 33-64)
**Game:** Brick-breaking paddle game
**Playable by:** Lesson 48-52
**Key Techniques:** Ball physics, paddle control, brick destruction via blitter
**Amiga Specific:** Blitter rectangle fills, sprite multiplexing for multiple balls

### Tier 3: Platform Game (Lessons 65-96)
**Game:** Single-screen platformer (jump between platforms, collect items)
**Playable by:** Lesson 80-84
**Key Techniques:** Gravity simulation, jumping physics, tile-based collision
**Amiga Specific:** Hardware scrolling registers, sprite animation frames

### Tier 4: Puzzle Game (Lessons 97-128)
**Game:** Match-3 or falling block puzzle
**Playable by:** Lesson 112-116
**Key Techniques:** Grid logic, line clearing, pattern matching
**Amiga Specific:** Blitter copies for grid rendering, copper palette effects

### Tier 5: Horizontal Shooter (Lessons 129-160)
**Game:** Side-scrolling space shooter
**Playable by:** Lesson 144-148
**Key Techniques:** Horizontal scrolling, enemy waves, simple patterns
**Amiga Specific:** Playfield scrolling, sprite reuse, parallax starfield

### Tier 6: Racing (Lessons 161-192)
**Game:** Top-down racing game
**Playable by:** Lesson 176-180
**Key Techniques:** Sprite rotation (pre-calculated), track scrolling, AI opponents
**Amiga Specific:** Copper-based road rendering, sprite scaling tables

### Tier 7: Vertical Shooter (Lessons 193-224)
**Game:** Top-down vertical scrolling shooter
**Playable by:** Lesson 208-212
**Key Techniques:** Vertical scrolling, formation enemies, bullet patterns
**Amiga Specific:** Dual playfield for background layers, sprite multiplexing

### Tier 8: Maze Game (Lessons 225-256)
**Game:** 2D maze exploration (Pac-Man inspired)
**Playable by:** Lesson 240-244
**Key Techniques:** Tile-based maze, AI pathfinding, item collection
**Amiga Specific:** Character-based rendering using blitter, wrap-around scrolling

### Tier 9: Artillery (Lessons 257-288)
**Game:** Scorched Earth-style angle/power shooting
**Playable by:** Lesson 272-276
**Key Techniques:** Trajectory calculation, destructible terrain, wind physics
**Amiga Specific:** Blitter-based terrain modification, vector drawing

### Tier 10: Pong (Lessons 289-320)
**Game:** Classic two-paddle ball game
**Playable by:** Lesson 304-308
**Key Techniques:** Two-player input, ball physics, score display
**Amiga Specific:** Hardware sprites for paddles/ball, simple collision

### Tier 11: Target Shooter (Lessons 321-352)
**Game:** Shooting gallery with moving targets
**Playable by:** Lesson 336-340
**Key Techniques:** Target patterns, timing, scoring system
**Amiga Specific:** Sprite animation, mouse input via CIA

### Tier 12: Snake (Lessons 353-384)
**Game:** Growing snake collecting food
**Playable by:** Lesson 368-372
**Key Techniques:** Dynamic tail growth, self-collision, food spawning
**Amiga Specific:** Blitter-based snake rendering, fast screen updates

### Tier 13: Defender Clone (Lessons 385-416)
**Game:** Protect humans from alien abduction (bidirectional)
**Playable by:** Lesson 400-404
**Key Techniques:** Wrap-around scrolling, radar display, rescue mechanics
**Amiga Specific:** Bidirectional playfield scrolling, mini-map rendering

### Tier 14: Lunar Lander (Lessons 417-448)
**Game:** Physics-based landing game
**Playable by:** Lesson 432-436
**Key Techniques:** Thrust physics, fuel management, terrain collision
**Amiga Specific:** Vector terrain using blitter lines, particle thrust effects

### Tier 15: Flick-Screen Platformer (Lessons 449-480)
**Game:** Screen-by-screen platformer (Manic Miner-style)
**Playable by:** Lesson 464-468
**Key Techniques:** Screen transitions, hazards, precise timing
**Amiga Specific:** Copper-based screen wipes, animated tile hazards

### Tier 16: Fixed Shooter (Lessons 481-512)
**Game:** Space Invaders-style fixed formation shooter
**Playable by:** Lesson 496-500
**Key Techniques:** Formation movement, shields, progressive difficulty
**Amiga Specific:** Sprite reuse for formations, copper color cycling

---

## Phase 2: Enhancement (1987-1988 Era)

**Target Quality:** Maturing Amiga development - multi-layered parallax, complex sprite use, refined copper effects. Think *Shadow of the Beast*, *Menace*, *Blood Money*.

**Technical Focus:**
- Advanced copper list programming
- Multi-layered parallax scrolling
- Sprite multiplexing techniques
- Blitter optimization
- Dual playfield graphics
- Trackloader basics
- Advanced collision detection
- Simple line-based 3D

**Genre Mix:**
- **Enhanced from Phase 1:** Space Shooter, Horizontal Shooter, Platform Game, Vertical Shooter, Racing, Maze Game
- **Evolved:** Flick-Screen Platformer → Multi-Screen Platformer
- **New for Phase 2:** Run 'n' Gun, Beat 'Em Up, Isometric Action
- **Dropped:** Breakout, Puzzle Game, Artillery, Pong, Target Shooter, Snake, Defender Clone, Lunar Lander, Fixed Shooter

### Tier 1: Space Shooter - Enhanced (Lessons 1-32)
Multiple enemy types, power-ups, large sprites, animated explosions

### Tier 2: Horizontal Shooter - Enhanced (Lessons 33-64)
Multi-layer parallax scrolling, ground targets, end-of-level bosses

### Tier 3: Platform Game - Enhanced (Lessons 65-96)
Multi-screen scrolling, varied enemies, collectibles, secret areas

### Tier 4: Run 'n' Gun (Lessons 97-128)
**New Genre:** Commando-style overhead walking shooter with 8-way movement

### Tier 5: Vertical Shooter - Enhanced (Lessons 129-160)
Formation attacks, bonus stages, weapon variety, dramatic bosses

### Tier 6: Beat 'Em Up (Lessons 161-192)
**New Genre:** Side-scrolling fighting (Double Dragon-style), multiple enemies

### Tier 7: Racing - Enhanced (Lessons 193-224)
Pseudo-3D perspective (Out Run-style), multiple tracks, opponents

### Tier 8: Multi-Screen Platformer (Lessons 225-256)
**Evolution:** Connected screens with backtracking, keys/doors, map system

### Tier 9: Maze Game - Enhanced (Lessons 257-288)
Multi-level maze, complex AI, power-ups, boss encounters

### Tier 10: Isometric Action (Lessons 289-320)
**New Genre:** Zaxxon-style isometric perspective action game

### Tier 11: Puzzle-Platformer (Lessons 321-352)
**New Genre:** Platform mechanics with Sokoban-style environmental puzzles

### Tier 12: Collect-Em-Up (Lessons 353-384)
**New Genre:** Jetpac-style collect and build objectives

### Tier 13: Climb-and-Avoid (Lessons 385-416)
**New Genre:** Donkey Kong-style vertical climbing with obstacles

### Tier 14: Flight Combat (Lessons 417-448)
**New Genre:** Side-view dogfighting with terrain avoidance

### Tier 15: Twin-Stick Shooter (Lessons 449-480)
**New Genre:** Robotron-style arena shooter with multi-directional firing

### Tier 16: Defense Game (Lessons 481-512)
**New Genre:** Defend base from waves of attackers (Missile Command-inspired)

---

## Phase 3: Sophistication (1988-1989 Era)

**Target Quality:** Amiga's golden age - stunning visuals, complex gameplay, advanced copper effects. Think *Xenon 2*, *Speedball 2*, *R-Type*, *Rainbow Islands*.

**Technical Focus:**
- Advanced blitter routines
- Copper effects (raster bars, sky gradients, sprite splits)
- Sprite multiplexing mastery
- Trackloaders for seamless audio
- Advanced scrolling techniques
- Line-based 3D rendering
- Complex enemy AI patterns

**Genre Mix:**
- **All-Phase Core:** Horizontal Shooter, Platform Game, Vertical Shooter, Run 'n' Gun, Racing, Beat 'Em Up
- **Continued:** Multi-Screen Platformer, Isometric Action
- **New for Phase 3:** Dungeon Crawler, Point-and-Click Adventure, Strategy Game, Top-Down Action
- **Dropped:** Space Shooter, Maze Game, Puzzle-Platformer, Collect-Em-Up, Climb-and-Avoid, Flight Combat, Twin-Stick Shooter, Defense Game

### Tier 1: Horizontal Shooter - Advanced (Lessons 1-32)
Xenon 2 quality: complex patterns, innovative weapons, huge sprites, techno aesthetic

### Tier 2: Platform Game - Advanced (Lessons 33-64)
Rainbow Islands quality: creative mechanics per level, polished scrolling

### Tier 3: Vertical Shooter - Advanced (Lessons 65-96)
SWIV quality: ground/air targets, weapon variety, memorable bosses

### Tier 4: Run 'n' Gun - Advanced (Lessons 97-128)
8-directional shooting, destructible scenery, vehicle sections

### Tier 5: Racing - Advanced (Lessons 129-160)
Lotus quality: smooth pseudo-3D, detailed circuits, split-screen two-player

### Tier 6: Beat 'Em Up - Advanced (Lessons 161-192)
Golden Axe quality: magic attacks, weapons, mounts, depth mechanics

### Tier 7: Multi-Screen Platformer - Advanced (Lessons 193-224)
Large connected world, item-based progression, boss battles

### Tier 8: Isometric Action - Advanced (Lessons 225-256)
Complex isometric movement, layered sprites, height mechanics

### Tier 9: Dungeon Crawler (Lessons 257-288)
**New Genre:** First-person dungeon exploration (Dungeon Master-inspired)

### Tier 10: Point-and-Click Adventure (Lessons 289-320)
**New Genre:** Mouse-driven graphic adventure with inventory and dialogue

### Tier 11: Strategy Game (Lessons 321-352)
**New Genre:** Real-time or turn-based tactical combat with units

### Tier 12: Top-Down Action (Lessons 353-384)
**New Genre:** Gauntlet-style multi-directional dungeon action

### Tier 13: Combat Racer (Lessons 385-416)
**New Genre:** Racing with weapons (Road Rash-style)

### Tier 14: Hack 'n' Slash (Lessons 417-448)
**New Genre:** Barbarian-style one-on-one combat with gore effects

### Tier 15: God Game (Lessons 449-480)
**New Genre:** Populous-style terrain manipulation and indirect control

### Tier 16: Sports Game (Lessons 481-512)
**New Genre:** Football/soccer with tactical controls (Kick Off-inspired)

---

## Phase 4: Commercial Quality (1989-1990 Era)

**Target Quality:** Commercial-grade polish, innovation, memorable presentation. Think *Turrican*, *Shadow of the Beast II*, *The Secret of Monkey Island*, *Speedball 2*.

**Technical Focus:**
- Optimized 68000 assembly techniques
- HAM mode graphics (extra colors)
- Advanced copper programming
- Sample-based music with mixing
- Memory management and overlays
- Compression techniques
- Professional production values

**Genre Mix:**
- **All-Phase Core:** Horizontal Shooter, Platform Game, Vertical Shooter, Run 'n' Gun, Racing, Beat 'Em Up
- **Continued:** Point-and-Click Adventure, Dungeon Crawler, Strategy Game, Isometric Action
- **New for Phase 4:** Action RPG, Metroidvania, Management Sim
- **Dropped:** Multi-Screen Platformer, Top-Down Action, Combat Racer, Hack 'n' Slash, God Game, Sports Game

### Tier 1: Horizontal Shooter - Commercial (Lessons 1-32)
R-Type quality: memorable bosses, perfect difficulty curve, iconic presentation

### Tier 2: Platform Game - Commercial (Lessons 33-64)
Turrican quality: exploration + action, huge levels, secrets, power-ups

### Tier 3: Metroidvania (Lessons 65-96)
**New Genre:** Connected world with ability-gating and backtracking

### Tier 4: Vertical Shooter - Commercial (Lessons 97-128)
Polished bullet patterns, scoring chains, dramatic boss encounters

### Tier 5: Run 'n' Gun - Commercial (Lessons 129-160)
Chaos Engine aesthetic: co-op mechanics, unique characters, variety

### Tier 6: Racing - Commercial (Lessons 161-192)
Formula One quality: realistic handling, career mode, detailed cars

### Tier 7: Beat 'Em Up - Commercial (Lessons 193-224)
Final Fight quality: depth of combat, enemy variety, environmental attacks

### Tier 8: Point-and-Click Adventure - Commercial (Lessons 225-256)
Monkey Island quality: humor, complex puzzles, multiple solutions, dialogue trees

### Tier 9: Dungeon Crawler - Commercial (Lessons 257-288)
Eye of the Beholder quality: party management, spell system, complex dungeons

### Tier 10: Strategy Game - Commercial (Lessons 289-320)
Dune II quality: RTS mechanics, base building, resource management, unit production

### Tier 11: Isometric Action - Commercial (Lessons 321-352)
Head Over Heels quality: puzzle-solving, character switching, precise control

### Tier 12: Action RPG (Lessons 353-384)
**New Genre:** Real-time combat with stats, inventory, quests (Zelda-inspired)

### Tier 13: Management Sim (Lessons 385-416)
**New Genre:** Railroad Tycoon-style economic simulation with objectives

### Tier 14: Cinematic Platformer (Lessons 417-448)
**New Genre:** Another World-style rotoscoped animation, cinematic presentation

### Tier 15: Flight Sim (Lessons 449-480)
**New Genre:** 3D flight simulation with mission objectives

### Tier 16: Tactical RPG (Lessons 481-512)
**New Genre:** Turn-based tactical grid combat with character progression

---

## Phase 5: Mastery (1990-1991 Era)

**Target Quality:** Pushing OCS/ECS limits, early AGA exploration. Think *Agony*, *Apidya*, *The Chaos Engine*, *Lemmings*.

**Technical Focus:**
- Maximum 68000 optimization
- HAM-8 mode (early AGA)
- Complex copper effects
- Advanced blitter techniques
- Procedural generation
- Advanced physics engines
- Sample mixing and effects
- Trackdisk streaming

**Genre Mix:**
- **All-Phase Core:** Horizontal Shooter, Platform Game, Vertical Shooter, Run 'n' Gun, Racing, Beat 'Em Up
- **Continued:** Point-and-Click Adventure, Metroidvania, Strategy Game, Action RPG
- **New for Phase 5:** FPS (First-Person Shooter), Roguelike, Puzzle Action
- **Dropped:** Dungeon Crawler, Isometric Action, Management Sim, Cinematic Platformer, Flight Sim, Tactical RPG

### Tier 1: Horizontal Shooter - Master (Lessons 1-32)
Agony quality: organic enemies, HAM graphics, atmospheric music, technical showcase

### Tier 2: Platform Game - Master (Lessons 33-64)
Apidya quality: gorgeous graphics, creative design, smooth gameplay, variety

### Tier 3: Metroidvania - Advanced (Lessons 65-96)
Large interconnected world, multiple abilities, sequence breaking

### Tier 4: Vertical Shooter - Master (Lessons 97-128)
Perfect bullet patterns, deep scoring systems, rank-based difficulty

### Tier 5: Run 'n' Gun - Master (Lessons 129-160)
Chaos Engine quality: steampunk perfection, balanced co-op, strategic depth

### Tier 6: Racing - Master (Lessons 161-192)
Grand Prix quality: realistic handling, weather effects, pit strategy

### Tier 7: Beat 'Em Up - Master (Lessons 193-224)
Streets of Rage quality: combo systems, weapons, special moves, depth

### Tier 8: Point-and-Click Adventure - Master (Lessons 225-256)
Simon the Sorcerer quality: voice samples, detailed graphics, humor, complexity

### Tier 9: Strategy Game - Master (Lessons 257-288)
Perfect RTS balance, fog of war, diverse factions, strategic depth

### Tier 10: Action RPG - Advanced (Lessons 289-320)
Equipment progression, magic system, open world exploration, quests

### Tier 11: FPS (First-Person Shooter) (Lessons 321-352)
**New Genre:** Wolfenstein 3D-style raycasting engine with texture mapping

### Tier 12: Roguelike (Lessons 353-384)
**New Genre:** Procedural dungeons, permadeath, deep systems (NetHack-inspired)

### Tier 13: Puzzle Action (Lessons 385-416)
**New Genre:** Lemmings-style guide characters using assigned skills

### Tier 14: Artillery Strategy (Lessons 417-448)
**New Genre:** Worms prototype - turn-based destructible terrain combat

### Tier 15: Twin-Stick Arena (Lessons 449-480)
**New Genre:** Smash TV-style arena shooter with dual joystick

### Tier 16: Physics Puzzler (Lessons 481-512)
**New Genre:** Pang-style physics-based puzzle challenges

---

## Phase 6: Innovation (1991-1992 Era)

**Target Quality:** Genre-defining games with unique mechanics. Think *Superfrog*, *Body Blows*, *Alien Breed*, *Sensible World of Soccer*.

**Technical Focus:**
- AGA chipset optimization
- 256-color modes
- CD³² integration (CD-ROM)
- Advanced sample mixing
- Procedural content generation
- Complex particle systems
- Professional cinematics

**Genre Mix:**
- **All-Phase Core:** Horizontal Shooter, Platform Game, Vertical Shooter, Run 'n' Gun, Racing, Beat 'Em Up
- **Continued:** Point-and-Click Adventure, Metroidvania, Strategy Game, Action RPG, FPS, Roguelike
- **New for Phase 6:** Fighting Game, Open-World RPG
- **Dropped:** Puzzle Action, Artillery Strategy, Twin-Stick Arena, Physics Puzzler

### Tier 1: Horizontal Shooter - Ultimate (Lessons 1-32)
Genre-defining quality, innovative mechanics, unforgettable presentation

### Tier 2: Platform Game - Ultimate (Lessons 33-64)
Superfrog quality: smooth 256-color graphics, creative power-ups, polished

### Tier 3: Metroidvania - Master (Lessons 65-96)
Symphony of the Night-level interconnection (scaled to Amiga capabilities)

### Tier 4: Vertical Shooter - Ultimate (Lessons 97-128)
Genre perfection with innovation and memorable design

### Tier 5: Run 'n' Gun - Ultimate (Lessons 129-160)
Alien Breed quality: atmospheric, co-op perfection, tension and variety

### Tier 6: Racing - Ultimate (Lessons 161-192)
Genre excellence with track variety and presentation

### Tier 7: Beat 'Em Up - Ultimate (Lessons 193-224)
Body Blows quality: deep fighting mechanics, special moves, tournament balance

### Tier 8: Fighting Game (Lessons 225-256)
**New Genre:** Street Fighter II-style one-on-one with special move systems

### Tier 9: Point-and-Click Adventure - Ultimate (Lessons 257-288)
Beneath a Steel Sky quality: cinematic, CD-quality voice, complex narrative

### Tier 10: Strategy Game - Ultimate (Lessons 289-320)
Settlers quality: economic simulation, resource chains, peaceful expansion

### Tier 11: Action RPG - Master (Lessons 321-352)
Full equipment system, magic, quest network, NPC interaction

### Tier 12: FPS - Advanced (Lessons 353-384)
Doom-inspired with height variation, lighting effects, complex level design

### Tier 13: Roguelike - Advanced (Lessons 385-416)
Multiple classes, complex magic, deep procedural generation

### Tier 14: Open-World RPG (Lessons 417-448)
**New Genre:** Non-linear exploration, living world, dynamic events

### Tier 15: Stealth Action (Lessons 449-480)
**New Genre:** Metal Gear-style line-of-sight stealth mechanics

### Tier 16: Sports Sim (Lessons 481-512)
**New Genre:** Sensible World of Soccer - career mode, management, tactics

---

## Phase 7: Perfection (1992-1993 Era)

**Target Quality:** Best-of-platform showcase utilizing every hardware trick. Think *Lionheart*, *Banshee*, *Disposable Hero*, *The Strangers*.

**Technical Focus:**
- Maximum AGA optimization
- Copper effects mastery
- Blitter perfection
- CD³² feature utilization
- Professional audio production
- Complex AI systems
- Memory banking mastery

**Genre Mix:**
- **All-Phase Core:** Horizontal Shooter, Platform Game, Vertical Shooter, Run 'n' Gun, Racing, Beat 'Em Up
- **Continued:** Point-and-Click Adventure, Metroidvania, Strategy Game, Action RPG, FPS, Roguelike, Fighting Game, Open-World RPG
- **New for Phase 7:** None (perfecting existing genres)
- **Dropped:** Stealth Action, Sports Sim

### Tier 1: Horizontal Shooter - Perfected (Lessons 1-32)
Lionheart quality: absolute technical showcase, artistic masterpiece

### Tier 2: Platform Game - Perfected (Lessons 33-64)
Ruff 'n' Tumble quality: perfect controls, gorgeous AGA graphics

### Tier 3: Metroidvania - Perfected (Lessons 65-96)
Ultimate exploration-platformer with perfect pacing and design

### Tier 4: Vertical Shooter - Perfected (Lessons 97-128)
Banshee quality: stunning AGA visuals, perfect gameplay balance

### Tier 5: Run 'n' Gun - Perfected (Lessons 129-160)
Disposable Hero quality: genre-defining overhead shooter

### Tier 6: Racing - Perfected (Lessons 161-192)
Ultimate racing experience on Amiga hardware

### Tier 7: Beat 'Em Up - Perfected (Lessons 193-224)
Perfect fighting mechanics with depth and variety

### Tier 8: Fighting Game - Advanced (Lessons 225-256)
Tournament-quality balance, complex move sets, special systems

### Tier 9: Point-and-Click Adventure - Perfected (Lessons 257-288)
Ultimate adventure game with cinematic quality throughout

### Tier 10: Strategy Game - Perfected (Lessons 289-320)
Settlers II quality: economic depth, beautiful graphics, addictive

### Tier 11: Action RPG - Perfected (Lessons 321-352)
Epic adventure with all systems mastered and balanced

### Tier 12: FPS - Master (Lessons 353-384)
Advanced 3D rendering, complex design, variety and polish

### Tier 13: Roguelike - Master (Lessons 385-416)
Ultimate procedural crawler with emergent gameplay depth

### Tier 14: Open-World RPG - Advanced (Lessons 417-448)
Living world with NPC schedules, dynamic events, freedom

### Tier 15: Artillery Strategy (Lessons 449-480)
Worms-style turn-based destructible terrain with advanced physics

### Tier 16: Tower Defense (Lessons 481-512)
Strategic defender placement with wave management and upgrade systems

---

## Phase 8: Legacy (1993-1994 Era)

**Target Quality:** Final generation defining ultimate Amiga capability. Think *Benefactor*, *Pinball Fantasies*, *Alien Breed 3D*, late AGA masterpieces.

**Technical Focus:**
- Every optimization technique known
- Custom chipset programming mastery
- AGA mode full utilization
- Professional production quality
- CD³² complete feature set
- Hybrid innovative designs
- Commercial-release standards

**Genre Mix:**
- **All-Phase Core:** Horizontal Shooter, Platform Game, Vertical Shooter, Run 'n' Gun, Racing, Beat 'Em Up
- **Continued:** Point-and-Click Adventure, Metroidvania, Strategy Game, Action RPG, FPS, Roguelike, Fighting Game, Open-World RPG
- **New Advanced:** God Game, 4X Strategy

### Tier 1: Horizontal Shooter - Legacy (Lessons 1-32)
Ultimate showcase of the genre on Amiga platform

### Tier 2: Platform Game - Legacy (Lessons 33-64)
Genre-defining platforming with commercial quality

### Tier 3: Metroidvania - Legacy (Lessons 65-96)
Defining example of exploration-platformer excellence

### Tier 4: Vertical Shooter - Legacy (Lessons 97-128)
Shmup perfection with innovation and polish

### Tier 5: Run 'n' Gun - Legacy (Lessons 129-160)
Ultimate top-down shooter masterclass

### Tier 6: Racing - Legacy (Lessons 161-192)
Genre-defining racing on Amiga hardware

### Tier 7: Beat 'Em Up - Legacy (Lessons 193-224)
Fighting excellence with depth and variety

### Tier 8: Fighting Game - Legacy (Lessons 225-256)
Tournament-quality one-on-one combat perfection

### Tier 9: Point-and-Click Adventure - Legacy (Lessons 257-288)
Cinematic adventure game perfection

### Tier 10: Strategy Game - Legacy (Lessons 289-320)
Ultimate strategic depth and presentation

### Tier 11: Action RPG - Legacy (Lessons 321-352)
Epic adventure with commercial quality and depth

### Tier 12: FPS - Legacy (Lessons 353-384)
Alien Breed 3D quality: advanced 3D on Amiga hardware

### Tier 13: Roguelike - Legacy (Lessons 385-416)
Ultimate procedural gameplay with endless replayability

### Tier 14: Open-World RPG - Legacy (Lessons 417-448)
Living breathing game world with complete freedom

### Tier 15: God Game (Lessons 449-480)
Populous-style terrain manipulation, indirect control, sophisticated AI systems

### Tier 16: 4X Strategy (Lessons 481-512)
Civilization-inspired expand/explore/exploit/exterminate with diplomacy and tech trees

---

## Genre Lifecycle Roadmap

### All-Phase Genres (Phases 1-8)
These genres appear in all 8 phases with increasing sophistication:

1. **Horizontal Shooter** - Basic shooters → Xenon 2 → Agony → Lionheart perfection
2. **Platform Game** - Simple jumpers → Rainbow Islands → Turrican → Ruff 'n' Tumble mastery
3. **Vertical Shooter** - Basic shmups → SWIV → Banshee perfection
4. **Run 'n' Gun** - Overhead shooters → Chaos Engine → Alien Breed → Disposable Hero
5. **Racing** - Top-down → Lotus pseudo-3D → Formula One → Ultimate realism
6. **Beat 'Em Up** - Basic fighting → Golden Axe → Final Fight → Body Blows depth

### Evolving Genres

#### Multi-Screen Platformer → Metroidvania
- **Phase 2:** Connected screens with backtracking
- **Phase 3:** Large connected world with items
- **Phase 4+:** Full Metroidvania with ability-gating

#### Maze Game → Dungeon Crawler
- **Phase 1-2:** 2D maze exploration
- **Phase 3-4:** First-person dungeon crawler (Dungeon Master)
- **Phase 5+:** Evolved into FPS genre

### Phase-Limited Genres

#### Phase 1 Only
- **Breakout:** Teaching blitter basics
- **Puzzle Game:** Grid logic fundamentals
- **Artillery:** Trajectory physics
- **Pong:** Simple sprite collision
- **Target Shooter:** Basic patterns
- **Snake:** Dynamic rendering
- **Defender Clone:** Wrap-around scrolling
- **Lunar Lander:** Physics simulation
- **Fixed Shooter:** Formation logic

#### Phase 2 Only
- **Puzzle-Platformer:** Merged into main platformer genre
- **Collect-Em-Up:** Mechanics absorbed
- **Climb-and-Avoid:** Vertical mechanics integrated
- **Flight Combat:** Side-view dogfighting
- **Twin-Stick Shooter:** Dual-control mechanics
- **Defense Game:** Base defense patterns

#### Phase 3 Only
- **Top-Down Action:** Gauntlet-style mechanics
- **Combat Racer:** Road Rash weapons
- **Hack 'n' Slash:** One-on-one combat
- **God Game:** Populous indirect control
- **Sports Game:** Kick Off mechanics

#### Phase 4-5 Only
- **Isometric Action:** Zaxxon/Head Over Heels perspective
- **Management Sim:** Economic simulation depth
- **Cinematic Platformer:** Another World rotoscoping
- **Flight Sim:** 3D flight simulation
- **Tactical RPG:** Grid-based tactics
- **Artillery Strategy:** Worms-style combat
- **Twin-Stick Arena:** Smash TV mechanics
- **Physics Puzzler:** Pang-style physics

#### Phase 6 Only
- **Stealth Action:** Line-of-sight mechanics
- **Sports Sim:** Career mode management

### Emerging Genres by Phase

#### Phase 2 Introductions
- **Run 'n' Gun:** Commando-style - **CONTINUES TO PHASE 8**
- **Beat 'Em Up:** Double Dragon-style - **CONTINUES TO PHASE 8**
- **Isometric Action:** Zaxxon perspective - **CONTINUES TO PHASE 4**

#### Phase 3 Introductions
- **Dungeon Crawler:** First-person - **CONTINUES TO PHASE 4**
- **Point-and-Click Adventure:** Graphic adventure - **CONTINUES TO PHASE 8**
- **Strategy Game:** RTS mechanics - **CONTINUES TO PHASE 8**

#### Phase 4 Introductions
- **Action RPG:** Real-time RPG - **CONTINUES TO PHASE 8**
- **Metroidvania:** Connected exploration - **CONTINUES TO PHASE 8**
- **Management Sim:** Economic simulation

#### Phase 5 Introductions
- **FPS (First-Person Shooter):** Raycasting 3D - **CONTINUES TO PHASE 8**
- **Roguelike:** Procedural dungeons - **CONTINUES TO PHASE 8**

#### Phase 6 Introductions
- **Fighting Game:** Street Fighter II-style - **CONTINUES TO PHASE 8**
- **Open-World RPG:** Non-linear exploration - **CONTINUES TO PHASE 8**

### Genre Count by Phase
- **Phase 1:** 16 genres (foundation, learning chipset)
- **Phase 2:** 16 genres (6 enhanced, 1 evolved, 9 new, 9 dropped)
- **Phase 3:** 16 genres (6 core, 2 continued, 8 new, 8 dropped)
- **Phase 4:** 16 genres (6 core, 4 continued, 3 new, 6 dropped)
- **Phase 5:** 16 genres (6 core, 4 continued, 3 new, 6 dropped)
- **Phase 6:** 16 genres (6 core, 6 continued, 2 new, 4 dropped)
- **Phase 7:** 16 genres (6 core, 8 continued, 0 new, 2 dropped)
- **Phase 8:** 16 genres (6 core, 8 continued, 2 new advanced)

---

## Integration with Vault and Pattern Library

### The Vault: Contextual Links

Lessons should link to Vault entries when mentioning:

**People:** Programmers, musicians, artists, designers
- *Example:* "...inspired by the Bitmap Brothers' visual style..."
- *Link to:* `/vault/people/bitmap-brothers`

**Companies:** Studios, publishers, hardware manufacturers
- *Example:* "...techniques developed by Team17..."
- *Link to:* `/vault/companies/team17`

**Games:** Specific titles used as examples
- *Example:* "...the parallax scrolling from Shadow of the Beast..."
- *Link to:* `/vault/games/shadow-of-the-beast`

**Techniques:** Programming methods and approaches
- *Example:* "...using copper list programming for palette effects..."
- *Link to:* `/vault/techniques/amiga-copper-effects`

**Hardware:** Chips and components being programmed
- *Example:* "...the Paula chip's sample playback capabilities..."
- *Link to:* `/vault/hardware/paula-chip`

**Cultural Context:** Movies, music, events for era context
- *Example:* "...reflecting the demoscene's influence on commercial games..."
- *Link to:* `/vault/culture/amiga-demoscene`

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

For a complete, production-ready blitter routine with optimization notes,
see [Pattern: Blitter Rectangle Fill](/patterns/amiga/rendering/blitter-rectangle-fill).
```

**Pattern Evolution:**
As patterns evolve across phases, reference the appropriate version:
- Phase 1: [Pattern: Hardware Sprites (Basic)](/patterns/amiga/rendering/hardware-sprite-basic)
- Phase 3: [Pattern: Hardware Sprites (Multiplexed)](/patterns/amiga/rendering/hardware-sprite-multiplexed)
- Phase 5: [Pattern: Hardware Sprites (AGA Enhanced)](/patterns/amiga/rendering/hardware-sprite-aga)

**Pattern Categories for Amiga:**
- **Rendering:** BOBs, hardware sprites, blitter, copper, dual playfield
- **Input:** Mouse, joystick, keyboard
- **Audio:** Paula sample playback, MOD music, sound mixing
- **Physics:** Collision detection, gravity, projectiles
- **AI:** Enemy behavior, pathfinding
- **Framework:** VBlank interrupts, game loops, state machines
- **Optimization:** 68000 optimizations, blitter usage, memory management

### Integration Example

**Lesson excerpt:**
```markdown
In this lesson, we're using the Copper co-processor to create palette effects.
The Copper is a specialized processor that can modify chip registers in sync
with the video beam, enabling effects like sky gradients and raster bars.

[...lesson content teaching the concept step by step...]

This technique was showcased spectacularly in Shadow of the Beast, which used
the Copper to create multi-layer parallax with unique palettes per layer.
Psygnosis games became known for pushing the Copper to its limits.

## Further Reading

**Pattern Library:**
- [Copper Palette Effects](/patterns/amiga/rendering/copper-palette-effects)
- [Multi-Layer Parallax](/patterns/amiga/rendering/parallax-multilayer)

**Vault:**
- [Copper Co-Processor](/vault/hardware/copper)
- [Shadow of the Beast](/vault/games/shadow-of-the-beast)
- [Psygnosis](/vault/companies/psygnosis)
- [Roger Dean](/vault/people/roger-dean) (Cover artist who influenced aesthetic)
```

---

## Amiga-Specific Technical Notes

### OCS/ECS vs AGA Chipsets

**OCS/ECS (1985-1992):**
- 32 colors on-screen from 4096 palette (5 bitplanes)
- 64 colors with Extra Half-Brite mode
- 4096 colors with HAM (Hold-And-Modify) mode
- 8 hardware sprites (16-pixel wide, 4-color each)
- 512KB chip RAM limit

**AGA (1992-1994):**
- 256 colors on-screen from 16.8 million palette (8 bitplanes)
- Enhanced HAM-8 mode
- Improved sprite capabilities
- 2MB chip RAM
- Higher resolution modes

**Curriculum Progression:**
- **Phases 1-4:** OCS/ECS focus
- **Phase 5:** Early AGA introduction (HAM-8)
- **Phases 6-8:** Full AGA utilization

### Paula Sound Chip
4-channel 8-bit PCM sample playback with hardware DMA.

**Progression:**
- **Phase 1:** Simple sound effects
- **Phase 2:** MOD music playback (4-channel tracker)
- **Phase 3-4:** Advanced mixing, music + effects
- **Phase 5-8:** Professional audio, CD-quality samples (CD³²)

### Blitter (Bit Block Transfer)
Hardware acceleration for graphics operations.

**Evolution:**
- **Phase 1:** Basic rectangle fills and copies
- **Phase 2:** Line drawing, complex masks
- **Phase 3-4:** Advanced blitting routines, optimization
- **Phase 5-8:** Maximum performance extraction

### Copper (Co-Processor)
Display list processor for synchronized graphics effects.

**Progression:**
- **Phase 1:** Basic screen setup
- **Phase 2:** Simple palette changes, sprite splits
- **Phase 3-4:** Raster bars, sky gradients, complex effects
- **Phase 5-8:** Mastery of copper programming

### Memory Management
- **512KB (OCS/ECS):** Careful optimization, overlays, compression
- **1MB+:** Larger games, better graphics/sound
- **2MB+ (AGA):** 256-color graphics, extensive content
- **CD³² (Phase 6-8):** CD-ROM streaming, FMV potential

---

## Assessment & Progression

**Within Each Tier (32 Lessons):**
- Lessons 1-10: Core mechanics and hardware setup
- Lessons 11-15: Game loop and basic playability
- Lessons 16-20: **Playable milestone** - fully functional game
- Lessons 21-32: Polish, effects, content variety, commercial quality

**Between Tiers:**
- Complete playable game from previous tier
- Demonstrate understanding of chipset features
- Create one variation showing technical mastery

**Between Phases:**
- Portfolio of 16 playable games (one from each tier)
- Technical showcase demonstrating phase-appropriate quality
- Self-assessment of readiness for next complexity level

---

## Historical Context & Authenticity

Each phase maps to actual Amiga development eras:

- **Phase 1 (1985-1986):** Launch era, learning custom chipset
- **Phase 2 (1987-1988):** Maturing techniques, commercial viability
- **Phase 3 (1988-1989):** Golden age, technical excellence, Bitmap Brothers era
- **Phase 4 (1989-1990):** Commercial maturity, genre mastery, Psygnosis quality
- **Phase 5 (1990-1991):** Pushing OCS/ECS limits, early AGA
- **Phase 6 (1991-1992):** Genre-defining classics, CD³² introduction
- **Phase 7 (1992-1993):** AGA perfection, platform showcase
- **Phase 8 (1993-1994):** Legacy titles, maximum capability, swan song

Games teach not just 68000 assembly, but the evolution of game development on this revolutionary multimedia platform.

---

*This curriculum represents 4,096 lessons of progressive Amiga game development education, from 68000 assembly foundations through custom chipset mastery to commercial-quality AGA masterpieces.*
