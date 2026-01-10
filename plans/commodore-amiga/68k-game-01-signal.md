# Signal: 64-Unit Outline

**Game:** Amiga Game 1: Signal
**Units:** 64
**Concept:** Frogger-style lane crosser. Cross roads and rivers, avoid cars, ride logs, reach safety zones. A timing game that naturally exercises the entire Amiga custom chipset.

**Commercial Quality Target:** A game that could have sold for £19.99 on disk in 1987. Polished, responsive, with that distinctive Amiga look and sound.

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

## Phase 1: Foundation (Units 1-16)

*Goal: A complete, playable Frogger game. Simple graphics, but fully functional - cross lanes, avoid obstacles, reach home.*

*By the end of this phase, the learner has built a working game. The frog crosses roads, avoids cars (using hardware sprites), reaches home zones, loses lives, and wins levels. It's simple but complete.*

---

### Unit 1: The Amiga Architecture

**Learning Objectives:**
- Understand the Amiga's custom chipset (Agnus, Denise, Paula)
- Know the memory map (chip RAM, custom registers)
- Write a first 68000 assembly program
- See the program run on the Amiga

**Concepts Introduced:**
- 68000 CPU vs custom chips
- Chip RAM vs Fast RAM
- Custom chip base address ($DFF000)
- Program structure (code section)

**Code Written:**
```
- Minimal executable structure
- Set background colour via COLOR00
- Infinite loop to keep program running
- Exit cleanly (optional)
```

**What the Learner Sees:**
The Amiga screen changes to a solid colour. The program runs from their own code. First contact with the custom chipset.

**Technical Details:**
- Custom base: $DFF000
- COLOR00: $DFF180
- Background colour = bits 11-0 (RGB4 format)
- Colour value: $0F00 = bright red

---

### Unit 2: Taking Over the System

**Learning Objectives:**
- Understand why we disable the OS for games
- Save system state for clean exit
- Disable interrupts and DMA
- Restore system on exit

**Concepts Introduced:**
- Exec library and forbid/permit
- Interrupt control (INTENA)
- DMA control (DMACON)
- Saving/restoring state

**Code Written:**
```
- Save interrupt and DMA state
- Disable multitasking (Forbid)
- Disable all interrupts
- Disable all DMA
- On exit: restore everything
```

**What the Learner Sees:**
The Workbench disappears. A blank screen under total program control. Exit returns to Workbench cleanly.

**Technical Details:**
- INTENA: $DFF09A (write), $DFF01C (read)
- DMACON: $DFF096 (write), $DFF002 (read)
- Bit 15: SET/CLR bit
- Exec base at address 4

---

### Unit 3: Display Fundamentals

**Learning Objectives:**
- Understand bitplane display architecture
- Set up display window and data fetch
- Configure a single bitplane
- See pixels on screen

**Concepts Introduced:**
- Bitplanes (1 bit per pixel per plane)
- DIWSTRT/DIWSTOP (display window)
- DDFSTRT/DDFSTOP (data fetch)
- BPLCON0 (bitplane control)

**Code Written:**
```
- Allocate bitplane memory
- Set display window (standard PAL)
- Set data fetch timing
- Configure 1 bitplane
- Point BPL1PT to bitplane
- Enable bitplane DMA
```

**What the Learner Sees:**
A screen showing random memory as pixels. Then a cleared bitplane showing solid colour. The display system works.

**Technical Details:**
- DIWSTRT: $DFF08E (typically $2C81)
- DIWSTOP: $DFF090 (typically $2CC1)
- DDFSTRT: $DFF092 (typically $0038)
- DDFSTOP: $DFF094 (typically $00D0)
- BPLCON0: $DFF100

---

### Unit 4: The Copper

**Learning Objectives:**
- Understand the Copper coprocessor
- Write a basic Copper list
- Use Copper to set up display
- Change colours mid-screen

**Concepts Introduced:**
- Copper as display list processor
- WAIT instruction (wait for beam position)
- MOVE instruction (write to register)
- Copper list termination

**Code Written:**
```
- Create Copper list in memory
- Set display registers via Copper
- Set palette colours via Copper
- Add colour change mid-screen
- Point COP1LC to list
- Enable Copper DMA
```

**What the Learner Sees:**
A split-colour screen - different colours in top and bottom halves. The Copper controls the display without CPU intervention.

**Technical Details:**
- COP1LC: $DFF080-082 (Copper list pointer)
- Copper WAIT: $VVHH, $FFFE (wait for position)
- Copper MOVE: $0RRR, $DDDD (register, data)
- Copper end: $FFFF, $FFFE

---

### Unit 5: The Game Display

**Learning Objectives:**
- Plan the game screen layout
- Set up 5 bitplanes (32 colours)
- Draw road and river zones
- Create a proper playfield

**Concepts Introduced:**
- Multiple bitplanes
- Modulo for screen width
- Colour palette design
- Zone-based background

**Code Written:**
```
- Allocate 5 bitplanes
- Configure 32-colour display
- Set Copper palette (road grey, water blue, grass green)
- Use Copper for zone colours
- Clear screen to background colours
```

**What the Learner Sees:**
A proper game playfield: green safe zones at top and middle, grey road section, blue river section, green start zone at bottom. The stage is set.

**Technical Details:**
- 5 bitplanes = 32 colours
- Each bitplane: 320/8 × 256 = 10,240 bytes
- Total: 51,200 bytes for display
- Modulo: 0 for standard width

---

### Unit 6: Hardware Sprites

