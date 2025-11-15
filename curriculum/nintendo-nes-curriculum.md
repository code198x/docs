# Nintendo NES Curriculum

## Overview

This curriculum covers game development for the Nintendo Entertainment System (NES/Famicom) across 8 phases of increasing complexity, from foundational 6502 assembly games through sophisticated commercial-quality titles that defined console gaming.

**Total Structure:**
- **8 Phases** (2^3) - Technical progression from 1983-style to 1994-style games
- **16 Tiers per Phase** (2^4) - 16 different game genres/types
- **32 Lessons per Tier** (2^5) - Complete game development cycle
- **Total: 4,096 lessons** (2^12)

**Learning Approach:**
- **Spiral Learning:** Teach minimum needed first, deepen understanding later
- **Quick Interaction:** Lessons 2-3 have interactive elements
- **Playable Early:** Lessons 15-20 produce a playable game
- **Polish Phase:** Lessons 21-32 add effects, variety, commercial quality

**NES Technical Context:**
- **CPU:** MOS 6502 @ 1.79 MHz (NTSC), 1.66 MHz (PAL)
- **Graphics:** PPU (Picture Processing Unit) - tile-based rendering
- **Resolution:** 256×240 pixels (NTSC), 256×224 visible
- **Colors:** 52 colors in palette, 25 on-screen (4 bg palettes + 4 sprite palettes)
- **Sprites:** 64 total (8×8 or 8×16), max 8 per scanline
- **Sound:** APU (Audio Processing Unit) - 5 channels (2 pulse, 1 triangle, 1 noise, 1 DMC)
- **Memory:** 2KB work RAM, 2KB video RAM, 256-byte sprite RAM
- **Storage:** ROM cartridges with optional battery backup
- **Mappers:** Banking systems for larger games (MMC1, MMC3, etc.)

---

## Phase 1: Foundation (1983-1985 Era)

**Target Quality:** Early NES games - learning 6502 and PPU basics, simple sprites, basic sound. Think *Mario Bros.* (arcade port), *Excitebike*, *Ice Climber*, early single-screen games.

**Technical Focus:**
- 6502 assembly fundamentals
- PPU basics (nametables, pattern tables)
- Sprite management (OAM)
- Controller input reading
- Background tile rendering
- Simple scrolling
- APU basics (pulse and noise channels)
- Collision detection (sprite vs background, sprite vs sprite)

**16 Game Genres (Phase 1):**

### Tier 1: Fixed Screen Platformer (Lessons 1-32)
**Game:** Single-screen platform game (Mario Bros.-style)
**Playable by:** Lesson 15-20
**Key Techniques:** Sprite display, gravity, jumping, platform collision, enemies
**NES Specific:** OAM sprite setup, background tiles, controller reading

### Tier 2: Fixed Screen Shooter (Lessons 33-64)
**Game:** Space Invaders-style descending formation shooter
**Playable by:** Lesson 48-52
**Key Techniques:** Formation movement, player shooting, collision, score display
**NES Specific:** Sprite animation, APU pulse channels for shots, pattern updates

### Tier 3: Maze Chase (Lessons 65-96)
**Game:** Pac-Man inspired maze game
**Playable by:** Lesson 80-84
**Key Techniques:** Tile-based maze, AI pathfinding, pellet collection, power-ups
**NES Specific:** Nametable layout, attribute table colors, sprite multiplexing

### Tier 4: Breakout (Lessons 97-128)
**Game:** Brick-breaking paddle game
**Playable by:** Lesson 112-116
**Key Techniques:** Ball physics, paddle control, brick destruction, scoring
**NES Specific:** Ball sprite, paddle sprite, dynamic tile updates for bricks

### Tier 5: Vertical Platformer (Lessons 129-160)
**Game:** Ice Climber-style vertical climbing game
**Playable by:** Lesson 144-148
**Key Techniques:** Vertical scrolling, platform breaking, enemy bouncing
**NES Specific:** Vertical scroll register, sprite priority, animated tiles

### Tier 6: Racing (Lessons 161-192)
**Game:** Top-down racing (Excitebike-style)
**Playable by:** Lesson 176-180
**Key Techniques:** Horizontal scrolling, track obstacles, turbo/heat mechanics
**NES Specific:** Horizontal scrolling, sprite flickering management, APU engine sounds

### Tier 7: Pong (Lessons 193-224)
**Game:** Classic two-paddle ball game
**Playable by:** Lesson 208-212
**Key Techniques:** Two-player input, ball physics, score tracking
**NES Specific:** Sprite positioning, controller reading for two players, simple APU

### Tier 8: Target Shooter (Lessons 225-256)
**Game:** Duck Hunt-style light gun shooter (without Zapper, using controller)
**Playable by:** Lesson 240-244
**Key Techniques:** Moving targets, timing, accuracy scoring, crosshair
**NES Specific:** Sprite animation cycles, hit detection, score display

### Tier 9: Block Puzzle (Lessons 257-288)
**Game:** Falling block puzzle (simplified Tetris concept)
**Playable by:** Lesson 272-276
**Key Techniques:** Piece rotation, line clearing, grid collision, drop speed
**NES Specific:** Tile-based playfield, pattern table manipulation

