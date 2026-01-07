# Brick Basher: 64-Unit Outline

**Game:** 5 of 16
**Platform:** Commodore 64
**Units:** 64
**Concept:** Breakout clone. Paddle, ball, bricks. Clear the screen to progress through increasingly challenging levels.

---

## Skills Applied from Previous Games

| Skill | Learned In | Application in Brick Basher |
|-------|-----------|---------------------------|
| SID fundamentals | SID Symphony | Sound effects for bounces, brick hits, power-ups |
| ADSR envelopes | SID Symphony | Distinctive sounds for different brick types |
| Game loop structure | SID Symphony | Main game timing and update cycle |
| Keyboard input | SID Symphony | Menu navigation, pause |
| Hardware sprites | Starfield | Paddle and ball as sprites |
| Joystick input | Starfield | Paddle control |
| Sprite collision | Starfield | Ball-paddle and ball-brick detection |
| Score display | Starfield | Score, lives, level display |
| Object management | Starfield | Multiple balls, power-ups |
| Custom character sets | Maze Raider | Brick graphics |
| Tile-based maps | Maze Raider | Brick grid layout |
| Tile collision | Maze Raider | Ball-to-brick collision |
| Physics simulation | Platform Panic | Ball velocity and movement |
| Animation frames | Platform Panic | Paddle stretch, brick destruction |

## New Skills Introduced

| Skill | Units | Description |
|-------|-------|-------------|
| Velocity vectors | 5-8 | Ball movement using dx/dy components |
| Reflection physics | 9-12 | Angle of incidence = angle of reflection |
| Paddle angle influence | 17-20 | Ball trajectory affected by paddle hit position |
| Grid destruction | 13-16 | Removing bricks from play field |
| Multi-hit bricks | 21-24 | Bricks requiring multiple hits |
| Power-up spawning | 25-28 | Dropping collectables from destroyed bricks |
| Power-up variety | 29-32 | Different power-up behaviours |
| Multi-ball | 33-36 | Managing multiple simultaneous balls |
| Ball spin | 37-40 | Spin affecting trajectory |
| Speed ramping | 41-44 | Ball acceleration over time |
| Bonus stages | 45-48 | Special levels with different rules |
| Combo systems | 53-56 | Score multipliers for rapid hits |
| Level streaming | 57-60 | Efficient level data loading |

---

## Phase 1: Foundation (Units 1-16)
*Core mechanics: paddle, ball, bricks, and a playable game.*

### Unit 1: The Playfield

**Learning Objectives:**
- Understand Breakout's spatial layout
- Set up screen for brick game
- Position fixed elements

**Concepts Introduced:**
- Breakout as a genre (Atari 1976 history)
- Playfield regions (brick area, play area, paddle zone)
- Border graphics for ball containment

**Code Written:**
- Initialise screen mode and colours
- Draw border walls (left, right, top)
- Clear brick and play areas
- Position score/lives display area

**What the Learner Sees:**
Empty playfield with borders - a "court" ready for action.

**Reference to Previous Games:**
"We use custom characters for borders (Maze Raider technique) and screen layout principles from SID Symphony."

---

### Unit 2: The Paddle Sprite

**Learning Objectives:**
- Create paddle sprite data
- Position paddle at bottom of screen
- Constrain paddle movement to horizontal

**Concepts Introduced:**
- Paddle dimensions (24 pixels wide × 4 pixels tall typical)
- X-position constraints for screen boundaries
- Sprite Y fixed, only X moves

**Code Written:**
- Define paddle sprite data (rectangular shape)
- Enable sprite 0 for paddle
- Set paddle Y position (fixed near bottom)
- Set initial X position (centre)

**What the Learner Sees:**
A paddle sprite sitting at the bottom of the playfield, ready to move.

**Reference to Starfield:**
"Sprite enabling and positioning carries directly from Starfield. The paddle is just a differently-shaped sprite."

---

### Unit 3: Paddle Control

**Learning Objectives:**
- Read joystick for paddle movement
- Implement smooth left/right movement
- Handle boundary collision

**Concepts Introduced:**
- Continuous input vs. discrete (joystick held, not pressed)
- Movement speed (pixels per frame)
- Boundary clamping

**Code Written:**
- Read joystick port 2
- Move paddle left/right based on input
- Clamp X position to playfield bounds
- Update sprite position register

**What the Learner Sees:**
Paddle moves smoothly left and right with joystick, stopping at walls.

**Reference to Starfield:**
"Joystick reading is identical to Starfield's player ship control. Boundary checking prevents paddle escaping the court."

---

### Unit 4: The Ball Sprite

**Learning Objectives:**
- Create ball sprite data
- Position ball initially on paddle
- Distinguish ball from paddle visually

**Concepts Introduced:**
- Ball size considerations (4×4 or 8×8 pixels)
- Ball colour contrast
- Ball starting position ("serving" position)

**Code Written:**
- Define ball sprite data (circular or square shape)
- Enable sprite 1 for ball
- Position ball centred on paddle
- Set ball colour