**Learning Objectives:**
- Understand Amiga hardware sprites
- Create sprite data structure
- Display a sprite on screen
- Set sprite colours

**Concepts Introduced:**
- Sprite DMA channels (8 sprites)
- Sprite data format (control words + image)
- Sprite positioning (SPRPOS, SPRCTL)
- Sprite colours (SPRxCOL)

**Code Written:**
```
- Create sprite data (control + image)
- Set sprite position
- Point SPR0PT to sprite data
- Set sprite colours
- Enable sprite DMA
```

**What the Learner Sees:**
A small coloured shape appears on screen - the first hardware sprite. It can be moved by changing the control words.

**Technical Details:**
- SPR0PT: $DFF120 (sprite 0 pointer)
- Sprite format: 2 control words, then pairs of data words
- Control word 1: VSTART, HSTART
- Control word 2: VSTOP, control bits
- 3 colours + transparent per sprite

---

### Unit 7: The Player Frog

**Learning Objectives:**
- Design the frog sprite (16×16 pixels)
- Display frog at starting position
- Plan movement grid
- Understand sprite positioning maths

**Concepts Introduced:**
- Sprite design (16 wide, variable height)
- Grid-based positioning
- Screen coordinates vs game grid
- Sprite attachment (for more colours, future use)

**Code Written:**
```
- Frog sprite data (16×16)
- Calculate grid cell to screen position
- Place frog at bottom centre
- Store frog grid position in variables
- Display frog correctly
```

**What the Learner Sees:**
A recognisable frog sprite at the bottom of the playfield. Positioned on the starting zone, ready to hop.

**Technical Details:**
- Grid: 20 columns × 13 rows
- Cell size: 16×16 pixels
- Screen offset: adjust for centring
- Starting position: row 0, column 10

---

### Unit 8: Joystick Input

**Learning Objectives:**
- Read joystick from CIA port
- Detect direction presses
- Handle fire button
- Debounce input

**Concepts Introduced:**
- CIA-A port register ($BFE001)
- Joystick direction bits
- JOYxDAT register (alternative)
- Edge detection for presses

**Code Written:**
```
- Read joystick port
- Decode up/down/left/right
- Detect new presses (not held)
- Store direction in variable
- Visual feedback (border flash)
```

**What the Learner Sees:**
Pressing joystick directions causes the border to flash in different colours. Input is detected and debounced properly.

**Technical Details:**
- CIA-A: $BFE001
- JOY1DAT: $DFF00C (mouse/joy port 1)
- Direction decoding from bit differences
- Fire: CIA-A bit 7 (directly readable)

---

### Unit 9: Frog Movement

**Learning Objectives:**
- Move frog in response to input
- Animate hop movement
- Constrain to grid
- Respect screen boundaries

**Concepts Introduced:**
- Grid-based movement
- Movement state (idle, hopping)
- Frame-by-frame animation
- Boundary checking

**Code Written:**
```
- Movement state variable
- On input: start hop in direction
- Each frame: move sprite partway
- On hop complete: snap to grid
- Check boundaries before moving
```

**What the Learner Sees:**
The frog hops smoothly in the direction pushed. Movement is grid-aligned. Can't move off screen. Feels responsive.

**Technical Details:**
- Hop duration: 8 frames
- Pixels per frame: 2 (16 pixels / 8 frames)
- Movement state: 0=idle, 1-8=hopping
- Direction stored during hop

---

### Unit 10: VBlank and Timing

**Learning Objectives:**
- Understand VBlank interrupt
- Set up interrupt handler
- Synchronise game to frame rate
- Consistent 50Hz update

**Concepts Introduced:**
- Vertical blank period
- Interrupt vectors
- Level 3 interrupt (VBlank)
- Frame-based timing

**Code Written:**
```
- Set up VBlank interrupt handler
- Enable VBlank interrupt
- Main loop waits for VBlank flag
- Game logic runs once per frame
- Stable 50 FPS
```

**What the Learner Sees:**
Frog movement is now perfectly smooth and consistent. No variation in speed. Professional game feel.

**Technical Details:**
- Level 3 autovector: $6C
- INTENA bit 5: VERTB (vertical blank)
- INTREQ: $DFF09C (acknowledge)
- 50 Hz PAL, 60 Hz NTSC

---

### Unit 11: Obstacles - Cars

**Learning Objectives:**
- Use additional sprites for cars
- Move cars across lanes
- Handle screen wrapping
- Different speeds per lane

**Concepts Introduced:**
- Multiple sprite management
- Horizontal wrapping
- Lane data structure
- Speed variation

**Code Written:**
```
- Car sprite data (simple rectangle)
- 4 cars using sprites 1-4
- Each car has: x, y, speed, lane
- Update positions each frame
- Wrap at screen edges
```

**What the Learner Sees:**
Cars move across the road lanes at different speeds. Some go left, some go right. They wrap around the screen edges.

**Technical Details:**
- Sprites 1-4 for cars
- Lane speeds: 1, 2, -1, -2 (pixels/frame)
- Wrap: if x > 336, x = 0; if x < 0, x = 336
- Y fixed per lane

---

### Unit 12: Collision Detection

**Learning Objectives:**
- Detect frog-car collision
- Handle death event
- Implement lives system
- Respawn after death

**Concepts Introduced:**
- Bounding box collision
- Hardware collision detection (CLXDAT)
- Death animation
- Respawn logic

**Code Written:**
```
- Check bounding box overlap
- Or use CLXDAT sprite collision
- On collision: trigger death
- Death: play sound, flash, lose life
- Respawn at start position
```

