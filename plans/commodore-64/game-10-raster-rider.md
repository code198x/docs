# Raster Rider: 64-Unit Outline

**Game:** 10 of 16
**Platform:** Commodore 64
**Units:** 64
**Concept:** Racing game with pseudo-3D road using raster effects. OutRun/Pole Position style racing with perspective road, roadside objects, and opponent cars.

---

## Skills Applied from Previous Games

| Skill | Learned In | Application in Raster Rider |
|-------|-----------|---------------------------|
| SID fundamentals | SID Symphony | Engine sound, music |
| Hardware sprites | Starfield | Player car, opponents, roadside |
| Joystick input | Starfield | Steering control |
| Speed ramping | Brick Basher | Speed/difficulty |
| Timer systems | Various | Race timer |
| Raster interrupts | Scroll Runner | Road rendering |
| Colour RAM manipulation | Scroll Runner | Road colours |
| Sprite multiplexing | Sprite Storm | Roadside objects, opponent cars |
| Y-sorted sprites | Sprite Storm | Depth-correct object display |
| Raster-precise timing | Sprite Storm | Stable road rendering |

## New Skills Introduced

| Skill | Units | Description |
|-------|-------|-------------|
| Perspective mathematics | 5-8 | Z-depth to screen position |
| Road curve rendering | 9-12 | Curve offset per raster line |
| Road width perspective | 13-16 | Narrower at horizon |
| Multi-line raster splits | 17-20 | Colour change every few lines |
| Horizon rendering | 21-24 | Sky/road boundary |
| Roadside scaling | 25-28 | Object size by distance |
| Speed-based scrolling | 29-32 | Road stripe movement |
| Track design | 37-40 | Curve sequence data |
| Hill simulation | 41-44 | Vertical perspective |

---

## Phase 1: Foundation (Units 1-16)
*Core mechanics: perspective road, player car, basic racing.*

### Unit 1: Pseudo-3D Racing Concept

**Learning Objectives:**
- Understand pseudo-3D road rendering
- Analyse OutRun/Pole Position techniques
- Plan implementation approach

**Concepts Introduced:**
- No true 3D on C64
- Raster effects create illusion
- Road narrows toward horizon
- Colour banding creates stripes

**Code Written:**
- Design document
- Screen layout planning
- Raster technique outline
- Reference analysis

**What the Learner Sees:**
Understanding how pseudo-3D racing works - the illusion explained.

---

### Unit 2: Screen Layout

**Learning Objectives:**
- Divide screen for racing
- Sky area, road area
- UI positioning

**Concepts Introduced:**
- Top third: sky/horizon
- Bottom two-thirds: road
- HUD position
- Render order

**Code Written:**
- Screen zone definitions
- Initial colours
- UI area reservation
- Layout constants

**What the Learner Sees:**
Screen divided into zones - sky blue above, road area below.

---

### Unit 3: Basic Raster Setup

**Learning Objectives:**
- Multiple raster interrupts
- Change colours per zone
- Stable timing

**Concepts Introduced:**
- Multiple IRQ points
- Chain interrupts
- Zone boundaries
- Colour register changes

**Code Written:**
- Multiple raster IRQs
- Zone colour changes
- Chain linking
- Stable timing

**What the Learner Sees:**
Sky is blue, road is grey - colours change at correct raster lines.

**Reference to Scroll Runner:**
"Raster techniques from Scroll Runner, but now with many more split points."

---

### Unit 4: Road Stripe Pattern

**Learning Objectives:**
- Alternating road colours
- Stripe pattern
- Movement preparation

**Concepts Introduced:**
- Road stripe colours
- Alternating pattern
- Stripe height per zone
- Pattern data structure

**Code Written:**
- Stripe colour table
- Raster-based application
- Pattern generation
- Multiple stripes visible

**What the Learner Sees:**
Road has alternating stripe pattern - white/grey stripes across the road!

---

### Unit 5: Stripe Animation