**What the Learner Sees:**
A ball sitting on the paddle, waiting to be launched.

---

### Unit 5: Ball Launch

**Learning Objectives:**
- Implement ball launch mechanic
- Set initial ball velocity
- Introduce velocity vectors (dx, dy)

**Concepts Introduced:**
- Velocity vectors - separate X and Y components
- Signed values for direction (negative = left/up)
- Launch angle (typically 45° upward)
- State machine: attached → in play

**Code Written:**
- Add game state variable (ball attached/in play)
- Detect fire button press
- Set initial dx and dy values on launch
- Transition ball state to "in play"

**What the Learner Sees:**
Press fire - ball launches upward at an angle from the paddle.

**Reference to Platform Panic:**
"Velocity concepts transfer from Platform Panic's gravity, but here we control both X and Y velocity directly rather than just Y."

---

### Unit 6: Ball Movement

**Learning Objectives:**
- Apply velocity to ball position
- Handle sub-pixel movement
- Create smooth ball motion

**Concepts Introduced:**
- Position += velocity each frame
- Fixed-point maths for sub-pixel accuracy
- 8.8 fixed-point representation
- Fractional position accumulation

**Code Written:**
- Add fractional position storage (low bytes)
- Add velocity to position each frame
- Update sprite position from integer portion
- Handle 9-bit X position

**What the Learner Sees:**
Ball moves smoothly in a straight line after launch.

**Reference to Starfield:**
"We used position updates in Starfield, but now add fractional precision for smooth diagonal movement at any angle."

---

### Unit 7: Wall Reflection

**Learning Objectives:**
- Detect wall collisions
- Implement reflection physics
- Reverse appropriate velocity component

**Concepts Introduced:**
- Collision detection with boundaries
- Reflection: reverse the perpendicular component
- Left/right wall: negate dx
- Top wall: negate dy

**Code Written:**
- Check ball X against left/right boundaries
- Check ball Y against top boundary
- Negate dx for horizontal wall hits
- Negate dy for top wall hit
- Add bounce sound effect

**What the Learner Sees:**
Ball bounces off walls realistically, changing direction appropriately.

**Reference to SID Symphony:**
"We add a short, punchy sound effect for wall bounces using SID voice 1 with a quick ADSR decay."

---

### Unit 8: Paddle Collision

**Learning Objectives:**
- Detect ball-paddle collision
- Reflect ball upward from paddle
- Handle edge cases (ball behind paddle)

**Concepts Introduced:**
- Rectangle-to-rectangle collision
- Collision boxes vs sprite sizes
- Vertical reflection on paddle hit
- Ball Y constraint (must be moving down to hit paddle)

**Code Written:**
- Check ball Y against paddle Y
- Check ball X overlaps paddle X range
- Verify ball is moving downward (dy positive)
- Negate dy to bounce upward
- Add paddle hit sound effect

**What the Learner Sees:**
Ball bounces off the paddle and returns upward.

---

### Unit 9: Basic Brick Grid

**Learning Objectives:**
- Define brick layout data structure
- Understand brick dimensions
- Create simple brick arrangement

**Concepts Introduced:**
- Grid representation (2D array or 1D with row stride)
- Brick presence flags (1 = brick, 0 = empty)
- Character-based brick display (2×1 chars = 16×8 pixels)
- Screen RAM for brick display

**Code Written:**
- Define brick grid data (8 rows × 12 columns)
- Create brick character graphics
- Write routine to draw brick grid
- Map grid positions to screen positions

**What the Learner Sees:**
A grid of coloured bricks fills the upper portion of the screen.

**Reference to Maze Raider:**
"Brick grids are tile maps by another name. We apply the same techniques from Maze Raider's maze layout."

---

### Unit 10: Brick Colours

**Learning Objectives:**
- Assign colours to brick rows
- Use colour RAM for variety
- Create visual hierarchy

**Concepts Introduced:**
- Colour RAM at $D800
- Row-based colour schemes
- Colour cycle progression (red → orange → yellow)
- Higher rows = higher value (classic Breakout convention)

**Code Written:**
- Extend draw routine with colour RAM writes
- Define colour per row table
- Apply colours when drawing bricks
- Match brick value to colour (optional)

**What the Learner Sees:**
Bricks in rainbow rows - red at top (most valuable), yellow at bottom.

---

### Unit 11: Ball-Brick Collision Detection

**Learning Objectives:**
- Determine which brick the ball is touching
- Convert ball position to grid coordinates
- Check brick presence at that position

**Concepts Introduced:**
- Pixel-to-grid coordinate conversion
- Division by brick dimensions
- Grid boundary checking
- Checking brick array for presence

**Code Written:**
- Calculate grid X from ball screen X
- Calculate grid Y from ball screen Y
- Check if coordinates in valid range
- Read brick array at calculated position
- Return collision result

**What the Learner Sees:**
(Internal change - detection happens silently for now.)

---

### Unit 12: Brick Destruction

**Learning Objectives:**
- Remove hit brick from game
- Update screen to show removal
- Update brick count

