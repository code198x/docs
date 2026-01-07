# Arena Fighter: 64-Unit Outline

**Game:** 12 of 16
**Platform:** Commodore 64
**Units:** 64
**Concept:** One-on-one combat. Two fighters, health bars, special moves. An IK+/Street Fighter-inspired fighting game.

---

## Skills Applied from Previous Games

| Skill | Learned In | Application in Arena Fighter |
|-------|-----------|---------------------------|
| SID fundamentals | SID Symphony | Impact sounds, music |
| Hardware sprites | Starfield | Fighter sprites |
| Joystick input | Starfield | Player control |
| Animation frames | Platform Panic | Fighter animation |
| Collision detection | Various | Hit detection |
| Health systems | Dungeon Crawl | Health bars |
| Object state machines | Various | Fighter states |
| Two-player input | Various | Versus play |
| Sprite multiplexing | Sprite Storm | Complex fighters |
| Character graphics | Maze Raider | Arena backgrounds |

## New Skills Introduced

| Skill | Units | Description |
|-------|-------|-------------|
| Animation state machines | 5-8 | Complex state transitions |
| Hitbox/hurtbox | 9-12 | Attack and vulnerable areas |
| Frame data | 13-16 | Startup, active, recovery |
| Move priority | 21-24 | Attack beats defence timing |
| Input buffering | 25-28 | Smooth combo inputs |
| Special move input | 29-32 | Motion + button moves |
| Round/match structure | 17-20 | Best-of-3, win conditions |
| AI opponent | 37-40 | Computer-controlled fighter |

---

## Phase 1: Foundation (Units 1-16)
*Core mechanics: fighters, movement, basic attacks.*

### Unit 1: Fighting Game Concept

**Learning Objectives:**
- Understand fighting game mechanics
- Analyse IK+/Street Fighter structure
- Plan game design

**Concepts Introduced:**
- One-on-one combat
- Health bars
- Round structure
- Attack/defence mechanics

**Code Written:**
- Design document
- Move set planning
- UI design
- Game structure

**What the Learner Sees:**
Understanding fighting game design - move sets, health, rounds.

---

### Unit 2: Arena Setup

**Learning Objectives:**
- Design fighting arena
- Background graphics
- Visual grounding

**Concepts Introduced:**
- Arena character graphics
- Floor and background
- Visual style
- Fixed play area

**Code Written:**
- Arena characters
- Background drawing
- Floor definition
- Visual setup

**What the Learner Sees:**
Fighting arena displayed - dojo/temple background, fighting floor.

---

### Unit 3: Fighter Sprite - Standing

**Learning Objectives:**
- Create fighter sprite
- Standing pose
- Visual representation

**Concepts Introduced:**
- Fighter sprite size
- Standing idle animation
- Character design
- Sprite allocation

**Code Written:**
- Standing sprite data
- Idle animation (2 frames)
- Sprite setup
- Position on ground

**What the Learner Sees:**
Fighter standing in arena - idle animation breathing!

---

### Unit 4: Fighter Data Structure

**Learning Objectives:**
- Track fighter state
- Position, health, state
- Extensible structure

**Concepts Introduced:**
- Fighter data struct
- Position (X, Y)
- Health points
- Current state
- Facing direction

**Code Written:**
- Fighter struct
- Initial values
- Two fighter instances
- State definitions

**What the Learner Sees:**
(Data structure ready - two fighters tracked.)

---

### Unit 5: Fighter Movement - Walking

**Learning Objectives:**
- Walk left and right
- Walking animation
- Arena boundaries

**Concepts Introduced:**
- Walking state
- Movement speed
- Walk cycle animation
- Arena edge clamp

**Code Written:**
- Walk state handling
- Position updates
- Walk animation
- Boundary checks

**What the Learner Sees:**
Fighter walks! Left/right movement with animation.

---

### Unit 6: Fighter Facing

**Learning Objectives:**
- Always face opponent
- Sprite flipping
- Fighting game convention

**Concepts Introduced:**
- Auto-face toward enemy
- Sprite X-flip
- Position comparison
- Smooth facing change

**Code Written:**
- Face direction calc
- Sprite flip handling
- Auto-facing logic
- Smooth updates

**What the Learner Sees:**
Fighter always faces opponent! Walking backward/forward context.

---