**Learning Objectives:**
- Move stripes toward player
- Speed simulation
- Infinite road illusion

**Concepts Introduced:**
- Stripe offset variable
- Offset changes stripe start
- Faster change = faster speed
- Cycling creates movement

**Code Written:**
- Stripe offset tracking
- Offset increment per frame
- Cycle management
- Speed variable

**What the Learner Sees:**
Road stripes move toward player - creates sense of speed!

---

### Unit 6: Speed Control

**Learning Objectives:**
- Accelerator input
- Speed variable
- Stripe speed relation

**Concepts Introduced:**
- Acceleration on button
- Deceleration when released
- Maximum speed
- Speed-to-stripe mapping

**Code Written:**
- Speed variable
- Acceleration/deceleration
- Speed limits
- Stripe rate = f(speed)

**What the Learner Sees:**
Hold fire to accelerate - stripes move faster! Release to slow down.

**Reference to Starfield:**
"Button input from Starfield, now controlling speed rather than firing."

---

### Unit 7: Perspective Road Width

**Learning Objectives:**
- Road narrows toward horizon
- Width per raster line
- Perspective mathematics

**Concepts Introduced:**
- Far = narrow, near = wide
- Width lookup table
- Raster line → width mapping
- Screen-space perspective

**Code Written:**
- Width calculation
- Lookup table generation
- Apply to rendering
- Edge position calculation

**What the Learner Sees:**
Road gets narrower toward the top - perspective effect!

---

### Unit 8: Road Edges

**Learning Objectives:**
- Render road edges
- Edge colour/pattern
- Clear boundary

**Concepts Introduced:**
- Edge position per line
- Edge rendering technique
- Colour for edges
- Visual boundary

**Code Written:**
- Edge position lookup
- Edge character/colour
- Render in raster
- Clear road boundary

**What the Learner Sees:**
Road has clear edges - red/white chevron pattern or solid line.

---

### Unit 9: Player Car Sprite

**Learning Objectives:**
- Create player car
- Fixed screen position
- Visual representation

**Concepts Introduced:**
- Player car at screen bottom-centre
- Car sprite design
- Bonnet view style
- Fixed Y, variable X

**Code Written:**
- Player car sprite
- Position at bottom
- Fixed Y position
- Initial X at centre

**What the Learner Sees:**
Player car visible at bottom of screen - bonnet view racing!

---

### Unit 10: Steering Control

**Learning Objectives:**
- Left/right steering
- Car X position
- Road-relative position

**Concepts Introduced:**
- Steering input
- Car X movement
- Road-relative positioning
- Screen boundaries

**Code Written:**
- Joystick left/right
- Car X position update
- Boundary clamping
- Smooth movement

**What the Learner Sees:**
Steer left and right - car moves across the road!

---

### Unit 11: Road Curves - Concept

**Learning Objectives:**
- Understand curve rendering
- Offset per raster line
- Curve data format

**Concepts Introduced:**
- Curve = horizontal offset per line
- Offset increases toward horizon
- Curve direction (left/right)
- Curve intensity

**Code Written:**
- Curve offset concept
- Test offset application
- Curve direction variable
- Document technique

**What the Learner Sees:**
Understanding how curves work - offset creates the bend illusion.

---

### Unit 12: Road Curves - Implementation

**Learning Objectives:**
- Apply curve offset to road
- Smooth curve appearance
- Variable curve intensity

**Concepts Introduced:**
- Curve offset table
- Apply to edge positions
- Curve intensity scaling
- Smooth appearance

**Code Written:**
- Curve offset calculation
- Apply to road rendering
- Intensity variable
- Test curves

**What the Learner Sees:**
Road curves! Left and right bends appear correctly with perspective!

---

### Unit 13: Track Data Format

**Learning Objectives:**
- Define track segment data
- Segment types (straight, curve)
- Track length

**Concepts Introduced:**
- Segment-based track
- Segment type and length
- Curve direction and intensity
- Track sequencing