### Tier 10: Artillery (Lessons 289-320)
**Game:** Angle/power tank shooting (Scorched Earth-lite)
**Playable by:** Lesson 304-308
**Key Techniques:** Trajectory calculation, terrain collision, turn-based
**NES Specific:** Sprite rotation tables, background terrain, APU explosions

### Tier 11: Snake (Lessons 321-352)
**Game:** Growing snake collecting food
**Playable by:** Lesson 336-340
**Key Techniques:** Dynamic tail growth, self-collision, food spawning
**NES Specific:** Sprite chain management, tile-based movement

### Tier 12: Sports - Baseball (Lessons 353-384)
**Game:** Simple baseball game (batting/pitching)
**Playable by:** Lesson 368-372
**Key Techniques:** Ball physics, timing mechanics, score tracking
**NES Specific:** Multiple sprite control, field rendering, controller timing

### Tier 13: Balloon Fight Clone (Lessons 385-416)
**Game:** Floating combat with balloon physics
**Playable by:** Lesson 400-404
**Key Techniques:** Float physics, enemy popping, stage hazards, waves
**NES Specific:** Sprite flipping, water scrolling effects

### Tier 14: Pinball (Lessons 417-448)
**Game:** Digital pinball table
**Playable by:** Lesson 432-436
**Key Techniques:** Ball physics, flipper control, bumper collision, scoring
**NES Specific:** Complex collision detection, sprite trails, APU bumper sounds

### Tier 15: Lunar Lander (Lessons 449-480)
**Game:** Physics-based moon landing
**Playable by:** Lesson 464-468
**Key Techniques:** Thrust physics, fuel management, terrain collision
**NES Specific:** Smooth sprite movement, terrain rendering, thrust particles

### Tier 16: Wrecking Crew Clone (Lessons 481-512)
**Game:** Puzzle-action demolition game
**Playable by:** Lesson 496-500
**Key Techniques:** Tile destruction, enemy avoidance, ladder climbing, stage design
**NES Specific:** Dynamic nametable updates, sprite enemy patterns

---

## Phase 2: Enhancement (1985-1986 Era)

**Target Quality:** Maturing NES development - scrolling games, better graphics, refined controls. Think *Super Mario Bros.*, *Metroid*, *The Legend of Zelda*, *Castlevania*.

**Technical Focus:**
- Smooth scrolling (horizontal and vertical)
- Advanced sprite techniques
- Multiple screen layouts
- Simple memory mappers (NROM, UNROM)
- Music composition for APU
- Metatile systems
- Advanced collision detection
- Status bar with scroll splits

**Genre Mix:**
- **Enhanced from Phase 1:** Fixed Screen Platformer → Side-Scrolling Platformer, Maze Chase, Racing, Vertical Platformer
- **New for Phase 2:** Action-Adventure, Run 'n' Gun, Beat 'Em Up, Side-Scrolling Shooter
- **Dropped:** Fixed Screen Shooter, Breakout, Pong, Target Shooter, Block Puzzle, Artillery, Snake, Sports - Baseball, Balloon Fight Clone, Pinball, Lunar Lander, Wrecking Crew Clone

### Tier 1: Side-Scrolling Platformer (Lessons 1-32)
**Evolution:** Super Mario Bros. quality - smooth scrolling, power-ups, secrets, worlds

### Tier 2: Action-Adventure (Lessons 33-64)
**New Genre:** The Legend of Zelda-style top-down exploration with combat and items

### Tier 3: Maze Chase - Enhanced (Lessons 65-96)
Multi-screen maze with map system, varied enemies, power-up progression

### Tier 4: Metroidvania (Lessons 97-128)
**New Genre:** Metroid-style side-scrolling exploration with ability-gating

### Tier 5: Run 'n' Gun (Lessons 129-160)
**New Genre:** Contra-style action platformer with shooting focus

### Tier 6: Racing - Enhanced (Lessons 161-192)
Multiple tracks, obstacles, opponents, championship mode

### Tier 7: Beat 'Em Up (Lessons 193-224)
**New Genre:** Side-scrolling fighting with multiple enemies (Kung-Fu style)

### Tier 8: Vertical Platformer - Enhanced (Lessons 225-256)
Multi-screen vertical climbing with varied mechanics per stage

### Tier 9: Side-Scrolling Shooter (Lessons 257-288)
**New Genre:** Gradius-style horizontal shoot-'em-up with power-ups

### Tier 10: Platform-Puzzler (Lessons 289-320)
**New Genre:** Lolo-style push-puzzle with enemies and environmental hazards

### Tier 11: Sports - Soccer (Lessons 321-352)
**New Genre:** Top-down soccer with team control and tactics

### Tier 12: Vertical Shooter (Lessons 353-384)
**New Genre:** 1942-style top-down vertical shoot-'em-up

### Tier 13: Action-Platformer (Lessons 385-416)
**New Genre:** Castlevania-style deliberate platforming with combat and subweapons

### Tier 14: Collect-Em-Up (Lessons 417-448)
**New Genre:** Collect items within time limit across stages