### Unit 7: Fighter Animation States

**Learning Objectives:**
- Animation state machine
- State transitions
- State persistence

**Concepts Introduced:**
- State enumeration (idle, walk, attack, etc.)
- State transitions
- Animation per state
- Frame tracking

**Code Written:**
- State machine structure
- Transition rules
- Animation lookup
- Frame counter

**What the Learner Sees:**
(State machine ready - smooth transitions between states.)

**Reference to Platform Panic:**
"Animation states expanded from Platform Panic - now more complex with many states."

---

### Unit 8: Crouch State

**Learning Objectives:**
- Crouching state
- Lower profile
- Block preparation

**Concepts Introduced:**
- Crouch input (down)
- Crouch sprite
- Reduced height
- State transition

**Code Written:**
- Crouch detection
- Crouch sprite data
- State handling
- Return to standing

**What the Learner Sees:**
Press down - fighter crouches! Lower position, different sprite.

---

### Unit 9: Basic Punch Attack

**Learning Objectives:**
- Attack state
- Punch animation
- Attack mechanics

**Concepts Introduced:**
- Attack input (fire button)
- Attack animation frames
- Attack state
- Recovery time

**Code Written:**
- Punch animation data
- Attack state handling
- Frame progression
- Recovery to idle

**What the Learner Sees:**
Press fire - fighter punches! Animation plays, returns to idle.

---

### Unit 10: Hit Detection - Concept

**Learning Objectives:**
- Understand hitbox/hurtbox
- Attack areas
- Vulnerable areas

**Concepts Introduced:**
- Hitbox = attack area
- Hurtbox = vulnerable area
- Per-frame hitbox data
- Collision between them

**Code Written:**
- Hitbox data structure
- Hurtbox data structure
- Per-animation definitions
- Documentation

**What the Learner Sees:**
(Collision concept ready - hitboxes defined.)

---

### Unit 11: Hit Detection - Implementation

**Learning Objectives:**
- Check hitbox overlap
- Detect successful hits
- Trigger damage

**Concepts Introduced:**
- Rectangle overlap test
- Active hitbox check
- Position-relative boxes
- Hit confirmation

**Code Written:**
- Overlap detection
- Hitbox activation
- Position calculation
- Hit flag

**What the Learner Sees:**
Punch hits opponent - hit detected! (Damage next unit.)

---

### Unit 12: Damage and Health

**Learning Objectives:**
- Health bar system
- Damage on hit
- Visual feedback

**Concepts Introduced:**
- Health points (100)
- Damage per attack
- Health bar display
- Hitstun state

**Code Written:**
- Health tracking
- Damage application
- Health bar rendering
- Hitstun handling

**What the Learner Sees:**
Hit opponent - health bar decreases! Fighter reels in hitstun.

---

### Unit 13: Kick Attack

**Learning Objectives:**
- Second attack type
- Different properties
- Move variety

**Concepts Introduced:**
- Kick attack
- Different hitbox
- Different damage
- Input (fire + direction)

**Code Written:**
- Kick animation
- Kick hitbox
- Damage value
- Input handling

**What the Learner Sees:**
Fire + forward = kick! Different animation, different range!

---

### Unit 14: Crouching Attacks

**Learning Objectives:**
- Attacks from crouch
- Low attacks
- Position variety

**Concepts Introduced:**
- Crouch punch/kick
- Low hitbox
- Standing/crouching targets
- Attack variety

**Code Written:**
- Crouch attack anims
- Low hitboxes
- Standing target hit
- State handling

**What the Learner Sees:**
Attack while crouching - low attacks! Different strategic options.

---

### Unit 15: Two-Player Input

**Learning Objectives:**
- Two joystick inputs
- Simultaneous play
- Player 1 vs Player 2

**Concepts Introduced:**
- Port 1 and Port 2
- Simultaneous reading
- Independent control
- True versus mode

**Code Written:**
- Dual input reading
- Fighter assignment
- Independent state
- Full two-player

**What the Learner Sees:**
Two players! Both fighters controlled independently - versus fighting!

---

### Unit 16: Complete Basic Fighting

**Learning Objectives:**
- Integrate all systems
- Playable fighting
- Basic combat

**Concepts Introduced:**
- Complete game loop
- Round win (KO)
- Basic match
- Title screen