**Concepts Introduced:**
- Marking brick as destroyed (set to 0)
- Erasing brick from screen (space characters)
- Clearing colour RAM
- Tracking bricks remaining for level complete

**Code Written:**
- Set brick array position to 0
- Write space chars to screen positions
- Decrement brick counter
- Check for level complete condition

**What the Learner Sees:**
Hit bricks vanish! The grid shows gaps where balls have struck.

---

### Unit 13: Ball-Brick Reflection

**Learning Objectives:**
- Determine reflection direction after brick hit
- Handle horizontal vs vertical impacts
- Create accurate bounce behaviour

**Concepts Introduced:**
- Impact side detection
- Comparing ball entry direction with brick edges
- Horizontal impact: negate dx
- Vertical impact: negate dy

**Code Written:**
- Determine which edge the ball struck
- Compare ball velocity direction
- Apply appropriate reflection
- Add brick hit sound effect

**What the Learner Sees:**
Ball bounces correctly off bricks - sideways hits reflect horizontally, top/bottom hits reflect vertically.

**Reference to SID Symphony:**
"Brick hit sound is distinct from wall bounce - higher pitch, different waveform. Audio feedback matters!"

---

### Unit 14: Losing a Ball

**Learning Objectives:**
- Detect ball falling below paddle
- Decrement lives
- Reset ball to paddle

**Concepts Introduced:**
- Death zone at screen bottom
- Lives system
- Game state: lost ball
- Respawn mechanics

**Code Written:**
- Check ball Y against bottom boundary
- Decrement lives counter
- Update lives display
- Reset ball to "attached" state on paddle
- Check for game over (lives = 0)

**What the Learner Sees:**
Miss the ball - lose a life! Ball resets to paddle. Lives display updates.

**Reference to Starfield:**
"Lives system works like Starfield - display, decrement, game over check."

---

### Unit 15: Score System

**Learning Objectives:**
- Award points for brick destruction
- Display score on screen
- Implement score update routine

**Concepts Introduced:**
- Point values (different by brick colour/row)
- Multi-digit score display
- Score update routine (adding to BCD or binary)
- Screen update for score digits

**Code Written:**
- Add points on brick destruction
- Implement add-to-score routine
- Convert score to digits
- Display score in header area

**What the Learner Sees:**
Score increases with each brick destroyed! Red bricks worth more than yellow.

**Reference to Starfield:**
"Score display uses the same decimal conversion from Starfield, extended for higher scores."

---

### Unit 16: Complete Playable Game

**Learning Objectives:**
- Integrate all systems
- Add game over and restart
- Polish game loop

**Concepts Introduced:**
- Game state machine (title → play → game over)
- Restart flow
- Level complete detection
- Basic title screen

**Code Written:**
- Add simple title screen
- Implement game over screen
- Add restart on fire button
- Level complete → restart with new grid
- Polish timing and feel

**What the Learner Sees:**
A complete, playable Breakout game! Title, gameplay, game over, restart.

---

## Phase 2: Expansion (Units 17-32)
*Content variety: brick types, power-ups, levels.*

### Unit 17: Paddle Angle Influence - Theory

**Learning Objectives:**
- Understand angle-based reflection
- Learn how paddle position affects ball direction
- Design the angle system

**Concepts Introduced:**
- Where ball hits paddle determines exit angle
- Centre hit = straight up
- Edge hits = steep angles
- Lookup table for angle-to-velocity mapping

**Code Written:**
- Calculate hit offset (ball X - paddle centre X)
- Create angle lookup table (offset → dx value)
- Document velocity pairs for each angle

**What the Learner Sees:**
(Design document - implementation next unit.)

---

### Unit 18: Paddle Angle Implementation

**Learning Objectives:**
- Replace fixed reflection with angle system
- Use lookup table for velocity
- Test angle coverage

**Concepts Introduced:**
- Signed offset calculation
- Table indexing with signed values
- Velocity pair assignment from table
- Normalising speed (dx² + dy² roughly constant)

**Code Written:**
- Calculate paddle hit offset
- Look up dx from angle table
- Look up corresponding dy
- Apply new velocity to ball
- Test across paddle width

**What the Learner Sees:**
Ball angle changes based on where it hits the paddle! Edge hits go steep, centre hits go straight up.

---

### Unit 19: Visual Feedback for Paddle Hits

**Learning Objectives:**
- Add paddle "squash" animation
- Create visual impact feedback
- Enhance game feel

**Concepts Introduced:**
- Sprite animation on events
- Frame timing for brief animations
- Returning to default frame
- "Juice" in game design

**Code Written:**
- Create paddle squash sprite frame
- Trigger animation on ball hit
- Timer to return to normal
- Smooth transition

**What the Learner Sees:**
Paddle visually squashes when hit - satisfying tactile feedback!

---

### Unit 20: Paddle Speed Influence

**Learning Objectives:**
- Affect ball velocity based on paddle movement
- Add skill-based control
- Implement spin concept

**Concepts Introduced:**
- Paddle velocity tracking
- Adding paddle velocity to ball dx
- Speed caps to prevent extreme angles
- Spin mechanics

