# Invader Wave: 64-Unit Outline

**Game:** 6 of 16
**Platform:** Commodore 64
**Units:** 64
**Concept:** Space Invaders style fixed shooter. Enemy formation descends, player defends Earth.

---

## Skills Applied from Previous Games

| Skill | Learned In | Application in Invader Wave |
|-------|-----------|---------------------------|
| SID fundamentals | SID Symphony | Iconic descending bass, explosion sounds |
| ADSR envelopes | SID Symphony | Varied alien and weapon sounds |
| Game loop structure | SID Symphony | Main game timing |
| Hardware sprites | Starfield | Player ship, bullets |
| Joystick input | Starfield | Player movement and firing |
| Sprite collision | Starfield | Bullet-enemy collision |
| Score display | Starfield | Score, lives, high score |
| Object management | Starfield | Multiple bullets |
| Custom character sets | Maze Raider | Alien graphics, shields |
| Tile-based maps | Maze Raider | Shield structure |
| Tile collision | Maze Raider | Bullet-shield collision |
| Animation frames | Platform Panic | Alien animation cycles |
| Grid destruction | Brick Basher | Destructible shields |
| Speed ramping | Brick Basher | Accelerating difficulty |
| High score persistence | Brick Basher | Save/load high scores |
| Attract mode | Brick Basher | Demo mode on title |

## New Skills Introduced

| Skill | Units | Description |
|-------|-------|-------------|
| Formation movement | 5-8 | Coordinated group movement patterns |
| Edge-triggered direction | 9-12 | Formation reverses at screen edges |
| Step-based movement | 13-16 | Move one column, then next row, etc. |
| Enemy bullet patterns | 21-24 | Multiple enemy fire behaviours |
| Column-based targeting | 25-28 | Enemies above player more likely to fire |
| Accelerating tempo | 29-32 | Fewer enemies = faster movement |
| Wave progression | 33-36 | Waves start lower each time |
| Mystery ship mechanics | 37-40 | Timed bonus enemy with scoring rules |
| Shield erosion patterns | 17-20 | Directional damage on shields |

---

## Phase 1: Foundation (Units 1-16)
*Core mechanics: player, enemies, shooting, and a playable game.*

### Unit 1: The Battlefield

**Learning Objectives:**
- Understand Space Invaders' fixed-shooter format
- Set up screen layout
- Position fixed elements

**Concepts Introduced:**
- Space Invaders as genre (Taito 1978, cultural impact)
- Fixed shooter vs. scrolling shooter
- Screen regions (score, shields, play area, player zone)

**Code Written:**
- Initialise screen mode and colours
- Draw score area at top
- Clear play area
- Reserve player row at bottom
- Draw ground line

**What the Learner Sees:**
Empty battlefield - score display ready, ground line drawn, space for shields and enemies.

---

### Unit 2: The Player Ship

**Learning Objectives:**
- Create player ship sprite
- Position at bottom of screen
- Constrain to horizontal movement

**Concepts Introduced:**
- Player ship design (tank/cannon style)
- Fixed Y position
- X movement constraints
- Player sprite colour

**Code Written:**
- Define player ship sprite data
- Enable sprite 0 for player
- Set fixed Y position
- Set initial X position (centre)

**What the Learner Sees:**
Player ship sitting at bottom of screen, ready for battle.

**Reference to Starfield:**
"Player ship setup is familiar from Starfield - same sprite enabling, just positioned at screen bottom instead of left."

---

### Unit 3: Player Movement

**Learning Objectives:**
- Read joystick for left/right
- Implement smooth movement
- Handle screen boundaries

**Concepts Introduced:**
- Horizontal-only movement
- Movement speed (deliberate, not fast)
- Boundary clamping
- Position variable vs. sprite position

**Code Written:**
- Read joystick left/right
- Move player position
- Clamp to screen boundaries
- Update sprite X position

**What the Learner Sees:**
Ship moves smoothly left and right with joystick input, stopping at screen edges.

---

### Unit 4: Player Shooting

**Learning Objectives:**
- Fire bullet on button press
- Single bullet limitation
- Bullet movement upward

**Concepts Introduced:**
- Classic single-bullet limitation
- Bullet state (inactive/active)
- Bullet velocity (upward only)
- Bullet sprite

**Code Written:**
- Define bullet sprite
- Fire bullet on fire button
- Only one bullet at a time
- Move bullet upward each frame
- Deactivate at top of screen

**What the Learner Sees:**
Press fire - single shot races upward! Can't fire again until it leaves screen.

**Reference to Starfield:**
"Starfield had unlimited bullets. Space Invaders' single-bullet rule is a design choice forcing accuracy over spam."