**Code Written:**
- Integration
- KO detection
- Round handling
- Title/restart

**What the Learner Sees:**
Complete fighting game! Move, punch, kick, damage - first to KO wins!

---

## Phase 2: Expansion (Units 17-32)
*Rounds, special moves, blocking, more depth.*

### Unit 17: Round System

**Learning Objectives:**
- Best-of-3 rounds
- Round tracking
- Match winner

**Concepts Introduced:**
- Round counter
- Round win tracking
- Match conclusion
- Round reset

**Code Written:**
- Round tracking
- Win counting
- Match logic
- Reset handling

**What the Learner Sees:**
Best of 3 rounds! Win 2 rounds to win the match!

---

### Unit 18: Round Display

**Learning Objectives:**
- Round indicator UI
- Victory markers
- Clear information

**Concepts Introduced:**
- Round indicator icons
- Win markers
- UI positioning
- Visual clarity

**Code Written:**
- Round display
- Win markers
- UI rendering
- Update logic

**What the Learner Sees:**
Round indicators show match progress - clear who's winning!

---

### Unit 19: Fight Timer

**Learning Objectives:**
- Round time limit
- Time-out victory
- Urgency creation

**Concepts Introduced:**
- Round timer
- Time-out condition
- Most health wins
- Draw handling

**Code Written:**
- Timer countdown
- Display formatting
- Time-out logic
- Winner by health

**What the Learner Sees:**
Timer counts down! Time out - most health wins the round!

---

### Unit 20: Blocking

**Learning Objectives:**
- Defensive option
- Block state
- Reduced damage

**Concepts Introduced:**
- Block input (back)
- Block state
- Chip damage
- Block stun

**Code Written:**
- Block detection
- Block state
- Damage reduction
- Block stun

**What the Learner Sees:**
Hold back - fighter blocks! Reduced damage, safer option!

---

### Unit 21: Standing vs Crouching Attacks

**Learning Objectives:**
- Attack height matters
- Block height matters
- Strategic depth

**Concepts Introduced:**
- Attack height (high/mid/low)
- Block height
- Cross-up blocking
- Mind games

**Code Written:**
- Height checking
- Block effectiveness
- Low attacks vs standing block
- Strategic layer

**What the Learner Sees:**
Low attacks hit standing blockers! Must crouch-block low attacks!

---

### Unit 22: Knockdown

**Learning Objectives:**
- Knockdown state
- Down on ground
- Wake-up

**Concepts Introduced:**
- Knockdown trigger
- Down animation
- Invulnerable while down
- Wake-up transition

**Code Written:**
- Knockdown state
- Down sprite
- Invulnerability
- Wake-up timing

**What the Learner Sees:**
Strong hit knocks down! Fighter falls, invulnerable, gets up.

---

### Unit 23: Jump State

**Learning Objectives:**
- Jumping mechanic
- Aerial movement
- Jump attacks

**Concepts Introduced:**
- Jump input (up)
- Arc trajectory
- Aerial vulnerability
- Landing transition

**Code Written:**
- Jump physics
- Air control
- Landing detection
- State transitions

**What the Learner Sees:**
Jump! Fighter arcs through air, lands in crouch/stand.

**Reference to Platform Panic:**
"Jump physics from Platform Panic applied to fighting game context."

---

### Unit 24: Jump Attacks

**Learning Objectives:**
- Attacks while jumping
- Air-to-ground combat
- Strategic option

**Concepts Introduced:**
- Jump punch/kick
- Air hitboxes
- Cross-up attacks
- Risk/reward

**Code Written:**
- Jump attack anims
- Air hitboxes
- Landing cancel
- Strategic depth

**What the Learner Sees:**
Attack while jumping! Jump kicks for combo starters!

---

### Unit 25: Input Buffering

**Learning Objectives:**
- Smooth input handling
- Buffer during animation
- Responsive combos

**Concepts Introduced:**
- Input buffer
- Store during animation
- Execute on recovery
- Smooth feel

**Code Written:**
- Input buffer system
- Buffer window
- Execution timing
- Responsive control

**What the Learner Sees:**
(Smoother controls - inputs feel more responsive.)

---

### Unit 26: Throw Mechanic

**Learning Objectives:**
- Close-range throw
- Beats blocking
- Rock-paper-scissors