### Tier 15: Puzzle Game (Lessons 449-480)
**New Genre:** Dr. Mario-style match-and-clear puzzle

### Tier 16: Overhead Action (Lessons 481-512)
**New Genre:** Commando-style overhead run 'n' gun with multi-directional movement

---

## Phase 3: Sophistication (1987-1988 Era)

**Target Quality:** "Golden Era" NES - advanced techniques, memorable gameplay, iconic franchises. Think *Mega Man 2*, *Ninja Gaiden*, *Contra*, *Castlevania III*.

**Technical Focus:**
- MMC1/MMC3 mapper utilization
- Advanced scrolling techniques
- Sprite multiplexing mastery
- Complex music (triangle bass, DPCM samples)
- Advanced animation techniques
- Split-screen effects
- Password/battery save systems
- Advanced metatile engines

**Genre Mix:**
- **All-Phase Core:** Side-Scrolling Platformer, Action-Adventure, Metroidvania, Run 'n' Gun, Beat 'Em Up, Action-Platformer
- **Continued:** Side-Scrolling Shooter, Vertical Shooter, Racing, Overhead Action
- **New for Phase 3:** Action RPG, Sports - Football, Strategy Game
- **Dropped:** Maze Chase, Vertical Platformer, Platform-Puzzler, Sports - Soccer, Collect-Em-Up, Puzzle Game

### Tier 1: Side-Scrolling Platformer - Advanced (Lessons 1-32)
Mega Man quality: weapon variety, boss patterns, stage selection, challenge

### Tier 2: Action-Adventure - Advanced (Lessons 33-64)
Zelda II quality: towns, overworld, side-scrolling combat, RPG elements

### Tier 3: Metroidvania - Advanced (Lessons 65-96)
Large interconnected world, multiple weapons, item progression, exploration

### Tier 4: Run 'n' Gun - Advanced (Lessons 97-128)
Contra quality: two-player co-op, varied weapons, memorable bosses

### Tier 5: Action-Platformer - Advanced (Lessons 129-160)
Ninja Gaiden quality: cutscenes, wall jumping, cinematic presentation

### Tier 6: Beat 'Em Up - Advanced (Lessons 161-192)
Double Dragon quality: grab moves, weapons, two-player co-op

### Tier 7: Side-Scrolling Shooter - Advanced (Lessons 193-224)
Gradius III quality: multiple weapon configurations, complex patterns

### Tier 8: Vertical Shooter - Advanced (Lessons 225-256)
1943 quality: loops, formations, ground/air targets, dramatic bosses

### Tier 9: Racing - Advanced (Lessons 257-288)
RC Pro-Am quality: isometric perspective, weapons, track variety

### Tier 10: Overhead Action - Advanced (Lessons 289-320)
Ikari Warriors quality: vehicles, varied weapons, destructible scenery

### Tier 11: Action RPG (Lessons 321-352)
**New Genre:** Crystalis-style real-time combat with stats and magic

### Tier 12: Sports - Football (Lessons 353-384)
**New Genre:** Tecmo Bowl quality: play calling, stats, team management

### Tier 13: Strategy Game (Lessons 385-416)
**New Genre:** Turn-based tactical combat with unit management

### Tier 14: Puzzle-Platformer Hybrid (Lessons 417-448)
**New Genre:** Environmental puzzles integrated with platforming (Gimmick!-style)

### Tier 15: Pinball Action (Lessons 449-480)
**New Genre:** Pinball with adventure elements (Pinball Quest-style)

### Tier 16: Shoot-'Em-Up Hybrid (Lessons 481-512)
**New Genre:** Unique shmup mechanics (Guardian Legend-style adventure-shooter)

---

## Phase 4: Commercial Quality (1988-1990 Era)

**Target Quality:** Commercial-grade polish with advanced techniques. Think *Super Mario Bros. 3*, *Kirby's Adventure*, *Mega Man 3-6*, *Batman*.

**Technical Focus:**
- MMC3 advanced features (IRQ scanline splits)
- Large ROM sizes (256KB+)
- Advanced sprite techniques (8×16 mode)
- Complex music arrangements
- Detailed animation
- Advanced physics engines
- Multiple game modes
- Polish and presentation

**Genre Mix:**
- **All-Phase Core:** Side-Scrolling Platformer, Action-Adventure, Metroidvania, Run 'n' Gun, Beat 'Em Up, Action-Platformer
- **Continued:** Side-Scrolling Shooter, Vertical Shooter, Action RPG, Strategy Game
- **New for Phase 4:** Hybrid Platformer, Fighting Game, JRPG
- **Dropped:** Racing, Overhead Action, Sports - Football, Puzzle-Platformer Hybrid, Pinball Action, Shoot-'Em-Up Hybrid

### Tier 1: Side-Scrolling Platformer - Commercial (Lessons 1-32)
Super Mario Bros. 3 quality: varied power-ups, world map, mini-games, secrets

### Tier 2: Action-Adventure - Commercial (Lessons 33-64)
Advanced Zelda quality: complex dungeons, item variety, overworld secrets

### Tier 3: Metroidvania - Commercial (Lessons 65-96)
Full non-linear exploration, extensive ability set, sequence breaking