**Code Written:**
- Track paddle velocity (current X - previous X)
- Add portion of paddle velocity to ball dx on hit
- Clamp resulting velocity
- Test extreme cases

**What the Learner Sees:**
Moving the paddle while hitting adds spin - skilled players can curve shots!

---

### Unit 21: Multi-Hit Bricks - Silver

**Learning Objectives:**
- Introduce bricks requiring multiple hits
- Track hit count per brick
- Show damage visually

**Concepts Introduced:**
- Brick hit points (HP)
- Damage tracking in brick array (2 bits for HP)
- Visual damage states
- Silver brick = 2 hits

**Code Written:**
- Extend brick data to include HP
- Decrement HP on hit instead of destroying
- Change brick appearance when damaged
- Destroy when HP reaches 0

**What the Learner Sees:**
Silver bricks take two hits! First hit shows crack, second hit destroys.

---

### Unit 22: Multi-Hit Bricks - Gold

**Learning Objectives:**
- Add tougher brick type
- Create 3-hit sequence
- Progressive damage states

**Concepts Introduced:**
- Gold brick = 3 hits
- Three visual states (fresh, cracked, breaking)
- Character animation for damage
- Higher point value

**Code Written:**
- Add gold brick type
- Create three damage state characters
- Update drawing for damage level
- Award bonus points for gold bricks

**What the Learner Sees:**
Gold bricks need three hits - fresh → cracked → breaking → destroyed.

---

### Unit 23: Indestructible Bricks

**Learning Objectives:**
- Add bricks that cannot be destroyed
- Create strategic obstacles
- Handle level complete with indestructibles

**Concepts Introduced:**
- Unbreakable brick type (HP = infinite)
- Brick not counting toward level completion
- Strategic placement for level design
- Distinct visual appearance

**Code Written:**
- Add indestructible flag to brick type
- Skip destruction on hit
- Reflect ball but don't damage
- Exclude from brick count
- Create distinct graphic

**What the Learner Sees:**
Metal bricks cannot be destroyed! Ball bounces off but they remain.

---

### Unit 24: Brick Type System

**Learning Objectives:**
- Unify all brick types into system
- Create type lookup tables
- Streamline brick handling

**Concepts Introduced:**
- Brick type enumeration
- Property tables (HP, colour, points, flags)
- Table-driven design
- Extensibility for new types

**Code Written:**
- Define brick type constants
- Create HP table per type
- Create colour table per type
- Create points table per type
- Create flags table (indestructible, etc.)
- Refactor brick code to use tables

**What the Learner Sees:**
(Internal refactor - same gameplay, cleaner code.)

---

### Unit 25: Power-Up Framework

**Learning Objectives:**
- Design power-up drop system
- Create power-up sprite
- Implement falling behaviour

**Concepts Introduced:**
- Power-up spawn chance on brick destroy
- Power-up entity (position, type, active)
- Falling speed
- Capsule sprite

**Code Written:**
- Define power-up data structure
- Create capsule sprite
- Spawn power-up on brick destroy (random chance)
- Fall power-up each frame

**What the Learner Sees:**
Sometimes when bricks break, a capsule falls down!

---

### Unit 26: Power-Up Collection

**Learning Objectives:**
- Detect paddle catching power-up
- Activate power-up effect
- Handle power-up lifetime

**Concepts Introduced:**
- Paddle-powerup collision
- Power-up activation
- Effect duration timers
- Power-up lost if missed

**Code Written:**
- Check power-up position against paddle
- Trigger effect on collection
- Start duration timer
- Remove power-up if falls off screen

**What the Learner Sees:**
Catch power-ups with the paddle to activate effects!

---

### Unit 27: Wide Paddle Power-Up

**Learning Objectives:**
- Implement first power-up effect
- Extend paddle width temporarily
- Handle expanded collision

**Concepts Introduced:**
- Paddle width variable
- Expanded paddle sprite
- Adjusted boundary checks
- Timer countdown

**Code Written:**
- Create wide paddle sprite
- Switch sprite on power-up collection
- Adjust paddle collision box
- Timer to revert to normal size

**What the Learner Sees:**
Catch the Expand capsule - paddle grows wider! Timer counts down, then shrinks back.

---

### Unit 28: Laser Paddle Power-Up

**Learning Objectives:**
- Add shooting capability
- Create laser bullets
- Fire at bricks directly

**Concepts Introduced:**
- Mode change (paddle can fire)
- Laser bullet sprites
- Fire button dual use (launch ball / fire laser)
- Laser-brick collision

**Code Written:**
- Create laser bullet sprites
- Fire bullets on button press
- Move bullets upward
- Check bullet-brick collision
- Destroy bricks with laser hits

**What the Learner Sees:**
Laser mode! Fire button shoots lasers that destroy bricks directly.

---

### Unit 29: Slow Ball Power-Up

**Learning Objectives:**
- Implement speed modification
- Reduce ball velocity temporarily
- Create visual indicator

**Concepts Introduced:**
- Speed multiplier
- Velocity scaling
- Duration-based effect
- Ball colour change to indicate slow

