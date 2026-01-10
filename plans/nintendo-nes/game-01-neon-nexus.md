# Neon Nexus: 64-Unit Outline

**Game:** NES Game 1: Neon Nexus
**Units:** 64
**Concept:** Fixed-screen action game. Navigate a digital grid, collect data cores, avoid security programs. A futuristic collect-and-avoid game that teaches NES PPU fundamentals.

**Commercial Quality Target:** A game that could have sold for $29.99 on cartridge in 1987. Polished, responsive, with that distinctive NES look and sound.

---

## The Finished Game

Before detailing the units, here's what the learner builds:

### Core Gameplay
- Fixed single-screen arena
- Player navigates a grid-based level
- Collect all data cores to complete the level
- Avoid security programs (enemies) that patrol the grid
- Touch an enemy = lose a life
- Collect all cores = advance to next level

### Content
- 16 levels with increasing difficulty
- Different enemy patterns per level
- Speed increases as levels progress
- Power-ups: temporary invincibility, speed boost
- High score tracking

### Audio
- APU sound effects (collect, hit, game over)
- Background music during gameplay
- Jingles for level complete, game over
- Different music per level zone

### Visuals
- Custom tile graphics
- Animated player sprite (4 directions)
- Multiple enemy types
- Palette cycling effects
- Level variety through tile/colour changes

### Polish
- Animated title screen
- High score display
- Level select (unlocked)
- Pause functionality
- Smooth animations

---

## Phase 1: Foundation (Units 1-16)

*Goal: A complete, playable collect-and-avoid game. Navigate the arena, collect items, avoid enemies, win or lose.*

*By the end of this phase, the learner has built a working game. The player moves around the screen, collects data cores, avoids enemies, loses lives, and completes levels. Simple but complete.*

---

### Unit 1: NES Architecture

**Learning Objectives:**
- Understand NES hardware (CPU, PPU, APU)
- Know the memory map (RAM, ROM, PPU)
- Write a first 6502 assembly program
- See the program run on the NES

**Concepts Introduced:**
- 6502 CPU at 1.79 MHz
- Picture Processing Unit (PPU)
- Audio Processing Unit (APU)
- Memory-mapped I/O

**Code Written:**
```
- iNES header (16 bytes)
- Reset vector setup
- Infinite loop
- Basic structure
```

**What the Learner Sees:**
A blank screen, but the NES runs their code. The emulator doesn't crash. First contact with NES development.

**Technical Details:**
- CPU RAM: $0000-$07FF (2KB, mirrored)
- PPU registers: $2000-$2007
- APU/IO: $4000-$4017
- PRG ROM: $8000-$FFFF
- Vectors: $FFFA-$FFFF

---

### Unit 2: PPU Fundamentals

**Learning Objectives:**
- Understand tile-based graphics
- Know PPU memory layout
- Learn about pattern tables and nametables
- Prepare for display setup

**Concepts Introduced:**
- Pattern tables (CHR ROM)
- Nametables (screen layout)
- Attribute tables (palette assignment)
- PPU address space ($0000-$3FFF)

**Code Written:**
```
- Theory unit, minimal code
- PPU register definitions
- Wait for VBlank routine
- Basic structure
```

**What the Learner Sees:**
Understanding of how the PPU works. Preparation for creating graphics.

**Technical Details:**
- Pattern table 0: $0000-$0FFF (background)
- Pattern table 1: $1000-$1FFF (sprites)
- Nametable 0: $2000-$23FF
- Palettes: $3F00-$3F1F

---

### Unit 3: VBlank and NMI

**Learning Objectives:**
- Understand vertical blanking
- Set up NMI handler
- Know when it's safe to update PPU
- Create stable timing

**Concepts Introduced:**
- VBlank period
- NMI (Non-Maskable Interrupt)
- PPU timing constraints
- Frame synchronisation

**Code Written:**
```
- NMI handler routine
- VBlank wait flag
- Enable NMI in PPUCTRL
- Frame-synced main loop
```

**What the Learner Sees:**
Code runs at stable 60 FPS (NTSC) or 50 FPS (PAL). Foundation for all PPU updates.

**Technical Details:**
- PPUCTRL ($2000) bit 7: NMI enable
- PPUSTATUS ($2002) bit 7: VBlank flag
- VBlank: ~2273 cycles to update PPU
- NMI vector: $FFFA

---

### Unit 4: Palettes and Colours

**Learning Objectives:**
- Understand NES colour system
- Set up background and sprite palettes
- Write to PPU during VBlank
- See colours on screen

**Concepts Introduced:**
- 64-colour master palette
- 4 background palettes (4 colours each)
- 4 sprite palettes (3 colours + transparent)
- Shared background colour

**Code Written:**
```
- Define palette data
- Write palettes during VBlank
- Set PPUADDR to $3F00
- Write 32 bytes via PPUDATA
```

**What the Learner Sees:**
The screen shows a solid colour from the palette. Colours work!

**Technical Details:**
- Palette address: $3F00-$3F1F
- Background: $3F00, $3F01-$3F03, $3F05-$3F07, etc.
- Sprites: $3F10-$3F1F (but $3F10 mirrors $3F00)
- Colour 0 of each palette is transparent (uses $3F00)

---

### Unit 5: Pattern Tables

**Learning Objectives:**
- Design 8x8 pixel tiles
- Understand tile data format
- Create CHR ROM with tiles
- Prepare graphics for game

