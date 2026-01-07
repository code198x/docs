# Platform Panic: 64-Unit Outline

**Game:** C64 Game 4: Platform Panic
**Units:** 64
**Prerequisites:** SID Symphony, Starfield, Maze Raider
**Concept:** Single-screen platformer. Jump between platforms, avoid hazards, collect items, reach the exit. Bubble Bobble meets Manic Miner.

**Commercial Quality Target:** A game comparable to Bubble Bobble, Manic Miner, or Jet Set Willy. Multiple single-screen levels, precise platforming, hazard timing, collectibles. Something that would have competed on shop shelves in 1984-87.

---

## Skill Progression

### Skills Applied from Previous Games

| Skill | Origin | Application in Platform Panic |
|-------|--------|------------------------------|
| Program structure | SID Symphony | Assumed |
| Screen memory | SID Symphony, Maze Raider | Level display |
| Custom character sets | SID Symphony, **Maze Raider (deep)** | Platform tiles, hazards |
| Game loop, raster sync | All previous | Applied |
| Sprite handling | **Starfield (deep)** | Player and enemy sprites |
| Sprite animation | Starfield, Maze Raider | **Deep expansion** - movement states |
| Score display | SID Symphony | Applied |
| Lives system | All previous | Applied |
| Tile-based maps | **Maze Raider** | Level layouts |
| Tile collision | **Maze Raider** | **Adapted** for platforming |
| Enemy AI | Starfield, Maze Raider | Patrol patterns |
| State machines | All previous | **Deep expansion** - player states |
| SID sound/music | All previous | Applied |
| Menus, title, high scores | All previous | Applied |
| Polish methodology | All previous | Applied |

### New Skills Introduced

| New Skill | Description |
|-----------|-------------|
| Gravity simulation | Downward acceleration |
| Jump physics | Initial velocity, arc, variable height |
| Platform collision | Landing on platforms, head bumps |
| One-way platforms | Pass through from below |
| Character states | Standing, running, jumping, falling |
| State-based animation | Animation tied to character state |
| Hazard timing | Timed obstacles, patterns |
| Conveyor belts | Moving platforms |
| Ladders | Vertical climbing |
| Crumbling platforms | Time-limited supports |
| Level-based design | Single-screen arena design |
| Exit conditions | Collect all items, reach exit |
| Level select (earned) | Non-linear progression |
| Pixel-perfect platforming | Precise collision requirements |

---

## The Finished Game

### Core Gameplay
- Player navigates single-screen levels
- Jump between platforms
- Collect all gems/items to unlock exit
- Avoid hazards and enemies
- Reach exit door to complete level
- Limited lives, continues

### Player Abilities
- Walk left/right
- Jump (variable height based on button hold)
- Climb ladders
- Duck (optional, for low passages)

### Level Elements
- Solid platforms (stand on, block from sides)
- One-way platforms (pass through from below)
- Ladders (vertical movement)
- Conveyor belts (push player)
- Crumbling platforms (fall after stepped on)
- Springs/bounce pads (high jump)
- Locked doors (require key)
- Exit door (level completion)

### Hazards
- Spikes (instant death)
- Patrolling enemies
- Timed flames
- Falling objects
- Crushing platforms
- Water/pits (death)

### Collectibles
- Gems (required for exit)
- Keys (unlock doors)
- Extra life
- Bonus points
- Time bonus (speed completion)

### Structure
- 32 single-screen levels
- 4 worlds of 8 levels each
- World themes (cave, castle, factory, sky)
- Boss/challenge level each world
- Password/continue system

---

## Phase 1: Foundation (Units 1-16)

*Goal: Core platforming. Player moves, jumps, lands on platforms. Basic gravity works. One simple level playable.*

---

### Unit 1: Platform Tile Set

**Prerequisites:** Custom characters (Maze Raider deep mastery)

**Learning Objectives:**
- Design platform-appropriate tiles
- Solid blocks vs background
- Visual platform language
- Tileset planning

**Concepts Introduced:**
- Platform tile types
- Visual collision hints
- Tileset for platformer
- Art direction

**Code Written:**
```
- Platform tiles (solid block, variations)
- Background tiles
- Hazard tiles (spikes)
- Ladder tiles
- Exit door tiles
```

**What the Learner Sees:**
Complete tileset for platforming. Visual language established.

**Reference to Maze Raider:**
"Tileset design from Unit 1. Different aesthetic - platforms instead of maze walls. Same technique, different application."

