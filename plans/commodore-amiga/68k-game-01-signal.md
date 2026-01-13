# Signal: 64-Unit Outline

**Game:** Amiga Game 1: Signal
**Units:** 64
**Concept:** Frogger-style lane crosser. Cross roads and rivers, avoid cars, ride logs, reach safety zones. A timing game that naturally exercises the entire Amiga custom chipset.

**Commercial Quality Target:** A game that could have sold for £19.99 on disk in 1987. Polished, responsive, with that distinctive Amiga look and sound.

**Design Principle:** "Show First, Explain Later" - Scaffold provides working code immediately; theory follows experience.

---

## The Finished Game

Before detailing the units, here's what the learner builds:

### Core Gameplay
- 5 lanes of road traffic (cars moving left/right)
- 5 lanes of river (logs and turtles to ride)
- Player frog moves in grid steps
- Joystick controls movement (8-way, but snaps to grid)
- Reach one of 5 home bases at the top
- Fill all 5 homes to complete a level
- Hit a car = death
- Fall in water = death
- Ride logs to cross river safely

### Content
- 8 levels with increasing difficulty
- Speed increases each level
- More obstacles, tighter gaps
- Bonus items on logs (flies for extra points)
- Time limit per attempt
- High score tracking

### Audio
- Paula sampled sound effects
- Hop sound, splash, car horn, death
- Background music during gameplay
- Jingles for level complete, game over

### Visuals
- 32-colour display
- Smooth hardware sprite player
- Blitter-drawn obstacles (cars, logs, turtles)
- Copper gradient sky
- Animated water
- Sprite-based bonus items

### Polish
- Animated title screen
- High score table with name entry
- Options (starting level, lives)
- Pause functionality
- Attract mode demo

---

## Engagement Milestones

| Milestone | Unit |
|-----------|------|
| First visible output (sprite + playfield) | 1 |
| First interactivity (joystick movement) | 2 |
| First "game feel" (obstacles, collision) | 8 |
| Complete roads game | 16 |
| Complete roads + river game | 32 |
| Full polish (music, effects, menus) | 48 |
| Distribution ready | 64 |

---

## Phase 1: Foundation (Units 1-16)

*Goal: A complete, playable Frogger game with roads, cars, collision, lives, and scoring. River section comes in Phase 2.*

*By the end of this phase, the learner has built a working game. The frog crosses roads, avoids cars, reaches home zones, loses lives, and wins levels. It's roads-only but complete.*

---

### Unit 1: Hello Amiga

**Learning Objectives:**
- Run a working Amiga program
- See the custom chipset in action
- Modify sprite position and colours
- Understand immediate feedback

**Concepts Introduced:**
- Scaffold approach (working code provided)
- Custom chipset overview (Agnus, Denise, Paula)
- Hardware sprites
- Copper display lists

**Scaffold Provides:**
- System takeover and clean restoration
- 5-bitplane display (32 colours)
- Copper list with zone colours
- Hardware sprite 0 (frog) displayed
- VBlank interrupt handler
- Exit on right mouse button

**What the Learner Does:**
```asm
FROG_START_X = 160    ; Change to move frog horizontally
FROG_START_Y = 220    ; Change to move frog vertically
; Modify palette entries to change zone colours
; Modify sprite data to change frog appearance
```

**What the Learner Sees:**
Coloured playfield with frog sprite visible. Changes to constants immediately affect the display. First contact with the Amiga.

**Technical Details (hidden in scaffold):**
- Custom base: $DFF000
- Forbid/Permit for OS takeover
- INTENA/DMACON state save/restore
- DIWSTRT/DIWSTOP, DDFSTRT/DDFSTOP
- Copper list structure

---

### Unit 2: Moving the Frog

**Learning Objectives:**
- Read joystick input
- Update sprite position from input
- Constrain movement to boundaries
- Achieve interactivity

**Concepts Introduced:**
- CIA port reading ($BFE001)
- Direction decoding
- Sprite position updates
- Boundary checking

**Code Written:**
```asm
read_joystick:
    move.b  $BFE001,d0      ; Read CIA port
    ; Decode up/down/left/right
    ; Store direction

update_frog:
    ; Add direction to frog position
    ; Check screen boundaries
    ; Update sprite control words
```

**What the Learner Sees:**
Push joystick, frog moves. Interactivity achieved in Unit 2.

**Technical Details:**
- CIA-A: $BFE001
- Direction bits decoded from port
- Sprite VSTART/HSTART in control words

---

### Unit 3: Understanding What We Built

**Learning Objectives:**
- Understand system takeover (why we disable the OS)
- Understand Copper lists (how the display works)
- Understand hardware sprites (how the frog appears)
- Understand VBlank (why timing is consistent)

**Concepts Introduced:**
- Exec library and Forbid/Permit
- Interrupt and DMA control
- Copper as display list processor
- Sprite data format
- Vertical blank synchronisation

**Code Written:**
None - this unit explains the scaffold code.

**What the Learner Sees:**
Same as Unit 2. This unit is about understanding, not new output.

**Technical Details:**
- INTENA: $DFF09A (write), $DFF01C (read)
- DMACON: $DFF096 (write), $DFF002 (read)
- Copper WAIT/MOVE instruction format
- Sprite control word structure
- Level 3 autovector at $6C

---

### Unit 4: The Playfield

**Learning Objectives:**
- Modify Copper list for zone colours
- Design the game layout
- Understand Copper timing

**Concepts Introduced:**
- Copper WAIT for scanline position
- Copper MOVE for register writes
- Zone-based colour design
- Playfield planning

**Code Written:**
```asm
copper_list:
    dc.w    $0180,$0030     ; COLOR00 = dark blue
    dc.w    $2C01,$FFFE     ; Wait for line $2C
    dc.w    $0180,$0050     ; Green for home zone
    dc.w    $5001,$FFFE     ; Wait for river start
    dc.w    $0180,$0058     ; Blue for river
    ; ... more zone transitions
```

**What the Learner Sees:**
Proper game playfield: green home zones, blue river area, grey road section, green start zone.

**Technical Details:**
- Copper WAIT: $VVHH,$FFFE
- Copper MOVE: $0RRR,$DDDD
- Zone layout for 13-row grid

