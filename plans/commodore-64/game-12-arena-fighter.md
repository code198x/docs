# Arena Fighter: 128-Unit Outline

**Game:** 12 of 16
**Platform:** Commodore 64
**Units:** 128
**Concept:** One-on-one fighting game. Two fighters, health bars, special moves, combos. An IK+/Street Fighter-inspired fighting game with deep mechanics.

---

## Why 128 Units?

Arena Fighter introduces the most complex state machines and timing systems in the curriculum:
1. **Animation state machines** - Many states with complex transitions
2. **Hitbox/hurtbox system** - Per-frame collision data
3. **Frame data** - Startup, active, recovery frames for every move
4. **Special move inputs** - Motion detection (QCF, DP, charge)
5. **Input buffering** - Smooth combo execution
6. **AI opponent** - Reactive, difficulty-scaled computer player
7. **4 complete characters** - Each needs unique animations, moves, specials
8. **Multiple game modes** - Versus, Arcade, Training, Tournament

At 64 units, characters 3 and 4 get only 1 unit each - impossible for proper implementation. 128 units allows each character to be fully developed with proper AI and multiple modes.

---

## Skills Applied from Previous Games

| Skill | Learned In | Application in Arena Fighter |
|-------|-----------|---------------------------|
| SID fundamentals | SID Symphony | Impact sounds, fighting music |
| Hardware sprites | Starfield | Fighter sprites, effects |
| Joystick input | Starfield | Player control |
| Animation frames | Platform Panic | Fighter animations |
| Collision detection | Various | Hitbox/hurtbox overlap |
| Health systems | Dungeon Crawl | Health bars |
| Object state machines | Dungeon Crawl | Fighter states |
| Two-player input | Various | Versus play |
| Sprite multiplexing | Sprite Storm | Large fighter sprites |
| Character graphics | Maze Raider | Arena backgrounds |
| Combat systems | Dungeon Crawl | Attack, damage, defeat |

## New Skills Introduced

| Skill | Phase | Description |
|-------|-------|-------------|
| Animation state machine | 2 | Complex state transitions with rules |
| Hitbox/hurtbox system | 3 | Per-frame attack and vulnerable areas |
| Frame data | 3 | Startup, active, recovery timing |
| Move priority | 4 | Attack beats throw, etc. |
| Input buffering | 4 | Store inputs during animation |
| Motion inputs | 5 | QCF, DP, charge detection |
| Super meter | 5 | Build and spend resource |
| AI opponent | 6 | Reactive computer fighter |
| Character archetypes | 7 | Different fighting styles |
| Combo systems | 4 | Chain attacks together |

---

## Phase 1: Arena Foundation (Units 1-16)
*Project setup and fighting arena.*

### Units 1-4: Project Setup
- **Unit 1:** Fighting game concept - analysing IK+, SF2, Mortal Kombat
- **Unit 2:** Move set design - punches, kicks, specials, supers
- **Unit 3:** Memory layout - animation data, state, hitbox storage
- **Unit 4:** Main loop architecture - input, update, render

### Units 5-8: Arena Design
- **Unit 5:** Arena character set - floor, walls, decorations
- **Unit 6:** Arena rendering - background display
- **Unit 7:** Arena boundaries - fighting area limits
- **Unit 8:** Multiple arena designs - 2-3 visual styles

### Units 9-12: HUD Framework
- **Unit 9:** Health bar design - layout, colours
- **Unit 10:** Health bar rendering - both players
- **Unit 11:** Round indicators - win markers
- **Unit 12:** Timer display - countdown formatting

### Units 13-16: Match Structure
- **Unit 13:** Round system - best of 3 rounds
- **Unit 14:** Round timer - time limit, timeout handling
- **Unit 15:** Win conditions - KO, timeout, double KO
- **Unit 16:** Match flow - round start, end, match complete

**Phase Goal:** Complete arena with HUD and match structure (no fighters yet).

---

## Phase 2: Fighter Foundation (Units 17-32)
*Fighter sprites and state machine.*

### Units 17-20: Fighter Sprites
- **Unit 17:** Fighter sprite design - base pose, proportions
- **Unit 18:** Standing idle animation - 2-frame breathing
- **Unit 19:** Fighter data structure - position, state, health, direction
- **Unit 20:** Two fighter instances - player 1 and player 2 data

### Units 21-24: Basic Movement
- **Unit 21:** Walking forward - toward opponent
- **Unit 22:** Walking backward - away from opponent
- **Unit 23:** Walk animation frames - 4-frame walk cycle
- **Unit 24:** Arena boundary enforcement - clamp to edges

### Units 25-28: State Machine
- **Unit 25:** State enumeration - idle, walk, crouch, attack, hit, etc.
- **Unit 26:** State transitions - rules for changing states
- **Unit 27:** Animation per state - lookup tables
- **Unit 28:** State machine update - frame-by-frame progression

### Units 29-32: Facing and Crouch
- **Unit 29:** Auto-facing - always face opponent
- **Unit 30:** Sprite flipping - mirror based on direction
- **Unit 31:** Crouch state - down input, shorter hurtbox
- **Unit 32:** Crouch transitions - smooth enter/exit