---

### Unit 2: Level Data Format

**Prerequisites:** Tile maps (Maze Raider 2)

**Learning Objectives:**
- Single-screen level format
- Tile type data
- Player start position
- Exit position

**Concepts Introduced:**
- Level as screen-sized data
- Collision tile flags
- Spawn points
- Level metadata

**Code Written:**
```
- Level data array (40x24 tiles)
- Tile type constants
- Player start X,Y
- Exit position
- Gem count for level
```

**What the Learner Sees:**
Level data structure defined. First level layout ready.

**Reference to Maze Raider:**
"Same concept as maze data from Unit 2. Different content, same structure."

---

### Unit 3: Level Rendering

**Prerequisites:** Tile rendering (Maze Raider 3)

**Learning Objectives:**
- Render level from data
- Display platforms and hazards
- Background elements
- Visual clarity

**Concepts Introduced:**
- Platform rendering
- Layered display
- Applied rendering

**Code Written:**
```
- render_level: draw all tiles
- Tile type to character mapping
- Colour per tile type
- HUD area reserved
```

**What the Learner Sees:**
Platform level displayed. Platforms, hazards, decorations visible. Looks like a platformer.

**Reference to Maze Raider:**
"Level rendering from Unit 3. Applied directly to platform tileset."

---

### Unit 4: Player Sprite

**Prerequisites:** Sprites (Starfield, Maze Raider)

**Learning Objectives:**
- Platformer player design
- Standing sprite
- Position over tiles
- Sprite-tile relationship

**Concepts Introduced:**
- Platformer character design
- Feet position (collision point)
- Character proportions
- Standing frame

**Code Written:**
```
- Player sprite design
- Standing frame
- Position at level start
- Colour scheme
```

**What the Learner Sees:**
Player character on the platform level. Standing sprite visible. Ready to move.

---

### Unit 5: Horizontal Movement

**Prerequisites:** Sprite movement (all previous)

**Learning Objectives:**
- Left/right walking
- Movement speed
- Screen boundaries
- Tile boundary awareness

**Concepts Introduced:**
- Horizontal velocity
- Speed constant
- Boundary clamping
- Smooth movement

**Code Written:**
```
- Read joystick left/right
- Apply horizontal velocity
- Clamp to screen edges
- Update sprite position
```

**What the Learner Sees:**
Player walks left and right. Smooth movement. Stops at edges.

---

### Unit 6: Gravity

**Learning Objectives:**
- Implement downward pull
- Velocity accumulation
- Terminal velocity
- Falling state

**Concepts Introduced:**
- Gravity as acceleration
- Vertical velocity variable
- Terminal velocity cap
- Falling flag

**Code Written:**
```
- gravity_constant = acceleration per frame
- velocity_y: vertical speed
- Apply gravity each frame
- Cap at terminal velocity
- Player falls without support
```

**What the Learner Sees:**
Player falls when in the air! Gravity pulls down. Falls off platforms into void. Core physics working.

---

### Unit 7: Platform Collision - Landing

**Prerequisites:** Tile collision (Maze Raider 6)

**Learning Objectives:**
- Detect platform below player
- Stop falling on contact
- Ground state
- Standing on platforms

**Concepts Introduced:**
- Foot position checking
- Collision from above
- Grounded flag
- Landing snap

**Code Written:**
```
- Check tile below player feet
- If solid and moving down: land
- Set grounded = true
- Stop vertical velocity
- Snap to platform top
```

**What the Learner Sees:**
Player lands on platforms! Falls and stops when hitting platform. Can stand on different heights.

**Reference to Maze Raider:**
"Tile collision from Unit 6. Adapted - instead of blocking movement, we detect landing and snap position."

---

### Unit 8: Platform Collision - Walls

**Learning Objectives:**
- Detect walls beside player
- Block horizontal movement
- Side collision
- Wall sliding

**Concepts Introduced:**
- Side collision checks
- Collision at multiple heights
- Movement blocking
- Wall detection

**Code Written:**
```
- Check tiles to left/right of player
- If solid: block horizontal movement
- Check at head and feet height
- Prevent walking through walls
```

**What the Learner Sees:**
Player can't walk through walls. Blocked by solid platforms on sides. Proper collision.

---

### Unit 9: Platform Collision - Ceiling

**Learning Objectives:**
- Detect ceiling above player
- Stop upward movement
- Head bump
- Ceiling collision