### Tier 4: Run 'n' Gun - Commercial (Lessons 97-128)
Polished co-op action with varied stages and memorable set pieces

### Tier 5: Action-Platformer - Commercial (Lessons 129-160)
Batman quality: gadgets, varied stage mechanics, licensed quality

### Tier 6: Beat 'Em Up - Commercial (Lessons 161-192)
River City Ransom quality: RPG elements, open structure, unique mechanics

### Tier 7: Side-Scrolling Shooter - Commercial (Lessons 193-224)
Multiple weapon systems, balanced difficulty, memorable boss design

### Tier 8: Vertical Shooter - Commercial (Lessons 225-256)
Genre-defining bullet patterns, scoring depth, perfect balance

### Tier 9: Hybrid Platformer (Lessons 257-288)
**New Genre:** Kirby-style unique copy ability mechanics, accessible design

### Tier 10: Action RPG - Advanced (Lessons 289-320)
Full equipment system, magic, complex world, quest progression

### Tier 11: Strategy Game - Advanced (Lessons 321-352)
Fire Emblem quality: character development, permadeath, tactical depth

### Tier 12: Fighting Game (Lessons 353-384)
**New Genre:** One-on-one fighting with special moves and combos

### Tier 13: JRPG (Lessons 385-416)
**New Genre:** Dragon Warrior/Final Fantasy-style turn-based RPG with story

### Tier 14: Platformer-Shooter Hybrid (Lessons 417-448)
**New Genre:** Integrated platforming and shooting mechanics

### Tier 15: Experimental Platformer (Lessons 449-480)
**New Genre:** Unique movement mechanics (grappling, magnetism, etc.)

### Tier 16: Multi-Genre Game (Lessons 481-512)
**New Genre:** Multiple gameplay styles in one game (Blaster Master-style)

---

## Phase 5: Mastery (1990-1991 Era)

**Target Quality:** Pushing NES limits with every trick known. Think *Kirby's Adventure*, *Gimmick!*, *Crisis Force*, *Mr. Gimmick*.

**Technical Focus:**
- Maximum 6502 optimization
- Custom mappers (VRC6 with extra sound)
- Advanced sprite multiplexing
- Complex animation systems
- Wavetable synthesis (VRC6/VRC7)
- Advanced compression
- Parallax scrolling effects
- Dynamic difficulty

**Genre Mix:**
- **All-Phase Core:** Side-Scrolling Platformer, Action-Adventure, Metroidvania, Run 'n' Gun, Beat 'Em Up, Action-Platformer
- **Continued:** Side-Scrolling Shooter, Vertical Shooter, Action RPG, JRPG, Fighting Game
- **New for Phase 5:** Roguelike, Puzzle Action
- **Dropped:** Hybrid Platformer, Strategy Game, Platformer-Shooter Hybrid, Experimental Platformer, Multi-Genre Game

### Tier 1: Side-Scrolling Platformer - Master (Lessons 1-32)
Kirby's Adventure quality: gorgeous graphics, smooth gameplay, creative power system

### Tier 2: Action-Adventure - Master (Lessons 33-64)
Ultimate top-down adventure with all systems perfected

### Tier 3: Metroidvania - Master (Lessons 65-96)
Symphony of the Night-level design (scaled to NES), perfect exploration

### Tier 4: Run 'n' Gun - Master (Lessons 97-128)
Crisis Force quality: technical showcase, perfect gameplay

### Tier 5: Action-Platformer - Master (Lessons 129-160)
Gimmick! quality: physics-based gameplay, VRC6 audio, visual excellence

### Tier 6: Beat 'Em Up - Master (Lessons 161-192)
TMNT Tournament Fighters quality: deep combat, technical excellence

### Tier 7: Side-Scrolling Shooter - Master (Lessons 193-224)
Ultimate horizontal shmup with perfect patterns and presentation

### Tier 8: Vertical Shooter - Master (Lessons 225-256)
Genre perfection with innovation and polish

### Tier 9: Action RPG - Master (Lessons 257-288)
Full adventure with all systems mastered and balanced

### Tier 10: JRPG - Advanced (Lessons 289-320)
Final Fantasy III quality: job system, epic story, complex battles

### Tier 11: Fighting Game - Advanced (Lessons 321-352)
Tournament-quality balance, special move depth, variety

### Tier 12: Roguelike (Lessons 353-384)
**New Genre:** Procedural dungeons, permadeath, deep systems (Mystery Dungeon-style)

### Tier 13: Puzzle Action (Lessons 385-416)
**New Genre:** Real-time puzzle solving under pressure

### Tier 14: Tower Defense (Lessons 417-448)
**New Genre:** Strategic defender placement with wave management

### Tier 15: Narrative Action (Lessons 449-480)
**New Genre:** Story-driven action with cinematic sequences

### Tier 16: Hybrid Excellence (Lessons 481-512)
**New Genre:** Perfect blend of two genres (adventure-shooter, RPG-platformer)

---

## Phase 6: Innovation (1991-1992 Era)

**Target Quality:** Late-era innovation as 16-bit consoles rise. Think *Metal Storm*, *Shatterhand*, *Power Blade 2*, final NES masterpieces.