---

### Unit 5: Enemy Formation - Static

**Learning Objectives:**
- Create enemy grid layout
- Position 55 enemies (11×5)
- Understand formation structure

**Concepts Introduced:**
- Formation as 2D array
- Screen position calculation
- Character-based enemy display
- Enemy presence flags

**Code Written:**
- Define enemy grid (11 columns × 5 rows)
- Set all enemies to active
- Calculate screen positions
- Draw enemies using characters

**What the Learner Sees:**
Full formation of 55 aliens arranged in neat rows!

**Reference to Maze Raider:**
"Enemy grid uses same tile map concepts as Maze Raider's maze - positions calculated from grid coordinates."

---

### Unit 6: Enemy Graphics

**Learning Objectives:**
- Create three enemy types
- Design animation frames
- Apply row-based enemy types

**Concepts Introduced:**
- Three alien types (top row, middle rows, bottom rows)
- Two animation frames per type
- Character set for aliens
- Point values per type

**Code Written:**
- Create character data for 6 alien characters (3 types × 2 frames)
- Map enemy type to row
- Draw with correct character
- Assign point values

**What the Learner Sees:**
Three distinct alien types in formation - octopus at top (30 pts), crab middle (20 pts), squid bottom (10 pts).

---

### Unit 7: Enemy Animation

**Learning Objectives:**
- Animate enemies between frames
- Sync animation with movement
- Create classic "step" animation

**Concepts Introduced:**
- Animation frame toggle
- Animation tied to movement
- Frame counter per step
- Visual rhythm

**Code Written:**
- Track animation frame state
- Toggle frame on movement
- Redraw enemies with new frame
- Time animation to movement steps

**What the Learner Sees:**
Aliens animate as they step - arms/legs move with each march step!

---

### Unit 8: Formation Movement - Horizontal

**Learning Objectives:**
- Move entire formation together
- Understand step-based movement
- Calculate new positions

**Concepts Introduced:**
- Formation offset (X and Y)
- Step-based movement (one column at a time)
- Movement direction flag
- Position = base + offset

**Code Written:**
- Add formation X offset
- Step offset each frame
- Apply offset when drawing
- Track movement direction

**What the Learner Sees:**
Entire alien formation marches sideways in unison!

---

### Unit 9: Formation Edge Detection

**Learning Objectives:**
- Detect when formation reaches edge
- Check rightmost/leftmost alive enemy
- Trigger direction change

**Concepts Introduced:**
- Live enemy boundary calculation
- Only count active enemies
- Edge collision triggers reversal
- Adaptive boundary (shrinks as enemies die)

**Code Written:**
- Scan for leftmost alive column
- Scan for rightmost alive column
- Check formation boundaries
- Set reversal flag at edge

**What the Learner Sees:**
Formation reaches edge - reverses direction! As enemies die, boundary adapts.

---

### Unit 10: Formation Descent

**Learning Objectives:**
- Drop formation on edge hit
- Approach player over time
- Create tension through descent

**Concepts Introduced:**
- Descent on direction reversal
- Formation Y offset
- Descent amount (one row height)
- Game over condition (formation reaches bottom)

**Code Written:**
- Increment formation Y on reversal
- Move formation down
- Check for game over height
- Increase tension as aliens descend

**What the Learner Sees:**
Formation hits edge - drops down a row! Aliens march closer to Earth!

---

### Unit 11: Bullet-Enemy Collision

**Learning Objectives:**
- Detect bullet hitting enemy
- Convert bullet position to grid
- Mark enemy as destroyed

**Concepts Introduced:**
- Pixel to grid conversion
- Check enemy active status
- Collision area per enemy
- Score enemy on hit

**Code Written:**
- Convert bullet position to grid coordinates
- Check enemy at that position
- Mark enemy as destroyed
- Award points for kill

**What the Learner Sees:**
Bullet hits alien - alien dies! Score increases!

---

### Unit 12: Enemy Destruction Effect

**Learning Objectives:**
- Display explosion on death
- Brief visual feedback
- Remove from formation

**Concepts Introduced:**
- Explosion character/sprite
- Timed display (few frames)
- Clear after explosion
- Death sound effect

**Code Written:**
- Show explosion character
- Timer for explosion display
- Clear explosion when done
- Play death sound

**What the Learner Sees:**
Alien explodes in a burst! Satisfying destruction effect with sound.

**Reference to SID Symphony:**
"Death sound uses short, punchy noise burst - classic arcade explosion effect."

---

### Unit 13: Score System

**Learning Objectives:**
- Track and display score
- Different points per enemy type
- Update score display