**Concepts Introduced:**
- Ceiling detection
- Upward movement blocking
- Head collision point
- Vertical blocking

**Code Written:**
```
- When moving up: check tile above head
- If solid: stop upward movement
- Set velocity_y to 0 or small downward
- "Bump" sensation
```

**What the Learner Sees:**
Player can't pass through ceilings. Head bumps stop upward movement. Full tile collision.

---

### Unit 10: Jumping - Basic

**Learning Objectives:**
- Jump on button press
- Initial upward velocity
- Jump arc
- Jump only when grounded

**Concepts Introduced:**
- Jump impulse
- Initial velocity
- Jump arc (gravity shapes it)
- Grounded check for jump

**Code Written:**
```
- If fire pressed and grounded:
- Set velocity_y = jump_strength (negative = up)
- Set grounded = false
- Gravity creates arc naturally
```

**What the Learner Sees:**
Player jumps! Press button, character arcs upward and falls back down. Core platforming works.

---

### Unit 11: Variable Jump Height

**Learning Objectives:**
- Hold button for higher jump
- Release for lower jump
- Jump control feel
- Precision jumping

**Concepts Introduced:**
- Jump cut-off
- Button hold detection
- Variable height control
- Nuanced jump feel

**Code Written:**
```
- Track jump button state
- If released early and still rising:
- Cut vertical velocity (divide by 2 or set to 0)
- Results in shorter jump
```

**What the Learner Sees:**
Tap for short hop, hold for full jump. Player has fine control over jump height. Precision platforming enabled.

---

### Unit 12: Walking Animation

**Prerequisites:** Animation (Starfield 35, Maze Raider 35)

**Learning Objectives:**
- Walking animation frames
- Direction facing
- Animation speed
- State-based animation

**Concepts Introduced:**
- Walk cycle frames
- Animation state machine
- Facing direction
- Frame timing

**Code Written:**
```
- Walk animation: 4 frames
- Cycle through when moving
- Flip for left/right facing
- Stand frame when still
```

**What the Learner Sees:**
Player animates while walking. Feet move. Character faces movement direction. Polished movement.

**Reference to Previous:**
"Animation from Starfield Unit 35 and Maze Raider Unit 35. Now tied to movement state."

---

### Unit 13: Jump/Fall Animation

**Learning Objectives:**
- Jumping animation frame
- Falling animation frame
- State transitions
- Visual feedback

**Concepts Introduced:**
- Air state animations
- Rising vs falling frames
- State-based sprite selection
- Animation state machine

**Code Written:**
```
- Jump frame (ascending)
- Fall frame (descending)
- Select based on velocity_y
- Smooth transitions
```

**What the Learner Sees:**
Player looks different when jumping vs falling. Visual state matches physics state. Reads clearly.

---

### Unit 14: Collectibles

**Prerequisites:** Collection (Maze Raider 9)

**Learning Objectives:**
- Place gems in level
- Collection detection
- Score and counter
- Level completion condition

**Concepts Introduced:**
- Collectible tiles
- Pickup collision
- Gem counter
- Collection requirement

**Code Written:**
```
- Gem tile type
- Detect player overlap with gem
- Remove gem, add to counter
- gems_remaining for level
```

**What the Learner Sees:**
Gems in level. Collect them! Counter decreases. Score increases. Goal is clear.

**Reference to Maze Raider:**
"Same pellet collection logic from Unit 9. Applied to gems in platformer."

---

### Unit 15: Level Complete

**Prerequisites:** Level progression (Maze Raider 14)

**Learning Objectives:**
- Exit door functionality
- All gems required
- Level complete sequence
- Next level loading

**Concepts Introduced:**
- Exit activation
- Completion requirements
- Level transition
- Progress tracking

**Code Written:**
```
- Exit door tile
- If player at exit and gems_remaining == 0:
- Level complete!
- Play jingle, advance level
- Load next level
```

**What the Learner Sees:**
Exit door opens when all gems collected. Walk to exit = level complete! Next level loads.

---

### Unit 16: Phase 1 Complete - Core Playtest

**Learning Objectives:**
- Playtest platforming
- Jump feel tuning
- Collision verification
- Foundation sign-off

**Concepts Introduced:**
- Platformer feel tuning
- Jump curve adjustment
- Applied playtesting

**Code Written:**
```
- Playtest core movement
- Tune jump height, gravity
- Verify all collisions
- Document Phase 2 needs
```

