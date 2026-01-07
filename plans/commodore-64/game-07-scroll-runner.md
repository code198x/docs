# Scroll Runner: 64-Unit Outline

**Game:** 7 of 16
**Platform:** Commodore 64
**Units:** 64
**Concept:** Horizontal scrolling introduction. Runner dodges obstacles in an endless scroll, jumping and ducking to survive.

---

## Skills Applied from Previous Games

| Skill | Learned In | Application in Scroll Runner |
|-------|-----------|---------------------------|
| SID fundamentals | SID Symphony | Music and sound effects |
| Game loop structure | SID Symphony | Frame-perfect timing for scrolling |
| Hardware sprites | Starfield | Player character sprite |
| Joystick input | Starfield | Jump and duck controls |
| Sprite collision | Starfield | Player-obstacle collision |
| Score display | Starfield | Distance/score display |
| Custom character sets | Maze Raider | Terrain graphics |
| Tile-based concepts | Maze Raider | Ground and obstacle tiles |
| Gravity/jumping | Platform Panic | Player jump mechanics |
| Animation frames | Platform Panic | Running animation |
| Speed ramping | Brick Basher | Scroll speed increases |
| High score persistence | Brick Basher | Save best distance |
| Wave progression | Invader Wave | Difficulty zones |

## New Skills Introduced

| Skill | Units | Description |
|-------|-------|-------------|
| Hardware scroll register | 5-8 | VIC-II $D016 for smooth scrolling |
| Character column update | 9-12 | Shifting screen and updating new column |
| Colour RAM scrolling | 13-16 | The tricky colour RAM sync |
| Double buffering | 21-24 | Preparing data while displaying |
| Procedural generation | 25-32 | Generating endless terrain |
| Raster colour splits | 17-20 | Different colours at different screen heights |
| Screen buffer management | 37-40 | Managing multiple screen banks |
| Scroll speed control | 41-44 | Variable scroll speeds |

---

## Phase 1: Foundation (Units 1-16)
*Core mechanics: scrolling, runner, obstacles, and a playable game.*

### Unit 1: Understanding C64 Scrolling

**Learning Objectives:**
- Understand hardware scrolling concept
- Learn VIC-II scroll registers
- Distinguish hardware vs. software scroll

**Concepts Introduced:**
- Software scrolling (moving every character - slow!)
- Hardware scrolling (VIC-II shifts display - fast!)
- $D016 horizontal scroll bits (0-7)
- Screen appears to move by pixels

**Code Written:**
- Set up screen with characters
- Demonstrate software scroll (slow)
- Document $D016 scroll register
- Prepare for hardware method

**What the Learner Sees:**
Software scroll demonstration showing why it's slow - setting up the "why" for hardware scroll.

---

### Unit 2: Hardware Scroll Register

**Learning Objectives:**
- Control $D016 scroll bits
- Observe smooth pixel scrolling
- Understand the 8-pixel cycle

**Concepts Introduced:**
- $D016 bits 0-2 = scroll offset (0-7)
- Screen shifts 0-7 pixels right
- After 7, must shift characters and reset
- 8-pixel scroll cycle

**Code Written:**
- Read $D016
- Modify scroll bits
- Increment scroll value each frame
- Watch screen content shift

**What the Learner Sees:**
Screen content smoothly shifts left pixel by pixel! But wait - after 8 pixels something needs to happen...

---

### Unit 3: The 8-Pixel Reset

**Learning Objectives:**
- Understand character boundary wrap
- Shift screen data on reset
- Create continuous scroll

**Concepts Introduced:**
- Scroll 0→7, then reset to 0
- On reset, shift all screen data left one character
- New data enters from right
- Illusion of continuous movement

**Code Written:**
- Track scroll position
- Detect scroll wrap (7→0)
- Shift screen memory left
- Reset scroll register to 0

**What the Learner Sees:**
Continuous scrolling! Every 8 pixels, screen shifts and new column appears at right.

---

### Unit 4: Screen Memory Shifting

**Learning Objectives:**
- Efficiently copy screen data
- Shift 40 columns left by one
- Handle all 25 rows

**Concepts Introduced:**
- Screen memory layout ($0400-$07E7)
- Row-by-row copying
- Destination = source + 1
- 25 rows × 39 characters = 975 copies

**Code Written:**
- Screen shift routine
- Copy each row left
- Handle all rows
- Leave rightmost column for new data