**What the Learner Sees:**
Hitting a car causes the frog to "die" - a brief flash, and it reappears at the start. Lives counter decreases.

**Technical Details:**
- CLXDAT: $DFF00E (collision data)
- Bounding box: simpler and more control
- Collision margin: 2-4 pixels for fairness
- Lives: start with 3

---

### Unit 13: Safe Zones and Goals

**Learning Objectives:**
- Define home zone positions
- Detect frog reaching home
- Mark home as filled
- Track level completion

**Concepts Introduced:**
- Goal zones
- Zone state (empty, filled)
- Score on reaching goal
- Level complete condition

**Code Written:**
```
- 5 home zones across top
- Check if frog Y at top row
- Check if frog X in home zone
- If home empty: fill it, award points
- If all homes filled: level complete
```

**What the Learner Sees:**
Reaching a home zone at the top fills it in (colour change) and scores points. The frog respawns. Fill all 5 to complete the level.

**Technical Details:**
- Home zones: columns 2, 6, 10, 14, 18
- Home width: 2 grid cells
- Points per home: 50
- Level complete: all 5 filled

---

### Unit 14: Game States

**Learning Objectives:**
- Implement state machine (title, playing, game over)
- Handle transitions between states
- Create simple title screen
- Display game over

**Concepts Introduced:**
- Game state variable
- State machine pattern
- State initialisation
- Key/button to start

**Code Written:**
```
- game_state: TITLE, PLAYING, GAME_OVER
- Main loop dispatches to state handler
- TITLE: show text, wait for fire
- PLAYING: run game logic
- GAME_OVER: show message, wait, → TITLE
```

**What the Learner Sees:**
Game starts with title screen. Press fire to play. Game over returns to title. Proper game flow.

**Technical Details:**
- States: 0=TITLE, 1=PLAYING, 2=GAME_OVER
- Simple text display using Blitter (or pre-drawn)
- Transition on fire button

---

### Unit 15: Score and Lives Display

**Learning Objectives:**
- Display score on screen
- Display remaining lives
- Update efficiently
- Format numbers

**Concepts Introduced:**
- Number to text conversion
- Blitter text (or sprite numbers)
- HUD area reservation
- Efficient updates

**Code Written:**
```
- Reserve top 16 pixels for HUD
- Score: 6-digit display
- Lives: numeric or icons
- Update only when changed
- Binary to decimal conversion
```

**What the Learner Sees:**
Score and lives displayed at top of screen. Score increases when reaching homes. Lives decrease on death.

**Technical Details:**
- Score: 32-bit value
- Display as 6 decimal digits
- Lives: simple icons or number 0-9
- HUD above playfield

---

### Unit 16: Complete Frog Game

**Learning Objectives:**
- Polish the complete experience
- Verify all game paths
- Add level restart
- Celebrate completion

**Concepts Introduced:**
- Integration testing
- Edge cases
- Game loop completeness
- Phase milestone

**Code Written:**
```
- Level complete: brief celebration, restart harder
- Speed increase per level
- Final testing pass
- Fix any remaining issues
```

**What the Learner Sees:**
A complete, playable Frogger game. Cross roads, avoid cars, reach homes. Die, respawn, game over, restart. Simple but fully functional.

**Phase 1 Checkpoint:**
The learner has built a working game. Hardware sprites for the frog and cars, joystick input, collision detection, scoring, lives, and level completion. It's simple (no river yet, no Blitter graphics) but complete. Everything from here builds on this foundation.

---

## Phase 2: Expansion (Units 17-32)

*Goal: Add the river section, log riding, Blitter graphics, and sound. Transform the simple game into proper Frogger.*

*By the end of this phase, the game has roads AND river, logs to ride, Blitter-drawn obstacles for more on screen, and Paula sound effects. It looks and sounds like an Amiga game.*

---

### Unit 17: The Blitter Concept

**Learning Objectives:**
- Understand the Blitter's role
- Know the difference between sprites and BOBs
- Understand Blitter channels (A, B, C, D)
- Prepare for Blitter graphics

**Concepts Introduced:**
- Blitter as DMA graphics engine
- BOBs (Blitter Objects) vs sprites
- Source and destination channels
- Why we need the Blitter

**Code Written:**
```
- Blitter register overview
- Simple fill operation
- Wait for Blitter (BLTBUSY)
- Theory unit, minimal code
```

**What the Learner Sees:**
Understanding of why 8 sprites isn't enough for a full game, and how the Blitter provides the solution.

**Technical Details:**
- BLTCON0: $DFF040 (control)
- BLTCON1: $DFF042 (control 2)
- BLTxPT: pointers for A, B, C, D
- BLTSIZE: $DFF058 (triggers blit)

---

### Unit 18: Blitter Copy

**Learning Objectives:**
- Perform a simple Blitter copy
- Understand source and destination
- Set up modulos correctly
- Wait for completion

**Concepts Introduced:**
- A→D copy operation
- Modulo calculation
- BLTSIZE encoding
- Blitter wait loop

**Code Written:**
```
- Set up source pointer (A)
- Set up destination pointer (D)
- Configure modulos
- Set BLTCON0 for A→D copy
- Set BLTSIZE to trigger
- Wait for completion
```

**What the Learner Sees:**
A rectangle copied from one screen location to another. The Blitter works independently of the CPU.