**Code Written:**
- Track data structure
- Segment definitions
- Sample track data
- Segment reading

**What the Learner Sees:**
(Data format ready - track plays through segments.)

---

### Unit 14: Track Progression

**Learning Objectives:**
- Progress through track segments
- Segment transitions
- Distance tracking

**Concepts Introduced:**
- Distance counter
- Segment boundary detection
- Next segment loading
- Smooth transitions

**Code Written:**
- Distance tracking
- Segment progress
- Transition handling
- New segment loading

**What the Learner Sees:**
Road changes! Straights lead to curves lead to straights - track flows!

---

### Unit 15: Race Timer

**Learning Objectives:**
- Implement race timer
- Time limit gameplay
- Timer display

**Concepts Introduced:**
- Countdown timer
- Time = resource
- Game over on timeout
- Time display format

**Code Written:**
- Timer countdown
- Timer display
- Timeout detection
- Game over trigger

**What the Learner Sees:**
Timer counts down! Reach checkpoints before time runs out!

---

### Unit 16: Complete Basic Racing

**Learning Objectives:**
- Integrate all systems
- Playable racing game
- Foundation complete

**Concepts Introduced:**
- Complete game loop
- Title screen
- Game over
- Basic playable racer

**Code Written:**
- Title screen
- Game integration
- Game over screen
- Restart flow

**What the Learner Sees:**
Complete racing game! Perspective road, steering, acceleration, timer. Playable!

---

## Phase 2: Expansion (Units 17-32)
*Roadside objects, opponent cars, checkpoints.*

### Unit 17: Multi-Line Raster Splits

**Learning Objectives:**
- More raster splits per frame
- Finer colour banding
- Enhanced perspective

**Concepts Introduced:**
- Raster split per N lines
- Tighter stripe banding
- Performance trade-offs
- Enhanced visual

**Code Written:**
- Increased split count
- Tighter stripe pattern
- Performance management
- Visual enhancement

**What the Learner Sees:**
Road stripes more detailed - finer banding creates better perspective!

---

### Unit 18: Colour Cycling for Speed

**Learning Objectives:**
- Colour changes simulate speed
- Palette rotation
- Speed feedback

**Concepts Introduced:**
- Colour palette cycling
- Rotation per frame
- Speed-based rate
- Visual speed cue

**Code Written:**
- Colour table rotation
- Speed-based rate
- Apply to road colours
- Visual speed effect

**What the Learner Sees:**
Colours cycle faster at high speed - visual speed feedback!

---

### Unit 19: Horizon Line

**Learning Objectives:**
- Define horizon position
- Sky/road boundary
- Visual grounding

**Concepts Introduced:**
- Horizon Y position
- Raster boundary
- Sky above, road below
- Visual anchor

**Code Written:**
- Horizon definition
- Raster split at horizon
- Sky rendering above
- Clean boundary

**What the Learner Sees:**
Clean horizon line separates sky from road - visual grounding.

---

### Unit 20: Horizon Hills

**Learning Objectives:**
- Hills behind horizon
- Character graphics
- Depth perception

**Concepts Introduced:**
- Hill silhouette characters
- Slow parallax scroll
- Depth enhancement
- Visual interest

**Code Written:**
- Hill characters
- Horizontal scroll
- Speed relationship
- Visual depth

**What the Learner Sees:**
Hills scroll behind horizon - depth and scenery!

---

### Unit 21: Roadside Object Framework

**Learning Objectives:**
- Objects beside road
- Scaling by distance
- Sprite management

**Concepts Introduced:**
- Roadside object concept
- Y-position = distance
- Scale by Y
- Sprite allocation

**Code Written:**
- Object data structure
- Y-based positioning
- Scale concept
- Sprite assignment

**What the Learner Sees:**
(Framework ready for objects.)

---

### Unit 22: Roadside - Trees

**Learning Objectives:**
- Trees beside road
- Pass by at speed
- Visual rhythm