**Concepts Introduced:**
- Throw input
- Range check (close)
- Throw tech (counter)
- Damage and reset

**Code Written:**
- Throw detection
- Range checking
- Throw animation
- Tech option

**What the Learner Sees:**
Close + grab = throw! Throws beat blocking - mind games!

---

### Unit 27: Special Move Framework

**Learning Objectives:**
- Motion input moves
- Special move concept
- Input detection

**Concepts Introduced:**
- Motion inputs (QCF, DP, etc.)
- Input history
- Motion detection
- Special properties

**Code Written:**
- Input history buffer
- Motion detection
- Framework ready

**What the Learner Sees:**
(Special move framework ready.)

---

### Unit 28: Fireball Special Move

**Learning Objectives:**
- Projectile special
- QCF + punch
- Classic move

**Concepts Introduced:**
- Quarter-circle forward
- Projectile spawn
- Travel and collision
- Counter options

**Code Written:**
- QCF detection
- Projectile spawn
- Projectile logic
- Collision handling

**What the Learner Sees:**
Quarter-circle forward + punch = fireball! Projectile travels across!

---

### Unit 29: Uppercut Special Move

**Learning Objectives:**
- Anti-air special
- Dragon punch motion
- Invincible frames

**Concepts Introduced:**
- Forward, down, down-forward
- Anti-air purpose
- Invincible startup
- Big risk/reward

**Code Written:**
- DP motion detection
- Uppercut animation
- Invincibility frames
- High damage

**What the Learner Sees:**
Dragon punch motion = uppercut! Rising attack, beats jump-ins!

---

### Unit 30: Super Meter

**Learning Objectives:**
- Build meter with attacks
- Resource management
- Enhanced moves

**Concepts Introduced:**
- Super meter
- Build on hit/block
- Spend for power
- Strategic resource

**Code Written:**
- Meter tracking
- Meter display
- Build triggers
- Spend mechanic

**What the Learner Sees:**
Meter builds during combat! Full meter = powerful options!

---

### Unit 31: Super Move

**Learning Objectives:**
- Cinematic super attack
- Meter consumption
- High damage

**Concepts Introduced:**
- Super input
- Meter requirement
- Enhanced animation
- High damage

**Code Written:**
- Super detection
- Meter check
- Super animation
- Big damage

**What the Learner Sees:**
Full meter + special input = SUPER MOVE! Dramatic, high damage!

---

### Unit 32: Character Variety (Second Fighter)

**Learning Objectives:**
- Second playable fighter
- Different move set
- Character choice

**Concepts Introduced:**
- Multiple characters
- Different sprites
- Different specials
- Character selection

**Code Written:**
- Second character data
- Different animations
- Different specials
- Selection screen

**What the Learner Sees:**
Two different fighters! Choose your character - different play styles!

---

## Phase 3: Polish (Units 33-48)
*AI, effects, sound, presentation.*

### Unit 33: Hit Effects

**Learning Objectives:**
- Visual hit feedback
- Impact effects
- Satisfaction

**Concepts Introduced:**
- Hit spark sprites
- Hit flash
- Screen shake on big hits
- Impact feel

**Code Written:**
- Hit spark rendering
- Flash effect
- Screen shake
- Feel enhancement

**What the Learner Sees:**
Hits look impactful! Sparks, flashes, screen shake on big hits!

---

### Unit 34: Sound Design - Impacts

**Learning Objectives:**
- Hit sounds
- Block sounds
- Audio feedback

**Concepts Introduced:**
- Impact sound palette
- Punch/kick variation
- Block sounds
- Whiff sounds

**Code Written:**
- Impact sounds
- Variation handling
- Block audio
- Complete feedback

**What the Learner Sees:**
Every hit sounds powerful! Punchy audio feedback.

**Reference to SID Symphony:**
"SID percussion techniques for impactful fighting sounds."

---

### Unit 35: Sound Design - Voice

**Learning Objectives:**
- Character voices
- Attack shouts
- Impact grunts

**Concepts Introduced:**
- Voice samples (or SID approximation)
- Attack calls
- Hit reactions
- Character personality

**Code Written:**
- Voice sounds
- Trigger points
- Character distinction
- Integration

**What the Learner Sees:**
Fighters grunt and shout! Character personality through audio.

---

### Unit 36: Fighting Music