**Concepts Introduced:**
- Point values (10, 20, 30)
- Score addition routine
- Display formatting
- High score comparison

**Code Written:**
- Add-to-score routine
- Point lookup by enemy type
- Update score display on screen
- Track high score

**What the Learner Sees:**
Score increases with each kill - different points for different aliens!

---

### Unit 14: Lives System

**Learning Objectives:**
- Track player lives
- Detect player death
- Respawn mechanics

**Concepts Introduced:**
- Lives counter
- Player death detection (by enemy bullet - coming soon)
- Respawn delay
- Game over when lives = 0

**Code Written:**
- Lives counter
- Display lives
- Death handler (placeholder)
- Respawn routine
- Game over check

**What the Learner Sees:**
Lives displayed - ready for when enemies can fight back!

---

### Unit 15: Enemy Shooting - Basic

**Learning Objectives:**
- Enemies fire back
- Random enemy selection
- Enemy bullets fall

**Concepts Introduced:**
- Enemy bullet pool
- Random firing enemy
- Bullet direction (downward)
- Multiple enemy bullets

**Code Written:**
- Enemy bullet array (3 bullets)
- Select random alive enemy
- Spawn bullet at enemy position
- Move bullets downward

**What the Learner Sees:**
Aliens shoot back! Bullets rain down from random enemies.

---

### Unit 16: Player Death and Restart

**Learning Objectives:**
- Detect enemy bullet hitting player
- Handle player death
- Game over and restart flow

**Concepts Introduced:**
- Player-bullet collision
- Death animation
- Lives decrement
- Restart wave on last enemy/game over on no lives

**Code Written:**
- Check bullet-player collision
- Play death animation
- Decrement lives
- Respawn or game over
- Restart game option

**What the Learner Sees:**
Hit by alien bullet - ship explodes! Lose a life, respawn, or game over.

---

## Phase 2: Expansion (Units 17-32)
*Shields, wave progression, mystery ship, difficulty scaling.*

### Unit 17: Shield Structure

**Learning Objectives:**
- Design destructible shields
- Create shield shape
- Position shields on screen

**Concepts Introduced:**
- Shield as character grid (4×3 chars)
- Shield shape (bunker shape)
- Four shields across screen
- Shield colour

**Code Written:**
- Define shield character shapes
- Create shield template
- Position four shields
- Draw shields on screen

**What the Learner Sees:**
Four protective bunkers positioned between player and aliens!

**Reference to Maze Raider:**
"Shields are tile structures like Maze Raider's walls - but these will be destructible like Brick Basher's bricks."

---

### Unit 18: Shield-Bullet Collision (Player)

**Learning Objectives:**
- Detect player bullet hitting shield
- Damage shield on impact
- Stop bullet on shield

**Concepts Introduced:**
- Character-level collision detection
- Shield damage representation
- Bullet absorption
- Damage from below (player side)

**Code Written:**
- Check bullet against shield positions
- Detect non-empty shield character
- Damage that character
- Deactivate bullet

**What the Learner Sees:**
Player bullet hits shield - chips away at it! Strategic cost to hitting own shields.

---

### Unit 19: Shield Damage Patterns

**Learning Objectives:**
- Visual degradation of shields
- Multiple damage states
- Character animation for erosion

**Concepts Introduced:**
- Four damage states per shield character
- Direction-aware damage (hit from below vs. above)
- Character replacement on damage
- Complete destruction after four hits

**Code Written:**
- Create damage state characters (4 levels)
- Track damage per shield char
- Apply appropriate character
- Destroy when fully damaged

**What the Learner Sees:**
Shields erode gradually - crumble bite by bite as they take fire!

---

### Unit 20: Shield-Bullet Collision (Enemy)

**Learning Objectives:**
- Enemy bullets damage shields from above
- Different damage pattern from player
- Shields protect player

**Concepts Introduced:**
- Same collision different direction
- Top-down erosion pattern
- Strategic shield use
- Shields as limited resource

**Code Written:**
- Check enemy bullets against shields
- Damage from above pattern
- Stop enemy bullet on hit
- Same destruction flow

**What the Learner Sees:**
Enemy fire erodes shields from above - shields slowly fail under bombardment!

---

### Unit 21: Enemy Shooting - Column Priority

**Learning Objectives:**
- Bottom enemy in column shoots
- More realistic fire pattern
- Only front-line aliens attack

**Concepts Introduced:**
- Column scanning for bottom alive
- Bottom enemy more likely to fire
- Prevents "shooting through" own formation
- Authentic Space Invaders behaviour