**Code Written:**
- Store base velocity
- Apply speed multiplier on collection
- Change ball colour to indicate slow
- Timer to restore normal speed

**What the Learner Sees:**
Slow capsule - ball moves slower, giving more reaction time!

---

### Unit 30: Extra Life Power-Up

**Learning Objectives:**
- Award bonus life
- Cap maximum lives
- Create celebratory effect

**Concepts Introduced:**
- Lives increment
- Maximum lives cap
- Visual/audio celebration
- Rare power-up

**Code Written:**
- Increment lives on collection
- Cap at maximum (usually 5)
- Update lives display
- Play celebratory sound
- Flash effect

**What the Learner Sees:**
Extra life capsule - bonus life awarded with celebratory sound!

**Reference to SID Symphony:**
"We use a triumphant ascending arpeggio from SID Symphony techniques for the extra life sound."

---

### Unit 31: Power-Up Variety System

**Learning Objectives:**
- Manage multiple power-up types
- Implement random selection
- Balance spawn rates

**Concepts Introduced:**
- Power-up type enumeration
- Weighted random selection
- Spawn rate tuning
- Type indicator on capsule (letter)

**Code Written:**
- Define all power-up types
- Create spawn weight table
- Random type selection on drop
- Display type letter on capsule sprite
- Route to appropriate handler

**What the Learner Sees:**
Different capsules with different letters fall - E for Expand, L for Laser, S for Slow, etc.

---

### Unit 32: Multiple Levels

**Learning Objectives:**
- Create level data format
- Implement level progression
- Design multiple layouts

**Concepts Introduced:**
- Level data structure
- Level-to-brick array loading
- Level number display
- Increasing difficulty

**Code Written:**
- Define 8 level layouts
- Create level loading routine
- Progress to next level on complete
- Display current level number
- Loop levels after final (with speed increase)

**What the Learner Sees:**
Beat all bricks - advance to next level! Different brick patterns each level.

---

## Phase 3: Polish (Units 33-48)
*Effects, sound, visual feedback, and "juice".*

### Unit 33: Multi-Ball Framework

**Learning Objectives:**
- Support multiple simultaneous balls
- Create ball array
- Handle independent ball movement

**Concepts Introduced:**
- Ball array (position, velocity per ball)
- Active ball count
- Independent collision detection
- Sprite allocation for balls

**Code Written:**
- Convert single ball to ball array
- Track active ball count
- Loop through all balls for movement
- Handle sprite allocation (up to 3 balls)

**What the Learner Sees:**
(Framework ready - same single ball gameplay.)

---

### Unit 34: Multi-Ball Power-Up

**Learning Objectives:**
- Split ball into three
- Spawn additional balls
- Handle ball death correctly

**Concepts Introduced:**
- Ball spawn at current position
- Velocity spread (different angles)
- Individual ball death
- Game over only when all balls lost

**Code Written:**
- Multi-ball power-up handler
- Spawn two additional balls at current ball position
- Assign spread velocities
- Track individual ball states
- Game continues while any ball active

**What the Learner Sees:**
Multi-ball capsule - ball splits into three! Chaos ensues. Lose all three to lose a life.

---

### Unit 35: Multi-Ball Polish

**Learning Objectives:**
- Visual distinction for balls
- Independent collision sounds
- Performance considerations

**Concepts Introduced:**
- Ball colour variation
- Sound variations per ball
- Collision priority
- Sprite flicker concerns (preview)

**Code Written:**
- Assign slight colour variations
- Vary sound pitch per ball
- Optimise collision detection order
- Handle sprite limit gracefully

**What the Learner Sees:**
Three distinct balls bouncing independently, each with its own sound!

---

### Unit 36: Brick Destruction Animation

**Learning Objectives:**
- Animate brick destruction
- Create particle effects
- Add visual satisfaction

**Concepts Introduced:**
- Animation frames for destruction
- Particle spawning
- Brief delay before clearing
- Screen shake concept

**Code Written:**
- Create destruction animation frames
- Play animation on brick hit
- Spawn small particle chars
- Clear brick after animation completes

**What the Learner Sees:**
Bricks explode with particle effects when destroyed - much more satisfying!

---

### Unit 37: Spin Visual Indicator

**Learning Objectives:**
- Show ball spin visually
- Create spinning ball animation
- Indicate trajectory influence

**Concepts Introduced:**
- Ball rotation frames
- Spin direction indication
- Animation speed tied to spin amount
- Visual feedback for player skill

**Code Written:**
- Create ball rotation animation frames
- Animate based on spin value
- Faster spin = faster rotation
- Direction matches spin direction

**What the Learner Sees:**
Ball visually spins when paddle imparts spin - player can see curve influence!

---

### Unit 38: Streak System

**Learning Objectives:**
- Track consecutive hits without paddle
- Award bonus points
- Create combo feedback

**Concepts Introduced:**
- Hit streak counter
- Streak bonus multiplier
- Visual streak indicator
- Streak break detection