**Learning Objectives:**
- Combat music
- Energy and tension
- Stage theme

**Concepts Introduced:**
- Fight music
- Tempo and energy
- Stage-appropriate
- Music system

**Code Written:**
- Fight music composition
- Music playback
- Round integration
- Victory music

**What the Learner Sees:**
Energetic fighting music drives the action!

---

### Unit 37: AI Opponent - Framework

**Learning Objectives:**
- Computer opponent
- Decision making
- Single-player mode

**Concepts Introduced:**
- AI state machine
- Decision factors
- Reaction system
- Difficulty levels

**Code Written:**
- AI framework
- Decision structure
- Input generation
- Framework ready

**What the Learner Sees:**
(AI framework ready.)

---

### Unit 38: AI Opponent - Basic

**Learning Objectives:**
- Basic AI behaviour
- Attack and defence
- Playable single-player

**Concepts Introduced:**
- Distance evaluation
- Attack selection
- Block on attack
- Basic competence

**Code Written:**
- Distance checking
- Attack decisions
- Defence reaction
- Basic AI

**What the Learner Sees:**
Fight against CPU! AI attacks and blocks - decent challenge!

---

### Unit 39: AI Opponent - Difficulty

**Learning Objectives:**
- Difficulty scaling
- Reaction speed
- Challenge curve

**Concepts Introduced:**
- Difficulty parameters
- Reaction delay
- Aggression levels
- Easy/Medium/Hard

**Code Written:**
- Difficulty tables
- Parameter adjustment
- Scaling application
- Selectable difficulty

**What the Learner Sees:**
Choose AI difficulty! Easy for learning, Hard for challenge!

---

### Unit 40: Combo System

**Learning Objectives:**
- Chain attacks together
- Combo counter
- Skill expression

**Concepts Introduced:**
- Cancel windows
- Chain rules
- Combo counting
- Damage scaling

**Code Written:**
- Cancel detection
- Chain allowance
- Combo counter
- Scaling

**What the Learner Sees:**
Chain attacks! "3 HIT COMBO!" - skill expression!

---

### Unit 41: Title Screen

**Learning Objectives:**
- Professional presentation
- Mode selection
- Polish

**Concepts Introduced:**
- Fighting game title
- Mode selection
- Character select flow
- Professional look

**Code Written:**
- Title screen
- Mode menu
- Flow handling
- Polish

**What the Learner Sees:**
Professional fighting game title - arcade quality presentation!

---

### Unit 42: Character Select

**Learning Objectives:**
- Fighter selection UI
- Portrait display
- Versus screen

**Concepts Introduced:**
- Selection screen
- Character portraits
- Confirmation
- Versus intro

**Code Written:**
- Selection UI
- Portrait display
- Confirmation handling
- Versus transition

**What the Learner Sees:**
Character select screen with portraits! Choose and confirm!

---

### Unit 43: Victory Screen

**Learning Objectives:**
- Match victory display
- Winner celebration
- Statistics

**Concepts Introduced:**
- Victory screen
- Winner pose
- Match stats
- Rematch option

**Code Written:**
- Victory display
- Winner animation
- Stats formatting
- Rematch flow

**What the Learner Sees:**
Victory! Winner poses, stats shown, rematch option!

---

### Unit 44: Training Mode

**Learning Objectives:**
- Practice environment
- Move testing
- Learning space

**Concepts Introduced:**
- Training mode
- Dummy opponent
- Reset options
- Learning tool

**Code Written:**
- Training mode
- Dummy settings
- Reset handling
- Move display

**What the Learner Sees:**
Training mode! Practice moves against dummy - learn combos!

---

### Unit 45: Additional Arena

**Learning Objectives:**
- Second fighting arena
- Visual variety
- Stage selection

**Concepts Introduced:**
- Multiple stages
- Different visuals
- Selection option
- Variety value

**Code Written:**
- Second arena data
- Stage selection
- Visual variation
- Integration

**What the Learner Sees:**
Multiple arenas! Different backgrounds for variety!

---

### Unit 46: Visual Polish

**Learning Objectives:**
- Final visual refinements
- Animation smoothness
- Professional quality

**Concepts Introduced:**
- Animation review
- Visual consistency
- Effect polish
- Professional look

**Code Written:**
- Visual adjustments
- Animation fixes
- Effect refinement
- Polish