**Code Written:**
- Find bottom alive enemy in column
- Select from front-line only
- Fire from selected enemy
- Handle empty columns

**What the Learner Sees:**
Only front-row aliens in each column shoot - authentic formation behaviour!

---

### Unit 22: Enemy Shooting - Targeting

**Learning Objectives:**
- Enemies above player more likely to fire
- Column-based targeting
- Strategic enemy behaviour

**Concepts Introduced:**
- Player column detection
- Weighted random selection
- Columns above player prioritised
- Difficulty through targeting

**Code Written:**
- Determine player's column
- Weight selection toward that column
- Apply weighted random
- More dangerous positioning

**What the Learner Sees:**
Aliens above you fire more often - don't stay still! Strategic movement matters.

---

### Unit 23: Wave Complete

**Learning Objectives:**
- Detect all enemies destroyed
- Transition to new wave
- Brief celebration

**Concepts Introduced:**
- Enemy count tracking
- Wave complete detection
- Brief pause/fanfare
- Wave reset

**Code Written:**
- Track alive enemy count
- Detect count = 0
- Victory pause
- Reset formation for new wave

**What the Learner Sees:**
Last alien destroyed - wave complete! Brief celebration before next wave begins.

---

### Unit 24: Wave Progression

**Learning Objectives:**
- New waves start lower
- Increase difficulty
- Track wave number

**Concepts Introduced:**
- Wave number tracking
- Starting Y offset increases
- More immediate danger
- Difficulty curve

**Code Written:**
- Wave counter
- Calculate starting Y from wave
- Clamp to reasonable start
- Display wave number

**What the Learner Sees:**
Wave 2 starts lower than Wave 1! Aliens begin closer to Earth each wave.

---

### Unit 25: Speed Ramping - Basic

**Learning Objectives:**
- Fewer enemies = faster movement
- Classic tension building
- Calculate speed from count

**Concepts Introduced:**
- Speed lookup table
- Enemy count triggers
- Last few enemies very fast
- Authentic arcade tension

**Code Written:**
- Create speed table (count → speed)
- Check enemy count after each kill
- Adjust movement speed
- Handle very few enemies

**What the Learner Sees:**
As aliens die, survivors speed up! Last few aliens race across screen!

**Reference to Brick Basher:**
"Speed ramping concept from Brick Basher, but here it's enemy-count-based rather than time-based."

---

### Unit 26: Speed Ramping - Sound

**Learning Objectives:**
- Accelerating "heartbeat" sound
- Audio matches movement speed
- Classic Space Invaders audio

**Concepts Introduced:**
- Four-note descending bass
- Tempo tied to movement speed
- Iconic audio signature
- Audio tension building

**Code Written:**
- Create four-note bass pattern
- Time notes to movement steps
- Accelerate with movement speed
- Loop pattern continuously

**What the Learner Sees:**
Iconic "DUM-DUM-DUM-DUM" speeds up as aliens are destroyed - classic audio tension!

**Reference to SID Symphony:**
"The accelerating bass line is pure SID Symphony work - simple notes, powerful effect."

---

### Unit 27: Mystery Ship Framework

**Learning Objectives:**
- Understand UFO bonus mechanics
- Design mystery ship system
- Timer-based spawning

**Concepts Introduced:**
- Mystery ship (UFO/flying saucer)
- Random spawn timing
- Flies across top of screen
- Bonus points if hit

**Code Written:**
- Mystery ship sprite
- Spawn timer (random interval)
- Active/inactive state
- Position at screen edge

**What the Learner Sees:**
(Framework ready - ship appears in next unit.)

---

### Unit 28: Mystery Ship Movement

**Learning Objectives:**
- Move mystery ship across screen
- Handle direction (left or right)
- Despawn at edge

**Concepts Introduced:**
- Horizontal movement
- Direction variation (sometimes left, sometimes right)
- Speed (faster than formation)
- Edge despawn

**Code Written:**
- Move mystery ship each frame
- Direction random on spawn
- Despawn at opposite edge
- Distinctive sound while flying

**What the Learner Sees:**
UFO flies across top of screen with distinctive sound! A moving bonus target.

---

### Unit 29: Mystery Ship Scoring

**Learning Objectives:**
- Score mystery ship
- Variable point values
- Classic scoring rules

**Concepts Introduced:**
- Score depends on shots fired
- Authentic arcade scoring
- Display score briefly
- High risk/reward target

**Code Written:**
- Track shots fired this life
- Calculate score from shot count
- Display floating score
- Add to total score

**What the Learner Sees:**
Hit the UFO - 50, 100, 150, or even 300 points! Score depends on timing.

---