**What the Learner Sees:**
(Internal mechanics - scroll now works smoothly.)

---

### Unit 5: Optimizing Screen Shift

**Learning Objectives:**
- Optimize the shift routine
- Reduce cycle cost
- Maintain frame budget

**Concepts Introduced:**
- Cycle counting
- Unrolled loops
- Page-aligned benefits
- Split across frames (if needed)

**Code Written:**
- Profile current routine
- Unroll inner loop
- Test timing
- Ensure fits in frame

**What the Learner Sees:**
(Performance improvement - no visible stutter during shift.)

---

### Unit 6: Adding New Column

**Learning Objectives:**
- Write new data to right column
- Create basic terrain
- Establish ground line

**Concepts Introduced:**
- Column 39 receives new data
- Terrain column format
- Ground characters
- Sky characters (empty)

**Code Written:**
- Column write routine
- Define ground character
- Write ground at bottom rows
- Sky above ground

**What the Learner Sees:**
Scrolling terrain! Ground moves left, sky above, endless landscape.

---

### Unit 7: The Player Runner

**Learning Objectives:**
- Create runner sprite
- Position at left side
- Fixed X, variable Y

**Concepts Introduced:**
- Runner sprite design
- Screen-left positioning
- Y position for ground level
- Sprite stays still, world moves

**Code Written:**
- Define runner sprite data
- Position sprite on ground
- Fixed X position (left third)
- Y at ground height

**What the Learner Sees:**
Runner sprite stands on scrolling ground - world flows past!

**Reference to Starfield:**
"Sprite setup from Starfield, but now the player is stationary while the world moves."

---

### Unit 8: Running Animation

**Learning Objectives:**
- Animate runner during scroll
- Sync animation to scroll
- Create running illusion

**Concepts Introduced:**
- Animation frames (4+ frames)
- Animation timer
- Sync with scroll speed
- Faster scroll = faster animation

**Code Written:**
- Create 4 running frames
- Animation frame counter
- Cycle frames while scrolling
- Speed matches scroll

**What the Learner Sees:**
Runner's legs pump as ground scrolls - looks like running!

**Reference to Platform Panic:**
"Animation frames from Platform Panic, now synced to scroll speed rather than player velocity."

---

### Unit 9: Jumping Mechanic

**Learning Objectives:**
- Implement jump on button press
- Use gravity from Platform Panic
- Land back on ground

**Concepts Introduced:**
- Jump state (grounded/jumping)
- Initial upward velocity
- Gravity pulls down
- Landing detection

**Code Written:**
- Detect fire button
- Apply jump velocity
- Apply gravity each frame
- Detect ground and land

**What the Learner Sees:**
Press fire - runner jumps! Gravity brings them back down. Classic endless runner control.

**Reference to Platform Panic:**
"Direct application of Platform Panic's jump physics - same gravity, same velocity system."

---

### Unit 10: Jump Animation

**Learning Objectives:**
- Different sprite for jumping
- Transition frames
- Land animation

**Concepts Introduced:**
- Jump sprite frame
- Fall sprite frame
- Landing transition
- State-based animation

**Code Written:**
- Jump sprite data
- Fall sprite data
- Animation state machine
- Smooth transitions

**What the Learner Sees:**
Runner tucks legs while jumping, extends on descent - smooth jump animation!

---

### Unit 11: Basic Obstacles

**Learning Objectives:**
- Add obstacles in terrain
- Simple ground-level hazards
- Requires jumping to avoid

**Concepts Introduced:**
- Obstacle characters
- Placement in terrain data
- Jump-over obstacles
- Visual distinction

**Code Written:**
- Define obstacle character
- Add obstacles to terrain generation
- Random placement
- Visual clarity

**What the Learner Sees:**
Obstacles appear in path! Must jump over them to survive.

---

### Unit 12: Collision Detection

**Learning Objectives:**
- Detect runner hitting obstacle
- Character-based collision
- Pixel-perfect not needed