**Technical Details:**
- BLTCON0: $09F0 for A→D with all minterms
- BLTAMOD, BLTDMOD: modulo values
- BLTSIZE: (height << 6) | (width_in_words)
- Wait: check DMACON bit 14

---

### Unit 19: Blitter Masking (Cookie Cut)

**Learning Objectives:**
- Understand cookie-cut mode
- Use mask data for shaped objects
- Draw object over background
- Proper BOB compositing

**Concepts Introduced:**
- Cookie-cut concept
- Mask (stencil) channel
- Minterm selection
- Preserving background

**Code Written:**
```
- Create object with mask
- Configure A (mask), B (object), C (background), D (output)
- Set minterms for cookie-cut
- Draw masked object
```

**What the Learner Sees:**
A shaped object (car or log) appears on the background without a rectangular box around it. Proper game graphics.

**Technical Details:**
- Cookie-cut minterms: $0FCA
- A=mask, B=object, C=background, D=destination
- All four channels active
- Mask: 1 where object, 0 where background shows

---

### Unit 20: BOB Cars

**Learning Objectives:**
- Replace sprite cars with Blitter BOBs
- Draw multiple cars efficiently
- Erase and redraw each frame
- Handle many more cars

**Concepts Introduced:**
- BOB lifecycle (erase, draw)
- Save-behind for erasure
- Sorted draw order
- Performance considerations

**Code Written:**
```
- Car BOB graphics data
- Erase old positions
- Draw at new positions
- 8+ cars now possible
```

**What the Learner Sees:**
More cars on screen than the 8-sprite limit allowed. Traffic is denser and more challenging.

**Technical Details:**
- Erase: restore background (or clear)
- Draw: cookie-cut each car
- Order: erase all, then draw all
- Performance: Blitter is fast

---

### Unit 21: The River Section

**Learning Objectives:**
- Add river lanes to display
- Different collision rules for water
- Introduce log concept
- Plan river mechanics

**Concepts Introduced:**
- Water as deadly (without log)
- Logs as platforms
- Lane types (road vs river)
- Platform riding

**Code Written:**
```
- Add river lanes to level data
- Lane type flag (road/river)
- Water = death if not on log
- Visual distinction
```

**What the Learner Sees:**
River section visible in the playfield. Blue water between the road and top safe zones.

**Technical Details:**
- 5 river lanes above safe zone
- 5 road lanes below safe zone
- Water colour: palette modification
- Lane data includes type

---

### Unit 22: Logs and Platforms

**Learning Objectives:**
- Draw logs as BOBs
- Logs move across lanes
- Logs wrap at screen edges
- Multiple log sizes

**Concepts Introduced:**
- Platform objects
- Log lengths (short, medium, long)
- Wrapping platforms
- Platform array

**Code Written:**
```
- Log BOB graphics (3 sizes)
- Log data: x, y, size, speed
- Draw logs each frame
- Wrap at screen edges
```

**What the Learner Sees:**
Logs floating across river lanes, moving left and right at different speeds. They wrap around screen edges.

**Technical Details:**
- Log sizes: 32, 48, 64 pixels wide
- Log array: 12-16 logs
- Mixed with cars in object list
- Or separate rendering pass

---

### Unit 23: Log Riding

**Learning Objectives:**
- Detect frog on log
- Frog moves with log
- Fall off = water death
- Safe while on log

**Concepts Introduced:**
- Platform attachment
- Relative movement
- Detachment on hop
- Combined collision

**Code Written:**
```
- Check frog overlaps log
- If on river and on log: safe, move with log
- If on river and not on log: death
- Detach when hopping
```

**What the Learner Sees:**
Frog can hop onto logs and ride them across the river. Falling in water causes death. River is crossable.

**Technical Details:**
- Check each log for overlap
- attached_log variable
- Add log.dx to frog.x each frame
- Clear attachment on movement input

---

### Unit 24: Turtles

**Learning Objectives:**
- Add turtle platforms
- Turtles dive underwater periodically
- Unsafe when diving
- Animation states

**Concepts Introduced:**
- Animated platforms
- State: swimming, diving, surfacing
- Timer-based state changes
- Conditional safety

**Code Written:**
```
- Turtle BOB graphics (3 frames)
- Turtle state machine
- Diving timer
- Only safe when swimming
```

**What the Learner Sees:**
Turtles swim across river, periodically diving. Must time jumps to catch them when safe.

**Technical Details:**
- Turtle states: 0=swimming, 1=diving, 2=underwater
- Dive cycle: ~120 frames
- Animation frames during state
- Check state for safety

---

### Unit 25: Paula Audio Basics

**Learning Objectives:**
- Understand Paula audio channels
- Set up sample playback
- Play a simple sound
- Control volume and period

**Concepts Introduced:**
- 4 audio channels
- Sample format (8-bit signed)
- AUDxLC, AUDxLEN, AUDxPER, AUDxVOL
- DMA audio playback

**Code Written:**
```
- Load/create sample data
- Set sample pointer and length
- Set period (pitch)
- Set volume
- Enable audio DMA
```

**What the Learner Sees:**
A sound plays from the Amiga! First audio output from their code.

**Technical Details:**
- AUD0LC: $DFF0A0 (sample pointer)
- AUD0LEN: $DFF0A4 (length in words)
- AUD0PER: $DFF0A6 (period)
- AUD0VOL: $DFF0A8 (volume 0-64)

---

### Unit 26: Sound Effects

**Learning Objectives:**
- Create game sound effects
- Trigger sounds on events
- Hop, death, splash, home sounds
- Sound priority