**What the Learner Sees:**
Core platformer complete. Movement feels good. Jumping is precise. Ready for content.

**Phase 1 Checkpoint:**
Core platforming works. Walk, jump, land, collect, exit. One level playable. Jump feel is good. Foundation solid.

---

## Phase 2: Expansion (Units 17-32)

*Goal: Full level variety. Hazards, enemies, special platforms, multiple levels. Complete platformer content.*

---

### Unit 17: Spikes Hazard

**Learning Objectives:**
- Instant death hazard
- Hazard collision
- Death handling
- Visual clarity

**Concepts Introduced:**
- Hazard tiles
- Death on contact
- Applied death system
- Visual danger

**Code Written:**
```
- Spike tile type
- If player contacts spikes: death
- Apply death from previous games
- Respawn at level start
```

**What the Learner Sees:**
Spikes kill player! Clear visual danger. Death and respawn work. Stakes established.

**Reference to Previous:**
"Death handling from Starfield and Maze Raider. Applied to spike contact."

---

### Unit 18: Patrolling Enemy

**Prerequisites:** Enemy AI (Starfield 7, Maze Raider 10-13)

**Learning Objectives:**
- Basic enemy sprite
- Patrol movement
- Edge detection
- Enemy collision

**Concepts Introduced:**
- Platform-aware patrol
- Edge turnaround
- Enemy as hazard
- Applied enemy AI

**Code Written:**
```
- Enemy sprite design
- Walk until edge or wall
- Turn around and continue
- Kill player on contact
```

**What the Learner Sees:**
Enemy patrols platform. Turns at edges. Touching it = death. Avoidance gameplay.

**Reference to Previous:**
"Enemy AI from Starfield and Maze Raider. Adapted for platform patrol."

---

### Unit 19: Multiple Enemies

**Learning Objectives:**
- Enemy pool management
- Multiple enemies per level
- Level enemy data
- Performance management

**Concepts Introduced:**
- Enemy spawn from level data
- Multiple enemy handling
- Applied object pools

**Code Written:**
```
- Enemy array (4-6 enemies)
- Spawn from level data
- Update all enemies
- Individual behaviour
```

**What the Learner Sees:**
Multiple enemies per level. Different platforms, different timing. Increased challenge.

---

### Unit 20: One-Way Platforms

**Learning Objectives:**
- Platforms passable from below
- Land from above only
- Platform type flag
- Expanded collision

**Concepts Introduced:**
- One-way collision
- Direction-based collision
- Platform types
- Pass-through logic

**Code Written:**
```
- ONE_WAY platform type
- Only collide when falling
- Pass through when jumping
- Land when descending
```

**What the Learner Sees:**
Some platforms can be jumped through. Land on them from above. Opens level design options.

---

### Unit 21: Ladders

**Learning Objectives:**
- Vertical climbing
- Ladder detection
- Climb controls
- Ladder-platform interaction

**Concepts Introduced:**
- Ladder tiles
- Climb state
- Up/down movement on ladder
- Gravity suspension

**Code Written:**
```
- Ladder tile type
- When overlapping ladder: can climb
- Up/down moves on ladder
- Gravity disabled while climbing
- Jump off ladder
```

**What the Learner Sees:**
Ladders allow vertical movement. Climb up and down. Jump off to platform. Classic mechanic.

---

### Unit 22: Conveyor Belts

**Learning Objectives:**
- Moving platforms concept
- Push player while standing
- Conveyor direction
- Timing challenges

**Concepts Introduced:**
- Conveyor tile type
- Velocity modification
- Direction from tile data
- Moving hazard creation

**Code Written:**
```
- Conveyor tile type (left/right)
- When standing on: add horizontal velocity
- Player pushed in direction
- Can walk against (slower)
```

**What the Learner Sees:**
Conveyor belts push player. Walk against to slow down. Creates timing challenges.

---

### Unit 23: Timed Hazards

**Learning Objectives:**
- Hazards that toggle
- Timing patterns
- Safe windows
- Pattern memorisation

**Concepts Introduced:**
- Hazard timers
- On/off states
- Timing patterns
- Pattern gameplay

**Code Written:**
```
- Flame hazard with timer
- On for N frames, off for N frames
- Visual state matches danger
- Safe to pass when off
```

**What the Learner Sees:**
Flames turn on and off. Wait for safe window. Timing-based challenge.

---

### Unit 24: Crumbling Platforms