**Concepts Introduced:**
- 8x8 pixel tiles
- 2 bits per pixel (4 colours)
- Low byte + high byte planes
- CHR ROM organisation

**Code Written:**
```
- Design player tile (8x8)
- Design wall tile
- Design floor tile
- Design data core tile
- Assemble as CHR data
```

**What the Learner Sees:**
Tile graphics defined in code. Ready to display on screen.

**Technical Details:**
- 16 bytes per tile (8 low + 8 high)
- 256 tiles per pattern table
- Tiles numbered 0-255
- Background and sprite tables separate

---

### Unit 6: The Nametable

**Learning Objectives:**
- Understand screen layout via nametable
- Fill nametable with tile references
- Create a visible background
- Design the game arena

**Concepts Introduced:**
- Nametable as 32x30 tile grid
- Attribute table for palette selection
- Screen composition
- Border and playfield design

**Code Written:**
```
- Define arena layout data
- Fill nametable during init
- Set attribute table
- Enable rendering
```

**What the Learner Sees:**
A game arena appears! Border tiles around the edge, floor tiles inside. The playfield is visible.

**Technical Details:**
- Nametable: 960 bytes (32x30)
- Attribute table: 64 bytes (2x2 tile palette groups)
- PPUADDR: $2006 (write twice for address)
- PPUDATA: $2007 (write tile number)

---

### Unit 7: Sprites and OAM

**Learning Objectives:**
- Understand sprite rendering
- Learn OAM structure
- Display a single sprite
- Position sprite on screen

**Concepts Introduced:**
- Object Attribute Memory (256 bytes)
- Sprite structure: Y, tile, attributes, X
- 64 sprites maximum
- 8 sprites per scanline limit

**Code Written:**
```
- OAM shadow buffer in RAM ($0200)
- Set sprite data (Y, tile, attr, X)
- OAM DMA transfer ($4014)
- Sprite appears on screen
```

**What the Learner Sees:**
A sprite appears on the screen - the player character! It can be repositioned by changing OAM values.

**Technical Details:**
- OAM: $2003 (address), $2004 (data)
- OAM DMA: write page to $4014
- Sprite Y: actual Y - 1 (hardware quirk)
- Attributes: palette, flip, priority

---

### Unit 8: The Player Sprite

**Learning Objectives:**
- Design player character graphics
- Set up player variables
- Display player at starting position
- Prepare for movement

**Concepts Introduced:**
- Multi-tile sprites (if needed)
- Player position variables
- Screen coordinate system
- Sprite positioning

**Code Written:**
```
- Player tile graphics (4 frames for directions)
- player_x, player_y in zero page
- Update OAM from variables
- Player visible at centre of arena
```

**What the Learner Sees:**
A recognisable player character in the centre of the arena. Ready to move.

**Technical Details:**
- Zero page for speed: $00-$FF
- Player position: 8-bit values
- Sprite Y offset: subtract 1
- Starting position: centre of arena

---

### Unit 9: Controller Input

**Learning Objectives:**
- Read NES controller
- Detect D-pad presses
- Debounce input
- Respond to buttons

**Concepts Introduced:**
- Controller registers ($4016, $4017)
- Strobe and shift reading
- Button order (A, B, Select, Start, Up, Down, Left, Right)
- Edge detection

**Code Written:**
```
- Read controller routine
- Strobe controller ($4016)
- Shift 8 button bits
- Store button state
- Detect new presses
```

**What the Learner Sees:**
Pressing controller buttons causes visual feedback (border colour change). Input is detected and debounced.

**Technical Details:**
- $4016 write: strobe (bit 0)
- $4016 read: button state (bit 0)
- Read 8 times for all buttons
- Compare with previous frame for edges

---

### Unit 10: Player Movement

**Learning Objectives:**
- Move player in response to input
- Animate movement
- Constrain to playfield
- Smooth motion

**Concepts Introduced:**
- Position updates from input
- Boundary checking
- Movement speed
- Frame-based motion

**Code Written:**
```
- Check D-pad input
- Update player_x, player_y
- Check boundaries (wall tiles)
- Update OAM each frame
```

**What the Learner Sees:**
The player moves smoothly around the arena with the D-pad. Can't walk through walls. Feels responsive.

**Technical Details:**
- Movement speed: 1-2 pixels per frame
- Boundary check: arena edges
- 8 directions possible (diagonals)
- Tile-based collision later

---

### Unit 11: Collectible Items

**Learning Objectives:**
- Place data cores on screen
- Track item state (collected/uncollected)
- Display items as sprites or tiles
- Count remaining items

**Concepts Introduced:**
- Item placement data
- Collection state array
- Item sprites
- Item counter

**Code Written:**
```
- Item positions array
- Item collected flags
- Draw uncollected items as sprites
- items_remaining counter
```

**What the Learner Sees:**
Data cores appear around the arena. They're visible and waiting to be collected.

**Technical Details:**
- 10-15 items per level
- Items as sprites (or background tiles)
- Boolean array for collected state
- Counter decrements on collection

---

### Unit 12: Item Collection

**Learning Objectives:**
- Detect player-item collision
- Handle collection event
- Update item display
- Track progress

**Concepts Introduced:**
- Bounding box collision
- Collection response
- Sprite removal
- Score/progress update

**Code Written:**
```
- Check player vs each item
- If overlap and not collected: collect
- Mark as collected, hide sprite
- Decrement items_remaining
- Play collection sound (stub)
```