---

### Unit 5: Grid-Based Movement

**Learning Objectives:**
- Convert free movement to grid hops
- Implement hop animation
- Add movement state machine
- Create Frogger's distinctive feel

**Concepts Introduced:**
- Grid coordinate system
- Movement states (idle, hopping)
- Frame-based animation
- Smooth interpolation

**Code Written:**
```asm
frog_grid_x:    dc.w    10      ; Column (0-19)
frog_grid_y:    dc.w    0       ; Row (0-12)
frog_state:     dc.w    0       ; 0=idle, 1-8=hopping
frog_dir:       dc.w    0       ; Current hop direction

update_frog_position:
    ; If idle and input: start hop
    ; If hopping: interpolate position
    ; On frame 8: snap to grid, return to idle
```

**What the Learner Sees:**
Frog hops in discrete steps, smoothly animated. Grid-based movement like real Frogger.

**Technical Details:**
- Grid: 20 columns × 13 rows
- Cell size: 16×16 pixels
- Hop duration: 8 frames
- Movement: 2 pixels per frame

---

### Unit 6: The Blitter Introduction

**Learning Objectives:**
- Understand why 8 sprites isn't enough
- Learn Blitter basics (copy operation)
- Perform a simple Blitter copy
- Prepare for BOB graphics

**Concepts Introduced:**
- Blitter as DMA graphics engine
- BOBs (Blitter Objects) vs hardware sprites
- Source/destination channels
- BLTSIZE triggering

**Code Written:**
```asm
blit_copy:
    btst    #14,DMACONR(a6) ; Wait for Blitter
    bne.s   blit_copy
    move.l  #source,BLTAPT(a6)
    move.l  #dest,BLTDPT(a6)
    move.w  #0,BLTAMOD(a6)
    move.w  #0,BLTDMOD(a6)
    move.w  #$09F0,BLTCON0(a6)  ; A->D copy
    move.w  #$0000,BLTCON1(a6)
    move.w  #(16<<6)|1,BLTSIZE(a6)  ; 16 lines, 1 word
```

**What the Learner Sees:**
A rectangle copied on screen. Understanding of how we'll draw many cars.

**Technical Details:**
- BLTCON0: $DFF040
- BLTAPT/BLTDPT: source/dest pointers
- BLTSIZE: triggers blit, encodes dimensions
- Wait via DMACONR bit 14

---

### Unit 7: Cars on the Road

**Learning Objectives:**
- Draw cars using Blitter
- Move multiple cars each frame
- Handle screen wrapping
- Vary speed per lane

**Concepts Introduced:**
- Object data structures
- Blitter drawing loop
- Screen edge wrapping
- Lane-based behaviour

**Code Written:**
```asm
NUM_CARS = 8
car_x:      ds.w    NUM_CARS
car_y:      ds.w    NUM_CARS
car_speed:  ds.w    NUM_CARS
car_lane:   ds.w    NUM_CARS

move_cars:
    ; For each car:
    ;   Add speed to X
    ;   If X > 336: X = 0
    ;   If X < 0: X = 336

draw_cars:
    ; For each car:
    ;   Blitter copy car graphic to screen position
```

**What the Learner Sees:**
Cars moving across road lanes at different speeds. Traffic!

**Technical Details:**
- Lane Y positions calculated from grid
- Speeds: 1, 2, -1, -2 pixels/frame
- Wrap threshold: screen width + car width

---

### Unit 8: Collision Detection

**Learning Objectives:**
- Detect frog-car overlap
- Handle death event
- Implement respawn
- Add consequence to gameplay

**Concepts Introduced:**
- Bounding box collision
- Absolute value distance
- Death state
- Respawn logic

**Code Written:**
```asm
check_collision:
    ; For each car:
    ;   dx = abs(frog_x - car_x)
    ;   dy = abs(frog_y - car_y)
    ;   if dx < threshold AND dy < threshold:
    ;       trigger death

trigger_death:
    ; Flash screen
    ; Brief pause
    ; Decrement lives
    ; Respawn at start
```

**What the Learner Sees:**
Hit a car → screen flash → frog reappears at start. It's a game!

**Technical Details:**
- Collision threshold: 12 pixels (box overlap)
- Flash via Copper palette change
- Death pause: 30 frames

---

### Unit 9: Lives System

**Learning Objectives:**
- Track lives variable
- Display lives as icons
- Handle game over condition
- Add stakes to gameplay

**Concepts Introduced:**
- Lives counter
- Sprite-based HUD
- Game over state
- Multi-sprite display

**Code Written:**
```asm
lives:      dc.w    3

display_lives:
    ; Use sprites 1-3 for life icons
    ; Position in top-left corner
    ; Hide unused sprites (Y = 0)

check_game_over:
    tst.w   lives
    beq     game_over
```

**What the Learner Sees:**
Small frog icons in corner show remaining lives. Lose all 3 → game over.

**Technical Details:**
- Sprites 1-3 for lives display
- Life icon: 8×8 mini frog
- Position: top-left, 8 pixels apart

---

### Unit 10: Home Zones

**Learning Objectives:**
- Define goal positions
- Detect frog reaching home
- Mark homes as filled
- Award points

**Concepts Introduced:**
- Goal zone detection
- State per home (empty/filled)
- Scoring events
- Level completion check

**Code Written:**
```asm
NUM_HOMES = 5
home_filled:    ds.b    NUM_HOMES   ; 0=empty, 1=filled
score:          ds.l    1

check_home:
    ; If frog at top row:
    ;   Determine which home zone
    ;   If home empty:
    ;       Mark filled
    ;       Add 50 to score
    ;       Respawn frog
    ;   Check if all homes filled → level complete
```

**What the Learner Sees:**
Reach top → home fills in (colour change) → points awarded → frog respawns.

**Technical Details:**
- Home columns: 2, 6, 10, 14, 18
- Home width: 2 grid cells each
- Points per home: 50

---

### Unit 11: Sound Effects

**Learning Objectives:**
- Set up Paula for samples
- Trigger sounds on events
- Create audio feedback

**Concepts Introduced:**
- Paula audio channels
- Sample format (8-bit signed)
- AUDxLC, AUDxLEN, AUDxPER, AUDxVOL
- DMA audio enable