**Code Written:**
- Track hits since last paddle bounce
- Apply score multiplier for streaks
- Display streak counter when active
- Reset on paddle hit
- Celebratory sound for high streaks

**What the Learner Sees:**
Hit multiple bricks without paddle touch - combo counter appears! Higher combos = bigger scores.

---

### Unit 39: Sound Design - Variety

**Learning Objectives:**
- Create distinct sounds for all events
- Build cohesive audio palette
- Implement sound priority

**Concepts Introduced:**
- Sound event enumeration
- Priority system (important sounds override)
- Voice allocation
- Audio consistency

**Code Written:**
- Define all sound events
- Create sound for each event type
- Implement priority queue
- Handle overlapping sounds
- Test audio mix

**What the Learner Sees:**
Every game event has its own distinctive sound - bounces, hits, power-ups, deaths all unique.

**Reference to SID Symphony:**
"We apply the full SID Symphony vocabulary - all three voices working together for a rich soundscape."

---

### Unit 40: Background Music

**Learning Objectives:**
- Add simple background tune
- Handle music-effects balance
- Create appropriate mood

**Concepts Introduced:**
- Music during gameplay
- Reserving voice for effects
- Volume balancing
- Music tempo matching game pace

**Code Written:**
- Create simple looping melody
- Reserve voice 3 for effects
- Balance music volume
- Integrate with game loop timing

**What the Learner Sees:**
Background music plays during gameplay! Effects still come through clearly.

---

### Unit 41: Speed Ramping

**Learning Objectives:**
- Increase ball speed over time
- Create escalating tension
- Balance difficulty curve

**Concepts Introduced:**
- Speed increase triggers
- Gradual vs sudden speed changes
- Maximum speed cap
- Speed reset on ball loss

**Code Written:**
- Track bricks destroyed
- Increase speed at thresholds
- Apply gradual velocity increase
- Cap maximum speed
- Reset speed on new ball

**What the Learner Sees:**
Ball gets faster as bricks are cleared! Creates mounting tension.

---

### Unit 42: Catch Paddle Power-Up

**Learning Objectives:**
- Implement sticky paddle
- Ball attaches on contact
- Re-aim and launch

**Concepts Introduced:**
- Paddle state (normal/sticky)
- Ball attachment mechanics
- Re-aim on paddle
- Strategic advantage

**Code Written:**
- Catch power-up handler
- Ball sticks on paddle contact
- Ball moves with paddle
- Fire to release ball
- Timer for catch duration

**What the Learner Sees:**
Catch capsule - ball sticks to paddle! Move to aim, fire to release.

---

### Unit 43: Break-Through Power-Up

**Learning Objectives:**
- Ball passes through bricks
- Destroy multiple without bouncing
- Devastating power-up

**Concepts Introduced:**
- Collision mode flag
- No-bounce destruction
- Duration-limited effect
- Visual indicator (flaming ball)

**Code Written:**
- Break-through mode flag
- Destroy brick without reflection
- Ball continues through
- Flaming ball visual
- Timer to end effect

**What the Learner Sees:**
Break-through mode - ball tears through bricks without stopping! Devastating!

---

### Unit 44: Level Transition Effects

**Learning Objectives:**
- Polish level complete transition
- Add screen effects
- Create sense of achievement

**Concepts Introduced:**
- Level complete fanfare
- Screen transition effect
- Bonus tally
- Brief pause for celebration

**Code Written:**
- Detect level complete
- Play victory fanfare
- Animate transition effect
- Display level bonus
- Load and transition to next level

**What the Learner Sees:**
Level complete! Fanfare plays, bonus points tally, dramatic transition to next level.

---

### Unit 45: Lives Display Enhancement

**Learning Objectives:**
- Visual lives indicator
- Mini paddle icons
- Death animation

**Concepts Introduced:**
- Icon-based lives display
- Character graphics for mini paddle
- Death animation effect
- Clear visual communication

**Code Written:**
- Create mini paddle character
- Display lives as paddle icons
- Animate paddle loss on death
- Update display dynamically

**What the Learner Sees:**
Lives shown as mini paddles - lose one and it fades away with animation.

---

### Unit 46: Title Screen Polish

**Learning Objectives:**
- Professional title screen
- Animated elements
- High score display

**Concepts Introduced:**
- Logo character graphics
- Animation on title
- High score persistence
- Attract mode concept

**Code Written:**
- Create game logo characters
- Animate title elements
- Display high scores
- Press fire to start

**What the Learner Sees:**
Professional title screen with animated logo, high scores, and "Press Fire" prompt.

---

### Unit 47: Game Over Screen

**Learning Objectives:**
- Polish game over presentation
- Final score display
- High score check

**Concepts Introduced:**
- Game over sequence
- Score ranking
- Name entry (if high score)
- Return to title

**Code Written:**
- Game over display
- Check against high scores
- Simple initial entry
- Display final stats
- Return to title option

**What the Learner Sees:**
Game over! Final score displayed, high score entry if earned, return to title.

---

### Unit 48: Bonus Stage Framework