### Unit 30: Player-Formation Collision

**Learning Objectives:**
- Detect aliens reaching player level
- Instant game over
- Ultimate failure state

**Concepts Introduced:**
- Formation Y threshold
- Collision means invasion complete
- Game over even with lives
- Prevents endless stalemate

**Code Written:**
- Check formation bottom Y
- Compare to player Y threshold
- Trigger invasion game over
- Special game over message

**What the Learner Sees:**
Aliens reach ground level - invasion complete! Game over regardless of lives.

---

### Unit 31: Enemy Bullet Variety

**Learning Objectives:**
- Different bullet types
- Visual and behaviour variation
- Three enemy bullet types

**Concepts Introduced:**
- Plunger bullet (basic)
- Rolling bullet (wiggles)
- Squiggly bullet (advanced enemies)
- Speed variation per type

**Code Written:**
- Three bullet characters
- Movement pattern per type
- Speed per type
- Enemy type determines bullet type

**What the Learner Sees:**
Different aliens fire different bullets - some faster, some with patterns!

---

### Unit 32: Difficulty Balancing

**Learning Objectives:**
- Tune all difficulty parameters
- Balance challenge curve
- Test extensively

**Concepts Introduced:**
- Difficulty parameter tables
- Fire rate by wave
- Speed curve by wave
- Starting height by wave

**Code Written:**
- Consolidate difficulty parameters
- Create per-wave tables
- Test and tune values
- Document settings

**What the Learner Sees:**
(Refined feel - difficulty curve feels fair and escalating.)

---

## Phase 3: Polish (Units 33-48)
*Effects, sound, visual feedback, and "juice".*

### Unit 33: Player Death Animation

**Learning Objectives:**
- Elaborate death sequence
- Visual disintegration
- Emotional impact

**Concepts Introduced:**
- Multi-frame death animation
- Player sprite animation
- Brief invulnerability after respawn
- Sound accompaniment

**Code Written:**
- Create death animation frames
- Play sequence on death
- Add invulnerability timer
- Respawn effect

**What the Learner Sees:**
Ship explodes dramatically - multiple frames of destruction! Brief flash when respawning.

---

### Unit 34: Enemy Death Variety

**Learning Objectives:**
- Different death effects per type
- Visual variation
- Enhanced satisfaction

**Concepts Introduced:**
- Death effect per enemy type
- Colour variation
- Sound pitch variation
- Point display pop-up

**Code Written:**
- Death effect per enemy type
- Vary explosion colours
- Vary sound pitch
- Brief floating point display

**What the Learner Sees:**
Each enemy type dies differently - unique explosions and sounds!

---

### Unit 35: Sound Design - Effects

**Learning Objectives:**
- Complete sound effect set
- Distinctive sounds per event
- Audio identity

**Concepts Introduced:**
- Sound palette design
- Effect prioritisation
- Channel allocation
- Audio consistency

**Code Written:**
- Player fire sound
- Enemy fire sound
- Explosion sounds (varied)
- Shield damage sound
- Mystery ship sounds

**What the Learner Sees:**
Every action has distinctive audio feedback - rich soundscape!

**Reference to SID Symphony:**
"Full SID Symphony expertise applied - three voices carefully managed for complete audio experience."

---

### Unit 36: Music - Title Screen

**Learning Objectives:**
- Create title screen melody
- Space theme music
- Player engagement

**Concepts Introduced:**
- Title music composition
- Space theme appropriate
- Loop point
- Music vs. gameplay

**Code Written:**
- Compose short title melody
- Implement music player
- Loop seamlessly
- Fade out on game start

**What the Learner Sees:**
Evocative space theme plays on title screen - sets the mood!

---

### Unit 37: Wave Start Sequence

**Learning Objectives:**
- Dramatic wave introduction
- Formation appears
- Build anticipation

**Concepts Introduced:**
- Wave introduction sequence
- "GET READY" message
- Brief pause before action
- Formation reveal

**Code Written:**
- "GET READY" display
- Formation draw-in effect
- Countdown timer
- Action begin

**What the Learner Sees:**
"GET READY" appears, formation revealed, brief pause - then battle begins!

---

### Unit 38: Bonus Life Award

**Learning Objectives:**
- Award extra life at score threshold
- Celebrate achievement
- One-time per threshold

**Concepts Introduced:**
- Score milestone checking
- Extra life award
- Celebration effect
- Milestone tracking

**Code Written:**
- Check score against threshold
- Award extra life
- Celebration sound/flash
- Mark threshold reached

**What the Learner Sees:**
Hit 1,000 points - bonus life! Celebration effect marks achievement.