**Code Written:**
```asm
play_sound:
    ; a0 = sample pointer
    ; d0 = length in words
    ; d1 = period (pitch)
    move.l  a0,AUD0LC(a6)
    move.w  d0,AUD0LEN(a6)
    move.w  d1,AUD0PER(a6)
    move.w  #64,AUD0VOL(a6)
    move.w  #$8001,DMACON(a6)
    rts

; Call on: hop, death, home reached
```

**What the Learner Sees:**
Hop makes a sound. Death makes a sound. Reaching home makes a sound. The game has audio presence.

**Technical Details:**
- AUD0LC: $DFF0A0
- AUD0LEN: $DFF0A4
- AUD0PER: $DFF0A6 (428 ≈ 8287 Hz)
- AUD0VOL: $DFF0A8 (0-64)

---

### Unit 12: Score Display

**Learning Objectives:**
- Convert score to decimal digits
- Display score on screen
- Update efficiently

**Concepts Introduced:**
- Binary to BCD conversion
- Blitter text rendering
- HUD positioning
- Dirty rectangle updates

**Code Written:**
```asm
display_score:
    ; Convert 32-bit score to 6 decimal digits
    ; Draw each digit using Blitter
    ; Position in HUD area
```

**What the Learner Sees:**
Score displayed at top of screen. Increases when reaching homes.

**Technical Details:**
- Score: 32-bit long word
- Display: 6 digits (up to 999,999)
- Digit graphics: 8×8 each

---

### Unit 13: Timer

**Learning Objectives:**
- Implement countdown timer
- Display time remaining
- Death on timeout
- Time bonus for speed

**Concepts Introduced:**
- Frame-based countdown
- Urgency mechanic
- Risk/reward balance
- Time display

**Code Written:**
```asm
timer:      dc.w    3000    ; 60 seconds × 50 frames

update_timer:
    subq.w  #1,timer
    beq     timeout_death
    ; Display timer / 50 as seconds

award_time_bonus:
    ; On reaching home: score += timer / 5
```

**What the Learner Sees:**
Timer counting down. Must reach home before time runs out. Faster = more bonus points.

**Technical Details:**
- 60 seconds = 3000 frames (PAL)
- Display as seconds (timer / 50)
- Bonus: timer × 2 points

---

### Unit 14: Level Progression

**Learning Objectives:**
- Track current level
- Increase difficulty per level
- Handle level completion
- Create progression

**Concepts Introduced:**
- Difficulty scaling
- Level state
- Speed multipliers
- Content variation

**Code Written:**
```asm
level:      dc.w    1

next_level:
    addq.w  #1,level
    ; Increase car speeds
    ; Add more cars
    ; Reset homes
    ; Reset frog position

calculate_speed:
    ; base_speed + (level - 1) × increment
```

**What the Learner Sees:**
Complete level → brief celebration → next level with faster cars.

**Technical Details:**
- Speed increase: +0.5 pixels/frame per level
- Car count: 8 + (level × 2)
- Max level: 8 (or endless)

---

### Unit 15: Game States

**Learning Objectives:**
- Implement state machine
- Create title screen
- Handle game over
- Manage transitions

**Concepts Introduced:**
- Game states (TITLE, PLAYING, GAME_OVER)
- State transitions
- Simple text display
- Fire button detection

**Code Written:**
```asm
STATE_TITLE     = 0
STATE_PLAYING   = 1
STATE_GAMEOVER  = 2

game_state:     dc.w    STATE_TITLE

main_loop:
    move.w  game_state,d0
    cmp.w   #STATE_TITLE,d0
    beq     handle_title
    cmp.w   #STATE_PLAYING,d0
    beq     handle_playing
    bra     handle_gameover
```

**What the Learner Sees:**
Title screen → press fire → play → game over → press fire → title. Complete flow.

**Technical Details:**
- State variable controls dispatch
- Title: simple text, wait for fire
- Game over: show score, wait, return to title

---

### Unit 16: Phase 1 Complete

**Learning Objectives:**
- Review all systems
- Final polish pass
- Test all paths
- Celebrate milestone

**Concepts Introduced:**
- Integration testing
- Polish methodology
- Phase completion
- Preview of Phase 2

**Code Written:**
- Bug fixes
- Timing adjustments
- Final balance tuning

**What the Learner Sees:**
Complete, polished roads-only Frogger. Playable game with title, gameplay, game over, scoring, lives, levels, and sound.

**Phase 1 Checkpoint:**
The learner has built a working game. Hardware sprite frog, Blitter cars, collision detection, lives, scoring, timer, level progression, and complete game flow. The river section comes in Phase 2.

---

## Phase 2: Expansion (Units 17-32)

*Goal: Add the river section with logs and turtles. Cookie-cut Blitter masking for proper BOBs. Complete Frogger gameplay.*

*By the end of this phase, the game has roads AND river, logs to ride, turtles that dive, crocodiles, and bonus items. It's complete Frogger.*

---

### Unit 17: Blitter Masking (Cookie Cut)

**Learning Objectives:**
- Understand cookie-cut compositing
- Use mask for shaped objects
- Draw BOBs over background
- Preserve background pixels

**Concepts Introduced:**
- Cookie-cut concept
- Mask (stencil) data
- Minterm selection for A,B,C,D channels
- Proper BOB drawing

**Code Written:**
```asm
cookie_cut:
    ; A = mask, B = object, C = background, D = destination
    move.l  #mask,BLTAPT(a6)
    move.l  #object,BLTBPT(a6)
    move.l  #screen,BLTCPT(a6)
    move.l  #screen,BLTDPT(a6)
    move.w  #$0FCA,BLTCON0(a6)  ; Cookie-cut minterms
    ; ... modulos and size
```

**What the Learner Sees:**
Shaped objects appear on screen without rectangular boxes. Proper game graphics.

**Technical Details:**
- Minterms: $0FCA for cookie-cut
- All 4 channels (A, B, C, D) used
- Mask: 1 where object, 0 where background shows through

---

### Unit 18: Improved Car Graphics

**Learning Objectives:**
- Apply cookie-cut to cars
- Design proper car shapes
- Multiple car designs
- Smooth drawing