**Learning Objectives:**
- Time-limited platforms
- Crumble after stepped on
- Visual warning
- Respawn timing

**Concepts Introduced:**
- Platform state (solid → crumbling → gone)
- Crumble timer
- Visual feedback
- Platform respawn

**Code Written:**
```
- Crumbling platform type
- When stepped on: start timer
- Visual shake/flash
- After timer: platform falls away
- Respawn after longer timer
```

**What the Learner Sees:**
Some platforms crumble! Step on and they shake, then fall. Must move quickly.

---

### Unit 25: Bounce Pads

**Learning Objectives:**
- High-jump platforms
- Bounce physics
- Super jump
- Level design tool

**Concepts Introduced:**
- Bounce pad tile
- Enhanced jump velocity
- Automatic bounce
- Reaching high areas

**Code Written:**
```
- Bounce pad tile type
- Landing on: apply super jump
- Higher than normal jump
- Visual/audio feedback
```

**What the Learner Sees:**
Bounce pads launch player high! Access otherwise unreachable platforms.

---

### Unit 26: Keys and Locked Doors

**Learning Objectives:**
- Key collectibles
- Locked door blocking
- Key-door matching
- Level puzzle element

**Concepts Introduced:**
- Key inventory
- Locked door state
- Key consumption
- Puzzle element

**Code Written:**
```
- Key collectible (coloured)
- Locked door blocks path
- Collect key → can open door
- Door opens permanently
```

**What the Learner Sees:**
Some doors locked. Find key to open. Adds puzzle element to platforming.

---

### Unit 27: Level Design - World 1

**Learning Objectives:**
- Design first world (8 levels)
- Difficulty progression
- Mechanic introduction
- Theme cohesion

**Concepts Introduced:**
- World structure
- Level difficulty curve
- Mechanic teaching levels
- Applied level design

**Code Written:**
```
- Levels 1-8 (World 1: Caves)
- Introduce mechanics gradually
- Level 1: basic platforms
- Level 8: world 1 challenge
```

**What the Learner Sees:**
First 8 levels playable. Cave theme. Teaches mechanics. Builds difficulty.

---

### Unit 28: Level Design - World 2

**Learning Objectives:**
- Design second world
- New visual theme
- Harder variations
- Mechanic combinations

**Concepts Introduced:**
- World themes
- Visual variation
- Applied design

**Code Written:**
```
- Levels 9-16 (World 2: Castle)
- Castle tileset variant
- Harder combinations
- New hazard arrangements
```

**What the Learner Sees:**
World 2: Castle theme. Harder levels. Same mechanics, new challenges.

---

### Unit 29: Level Design - Worlds 3-4

**Learning Objectives:**
- Complete level set
- Factory and Sky themes
- Expert difficulty
- Full 32 levels

**Concepts Introduced:**
- Full game content
- Expert level design
- Applied design

**Code Written:**
```
- Levels 17-24 (World 3: Factory)
- Levels 25-32 (World 4: Sky)
- Full difficulty curve
- Final challenge level
```

**What the Learner Sees:**
32 complete levels. Four worlds. Full game content.

---

### Unit 30: Password System

**Learning Objectives:**
- Level progress saving
- Password generation
- Password entry
- Continue from level

**Concepts Introduced:**
- Password encoding
- Level encoding
- Password UI
- Progress retention

**Code Written:**
```
- Generate 4-character password per level
- Display on level complete
- Password entry screen
- Decode to level number
```

**What the Learner Sees:**
Passwords shown on level complete. Enter password to continue. Progress saved.

---

### Unit 31: Time Bonus

**Learning Objectives:**
- Level timer
- Speed bonus
- Time pressure
- Optional challenge

**Concepts Introduced:**
- Level time tracking
- Bonus calculation
- Display timer
- Speed running appeal

**Code Written:**
```
- Level timer countdown
- Bonus points for fast completion
- No death on timeout (or optional hard mode)
- Display time
```

**What the Learner Sees:**
Timer counting down. Faster = more bonus points. Speed challenge.

---

### Unit 32: Content Complete Playtest

**Learning Objectives:**
- Play all 32 levels
- Balance difficulty
- Verify all mechanics
- Content sign-off

**Concepts Introduced:**
- Full game testing
- Applied playtesting

**Code Written:**
```
- Playtest all levels
- Adjust difficulty
- Fix issues
- Document polish needs
```

**What the Learner Sees:**
Complete 32-level platformer. All mechanics working. Ready for polish.