**What the Learner Sees:**
Everything polished - smooth animations, consistent visuals!

---

### Unit 47: Audio Polish

**Learning Objectives:**
- Final audio refinements
- Mix balance
- Impact enhancement

**Concepts Introduced:**
- Audio review
- Balance adjustments
- Impact refinement
- Final mix

**Code Written:**
- Audio adjustments
- Balance refinement
- Impact enhancement
- Final mix

**What the Learner Sees:**
Audio perfectly balanced - impactful, clear, professional!

---

### Unit 48: Arcade Mode

**Learning Objectives:**
- Ladder progression
- Multiple opponents
- Arcade experience

**Concepts Introduced:**
- Opponent ladder
- Difficulty progression
- Ending reward
- Arcade feel

**Code Written:**
- Ladder structure
- Progression logic
- Difficulty curve
- Ending handling

**What the Learner Sees:**
Arcade mode! Fight through opponents to reach the end!

---

## Phase 4: Mastery (Units 49-64)
*Advanced features, additional content, polish.*

### Unit 49: Third Fighter

**Learning Objectives:**
- Additional character
- More variety
- Roster expansion

**Concepts Introduced:**
- Third character design
- Unique specials
- Different archetype
- Roster depth

**Code Written:**
- Third character data
- Unique animations
- Unique specials
- Integration

**What the Learner Sees:**
Third fighter! Different style, new strategies to learn!

---

### Unit 50: Fourth Fighter

**Learning Objectives:**
- Roster completion
- Archetype coverage
- Character variety

**Concepts Introduced:**
- Fourth character design
- Complete archetypes
- Balanced roster
- Final variety

**Code Written:**
- Fourth character data
- Unique content
- Balance consideration
- Integration

**What the Learner Sees:**
Four fighters total! Complete roster with variety!

---

### Unit 51: Frame Data Display

**Learning Objectives:**
- Show move properties
- Training tool
- Knowledge sharing

**Concepts Introduced:**
- Frame data concept
- Startup/active/recovery
- Display in training
- Learning aid

**Code Written:**
- Frame data tracking
- Display system
- Training integration
- Documentation

**What the Learner Sees:**
Training mode shows frame data! Learn move properties!

---

### Unit 52: Input Display

**Learning Objectives:**
- Show inputs on screen
- Learning tool
- Combo verification

**Concepts Introduced:**
- Input history display
- Direction + button
- Training tool
- Verification

**Code Written:**
- Input display
- History tracking
- Visual representation
- Training integration

**What the Learner Sees:**
Input display shows what you're pressing - learning aid!

---

### Unit 53: Performance Optimization

**Learning Objectives:**
- Smooth gameplay
- Consistent timing
- Optimization

**Concepts Introduced:**
- Performance profiling
- Animation optimization
- Collision optimization
- Smooth gameplay

**Code Written:**
- Optimization passes
- Efficiency improvements
- Verification
- Documentation

**What the Learner Sees:**
(Rock-solid 50fps gameplay.)

---

### Unit 54: Advanced AI

**Learning Objectives:**
- Smarter AI behaviour
- Pattern recognition
- Competitive challenge

**Concepts Introduced:**
- Pattern adaptation
- Punish recognition
- Combo execution
- True challenge

**Code Written:**
- Advanced AI logic
- Pattern tracking
- Combo AI
- Challenge tuning

**What the Learner Sees:**
Hardest AI is truly challenging - adapts to patterns!

---

### Unit 55: Command List

**Learning Objectives:**
- Move list display
- In-game reference
- Player resource

**Concepts Introduced:**
- Move list UI
- Command notation
- Per-character list
- Accessibility

**Code Written:**
- Move list screen
- Command display
- Per-character content
- Integration

**What the Learner Sees:**
Pause for command list! See all moves for your character!

---

### Unit 56: Versus Records

**Learning Objectives:**
- Track win/loss
- Player records
- Competition tracking

**Concepts Introduced:**
- Record tracking
- Per-character records
- Display screen
- Competition history

**Code Written:**
- Record system
- Storage
- Display
- Persistence

**What the Learner Sees:**
Records track wins and losses! Competition history!

---

### Unit 57: Tournament Mode

**Learning Objectives:**
- Multi-player tournament
- Bracket structure
- Group play