**Code Written:**
- Car graphics with masks
- Cookie-cut drawing routine
- Different car types per lane

**What the Learner Sees:**
Cars now have proper shapes, not just rectangles. Different coloured cars.

---

### Unit 19: The River Section

**Learning Objectives:**
- Add river lanes to playfield
- Different collision rules for water
- Plan log mechanics
- Extend Copper list

**Concepts Introduced:**
- Lane types (road vs river)
- Water as deadly zone
- Platform concept
- Zone-specific rules

**Code Written:**
```asm
LANE_ROAD   = 0
LANE_RIVER  = 1

lane_type:  dc.b    LANE_ROAD,LANE_ROAD,LANE_ROAD,LANE_ROAD,LANE_ROAD
            dc.b    LANE_RIVER,LANE_RIVER,LANE_RIVER,LANE_RIVER,LANE_RIVER
```

**What the Learner Sees:**
River section visible with blue water. Entering water without a log = death.

---

### Unit 20: Logs

**Learning Objectives:**
- Draw logs as BOBs
- Move logs across river
- Multiple log sizes
- Screen wrapping

**Code Written:**
```asm
NUM_LOGS = 12
log_x:      ds.w    NUM_LOGS
log_y:      ds.w    NUM_LOGS
log_size:   ds.w    NUM_LOGS    ; 0=short, 1=medium, 2=long
log_speed:  ds.w    NUM_LOGS
```

**What the Learner Sees:**
Logs floating across river lanes. Different sizes and speeds.

**Technical Details:**
- Log sizes: 32, 48, 64 pixels wide
- Cookie-cut drawing
- Wrap at screen edges

---

### Unit 21: Log Riding

**Learning Objectives:**
- Detect frog on log
- Move frog with log
- Fall off = death
- Platform attachment

**Concepts Introduced:**
- Platform riding mechanic
- Relative movement
- Attachment/detachment
- Combined collision

**Code Written:**
```asm
attached_log:   dc.w    -1      ; -1 = not attached

check_log_collision:
    ; For each log:
    ;   If frog overlaps log:
    ;       attached_log = log index
    ;       return
    ; If in river and attached_log = -1:
    ;   death (fell in water)

move_with_log:
    ; If attached_log >= 0:
    ;   frog_x += log_speed[attached_log]
```

**What the Learner Sees:**
Frog can hop onto logs and rides them across the river. Miss a log = splash!

---

### Unit 22: Turtles

**Learning Objectives:**
- Add turtle platforms
- Implement diving behaviour
- Unsafe when underwater
- Animation states

**Concepts Introduced:**
- Animated platforms
- State machine per object
- Timer-based state changes
- Conditional safety

**Code Written:**
```asm
TURTLE_SWIMMING = 0
TURTLE_DIVING   = 1
TURTLE_UNDER    = 2

turtle_state:   ds.b    NUM_TURTLES
turtle_timer:   ds.w    NUM_TURTLES
```

**What the Learner Sees:**
Turtles swim across river, periodically diving. Must time jumps carefully.

---

### Unit 23: Crocodiles

**Learning Objectives:**
- Add crocodile hazard
- Safe to ride (body), dangerous (mouth)
- Mouth opens periodically
- Visual warning

**Code Written:**
- Crocodile graphics (open/closed mouth)
- State-based danger
- Warning animation

**What the Learner Sees:**
Some "logs" are crocodiles. Ride the body, avoid the open mouth.

---

### Unit 24: Bonus Flies

**Learning Objectives:**
- Spawn bonus items on logs
- Time-limited appearance
- Collection for points
- Risk/reward

**Code Written:**
```asm
fly_active:     dc.w    0
fly_x:          dc.w    0
fly_y:          dc.w    0
fly_timer:      dc.w    0

spawn_fly:
    ; Random chance each frame
    ; Place on random log
    ; Set despawn timer
```

**What the Learner Sees:**
Flies appear occasionally on logs. Collect for 200 bonus points.

---

### Unit 25: Home Zone Hazards

**Learning Objectives:**
- Add alligators blocking homes
- Timing for safe entry
- Late-game challenge

**What the Learner Sees:**
Some home zones temporarily blocked by alligators. Must wait or choose another.

---

### Unit 26: Water Animation

**Learning Objectives:**
- Animate water surface
- Copper colour cycling
- Ambient motion effect

**Code Written:**
- Water colours in palette
- Rotate colours via Copper or VBlank
- Subtle shimmer effect

**What the Learner Sees:**
River water appears to flow and shimmer.

---

### Unit 27: Improved Death Effects

**Learning Objectives:**
- Different death animations
- Squash (car), splash (water)
- Visual feedback

**Code Written:**
- Squash animation frames
- Splash animation frames
- Trigger appropriate version

**What the Learner Sees:**
Hit by car = squash. Fall in water = splash. Better feedback.

---

### Unit 28: Level Variety

**Learning Objectives:**
- Different layouts per level
- Vary obstacle patterns
- Maintain difficulty curve

**Code Written:**
- Level data tables
- Pattern variation
- Difficulty parameters per level

**What the Learner Sees:**
Each level feels slightly different. Not just faster, but varied.

---

### Unit 29: Female Frog Bonus

**Learning Objectives:**
- Bonus escort objective
- Carry to home for extra points
- Optional challenge

**Code Written:**
- Female frog sprite
- Pickup mechanic
- Escort to home
- Bonus scoring

**What the Learner Sees:**
Pink frog appears on logs. Rescue her for big bonus.

---

### Unit 30: HUD Improvements

**Learning Objectives:**
- Better score display
- Level indicator
- Time bar visualisation

**What the Learner Sees:**
Cleaner HUD with all information visible at a glance.

---

### Unit 31: Integration Testing

**Learning Objectives:**
- Test all river mechanics
- Verify log/turtle/croc interactions
- Balance difficulty

**Code Written:**
- Bug fixes
- Balance adjustments

**What the Learner Sees:**
All systems working together smoothly.

---

### Unit 32: Phase 2 Complete

**Learning Objectives:**
- Full game verification
- Polish pass
- Phase milestone

**What the Learner Sees:**
Complete Frogger game with roads AND river. All hazards, bonuses, and mechanics working.