**Concepts Introduced:**
- Sound effect triggering
- Channel allocation
- Priority (death over hop)
- Short one-shot samples

**Code Written:**
```
- 4 sound effects (hop, death, splash, score)
- play_sound routine
- Trigger on events
- Simple priority system
```

**What the Learner Sees:**
Hopping makes a sound. Deaths have a splash. Reaching home celebrates. The game has audio.

**Technical Details:**
- Hop: short pop (~500 samples)
- Death: noise burst (~2000 samples)
- Splash: water sound (~3000 samples)
- Score: ascending tone (~1500 samples)

---

### Unit 27: Timer and Urgency

**Learning Objectives:**
- Add time limit per life
- Display countdown timer
- Death on timeout
- Bonus for time remaining

**Concepts Introduced:**
- Frame-based timer
- Time display
- Timeout handling
- Risk/reward

**Code Written:**
```
- Time limit: 60 seconds
- Decrement each frame
- Display seconds remaining
- Timeout = death
- Bonus points for remaining time
```

**What the Learner Sees:**
Timer counting down adds urgency. Must reach home before time expires. Extra points for speed.

**Technical Details:**
- Frames per second: 50 (PAL)
- Timer: frames remaining
- Display: seconds (timer / 50)
- Bonus: timer × 10 points

---

### Unit 28: Multiple Levels

**Learning Objectives:**
- Implement level progression
- Increase difficulty each level
- Vary traffic patterns
- Track current level

**Concepts Introduced:**
- Level data
- Difficulty scaling
- Pattern variation
- Progression

**Code Written:**
```
- Level number tracking
- Speed multiplier per level
- More objects per level
- Display level number
```

**What the Learner Sees:**
Completing a level moves to the next with faster traffic and tighter gaps. Visible level number.

**Technical Details:**
- Speed scale: 1.0 + (level × 0.1)
- Object count: base + (level × 2)
- Maximum level: 8 or endless
- Level display in HUD

---

### Unit 29: Bonus Items

**Learning Objectives:**
- Add bonus flies on logs
- Time-limited appearance
- Points for collection
- Visual distinction

**Concepts Introduced:**
- Bonus spawning
- Timeout despawn
- Collision with items
- Extra scoring

**Code Written:**
```
- Fly sprite/BOB
- Random spawn timer
- Position on random log
- Collect for bonus points
- Despawn after timeout
```

**What the Learner Sees:**
Occasionally a fly appears on a log. Collecting it gives bonus points. Adds risk/reward.

**Technical Details:**
- Spawn chance: 1/200 per frame
- Despawn after: 300 frames
- Bonus: 200 points
- One fly at a time

---

### Unit 30: Crocodiles

**Learning Objectives:**
- Add crocodile hazard
- Croc looks like log but kills
- Mouth opens = danger
- Adds river hazard

**Concepts Introduced:**
- Hazard platform
- Visual warning
- State-based danger
- Risk assessment

**Code Written:**
```
- Crocodile BOB graphics
- Mouth closed = safe to ride
- Mouth open = death
- Random timing
```

**What the Learner Sees:**
Some "logs" are crocodiles. Their mouths open periodically. Must jump away before they bite.

**Technical Details:**
- Croc states: closed, opening, open, closing
- Open mouth = death on contact
- Cycle timing: random 150-250 frames
- Warning: opening animation

---

### Unit 31: Home Zone Hazards

**Learning Objectives:**
- Add alligators in homes
- Some homes temporarily blocked
- Must time approach
- Adds endgame challenge

**Concepts Introduced:**
- Goal hazards
- Blocking state
- Clear timing
- Late-game difficulty

**Code Written:**
```
- Alligator in home animation
- Home blocked when occupied
- Wait for clear
- Only 1-2 homes blocked at once
```

**What the Learner Sees:**
Some home zones have alligators blocking them. Must wait for them to leave or choose another home.

**Technical Details:**
- Random home selection
- Block duration: 100-200 frames
- Maximum 2 blocked simultaneously
- Higher levels = more frequent

---

### Unit 32: Phase 2 Complete

**Learning Objectives:**
- Integration testing
- Balance difficulty curve
- Verify all mechanics
- Polish gameplay

**Concepts Introduced:**
- Full game testing
- Balance tuning
- Feature verification
- Phase gate

**Code Written:**
```
- Test all combinations
- Adjust speeds and timing
- Fix integration issues
- Document improvements needed
```

**What the Learner Sees:**
Complete Frogger game with roads AND river. Cars, logs, turtles, crocodiles. Sound effects. Multiple levels. A real game.

**Phase 2 Checkpoint:**
The game now has the complete Frogger experience: road and river sections, Blitter graphics for many objects, platform riding, hazards, sound effects, and level progression. It's a proper Amiga game.

---

## Phase 3: Polish (Units 33-48)

*Goal: Professional presentation - title screen, menus, visual effects, music.*

*By the end of this phase, the game has animated title, attract mode, high scores, options, Copper effects, and background music. Commercial quality presentation.*

---

### Unit 33: Title Screen Design

**Learning Objectives:**
- Design impactful title screen
- Create game logo graphics
- Plan menu structure
- Establish visual identity

**Concepts Introduced:**
- Title screen composition
- Logo design
- Colour palette for branding
- Menu layout

**Code Written:**
```
- Title screen background
- "SIGNAL" logo graphics
- Menu options: Start, Options, High Scores
- Colour scheme
```

**What the Learner Sees:**
Professional title screen with large logo, clear menu options. Looks like a commercial game.

---