**What the Learner Sees:**
Walking over a data core collects it - it disappears and the counter goes down. Satisfying!

**Technical Details:**
- Collision: position within 8 pixels
- Collection: set flag, move sprite off-screen
- Counter: displayed on screen or tracked
- All collected = level complete (later)

---

### Unit 13: Enemy Sprites

**Learning Objectives:**
- Add enemy characters
- Display multiple enemies
- Store enemy state
- Prepare for movement

**Concepts Introduced:**
- Enemy data structure (x, y, direction)
- Multiple sprite management
- Enemy graphics
- Array of enemies

**Code Written:**
```
- Enemy tile graphics
- enemies array (4-6 enemies)
- Each: x, y, direction, active
- Draw all enemies as sprites
```

**What the Learner Sees:**
Security program enemies appear in the arena. They're visible but don't move yet.

**Technical Details:**
- 4-6 enemies per level initially
- Each uses 1-2 sprites
- Sprite limit: 64 total, 8 per line
- Priority: enemies behind player

---

### Unit 14: Enemy Movement

**Learning Objectives:**
- Move enemies automatically
- Implement simple AI patterns
- Handle wall collision
- Create challenge

**Concepts Introduced:**
- Patrol patterns
- Direction reversal
- Wall detection
- Different speeds

**Code Written:**
```
- Update enemy positions each frame
- Simple patrol: move until wall, reverse
- Different speeds per enemy
- Wrap or bounce at boundaries
```

**What the Learner Sees:**
Enemies patrol the arena, moving back and forth or in patterns. The arena feels dangerous.

**Technical Details:**
- Pattern 0: horizontal patrol
- Pattern 1: vertical patrol
- Pattern 2: chase player (later)
- Speed: 1 pixel per 2-4 frames

---

### Unit 15: Collision and Lives

**Learning Objectives:**
- Detect player-enemy collision
- Handle damage/death
- Implement lives system
- Respawn player

**Concepts Introduced:**
- Player-enemy collision
- Damage response
- Lives counter
- Respawn position

**Code Written:**
```
- Check player vs each enemy
- If overlap: lose life, respawn
- lives counter (start with 3)
- Brief invincibility after respawn
```

**What the Learner Sees:**
Touching an enemy causes death - brief flash, respawn at start. Lives decrease. Real stakes.

**Technical Details:**
- Collision radius: 6 pixels
- Invincibility: 60 frames (1 second)
- Visual: flash during invincibility
- Respawn: centre of arena

---

### Unit 16: Complete Game Loop

**Learning Objectives:**
- Implement game states (title, playing, game over)
- Level completion detection
- Game over handling
- Restart capability

**Concepts Introduced:**
- State machine
- Level complete trigger
- Game over state
- State transitions

**Code Written:**
```
- game_state: TITLE, PLAYING, GAME_OVER
- If items_remaining == 0: level complete
- If lives == 0: game over
- Press Start to restart
```

**What the Learner Sees:**
A complete game! Collect all items to win. Lose all lives to lose. Press Start to play again. Simple but functional.

**Phase 1 Checkpoint:**
The learner has built a working game. Player movement, item collection, enemy avoidance, lives, and win/lose conditions. It's simple (one level, basic graphics) but complete. Everything from here builds on this foundation.

---

## Phase 2: Expansion (Units 17-32)

*Goal: Multiple levels, better graphics, sound effects, and improved gameplay.*

*By the end of this phase, the game has multiple levels, animated sprites, APU sound effects, power-ups, and feels like a proper NES game.*

---

### Unit 17: Level Data Structure

**Learning Objectives:**
- Design level data format
- Store multiple levels
- Load level on start
- Reset level on death

**Concepts Introduced:**
- Level data compression
- Item placement per level
- Enemy placement per level
- Level progression

**Code Written:**
```
- Level data format (item/enemy positions)
- Level table (pointers to levels)
- load_level routine
- current_level variable
```

**What the Learner Sees:**
Same gameplay, but level data is now structured for expansion.

**Technical Details:**
- Level data: item count, positions, enemy count, positions
- RLE for arena layout (optional)
- Level index: 0-15
- Pointer table for quick access

---

### Unit 18: Multiple Levels

**Learning Objectives:**
- Implement level progression
- Increase difficulty
- Different layouts
- Track progress

**Concepts Introduced:**
- Level advancement
- Difficulty scaling
- Layout variation
- Progress tracking

**Code Written:**
```
- On level complete: advance to next
- Load new level data
- Increase enemy speed per level
- More enemies in later levels
```

**What the Learner Sees:**
Completing a level advances to the next with different layout and harder enemies. Progression!

**Technical Details:**
- 4 levels initially
- Speed increase: +1 every 2 levels
- Enemy count: +1 every 2 levels
- Wrap to level 1 or endless

---

### Unit 19: Player Animation

**Learning Objectives:**
- Animate player movement
- Direction-based frames
- Frame timing
- Smooth motion feel

**Concepts Introduced:**
- Animation frames
- Frame counter
- Direction states
- Idle vs moving

**Code Written:**
```
- 4 direction frames (or 2 + flip)
- 2 frames per direction (walk cycle)
- Frame timer
- Update tile in OAM
```

**What the Learner Sees:**
Player animates while moving - legs cycle, direction changes. Much more alive.

**Technical Details:**
- 2-4 frames per direction
- Frame rate: every 8-12 frames
- Horizontal flip for left/right
- Idle frame when stationary