**Phase 2 Checkpoint:**
The game now has complete Frogger gameplay: roads with cars, river with logs/turtles/crocodiles, bonus items, water animation, and proper death effects. It's a real Amiga game.

---

## Phase 3: Polish (Units 33-48)

*Goal: Professional presentation - animated title, menus, music, visual effects.*

*By the end of this phase, the game has animated title screen, attract mode, high score table, options menu, background music, Copper visual effects, and polished transitions. Commercial presentation quality.*

---

### Unit 33: Title Screen Design

**Learning Objectives:**
- Design impactful title screen layout
- Create game logo graphics
- Plan menu structure
- Establish visual identity

**Concepts Introduced:**
- Title screen composition
- Logo design principles
- Colour palette for branding
- Menu layout planning

**Code Written:**
```asm
title_screen:
    ; Load title graphics
    ; Display "SIGNAL" logo
    ; Show menu options
    ; Position cursor

menu_options:
    dc.b    "START GAME",0
    dc.b    "OPTIONS",0
    dc.b    "HIGH SCORES",0
```

**What the Learner Sees:**
Professional title screen with large logo and clear menu options. Looks like a commercial game.

---

### Unit 34: Title Animation

**Learning Objectives:**
- Animate title elements via Copper
- Implement colour cycling
- Create visual interest
- Loop animations smoothly

**Concepts Introduced:**
- Copper palette animation
- Colour cycling tables
- Sine-wave movement
- Frame-based animation timing

**Code Written:**
```asm
animate_title:
    ; Rotate logo colours via Copper
    ; Pulse menu cursor
    ; Update animation frame
    ; Smooth cycling

colour_cycle:
    ; Table of gradient colours
    ; Advance index each frame
    ; Write to Copper list
```

**What the Learner Sees:**
Title screen comes alive. Logo shimmers with cycling colours, cursor pulses. The game feels alive before playing.

---

### Unit 35: Menu Navigation

**Learning Objectives:**
- Implement joystick menu control
- Provide visual selection feedback
- Handle menu state transitions
- Create responsive UI

**Concepts Introduced:**
- Menu state management
- Cursor navigation
- Selection confirmation
- Input debouncing for menus

**Code Written:**
```asm
menu_cursor:    dc.w    0       ; Current selection

handle_menu:
    ; Read joystick
    ; Up/down moves cursor
    ; Fire confirms selection
    ; Update cursor display

update_cursor:
    ; Highlight current option
    ; Dehighlight others
```

**What the Learner Sees:**
Navigate menus with joystick. Selection clearly highlighted. Press fire to choose. Responsive and intuitive.

---

### Unit 36: Attract Mode

**Learning Objectives:**
- Implement auto-play demonstration
- Script or AI-control gameplay
- Return to title on input
- Cycle from title after timeout

**Concepts Introduced:**
- Demo playback system
- Simple AI for demonstration
- Attract cycle timing
- Input interruption

**Code Written:**
```asm
ATTRACT_TIMEOUT = 500   ; Frames before attract starts

attract_mode:
    ; AI controls frog
    ; Simple pattern: hop toward nearest home
    ; Avoid obvious cars
    ; Any input returns to title

attract_ai:
    ; Determine safe direction
    ; Execute hop
    ; Basic pathfinding
```

**What the Learner Sees:**
Leave game idle → it plays itself, demonstrating gameplay. Press any button to return to title.

---

### Unit 37: Options Screen

**Learning Objectives:**
- Create options menu
- Implement setting toggles
- Apply settings to gameplay
- Save user preferences

**Concepts Introduced:**
- Settings data structure
- Toggle UI pattern
- Value adjustment controls
- Settings application

**Code Written:**
```asm
options:
    lives_setting:      dc.w    3   ; 3, 5, or 7
    start_level:        dc.w    1   ; 1-5
    sound_enabled:      dc.w    1   ; 0 or 1

options_screen:
    ; Display current settings
    ; Left/right adjusts values
    ; Fire returns to title
```

**What the Learner Sees:**
Options menu with adjustable settings: starting lives (3/5/7), starting level (1-5), sound on/off. Settings apply to next game.

---

### Unit 38: High Score Table

**Learning Objectives:**
- Track top 10 scores
- Implement name entry
- Display formatted leaderboard
- Sort and insert scores

**Concepts Introduced:**
- Score data structure
- Name entry UI (3 letters)
- Sorting/insertion algorithms
- Display formatting

**Code Written:**
```asm
NUM_HIGH_SCORES = 10

high_scores:
    ds.l    NUM_HIGH_SCORES     ; Score values
    ds.b    NUM_HIGH_SCORES*4   ; Names (3 chars + null)

check_high_score:
    ; Compare against table
    ; If qualifies: trigger name entry
    ; Insert in sorted position

name_entry:
    ; Display alphabet
    ; Joystick selects letter
    ; Fire confirms
```

**What the Learner Sees:**
High score table with names and scores. New high score prompts name entry with joystick-controlled letter selection.

---

### Unit 39: MOD Music Basics

**Learning Objectives:**
- Understand MOD file format
- Implement basic replay routine
- Play background music
- Understand pattern sequencing

**Concepts Introduced:**
- MOD format structure (samples, patterns, sequence)
- Pattern-based playback
- Sample triggering via Paula
- Tick-based timing

**Code Written:**
```asm
mod_player:
    ; Parse MOD header
    ; Load sample pointers
    ; Set up pattern sequence
    ; Play routine called each tick

play_tick:
    ; Advance pattern position
    ; Trigger notes on channels
    ; Handle effects (volume, pitch)
```

**What the Learner Sees:**
Background music plays! Four-channel MOD music during gameplay. The Amiga sound.

**Technical Details:**
- MOD format: 4 channels, 31 samples
- Pattern: 64 rows of note data
- Tick rate: typically 6 ticks per row at 125 BPM

---

### Unit 40: Music Integration

**Learning Objectives:**
- Different music per game state
- Smooth music transitions
- Volume control
- Performance budgeting

**Concepts Introduced:**
- State-based music selection
- Music fade in/out
- Volume adjustment
- CPU time management