**Concepts Introduced:**
- Tournament structure
- Bracket management
- Multiple players
- Champion determination

**Code Written:**
- Tournament logic
- Bracket display
- Match progression
- Champion declaration

**What the Learner Sees:**
Tournament mode for multiple players! Bracket competition!

---

### Unit 58: Balance Adjustment

**Learning Objectives:**
- Damage tuning
- Move balance
- Fair competition

**Concepts Introduced:**
- Balance testing
- Damage adjustment
- Move property tuning
- Fair matches

**Code Written:**
- Balance parameters
- Adjustment passes
- Testing
- Documentation

**What the Learner Sees:**
(Balanced, fair fighting experience.)

---

### Unit 59: Sound Options

**Learning Objectives:**
- Audio preferences
- Music/SFX volume
- Player control

**Concepts Introduced:**
- Audio options
- Volume controls
- Save preferences
- Customization

**Code Written:**
- Options menu
- Volume controls
- Preference saving
- Integration

**What the Learner Sees:**
Audio options - adjust music and sound effect volumes!

---

### Unit 60: Gallery Mode

**Learning Objectives:**
- View character art
- Unlockable content
- Reward system

**Concepts Introduced:**
- Gallery screen
- Unlock conditions
- Art display
- Progression reward

**Code Written:**
- Gallery system
- Unlock tracking
- Art display
- Integration

**What the Learner Sees:**
Gallery shows character art! Unlock by playing!

---

### Unit 61: Memory Optimization

**Learning Objectives:**
- Efficient data storage
- Animation compression
- Memory management

**Concepts Introduced:**
- Memory review
- Data optimization
- Animation efficiency
- Documentation

**Code Written:**
- Memory optimization
- Data compression
- Layout cleanup
- Documentation

**What the Learner Sees:**
(Internal - efficient memory use.)

---

### Unit 62: Bug Hunting

**Learning Objectives:**
- Find and fix bugs
- Edge cases
- Quality assurance

**Concepts Introduced:**
- Systematic testing
- Edge case handling
- Bug fixing
- Polish

**Code Written:**
- Bug fixes
- Edge cases
- Polish fixes
- Verification

**What the Learner Sees:**
(Stable, polished fighting game.)

---

### Unit 63: Documentation

**Learning Objectives:**
- Document fighting system
- Technical reference
- Knowledge preservation

**Concepts Introduced:**
- System documentation
- Frame data docs
- Reference guide
- Teaching value

**Code Written:**
- Documentation
- Reference material
- Code comments
- Guide

**What the Learner Sees:**
Complete fighting game documentation!

---

### Unit 64: Release Build

**Learning Objectives:**
- Final release
- Debug removal
- Distribution ready

**Concepts Introduced:**
- Release process
- Debug removal
- Final testing
- Distribution

**Code Written:**
- Debug removal
- Final integration
- Release PRG
- Distribution

**What the Learner Sees:**
Complete Arena Fighter! Professional fighting game ready for distribution!

---

## Summary

**Arena Fighter** teaches fighting game development:

**Phase 1 (Foundation):** Core combat - movement, attacks, hit detection, damage.

**Phase 2 (Expansion):** Depth - rounds, special moves, blocking, combos.

**Phase 3 (Polish):** Presentation - AI, effects, sound, modes.

**Phase 4 (Mastery):** Content - additional fighters, balance, features.

### Skills Transferred Forward

The following skills debut in Arena Fighter:

1. **Complex animation state machines** → Mega Blaster, Symphony's End
2. **Hitbox/hurtbox collision** → Any game with complex combat
3. **Frame data concepts** → Action games with timing
4. **Input buffering** → Complex input games
5. **AI opponent behaviour** → All subsequent AI games
6. **Round/match structure** → Sports/competitive games

### Game Specifications

- **Fighters:** 4 playable characters
- **Attacks:** Punch, kick, crouch variants, jump variants
- **Special moves:** 2-3 per character (fireball, uppercut, etc.)
- **Super moves:** 1 per character
- **Defence:** Block (standing/crouching), throw tech
- **Match:** Best of 3 rounds, 60-second timer
- **Modes:** Versus, Arcade, Training, Tournament
- **Players:** 1-2 (vs CPU or human)
- **Features:** Combo counter, super meter, character select