**Learning Objectives:**
- Create special stage type
- Different rules for variety
- Reward for progress

**Concepts Introduced:**
- Stage type flag
- Modified rules (all bricks worth bonus)
- Time limit
- No ball loss possible

**Code Written:**
- Bonus stage flag
- Modified scoring
- Timer countdown
- Automatic level complete on time
- Bonus calculation

**What the Learner Sees:**
Every few levels - bonus stage! Destroy as many bricks as possible in time limit for mega points!

---

## Phase 4: Mastery (Units 49-64)
*Optimization, advanced mechanics, and professional polish.*

### Unit 49: Performance Profiling

**Learning Objectives:**
- Analyse game performance
- Identify bottlenecks
- Measure frame timing

**Concepts Introduced:**
- Raster position for timing
- Frame budget analysis
- Collision detection cost
- Sprite update cost

**Code Written:**
- Add raster timing display
- Measure each major routine
- Identify slow sections
- Document optimization targets

**What the Learner Sees:**
Debug mode showing timing - learn where CPU time goes.

**Reference to Starfield:**
"We apply Starfield's profiling techniques to ensure the game runs smoothly even with many balls."

---

### Unit 50: Collision Optimization

**Learning Objectives:**
- Optimize ball-brick detection
- Reduce unnecessary checks
- Use spatial optimization

**Concepts Introduced:**
- Bounding box early-out
- Only check nearby bricks
- Grid-based spatial partitioning
- Exit early on no-collision

**Code Written:**
- Calculate brick row/column range
- Only check bricks in range
- Early exit optimizations
- Measure improvement

**What the Learner Sees:**
(Performance improvement - smoother gameplay.)

---

### Unit 51: Ball Movement Optimization

**Learning Objectives:**
- Optimize ball update loop
- Unroll where beneficial
- Use efficient maths

**Concepts Introduced:**
- Loop unrolling for multiple balls
- Shift operations for multiply
- Register allocation
- Memory access patterns

**Code Written:**
- Optimize ball loop
- Use shifts for velocity operations
- Minimize memory reads
- Measure improvement

**What the Learner Sees:**
(Performance improvement - even smoother multi-ball.)

---

### Unit 52: Sprite Multiplexing Preview

**Learning Objectives:**
- Understand sprite limits
- Preview multiplexing concepts
- Handle many sprites gracefully

**Concepts Introduced:**
- 8-sprite hardware limit
- Multiplexing for more
- Graceful degradation
- When to use (many power-ups/balls)

**Code Written:**
- Detect sprite overflow
- Basic sprite hiding for overflow
- Preview multiplexing structure
- Comment for future expansion

**What the Learner Sees:**
(Graceful handling when many objects on screen.)

**Reference to Sprite Storm (Preview):**
"Sprite Storm (Game 9) covers multiplexing in depth. Here we handle overflow gracefully."

---

### Unit 53: Combo System Enhancement

**Learning Objectives:**
- Elaborate combo mechanics
- Risk/reward for big combos
- Visual combo meter

**Concepts Introduced:**
- Combo multiplier curve
- Risk/reward (high combo = high score but dangerous)
- Combo meter display
- Combo break penalty concept

**Code Written:**
- Enhanced combo multiplier
- Visual combo meter
- Animated meter fill
- Audio escalation with combo

**What the Learner Sees:**
Combo meter shows current multiplier - goes up with each hit, resets on paddle touch!

---

### Unit 54: Boss Brick

**Learning Objectives:**
- Create special challenge brick
- Boss brick mechanics
- End-of-level mini-boss

**Concepts Introduced:**
- Boss brick (large, many HP)
- Changing behaviour as damaged
- Multiple phases
- Big point reward

**Code Written:**
- Create boss brick type
- Spans multiple grid cells
- Many hit points
- Behaviour changes at HP thresholds
- Destruction celebration

**What the Learner Sees:**
Boss brick appears in certain levels - huge, takes many hits, changes colour as damaged!

---

### Unit 55: Level Editor Concept

**Learning Objectives:**
- Design level data format
- Create level building tool
- Enable custom levels

**Concepts Introduced:**
- Level format specification
- External tool workflow
- Level testing flow
- Player creativity

**Code Written:**
- Document level format
- Create simple BASIC level loader
- Test custom levels
- Integration notes

**What the Learner Sees:**
(Tool for creating custom levels - documentation and simple builder.)

---

### Unit 56: Advanced Level Designs

**Learning Objectives:**
- Create 24 total levels
- Design patterns and progressions
- Balance difficulty curve

**Concepts Introduced:**
- Level design principles
- Visual patterns in brick layouts
- Difficulty progression
- Level themes

**Code Written:**
- Design and implement 24 levels
- Variety of patterns
- Progressive difficulty
- Interesting use of brick types

**What the Learner Sees:**
24 unique levels with creative patterns - faces, shapes, mazes, challenges!

---

### Unit 57: High Score System

**Learning Objectives:**
- Persistent high scores
- Save to disk/tape
- Restore on load

**Concepts Introduced:**
- Save data format
- File operations
- Load at startup
- Save on new high score