**Code Written:**
```asm
music_state:    dc.w    MUSIC_TITLE

set_music:
    ; Fade out current
    ; Load new module
    ; Fade in

music_volume:
    ; Adjust Paula volumes
    ; Smooth transitions
```

**What the Learner Sees:**
Title has one tune, gameplay another. Clean transitions between states. Music pauses when game pauses.

---

### Unit 41: Copper Sky Gradient

**Learning Objectives:**
- Create per-line colour gradient
- Build dynamic Copper list
- Implement time-of-day effect
- Add visual depth

**Concepts Introduced:**
- Copper WAIT per scanline
- Gradient colour calculation
- Dynamic Copper list building
- Visual atmosphere

**Code Written:**
```asm
build_sky_gradient:
    ; For each line in sky area:
    ;   Calculate gradient colour
    ;   Add WAIT for line
    ;   Add MOVE to COLOR00
    ; Terminate Copper list

gradient_colour:
    ; Interpolate between top and horizon colours
    ; Smooth blue-to-orange transition
```

**What the Learner Sees:**
Beautiful gradient sky above the playfield, transitioning from deep blue to orange at the horizon. Distinctly Amiga.

---

### Unit 42: Level Complete Effects

**Learning Objectives:**
- Celebrate level completion
- Display bonus calculation
- Create transition to next level
- Provide positive feedback

**Concepts Introduced:**
- Victory effects
- Score count-up animation
- Screen transitions
- Celebration timing

**Code Written:**
```asm
level_complete:
    ; Flash all homes
    ; Play victory jingle
    ; Count up time bonus
    ; Fade to next level

bonus_countup:
    ; Display "TIME BONUS"
    ; Tick up points visually
    ; Sound per tick
```

**What the Learner Sees:**
Completing level triggers celebration: homes flash, bonus points count up audibly, smooth transition to next level.

---

### Unit 43: Pause System

**Learning Objectives:**
- Implement pause functionality
- Create pause menu overlay
- Resume cleanly
- Handle pause during music

**Concepts Introduced:**
- Pause state
- State preservation
- Overlay rendering
- Music pause/resume

**Code Written:**
```asm
paused:     dc.w    0

handle_pause:
    ; Check pause button
    ; If pressed: toggle pause state
    ; Pause music
    ; Show pause menu

pause_menu:
    ; RESUME
    ; RESTART LEVEL
    ; QUIT TO TITLE
```

**What the Learner Sees:**
Press P (or Start) to pause. Overlay menu appears. Resume continues exactly where left off. Music pauses too.

---

### Unit 44: Screen Transitions

**Learning Objectives:**
- Implement fade effects
- Create smooth state changes
- Use Copper for fades
- Professional feel

**Concepts Introduced:**
- Fade to/from black via Copper
- Palette manipulation
- Transition timing
- Effect queuing

**Code Written:**
```asm
fade_out:
    ; Reduce all palette entries toward black
    ; Each frame: subtract from RGB
    ; Until all zero

fade_in:
    ; Increase from black to target palette
    ; Each frame: add toward target
    ; Until target reached
```

**What the Learner Sees:**
Screens don't cut abruptly. Smooth fades between title, game, results. Professional polish.

---

### Unit 45: Sound Priority

**Learning Objectives:**
- Manage multiple sound effects
- Implement priority system
- Allocate channels appropriately
- Handle sound conflicts

**Concepts Introduced:**
- Sound priority levels
- Channel allocation
- Sound queuing
- Interruption rules

**Code Written:**
```asm
PRIORITY_DEATH  = 3     ; Highest
PRIORITY_SCORE  = 2
PRIORITY_HOP    = 1     ; Lowest

play_sound_priority:
    ; Check if channel busy
    ; Compare priorities
    ; If new higher: interrupt
    ; Else: queue or skip
```

**What the Learner Sees:**
Important sounds (death) always play. Less important sounds (hop) yield to higher priority. No audio glitches.

---

### Unit 46: Additional Sound Effects

**Learning Objectives:**
- Add variety to audio
- Create ambient sounds
- Implement car horns
- Polish audio experience

**Concepts Introduced:**
- Sound variety
- Random sound selection
- Ambient audio
- Audio polish

**Code Written:**
```asm
; New samples:
; - Car horn (triggered randomly by cars)
; - Ambient river (looping)
; - Level complete jingle
; - Game over jingle

random_car_horn:
    ; Small chance each frame
    ; Play horn from random car
```

**What the Learner Sees:**
Richer audio: occasional car horns, ambient water sounds, distinct jingles for win/lose. Game sounds complete.

---

### Unit 47: Polish Pass

**Learning Objectives:**
- Review entire game
- Fix visual inconsistencies
- Tighten timing
- Final adjustments

**Concepts Introduced:**
- Polish methodology
- Detail attention
- Quality threshold
- Pre-release review

**Code Written:**
- Alignment fixes
- Colour adjustments
- Timing refinements
- Bug fixes

**What the Learner Sees:**
Subtle improvements throughout. Colours more consistent, timing tighter, everything more refined.

---

### Unit 48: Phase 3 Complete

**Learning Objectives:**
- Full integration test
- Feature verification
- Quality sign-off
- Phase milestone

**Concepts Introduced:**
- Release candidate assessment
- Feature completeness check
- Quality bar evaluation
- Phase gate

**Code Written:**
- Final bug fixes
- Documentation updates
- Feature verification

**What the Learner Sees:**
Complete, polished game with professional presentation. Title animation, menus, music, effects, transitions.

**Phase 3 Checkpoint:**
Professional presentation with animated title, attract mode, high scores, options, music, Copper effects, and polished transitions. Commercial quality.

---

## Phase 4: Mastery (Units 49-64)

*Goal: Advanced techniques, optimisation, multiplayer, and distribution.*

*By the end of this phase, the game is optimised for performance, has two-player modes, difficulty options, and is packaged as a bootable disk ready for distribution. Professional release quality.*

---

### Unit 49: Code Review

**Learning Objectives:**
- Review entire codebase architecture
- Document code structure
- Identify optimisation targets
- Plan improvements

**Concepts Introduced:**
- Code review methodology
- Technical debt assessment
- Documentation practices
- Refactoring planning