**Phase Goal:** Fighter moves around arena with proper state machine.

---

## Phase 3: Basic Combat (Units 33-48)
*Attacks, hitboxes, and damage.*

### Units 33-36: Hitbox System
- **Unit 33:** Hitbox concept - attack area definition
- **Unit 34:** Hurtbox concept - vulnerable area definition
- **Unit 35:** Per-frame hitbox data - position and size per animation frame
- **Unit 36:** Hitbox/hurtbox overlap detection

### Units 37-40: Basic Attacks
- **Unit 37:** Standing punch - animation, hitbox
- **Unit 38:** Standing kick - animation, hitbox, longer range
- **Unit 39:** Crouch punch - low position
- **Unit 40:** Crouch kick - low, hits standing blockers

### Units 41-44: Damage System
- **Unit 41:** Damage values - per attack
- **Unit 42:** Health reduction - on successful hit
- **Unit 43:** Hit stun state - brief vulnerability after hit
- **Unit 44:** Visual feedback - flash, push back

### Units 45-48: Frame Data
- **Unit 45:** Startup frames - animation before hitbox active
- **Unit 46:** Active frames - hitbox can hit during these
- **Unit 47:** Recovery frames - animation after attack
- **Unit 48:** Frame data tables - complete timing for all moves

**Phase Goal:** Working combat with proper timing and hit detection.

---

## Phase 4: Advanced Combat (Units 49-64)
*Jumping, blocking, combos, throws.*

### Units 49-52: Jump System
- **Unit 53:** Jump input - up direction
- **Unit 50:** Jump arc - physics and trajectory
- **Unit 51:** Air state - different rules while jumping
- **Unit 52:** Landing transition - back to ground state

### Units 53-56: Air Attacks
- **Unit 53:** Jump punch - air-to-air, air-to-ground
- **Unit 54:** Jump kick - cross-up potential
- **Unit 55:** Air hitbox positioning - relative to jump position
- **Unit 56:** Landing cancel - attack continues on ground

### Units 57-60: Blocking
- **Unit 57:** Block input - hold back direction
- **Unit 58:** Standing block - blocks high/mid attacks
- **Unit 59:** Crouching block - blocks low attacks
- **Unit 60:** Block stun and chip damage

### Units 61-64: Throws and Combos
- **Unit 61:** Throw mechanic - close range, beats block
- **Unit 62:** Throw tech - counter-throw timing
- **Unit 63:** Input buffering - queue inputs during animation
- **Unit 64:** Basic combos - chain attacks together, combo counter

**Phase Goal:** Complete combat with blocking, throws, and combos.

---

## Phase 5: Special Moves (Units 65-80)
*Motion inputs, specials, super meter.*

### Units 65-68: Input Detection
- **Unit 65:** Input history buffer - store recent inputs
- **Unit 66:** Motion detection - recognise patterns in buffer
- **Unit 67:** Quarter-circle forward (QCF) detection
- **Unit 68:** Dragon punch (DP) motion detection

### Units 69-72: Special Moves
- **Unit 69:** Fireball special - QCF + punch, projectile
- **Unit 70:** Projectile behaviour - travel, collision, destruction
- **Unit 71:** Uppercut special - DP + punch, rising anti-air
- **Unit 72:** Invincibility frames - on special startup

### Units 73-76: Super Meter
- **Unit 73:** Meter data structure - current level, max level
- **Unit 74:** Meter building - gain on hit, block, special
- **Unit 75:** Meter display - bar below health
- **Unit 76:** Meter spending - requirement for super move

### Units 77-80: Super Move
- **Unit 77:** Super move input - QCF QCF + punch
- **Unit 78:** Super move animation - extended, dramatic
- **Unit 79:** Super move damage - high, meter cost
- **Unit 80:** Super flash - freeze frame, dramatic pause

**Phase Goal:** Special moves with motion inputs and super meter system.

---

## Phase 6: AI and Modes (Units 81-96)
*Computer opponent and game modes.*

### Units 81-84: AI Framework
- **Unit 81:** AI decision structure - evaluate, decide, act
- **Unit 82:** Distance evaluation - close, mid, far ranges
- **Unit 83:** Threat assessment - opponent's current state
- **Unit 84:** AI input generation - simulated joystick

### Units 85-88: AI Behaviours
- **Unit 85:** Defensive AI - block, retreat, counter
- **Unit 86:** Aggressive AI - advance, attack, pressure
- **Unit 87:** Mixed AI - adapt to situation
- **Unit 88:** Difficulty scaling - reaction time, mistakes

### Units 89-92: Game Modes
- **Unit 89:** Title screen - logo, menu options
- **Unit 90:** Mode selection - versus, arcade, training
- **Unit 91:** Versus mode - 2P human vs human
- **Unit 92:** Single player mode - vs CPU

### Units 93-96: Training Mode
- **Unit 93:** Training environment - infinite health, reset
- **Unit 94:** Dummy settings - stand, crouch, jump, CPU
- **Unit 95:** Input display - show player inputs
- **Unit 96:** Frame data display - show move properties