### Unit 34: Title Animation

**Learning Objectives:**
- Animate title elements
- Copper colour cycling
- Create visual interest
- Loop animations

**Concepts Introduced:**
- Copper for animation
- Palette cycling
- Sine-wave movement
- Attention management

**Code Written:**
```
- Logo colour cycling via Copper
- Pulsing menu cursor
- Background animation
- Smooth loops
```

**What the Learner Sees:**
Title screen moves and breathes. Logo shimmers, colours cycle. The game feels alive before playing.

---

### Unit 35: Menu Navigation

**Learning Objectives:**
- Implement menu system
- Handle up/down selection
- Visual feedback for cursor
- State transitions

**Concepts Introduced:**
- Menu state management
- Cursor navigation
- Selection confirmation
- Sub-menus

**Code Written:**
```
- Menu cursor position
- Up/down joystick navigation
- Fire to confirm selection
- Visual cursor indicator
```

**What the Learner Sees:**
Navigate menus with joystick. Selection clearly highlighted. Press fire to choose.

---

### Unit 36: Attract Mode

**Learning Objectives:**
- Implement auto-play demo
- Record or script gameplay
- Return on input
- Cycle from title

**Concepts Introduced:**
- Demo playback
- AI plays game
- Attract cycle
- Input interrupt

**Code Written:**
```
- AI plays simple pattern
- Timeout from title triggers
- Any input returns to title
- Shows off gameplay
```

**What the Learner Sees:**
Leave game idle and it plays itself. Demonstrates gameplay automatically.

---

### Unit 37: Options Screen

**Learning Objectives:**
- Create options menu
- Starting lives setting
- Starting level setting
- Sound toggle

**Concepts Introduced:**
- Settings storage
- Toggle UI pattern
- Value adjustment
- Apply settings

**Code Written:**
```
- Options screen layout
- Lives: 3, 5, 7
- Start level: 1-5
- Sound: On/Off
```

**What the Learner Sees:**
Options menu allows customisation. Settings apply to next game.

---

### Unit 38: High Score Table

**Learning Objectives:**
- Track top scores
- Name entry system
- Display leaderboard
- Rank scores

**Concepts Introduced:**
- Score data structure
- Name entry UI
- Sorting/insertion
- Display formatting

**Code Written:**
```
- Top 10 scores array
- Name entry (3 letters)
- Insert in sorted order
- Formatted display
```

**What the Learner Sees:**
High score table with names. New high scores prompt name entry.

---

### Unit 39: Background Music - Module Basics

**Learning Objectives:**
- Understand MOD format
- Load module data
- Basic replay routine
- Music during gameplay

**Concepts Introduced:**
- MOD file format
- Pattern/sequence structure
- Simple replay loop
- Channel mixing

**Code Written:**
```
- Basic MOD replay routine
- Load module data
- Play during game
- Pause on pause
```

**What the Learner Sees:**
Background music plays during gameplay. Adds atmosphere and polish.

**Technical Details:**
- MOD format: 4 channels
- Pattern-based sequencing
- Sample playback via Paula
- CPU time consideration

---

### Unit 40: Music Integration

**Learning Objectives:**
- Different music per state
- Title music, game music
- Music stops on game over
- Volume control

**Concepts Introduced:**
- State-based music
- Music transitions
- Volume adjustment
- Performance budget

**Code Written:**
```
- Title music loop
- Game music loop
- Fade on state change
- Stop on game over
```

**What the Learner Sees:**
Different music for title and gameplay. Clean transitions between states.

---

### Unit 41: Copper Sky Gradient

**Learning Objectives:**
- Create gradient background
- Copper colour changes per line
- Time of day effect
- Visual depth

**Concepts Introduced:**
- Per-line colour changes
- Gradient generation
- Colour interpolation
- Copper list size

**Code Written:**
```
- Generate gradient colours
- Copper list with WAIT/MOVE per line
- Sky gradient above playfield
- Optional time progression
```

**What the Learner Sees:**
Beautiful gradient sky above the playfield. Distinctly Amiga visual effect.

---

### Unit 42: Water Animation

**Learning Objectives:**
- Animate water surface
- Colour cycling effect
- Sync with frame rate
- Subtle motion

**Concepts Introduced:**
- Palette animation
- Colour rotation
- Cycle timing
- Ambient motion

**Code Written:**
```
- Water colours in palette
- Rotate colours each frame
- Creates wave effect
- Subtle but effective
```

**What the Learner Sees:**
River water appears to shimmer and flow. Adds life to the playfield.

---

### Unit 43: Death Animation

**Learning Objectives:**
- Elaborate death effect
- Car hit vs water death
- Animation sequence
- Brief but satisfying

**Concepts Introduced:**
- Animation sequences
- Effect variation
- Particle-like effects
- Timing

**Code Written:**
```
- Squash animation for car
- Splash animation for water
- Frame sequences
- Trigger appropriate version
```

**What the Learner Sees:**
Death has visual feedback beyond just respawn. Car hits squash, water falls splash.

---

### Unit 44: Level Complete Effect

**Learning Objectives:**
- Celebrate level completion
- Bonus calculation display
- Transition to next level
- Positive feedback

**Concepts Introduced:**
- Victory effects
- Score count-up
- Screen transitions
- Celebration

**Code Written:**
```
- Fill all homes triggers
- Flash effect
- Bonus points count up
- Fade to next level
```

**What the Learner Sees:**
Completing a level is celebrated. Bonus points tick up. Transition effect to next level.

---