**Code Written:**
```asm
; Add comprehensive comments
; Document memory map
; Create routine index
; Identify hot paths for optimisation
```

**What the Learner Sees:**
Cleaner, well-documented code. Clear understanding of where time is spent and what can be improved.

---

### Unit 50: Memory Optimisation

**Learning Objectives:**
- Reduce memory footprint
- Compress graphics data
- Optimise data structures
- Free chip RAM for future use

**Concepts Introduced:**
- Memory profiling
- RLE compression for graphics
- Data packing techniques
- Chip RAM budgeting

**Code Written:**
```asm
; RLE decompress routine
decompress_rle:
    ; Read byte
    ; If high bit set: repeat next byte N times
    ; Else: copy N literal bytes

; Pack multiple flags into single bytes
; Reuse memory where possible
```

**What the Learner Sees:**
Same game, smaller memory use. Graphics compressed. More room for additional content.

**Technical Details:**
- Before: ~100KB graphics
- After: ~60KB compressed
- Decompression during load

---

### Unit 51: Blitter Optimisation

**Learning Objectives:**
- Optimise Blitter operations
- Use interleaved bitplane format
- Combine operations
- Maximise throughput

**Concepts Introduced:**
- Interleaved vs planar format
- Blitter scheduling
- Combined erase/draw operations
- DMA efficiency

**Code Written:**
```asm
; Convert to interleaved format
; Single blit draws all bitplanes
; Combine background restore with object draw
; Optimal modulo calculations
```

**What the Learner Sees:**
More objects possible. Smoother animation. Better performance headroom.

**Technical Details:**
- Interleaved: all planes in one blit
- Reduces blit count by 5x (for 5 planes)
- More complex setup, faster execution

---

### Unit 52: CPU/Blitter Parallelism

**Learning Objectives:**
- Do CPU work during Blitter operations
- Avoid blocking waits
- Schedule work efficiently
- Maximise throughput

**Concepts Introduced:**
- CPU/Blitter parallelism
- Deferred Blitter waits
- Work scheduling patterns
- Resource utilisation

**Code Written:**
```asm
game_loop:
    ; Start background restore blit
    jsr start_restore_blit

    ; Do CPU work while Blitter runs
    jsr update_game_logic
    jsr read_input
    jsr update_positions

    ; Now wait for Blitter (probably already done)
    jsr wait_blitter

    ; Start object drawing
    jsr draw_objects
```

**What the Learner Sees:**
More responsive game. Better frame rate. CPU and Blitter working in parallel.

---

### Unit 53: Advanced Copper

**Learning Objectives:**
- Build Copper lists dynamically
- Implement per-line effects
- Double-buffer Copper lists
- Advanced timing tricks

**Concepts Introduced:**
- Dynamic Copper list generation
- Copper double-buffering
- Sprite repositioning via Copper
- Scanline effects

**Code Written:**
```asm
build_copper_list:
    ; Generate list based on game state
    ; Add sprite repositions for more sprites
    ; Add per-line colour effects
    ; Swap lists each frame

copper_sprite_multiplex:
    ; Reposition sprite mid-screen
    ; Effectively doubles sprite count
```

**What the Learner Sees:**
More dynamic visual effects. Additional sprites via multiplexing. Effects respond to gameplay.

---

### Unit 54: More Hazards

**Learning Objectives:**
- Add snakes on road edges
- Implement fast car variants
- Create hazard variety
- Balance difficulty

**Concepts Introduced:**
- Enemy variety design
- Behaviour variation
- Difficulty layering
- Content expansion

**Code Written:**
```asm
; Snake hazard
snake_x:        ds.w    NUM_SNAKES
snake_dir:      ds.w    NUM_SNAKES

update_snakes:
    ; Move along road edge
    ; Reverse at boundaries
    ; Collision = death

; Fast car (appears in later levels)
spawn_fast_car:
    ; Double speed
    ; Different colour
    ; Warning sound
```

**What the Learner Sees:**
More variety in hazards. Snakes patrol road edges. Occasional fast cars add surprise.

---

### Unit 55: Two Player (Alternating)

**Learning Objectives:**
- Implement turn-based multiplayer
- Track separate scores
- Handle player switching
- Create competitive mode

**Concepts Introduced:**
- Multiplayer state management
- Per-player data
- Turn alternation logic
- Score comparison

**Code Written:**
```asm
current_player:     dc.w    0
player_scores:      ds.l    2
player_lives:       ds.w    2

switch_player:
    ; Save current player state
    ; Load other player state
    ; Update display
    ; Show "PLAYER X" indicator
```

**What the Learner Sees:**
Two player option in menu. Players take turns on death or home reached. Separate scores. Winner announced.

---

### Unit 56: Two Player (Simultaneous)

**Learning Objectives:**
- Both frogs on screen together
- Separate joystick controls
- Handle player interaction
- Competitive racing

**Concepts Introduced:**
- Simultaneous multiplayer
- Control separation (port 1 vs port 2)
- Player-player collision
- Race mechanics

**Code Written:**
```asm
NUM_PLAYERS = 2

player_x:       ds.w    NUM_PLAYERS
player_y:       ds.w    NUM_PLAYERS
player_state:   ds.w    NUM_PLAYERS

read_both_joysticks:
    ; Read JOY0DAT and JOY1DAT
    ; Decode for each player

check_player_collision:
    ; If players overlap: bump apart
    ; Or: pass through (design choice)
```

**What the Learner Sees:**
Both players on screen simultaneously. Race to fill homes. Can bump each other. Frantic fun.

---

### Unit 57: Statistics Tracking

**Learning Objectives:**
- Track gameplay statistics
- Display session records
- Implement achievements
- Long-term goals

**Concepts Introduced:**
- Statistics collection
- Record tracking
- Achievement system
- Display formatting

**Code Written:**
```asm
stats:
    total_homes:    ds.l    1
    total_deaths:   ds.l    1
    highest_level:  ds.w    1
    fastest_level:  ds.w    1

achievements:
    ; Reach level 5
    ; Score 10,000
    ; Complete level without dying
    ; Rescue 10 female frogs
```

**What the Learner Sees:**
Statistics screen showing total progress. Achievements to unlock. Long-term goals beyond single game.

---