---

### Unit 39: Near-Miss Feedback

**Learning Objectives:**
- Visual feedback for close calls
- Reward risky play
- Enhance tension

**Concepts Introduced:**
- Proximity detection
- Near-miss definition
- Brief visual flash
- Psychological reward

**Code Written:**
- Detect near-miss (bullet passes close)
- Flash screen edge
- Brief audio cue
- Count near-misses (stats)

**What the Learner Sees:**
Enemy bullet whizzes past - screen flashes! Visceral near-miss feedback.

---

### Unit 40: Last Alien Tension

**Learning Objectives:**
- Special treatment for final enemy
- Maximum tension
- Climactic moment

**Concepts Introduced:**
- Single enemy detection
- Extra audio emphasis
- Visual highlight
- Maximum satisfaction on kill

**Code Written:**
- Detect single enemy remaining
- Enhanced audio tempo
- Subtle visual highlight
- Big celebration on final kill

**What the Learner Sees:**
Last alien - tension peaks! Audio racing, all focus on the survivor. Massive satisfaction when destroyed.

---

### Unit 41: Title Screen Polish

**Learning Objectives:**
- Professional title presentation
- Animated elements
- High score display

**Concepts Introduced:**
- Logo animation
- High score table
- Credit attribution
- Press fire prompt

**Code Written:**
- Animated title logo
- High score table display
- Simple animation loop
- Fire to start

**What the Learner Sees:**
Professional title screen with animation, high scores, polished presentation.

---

### Unit 42: High Score Entry

**Learning Objectives:**
- Name entry for high scores
- Three-initial system
- Table management

**Concepts Introduced:**
- Initial entry interface
- Character selection
- Score table insertion
- Persistence ready

**Code Written:**
- Initial entry screen
- Up/down character selection
- Three initial slots
- Insert into table

**What the Learner Sees:**
High score achieved! Enter your initials: A A A → select and save.

---

### Unit 43: High Score Persistence

**Learning Objectives:**
- Save high scores to storage
- Load on game start
- Survive power off

**Concepts Introduced:**
- Save data format
- File operations
- Load at startup
- Error handling

**Code Written:**
- Save routine
- Load routine
- Error handling
- Default scores if no file

**What the Learner Sees:**
High scores saved! Return tomorrow - your scores are remembered.

**Reference to Brick Basher:**
"Same persistence techniques from Brick Basher - standard file operations for high scores."

---

### Unit 44: Game Over Presentation

**Learning Objectives:**
- Polish game over screen
- Statistics display
- Retry prompt

**Concepts Introduced:**
- Final score emphasis
- Statistics (enemies killed, waves cleared)
- High score check
- Play again prompt

**Code Written:**
- Game over display
- Statistics formatting
- High score transition
- Fire to retry

**What the Learner Sees:**
Game over! Final stats displayed, high score entry if earned, press fire to retry.

---

### Unit 45: Attract Mode

**Learning Objectives:**
- Demo mode on title
- Auto-playing game
- Showcase gameplay

**Concepts Introduced:**
- AI player control
- Demo game limitations
- Return to title
- Attract sequence

**Code Written:**
- Simple AI targeting
- Demo game flow
- Timer to return to title
- Interrupt on fire button

**What the Learner Sees:**
Leave title screen - game plays itself! Demonstrates gameplay to attract players.

**Reference to Brick Basher:**
"Same attract mode concept - AI plays to showcase the game."

---

### Unit 46: Two-Player Mode Framework

**Learning Objectives:**
- Alternating two-player mode
- Separate scores
- Turn-based play

**Concepts Introduced:**
- Two-player alternating
- Score per player
- Lives per player
- Player indicator

**Code Written:**
- Player select on title
- Separate score tracking
- Alternate on life loss
- Current player indicator

**What the Learner Sees:**
Press fire for 1P, press again for 2P. Take turns competing for high score!

---

### Unit 47: Two-Player Polish

**Learning Objectives:**
- Smooth player transitions
- Clear player indicator
- Competitive features

**Concepts Introduced:**
- "PLAYER 1" / "PLAYER 2" display
- Transition animation
- Score comparison
- Winner announcement

**Code Written:**
- Player transition display
- Current player highlight
- Score comparison
- Winner display at game over

**What the Learner Sees:**
Clear player transitions, competitive score display, winner announced!

---

### Unit 48: Bonus Wave

**Learning Objectives:**
- Special bonus wave
- Modified rules
- Score opportunity

**Concepts Introduced:**
- Bonus wave flag
- Modified enemy behaviour
- Time limit
- Bonus scoring