---

### Unit 20: Enemy Animation

**Learning Objectives:**
- Animate enemy sprites
- Different animations per type
- Sync with movement
- Visual variety

**Concepts Introduced:**
- Enemy animation frames
- Type-based graphics
- Animation timing
- Visual distinction

**Code Written:**
```
- Enemy animation frames (2 per type)
- Animation timer per enemy
- Update enemy tiles
- Different speeds per type
```

**What the Learner Sees:**
Enemies animate as they move. Different enemy types look distinct. Arena feels dynamic.

**Technical Details:**
- 2 frames per enemy type
- Frame cycle: every 15 frames
- 2-3 enemy types
- Colour variation via palettes

---

### Unit 21: APU Basics

**Learning Objectives:**
- Understand APU channels
- Set up pulse channel
- Play a simple tone
- Control volume and pitch

**Concepts Introduced:**
- 5 APU channels (2 pulse, triangle, noise, DMC)
- Pulse registers ($4000-$4003)
- Frequency and duty cycle
- Volume envelope

**Code Written:**
```
- APU register definitions
- Play_tone routine
- Set pulse frequency
- Set volume
- Enable channel
```

**What the Learner Sees:**
A tone plays from the NES! First audio output.

**Technical Details:**
- Pulse 1: $4000-$4003
- Pulse 2: $4004-$4007
- Triangle: $4008-$400B
- Noise: $400C-$400F
- DMC: $4010-$4013
- Status: $4015

---

### Unit 22: Sound Effects

**Learning Objectives:**
- Create game sound effects
- Trigger on events
- Different sounds per event
- Sound priority

**Concepts Introduced:**
- Sound effect data
- Event-based triggering
- Channel allocation
- Priority system

**Code Written:**
```
- Collect sound (ascending tone)
- Death sound (descending noise)
- Level complete jingle
- Play_sfx routine
```

**What the Learner Sees:**
Collecting items makes a happy sound. Death makes a sad sound. The game has audio feedback.

**Technical Details:**
- Collect: pulse sweep up
- Death: noise burst
- Complete: short melody
- Use pulse 2 for SFX (reserve pulse 1 for music)

---

### Unit 23: Power-Ups

**Learning Objectives:**
- Add power-up items
- Temporary effects
- Visual feedback
- Strategic depth

**Concepts Introduced:**
- Power-up types
- Timed effects
- Effect stacking
- Power-up spawning

**Code Written:**
```
- Speed boost power-up
- Invincibility power-up
- power_up_timer
- Visual indication (palette change)
```

**What the Learner Sees:**
Occasional power-ups appear. Speed boost makes player faster. Invincibility lets player pass through enemies briefly.

**Technical Details:**
- Speed boost: 2x movement
- Invincibility: 180 frames (3 seconds)
- Spawn: random, low chance
- Visual: sprite palette change

---

### Unit 24: Smarter Enemies

**Learning Objectives:**
- Implement chase behaviour
- Mix enemy types
- Increase challenge
- Strategic enemy placement

**Concepts Introduced:**
- Chase AI
- Mixed behaviours
- Threat escalation
- Level-specific enemies

**Code Written:**
```
- Chase behaviour: move toward player
- Mix patrol and chase enemies
- Chase speed slower than patrol
- Level defines enemy types
```

**What the Learner Sees:**
Some enemies chase the player. Mix of patrol and chase creates interesting dynamics. More challenging!

**Technical Details:**
- Chase: compare positions, move toward
- Update chase direction every 30 frames
- Chase speed: 50% of patrol
- Max 2 chasers per level

---

### Unit 25: Score System

**Learning Objectives:**
- Implement scoring
- Points per collection
- Bonus points
- Display score

**Concepts Introduced:**
- Score variable (16-bit or BCD)
- Point values
- Score display
- High score

**Code Written:**
```
- score variable (16-bit)
- Add points on collect
- Display score on screen
- Track high score
```

**What the Learner Sees:**
Score displayed at top of screen. Increases when collecting items. High score tracked.

**Technical Details:**
- BCD for easy display
- Collect: 100 points
- Power-up: 500 points
- Level complete bonus: 1000
- Display: 6 digits

---

### Unit 26: HUD Display

**Learning Objectives:**
- Create heads-up display
- Show lives, score, level
- Update efficiently
- Reserve screen space

**Concepts Introduced:**
- HUD area (top or bottom rows)
- Nametable updates
- Efficient updates
- Information display

**Code Written:**
```
- Reserve top 2 rows for HUD
- Display: SCORE, LIVES, LEVEL
- Update only changed values
- Number tile graphics
```

**What the Learner Sees:**
Clean HUD showing score, lives, and level number. Professional appearance.

**Technical Details:**
- HUD: rows 0-1 of nametable
- Score: 6 digit tiles
- Lives: number or icons
- Level: 2 digits
- Update during VBlank

---

### Unit 27: Title Screen

**Learning Objectives:**
- Create title screen
- Menu options
- State transition
- First impression

**Concepts Introduced:**
- Title state
- Start button detection
- Screen composition
- Branding

**Code Written:**
```
- Title nametable data
- "NEON NEXUS" logo tiles
- "PRESS START" message
- Transition to game on Start
```

**What the Learner Sees:**
Proper title screen with game logo. Press Start to play. Professional presentation.

**Technical Details:**
- Title tiles in CHR ROM
- Full nametable for title
- Palette animation (optional)
- State: TITLE → PLAYING