**Technical Focus:**
- Every optimization technique
- Advanced mapper features
- Maximum sprite utilization
- Professional audio production
- Complex state machines
- Procedural content
- Battery backup mastery

**Genre Mix:**
- **All-Phase Core:** Side-Scrolling Platformer, Action-Adventure, Metroidvania, Run 'n' Gun, Beat 'Em Up, Action-Platformer
- **Continued:** Side-Scrolling Shooter, Vertical Shooter, Action RPG, JRPG, Fighting Game, Roguelike
- **New for Phase 6:** None (perfecting existing)
- **Dropped:** Puzzle Action, Tower Defense, Narrative Action, Hybrid Excellence

### Tier 1: Side-Scrolling Platformer - Ultimate (Lessons 1-32)
Genre-defining platformer pushing every limit

### Tier 2: Action-Adventure - Ultimate (Lessons 33-64)
Ultimate top-down adventure experience

### Tier 3: Metroidvania - Ultimate (Lessons 65-96)
Perfect exploration-platformer with all systems mastered

### Tier 4: Run 'n' Gun - Ultimate (Lessons 97-128)
Ultimate action-shooter with perfect execution

### Tier 5: Action-Platformer - Ultimate (Lessons 129-160)
Metal Storm quality: gravity flipping, technical excellence, innovation

### Tier 6: Beat 'Em Up - Ultimate (Lessons 161-192)
Perfect fighting mechanics with depth and variety

### Tier 7: Side-Scrolling Shooter - Ultimate (Lessons 193-224)
Ultimate horizontal shmup masterpiece

### Tier 8: Vertical Shooter - Ultimate (Lessons 225-256)
Ultimate vertical shmup perfection

### Tier 9: Action RPG - Ultimate (Lessons 257-288)
Epic adventure with commercial quality throughout

### Tier 10: JRPG - Master (Lessons 289-320)
Ultimate turn-based RPG with deep systems and story

### Tier 11: Fighting Game - Master (Lessons 321-352)
Tournament-quality one-on-one combat perfection

### Tier 12: Roguelike - Advanced (Lessons 353-384)
Deep procedural systems with emergent gameplay

### Tier 13: Innovative Platformer (Lessons 385-416)
Unique mechanics not seen before in genre

### Tier 14: Innovative Shooter (Lessons 417-448)
Unique shmup mechanics defining new sub-genre

### Tier 15: Innovative Adventure (Lessons 449-480)
Unique adventure mechanics and presentation

### Tier 16: Genre-Defying (Lessons 481-512)
Game that transcends genre classification

---

## Phase 7: Perfection (1992-1993 Era)

**Target Quality:** Final commercial releases showing ultimate NES capability. Think late unlicensed gems and final official releases.

**Technical Focus:**
- Absolute optimization mastery
- Every hardware trick known
- Professional production values
- Complex mapper utilization
- Advanced compression techniques
- Perfect audio production

**Genre Mix:**
- **All-Phase Core:** Side-Scrolling Platformer, Action-Adventure, Metroidvania, Run 'n' Gun, Beat 'Em Up, Action-Platformer
- **Continued:** Side-Scrolling Shooter, Vertical Shooter, Action RPG, JRPG, Fighting Game, Roguelike
- **New for Phase 7:** None (absolute perfection of existing)
- **Dropped:** Innovative Platformer, Innovative Shooter, Innovative Adventure, Genre-Defying

### Tier 1: Side-Scrolling Platformer - Perfected (Lessons 1-32)
Absolute platforming perfection on NES hardware

### Tier 2: Action-Adventure - Perfected (Lessons 33-64)
Ultimate top-down adventure perfection

### Tier 3: Metroidvania - Perfected (Lessons 65-96)
Definitive exploration-platformer experience

### Tier 4: Run 'n' Gun - Perfected (Lessons 97-128)
Ultimate action-shooter perfection

### Tier 5: Action-Platformer - Perfected (Lessons 129-160)
Perfect action-platforming with all techniques mastered

### Tier 6: Beat 'Em Up - Perfected (Lessons 161-192)
Ultimate fighting excellence

### Tier 7: Side-Scrolling Shooter - Perfected (Lessons 193-224)
Definitive horizontal shmup on NES

### Tier 8: Vertical Shooter - Perfected (Lessons 225-256)
Definitive vertical shmup on NES

### Tier 9: Action RPG - Perfected (Lessons 257-288)
Ultimate action-RPG experience

### Tier 10: JRPG - Perfected (Lessons 289-320)
Ultimate turn-based RPG perfection

### Tier 11: Fighting Game - Perfected (Lessons 321-352)
Ultimate one-on-one combat on NES

### Tier 12: Roguelike - Master (Lessons 353-384)
Ultimate procedural dungeon crawler

### Tier 13: Artillery Strategy (Lessons 385-416)
Worms-style turn-based destructible terrain combat

### Tier 14: Puzzle-Platformer Hybrid (Lessons 417-448)
Environmental puzzles integrated with precision platforming

### Tier 15: God Game (Lessons 449-480)
Populous-style terrain manipulation and indirect control

### Tier 16: 4X Strategy Lite (Lessons 481-512)
Turn-based expand/explore/exploit/exterminate strategy