**Concepts Introduced:**
- Tree sprite
- Placement pattern
- Pass-by motion
- Visual rhythm

**Code Written:**
- Tree sprite data
- Spawn logic
- Movement with road
- Scaling application

**What the Learner Sees:**
Trees whoosh past! Roadside objects add sense of speed!

---

### Unit 23: Roadside - Signs

**Learning Objectives:**
- Road signs
- Curve warnings
- Gameplay information

**Concepts Introduced:**
- Sign sprites
- Curve warning signs
- Information display
- Visual variety

**Code Written:**
- Sign sprites
- Warning placement
- Information display
- Visual variety

**What the Learner Sees:**
Road signs warn of curves! Arrow signs show bend direction.

---

### Unit 24: Roadside Scaling

**Learning Objectives:**
- Object size by distance
- Multiple sprite sizes
- Perspective accuracy

**Concepts Introduced:**
- Sprite scaling
- Size lookup by Y
- Multiple sprite versions
- Smooth scaling

**Code Written:**
- Scale lookup table
- Size selection
- Sprite version switching
- Smooth appearance

**What the Learner Sees:**
Objects grow as they approach! Trees start small, grow as they pass!

**Reference to Sprite Storm:**
"Y-sorted sprites from Sprite Storm, now with scaling for perspective."

---

### Unit 25: Opponent Car Framework

**Learning Objectives:**
- Other cars on track
- Collision obstacles
- Racing competition

**Concepts Introduced:**
- Opponent data structure
- Track position (Z depth)
- Lateral position
- Collision target

**Code Written:**
- Opponent structure
- Position tracking
- Sprite rendering
- Framework ready

**What the Learner Sees:**
(Framework for opponents ready.)

---

### Unit 26: Opponent Car Rendering

**Learning Objectives:**
- Display opponent cars
- Scale by distance
- Road-relative position

**Concepts Introduced:**
- Opponent sprites
- Z-to-Y mapping
- Scale selection
- Road offset application

**Code Written:**
- Opponent rendering
- Scale by Z
- Position calculation
- Sprite display

**What the Learner Sees:**
Other cars on the road! They scale correctly with distance!

---

### Unit 27: Opponent Movement

**Learning Objectives:**
- Opponents move relative to player
- Overtaking/being overtaken
- Track-relative motion

**Concepts Introduced:**
- Relative Z movement
- Faster = approach
- Slower = recede
- Overtaking mechanics

**Code Written:**
- Relative movement
- Speed difference handling
- Approach/recede logic
- Smooth motion

**What the Learner Sees:**
Opponents move! Faster cars approach, slower cars recede!

---

### Unit 28: Opponent Collision

**Learning Objectives:**
- Crash on opponent contact
- Speed loss/crash
- Avoidance gameplay

**Concepts Introduced:**
- Collision detection
- Crash handling
- Speed penalty
- Avoidance skill

**Code Written:**
- Collision detection
- Crash handling
- Speed reduction
- Spin effect

**What the Learner Sees:**
Hit opponent - crash! Spin out, lose speed, get back on track!

---

### Unit 29: Checkpoint System

**Learning Objectives:**
- Checkpoints extend time
- Race structure
- Progress milestones

**Concepts Introduced:**
- Checkpoint distance markers
- Time extension
- Progress indication
- Race structure

**Code Written:**
- Checkpoint distances
- Time extension on reach
- Progress display
- Checkpoint celebration

**What the Learner Sees:**
Reach checkpoint - time extended! Keep racing!

---

### Unit 30: Track Roadside Variation

**Learning Objectives:**
- Different roadside per segment
- Visual themes
- Track variety

**Concepts Introduced:**
- Segment-based roadside
- Object type selection
- Theme consistency
- Visual variety

**Code Written:**
- Segment roadside data
- Object spawning per type
- Theme application
- Variety management

**What the Learner Sees:**
Different track sections have different scenery - forest, desert, city!

---

### Unit 31: Night/Day Transition