**Phase 2 Checkpoint:**
Full platformer content. 32 levels, 4 worlds, all hazards and mechanics. Password system. Content complete.

---

## Phase 3: Polish (Units 33-48)

*Goal: Visual and audio polish. Animations, effects, sound, menus. Commercial quality presentation.*

---

### Unit 33: Title Screen

**Prerequisites:** All previous title screens

**Learning Objectives:**
- Platform game title
- Character showcase
- Menu system
- Applied techniques

**Code Written:**
```
- "PLATFORM PANIC" logo
- Player character animation
- Menu: Start, Password, Options, Scores
- Applied from previous games
```

**What the Learner Sees:**
Professional title screen. Animated character. Clear menu.

---

### Unit 34: Attract Mode

**Prerequisites:** All previous attract modes

**Learning Objectives:**
- Demo level playback
- Mechanic showcase
- Applied attract mode

**Code Written:**
```
- Demo plays level 1
- Shows basic mechanics
- Any key returns to title
```

**What the Learner Sees:**
Game demonstrates itself. Shows platforming. Commercial presentation.

---

### Unit 35: Player Animation Polish

**Learning Objectives:**
- Full animation set
- All states covered
- Smooth transitions
- Character personality

**Code Written:**
```
- Idle animation
- Walk cycle polish
- Jump/fall polish
- Death animation
- Victory pose
```

**What the Learner Sees:**
Fully animated character. Every state has polish. Character has personality.

---

### Unit 36: Enemy Animation Polish

**Learning Objectives:**
- Enemy animations
- Different enemy types
- Visual variety
- Character through motion

**Code Written:**
```
- Enemy walk cycles
- Death/defeat animation
- Type-specific animations
- Polish all enemies
```

**What the Learner Sees:**
All enemies animated. Each type distinct. Polished movement.

---

### Unit 37: Level Transition Effects

**Learning Objectives:**
- Level entry effect
- Level complete effect
- World transition
- Satisfying feedback

**Code Written:**
```
- Fade or wipe on level change
- Level number display
- World title card
- Smooth transitions
```

**What the Learner Sees:**
Professional level transitions. World title cards. Polished flow.

---

### Unit 38: Sound Effects

**Prerequisites:** All previous SID work

**Learning Objectives:**
- Platformer sound design
- Jump, land, collect sounds
- Death, hazard sounds
- Applied sound design

**Code Written:**
```
- Jump sound
- Land sound
- Collect sound
- Death sound
- Door open sound
- Applied from SID Symphony foundation
```

**What the Learner Sees:**
Full sound design. Every action has feedback. Satisfying audio.

---

### Unit 39: Background Music

**Learning Objectives:**
- Platformer music style
- Per-world themes
- Applied composition

**Code Written:**
```
- World 1 theme
- World 2 theme
- Worlds 3-4 themes
- Death jingle, victory jingle
```

**What the Learner Sees:**
Music per world. Distinct themes. Fits platforming pace.

---

### Unit 40: HUD Polish

**Learning Objectives:**
- Score display
- Lives icons
- Time display
- Gem counter

**Code Written:**
```
- Score: top left
- Lives: icons
- Time: countdown
- Gems: X remaining
- World/level: display
```

**What the Learner Sees:**
Clean HUD. All info visible. Doesn't interfere with gameplay.

---

### Unit 41: Death and Respawn Polish

**Learning Objectives:**
- Death animation full
- Respawn effect
- Brief invincibility
- Smooth flow

**Code Written:**
```
- Full death sequence
- Screen effect
- Respawn animation
- Brief flash invincibility
```

**What the Learner Sees:**
Polished death handling. Respawn feels smooth. Clear feedback.

---

### Unit 42: Hazard Visual Polish

**Learning Objectives:**
- Animated hazards
- Visual clarity
- Danger communication
- Polish all hazards

**Code Written:**
```
- Animated spikes (optional)
- Flame animation
- Conveyor animation
- Crumble visual polish
```

**What the Learner Sees:**
All hazards visually polished. Animations add life. Danger clear.

---

### Unit 43: World Complete Screens

**Learning Objectives:**
- World completion reward
- Statistics display
- Progress celebration
- Motivation

**Code Written:**
```
- World complete screen
- Time bonus total
- Progress percentage
- "World 2 Complete!"
```

**What the Learner Sees:**
World completion celebrated. Statistics shown. Motivated to continue.