**Code Written:**
- High score data structure
- Save routine
- Load routine
- Error handling

**What the Learner Sees:**
High scores persist between plays! Your achievements are remembered.

---

### Unit 58: Attract Mode

**Learning Objectives:**
- Demo mode on title
- AI paddle player
- Showcase gameplay

**Concepts Introduced:**
- Attract mode state
- Simple AI paddle movement
- Demo timing
- Return to title

**Code Written:**
- AI paddle tracking ball
- Demo game loop
- Timer to return to title
- Interrupt on fire button

**What the Learner Sees:**
Leave title screen idle - game plays itself! AI demonstrates gameplay.

---

### Unit 59: Continue System

**Learning Objectives:**
- Credit-based continues
- Continue screen
- Extend play sessions

**Concepts Introduced:**
- Credits concept
- Continue countdown
- Score penalty for continue
- Arcade-style progression

**Code Written:**
- Credit counter
- Continue screen on game over
- Countdown timer
- Score reduction on continue
- Resume game state

**What the Learner Sees:**
Game over? Continue option! Countdown timer - press fire to continue with reduced score.

---

### Unit 60: Statistics Tracking

**Learning Objectives:**
- Track player statistics
- Bricks destroyed, time played, etc.
- Display statistics screen

**Concepts Introduced:**
- Lifetime statistics
- Statistics display
- Running totals
- Achievement-like milestones

**Code Written:**
- Statistics data structure
- Increment counters during play
- Statistics display screen
- Milestone messages

**What the Learner Sees:**
Statistics screen shows lifetime play - total bricks destroyed, levels completed, etc.

---

### Unit 61: Visual Polish Pass

**Learning Objectives:**
- Final visual refinements
- Colour scheme tuning
- Animation smoothness

**Concepts Introduced:**
- Visual consistency check
- Colour harmony
- Animation timing review
- Professional presentation

**Code Written:**
- Colour palette adjustments
- Animation timing tweaks
- Visual consistency fixes
- Border and background refinement

**What the Learner Sees:**
Everything looks just a bit better - polished, consistent, professional.

---

### Unit 62: Audio Polish Pass

**Learning Objectives:**
- Final audio refinements
- Mix balancing
- Sound priority review

**Concepts Introduced:**
- Audio mix review
- Volume balancing
- Priority system check
- Music-effect balance

**Code Written:**
- Volume adjustments
- Priority order fixes
- Music tempo tuning
- Effect variations

**What the Learner Sees:**
Audio is perfectly balanced - effects punch through, music complements, nothing overwhelms.

---

### Unit 63: Memory Optimization

**Learning Objectives:**
- Reduce memory footprint
- Efficient data structures
- Room for expansion

**Concepts Introduced:**
- Memory map review
- Data compression opportunities
- Code size reduction
- Future-proofing

**Code Written:**
- Review memory layout
- Compress where possible
- Remove redundancy
- Document final memory map

**What the Learner Sees:**
(Internal optimization - same gameplay, more efficient.)

---

### Unit 64: Release Build

**Learning Objectives:**
- Create final release version
- Remove debug code
- Optimise load sequence

**Concepts Introduced:**
- Debug/release builds
- Final testing checklist
- Version numbering
- Distribution preparation

**Code Written:**
- Remove debug displays
- Optimize startup
- Final integration test
- Create release PRG

**What the Learner Sees:**
Complete, polished Brick Basher! A game worthy of commercial release in 1985.

---

## Summary

**Brick Basher** takes the classic Breakout formula and builds it into a feature-complete game over 64 units:

**Phase 1 (Foundation):** Core mechanics - paddle, ball, bricks, collision, and a playable game.

**Phase 2 (Expansion):** Content - brick types, power-ups, paddle physics, multiple levels.

**Phase 3 (Polish):** Feel - multi-ball, animations, combos, sound design, transitions.

**Phase 4 (Mastery):** Professional quality - optimization, boss bricks, statistics, release build.

### Skills Transferred Forward

The following skills debut in Brick Basher and will be applied in future games:

1. **Velocity vectors (dx/dy)** → Night Raid (missile physics), Raster Rider (car physics)
2. **Reflection physics** → Arena Fighter (projectiles), any game with bouncing
3. **Grid destruction** → Invader Wave (shield destruction), any destructible environment
4. **Power-up systems** → Nearly every game from here forward
5. **Multi-object management** → Sprite Storm (many sprites), all complex games
6. **Speed ramping** → Most action games from here forward
7. **Combo/streak systems** → Arena Fighter, Mega Blaster
8. **Attract mode** → All subsequent games

### Game Specifications

- **Levels:** 24 unique layouts
- **Brick types:** 5 (normal, silver 2-hit, gold 3-hit, indestructible, boss)
- **Power-ups:** 7 (wide paddle, laser, slow, extra life, multi-ball, catch, break-through)
- **Maximum balls:** 3 simultaneous
- **Lives:** 3 (max 5 with extra life power-ups)
- **Features:** Combo system, speed ramping, attract mode, high scores, statistics