---

## Phase 8: Legacy (1993-1994 Era)

**Target Quality:** Absolute limits of NES, final swan songs. Think unlicensed late releases and homebre excellence.

**Technical Focus:**
- Every optimization known to humanity
- Custom solutions for every limitation
- Professional commercial quality
- Absolute mapper mastery
- Perfect audio engineering
- Complete production pipeline

**Genre Mix:**
- **All-Phase Core:** All 6 core genres perfected
- **Continued:** All 6 continued genres perfected
- **New Advanced:** Stealth-Action, Construction/Management, Pinball Simulation, Multi-Genre Epic

### Tier 1: Side-Scrolling Platformer - Legacy (Lessons 1-32)
Ultimate platformer defining what's possible on NES

### Tier 2: Action-Adventure - Legacy (Lessons 33-64)
Ultimate adventure defining NES capability

### Tier 3: Metroidvania - Legacy (Lessons 65-96)
Ultimate exploration-platformer legacy

### Tier 4: Run 'n' Gun - Legacy (Lessons 97-128)
Ultimate action-shooter legacy

### Tier 5: Action-Platformer - Legacy (Lessons 129-160)
Ultimate action-platforming legacy

### Tier 6: Beat 'Em Up - Legacy (Lessons 161-192)
Ultimate fighting game legacy

### Tier 7: Side-Scrolling Shooter - Legacy (Lessons 193-224)
Ultimate horizontal shmup legacy

### Tier 8: Vertical Shooter - Legacy (Lessons 225-256)
Ultimate vertical shmup legacy

### Tier 9: Action RPG - Legacy (Lessons 257-288)
Ultimate action-RPG legacy

### Tier 10: JRPG - Legacy (Lessons 289-320)
Ultimate turn-based RPG legacy

### Tier 11: Fighting Game - Legacy (Lessons 321-352)
Ultimate fighting legacy

### Tier 12: Roguelike - Legacy (Lessons 353-384)
Ultimate procedural crawler legacy

### Tier 13: Stealth-Action (Lessons 385-416)
Metal Gear-style line-of-sight infiltration and detection mechanics

### Tier 14: Construction/Management (Lessons 417-448)
SimCity-inspired building and resource management simulation

### Tier 15: Pinball Simulation (Lessons 449-480)
Realistic pinball physics with multiple tables and modes

### Tier 16: Multi-Genre Epic (Lessons 481-512)
Blaster Master-style game with distinct gameplay modes per area

---

## Genre Lifecycle Roadmap

### All-Phase Genres (Phases 1-8)
These genres appear in all 8 phases with increasing sophistication:

1. **Side-Scrolling Platformer** - Single-screen → Mario → Mega Man → SMB3 → Kirby → Perfection
2. **Action-Adventure** (from Phase 2) - Zelda → Zelda II → Advanced → Master → Legacy
3. **Metroidvania** (from Phase 2) - Metroid → Advanced → Master → Perfection
4. **Run 'n' Gun** (from Phase 2) - Simple → Contra → Advanced → Crisis Force → Legacy
5. **Beat 'Em Up** (from Phase 2) - Kung-Fu → Double Dragon → River City → TMNT → Legacy
6. **Action-Platformer** (from Phase 2) - Castlevania → Ninja Gaiden → Batman → Gimmick! → Legacy

### Continuing Genres (Appear 6+ Phases)

7. **Side-Scrolling Shooter** (Phases 2-8) - Gradius progression to perfection
8. **Vertical Shooter** (Phases 2-8) - 1942 → 1943 → Perfection
9. **Action RPG** (Phases 3-8) - Crystalis → Advanced → Master
10. **JRPG** (Phases 4-8) - Dragon Warrior → Final Fantasy → Perfection
11. **Fighting Game** (Phases 4-8) - Basic → Tournament quality
12. **Roguelike** (Phases 5-8) - Mystery Dungeon → Mastery

### Phase-Limited Genres

#### Phase 1 Only
- **Fixed Screen Shooter:** Space Invaders teaching
- **Breakout:** Ball physics basics
- **Pong:** Simple collision
- **Target Shooter:** Timing and accuracy
- **Block Puzzle:** Grid logic
- **Artillery:** Trajectory physics
- **Snake:** Dynamic growth
- **Sports - Baseball:** Basic sports mechanics
- **Balloon Fight Clone:** Float physics
- **Pinball:** Complex collision
- **Lunar Lander:** Thrust physics
- **Wrecking Crew Clone:** Puzzle-action

#### Phase 2 Only
- **Platform-Puzzler:** Lolo-style pushing
- **Sports - Soccer:** Team control
- **Collect-Em-Up:** Time-based collection
- **Puzzle Game:** Dr. Mario-style
- **Overhead Action:** Commando-style (continues to Phase 3)

#### Phase 3 Only
- **Sports - Football:** Tecmo Bowl quality
- **Strategy Game:** Turn-based tactics (continues to Phase 4)
- **Puzzle-Platformer Hybrid:** Environmental puzzles
- **Pinball Action:** Pinball Quest-style
- **Shoot-'Em-Up Hybrid:** Guardian Legend-style