**Code Written:**
- Trigger bonus wave (every N waves)
- Modified enemy patterns
- Time limit countdown
- Bonus score calculation

**What the Learner Sees:**
Every 5 waves - bonus wave! All enemies worth double, limited time to score big!

---

## Phase 4: Mastery (Units 49-64)
*Optimization, advanced mechanics, and professional polish.*

### Unit 49: Performance Analysis

**Learning Objectives:**
- Profile game performance
- Identify bottlenecks
- Measure timing

**Concepts Introduced:**
- Raster timing
- Frame budget
- Collision detection cost
- Formation update cost

**Code Written:**
- Add timing display
- Measure major routines
- Identify slow areas
- Document targets

**What the Learner Sees:**
Debug display shows CPU time - learn where optimisation is needed.

---

### Unit 50: Formation Update Optimisation

**Learning Objectives:**
- Optimise formation drawing
- Reduce unnecessary updates
- Improve efficiency

**Concepts Introduced:**
- Dirty flag per enemy
- Only redraw changed
- Batch updates
- Skip empty positions

**Code Written:**
- Track dirty flags
- Selective redraw
- Skip destroyed enemies
- Measure improvement

**What the Learner Sees:**
(Performance improvement - smoother gameplay.)

---

### Unit 51: Collision Optimisation

**Learning Objectives:**
- Optimise collision detection
- Reduce checks
- Early exits

**Concepts Introduced:**
- Bounding box early-out
- Screen region checks
- Skip empty columns
- Exit on first hit

**Code Written:**
- Add bounding checks
- Regional partitioning
- Skip empty areas
- Measure improvement

**What the Learner Sees:**
(Performance improvement - consistent frame rate.)

---

### Unit 52: Enemy Variants

**Learning Objectives:**
- Additional enemy types
- Visual variety
- Behaviour variation

**Concepts Introduced:**
- Five enemy types instead of three
- Tougher top rows
- More point values
- Visual hierarchy

**Code Written:**
- Two additional enemy designs
- Integrate into formation
- Point values per type
- Update animations

**What the Learner Sees:**
Five different alien types in later waves - more variety and challenge!

---

### Unit 53: Mystery Ship Patterns

**Learning Objectives:**
- Multiple UFO types
- Different behaviours
- Strategy variety

**Concepts Introduced:**
- Three UFO variants
- Different speeds
- Different score rules
- Visual distinction

**Code Written:**
- Three UFO designs
- Variant-specific behaviour
- Score calculation per variant
- Random variant on spawn

**What the Learner Sees:**
Different UFOs with different behaviours and point values - each a unique opportunity!

---

### Unit 54: Wave Themes

**Learning Objectives:**
- Visual variation per wave
- Colour schemes
- Fresh presentation

**Concepts Introduced:**
- Per-wave colour palette
- Enemy colour variation
- Background colour changes
- Visual interest over long play

**Code Written:**
- Colour tables per wave group
- Apply colours on wave start
- Cycle through themes
- Maintain readability

**What the Learner Sees:**
Each wave group has different colours - green aliens, purple aliens, etc. Fresh look every few waves!

---

### Unit 55: Raster Effect - Stars

**Learning Objectives:**
- Add starfield background
- Raster-timed effect
- Enhanced atmosphere

**Concepts Introduced:**
- Simple raster effect
- Background stars
- Twinkling effect
- Performance consideration

**Code Written:**
- Raster interrupt setup
- Star character display
- Twinkle animation
- Performance-safe implementation

**What the Learner Sees:**
Twinkling stars in background - space atmosphere enhanced!

**Reference to Starfield:**
"We've come full circle - applying Starfield's star concepts as a background effect here!"

---

### Unit 56: Score Multipliers

**Learning Objectives:**
- Risk/reward scoring
- Kill streaks
- Bonus opportunities

**Concepts Introduced:**
- Rapid-kill streak
- Multiplier display
- Timer for streak
- Reset on miss

**Code Written:**
- Track rapid kills
- Apply multiplier
- Display current multiplier
- Streak timer

**What the Learner Sees:**
Quick successive kills build a multiplier - risk/reward for aggressive play!

---

### Unit 57: Challenge Waves

**Learning Objectives:**
- Special formation patterns
- Unique challenges
- Variety injection

**Concepts Introduced:**
- Challenge wave formations
- Different starting positions
- Speed variations
- Special scoring

**Code Written:**
- Alternative formation layouts
- Challenge wave trigger
- Special rules
- Bonus scoring

**What the Learner Sees:**
Occasional challenge waves with unique formations - diagonal patterns, split formations!

---

### Unit 58: Statistics Tracking