**Phase Goal:** AI opponent and multiple game modes.

---

## Phase 7: Characters (Units 97-112)
*Four complete playable fighters.*

### Units 97-100: Character 1 - Balanced
- **Unit 97:** Character 1 design - balanced all-rounder
- **Unit 98:** Character 1 animations - full set
- **Unit 99:** Character 1 specials - fireball, uppercut
- **Unit 100:** Character 1 super - signature move

### Units 101-104: Character 2 - Rushdown
- **Unit 101:** Character 2 design - fast, aggressive
- **Unit 102:** Character 2 animations - quick moves
- **Unit 103:** Character 2 specials - dash punch, rapid kicks
- **Unit 104:** Character 2 super - combo finisher

### Units 105-108: Character 3 - Grappler
- **Unit 105:** Character 3 design - slow, powerful, throws
- **Unit 106:** Character 3 animations - heavy, impactful
- **Unit 107:** Character 3 specials - command throws, armour
- **Unit 108:** Character 3 super - devastating grab

### Units 109-112: Character 4 - Zoner
- **Unit 109:** Character 4 design - keep-away, projectiles
- **Unit 110:** Character 4 animations - ranged focus
- **Unit 111:** Character 4 specials - multiple projectiles, traps
- **Unit 112:** Character 4 super - full screen attack

**Phase Goal:** Four distinct characters with unique playstyles.

---

## Phase 8: Polish and Release (Units 113-128)
*Effects, balance, modes, release.*

### Units 113-116: Visual Effects
- **Unit 113:** Hit sparks - impact visuals
- **Unit 114:** Block sparks - different from hit
- **Unit 115:** Special move effects - fireballs, trails
- **Unit 116:** Screen shake - on heavy hits

### Units 117-120: Audio Design
- **Unit 117:** Impact sounds - punch, kick variations
- **Unit 118:** Special move sounds - fireball, uppercut
- **Unit 119:** Voice effects - attack shouts, hit grunts
- **Unit 120:** Fighting music - energetic themes

### Units 121-124: Advanced Features
- **Unit 121:** Character select screen - portraits, selection
- **Unit 122:** Versus screen - pre-fight display
- **Unit 123:** Victory screen - winner pose, stats
- **Unit 124:** Arcade mode - ladder progression, ending

### Units 125-128: Balance and Release
- **Unit 125:** Balance testing - damage, timing adjustments
- **Unit 126:** Bug fixing and edge cases
- **Unit 127:** Tournament mode - bracket competition
- **Unit 128:** Release build - final testing, distribution

**Phase Goal:** Complete, polished fighting game ready for distribution.

---

## Summary

**Arena Fighter** at 128 units provides proper depth for a complete fighting game:

**Phase 1 (Arena):** Fighting arena, HUD, match structure.

**Phase 2 (Fighter):** Sprite, movement, state machine foundation.

**Phase 3 (Combat):** Hitbox system, attacks, damage, frame data.

**Phase 4 (Advanced):** Jumping, blocking, throws, combos.

**Phase 5 (Specials):** Motion inputs, special moves, super meter.

**Phase 6 (AI):** Computer opponent, game modes, training.

**Phase 7 (Characters):** Four complete, distinct fighters.

**Phase 8 (Polish):** Effects, audio, balance, release.

### Skills Transferred Forward

The following skills debut in Arena Fighter:

1. **Complex animation state machines** → Mega Blaster (player states), Symphony's End
2. **Hitbox/hurtbox collision** → Any game with precise combat
3. **Frame data concepts** → Action games with timing-critical mechanics
4. **Input buffering** → Complex input handling in future games
5. **Motion input detection** → Special move systems
6. **AI opponent behaviour** → All subsequent AI games
7. **Character archetypes** → Different playstyles in future games

### Comparison: 64 vs 128 Units

| System | 64-Unit Depth | 128-Unit Depth |
|--------|---------------|----------------|
| Arena/HUD | 2 units | 8 units |
| Fighter sprites | 4 units | 8 units |
| State machine | 4 units | 8 units |
| Basic attacks | 4 units | 8 units |
| Hitbox system | 4 units | 8 units |
| Advanced combat | 8 units | 16 units |
| Special moves | 6 units | 16 units |
| AI opponent | 4 units | 8 units |
| Characters | 4 units (rushed) | 16 units (proper) |
| Polish/release | 8 units | 16 units |

### Game Specifications

- **Fighters:** 4 playable characters with distinct archetypes
  - Balanced (all-rounder)
  - Rushdown (fast, aggressive)
  - Grappler (slow, powerful, throws)
  - Zoner (projectiles, keep-away)
- **Normal attacks:** Punch, kick (standing, crouching, jumping)
- **Special moves:** 2-3 per character with motion inputs
- **Super moves:** 1 per character, requires full meter
- **Defence:** Block (standing/crouching), throw tech
- **Match:** Best of 3 rounds, 60-second timer
- **Modes:** Versus, Arcade, Training, Tournament
- **AI:** 3 difficulty levels (Easy, Medium, Hard)
- **Features:** Combo counter, super meter, input display, frame data