### Unit 45: Pause System

**Learning Objectives:**
- Pause mid-game
- Pause menu options
- Resume cleanly
- Music pause

**Concepts Introduced:**
- Pause state
- State preservation
- Overlay display
- Music pause/resume

**Code Written:**
```
- Pause on specific button
- Display PAUSED overlay
- Menu: Resume, Restart, Quit
- Resume with countdown
```

**What the Learner Sees:**
Press pause to freeze game. Menu appears. Resume continues exactly where left off.

---

### Unit 46: Screen Transitions

**Learning Objectives:**
- Smooth state transitions
- Fade or wipe effects
- Copper-based fades
- Professional feel

**Concepts Introduced:**
- Transition effects
- Colour fading via Copper
- Effect timing
- Polish through transitions

**Code Written:**
```
- Fade to black
- Fade from black
- Wipe alternative
- Apply between states
```

**What the Learner Sees:**
Screens don't cut abruptly. Smooth fades between title, game, and results.

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
```
- Fix alignment issues
- Colour adjustments
- Timing refinements
- Verify all features
```

**What the Learner Sees:**
Subtle improvements throughout. Everything more consistent and refined.

---

### Unit 48: Phase 3 Complete

**Learning Objectives:**
- Full integration test
- Feature verification
- Quality sign-off
- Phase completion

**Concepts Introduced:**
- Release candidacy
- Feature completeness
- Quality bar
- Phase gate

**Code Written:**
```
- Complete playthrough
- All features verified
- Bug fixes
- Documentation
```

**What the Learner Sees:**
Complete, polished game with professional presentation. Commercial quality.

**Phase 3 Checkpoint:**
The game has professional presentation: animated title, attract mode, high scores, options, Copper effects, background music, and polished transitions. It looks and sounds like a commercial Amiga game.

---

## Phase 4: Mastery (Units 49-64)

*Goal: Advanced techniques, optimisation, and distribution.*

*By the end of this phase, the game uses advanced Amiga techniques, is optimised for performance, and is packaged for distribution as a bootable disk.*

---

### Unit 49: Code Review

**Learning Objectives:**
- Review codebase architecture
- Identify improvements
- Document code structure
- Plan optimisation

**Concepts Introduced:**
- Code review practices
- Technical debt
- Documentation
- Refactoring planning

**Code Written:**
```
- Add comprehensive comments
- Document memory map
- Identify hot paths
- Plan optimisation targets
```

**What the Learner Sees:**
Cleaner, documented code. Preparation for optimisation.

---

### Unit 50: Memory Optimisation

**Learning Objectives:**
- Reduce memory footprint
- Compress graphics data
- Optimise data structures
- Free chip RAM

**Concepts Introduced:**
- Memory profiling
- RLE compression
- Data packing
- Chip RAM budgeting

**Code Written:**
```
- Compress BOB graphics
- Pack level data
- Remove redundancy
- Document savings
```

**What the Learner Sees:**
Same game, smaller memory use. More room for content.

---

### Unit 51: Blitter Optimisation

**Learning Objectives:**
- Optimise Blitter usage
- Reduce blit count
- Interleaved bitplanes
- Maximum performance

**Concepts Introduced:**
- Blitter scheduling
- Interleaved format
- Blit combining
- DMA efficiency

**Code Written:**
```
- Interleaved graphics
- Combined erase/draw
- Optimal modulos
- Verify performance
```

**What the Learner Sees:**
Smoother graphics, more objects possible, better performance.

---

### Unit 52: CPU/Blitter Parallelism

**Learning Objectives:**
- CPU work during Blitter operations
- Avoid Blitter wait loops
- Parallel processing
- Maximum throughput

**Concepts Introduced:**
- CPU/Blitter parallelism
- Deferred waits
- Work scheduling
- Resource utilisation

**Code Written:**
```
- Start blit, do CPU work, then wait
- Batch Blitter operations
- Optimise wait points
- Verify overlap
```

**What the Learner Sees:**
More responsive game. Better performance without visual change.

---

### Unit 53: Advanced Copper

**Learning Objectives:**
- Dynamic Copper list building
- Copper sprites
- Per-line effects
- Advanced timing

**Concepts Introduced:**
- Dynamic Copper lists
- Copper-based effects
- Scanline tricks
- Double-buffered Copper

**Code Written:**
```
- Build Copper list per frame
- Dynamic gradient changes
- Level-specific effects
- Double-buffer lists
```

**What the Learner Sees:**
More dynamic visual effects. Responsive to game state.

---

### Unit 54: More Enemies

**Learning Objectives:**
- Add snakes on road
- Cars that speed up
- Additional hazards
- Variety

**Concepts Introduced:**
- Enemy variety
- Behaviour variation
- Difficulty layering
- Content expansion

**Code Written:**
```
- Snake hazard on road edge
- Fast car variants
- Mix hazard types
- Level-based appearance
```

**What the Learner Sees:**
More variety in hazards. Game stays fresh longer.

---

### Unit 55: Female Frog Bonus

**Learning Objectives:**
- Add bonus objective
- Escort female frog home
- Extra points
- Risk/reward

**Concepts Introduced:**
- Bonus mechanics
- Escort gameplay
- Optional objectives
- Score multipliers

**Code Written:**
```
- Female frog appears on log
- Hop onto her to pick up
- Carry to home for bonus
- Timer while carrying
```

**What the Learner Sees:**
Pink frog appears occasionally on logs. Rescue her for bonus points.

---

### Unit 56: Two Player Mode