---

### Unit 44: Game Complete Ending

**Learning Objectives:**
- Ending sequence
- Victory celebration
- Story conclusion
- Credits lead-in

**Code Written:**
```
- Game complete screen
- Victory animation
- "You saved the kingdom!" etc.
- Transition to credits
```

**What the Learner Sees:**
Completing all levels shows ending. Victory! Satisfaction.

---

### Unit 45: High Score and Stats

**Prerequisites:** High scores from all previous

**Learning Objectives:**
- Applied high score
- Level-based stats
- Best times per level
- Applied system

**Code Written:**
```
- High score table
- Best time per level (optional)
- Name entry
- Applied from previous games
```

**What the Learner Sees:**
High score system. Times tracked. Applied system works.

---

### Unit 46: Options Screen

**Prerequisites:** Options from all previous

**Learning Objectives:**
- Starting lives
- Music/SFX toggle
- Starting world
- Applied options

**Code Written:**
```
- Lives: 3, 5, 7
- Music on/off
- Starting world: 1 (or unlocked)
- Applied framework
```

**What the Learner Sees:**
Options screen. Customisation. Applied from previous.

---

### Unit 47: Pause System

**Prerequisites:** Pause from all previous

**Learning Objectives:**
- Mid-level pause
- Resume options
- Applied pause

**Code Written:**
```
- Pause on button
- Resume/restart/quit
- Applied from previous
```

**What the Learner Sees:**
Pause works. Options available. Applied system.

---

### Unit 48: Polish Pass

**Learning Objectives:**
- Final polish playtest
- All states verified
- All levels played
- Release preparation

**Code Written:**
```
- Full playtest
- Fix issues
- Final tuning
- Document remaining work
```

**What the Learner Sees:**
Polished platformer. Everything feels right. Ready for mastery.

**Phase 3 Checkpoint:**
Fully polished platformer. Animations, sound, music, menus complete. Commercial presentation.

---

## Phase 4: Mastery (Units 49-64)

*Goal: Advanced features and final release. Two-player, expert features, optimisation, packaging.*

---

### Unit 49: Code Review and Optimisation

**Prerequisites:** Code review from all previous

**Learning Objectives:**
- Review codebase
- Optimise collision
- Performance verification
- Applied methodology

**Code Written:**
```
- Code review
- Optimise hot paths
- Document architecture
- Applied from previous
```

**What the Learner Sees:**
Smooth performance. Clean code. Professional quality.

---

### Unit 50: Two-Player Mode Design

**Learning Objectives:**
- Two-player platformer options
- Competitive vs cooperative
- Design decisions
- Implementation plan

**Code Written:**
```
- Design document
- Competitive: alternating turns
- Cooperative: same screen
- Implementation plan
```

**What the Learner Sees:**
Design complete for two-player. Ready for implementation.

---

### Unit 51: Two-Player Alternating

**Prerequisites:** Two-player from previous games

**Learning Objectives:**
- Alternating turns
- Separate scores
- Applied two-player

**Code Written:**
```
- Two-player option
- Turns on death or level complete
- Track scores separately
- Applied from previous
```

**What the Learner Sees:**
Two players take turns. Competition. Applied system.

---

### Unit 52: Two-Player Simultaneous (Challenge)

**Learning Objectives:**
- Both players on screen
- Cooperative play
- Sprite management
- Advanced feature

**Code Written:**
```
- Two player sprites
- Independent control
- Cooperative gem collection
- Race to exit (competitive variant)
```

**What the Learner Sees:**
Both players on screen! Chaos and fun. Advanced feature.

---

### Unit 53: Hard Mode

**Learning Objectives:**
- Expert difficulty option
- One-hit death
- No time bonus
- Hardcore challenge

**Code Written:**
```
- Hard mode toggle
- One life, no continues
- Faster hazards
- Expert challenge
```

**What the Learner Sees:**
Hard mode for experts. Real challenge. Bragging rights.

---

### Unit 54: Time Attack Mode

**Learning Objectives:**
- Speed running support
- Best times leaderboard
- Ghost (optional)
- Replay value

**Code Written:**
```
- Time attack option
- Per-level best times
- Display target time
- Speed running support
```

**What the Learner Sees:**
Time attack mode. Compete against best times. Replay value.

---

### Unit 55: Level Select

**Learning Objectives:**
- Unlock-based level select
- Replay any level
- Practice specific levels
- Applied feature