---

### Unit 28: Game Over Screen

**Learning Objectives:**
- Create game over display
- Show final score
- Restart option
- Closure

**Concepts Introduced:**
- Game over state
- Score display
- Restart flow
- Player feedback

**Code Written:**
```
- Game over nametable
- Display final score
- "PRESS START" to retry
- Return to title or restart
```

**What the Learner Sees:**
Game over shows final score. Can restart immediately. Clear game flow.

**Technical Details:**
- Load game over screen
- Copy score to display
- Wait for Start press
- Reset game state

---

### Unit 29: Level Complete

**Learning Objectives:**
- Celebrate level completion
- Show bonus
- Transition effect
- Positive feedback

**Concepts Introduced:**
- Completion celebration
- Bonus calculation
- Screen transition
- Reward feeling

**Code Written:**
```
- Level complete jingle
- Display "LEVEL COMPLETE"
- Calculate and show bonus
- Brief pause, load next level
```

**What the Learner Sees:**
Completing a level triggers celebration. Bonus points awarded. Transition to next level.

**Technical Details:**
- Bonus: time remaining × 10
- Display for 60-90 frames
- Fade or cut to next level
- Play completion jingle

---

### Unit 30: Background Music Basics

**Learning Objectives:**
- Implement music playback
- Simple melody loop
- Multi-channel music
- Music structure

**Concepts Introduced:**
- Music data format
- Note sequences
- Tempo control
- Channel mixing

**Code Written:**
```
- Simple music format (note, duration)
- Music tick routine
- Update channels each tick
- Loop point
```

**What the Learner Sees:**
Background music plays during gameplay. Adds atmosphere and energy.

**Technical Details:**
- Format: note (pitch), duration
- Tempo: ticks per frame
- Channels: pulse1 (melody), triangle (bass)
- Loop: return to start

---

### Unit 31: Music Integration

**Learning Objectives:**
- Different music per state
- Music transitions
- SFX over music
- Volume balance

**Concepts Introduced:**
- State-based music
- Music start/stop
- SFX priority
- Mix balance

**Code Written:**
```
- Title music
- Game music
- Stop on game over
- SFX interrupts briefly
```

**What the Learner Sees:**
Title has its own music. Game has energetic music. Music stops dramatically on game over.

**Technical Details:**
- music_playing flag
- start_music, stop_music
- SFX uses pulse 2
- Music uses pulse 1, triangle

---

### Unit 32: Phase 2 Complete

**Learning Objectives:**
- Integration testing
- Balance levels
- Verify all features
- Polish gameplay

**Concepts Introduced:**
- Full game testing
- Balance tuning
- Feature verification
- Phase gate

**Code Written:**
```
- Test all levels
- Adjust enemy patterns
- Verify sound and music
- Fix integration issues
```

**What the Learner Sees:**
Complete game with multiple levels, animation, sound, and music. Feels like a real NES game.

**Phase 2 Checkpoint:**
The game now has 4+ levels, animated sprites, APU sound effects and music, power-ups, and proper score/lives display. It looks and sounds like a commercial NES game.

---

## Phase 3: Polish (Units 33-48)

*Goal: Professional presentation - more levels, visual effects, menus, and polish.*

*By the end of this phase, the game has 16 levels, palette effects, options, and commercial quality presentation.*

---

### Unit 33: More Levels (5-8)

**Learning Objectives:**
- Create levels 5-8
- New enemy patterns
- Increased difficulty
- Level variety

**Concepts Introduced:**
- Level design
- Difficulty curve
- Pattern variety
- Playtesting

**Code Written:**
```
- Level 5-8 data
- New enemy formations
- Tighter item placement
- More challenging layouts
```

**What the Learner Sees:**
4 more levels with increased challenge. Different patterns keep it fresh.

---

### Unit 34: More Levels (9-12)

**Learning Objectives:**
- Create levels 9-12
- Near-end difficulty
- All enemy types
- Strategic layouts

**Concepts Introduced:**
- Late-game difficulty
- Pattern mastery
- Player skill testing
- Rewarding challenge

**Code Written:**
```
- Level 9-12 data
- Complex enemy patterns
- Multiple chasers
- Demanding but fair
```

**What the Learner Sees:**
Challenging levels that test all skills learned. Rewarding to complete.

---

### Unit 35: More Levels (13-16)

**Learning Objectives:**
- Create final levels
- Maximum difficulty
- Victory levels
- Endgame content

**Concepts Introduced:**
- Final challenge
- Victory reward
- Completion satisfaction
- Content completeness

**Code Written:**
```
- Level 13-16 data
- Hardest patterns
- Ending sequence (level 16)
- Victory message
```

**What the Learner Sees:**
Final levels are serious challenge. Completing level 16 shows victory. Full game content.

---

### Unit 36: Palette Animation

**Learning Objectives:**
- Animate colours
- Create visual effects
- Enhance atmosphere
- NES colour tricks

**Concepts Introduced:**
- Palette cycling
- Colour animation timing
- Atmospheric effects
- Visual polish

**Code Written:**
```
- Palette update routine
- Cycle background colours
- Flash effects on events
- Smooth transitions
```

**What the Learner Sees:**
Background colours shift subtly. Collection causes flash. More dynamic visuals.

**Technical Details:**
- Update palette during VBlank
- Cycle every 4-8 frames
- Flash: briefly brighten palette
- 4 palette entries to cycle