**Learning Objectives:**
- Alternating two player
- Separate scores
- Player indicator
- Competitive play

**Concepts Introduced:**
- Multiplayer design
- State per player
- Turn alternation
- Score comparison

**Code Written:**
```
- Two player option
- Alternate on death/home
- Separate score tracking
- Winner determination
```

**What the Learner Sees:**
Two player mode. Take turns, compete for high score.

---

### Unit 57: Simultaneous Two Player

**Learning Objectives:**
- Both players on screen
- Separate controls
- Collision between players
- Cooperative/competitive

**Concepts Introduced:**
- Simultaneous multiplayer
- Control separation
- Player collision
- Split attention

**Code Written:**
```
- Two frogs on screen
- Joy 1 and Joy 2
- Can collide (push?)
- Compete for homes
```

**What the Learner Sees:**
Both players play at once. Race to fill homes.

---

### Unit 58: Statistics Tracking

**Learning Objectives:**
- Track gameplay statistics
- Display stats screen
- Session records
- Achievement-like goals

**Concepts Introduced:**
- Statistics collection
- Persistent data
- Display formatting
- Goals

**Code Written:**
```
- Track: homes, deaths, levels, time
- Best stats this session
- Stats screen from menu
- Goals (reach level 5, etc.)
```

**What the Learner Sees:**
Statistics screen shows achievements. Long-term goals to pursue.

---

### Unit 59: Difficulty Options

**Learning Objectives:**
- Configurable difficulty
- Easy/Normal/Hard modes
- Affect speed and hazards
- Accessibility

**Concepts Introduced:**
- Difficulty parameters
- Player choice
- Balance tuning
- Accessibility

**Code Written:**
```
- Difficulty setting in options
- Easy: slower, fewer hazards
- Hard: faster, more hazards
- Apply to game parameters
```

**What the Learner Sees:**
Difficulty option makes game accessible to all skill levels.

---

### Unit 60: Final Content

**Learning Objectives:**
- Add remaining content
- Ensure 8 complete levels
- Verify progression
- Content complete

**Concepts Introduced:**
- Content completion
- Level design
- Difficulty curve
- Feature lock

**Code Written:**
```
- Complete all 8 levels
- Verify difficulty curve
- Final enemy patterns
- Content freeze
```

**What the Learner Sees:**
Complete game with all levels, features, and content.

---

### Unit 61: Loading Screen

**Learning Objectives:**
- Create loading display
- First impression
- Loading animation
- Set expectations

**Concepts Introduced:**
- Load-time experience
- First impressions
- Branding
- Professional start

**Code Written:**
```
- Loading screen graphics
- Simple animation during load
- Copyright/credits
- Transition to title
```

**What the Learner Sees:**
Professional loading screen while game loads. Good first impression.

---

### Unit 62: Disk Mastering

**Learning Objectives:**
- Create bootable ADF
- Organise files on disk
- Boot sector setup
- Distribution format

**Concepts Introduced:**
- ADF format
- Boot block
- File organisation
- Bootable disk

**Code Written:**
```
- Create boot sector
- Organise files efficiently
- Test boot process
- Create ADF image
```

**What the Learner Sees:**
Game boots directly from disk. No Workbench needed.

---

### Unit 63: Final Testing

**Learning Objectives:**
- Complete test pass
- Edge cases
- Compatibility testing
- Release candidate

**Concepts Introduced:**
- Release testing
- Compatibility
- Bug triage
- Release readiness

**Code Written:**
```
- Full playthrough all modes
- Test on different Amiga models
- Fix critical issues
- Declare RC
```

**What the Learner Sees:**
Thoroughly tested game. Works on A500, A1200, etc.

---

### Unit 64: Distribution

**Learning Objectives:**
- Create final distribution
- Documentation
- Package complete
- Release

**Concepts Introduced:**
- Distribution packaging
- Documentation
- Archive practices
- Release process

**Code Written:**
```
- Final ADF image
- Readme file
- Quick reference card
- Source archive
```

**What the Learner Sees:**
Complete distribution package. Professional release.

**Phase 4 Checkpoint:**
The game is complete. Optimised, full-featured, professionally packaged. It could have sold for £19.99 in 1987. The learner has built a commercial-quality Amiga game.

---

## Skills Mastery Summary

By completing all 64 units, learners have demonstrated mastery of:

### 68000 Assembly
- Registers (D0-D7, A0-A7) and addressing modes
- Data movement, arithmetic, and logic
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
- Code organisation and documentation
- Performance optimisation
- Distribution packaging
- Quality assurance

---

## Comparison: 16 Units vs 64 Units

| Aspect | 16-Unit Version | 64-Unit Version |
|--------|-----------------|-----------------|
| Graphics | Hardware sprites only | Blitter BOBs + sprites |
| Gameplay | Roads only | Roads + river + hazards |
| Audio | None | Full SFX + music |
| Visuals | Static | Copper effects, animations |
| Levels | 1 | 8 with progression |
| Modes | Single player only | 1P, 2P alternate, 2P simultaneous |
| Polish | Minimal | Full menus, options, high scores |
| Distribution | Executable | Bootable ADF |
| Commercial viable? | No | Yes |
| Time investment | 16-32 hours | 64-128 hours |

---

## Version History

- **2.0 (2026-01-10):** Complete restructure. Playable game by Unit 16. Full unit-by-unit detail matching SID Symphony/Ink War format.
- **1.0 (2026-01-07):** Initial outline (hardware-theory focused, no game until Phase 2).