**Learning Objectives:**
- Time-of-day changes
- Colour scheme shifts
- Visual variety

**Concepts Introduced:**
- Colour palette swaps
- Day/night schemes
- Transition effects
- Visual interest

**Code Written:**
- Multiple colour schemes
- Scheme selection
- Transition timing
- Visual variety

**What the Learner Sees:**
Track transitions day to night! Colour scheme changes dramatically!

---

### Unit 32: Complete Track

**Learning Objectives:**
- Design full race track
- Balanced challenge
- Complete race

**Concepts Introduced:**
- Full track design
- Challenge balance
- Checkpoint placement
- Complete experience

**Code Written:**
- Full track data
- Challenge tuning
- Checkpoint spacing
- Complete race

**What the Learner Sees:**
Complete race track! Multiple sections, checkpoints, finish line!

---

## Phase 3: Polish (Units 33-48)
*Effects, sound, visual feedback, and "juice".*

### Unit 33: Engine Sound

**Learning Objectives:**
- Continuous engine audio
- Pitch by speed
- Acceleration feel

**Concepts Introduced:**
- Engine noise generation
- Pitch modulation
- Speed-to-pitch mapping
- Continuous sound

**Code Written:**
- Engine sound routine
- Pitch control
- Speed relationship
- Mix management

**What the Learner Sees:**
Engine roars! Pitch rises with speed - visceral acceleration!

**Reference to SID Symphony:**
"SID noise and oscillator techniques for realistic engine sound."

---

### Unit 34: Crash Sound

**Learning Objectives:**
- Impact audio
- Dramatic crashes
- Audio feedback

**Concepts Introduced:**
- Crash sound design
- Impact effects
- Recovery sounds
- Drama creation

**Code Written:**
- Crash effects
- Impact sounds
- Recovery audio
- Sound priority

**What the Learner Sees:**
Crashes sound impactful! Dramatic audio for collisions.

---

### Unit 35: Music - Racing Theme

**Learning Objectives:**
- Driving music
- Energy appropriate
- Iconic racing audio

**Concepts Introduced:**
- Racing game music
- Energy and tempo
- SID composition
- Voice allocation

**Code Written:**
- Racing music composition
- Music playback
- Voice management
- Mix balance

**What the Learner Sees:**
Energetic racing music drives the gameplay! OutRun vibes!

---

### Unit 36: HUD Enhancement

**Learning Objectives:**
- Clear race information
- Speed display
- Position/time display

**Concepts Introduced:**
- Speedometer visual
- Position display
- Time display
- Information hierarchy

**Code Written:**
- Speedometer graphics
- Position indicator
- Time formatting
- Clear HUD layout

**What the Learner Sees:**
Professional HUD - speed, position, time all clearly displayed!

---

### Unit 37: Gear System

**Learning Objectives:**
- Manual gear changes
- Gear-based acceleration
- Skill element

**Concepts Introduced:**
- Gear states (Low/High)
- Acceleration per gear
- Optimal shifting
- Player skill

**Code Written:**
- Gear variable
- Shift mechanic
- Acceleration curves
- Gear display

**What the Learner Sees:**
Shift gears! Low for acceleration, high for top speed!

---

### Unit 38: Track Design - Multiple Tracks

**Learning Objectives:**
- Multiple race tracks
- Track selection
- Variety

**Concepts Introduced:**
- Multiple track data
- Track selection UI
- Difficulty variety
- Visual themes

**Code Written:**
- Additional track data
- Selection screen
- Track loading
- Visual themes

**What the Learner Sees:**
Choose your track! Multiple routes with different challenges!

---

### Unit 39: Weather Effects

**Learning Objectives:**
- Rain effect
- Handling changes
- Visual effect

**Concepts Introduced:**
- Rain sprite/character effect
- Handling modification
- Visual atmosphere
- Challenge variety

**Code Written:**
- Rain effect rendering
- Handling adjustment
- Wet road visuals
- Atmosphere creation