### Unit 58: Difficulty Options

**Learning Objectives:**
- Implement difficulty levels
- Scale game parameters
- Improve accessibility
- Balance challenge

**Concepts Introduced:**
- Difficulty parameters
- Scaling factors
- Accessibility design
- Player choice

**Code Written:**
```asm
DIFF_EASY   = 0
DIFF_NORMAL = 1
DIFF_HARD   = 2

difficulty:     dc.w    DIFF_NORMAL

apply_difficulty:
    ; EASY: slower speeds, more time, fewer hazards
    ; NORMAL: default settings
    ; HARD: faster speeds, less time, more hazards

speed_multiplier:
    dc.w    80, 100, 130    ; Percentages
```

**What the Learner Sees:**
Difficulty option in menu. Easy mode for beginners, Hard for experts. Game accessible to all skill levels.

---

### Unit 59: Final Content

**Learning Objectives:**
- Complete all 8 levels
- Verify difficulty curve
- Finalise patterns
- Content freeze

**Concepts Introduced:**
- Content completion
- Level design finalisation
- Difficulty curve verification
- Feature freeze

**Code Written:**
```asm
; Level data for all 8 levels
; Each level defines:
;   - Car speeds and counts
;   - Log speeds and counts
;   - Turtle/croc frequency
;   - Time limit
;   - Bonus spawn rates
```

**What the Learner Sees:**
Complete game with 8 distinct levels. Clear difficulty progression. Satisfying challenge curve.

---

### Unit 60: Loading Screen

**Learning Objectives:**
- Create loading display
- Establish first impression
- Show branding
- Professional start

**Concepts Introduced:**
- Load-time experience
- First impressions
- Branding display
- Progress indication

**Code Written:**
```asm
loading_screen:
    ; Display logo immediately
    ; Show "LOADING..." text
    ; Optional: progress bar
    ; Transition to title when ready

; Copyright and credits
dc.b    "(C) 2026 CODE198X",0
dc.b    "PROGRAMMING: LEARNER",0
```

**What the Learner Sees:**
Professional loading screen while game loads. Logo, credits, loading indication. Good first impression.

---

### Unit 61: Disk Mastering

**Learning Objectives:**
- Create bootable ADF
- Organise files on disk
- Write boot sector
- Distribution format

**Concepts Introduced:**
- ADF disk format
- Boot block structure
- File organisation
- Bootable disk creation

**Code Written:**
```asm
; Boot block code
boot_block:
    ; Minimal boot code
    ; Load main executable
    ; Jump to start

; Disk layout:
; Track 0: Boot block
; Track 1-79: Game data
```

**What the Learner Sees:**
Game boots directly from disk. No Workbench required. Insert disk, power on, play.

**Technical Details:**
- ADF: 880KB, 80 tracks, 11 sectors
- Boot block: first 1024 bytes
- Checksum required for boot

---

### Unit 62: Compatibility Testing

**Learning Objectives:**
- Test on multiple Amiga models
- Verify A500 compatibility
- Check A1200 compatibility
- Handle hardware differences

**Concepts Introduced:**
- Hardware compatibility
- Chipset variations
- Memory configurations
- Testing methodology

**Code Written:**
```asm
; Detect machine type
detect_machine:
    ; Check for AGA (A1200/A4000)
    ; Check for ECS (A500+/A600)
    ; Check for OCS (A500/A2000)

; Adjust for differences if needed
; (Signal targets OCS, should work everywhere)
```

**What the Learner Sees:**
Game tested and verified on A500, A600, A1200. Works across the Amiga range.

---

### Unit 63: Final Testing

**Learning Objectives:**
- Complete test pass
- Verify all features
- Test edge cases
- Release candidate

**Concepts Introduced:**
- Release testing methodology
- Edge case identification
- Bug triage
- Release readiness criteria

**Code Written:**
- Bug fixes from testing
- Edge case handling
- Final polish

**What the Learner Sees:**
Thoroughly tested game. All features verified. All modes tested. Ready for release.

**Test Checklist:**
- [ ] All 8 levels completable
- [ ] All menu options work
- [ ] High scores save correctly
- [ ] Two-player modes work
- [ ] All difficulty levels balanced
- [ ] Music plays correctly
- [ ] All sound effects trigger
- [ ] Boots on A500 with 512KB

---

### Unit 64: Distribution

**Learning Objectives:**
- Create final distribution package
- Write documentation
- Archive source code
- Release the game

**Concepts Introduced:**
- Distribution packaging
- Documentation writing
- Source archival
- Release process

**Files Created:**
```
SIGNAL.ADF          ; Bootable game disk
README.TXT          ; Game instructions
QUICKREF.TXT        ; Quick reference card
SOURCE.LHA          ; Source code archive
```

**What the Learner Sees:**
Complete distribution package. Professional readme. Source code archived. Game ready to share.

**Phase 4 Checkpoint:**
Complete, optimised, professionally packaged game. Two-player modes, difficulty options, statistics, and achievements. Boots from disk, works on all Amigas. Could have sold for £19.99 in 1987. The learner has built a commercial-quality Amiga game.

---

## Skills Mastery Summary

By completing all 64 units, learners demonstrate mastery of:

### 68000 Assembly
- Registers and addressing modes
- Data movement, arithmetic, logic
- Interrupt handling
- Performance optimisation

### Amiga Custom Chipset
- Agnus: Blitter operations, DMA coordination
- Denise: Display setup, sprites, colours
- Paula: Sample playback, 4-channel audio
- Copper: Display lists, timing, effects

### Game Development
- Game loop structure
- State machine patterns
- Collision detection
- Scoring and progression
- Multiplayer implementation

### Professional Skills
- Code organisation
- Performance optimisation
- Distribution packaging
- Quality assurance

---

## Version History

- **3.1 (2026-01-12):** Expanded Phases 2-4 with full unit descriptions matching Phase 1 detail level.
- **3.0 (2026-01-12):** Complete restructure following "scaffold first, explain later" approach. Sprite visible in Unit 1, interactivity in Unit 2. River moved to Phase 2.
- **2.0 (2026-01-10):** Previous restructure (playable game by Unit 16).
- **1.0 (2026-01-07):** Initial outline (theory-first approach).
