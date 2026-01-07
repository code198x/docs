# Starfield: 64-Unit Outline

**Game:** C64 Game 2: Starfield
**Units:** 64
**Prerequisite:** SID Symphony (Game 1)
**Concept:** Vertical space shooter. Player ship versus waves of enemies. Shoot, dodge, survive. Multiple enemy types, bosses, power-ups.

**Commercial Quality Target:** A game comparable to mid-era shooters like Galaga, Gyruss, or early Uridium. Fast action, multiple enemy types, boss battles, weapon upgrades. Something that would have competed on shop shelves in 1986-87.

---

## Skill Progression from SID Symphony

### Skills Applied (not re-taught)

These skills were mastered in SID Symphony. Starfield assumes them and builds upon them:

| Skill | SID Symphony Unit | Starfield Application |
|-------|-------------------|----------------------|
| BASIC stub, assembly setup | 1-2 | Assumed from Unit 1 |
| Screen memory ($0400) | 5 | HUD display, background |
| Colour RAM ($D800) | 5 | HUD colours, effects |
| Custom character sets | 6 | Starfield background, explosions |
| Game loop structure | 7 | Applied immediately |
| Raster synchronisation | 7, 52 | Stable sprite display |
| Frame-based timing | 7-10 | Enemy/bullet movement |
| Data structures | 8 | Enemy arrays, bullet pools |
| Score display (16-bit) | 13 | Applied directly |
| Health/lives system | 15 | Lives with continues |
| State machines | 16-17 | Game states |
| Menu systems | 17, 26 | Applied with new content |
| Difficulty levels | 19-20 | Applied to waves |
| SID sound effects | 41-43 | Shoot, explosion, power-up |
| SID filters | 42 | Dramatic moments |
| Title screen | 33-34 | New visuals, same techniques |
| Attract mode | 35 | Demo gameplay |
| High score table | 45 | Applied directly |
| Options screen | 46 | Control options |
| Pause functionality | 47 | Applied directly |
| Code optimisation | 49-51 | Critical for many sprites |
| Memory optimisation | 50 | Sprite/level data |
| Distribution packaging | 64 | Same process |

### New Skills Introduced

These are the primary learning objectives for Starfield:

| New Skill | Description |
|-----------|-------------|
| Hardware sprites | VIC-II sprite system, 8 hardware sprites |
| Sprite registers | Position, colour, enable, expand |
| X-position MSB | Handling X > 255 |
| Sprite pointers | Connecting sprites to graphic data |
| Sprite design | 24x21 pixel, single/multicolour |
| Joystick input | CIA $DC00 reading |
| Sprite-sprite collision | Hardware detection via $D01E |
| Sprite-background collision | Hardware detection via $D01F |
| Object pools | Managing bullets and enemies |
| Enemy AI | Movement patterns, behaviours |
| Sprite animation | Frame cycling, animation tables |
| Sprite multiplexing | Displaying 16+ sprites |
| Sorted sprite lists | Y-sorting for multiplexer |
| Raster interrupt sprites | Reusing sprites mid-screen |
| Parallax scrolling | Multi-speed background layers |
| Boss patterns | Complex multi-phase enemies |

---

## The Finished Game

### Core Gameplay
- Player ship with 8-directional movement
- Primary weapon (upgradeable: single → double → spread)
- Secondary weapon (limited bombs)
- Shield power-up (temporary invincibility)
- Speed power-up (faster movement)

### Enemies
- **Drone:** Simple, moves straight down
- **Weaver:** Sine-wave movement
- **Diver:** Swoops at player
- **Shooter:** Fires back at player
- **Formation:** Group that moves as unit
- **Boss:** Large, multi-phase, pattern-based

### Structure
- 8 stages, each with distinct enemy patterns
- Boss at end of stages 4 and 8
- Difficulty increases per stage
- Loop with harder enemies after stage 8
- Bonus stages between some levels

### Audio
- Full SID soundtrack (different tune per stage pair)
- Layered sound effects
- Boss music
- Victory/defeat jingles
- Power-up sounds

### Visuals
- Parallax scrolling starfield (3 layers)
- Animated player ship (thrust flames)
- Animated enemies
- Explosion sprites
- Power-up sprites with glow
- Screen shake on hits
- Flash effects

### Polish
- Title screen with ship animation
- Attract mode showing gameplay
- High score table
- Two-player alternating mode
- Stage select (after completion)
- Statistics tracking

---

## Phase 1: Foundation (Units 1-16)

*Goal: Core shooter gameplay. Ship moves, shoots, enemies appear and can be destroyed. Collision works. One enemy type, one weapon.*

*This phase moves faster than SID Symphony Phase 1 because fundamentals are established. Focus is on sprites and shooter mechanics.*

---

### Unit 1: First Sprite

**Prerequisites from SID Symphony:** BASIC stub, memory layout, assembly basics

**Learning Objectives:**
- Understand the VIC-II sprite system
- Enable and position a hardware sprite
- Set sprite colour
- See the difference between characters and sprites

**Concepts Introduced:**
- VIC-II sprite registers ($D000-$D02E)
- Sprite enable register ($D015)
- Sprite X/Y position registers
- Sprite colour registers ($D027-$D02E)
- Sprite pointers (SCREEN + $03F8)

**Code Written:**
```
- Apply SID Symphony BASIC stub (assumed knowledge)
- Enable sprite 0
- Set sprite pointer to built-in ROM data
- Position sprite at centre screen
- Set sprite colour to white
```

**What the Learner Sees:**
A sprite appears on screen - a simple shape from ROM. It's visually different from characters - smooth, positionable anywhere. The foundation of action games.

**Reference to SID Symphony:**
"Remember setting up the BASIC stub and screen colours? We'll use that same setup, but now we're adding something new - hardware sprites."

---

### Unit 2: Custom Sprite Design

**Learning Objectives:**
- Design a custom sprite graphic
- Understand sprite data format (63 bytes)
- Create a player ship sprite
- Position sprite precisely

**Concepts Introduced:**
- Sprite data format (24 pixels × 21 rows × 1 bit = 63 bytes)
- 64-byte alignment requirement
- Sprite pointer calculation (address / 64)
- Designing on 24×21 grid