**What the Learner Sees:**
Rain! Wet conditions - harder handling, atmospheric visuals!

---

### Unit 40: Tunnel Sections

**Learning Objectives:**
- Tunnel segments
- Different rendering
- Variety injection

**Concepts Introduced:**
- Tunnel segment type
- Modified rendering
- Lighting changes
- Visual variety

**Code Written:**
- Tunnel detection
- Modified rendering
- Lighting effect
- Transition handling

**What the Learner Sees:**
Tunnel sections! Different visuals, brief darkness, then back to daylight!

---

### Unit 41: Title Screen

**Learning Objectives:**
- Professional title
- Demo mode
- Options

**Concepts Introduced:**
- Animated title
- Demo playback
- Track selection
- Options menu

**Code Written:**
- Title animation
- Demo mode
- Menu system
- Option handling

**What the Learner Sees:**
Impressive title with animation and demo - professional presentation!

---

### Unit 42: High Score System

**Learning Objectives:**
- Best times
- Per-track records
- Persistence

**Concepts Introduced:**
- Time-based leaderboard
- Per-track records
- Initial entry
- Save/load

**Code Written:**
- Time leaderboards
- Per-track storage
- Entry screen
- Persistence

**What the Learner Sees:**
Best times saved! Compete against your records on each track!

---

### Unit 43: Ghost Mode

**Learning Objectives:**
- Race against recording
- Ghost car
- Self-competition

**Concepts Introduced:**
- Input recording
- Ghost playback
- Competition with self
- Target chasing

**Code Written:**
- Input recording
- Ghost rendering
- Playback system
- Storage

**What the Learner Sees:**
Race against your ghost! See your best run as a target to beat!

---

### Unit 44: Difficulty Options

**Learning Objectives:**
- Accessibility settings
- Challenge options
- Player choice

**Concepts Introduced:**
- Difficulty levels
- Parameter adjustment
- Accessibility value
- Player accommodation

**Code Written:**
- Difficulty settings
- Parameter tables
- Application
- Save preferences

**What the Learner Sees:**
Difficulty options - Easy for beginners, Hard for experts!

---

### Unit 45: Statistics

**Learning Objectives:**
- Track statistics
- Lifetime records
- Progress tracking

**Concepts Introduced:**
- Racing statistics
- Lifetime totals
- Display screen
- Achievement tracking

**Code Written:**
- Statistics tracking
- Display formatting
- Persistence
- Achievements

**What the Learner Sees:**
Statistics show racing career - races completed, best times, crashes!

---

### Unit 46: Instant Replay

**Learning Objectives:**
- Brief replay on crash
- Dramatic effect
- Feedback system

**Concepts Introduced:**
- State recording
- Brief replay
- Slow-motion option
- Drama enhancement

**Code Written:**
- State recording ring
- Replay playback
- Slow-motion
- Trigger on crash

**What the Learner Sees:**
Crash triggers brief replay - see what went wrong in slow-motion!

---

### Unit 47: Visual Polish

**Learning Objectives:**
- Final visual refinements
- Consistency check
- Professional quality

**Concepts Introduced:**
- Visual consistency
- Colour harmony
- Effect refinement
- Professional look

**Code Written:**
- Visual adjustments
- Consistency fixes
- Effect polish
- Final details

**What the Learner Sees:**
Everything polished and consistent - professional appearance.

---

### Unit 48: Audio Polish

**Learning Objectives:**
- Final audio refinements
- Mix balance
- Complete soundscape

**Concepts Introduced:**
- Audio mix review
- Engine/music balance
- Effect clarity
- Final tuning

**Code Written:**
- Mix adjustments
- Balance refinement
- Final audio touches

**What the Learner Sees:**
Audio perfectly balanced - engine, music, effects all clear!

---

## Phase 4: Mastery (Units 49-64)
*Optimization, advanced techniques, and professional polish.*

### Unit 49: Hill Simulation

**Learning Objectives:**
- Vertical road variation
- Uphill/downhill
- 3D enhancement