#### Phase 4-5 Only
- **Hybrid Platformer:** Kirby copy abilities
- **Platformer-Shooter Hybrid:** Integrated mechanics
- **Experimental Platformer:** Unique movement
- **Tower Defense:** Strategic defender placement
- **Narrative Action:** Story-driven action
- **Hybrid Excellence:** Genre blending

#### Phase 7 Only
- **Artillery Strategy:** Worms-style combat
- **Puzzle-Platformer Hybrid:** Environmental puzzles with platforming
- **God Game:** Populous-style indirect control
- **4X Strategy Lite:** Turn-based empire building

### Emerging Genres by Phase

#### Phase 2 Introductions
- **Action-Adventure:** Zelda-style - **CONTINUES TO PHASE 8**
- **Metroidvania:** Metroid-style - **CONTINUES TO PHASE 8**
- **Run 'n' Gun:** Contra-style - **CONTINUES TO PHASE 8**
- **Beat 'Em Up:** Kung-Fu/Double Dragon - **CONTINUES TO PHASE 8**
- **Action-Platformer:** Castlevania-style - **CONTINUES TO PHASE 8**
- **Side-Scrolling Shooter:** Gradius-style - **CONTINUES TO PHASE 8**
- **Vertical Shooter:** 1942-style - **CONTINUES TO PHASE 8**

#### Phase 3 Introductions
- **Action RPG:** Crystalis-style - **CONTINUES TO PHASE 8**

#### Phase 4 Introductions
- **Fighting Game:** One-on-one combat - **CONTINUES TO PHASE 8**
- **JRPG:** Turn-based RPG - **CONTINUES TO PHASE 8**

#### Phase 5 Introductions
- **Roguelike:** Procedural dungeons - **CONTINUES TO PHASE 8**

#### Phase 7 Introductions
- **Artillery Strategy:** Worms-style turn-based combat
- **Puzzle-Platformer Hybrid:** Environmental puzzles with platforming
- **God Game:** Populous-style indirect control
- **4X Strategy Lite:** Turn-based empire strategy

#### Phase 8 Introductions
- **Stealth-Action:** Metal Gear-style infiltration
- **Construction/Management:** SimCity-inspired building
- **Pinball Simulation:** Realistic pinball physics
- **Multi-Genre Epic:** Blaster Master-style mode switching

### Genre Count by Phase
- **Phase 1:** 16 genres (foundation, learning hardware)
- **Phase 2:** 16 genres (1 evolved, 7 new core, 8 other new, 12 dropped)
- **Phase 3:** 16 genres (6 core, 4 continued, 3 new, 6 dropped)
- **Phase 4:** 16 genres (6 core, 4 continued, 3 new, 6 dropped)
- **Phase 5:** 16 genres (6 core, 5 continued, 2 new, 5 dropped)
- **Phase 6:** 16 genres (6 core, 6 continued, 0 new, 4 dropped)
- **Phase 7:** 16 genres (6 core, 6 continued, 4 new)
- **Phase 8:** 16 genres (6 core, 6 continued, 4 new advanced)

---

## Integration with Vault and Pattern Library

### The Vault: Contextual Links

Lessons should link to Vault entries when mentioning:

**People:** Programmers, musicians, artists, designers
- *Example:* "...similar to Koji Kondo's approach in Super Mario Bros..."
- *Link to:* `/vault/people/koji-kondo`

**Companies:** Studios, publishers, hardware manufacturers
- *Example:* "...developed by Konami..."
- *Link to:* `/vault/companies/konami`

**Games:** Specific titles used as examples
- *Example:* "...the sprite multiplexing technique from Mega Man..."
- *Link to:* `/vault/games/mega-man`

**Techniques:** Programming methods and approaches
- *Example:* "...using MMC3 scanline IRQs for status bar splits..."
- *Link to:* `/vault/techniques/nes-mmc3-irq`

**Hardware:** Chips and components being programmed
- *Example:* "...the PPU's nametable system..."
- *Link to:* `/vault/hardware/nes-ppu`

**Cultural Context:** Movies, music, events for era context
- *Example:* "...released during the height of NES popularity in 1989..."
- *Link to:* `/vault/events/nes-golden-age`

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

For a complete, production-ready sprite management system with pooling,
see [Pattern: Sprite Management System](/patterns/nes/rendering/sprite-management).
```

**Pattern Evolution:**
As patterns evolve across phases, reference the appropriate version:
- Phase 1: [Pattern: Sprite Display (Basic)](/patterns/nes/rendering/sprite-basic)
- Phase 2: [Pattern: Sprite Multiplexing](/patterns/nes/rendering/sprite-multiplexing)
- Phase 4: [Pattern: 8×16 Sprite Mode](/patterns/nes/rendering/sprite-8x16)

**Pattern Categories for NES:**
- **Rendering:** Sprite management, PPU scrolling, nametable updates, CHR-RAM
- **Input:** Controller reading, two-player support, input buffering
- **Audio:** APU music playback, sound effects, DPCM samples
- **Physics:** Tile collision, platformer physics, projectiles
- **AI:** Enemy behavior, pathfinding
- **Framework:** NMI handlers, game loops, state machines
- **Data:** Memory mappers (MMC1, MMC3, etc.), compression, CHR-ROM banking

### Integration Example

**Lesson excerpt:**
```markdown
In this lesson, we're implementing sprite management for our platformer. The
NES PPU supports 64 sprites (8×8 or 8×16), but only 8 can be displayed per
scanline. We need to manage sprite priority and handle the 8-per-scanline
limit to minimize flickering.