**Learning Objectives:**
- Track player statistics
- Lifetime achievements
- Progress display

**Concepts Introduced:**
- Lifetime stats
- Sessions played
- Total aliens killed
- Best wave reached

**Code Written:**
- Stats data structure
- Increment during play
- Stats display screen
- Persistence

**What the Learner Sees:**
Statistics screen shows lifetime play - total aliens destroyed, waves completed!

---

### Unit 59: Control Options

**Learning Objectives:**
- Configure controls
- Sensitivity settings
- Accessibility

**Concepts Introduced:**
- Options menu
- Movement speed setting
- Autofire toggle option
- Save preferences

**Code Written:**
- Options screen
- Setting adjustments
- Apply settings
- Save/load preferences

**What the Learner Sees:**
Options screen allows customisation - adjust controls to preference!

---

### Unit 60: Difficulty Modes

**Learning Objectives:**
- Multiple difficulty settings
- Accessibility options
- Challenge options

**Concepts Introduced:**
- Easy/Normal/Hard modes
- Parameter adjustment per mode
- Mode selection
- Score modifier for difficulty

**Code Written:**
- Difficulty parameter tables
- Mode selection on title
- Apply selected parameters
- Score multiplier per difficulty

**What the Learner Sees:**
Choose difficulty before play - Easy for learning, Hard for experts!

---

### Unit 61: Visual Polish Pass

**Learning Objectives:**
- Final visual refinements
- Consistency check
- Professional appearance

**Concepts Introduced:**
- Colour harmony
- Animation smoothness
- Visual hierarchy
- Professional presentation

**Code Written:**
- Colour adjustments
- Animation timing tweaks
- Consistency fixes
- Final visual touches

**What the Learner Sees:**
Everything polished - consistent colours, smooth animations, professional feel.

---

### Unit 62: Audio Polish Pass

**Learning Objectives:**
- Final audio refinements
- Mix balancing
- Sound priority

**Concepts Introduced:**
- Audio mix review
- Volume balancing
- Effect priority
- Music integration

**Code Written:**
- Volume adjustments
- Priority refinements
- Mix balancing
- Final audio touches

**What the Learner Sees:**
Audio perfectly balanced - every sound clear, nothing overwhelming.

---

### Unit 63: Bug Hunt and Edge Cases

**Learning Objectives:**
- Find and fix bugs
- Edge case handling
- Stability testing

**Concepts Introduced:**
- Systematic testing
- Edge case identification
- Bug fixing
- Regression prevention

**Code Written:**
- Fix identified issues
- Edge case handling
- Stability improvements
- Test documentation

**What the Learner Sees:**
(Stability improvement - no more rare crashes or glitches.)

---

### Unit 64: Release Build

**Learning Objectives:**
- Create final release
- Remove debug code
- Distribution preparation

**Concepts Introduced:**
- Release build process
- Debug code removal
- Final testing
- Version marking

**Code Written:**
- Remove debug displays
- Optimize startup
- Final integration
- Create release PRG

**What the Learner Sees:**
Complete, polished Invader Wave! A worthy tribute to the arcade classic.

---

## Summary

**Invader Wave** recreates the Space Invaders experience with authentic mechanics and modern polish:

**Phase 1 (Foundation):** Core mechanics - player, formation, shooting, shields, basic game.

**Phase 2 (Expansion):** Content - shield destruction, mystery ship, wave progression, difficulty scaling.

**Phase 3 (Polish):** Feel - death animations, sound design, attract mode, two-player mode.

**Phase 4 (Mastery):** Professional quality - optimization, variants, statistics, release build.

### Skills Transferred Forward

The following skills debut in Invader Wave and will be applied in future games:

1. **Formation movement** → Scroll Runner (obstacle patterns), Night Raid (enemy waves)
2. **Coordinated group behaviour** → Any game with enemy groups
3. **Destructible environment** → Night Raid (terrain), Dungeon Crawl (breakable walls)
4. **Accelerating tempo** → Most action games (tension building)
5. **Two-player alternating** → Several future games
6. **Wave progression systems** → Nearly all remaining games

### Game Specifications

- **Formation:** 55 enemies (11×5)
- **Enemy types:** 5 (three base + two advanced)
- **Shields:** 4 bunkers with per-character destruction
- **Mystery ships:** 3 variants with different behaviours
- **Player bullets:** 1 at a time (classic limitation)
- **Enemy bullets:** 3 simultaneous, 3 types (plunger, rolling, squiggly)
- **Waves:** Endless with increasing difficulty
- **Players:** 1-2 alternating
- **Features:** High scores, attract mode, bonus waves, statistics