---

### Unit 37: Screen Transitions

**Learning Objectives:**
- Smooth state transitions
- Fade effects
- Professional feel
- No jarring cuts

**Concepts Introduced:**
- Fade to black
- Fade from black
- Palette-based fades
- Transition timing

**Code Written:**
```
- Fade out routine (darken palette)
- Fade in routine (restore palette)
- Apply between states
- Consistent timing
```

**What the Learner Sees:**
Screens fade smoothly between title, game, and game over. Professional presentation.

**Technical Details:**
- NES fade: reduce palette values
- 4-8 steps to full black
- 2-4 frames per step
- Store original palette

---

### Unit 38: Options Menu

**Learning Objectives:**
- Create options screen
- Difficulty setting
- Sound toggle
- Start level select

**Concepts Introduced:**
- Menu navigation
- Option storage
- Setting application
- User preference

**Code Written:**
```
- Options screen layout
- Difficulty: Easy/Normal/Hard
- Sound: On/Off
- Starting level: 1-4
```

**What the Learner Sees:**
Options menu accessible from title. Can adjust difficulty and starting level.

---

### Unit 39: Difficulty Implementation

**Learning Objectives:**
- Apply difficulty settings
- Easy: more forgiving
- Hard: more challenging
- Balance for all players

**Concepts Introduced:**
- Difficulty parameters
- Player choice
- Accessibility
- Challenge scaling

**Code Written:**
```
- Easy: slower enemies, more lives
- Normal: standard settings
- Hard: faster enemies, fewer lives
- Apply from options
```

**What the Learner Sees:**
Game difficulty matches selection. Accessible to beginners and challenging for experts.

**Technical Details:**
- Easy: 5 lives, 75% enemy speed
- Normal: 3 lives, 100% speed
- Hard: 2 lives, 125% speed

---

### Unit 40: High Score Table

**Learning Objectives:**
- Track top scores
- Display leaderboard
- Persist during session
- Motivate replay

**Concepts Introduced:**
- Score array
- Sorting/insertion
- Display formatting
- Achievement tracking

**Code Written:**
```
- Top 5 scores array
- Insert new score if qualifies
- Display high score table
- Show from title screen
```

**What the Learner Sees:**
High score table shows best attempts. Motivation to beat your best.

---

### Unit 41: Pause System

**Learning Objectives:**
- Pause mid-game
- Display pause message
- Resume cleanly
- Freeze all action

**Concepts Introduced:**
- Pause state
- State preservation
- Music pause
- Resume without issues

**Code Written:**
```
- Pause on Start button
- Display "PAUSED"
- Freeze all updates
- Resume on Start
```

**What the Learner Sees:**
Press Start to pause. Game freezes. Press Start again to continue exactly where you left off.

**Technical Details:**
- Check Start button edge
- Set paused flag
- Skip game logic when paused
- Keep NMI running (display stable)

---

### Unit 42: Death Animation

**Learning Objectives:**
- Animate player death
- Visual feedback
- Brief but impactful
- Respawn transition

**Concepts Introduced:**
- Death animation frames
- Explosion/fade effect
- Timing
- Emotional impact

**Code Written:**
```
- Death animation frames
- Flash and fade player
- Brief pause
- Respawn sequence
```

**What the Learner Sees:**
Death has visual impact - player flashes and fades. Brief pause before respawn. Feels consequential.

---

### Unit 43: Enemy Variety

**Learning Objectives:**
- Add more enemy types
- Unique behaviours
- Visual distinction
- Gameplay variety

**Concepts Introduced:**
- Enemy type system
- Behaviour variety
- Graphics per type
- Strategic variety

**Code Written:**
```
- Type 3: diagonal movement
- Type 4: teleporter
- New enemy graphics
- Mix in later levels
```

**What the Learner Sees:**
More enemy types with different behaviours. Keeps gameplay fresh.

**Technical Details:**
- Diagonal: move on both axes
- Teleporter: random position every 3 seconds
- Different graphics per type
- Introduced gradually in levels

---

### Unit 44: Bonus Stage

**Learning Objectives:**
- Add bonus round
- All items, no enemies
- Time limit
- Reward section

**Concepts Introduced:**
- Bonus stage design
- Time pressure
- Risk-free rewards
- Pace variation

**Code Written:**
```
- Bonus level data (no enemies)
- Time limit (30 seconds)
- Points per item collected
- Appears after level 4, 8, 12
```

**What the Learner Sees:**
Occasional bonus stage - collect items quickly for bonus points. Fun change of pace.

---

### Unit 45: Continue System

**Learning Objectives:**
- Implement continues
- Second chance
- Continue limit
- Player recovery

**Concepts Introduced:**
- Continue concept
- Limited continues
- Reset with progress
- Player retention

**Code Written:**
```
- 3 continues available
- On game over: "CONTINUE?"
- Yes: restart level with 3 lives
- No or timeout: title screen
```

**What the Learner Sees:**
Game over offers continue. Can keep trying without full restart. Less frustration.

**Technical Details:**
- continues variable
- 10 second countdown
- Decrement on use
- Display remaining continues

---

### Unit 46: Attract Mode

**Learning Objectives:**
- Auto-play demonstration
- Showcase gameplay
- Return on input
- Professional touch

**Concepts Introduced:**
- Demo playback
- AI plays game
- Input cancellation
- Attract cycle