**Concepts Introduced:**
- Horizon Y variation
- Perspective adjustment
- Hill feel
- Enhanced depth

**Code Written:**
- Horizon variation
- Hill segment type
- Perspective adjustment
- Visual enhancement

**What the Learner Sees:**
Hills! Road goes up and down - enhanced 3D feeling!

---

### Unit 50: Fork in Road

**Learning Objectives:**
- Track branching
- Route choice
- Replayability

**Concepts Introduced:**
- Branch points
- Route selection
- Merge points
- Route variety

**Code Written:**
- Branch detection
- Route handling
- Merge logic
- Visual indication

**What the Learner Sees:**
Choose your path! Track branches - different routes to the finish!

---

### Unit 51: Multiplayer Mode

**Learning Objectives:**
- Split-screen racing
- Two players
- Head-to-head competition

**Concepts Introduced:**
- Screen splitting
- Dual rendering
- Independent input
- Competition mode

**Code Written:**
- Split-screen setup
- Dual road rendering
- Two input streams
- Winner determination

**What the Learner Sees:**
Split-screen racing! Compete head-to-head with a friend!

---

### Unit 52: Performance Optimization

**Learning Objectives:**
- Optimize raster routines
- Maximum performance
- Stable framerate

**Concepts Introduced:**
- Raster optimization
- Cycle counting
- Stable timing
- Maximum efficiency

**Code Written:**
- Optimized rendering
- Timing verification
- Performance measurement
- Documentation

**What the Learner Sees:**
(Rock-solid performance - smooth gameplay.)

---

### Unit 53: Advanced Curves

**Learning Objectives:**
- S-curves
- Complex road shapes
- Track variety

**Concepts Introduced:**
- Compound curves
- S-bend data
- Smooth transitions
- Advanced road shapes

**Code Written:**
- S-curve handling
- Compound curve data
- Smooth rendering
- Visual verification

**What the Learner Sees:**
Complex curves! S-bends and compound turns challenge driving skills!

---

### Unit 54: Car Selection

**Learning Objectives:**
- Multiple car types
- Different handling
- Player choice

**Concepts Introduced:**
- Car types
- Handling parameters
- Sprite variations
- Player expression

**Code Written:**
- Car data structures
- Handling variations
- Sprite sets
- Selection UI

**What the Learner Sees:**
Choose your car! Different handling characteristics per vehicle!

---

### Unit 55: Championship Mode

**Learning Objectives:**
- Multi-track championship
- Points system
- Extended play

**Concepts Introduced:**
- Championship structure
- Point scoring
- Track sequence
- Winner determination

**Code Written:**
- Championship logic
- Point tracking
- Track sequence
- Results display

**What the Learner Sees:**
Championship mode! Race multiple tracks, earn points, become champion!

---

### Unit 56: AI Opponents

**Learning Objectives:**
- Computer-controlled racers
- Competitive AI
- Challenge without human

**Concepts Introduced:**
- AI driving logic
- Speed management
- Overtaking behaviour
- Challenge creation

**Code Written:**
- AI driver logic
- Speed control
- Line management
- Challenge tuning

**What the Learner Sees:**
AI racers! Computer opponents provide challenge in single-player!

---

### Unit 57: Traffic Mode

**Learning Objectives:**
- Non-racing traffic
- Obstacle avoidance
- Different gameplay

**Concepts Introduced:**
- Traffic vehicles
- Lane-based movement
- Collision avoidance
- Arcade mode

**Code Written:**
- Traffic spawning
- Lane behaviour
- Collision handling
- Mode variant

**What the Learner Sees:**
Traffic mode! Weave through civilian cars - different challenge!

---

### Unit 58: Bonus Stages

**Learning Objectives:**
- Special challenge segments
- Score opportunities
- Variety injection

**Concepts Introduced:**
- Bonus segment type
- Modified rules
- Score focus
- Brief variety

**Code Written:**
- Bonus detection
- Modified gameplay
- Score emphasis
- Return to normal