**Concepts Introduced:**
- Sprite-to-character collision
- Check character at runner's position
- Collision zone (runner's feet)
- Death on collision

**Code Written:**
- Calculate runner's character position
- Read screen character at position
- Check against obstacle character
- Trigger death on match

**What the Learner Sees:**
Hit an obstacle - runner crashes! Collision detection works.

**Reference to Maze Raider:**
"Tile collision concepts from Maze Raider applied to scrolling environment."

---

### Unit 13: The Colour RAM Problem

**Learning Objectives:**
- Understand colour RAM limitation
- Why colour doesn't scroll with hardware
- Plan colour solution

**Concepts Introduced:**
- Colour RAM at $D800
- Not affected by scroll register
- Must scroll manually
- Same timing as character shift

**Code Written:**
- Demonstrate colour RAM issue
- Document the problem
- Plan colour shift routine

**What the Learner Sees:**
Colours stay still while characters scroll - looks broken! This is why colour RAM needs work.

---

### Unit 14: Colour RAM Scrolling

**Learning Objectives:**
- Implement colour RAM shift
- Sync with screen shift
- Continuous coloured scroll

**Concepts Introduced:**
- Colour RAM shift routine
- Same timing as screen shift
- Copy $D800 region
- Write new colours on right

**Code Written:**
- Colour RAM shift routine
- Sync with screen shift
- Handle all rows
- New column colours

**What the Learner Sees:**
Colours now scroll with content! Proper coloured terrain flowing past.

---

### Unit 15: Death and Restart

**Learning Objectives:**
- Handle player death
- Display distance
- Restart game

**Concepts Introduced:**
- Death animation
- Distance as score
- Game over screen
- Restart flow

**Code Written:**
- Death animation
- Stop scrolling
- Display final distance
- Fire to restart

**What the Learner Sees:**
Crash into obstacle - death animation plays, distance shown, press fire to try again!

---

### Unit 16: Complete Playable Runner

**Learning Objectives:**
- Integrate all systems
- Add title screen
- Polish basic game

**Concepts Introduced:**
- Title screen
- Game state machine
- Distance counter display
- Basic difficulty (fixed obstacle rate)

**Code Written:**
- Title screen
- Distance counter
- Game states
- Basic playable loop

**What the Learner Sees:**
Complete endless runner! Title, gameplay, death, restart. First scrolling game complete!

---

## Phase 2: Expansion (Units 17-32)
*Content variety: terrain, obstacles, power-ups, difficulty.*

### Unit 17: Raster Interrupts Introduction

**Learning Objectives:**
- Understand raster timing
- Set up raster interrupt
- Change register mid-frame

**Concepts Introduced:**
- VIC-II raster line counter
- IRQ on specific raster line
- Change colours per screen section
- Raster splits

**Code Written:**
- Set up raster interrupt
- Trigger on specific line
- Change background colour
- Acknowledge interrupt

**What the Learner Sees:**
Sky is blue at top, darker at bottom - colour changes mid-screen!

---

### Unit 18: Sky Gradient

**Learning Objectives:**
- Multiple raster splits
- Create gradient sky
- Enhance visual depth

**Concepts Introduced:**
- Multiple colour changes
- Chained interrupts
- Colour gradient effect
- Performance consideration

**Code Written:**
- Multiple raster points
- Colour table for gradient
- Chain interrupt handlers
- Smooth colour transition

**What the Learner Sees:**
Beautiful gradient sky! Multiple shades creating depth illusion.

---

### Unit 19: Ducking Mechanic

**Learning Objectives:**
- Add duck/slide move
- Avoid high obstacles
- Different collision shape

**Concepts Introduced:**
- Duck state (standing/ducking)
- Duck sprite (shorter)
- High obstacles (only avoid by ducking)
- Input: joystick down

**Code Written:**
- Duck sprite data
- Detect down input
- Change collision height
- Return to standing when released

**What the Learner Sees:**
Push down - runner slides/ducks! Can pass under high obstacles.

---

### Unit 20: High Obstacles

**Learning Objectives:**
- Add obstacles requiring ducking
- Variety in challenge
- Strategic choice

**Concepts Introduced:**
- High obstacle character
- Requires ducking to pass
- Jump won't help (hits head)
- Visual distinction from jump obstacles

**Code Written:**
- High obstacle character
- Collision at standing height only
- Passes if ducking
- Distinct appearance

**What the Learner Sees:**
Overhead hazards! Must duck to avoid - jumping won't help!

---

### Unit 21: Terrain Variety - Pits

**Learning Objectives:**
- Add pit/gap obstacles
- Must jump to cross
- Multi-character hazards

**Concepts Introduced:**
- Pit as missing ground
- Width variable
- Fall = death
- Clear visual warning

**Code Written:**
- Pit terrain generation
- Variable width pits
- Fall detection
- Death on falling

**What the Learner Sees:**
Gaps in ground! Must jump to cross or fall to death!

---

### Unit 22: Pit Warning System

**Learning Objectives:**
- Visual warning before pits
- Edge characters
- Fair challenge

**Concepts Introduced:**
- Edge warning character
- Appears before pit
- Fair player warning
- Depth-cue graphics

**Code Written:**
- Edge character graphics
- Place before pits
- Visual depth effect
- Consistent warning distance

**What the Learner Sees:**
Ground edge warns of coming pit - fair chance to react!

---

### Unit 23: Double Buffer Concept

**Learning Objectives:**
- Understand double buffering
- Prepare next column while displaying
- Eliminate glitches

**Concepts Introduced:**
- Buffer A displays while buffer B prepares
- Swap buffers on update
- Eliminates torn updates
- Memory trade-off

**Code Written:**
- Set up two screen buffers
- Alternate between them
- Prepare ahead
- Swap pointer on shift

**What the Learner Sees:**
(Internal improvement - smoother scrolling, no glitches.)

---

### Unit 24: Buffer Implementation

**Learning Objectives:**
- Implement double buffering
- VIC-II screen pointer
- Sync buffer swap to scroll

**Concepts Introduced:**
- $D018 screen pointer
- Swap displayed screen
- Update non-displayed screen
- Raster-safe swap timing

**Code Written:**
- Configure second screen
- Point VIC-II to screens
- Prepare next screen
- Swap on scroll cycle

**What the Learner Sees:**
(Rock-solid scrolling - preparation happens invisibly.)

---

### Unit 25: Procedural Generation - Basics

**Learning Objectives:**
- Generate terrain algorithmically
- Simple rules for obstacles
- Reproducible with seed

**Concepts Introduced:**
- Random number generation
- Obstacle placement rules
- Minimum spacing
- Seed-based reproduction

**Code Written:**
- Random number generator
- Obstacle probability
- Minimum distance enforcement
- Seed storage

**What the Learner Sees:**
Different run each time! Procedural generation creates variety.

---

### Unit 26: Procedural Generation - Patterns

**Learning Objectives:**
- Generate recognisable patterns
- Jump sequences
- Fair difficulty

**Concepts Introduced:**
- Pattern library
- Random pattern selection
- Pattern-to-terrain conversion
- Difficulty-appropriate selection

**Code Written:**
- Define pattern library
- Select random pattern
- Place pattern in terrain
- Spacing between patterns

**What the Learner Sees:**
Recognisable challenge patterns - triple jump, duck-jump-duck, etc.!

---

### Unit 27: Difficulty Zones

**Learning Objectives:**
- Increase difficulty over distance
- Zone-based parameters
- Progressive challenge

**Concepts Introduced:**
- Distance thresholds
- Zone parameters (obstacle rate, speed)
- Gradual increase
- Maximum difficulty cap

**Code Written:**
- Track distance
- Define zone thresholds
- Adjust parameters at thresholds
- Cap at maximum difficulty

**What the Learner Sees:**
Further = harder! Obstacles more frequent, scroll faster.

**Reference to Invader Wave:**
"Zone progression similar to Invader Wave's wave system - difficulty parameters scale with progress."

---

### Unit 28: Scroll Speed Variation

**Learning Objectives:**
- Control scroll speed
- Faster zones, slower zones
- Variable frame timing

**Concepts Introduced:**
- Scroll speed variable
- Pixels per frame control
- Animation sync to speed
- Speed as difficulty lever

**Code Written:**
- Variable scroll increment
- Apply to scroll register
- Sync animation to speed
- Smooth speed transitions

**What the Learner Sees:**
Game speeds up as you progress - must react faster!

---

### Unit 29: Collectibles

**Learning Objectives:**
- Add pickup items
- Bonus points
- Risk/reward positioning

**Concepts Introduced:**
- Collectible characters
- Score on collection
- Positioned in risky spots
- Visual attraction

**Code Written:**
- Collectible character
- Spawn in generation
- Collision detection for collection
- Add to score

**What the Learner Sees:**
Coins/gems in terrain! Collect for bonus points - some require risky jumps!

---

### Unit 30: Magnet Power-Up

**Learning Objectives:**
- Power-up that attracts collectibles
- Time-limited effect
- Strategic advantage

**Concepts Introduced:**
- Power-up spawning
- Magnet effect (auto-collect nearby)
- Duration timer
- Visual indicator

**Code Written:**
- Power-up character
- Collection radius effect
- Duration countdown
- Effect indicator

**What the Learner Sees:**
Grab magnet power-up - collectibles fly to you! Lasts a few seconds.

**Reference to Brick Basher:**
"Power-up system concepts from Brick Basher applied to runner format."

---

### Unit 31: Invincibility Power-Up

**Learning Objectives:**
- Temporary invincibility
- Pass through obstacles
- Balanced duration

**Concepts Introduced:**
- Invincibility state
- Collision disabled
- Duration timer
- Visual flash effect

**Code Written:**
- Invincibility flag
- Skip collision when active
- Timer countdown
- Sprite flash while active

**What the Learner Sees:**
Star power-up - run through obstacles! Flashing indicates active. Limited time!

---

### Unit 32: Score Multiplier Power-Up

**Learning Objectives:**
- Multiplied point collection
- Risk/reward for distance
- Score chasing

**Concepts Introduced:**
- Score multiplier state
- 2× or 3× collection
- Duration timer
- Visual indicator

**Code Written:**
- Multiplier variable
- Apply to collectible value
- Duration countdown
- Multiplier display

**What the Learner Sees:**
Multiplier power-up - double points! Limited time to maximise score.

---

## Phase 3: Polish (Units 33-48)
*Effects, sound, visual feedback, and "juice".*

### Unit 33: Parallax Background

**Learning Objectives:**
- Slower-moving background layer
- Depth through parallax
- Character-based background

**Concepts Introduced:**
- Background layer (slower scroll)
- Separate update rate
- Mountains/clouds in distance
- Depth perception

**Code Written:**
- Background character graphics
- Slower update rate
- Background scroll logic
- Integration with main scroll

**What the Learner Sees:**
Distant mountains scroll slower than ground - parallax depth!

---

### Unit 34: Foreground Elements

**Learning Objectives:**
- Occasional foreground objects
- Pass behind player
- Depth layering

**Concepts Introduced:**
- Foreground layer concept
- Sprite priority
- Passing behind player
- Depth enhancement

**Code Written:**
- Foreground sprite objects
- Sprite behind character priority
- Spawn and scroll
- Depth effect

**What the Learner Sees:**
Trees/posts occasionally pass in foreground - three depth layers!

---

### Unit 35: Sound Design - Running

**Learning Objectives:**
- Footstep sounds
- Rhythm matches animation
- Grounded audio

**Concepts Introduced:**
- Footstep timing
- Sound variation
- Volume for surface type
- Running rhythm

**Code Written:**
- Footstep sound effect
- Trigger on animation frame
- Vary pitch slightly
- Surface-type variation

**What the Learner Sees:**
Rhythmic footsteps match runner's feet - satisfying running audio!

**Reference to SID Symphony:**
"SID percussion techniques create convincing footstep rhythm."

---

### Unit 36: Sound Design - Actions

**Learning Objectives:**
- Jump and duck sounds
- Collection sounds
- Death sound

**Concepts Introduced:**
- Action sound palette
- Distinctive per action
- Appropriate feedback
- Sound priority

**Code Written:**
- Jump whoosh sound
- Duck/slide sound
- Collection sparkle sound
- Death crash sound

**What the Learner Sees:**
Every action has audio feedback - whoosh on jump, sparkle on collect!

---

### Unit 37: Background Music

**Learning Objectives:**
- Running music track
- Energetic tempo
- Speed sync option

**Concepts Introduced:**
- Background music during gameplay
- Energy appropriate to action
- Tempo variation with speed
- Music/effects balance

**Code Written:**
- Compose running music
- Music playback routine
- Optional tempo scaling
- Voice allocation

**What the Learner Sees:**
Energetic music drives gameplay! Tempo can increase with speed.

---

### Unit 38: Visual Feedback - Near Miss

**Learning Objectives:**
- Flash on close calls
- Reward risky play
- Tension indicator

**Concepts Introduced:**
- Near-miss detection
- Brief screen flash
- Audio cue
- Player engagement

**Code Written:**
- Detect close pass
- Flash effect
- Audio cue
- Near-miss counter

**What the Learner Sees:**
Barely miss obstacle - screen flashes! Shows how close that was!

---

### Unit 39: Death Animation Polish

**Learning Objectives:**
- Elaborate death sequence
- Tumble animation
- Impact effects

**Concepts Introduced:**
- Multi-frame death animation
- Particle effects
- Screen shake
- Emotional impact

**Code Written:**
- Death tumble frames
- Particle spawn
- Screen shake effect
- Sound accompaniment

**What the Learner Sees:**
Dramatic death! Runner tumbles, particles fly, screen shakes - impactful!

---

### Unit 40: Distance Milestones

**Learning Objectives:**
- Celebrate distance achievements
- Milestone markers
- Progress feedback

**Concepts Introduced:**
- Distance thresholds
- Celebration effects
- Milestone sound
- Progress motivation

**Code Written:**
- Track distance milestones
- Celebration effect at milestone
- Sound fanfare
- Milestone display

**What the Learner Sees:**
Hit 1000m - fanfare plays! Milestone achievements celebrated.

---

### Unit 41: Terrain Themes

**Learning Objectives:**
- Visual theme zones
- Colour/character changes
- Fresh presentation

**Concepts Introduced:**
- Theme zones (forest, desert, snow)
- Character set variations
- Colour scheme changes
- Transition effects

**Code Written:**
- Multiple character sets
- Theme colour tables
- Zone-based theme selection
- Smooth transitions

**What the Learner Sees:**
Different zones have different themes - green forest, yellow desert, white snow!

---

### Unit 42: Theme Transitions

**Learning Objectives:**
- Smooth zone transitions
- Gradual colour shift
- Seamless change

**Concepts Introduced:**
- Transition timing
- Gradual colour fade
- Character swap timing
- Seamless appearance

**Code Written:**
- Transition detection
- Colour interpolation
- Character swap on screen edge
- Smooth visual change

**What the Learner Sees:**
Themes blend seamlessly - forest gradually becomes desert!

---

### Unit 43: Title Screen Polish

**Learning Objectives:**
- Professional title presentation
- Demo run in background
- High score display

**Concepts Introduced:**
- Animated title
- Background gameplay
- High scores
- Attract loop

**Code Written:**
- Title logo animation
- Demo run behind title
- High score display
- Fire to start

**What the Learner Sees:**
Impressive title screen - logo animates over running gameplay demo!

---

### Unit 44: High Score System

**Learning Objectives:**
- Track best distances
- Initial entry
- Persistence

**Concepts Introduced:**
- Distance as score
- Top scores list
- Initial entry UI
- Save/load

**Code Written:**
- High score checking
- Initial entry screen
- Score table management
- File operations

**What the Learner Sees:**
Beat your best! High scores persist - compete against yourself!

**Reference to Invader Wave:**
"Same high score system from Invader Wave, now tracking distance instead of points."

---

### Unit 45: Statistics Screen

**Learning Objectives:**
- Track lifetime stats
- Total distance, runs, deaths
- Achievement feel

**Concepts Introduced:**
- Lifetime statistics
- Running totals
- Statistics display
- Persistence

**Code Written:**
- Stats data structure
- Increment during play
- Display screen
- Save/load stats

**What the Learner Sees:**
Statistics show lifetime play - total kilometres run, deaths, best distance!

---

### Unit 46: Pause Functionality

**Learning Objectives:**
- Pause game mid-run
- Resume without loss
- Pause menu

**Concepts Introduced:**
- Pause state
- Game freeze
- Resume capability
- Pause indicator

**Code Written:**
- Pause detection (RUN/STOP key)
- Freeze game loop
- Pause display
- Resume on keypress

**What the Learner Sees:**
Press pause - game freezes! Press again to resume exactly where you were.

---

### Unit 47: Difficulty Options

**Learning Objectives:**
- Selectable difficulty
- Easy/Normal/Hard
- Accessibility

**Concepts Introduced:**
- Difficulty presets
- Starting parameters
- Score modifier
- Player choice

**Code Written:**
- Difficulty selection UI
- Parameter tables
- Apply at game start
- Score multiplier per difficulty

**What the Learner Sees:**
Choose difficulty before run - Easy to learn, Hard for experts!

---

### Unit 48: Game Over Polish

**Learning Objectives:**
- Statistics on game over
- Best run comparison
- Retry flow

**Concepts Introduced:**
- Run statistics display
- Personal best comparison
- Quick retry
- Return to title option

**Code Written:**
- Game over display
- This run stats
- Compare to best
- Retry/quit options

**What the Learner Sees:**
Game over shows your run stats - distance, collectibles, near misses. New best? Retry instantly!

---

## Phase 4: Mastery (Units 49-64)
*Optimization, advanced mechanics, and professional polish.*

### Unit 49: Performance Profiling

**Learning Objectives:**
- Profile scroll performance
- Identify tight spots
- Measure frame budget

**Concepts Introduced:**
- Raster timing measurement
- Frame budget analysis
- Scroll + update cost
- Optimization targets

**Code Written:**
- Timing display
- Measure major routines
- Document results
- Plan optimizations

**What the Learner Sees:**
Debug display shows where CPU time goes - learn what's expensive!

---

### Unit 50: Scroll Optimization

**Learning Objectives:**
- Optimize screen shift
- Minimize CPU usage
- Rock-solid performance

**Concepts Introduced:**
- Self-modifying code for speed
- Page-aligned buffers
- Unrolled shifts
- Maximum efficiency

**Code Written:**
- Optimized shift routine
- Self-modifying where helpful
- Tight inner loop
- Measure improvement

**What the Learner Sees:**
(Performance improvement - absolutely smooth scrolling.)

---

### Unit 51: Colour RAM Optimization

**Learning Objectives:**
- Optimize colour shift
- Match screen performance
- Complete optimization

**Concepts Introduced:**
- Same techniques applied to colour
- Parallel where possible
- Total shift optimized

**Code Written:**
- Optimized colour shift
- Combined optimization
- Measure total
- Verify improvement

**What the Learner Sees:**
(Further performance gains - more headroom for effects.)

---

### Unit 52: Advanced Obstacles - Moving

**Learning Objectives:**
- Obstacles that move
- Vertical movement
- Timing challenge

**Concepts Introduced:**
- Moving obstacle sprites
- Vertical oscillation
- Timing windows
- Increased challenge

**Code Written:**
- Moving obstacle sprite
- Oscillation pattern
- Timing-based collision
- Fair but challenging

**What the Learner Sees:**
Some obstacles move up and down! Must time jump precisely!

---

### Unit 53: Combo System

**Learning Objectives:**
- Chain collectibles for bonus
- Combo counter
- Risk/reward

**Concepts Introduced:**
- Combo chain mechanic
- Combo timer
- Multiplying bonus
- Combo display

**Code Written:**
- Combo counter
- Timer between collections
- Escalating multiplier
- Combo display

**What the Learner Sees:**
Chain pickups for combos! Multiplier grows with consecutive grabs!

---

### Unit 54: Boss Segments

**Learning Objectives:**
- Special boss sections
- Different gameplay
- Milestone challenges

**Concepts Introduced:**
- Boss segment trigger
- Modified rules
- Boss completion bonus
- Return to normal

**Code Written:**
- Boss segment detection
- Boss gameplay mode
- Completion handling
- Transition effects

**What the Learner Sees:**
Every 2000m - boss segment! Survive the gauntlet for huge bonus!

---

### Unit 55: Daily Challenge Concept

**Learning Objectives:**
- Seeded daily run
- Same run for everyone
- Competition element

**Concepts Introduced:**
- Date-based seed
- Consistent generation
- Daily score comparison
- Community competition

**Code Written:**
- Date to seed conversion
- Fixed generation mode
- Daily run designation
- Score marking

**What the Learner Sees:**
Daily Challenge mode - same run every day! Compete for best daily score.

---

### Unit 56: Screen Effects

**Learning Objectives:**
- Special visual effects
- Speed blur
- Danger warning

**Concepts Introduced:**
- Screen effect overlays
- Speed-based effects
- Danger indicators
- Visual communication

**Code Written:**
- Speed blur effect
- Danger flash effect
- Effect layering
- Performance-safe effects

**What the Learner Sees:**
Visual effects enhance gameplay - blur at high speed, flash for danger!

---

### Unit 57: Music Variation

**Learning Objectives:**
- Multiple music tracks
- Zone-appropriate music
- Theme consistency

**Concepts Introduced:**
- Multiple compositions
- Zone-based selection
- Smooth transitions
- Variety over long play

**Code Written:**
- Additional music tracks
- Zone music mapping
- Track transitions
- Consistent energy

**What the Learner Sees:**
Different zones have different music - forest theme, desert theme, etc.!

---

### Unit 58: Endless Mode Polish

**Learning Objectives:**
- True endless play
- Cycling themes
- Sustained engagement

**Concepts Introduced:**
- Endless with variety
- Theme cycling
- Difficulty plateau
- Engagement maintenance

**Code Written:**
- Theme cycle logic
- Difficulty ceiling
- Variety maintenance
- Long-term engagement

**What the Learner Sees:**
Game never ends - themes cycle, challenge stays fresh, play forever!

---

### Unit 59: Checkpoint System

**Learning Objectives:**
- Optional checkpoints
- Continue from distance
- Accessibility option

**Concepts Introduced:**
- Checkpoint storage
- Continue mechanic
- Score penalty for continue
- Accessibility vs. purity

**Code Written:**
- Checkpoint saving
- Continue option
- Score penalty
- Option to disable

**What the Learner Sees:**
Hit checkpoint - can continue from there! (Optional - purists can disable.)

---

### Unit 60: Controller Options

**Learning Objectives:**
- Multiple control schemes
- Keyboard support
- Accessibility

**Concepts Introduced:**
- Control scheme options
- Keyboard mapping
- One-button mode
- Player preference

**Code Written:**
- Control configuration
- Keyboard controls
- One-button auto-run mode
- Save preferences

**What the Learner Sees:**
Options for controls - joystick, keyboard, or simplified mode!

---

### Unit 61: Visual Polish Pass

**Learning Objectives:**
- Final visual refinements
- Consistency check
- Professional appearance

**Concepts Introduced:**
- Visual consistency
- Colour harmony
- Animation smoothness
- Polish details

**Code Written:**
- Colour adjustments
- Animation tweaks
- Consistency fixes
- Final details

**What the Learner Sees:**
Everything polished - consistent, smooth, professional.

---

### Unit 62: Audio Polish Pass

**Learning Objectives:**
- Final audio refinements
- Mix balancing
- Complete soundscape

**Concepts Introduced:**
- Audio mix review
- Volume balancing
- Effect/music balance
- Final adjustments

**Code Written:**
- Volume adjustments
- Mix refinements
- Final audio tweaks
- Complete soundscape

**What the Learner Sees:**
Audio perfectly mixed - footsteps, music, effects all clear and balanced.

---

### Unit 63: Memory Map Review

**Learning Objectives:**
- Review memory usage
- Optimize allocation
- Document layout

**Concepts Introduced:**
- Memory map documentation
- Optimization opportunities
- Clean architecture
- Future-proof design

**Code Written:**
- Memory map documentation
- Optimization where possible
- Clean allocation
- Final layout

**What the Learner Sees:**
(Documentation - clean memory architecture.)

---

### Unit 64: Release Build

**Learning Objectives:**
- Create final release
- Remove debug code
- Distribution ready

**Concepts Introduced:**
- Release build process
- Debug removal
- Final testing
- Version marking

**Code Written:**
- Remove debug displays
- Optimize startup
- Final integration
- Create release PRG

**What the Learner Sees:**
Complete, polished Scroll Runner! First proper scrolling game, ready for distribution.

---

## Summary

**Scroll Runner** introduces the crucial skill of hardware scrolling:

**Phase 1 (Foundation):** Core scrolling - hardware register, screen shift, colour RAM, basic runner.

**Phase 2 (Expansion):** Content - terrain variety, obstacles, power-ups, procedural generation.

**Phase 3 (Polish):** Feel - parallax, sound design, themes, visual feedback.

**Phase 4 (Mastery):** Professional quality - optimization, advanced features, release build.

### Skills Transferred Forward

The following skills debut in Scroll Runner and will be applied in future games:

1. **Hardware scroll registers** → Night Raid, Parallax Patrol, Mega Blaster
2. **Screen buffer management** → All scrolling games
3. **Colour RAM scrolling** → All coloured scrolling games
4. **Double buffering** → Night Raid, Parallax Patrol
5. **Procedural generation** → Dungeon Crawl (room generation), many others
6. **Raster colour splits** → Raster Rider (essential), many others
7. **Parallax backgrounds** → Parallax Patrol (advanced), Mega Blaster

### Game Specifications

- **Scroll type:** Hardware horizontal (VIC-II $D016)
- **Obstacles:** Ground level (jump), head level (duck), pits (jump)
- **Power-ups:** 3 types (magnet, invincibility, multiplier)
- **Themes:** 4 visual themes (forest, desert, snow, night)
- **Parallax layers:** 3 (background, midground, foreground)
- **Music tracks:** 4 (one per theme)
- **Score:** Distance-based with collectible bonuses
- **Features:** High scores, statistics, checkpoints, daily challenge mode