[...lesson content teaching the concept step by step...]

Super Mario Bros. 3 uses sophisticated sprite management to handle Mario,
enemies, power-ups, and effects simultaneously. The game prioritizes sprites
intelligently, ensuring important elements (like Mario) never flicker.

## Further Reading

**Pattern Library:**
- [Sprite Management System](/patterns/nes/rendering/sprite-management)
- [OAM DMA Transfer](/patterns/nes/rendering/oam-dma)

**Vault:**
- [PPU (Picture Processing Unit)](/vault/hardware/nes-ppu)
- [Super Mario Bros. 3](/vault/games/super-mario-bros-3)
- [Shigeru Miyamoto](/vault/people/shigeru-miyamoto)
- [Sprite Flickering Technique](/vault/techniques/nes-sprite-flickering)
```

---

## NES-Specific Technical Notes

### PPU (Picture Processing Unit)
Tile-based graphics system with specific limitations.

**Pattern Tables:**
- Two 4KB pattern tables (background and sprite tiles)
- 8×8 pixel tiles, 2-bit color depth per tile
- CHR-ROM (read-only) or CHR-RAM (writeable)

**Nametables:**
- Four 1KB nametables (background tile maps)
- 32×30 tiles visible area
- Attribute tables define 2×2 tile color groups

**Sprites:**
- 64 sprites total (8×8 or 8×16 mode)
- 8 sprites per scanline limit (causes flickering)
- Sprite 0 hit detection for timing

**Progression:**
- **Phase 1:** Basic sprite display, simple backgrounds
- **Phase 2:** Smooth scrolling, sprite multiplexing
- **Phase 3-4:** Advanced animation, sprite 0 splits for status bars
- **Phase 5-8:** Maximum optimization, every trick known

### APU (Audio Processing Unit)
5-channel sound synthesis.

**Channels:**
- Pulse 1 & 2: Square waves with duty cycle
- Triangle: Pure triangle wave (bass)
- Noise: White noise generator (percussion)
- DMC: Delta modulation for samples

**Progression:**
- **Phase 1:** Simple sound effects
- **Phase 2:** Music composition, multi-channel
- **Phase 3-4:** Complex arrangements, DPCM samples
- **Phase 5-8:** VRC6/VRC7 expansion audio, professional quality

### Memory Mappers
Banking systems for larger games.

**Common Mappers:**
- **NROM:** No mapper (32KB PRG, 8KB CHR)
- **MMC1:** 256KB PRG, 128KB CHR, switchable
- **MMC3:** 512KB PRG, 256KB CHR, IRQ counter for effects
- **VRC6:** Extra sound channels (3 additional)

**Progression:**
- **Phase 1:** NROM (simple games)
- **Phase 2:** MMC1 (basic banking)
- **Phase 3-4:** MMC3 (advanced features)
- **Phase 5-8:** VRC6, custom mappers

### Controller Input
Reading NES controller via $4016/$4017.

**Buttons:** A, B, Select, Start, Up, Down, Left, Right

**Progression:**
- **Phase 1:** Basic button reading
- **Phase 2:** Two-player support
- **Phase 3-8:** Advanced input buffering, frame-perfect detection

---

## Assessment & Progression

**Within Each Tier (32 Lessons):**
- Lessons 1-10: Core mechanics and hardware setup
- Lessons 11-15: Game loop and basic playability
- Lessons 16-20: **Playable milestone** - fully functional game
- Lessons 21-32: Polish, effects, content variety, commercial quality

**Between Tiers:**
- Complete playable game from previous tier
- Demonstrate understanding of PPU/APU features
- Create one variation showing technical mastery

**Between Phases:**
- Portfolio of 16 playable games (one from each tier)
- Technical showcase demonstrating phase-appropriate quality
- Self-assessment of readiness for next complexity level

---

## Historical Context & Authenticity

Each phase maps to actual NES development eras:

- **Phase 1 (1983-1985):** Launch era, arcade ports, simple games
- **Phase 2 (1985-1986):** First-party masterpieces defining genres
- **Phase 3 (1987-1988):** Golden age, third-party excellence
- **Phase 4 (1988-1990):** Commercial maturity, franchise peaks
- **Phase 5 (1990-1991):** Pushing limits as 16-bit arrives
- **Phase 6 (1991-1992):** Late innovation, final commercial masterpieces
- **Phase 7 (1992-1993):** Absolute perfection, unlicensed gems
- **Phase 8 (1993-1994):** Legacy swan songs, homebrew excellence

Games teach not just 6502 assembly, but the evolution of console game development on the platform that saved the industry.

---

*This curriculum represents 4,096 lessons of progressive NES game development education, from 6502 assembly foundations through PPU/APU mastery to commercial-quality cartridge games.*