**What the Learner Sees:**
Bonus stage! Different rules, score opportunities, brief variety!

---

### Unit 59: End Sequence

**Learning Objectives:**
- Race completion reward
- Victory celebration
- Satisfying conclusion

**Concepts Introduced:**
- Finish line handling
- Victory sequence
- Results display
- Celebration effects

**Code Written:**
- Finish detection
- Victory sequence
- Results formatting
- Celebration effects

**What the Learner Sees:**
Cross the finish! Victory celebration, results display, satisfying completion!

---

### Unit 60: Memory Optimization

**Learning Objectives:**
- Optimize memory usage
- Track data compression
- Efficient storage

**Concepts Introduced:**
- Memory review
- Data compression
- Efficient structures
- Documentation

**Code Written:**
- Memory optimization
- Data compression
- Structure refinement
- Documentation

**What the Learner Sees:**
(Internal - more tracks possible with efficient storage.)

---

### Unit 61: Additional Tracks

**Learning Objectives:**
- More track content
- Visual themes
- Extended game

**Concepts Introduced:**
- Additional track designs
- Theme variety
- Challenge variety
- Content expansion

**Code Written:**
- New track data
- Visual themes
- Challenge balance
- Content integration

**What the Learner Sees:**
More tracks! Extended content provides replay value!

---

### Unit 62: Final Balancing

**Learning Objectives:**
- Difficulty balance
- Time tuning
- Fair challenge

**Concepts Introduced:**
- Balance testing
- Parameter tuning
- Fairness verification
- Challenge curve

**Code Written:**
- Parameter adjustments
- Balance refinement
- Test verification
- Documentation

**What the Learner Sees:**
(Fair, balanced challenge across all tracks.)

---

### Unit 63: Documentation

**Learning Objectives:**
- Document raster techniques
- Technical reference
- Teaching value

**Concepts Introduced:**
- Technical documentation
- Technique reference
- Teaching material
- Knowledge preservation

**Code Written:**
- Technical documentation
- Code comments
- Reference guide
- Example explanations

**What the Learner Sees:**
Complete documentation of pseudo-3D racing techniques!

---

### Unit 64: Release Build

**Learning Objectives:**
- Create final release
- Remove debug code
- Distribution ready

**Concepts Introduced:**
- Release process
- Debug removal
- Final packaging
- Distribution preparation

**Code Written:**
- Debug removal
- Optimization pass
- Final integration
- Release PRG

**What the Learner Sees:**
Complete Raster Rider! Pseudo-3D racing mastered, ready for distribution!

---

## Summary

**Raster Rider** teaches advanced raster techniques for pseudo-3D:

**Phase 1 (Foundation):** Core racing - perspective road, stripes, curves, basic gameplay.

**Phase 2 (Expansion):** Content - roadside objects, opponents, checkpoints, full tracks.

**Phase 3 (Polish):** Feel - engine sound, music, weather, visual effects.

**Phase 4 (Mastery):** Advanced - hills, forks, multiplayer, optimization.

### Skills Transferred Forward

The following skills debut or are significantly enhanced in Raster Rider:

1. **Advanced raster splits** → All games requiring complex raster work
2. **Perspective mathematics** → Isometric Quest (different projection)
3. **Object scaling** → Any game with depth
4. **Colour cycling** → Visual effects in future games
5. **Track/level data structures** → All subsequent games
6. **Split-screen rendering** → Arena Fighter (if applicable)

### Game Specifications

- **Rendering:** Pseudo-3D raster road with perspective
- **Objects:** Roadside (trees, signs), opponent cars
- **Tracks:** 6+ with different themes (forest, desert, city, night)
- **Segments:** Straights, curves, S-bends, hills, tunnels
- **Effects:** Day/night, rain/clear, colour cycling
- **Modes:** Time trial, championship, traffic mode
- **Players:** 1-2 (split-screen)
- **Features:** Ghost mode, instant replay, car selection