**Code Written:**
```
- Design player ship sprite data
- Store at 64-byte aligned address
- Point sprite 0 to custom data
- Position at bottom centre of screen
```

**What the Learner Sees:**
A proper spaceship sprite - the player's ship - positioned at the bottom of the screen. It looks like a real game.

**Ship Design:**
```
       ████
      ██████
     ████████
    ██████████
   ████████████
  ██████████████
 ████████████████
████████████████████
  ████      ████
   ██        ██
```

---

### Unit 3: Joystick Input

**Prerequisites from SID Symphony:** Input handling concepts (keyboard)

**Learning Objectives:**
- Read joystick via CIA chip
- Understand joystick bit layout
- Move sprite based on input
- Apply movement boundaries

**Concepts Introduced:**
- CIA #1 Port A ($DC00)
- Joystick 2 bit layout (active low)
- Direction detection (up, down, left, right)
- Fire button detection

**Code Written:**
```
- Read $DC00 each frame
- Check each direction bit
- Modify sprite position accordingly
- Clamp to screen boundaries
```

**What the Learner Sees:**
The ship moves smoothly with the joystick. It stops at screen edges. The fire button is detected (but doesn't do anything yet). Interactive.

**Reference to SID Symphony:**
"In SID Symphony we read the keyboard matrix. Joystick reading is simpler - one register, five bits, active low."

**Technical Details:**
- Bit 0: Up (0 = pressed)
- Bit 1: Down
- Bit 2: Left
- Bit 3: Right
- Bit 4: Fire

---

### Unit 4: Game Loop with Sprites

**Prerequisites from SID Symphony:** Game loop structure, raster sync

**Learning Objectives:**
- Apply SID Symphony game loop pattern
- Update sprite positions each frame
- Maintain stable frame rate with sprites
- Separate update logic from display

**Concepts Introduced:**
- Sprite position updates in game loop
- Position variables vs register writes
- Double-buffering concept (preview)
- Frame timing with sprite updates

**Code Written:**
```
- Apply game loop structure from SID Symphony
- Player position in zero page
- Update position from input
- Write positions to VIC-II once per frame
- Verify smooth 50fps movement
```

**What the Learner Sees:**
Rock-solid smooth movement. No flickering, no tearing. The game loop pattern from SID Symphony works perfectly with sprites.

**Reference to SID Symphony:**
"This is exactly the game loop structure we built in Unit 7 of SID Symphony. Same raster wait, same frame structure, different content."

---

### Unit 5: The Bullet Sprite

**Learning Objectives:**
- Add a second sprite type
- Spawn sprite on button press
- Move sprite independently
- Understand sprite independence

**Concepts Introduced:**
- Multiple sprite management
- Sprite spawning (enable + position)
- Independent movement per sprite
- Sprite as "object"

**Code Written:**
```
- Design bullet sprite (small, bright)
- Fire button spawns bullet at ship position
- Bullet moves upward each frame
- Disable when off screen
```

**What the Learner Sees:**
Press fire and a bullet shoots upward from the ship. It disappears at the top of the screen. The ship can fire!

---

### Unit 6: Bullet Management

**Prerequisites from SID Symphony:** Data structures, arrays

**Learning Objectives:**
- Manage multiple bullets simultaneously
- Implement an object pool
- Fire rate limiting
- Efficient array traversal

**Concepts Introduced:**
- Bullet pool (4 simultaneous bullets)
- Active/inactive flags
- Finding free slots
- Fire delay timer

**Code Written:**
```
- bullet_active: array of 4 flags
- bullet_x, bullet_y: position arrays
- spawn_bullet: find free slot, initialise
- update_bullets: move all active bullets
- Fire delay prevents button mashing
```

**What the Learner Sees:**
Up to 4 bullets on screen at once. Can't fire too fast (rate limited). Bullets recycle when they leave the screen. Proper shoot-em-up feel.

**Reference to SID Symphony:**
"Remember the active notes array in SID Symphony? Bullets work the same way - a pool of objects we enable and disable as needed."

---

### Unit 7: The Enemy Sprite

**Learning Objectives:**
- Add enemy sprite
- Basic enemy movement (downward)
- Multiple enemies on screen
- Enemy spawning system

**Concepts Introduced:**
- Enemy object structure
- Simple AI (move down)
- Spawn timing
- Enemy pool management

**Code Written:**
```
- Design enemy sprite (alien/drone)
- Enemy pool (4 enemies to start)
- Spawn timer (new enemy every N frames)
- Enemies move downward
- Despawn at bottom of screen
```

**What the Learner Sees:**
Alien enemies appear at the top and drift downward. Multiple enemies on screen. They don't interact yet but it looks like a game.

---

### Unit 8: Sprite-Sprite Collision

**Learning Objectives:**
- Use hardware collision detection
- Read collision registers
- Determine which sprites collided
- React to collisions

**Concepts Introduced:**
- Sprite-sprite collision register ($D01E)
- Collision bits (one per sprite)
- Collision cleared on read
- Collision checking in game loop

**Code Written:**
```
- Read $D01E each frame
- Check if bullet sprites collide with enemy sprites
- If collision: deactivate both bullet and enemy
- Play explosion sound (apply SID Symphony knowledge)
```

**What the Learner Sees:**
Bullets destroy enemies! The collision is automatic (hardware detected). Destroyed enemies disappear. The core gameplay loop works.

**Technical Details:**
- $D01E: sprite-sprite collision
- Each bit represents one sprite
- Read clears the register
- Must check quickly or lose collision data

---

### Unit 9: Scoring

**Prerequisites from SID Symphony:** Score display, 16-bit arithmetic

**Learning Objectives:**
- Apply SID Symphony scoring system
- Award points for enemy kills
- Display score on screen
- Track high score

**Concepts Introduced:**
- Score values per enemy type
- Score display positioning (applied knowledge)
- High score tracking
- HUD layout for shooters

**Code Written:**
```
- Apply score system from SID Symphony
- 100 points per drone destroyed
- Display at top of screen
- Track high score (session)
```

**What the Learner Sees:**
Score at top of screen increases with kills. High score shown alongside. Same satisfying scoring from SID Symphony.

**Reference to SID Symphony:**
"This is exactly the scoring system from Unit 13. Same 16-bit addition, same decimal display. We're just applying it to a shooter context."

---

### Unit 10: Player Lives

**Prerequisites from SID Symphony:** Health/lives system

**Learning Objectives:**
- Implement lives system
- Detect player-enemy collision
- Handle player death
- Respawn with brief invincibility

**Concepts Introduced:**
- Player hitbox considerations
- Death state handling
- Respawn invincibility timer
- Visual feedback for damage

**Code Written:**
```
- 3 lives to start
- Enemy touching player = lose life
- Brief invincibility on respawn (flashing sprite)
- Game over when lives = 0
```

**What the Learner Sees:**
Enemies are dangerous now. Getting hit loses a life. The ship flashes when respawning. Three lives means three chances. Game over is possible.

**Reference to SID Symphony:**
"The lives system works like the health meter from SID Symphony - a resource that depletes on failure. We're just discretising it into lives instead of a continuous bar."

---

### Unit 11: Wave Structure

**Prerequisites from SID Symphony:** State machines, progression

**Learning Objectives:**
- Structure game into waves
- Increase difficulty per wave
- Wave completion detection
- Inter-wave display

**Concepts Introduced:**
- Wave as game unit
- Enemies per wave
- Wave completion trigger
- Difficulty scaling

**Code Written:**
```
- Wave counter
- Enemies spawned per wave (increases with wave)
- Wave complete when all enemies destroyed
- "WAVE X" display between waves
- Brief pause before next wave
```

**What the Learner Sees:**
Game structured into waves. "WAVE 1" appears, enemies come, clear them, "WAVE 2" appears with more enemies. Sense of progression.

---

### Unit 12: Sound Effects

**Prerequisites from SID Symphony:** Full SID sound design

**Learning Objectives:**
- Apply SID Symphony sound techniques
- Create shooter-appropriate sounds
- Layer sounds during gameplay
- Audio feedback for all actions

**Concepts Introduced:**
- Shoot sound design
- Explosion sound design
- Player death sound
- Sound priority (which voice for what)

**Code Written:**
```
- Shoot sound: short, punchy noise
- Enemy explosion: filtered noise burst
- Player death: longer, lower explosion
- Apply techniques from SID Symphony Units 41-43
```

**What the Learner Sees:**
Full audio feedback. Every shot, explosion, and death has a sound. The game has presence.

**Reference to SID Symphony:**
"Remember the perfect hit effects? Same idea - layer audio feedback on every significant event. We'll use voice 3 for shoot, voice 2 for explosions."

---

### Unit 13: Basic Enemy AI

**Learning Objectives:**
- Give enemies simple behaviour
- Movement patterns beyond "down"
- Enemies that react to player
- Variety through behaviour

**Concepts Introduced:**
- AI as behaviour function
- Pattern types (linear, sine, tracking)
- Behaviour parameters
- Enemy type determines behaviour

**Code Written:**
```
- Three behaviours: straight, sine-wave, track-player
- Enemy type field determines behaviour
- Sine wave using lookup table
- Tracking: move toward player X
```

**What the Learner Sees:**
Enemies aren't all the same anymore. Some drift down, some weave, some follow the player. Each feels distinct.

---

### Unit 14: Enemy Shooting

**Learning Objectives:**
- Enemies that fight back
- Enemy bullet pool
- Collision with player
- Dodging as mechanic

**Concepts Introduced:**
- Enemy bullets (separate pool)
- Aimed shots (toward player)
- Random shots (periodic)
- Bullet speed tuning

**Code Written:**
```
- Enemy bullet pool (4 bullets)
- Some enemies shoot periodically
- Bullets aimed at player position
- Player collision with enemy bullets
```

**What the Learner Sees:**
It's a real fight now. Enemies shoot back. The player must dodge as well as shoot. Tension increases.

---

### Unit 15: Game Over and Continue

**Prerequisites from SID Symphony:** Results screen, state handling

**Learning Objectives:**
- Game over state
- Results display
- Continue option
- Return to title

**Concepts Introduced:**
- Game over screen
- Final score display
- Continue prompt
- State reset

**Code Written:**
```
- Game over state
- Display final score, wave reached
- "CONTINUE? 9..." countdown
- If fire: restart with score
- If timeout: return to title
```

**What the Learner Sees:**
Game over screen with stats. Option to continue (for now, infinite continues). Countdown adds urgency. Complete game loop.

---

### Unit 16: Phase 1 Complete - Core Playtest

**Learning Objectives:**
- Playtest complete core loop
- Identify balance issues
- Tune difficulty curve
- Document improvements needed

**Concepts Introduced:**
- Playtesting methodology (applied)
- Balance tuning
- First playable milestone
- Feedback incorporation

**Code Written:**
```
- Playtest session
- Adjust enemy speed/spawn rates
- Tune collision feel
- Fix any bugs found
- Document Phase 2 priorities
```

**What the Learner Sees:**
A complete, if simple, shooter. Can play multiple waves, die, continue, game over. Core mechanics feel good. Ready for content.

**Phase 1 Checkpoint:**
Core shooter complete. Player ship, bullets, enemies, collision, scoring, lives, waves, game over. One enemy type, one weapon, basic AI. All built faster than SID Symphony Phase 1 because foundations exist.

---

## Phase 2: Expansion (Units 17-32)

*Goal: Content and variety. Multiple enemy types, weapon upgrades, power-ups, boss battles, stages. A game with depth.*

---

### Unit 17: Title Screen

**Prerequisites from SID Symphony:** Title screen design, menus

**Learning Objectives:**
- Apply SID Symphony title screen techniques
- Shooter-appropriate presentation
- Ship sprite in title
- Menu options

**Concepts Introduced:**
- Title screen composition for action game
- Sprite use in menus
- Visual identity

**Code Written:**
```
- "STARFIELD" logo with custom characters
- Player ship sprite animated on title
- Menu: Start Game, Options, High Scores
- Apply colour cycling from SID Symphony
```

**What the Learner Sees:**
Professional title screen with animated ship. Clear menu options. Sets expectations for quality.

**Reference to SID Symphony:**
"Same title screen techniques from Units 33-34. We'll add a sprite animation unique to Starfield."

---

### Unit 18: Enemy Type - Weaver

**Learning Objectives:**
- Implement distinct enemy type
- Sine-wave movement refined
- Visual distinction
- Behaviour variety

**Concepts Introduced:**
- Enemy type system
- Type-specific sprites
- Type-specific behaviour
- Spawn variety

**Code Written:**
```
- Weaver sprite design (different from drone)
- Refined sine movement
- Different point value
- Mixed spawning (drones + weavers)
```

**What the Learner Sees:**
A new enemy type - weaves across screen in sine pattern. Looks different, moves different, scores different. Variety.

---

### Unit 19: Enemy Type - Diver

**Learning Objectives:**
- Implement aggressive enemy type
- Diagonal dive toward player
- Threat assessment
- Spawn balancing

**Concepts Introduced:**
- Dive angle calculation
- Lock-on position
- Threat priority
- Danger communication (visual)

**Code Written:**
```
- Diver sprite design (angular, aggressive)
- Calculate dive vector when spawned
- Fast diagonal movement
- Higher point value (risky to let close)
```

**What the Learner Sees:**
Divers are dangerous - they swoop at you. Must be prioritised. Creates moment-to-moment decisions.

---

### Unit 20: Enemy Type - Shooter

**Learning Objectives:**
- Enemy that stays on screen
- Periodic shooting behaviour
- Strategic target
- Movement with shooting

**Concepts Introduced:**
- Stationary-ish enemies
- Fire timing
- Patrol patterns
- Priority targeting

**Code Written:**
```
- Shooter sprite design (gun visible)
- Horizontal patrol movement
- Shoot at intervals
- Aimed shots toward player
```

**What the Learner Sees:**
Shooters patrol and fire. They're priority targets because they keep shooting. Strategic layer emerges.

---

### Unit 21: Power-Up - Weapon Upgrade

**Learning Objectives:**
- Implement power-up system
- Weapon upgrade levels
- Power-up spawning
- Power-up collection

**Concepts Introduced:**
- Power-up sprite
- Collection collision
- Weapon levels (1-3)
- Shot patterns per level

**Code Written:**
```
- Power-up sprite (glowing P)
- Dropped by certain enemies
- Collect to upgrade weapon
- Level 1: single shot
- Level 2: double shot
- Level 3: spread shot
```

**What the Learner Sees:**
Some enemies drop power-ups. Collecting upgrades weapon from single → double → spread shot. Feels powerful.

---

### Unit 22: Power-Up - Shield

**Learning Objectives:**
- Implement defensive power-up
- Temporary invincibility
- Visual feedback for state
- Timer management

**Concepts Introduced:**
- Shield state
- Invincibility timer
- Shield sprite overlay
- Visual countdown (flashing)

**Code Written:**
```
- Shield power-up sprite (S)
- Collecting grants 5 seconds invincibility
- Shield sprite surrounds player
- Flashing when about to expire
```

**What the Learner Sees:**
Shield power-up grants temporary protection. Glowing shield around ship. Confidence to play aggressively briefly.

---

### Unit 23: Power-Up - Bomb

**Learning Objectives:**
- Implement screen-clear weapon
- Limited resource management
- Spectacular effect
- Strategic use

**Concepts Introduced:**
- Bomb counter
- Screen-clear logic
- Big explosion effect
- Resource scarcity

**Code Written:**
```
- Bomb power-up sprite (B)
- Press space to use bomb
- Destroys all enemies on screen
- Full-screen flash effect
- Limited to 3 max
```

**What the Learner Sees:**
Bombs clear the screen in an emergency. Spectacular explosion effect. Limited supply creates tension.

---

### Unit 24: Stage Structure

**Learning Objectives:**
- Structure game into stages
- Stage-specific enemy mix
- Stage progression
- Visual stage identity

**Concepts Introduced:**
- Stage as larger unit than wave
- Stage enemy composition
- Stage backgrounds (colour)
- 8-stage structure

**Code Written:**
```
- 8 stages, multiple waves each
- Each stage has enemy mix
- Background colour per stage
- "STAGE X" display
```

**What the Learner Sees:**
Game divided into stages. Each stage has distinct enemy mix. Background colour changes. Clearer progression.

---

### Unit 25: Boss - Design

**Learning Objectives:**
- Design a large enemy
- Multi-sprite boss
- Boss distinct from normal enemies
- Imposing presence

**Concepts Introduced:**
- Multi-sprite characters
- Sprite combining
- Large enemy design
- Boss as challenge

**Code Written:**
```
- Boss design: 2x2 sprites (4 total)
- Position sprites relative to boss position
- Boss sprite data
- Boss enable/disable
```

**What the Learner Sees:**
A large, imposing boss sprite. Takes up multiple sprite slots. Clearly different from regular enemies.

---

### Unit 26: Boss - Behaviour

**Learning Objectives:**
- Implement boss movement patterns
- Boss attack patterns
- Multi-phase behaviour
- Boss health system

**Concepts Introduced:**
- Boss health pool
- Phase transitions
- Attack patterns
- Boss-specific bullets

**Code Written:**
```
- Boss health (many hits required)
- Phase 1: side-to-side, shoots down
- Phase 2 (half health): faster, spreads shots
- Visual damage indication
```

**What the Learner Sees:**
Boss moves in patterns, shoots at player. Takes many hits. Gets more aggressive when damaged. Real boss fight.

---

### Unit 27: Boss - Defeat

**Learning Objectives:**
- Boss destruction sequence
- Reward for victory
- Stage completion
- Dramatic presentation

**Concepts Introduced:**
- Multi-explosion sequence
- Score bonus
- Victory fanfare
- Stage transition

**Code Written:**
```
- Boss defeat triggers explosion sequence
- Multiple explosions across boss sprite
- Big score bonus
- Victory sound
- Advance to next stage
```

**What the Learner Sees:**
Defeating the boss triggers spectacular explosion sequence. Big points. Victory music. Satisfying conclusion to stage.

---

### Unit 28: Second Boss

**Learning Objectives:**
- Implement variety in bosses
- Different attack patterns
- Stage 8 boss (finale)
- Unique challenge

**Concepts Introduced:**
- Boss variety
- Different bullet patterns
- Final boss difficulty
- Pattern memorisation

**Code Written:**
```
- Stage 8 boss: different sprite design
- Different movement pattern (circular?)
- Different attacks (spiral bullets)
- Harder than Stage 4 boss
```

**What the Learner Sees:**
Stage 8 boss is different and harder. New patterns to learn. Climactic final challenge.

---

### Unit 29: Enemy Formations

**Learning Objectives:**
- Groups of enemies moving together
- Formation patterns
- Formation breaking
- Visual spectacle

**Concepts Introduced:**
- Formation as meta-object
- Relative positioning
- Formation destruction bonus
- Formation types

**Code Written:**
```
- Formation data: positions relative to leader
- Formation movement (leader drives)
- Bonus for destroying entire formation
- V-formation, line formation, diamond
```

**What the Learner Sees:**
Enemies sometimes arrive in formation. Destroying the whole formation gives bonus. Strategic choice: formation or individuals?

---

### Unit 30: Bonus Stage

**Learning Objectives:**
- Implement special stage type
- No enemies, just targets
- Score opportunity
- Variety in gameplay

**Concepts Introduced:**
- Stage type flag
- Bonus rules (no death)
- Target spawning
- Bonus scoring

**Code Written:**
```
- Bonus stage between stages 4 and 5
- Rapid targets, no enemy bullets
- Every target hit = points
- Perfect clear bonus
```

**What the Learner Sees:**
A break from combat. Pure shooting gallery. Rack up points without danger. Refreshing change of pace.

---

### Unit 31: High Score Integration

**Prerequisites from SID Symphony:** High score table

**Learning Objectives:**
- Apply SID Symphony high score system
- Stage reached tracking
- Leaderboard display
- Initials entry

**Concepts Introduced:**
- Extended high score data (score + stage)
- Applied knowledge

**Code Written:**
```
- Apply high score system from SID Symphony
- Track stage reached per score
- Display: "AAA 123450 STG 5"
- Same entry system
```

**What the Learner Sees:**
High score table shows scores and stages reached. Name entry works same as SID Symphony.

**Reference to SID Symphony:**
"This is Unit 45 applied directly. Same data structure, same entry UI, extended to include stage reached."

---

### Unit 32: Content Complete Playtest

**Learning Objectives:**
- Full content playtest
- Balance across stages
- Enemy mix tuning
- Boss difficulty

**Concepts Introduced:**
- Full game playtest
- Balance spreadsheet
- Difficulty curve graphing
- Feedback processing

**Code Written:**
```
- Complete playtest all 8 stages
- Document difficulty spikes
- Adjust enemy counts, speeds
- Tune boss health
```

**What the Learner Sees:**
Complete game with all content. 8 stages, 2 bosses, 4 enemy types, 3 power-ups, formations, bonus stage. Ready for polish.

**Phase 2 Checkpoint:**
Full content game. 4 enemy types, 3 power-ups, weapon upgrades, 2 boss fights, 8 stages, bonus stage, formations. Rich variety built efficiently using SID Symphony foundations.

---

## Phase 3: Polish (Units 33-48)

*Goal: Visual spectacle and audio polish. Parallax starfield, explosions, animations, full soundtrack. Commercial presentation.*

---

### Unit 33: Parallax Starfield - Single Layer

**Learning Objectives:**
- Scrolling background basics
- Star character graphics
- Vertical scrolling
- Creating depth

**Concepts Introduced:**
- Background scrolling (characters)
- Star characters in custom set
- Scroll position tracking
- Wrap-around logic

**Code Written:**
```
- Star characters (dot, small star, large star)
- Single layer scrolling downward
- Different star densities
- Smooth scroll via colour RAM trick or char cycling
```

**What the Learner Sees:**
Stars scroll past in background. Creates sense of movement. Space feels like space.

---

### Unit 34: Parallax Starfield - Multi Layer

**Learning Objectives:**
- Multiple scroll speeds
- Depth perception
- Performance management
- Visual richness

**Concepts Introduced:**
- Parallax depth effect
- Layer management
- Speed ratios (1x, 2x, 4x)
- Memory/CPU trade-offs

**Code Written:**
```
- Three star layers
- Dim/slow, medium, bright/fast
- Different scroll speeds
- Seamless looping
```

**What the Learner Sees:**
Three layers of stars at different speeds. Strong sense of depth and speed. Professional space game feel.

---

### Unit 35: Player Ship Animation

**Learning Objectives:**
- Sprite animation frames
- State-based animation
- Thrust flame effect
- Banking on movement

**Concepts Introduced:**
- Animation frame cycling
- State-driven animation
- Direction-based sprites
- Animation timing

**Code Written:**
```
- Ship sprite frames: neutral, left bank, right bank
- Thrust flame animation (2 frames)
- Switch frames based on movement
- Smooth transitions
```

**What the Learner Sees:**
Ship banks when moving left/right. Thrust flame flickers. Ship feels alive and responsive.

---

### Unit 36: Enemy Animations

**Learning Objectives:**
- Animate enemy sprites
- Distinct animations per type
- Performance with many animations
- Character through motion

**Concepts Introduced:**
- Shared animation timing
- Type-specific frames
- Animation pools
- Character animation

**Code Written:**
```
- Each enemy type: 2-4 animation frames
- Weaver: undulating
- Diver: wings back when diving
- Shooter: gun flash when firing
```

**What the Learner Sees:**
All enemies animate. Each type has character. The screen is alive with motion.

---

### Unit 37: Explosion Effects

**Learning Objectives:**
- Multi-frame explosion
- Sprite-based explosions
- Explosion pool
- Particle feel

**Concepts Introduced:**
- Explosion sprite sequence
- Explosion as object
- Frame timing
- Multiple simultaneous explosions

**Code Written:**
```
- Explosion frames (4-6 stages)
- Explosion pool (4 simultaneous)
- Spawn at enemy death position
- Auto-destroy after sequence
```

**What the Learner Sees:**
Enemies explode with animated sequence. Multiple explosions on screen. Destruction feels impactful.

---

### Unit 38: Screen Effects

**Prerequisites from SID Symphony:** Screen flash, border effects

**Learning Objectives:**
- Apply SID Symphony effect techniques
- Shooter-appropriate effects
- Screen shake
- Flash on damage

**Concepts Introduced:**
- Screen shake (offset trick)
- Damage flash
- Boss hit flash
- Effect layering

**Code Written:**
```
- Screen shake on player hit
- Border flash on bomb use
- Boss flashes when hit
- Apply techniques from SID Symphony Units 37-39
```

**What the Learner Sees:**
Screen shakes on damage. Bombs flash the border. Hits have impact. Borrowed from SID Symphony's juice.

**Reference to SID Symphony:**
"Remember the perfect hit effects? Same principles. Layer visual feedback on significant events."

---

### Unit 39: Power-Up Polish

**Learning Objectives:**
- Power-up visual appeal
- Collection effects
- Glow/pulse animation
- Audio cues

**Concepts Introduced:**
- Item attraction (optional)
- Collection particle
- Upgrade flash
- Sound design for pickups

**Code Written:**
```
- Power-ups pulse/glow
- Collection sound (rising pitch)
- Weapon upgrade: brief invincibility flash
- Shield: activation sound
```

**What the Learner Sees:**
Power-ups look valuable. Collecting them feels rewarding. Clear audio feedback.

---

### Unit 40: SID Soundtrack - Main Theme

**Prerequisites from SID Symphony:** Music composition

**Learning Objectives:**
- Compose action game music
- Driving, energetic feel
- Apply SID Symphony techniques
- Music that fits shooting

**Concepts Introduced:**
- Action music composition
- Tempo for intensity
- Bass-driven energy
- Loop points

**Code Written:**
```
- Main game music: energetic, looping
- Uses techniques from SID Symphony
- Bassline drives rhythm
- 30-60 second loop
```

**What the Learner Sees:**
Driving music during gameplay. Matches the action intensity. Professional audio.

**Reference to SID Symphony:**
"Apply everything from SID Symphony about composition, but for action intensity rather than rhythm game."

---

### Unit 41: SID Soundtrack - Boss Theme

**Learning Objectives:**
- Compose boss music
- Different feel from main
- Tension and danger
- Victory transition

**Concepts Introduced:**
- Boss music conventions
- Musical tension
- Intensity increase
- Victory stinger

**Code Written:**
```
- Boss theme: tense, dangerous
- Different feel from main theme
- Higher intensity
- Victory stinger on defeat
```

**What the Learner Sees:**
Music changes for boss fights. Tension increases. Victory music celebrates win. Music tells the story.

---

### Unit 42: Sound Mix Polish

**Prerequisites from SID Symphony:** Sound mixing

**Learning Objectives:**
- Balance SFX with music
- Voice allocation strategy
- Priority system
- Clean mix

**Concepts Introduced:**
- Voice stealing
- Priority levels
- Mix balance
- Audio clarity

**Code Written:**
```
- Assign voices: 1-2 music, 3 SFX (or dynamic)
- Priority: explosion > shoot > ambient
- Mix levels balanced
- Test across speakers
```

**What the Learner Sees:**
Audio is clean and balanced. SFX don't drown music. Everything audible. Professional mix.

---

### Unit 43: HUD Polish

**Prerequisites from SID Symphony:** UI design

**Learning Objectives:**
- Shooter HUD best practices
- Information hierarchy
- Visual clarity during action
- Score/lives/bombs display

**Concepts Introduced:**
- HUD positioning for shooters
- Weapon level display
- Bomb inventory display
- Stage indicator

**Code Written:**
```
- Score: top left
- Lives: top right (ship icons)
- Bombs: below lives (bomb icons)
- Weapon level: bar or indicators
- Stage: subtle corner display
```

**What the Learner Sees:**
Clean, readable HUD. All information visible at a glance. Doesn't interfere with gameplay.

---

### Unit 44: Attract Mode

**Prerequisites from SID Symphony:** Attract mode

**Learning Objectives:**
- Apply SID Symphony attract mode
- Demo gameplay recording/playback
- Showcase features
- Cycle through content

**Concepts Introduced:**
- Demo recording (or scripted)
- Feature showcase
- Title cycle

**Code Written:**
```
- Record demo playthrough (or script)
- Play during title idle
- Show different stages
- Any key returns to title
```

**What the Learner Sees:**
Game plays itself on title screen. Shows off gameplay, enemies, bosses. Commercial presentation.

**Reference to SID Symphony:**
"Same attract mode system from Unit 35. Record or script a demo, play it back on idle."

---

### Unit 45: Options Screen

**Prerequisites from SID Symphony:** Options screen

**Learning Objectives:**
- Apply SID Symphony options
- Shooter-specific options
- Control configuration
- Difficulty selection

**Concepts Introduced:**
- Starting lives option
- Starting stage (after clear)
- Sound test
- Control layout

**Code Written:**
```
- Apply options framework from SID Symphony
- Lives: 3, 5, 7
- Starting stage: 1 (or unlocked)
- Sound test (music + SFX)
```

**What the Learner Sees:**
Options screen with shooter-relevant choices. Player control over experience.

**Reference to SID Symphony:**
"Same options structure from Unit 46. Different options for shooter context."

---

### Unit 46: Continue System Polish

**Learning Objectives:**
- Refine continue system
- Limited continues
- Continue points
- Tension management

**Concepts Introduced:**
- Limited continues (3)
- Continue from current stage
- Score reset on continue
- Continue count display

**Code Written:**
```
- 3 continues available
- Continue restarts current stage
- Score resets on continue
- Display continues remaining
```

**What the Learner Sees:**
Continues are limited - creates real stakes. Using one costs your score. Tension maintained.

---

### Unit 47: Pause Polish

**Prerequisites from SID Symphony:** Pause system

**Learning Objectives:**
- Apply SID Symphony pause
- Shooter pause needs
- Clean audio pause
- Resume countdown

**Concepts Introduced:**
- Music pause (not stop)
- Pause menu options
- Resume preparation

**Code Written:**
```
- Apply pause system from SID Symphony
- Music pauses cleanly
- Options: Resume, Restart Stage, Quit
- 3-2-1 countdown on resume
```

**What the Learner Sees:**
Pause works cleanly. Music pauses (doesn't restart). Countdown prepares for action.

**Reference to SID Symphony:**
"Same pause system from Unit 47. Applied directly."

---

### Unit 48: Polish Pass

**Learning Objectives:**
- Full game polish playtest
- Find and fix rough edges
- Visual consistency
- Audio consistency

**Concepts Introduced:**
- Polish methodology
- Bug triage
- Consistency checking
- Final tuning

**Code Written:**
```
- Playtest all content
- Fix visual inconsistencies
- Adjust animations
- Tune audio levels
- Performance check
```

**What the Learner Sees:**
Everything feels polished. No rough edges. Consistent quality throughout.

**Phase 3 Checkpoint:**
Polished, professional game. Parallax starfield, animations, effects, full soundtrack. Commercial presentation.

---

## Phase 4: Mastery (Units 49-64)

*Goal: Advanced techniques and final release. Sprite multiplexing for more enemies, optimisation, two-player, packaging.*

---

### Unit 49: Sprite Multiplexing - Theory

**Learning Objectives:**
- Understand sprite limitation
- Multiplexing concept
- Y-sorting requirement
- Raster interrupt approach

**Concepts Introduced:**
- 8 sprite hardware limit
- Raster-based reuse
- Sort by Y position
- Interrupt timing

**Code Written:**
```
- Document current sprite usage
- Plan multiplexer design
- Implement Y-sort routine
- Prototype interrupt timing
```

**What the Learner Sees:**
No visible change yet. Understanding builds for implementation.

---

### Unit 50: Sprite Multiplexing - Implementation

**Learning Objectives:**
- Implement working multiplexer
- Handle more than 8 objects
- Maintain stable display
- Performance management

**Concepts Introduced:**
- Multiplexer main loop
- Sprite allocation per raster zone
- Object-to-sprite mapping
- Debugging techniques

**Code Written:**
```
- Multiplexer core routine
- Up to 16 objects supported
- Automatic sprite assignment
- Raster interrupt handler
```

**What the Learner Sees:**
More than 8 enemies on screen! Formations of 12+ enemies. Bullets don't steal enemy slots. More intense gameplay.

---

### Unit 51: Multiplexer Polish

**Learning Objectives:**
- Handle edge cases
- Prevent flickering
- Optimise performance
- Production quality

**Concepts Introduced:**
- Flicker prevention
- Sort stability
- Priority handling
- Performance profiling

**Code Written:**
```
- Fix any flicker issues
- Handle worst-case scenarios
- Optimise sort routine
- Profile and document performance
```

**What the Learner Sees:**
Solid, stable multiplexing. No visible artifacts. Can have busy screens without issues.

---

### Unit 52: More Enemies On Screen

**Learning Objectives:**
- Use multiplexer for gameplay
- Increase enemy counts
- Adjust difficulty
- Visual spectacle

**Concepts Introduced:**
- Bullet hell lite
- Enemy count balancing
- Overwhelming moments
- Managing chaos

**Code Written:**
```
- Increase enemies per wave
- More complex formations
- Bullet counts increased
- Adjust difficulty for new intensity
```

**What the Learner Sees:**
Later stages have more enemies than before. Feels more intense. Multiplexer enables new gameplay possibilities.

---

### Unit 53: Code Optimisation

**Prerequisites from SID Symphony:** Optimisation techniques

**Learning Objectives:**
- Apply SID Symphony optimisation
- Profile shooter code
- Optimise hot paths
- Free up CPU for multiplexer

**Concepts Introduced:**
- Cycle budgeting
- Multiplexer overhead
- Shooter-specific bottlenecks
- Applied optimisation

**Code Written:**
```
- Profile game performance
- Optimise collision loops
- Optimise sprite updates
- Apply techniques from SID Symphony
```

**What the Learner Sees:**
Game runs smoother. Can handle more on screen. Professional performance.

**Reference to SID Symphony:**
"Same optimisation methodology from Units 49-51. Profile, identify hot paths, optimise."

---

### Unit 54: Memory Optimisation

**Prerequisites from SID Symphony:** Memory optimisation

**Learning Objectives:**
- Apply SID Symphony memory techniques
- Compress sprite data
- Optimise level data
- Free RAM

**Concepts Introduced:**
- Sprite data compression
- Level data format
- RAM map optimisation
- Applied techniques

**Code Written:**
```
- Compress sprite data where possible
- Optimise stage data
- Free unused RAM
- Document memory map
```

**What the Learner Sees:**
Same game, smaller footprint. Room for expansion if needed.

**Reference to SID Symphony:**
"Same memory optimisation from Unit 50. Applied to shooter data."

---

### Unit 55: Two-Player Mode - Alternating

**Learning Objectives:**
- Implement two-player option
- Alternating turns
- Separate scores
- Competition

**Concepts Introduced:**
- Two-player state
- Score per player
- Turn switching
- Winner determination

**Code Written:**
```
- Two-player option in menu
- Player 1 plays until death
- Player 2 takes turn
- Track scores separately
- Winner at game over
```

**What the Learner Sees:**
Two players can compete, taking turns. Each has own score. Winner announced.

---

### Unit 56: Two-Player Mode - Cooperative (Optional Challenge)

**Learning Objectives:**
- Simultaneous two-player
- Sprite budget management
- Shared screen
- Cooperative scoring

**Concepts Introduced:**
- Two ships on screen
- Sprite allocation for two
- Lives shared or separate
- Team scoring

**Code Written:**
```
- Both players on screen simultaneously
- Player 1: keyboard or joy 1
- Player 2: joy 2
- Shared lives pool
- Combined score
```

**What the Learner Sees:**
Two players on screen together! Chaos and fun. Cooperative or competitive (friendly fire option?).

---

### Unit 57: Stage Select

**Learning Objectives:**
- Implement stage select
- Unlock condition
- Practice past content
- Replay value

**Concepts Introduced:**
- Stage unlock tracking
- Stage select UI
- High score per stage
- Practice vs score mode

**Code Written:**
```
- Stage select screen (unlocked after clear)
- Can start from any cleared stage
- No score in stage select (practice)
- Tracks best stage time
```

**What the Learner Sees:**
After beating the game, can start from any stage. Practice specific sections. Replay value.

---

### Unit 58: Statistics and Achievements

**Prerequisites from SID Symphony:** Statistics tracking

**Learning Objectives:**
- Apply SID Symphony statistics
- Shooter-specific stats
- Achievement tracking
- Long-term goals

**Concepts Introduced:**
- Total enemies destroyed
- Bosses defeated
- Power-ups collected
- Stage clear times

**Code Written:**
```
- Statistics tracking (applied from SID Symphony)
- Shooter-specific stats
- Stats display screen
- Simple achievements
```

**What the Learner Sees:**
Statistics show lifetime progress. Achievements for milestones. Long-term engagement.

**Reference to SID Symphony:**
"Same statistics system from Unit 31. Extended for shooter metrics."

---

### Unit 59: Ending Sequence

**Learning Objectives:**
- Create game ending
- Victory celebration
- Story conclusion (simple)
- Reward for completion

**Concepts Introduced:**
- Ending sequence
- Story screens
- Victory music
- Credits roll

**Code Written:**
```
- Ending triggered after Stage 8 boss
- Simple story screens ("The galaxy is saved!")
- Victory music
- Roll into credits
```

**What the Learner Sees:**
Completing the game shows ending sequence. Story closure. Victory music. Satisfying conclusion.

---

### Unit 60: Credits Sequence

**Prerequisites from SID Symphony:** Credits sequence

**Learning Objectives:**
- Apply SID Symphony credits
- Shooter-appropriate presentation
- Credit roll with ship
- Closure

**Concepts Introduced:**
- Scrolling credits
- Ship sprite in credits
- Attribution

**Code Written:**
```
- Scrolling credits (from SID Symphony)
- Ship flies during credits
- Learner's name in credits
- Return to title after
```

**What the Learner Sees:**
Professional credits sequence. Ship animation adds personality. Learner's name in their game.

**Reference to SID Symphony:**
"Same credits system from Unit 61. Personalised for Starfield."

---

### Unit 61: Difficulty Modes

**Learning Objectives:**
- Implement distinct difficulty modes
- Easy/Normal/Hard/Insane
- Balance each mode
- Accessibility

**Concepts Introduced:**
- Difficulty parameters table
- Enemy speed per difficulty
- Bullet speed per difficulty
- Lives per difficulty

**Code Written:**
```
- Difficulty selection on title
- Easy: slow enemies, many lives, wide bullets
- Normal: balanced
- Hard: fast enemies, few lives
- Insane: unlockable, brutal
```

**What the Learner Sees:**
Game accessible at multiple skill levels. Easy is winnable. Insane is a challenge for experts.

---

### Unit 62: Bug Hunt

**Prerequisites from SID Symphony:** Bug hunt methodology

**Learning Objectives:**
- Apply SID Symphony bug hunt
- Systematic testing
- Edge cases
- Quality assurance

**Concepts Introduced:**
- Applied methodology
- Shooter-specific edge cases
- Collision edge cases
- Multiplexer edge cases

**Code Written:**
```
- Systematic test of all stages
- Test all enemy types
- Test multiplexer limits
- Fix issues found
```

**What the Learner Sees:**
Rock solid game. No crashes. No exploits. Professional quality.

**Reference to SID Symphony:**
"Same bug hunt methodology from Unit 62. Applied to shooter."

---

### Unit 63: Final Playtest

**Prerequisites from SID Symphony:** Final playtest

**Learning Objectives:**
- Apply SID Symphony final playtest
- Fresh eyes if possible
- Final tuning
- Release candidate

**Concepts Introduced:**
- Applied methodology
- Final balance
- Sign-off

**Code Written:**
```
- External playtest if possible
- Final difficulty tuning
- Any last polish
- Declare release candidate
```

**What the Learner Sees:**
Final, polished game. Ready for distribution.

**Reference to SID Symphony:**
"Same final playtest process from Unit 63."

---

### Unit 64: Packaging and Distribution

**Prerequisites from SID Symphony:** Packaging

**Learning Objectives:**
- Apply SID Symphony packaging
- Create distribution package
- Documentation
- Release

**Concepts Introduced:**
- Applied methodology
- Shooter-specific docs
- Distribution

**Code Written:**
```
- Create D64/TAP images
- Write instruction card
- Control reference
- Final archive
```

**What the Learner Sees:**
Complete distribution package. Documentation. Ready to share.

**Phase 4 Checkpoint:**
Advanced shooter with sprite multiplexing, two-player modes, optimised code, professional packaging. Skills built significantly on SID Symphony foundation.

---

## Skills Progression Summary

### From SID Symphony (Applied)
- Program structure, game loop, raster sync
- Screen memory, custom characters
- Score, lives, state machines
- Title screens, menus, high scores
- SID sound effects and music
- Polish methodology
- Optimisation and packaging

### New in Starfield
- Hardware sprites (complete mastery)
- Sprite collision detection
- Joystick input
- Object pools for bullets/enemies
- Enemy AI and patterns
- Boss battles
- Sprite animation
- Sprite multiplexing (deep)
- Parallax scrolling backgrounds
- Two-player modes

### Prepared for Game 3
- Custom character mastery (used in starfield)
- Complex object management
- AI patterns
- Multi-sprite entities (bosses)
- Performance under load
- Multiplexing concepts

---

## Comparison: Isolated 16-Unit Starfield vs Connected 64-Unit Starfield

| Aspect | 16-Unit (Isolated) | 64-Unit (Connected) |
|--------|-------------------|---------------------|
| Enemy types | 1 | 4+ with distinct AI |
| Bosses | 0 | 2+ with patterns |
| Power-ups | 0 | 3+ with strategy |
| Stages | Endless waves | 8 structured stages |
| Background | Static | 3-layer parallax |
| Sprites on screen | 8 max | 16+ via multiplexing |
| Sound | Basic beeps | Full soundtrack |
| Two-player | No | Alternating + co-op |
| Build time | 16-32 hours | 64-128 hours |
| Curriculum connection | Standalone | Deep SID Symphony integration |
| Skills transferred | Few | Many |
| Commercial viable | No | Yes |

---

## Version History

- **1.0 (2025-01-07):** Initial 64-unit outline with SID Symphony integration