**Code Written:**
```
- Record or script demo
- Auto-play level 1
- Any button returns to title
- Cycle from title after timeout
```

**What the Learner Sees:**
Leave game idle and it plays itself. Shows off gameplay. Any button to return.

---

### Unit 47: Polish Pass

**Learning Objectives:**
- Review entire game
- Fix inconsistencies
- Tighten timing
- Final tweaks

**Concepts Introduced:**
- Polish methodology
- Detail attention
- Player experience
- Quality threshold

**Code Written:**
```
- Colour adjustments
- Timing refinements
- Animation polish
- Sound balance
```

**What the Learner Sees:**
Subtle improvements throughout. Everything feels tighter and more polished.

---

### Unit 48: Phase 3 Complete

**Learning Objectives:**
- Full integration test
- All features verified
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
- Test all 16 levels
- Verify all features
- Document issues
```

**What the Learner Sees:**
Complete, polished game with 16 levels and all features. Commercial quality.

**Phase 3 Checkpoint:**
The game has 16 levels, multiple enemy types, options, continues, high scores, and polished presentation. It's ready for final enhancements.

---

## Phase 4: Mastery (Units 49-64)

*Goal: Advanced techniques, optimisation, and distribution.*

*By the end of this phase, the game uses advanced NES techniques, is optimised, and is ready for distribution.*

---

### Unit 49: Code Review

**Learning Objectives:**
- Review codebase
- Document architecture
- Identify improvements
- Plan optimisation

**Concepts Introduced:**
- Code organisation
- Documentation
- Technical debt
- Refactoring

**Code Written:**
```
- Add comments
- Document memory map
- Identify hot paths
- Plan improvements
```

**What the Learner Sees:**
Cleaner, documented code. Ready for optimisation.

---

### Unit 50: Memory Optimisation

**Learning Objectives:**
- Reduce RAM usage
- Optimise data structures
- Compress level data
- Efficient storage

**Concepts Introduced:**
- Memory profiling
- Data compression
- Efficient structures
- RAM budgeting

**Code Written:**
```
- RLE level compression
- Packed data structures
- Remove redundancy
- Document savings
```

**What the Learner Sees:**
Same game, less memory used. Room for more content.

**Technical Details:**
- NES RAM: only 2KB!
- Zero page: precious resource
- Compress what you can
- Reuse buffers

---

### Unit 51: CPU Optimisation

**Learning Objectives:**
- Profile code performance
- Optimise hot paths
- Reduce cycles
- Smooth performance

**Concepts Introduced:**
- Cycle counting
- Hot path identification
- Lookup tables
- Loop optimisation

**Code Written:**
```
- Replace calculations with tables
- Unroll critical loops
- Optimise collision checks
- Verify performance
```

**What the Learner Sees:**
Smoother gameplay. More room for features.

---

### Unit 52: Sprite Multiplexing

**Learning Objectives:**
- Overcome 8 sprite limit
- Flicker when needed
- Distribute across frames
- More sprites visible

**Concepts Introduced:**
- 8 sprite per line limit
- Flickering approach
- Priority rotation
- Visual trade-offs

**Code Written:**
```
- Detect sprite overlap
- Rotate priority each frame
- Flicker instead of disappear
- Handle gracefully
```

**What the Learner Sees:**
More sprites visible (with acceptable flicker). NES limitation managed.

**Technical Details:**
- Sort sprites by Y
- Rotate priority each frame
- Flicker is normal for NES
- Better than missing sprites

---

### Unit 53: Advanced Music

**Learning Objectives:**
- Richer music
- Multiple channels
- Better sound design
- Professional audio

**Concepts Introduced:**
- Full channel usage
- Harmony and melody
- Sound design
- Music variety

**Code Written:**
```
- 4-channel music
- Multiple songs
- Better SFX
- Audio polish
```

**What the Learner Sees:**
Richer, more varied music. Professional audio quality.

---

### Unit 54: Level Themes

**Learning Objectives:**
- Visual variety per zone
- Different palettes
- Theme graphics
- Fresh appearance

**Concepts Introduced:**
- Zone theming
- Palette variation
- Tile swapping
- Visual variety

**Code Written:**
```
- 4 zone themes (levels 1-4, 5-8, etc.)
- Different palettes per zone
- Thematic tile variations
- Fresh look each zone
```

**What the Learner Sees:**
Each zone looks different. Game stays visually fresh through all 16 levels.

---

### Unit 55: Two Player Mode

**Learning Objectives:**
- Alternating two player
- Separate scores
- Turn taking
- Competitive play

**Concepts Introduced:**
- Multiplayer design
- Player state separation
- Turn alternation
- Score comparison

**Code Written:**
```
- Two player option
- Alternate on death
- Separate score tracking
- Winner display
```

**What the Learner Sees:**
Two player mode. Take turns, compete for high score.

---

### Unit 56: Hidden Features

**Learning Objectives:**
- Add secret content
- Reward exploration
- Easter eggs
- Extra value

**Concepts Introduced:**
- Secret codes
- Hidden levels
- Easter eggs
- Player rewards

**Code Written:**
```
- Konami-style code
- Unlocks 4 bonus levels
- Secret room with message
- Reward for persistence
```

**What the Learner Sees:**
Secret code unlocks hidden content. Reward for dedicated players.

---

### Unit 57: Speed Run Mode

**Learning Objectives:**
- Add time attack
- Track best times
- No lives limit
- Different challenge

**Concepts Introduced:**
- Time attack design
- Timer display
- Best time tracking
- Alternative mode

**Code Written:**
```
- Time attack mode option
- Timer counts up
- No lives (restart on death)
- Best time per level
```

**What the Learner Sees:**
Speed run mode for time-based challenge. Different way to play.

---

### Unit 58: Statistics

**Learning Objectives:**
- Track play statistics
- Session records
- Achievement goals
- Long-term motivation

**Concepts Introduced:**
- Stats collection
- Display formatting
- Session persistence
- Goals

**Code Written:**
```
- Track: items, deaths, levels
- Display stats screen
- Best level reached
- Total items collected
```

**What the Learner Sees:**
Statistics screen shows achievements. Long-term goals to pursue.

---

### Unit 59: Intro Sequence

**Learning Objectives:**
- Create intro cutscene
- Story context
- Visual presentation
- Atmosphere setting

**Concepts Introduced:**
- Cutscene design
- Story presentation
- Timed sequences
- Player immersion

**Code Written:**
```
- Brief intro sequence
- Story text
- Character art
- Skip on button
```

**What the Learner Sees:**
Brief intro sets the scene. Press button to skip. Context for gameplay.

---

### Unit 60: Ending Sequence

**Learning Objectives:**
- Create victory ending
- Reward completion
- Credits display
- Closure

**Concepts Introduced:**
- Ending design
- Victory celebration
- Credits roll
- Player reward

**Code Written:**
```
- Victory screen
- Brief ending animation
- Credits display
- Return to title
```

**What the Learner Sees:**
Completing all levels shows victory sequence. Satisfying closure.

---

### Unit 61: ROM Optimisation

**Learning Objectives:**
- Fit in target ROM size
- Optimise CHR usage
- Bank if needed
- Size constraints

**Concepts Introduced:**
- ROM size limits
- CHR optimisation
- PRG organisation
- Size management

**Code Written:**
```
- Verify 32KB PRG fits
- Optimise CHR (8KB)
- Remove unused data
- Final size check
```

**What the Learner Sees:**
Game fits in standard NROM format. Distributable.

**Technical Details:**
- NROM: 32KB PRG, 8KB CHR
- No mapper needed
- Simplest cartridge type
- Maximum compatibility

---

### Unit 62: Controller 2 Support

**Learning Objectives:**
- Read second controller
- Two player simultaneous (optional)
- Alternative control
- Expanded input

**Concepts Introduced:**
- Controller 2 reading
- Simultaneous play option
- Control alternatives
- Input expansion

**Code Written:**
```
- Read $4017 for controller 2
- Optional simultaneous mode
- P1 + P2 scores
- Winner determination
```

**What the Learner Sees:**
Optional simultaneous two player mode. Both play at once.

---

### Unit 63: Final Testing

**Learning Objectives:**
- Complete test pass
- Edge cases
- Emulator compatibility
- Release candidate

**Concepts Introduced:**
- Release testing
- Compatibility
- Bug triage
- Release readiness

**Code Written:**
```
- Full playthrough all modes
- Test on multiple emulators
- Fix critical issues
- Declare RC
```

**What the Learner Sees:**
Thoroughly tested game. Works on all major emulators.

---

### Unit 64: Distribution

**Learning Objectives:**
- Create final ROM
- Documentation
- Package complete
- Release

**Concepts Introduced:**
- iNES format
- Documentation
- Distribution
- Release process

**Code Written:**
```
- Final .nes file
- Readme documentation
- Quick reference
- Source archive
```

**What the Learner Sees:**
Complete distribution package. Professional release.

**Phase 4 Checkpoint:**
The game is complete. Optimised, full-featured, professionally packaged. It could have sold for $29.99 in 1987. The learner has built a commercial-quality NES game.

---

## Skills Mastery Summary

By completing all 64 units, learners have demonstrated mastery of:

### 6502 Assembly
- Registers (A, X, Y) and addressing modes
- Stack operations and subroutines
- Zero page optimisation
- Interrupt handling

### NES PPU
- Pattern tables and tile graphics
- Nametables and screen layout
- Attribute tables and palettes
- OAM and sprite management
- VBlank timing and updates

### NES APU
- Pulse channels (melody, SFX)
- Triangle channel (bass)
- Noise channel (drums, SFX)
- Music playback systems

### Game Development
- Game loop structure
- State machine patterns
- Collision detection
- Scoring and progression
- Multiplayer implementation

### Professional Skills
- Code organisation
- Performance optimisation
- Testing methodology
- Distribution packaging

---

## Comparison: 16 Units vs 64 Units

| Aspect | 16-Unit Version | 64-Unit Version |
|--------|-----------------|-----------------|
| Levels | 1 | 16 + bonus + secret |
| Graphics | Static sprites | Animated, themed zones |
| Audio | None | Full SFX + music |
| Enemies | 1 type | 4 types |
| Modes | Single player | 1P, 2P, time attack |
| Features | Basic | Options, continues, high scores |
| Polish | Minimal | Transitions, intro, ending |
| Distribution | Working ROM | Complete package |
| Commercial viable? | No | Yes |
| Time investment | 16-32 hours | 64-128 hours |

---

## Version History

- **2.0 (2026-01-10):** Complete restructure. Playable game by Unit 16. Full unit-by-unit detail matching SID Symphony/Ink War format.
- **1.0 (2026-01-07):** Initial outline (PPU-theory focused, no game until Phase 2).