**Code Written:**
```
- Level select screen
- Shows unlocked levels
- Select any cleared level
- Practice or score attack
```

**What the Learner Sees:**
Level select for unlocked levels. Practice or replay. Quality of life.

---

### Unit 56: Statistics

**Prerequisites:** Statistics from previous

**Learning Objectives:**
- Applied statistics
- Platformer-specific stats
- Deaths per level
- Applied system

**Code Written:**
```
- Total gems collected
- Total deaths
- Levels completed
- Play time
```

**What the Learner Sees:**
Statistics tracked. Progress visible. Applied system.

---

### Unit 57: Easter Eggs

**Learning Objectives:**
- Hidden secrets
- Bonus content
- Player rewards
- Applied fun

**Code Written:**
```
- Secret level(s)
- Hidden warp
- Code for extras
- Easter egg rewards
```

**What the Learner Sees:**
Hidden content for explorers. Secrets reward dedication.

---

### Unit 58: Ending Variations

**Learning Objectives:**
- Multiple endings
- Completion-based ending
- 100% ending
- Reward thoroughness

**Code Written:**
```
- Basic ending (complete game)
- Good ending (all gems ever)
- Best ending (hard mode + fast)
- Reward variations
```

**What the Learner Sees:**
Different endings based on performance. Replay incentive.

---

### Unit 59: Bug Hunt

**Prerequisites:** Bug hunt from all previous

**Learning Objectives:**
- Applied bug hunt
- Platformer-specific issues
- Collision edge cases
- Quality assurance

**Code Written:**
```
- Systematic testing
- Collision edge cases
- Level-specific testing
- Fix all issues
```

**What the Learner Sees:**
Bug-free game. All states work. Professional quality.

---

### Unit 60: Final Balance

**Learning Objectives:**
- Final difficulty tuning
- All levels balanced
- All modes tested
- Parameters locked

**Code Written:**
```
- Final adjustments
- All difficulties verified
- All features working
- Sign off
```

**What the Learner Sees:**
Perfectly balanced. Fair challenge throughout.

---

### Unit 61: Credits Sequence

**Prerequisites:** Credits from all previous

**Learning Objectives:**
- Applied credits
- Platformer-themed
- Attribution
- Closure

**Code Written:**
```
- Scrolling credits
- Character animations
- Learner's name
- Applied from previous
```

**What the Learner Sees:**
Professional credits. Satisfying closure.

---

### Unit 62: Documentation

**Learning Objectives:**
- Control reference
- Mechanic explanations
- Level hints (optional)
- Complete documentation

**Code Written:**
```
- Controls
- Mechanic guide
- Tips
- Complete docs
```

**What the Learner Sees:**
Documentation for players. Everything explained.

---

### Unit 63: Final Playtest

**Prerequisites:** Final playtest from all previous

**Learning Objectives:**
- Fresh eyes playtest
- Final fixes
- Release candidate
- Sign off

**Code Written:**
```
- External playtest
- Final fixes
- RC declaration
```

**What the Learner Sees:**
Final version ready. Release candidate.

---

### Unit 64: Packaging and Distribution

**Prerequisites:** Packaging from all previous

**Learning Objectives:**
- Applied packaging
- Distribution files
- Final archive
- Release

**Code Written:**
```
- D64/TAP images
- Documentation included
- Source archived
- Complete
```

**What the Learner Sees:**
Fourth commercial-quality game complete. Distribution ready.

**Phase 4 Checkpoint:**
Complete platformer with advanced features. Two-player, time attack, hard mode. Professional quality, fully packaged.

---

## Skills Progression Summary

### From Previous Games (Applied)
- All fundamentals
- Sprite and tile graphics
- Sound and music
- Menus, polish, packaging
- Enemy AI concepts
- Object management

### New in Platform Panic
- Gravity simulation
- Jump physics with variable height
- Platform collision (landing, walls, ceiling)
- One-way platforms
- Character state machine (standing, running, jumping, falling)
- Ladders and climbing
- Conveyor belts
- Crumbling platforms
- Bounce pads
- Keys and locked doors
- Level-based progression with passwords
- Time-based scoring

### Prepared for Game 5 (Brick Basher)
- Physics simulation experience (gravity → ball physics)
- Precise collision detection
- Tile-based playfields
- State management
- Pattern-based gameplay readiness

---

## Version History

- **1.0 (2025-01-07):** Initial 64-unit outline with full curriculum integration
