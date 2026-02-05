# Amiga Game 6: Gobble - Full 128-Unit Outline

**Platform:** Commodore Amiga
**Game:** Gobble
**Units:** 128 (8 phases × 16 units)
**Concept:** Pac-Man style maze game polished to commercial quality. Collect dots, avoid ghosts with distinct AI personalities, eat power pills to turn the tables. Smooth 50fps with Copper-enhanced effects.

---

## Overview

Gobble introduces constrained corridor movement and enemy AI personalities on the Amiga. After dungeon exploration (Crypt), learners create a maze game with sophisticated enemy behaviours. The four ghosts each have unique targeting logic - teaching that variety in AI creates emergent gameplay.

**Key Learning Goals:**
- Tile-based maze with Blitter rendering
- Constrained corridor movement
- Ghost AI personalities (Blinky, Pinky, Inky, Clyde)
- State machine (chase, scatter, frightened)
- Screen wrapping via tunnels
- Power-up state transitions

---

## Phase 1: Maze Foundation (Units 1-16)

### Unit 1: Maze Tilemap
**Builds:** Draw maze using Blitter tiles.
**Teaches:** Blitter tile rendering for maze.
**Code pattern:**
```asm
; Maze data: 28x31 tiles
; Tile types
TILE_EMPTY  equ 0
TILE_WALL   equ 1
TILE_DOT    equ 2
TILE_POWER  equ 3
TILE_TUNNEL equ 4

maze_data:
    dc.b 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    dc.b 1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1
    dc.b 1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1
    dc.b 1,3,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,3,1
    ; ... continue for 31 rows

draw_maze:
    lea     maze_data,a0
    lea     screen,a1
    move.w  #31-1,d7            ; 31 rows

.row_loop:
    move.w  #28-1,d6            ; 28 columns

.col_loop:
    moveq   #0,d0
    move.b  (a0)+,d0            ; Get tile type
    bsr     draw_maze_tile
    add.l   #TILE_WIDTH/8,a1    ; Next column
    dbf     d6,.col_loop

    ; Next row
    add.l   #(SCREEN_WIDTH-28)*TILE_WIDTH/8,a1
    add.l   #SCREEN_WIDTH*(TILE_HEIGHT-1),a1
    dbf     d7,.row_loop
    rts
```
**If it doesn't work:** Maze garbled? Check Blitter modulo calculations. Wrong tiles? Verify tile graphics data.

---

### Unit 2: Player BOB
**Builds:** Pac-Man as BOB.
**Teaches:** BOB setup.

---

### Unit 3: Grid Movement
**Builds:** Move tile by tile.
**Teaches:** Tile-aligned movement.
**Code pattern:**
```asm
player_tile_x:  dc.w 14     ; Current tile position
player_tile_y:  dc.w 23
player_pixel_x: dc.w 14*8   ; Pixel position (for smooth anim)
player_pixel_y: dc.w 23*8
player_dir:     dc.w 0      ; 0=right,1=down,2=left,3=up
target_pixel_x: dc.w 0      ; Target pixel position
target_pixel_y: dc.w 0
moving:         dc.w 0      ; 1 if animating between tiles

; Direction deltas
dir_dx: dc.w 1, 0, -1, 0
dir_dy: dc.w 0, 1, 0, -1

move_player:
    tst.w   moving
    bne.s   .animate

    ; At tile center - check for direction change
    bsr     check_input
    bsr     try_move
    rts

.animate:
    ; Smoothly move toward target
    move.w  target_pixel_x,d0
    move.w  player_pixel_x,d1
    cmp.w   d0,d1
    beq.s   .check_y
    bgt.s   .move_left
    addq.w  #2,player_pixel_x
    bra.s   .check_y
.move_left:
    subq.w  #2,player_pixel_x

.check_y:
    move.w  target_pixel_y,d0
    move.w  player_pixel_y,d1
    cmp.w   d0,d1
    beq.s   .check_done
    bgt.s   .move_up
    addq.w  #2,player_pixel_y
    bra.s   .check_done
.move_up:
    subq.w  #2,player_pixel_y

.check_done:
    move.w  player_pixel_x,d0
    cmp.w   target_pixel_x,d0
    bne.s   .still_moving
    move.w  player_pixel_y,d0
    cmp.w   target_pixel_y,d0
    bne.s   .still_moving

    ; Arrived at target
    clr.w   moving
    ; Update tile position
    move.w  target_pixel_x,d0
    lsr.w   #3,d0
    move.w  d0,player_tile_x
    move.w  target_pixel_y,d0
    lsr.w   #3,d0
    move.w  d0,player_tile_y

.still_moving:
    rts
```

---

### Unit 4: Wall Collision
**Builds:** Can only move through corridors.
**Teaches:** Tile collision.

---

### Unit 5: Dot Collection
**Builds:** Eating dots.
**Teaches:** Pickup mechanics.

---

### Unit 6: Dot Counter
**Builds:** Track remaining dots.
**Teaches:** Win condition.

---

### Unit 7: Power Pills
**Builds:** Large dots at corners.
**Teaches:** Power-up items.

---

### Unit 8: Score Display
**Builds:** Points using Blitter text.
**Teaches:** HUD rendering.

---

### Unit 9: Lives Display
**Builds:** Show remaining lives.
**Teaches:** Life tracking.

---

### Unit 10: Single Ghost
**Builds:** One enemy ghost BOB.
**Teaches:** Enemy basics.

---

### Unit 11: Ghost Movement
**Builds:** Ghost navigates maze.
**Teaches:** AI movement.

---

### Unit 12: Ghost Collision
**Builds:** Ghost catches player.
**Teaches:** Damage collision.

---

### Unit 13: Death Animation
**Builds:** Player death sequence.
**Teaches:** Death handling.

---

### Unit 14: Respawn
**Builds:** Player returns.
**Teaches:** Respawn.

---

### Unit 15: Basic Sound
**Builds:** Paula sample effects.
**Teaches:** Audio feedback.

---

### Unit 16: Phase 1 Polish
**Builds:** Basic game working.

---

## Phase 2: Ghost AI (Units 17-32)

### Unit 17: Blinky AI
**Builds:** Red ghost - direct chase.
**Teaches:** Chase behaviour.
**Code pattern:**
```asm
; Blinky: targets player's current tile
blinky_update_target:
    move.w  player_tile_x,blinky_target_x
    move.w  player_tile_y,blinky_target_y
    rts

; Generic ghost movement toward target
; Ghost chooses direction at each junction that
; minimizes distance to target (except can't reverse)
ghost_choose_direction:
    ; A0 = ghost data pointer
    ; For each valid direction (not wall, not reverse):
    ;   Calculate distance from resulting tile to target
    ; Choose direction with minimum distance

    moveq   #3,d7               ; Check 4 directions
    move.l  #$7fffffff,d6       ; Best distance (start huge)
    moveq   #-1,d5              ; Best direction

.check_dir:
    ; Skip if this is reverse of current direction
    move.w  GHOST_DIR(a0),d0
    eor.w   #2,d0               ; Opposite direction
    cmp.w   d7,d0
    beq.s   .next_dir

    ; Get tile in this direction
    move.w  d7,d0
    bsr     get_adjacent_tile
    ; D0 = tile type at adjacent position

    cmp.w   #TILE_WALL,d0
    beq.s   .next_dir           ; Can't go through walls

    ; Calculate distance to target
    bsr     calc_distance_to_target
    cmp.l   d6,d0
    bge.s   .next_dir           ; Not better

    ; New best
    move.l  d0,d6
    move.w  d7,d5

.next_dir:
    dbf     d7,.check_dir

    ; D5 = best direction
    move.w  d5,GHOST_DIR(a0)
    rts
```

---

### Unit 18: Pinky AI
**Builds:** Pink ghost - ambush.
**Teaches:** Predictive AI.

---

### Unit 19: Inky AI
**Builds:** Cyan ghost - flanker.
**Teaches:** Complex targeting.

---

### Unit 20: Clyde AI
**Builds:** Orange ghost - shy.
**Teaches:** Conditional AI.

---

### Unit 21: Scatter Mode
**Builds:** Ghosts retreat to corners.
**Teaches:** Mode switching.

---

### Unit 22: Chase/Scatter Timer
**Builds:** Automatic mode switching.
**Teaches:** Timed states.

---

### Unit 23: Frightened Mode
**Builds:** Power pill vulnerability.
**Teaches:** Power-up effects.

---

### Unit 24: Ghost Eating
**Builds:** Catch blue ghosts.
**Teaches:** Role reversal.

---

### Unit 25: Ghost Eyes
**Builds:** Eaten ghosts return home.
**Teaches:** Respawn AI.

---

### Unit 26: Ghost House
**Builds:** Ghosts start in pen.
**Teaches:** Spawn area.

---

### Unit 27: Release Timer
**Builds:** Staggered ghost release.
**Teaches:** Wave spawning.

---

### Unit 28: Tunnel Wrapping
**Builds:** Side tunnels.
**Teaches:** Screen wrap.

---

### Unit 29: Ghost Speed
**Builds:** Different speeds per state.
**Teaches:** Speed variation.

---

### Unit 30: Frightened Flashing
**Builds:** Warning before normal.
**Teaches:** Warning feedback.

---

### Unit 31: Cruise Elroy
**Builds:** Blinky speeds up late.
**Teaches:** Dynamic difficulty.

---

### Unit 32: Phase 2 Polish
**Builds:** Complete ghost AI.

---

## Phase 3: Level System (Units 33-48)

### Unit 33: Level Counter
**Builds:** Track current level.
**Teaches:** Level tracking.

---

### Unit 34: Level Complete
**Builds:** Clear dots to advance.
**Teaches:** Level completion.

---

### Unit 35: Level Transition
**Builds:** Copper flash effect.
**Teaches:** Transitions.

---

### Unit 36: Speed Progression
**Builds:** Faster each level.
**Teaches:** Difficulty scaling.

---

### Unit 37: Fruit Bonus
**Builds:** Bonus items appear.
**Teaches:** Bonus spawning.

---

### Unit 38: Fruit Variety
**Builds:** Different fruit per level.
**Teaches:** Level theming.

---

### Unit 39: Ghost Mode Timing
**Builds:** Shorter scatter higher levels.
**Teaches:** Timer progression.

---

### Unit 40: Power Duration
**Builds:** Shorter fright time.
**Teaches:** Balance progression.

---

### Unit 41: Maze Variants
**Builds:** Different mazes.
**Teaches:** Level variety.

---

### Unit 42: Intermissions
**Builds:** Cut-scenes with Copper.
**Teaches:** Story breaks.

---

### Unit 43-47: Level Polish
**Builds:** Complete level system.
**Teaches:** Level design.

---

### Unit 48: Phase 3 Polish
**Builds:** 20+ levels.

---

## Phase 4: Audio (Units 49-64)

### Unit 49: Waka Sound
**Builds:** Dot eating rhythm.
**Teaches:** Rhythmic audio.

---

### Unit 50: Siren Sound
**Builds:** Background tension.
**Teaches:** Ambient audio.

---

### Unit 51: Frightened Sound
**Builds:** Power mode audio.
**Teaches:** State audio.

---

### Unit 52: Ghost Eat Sound
**Builds:** Catching ghost.
**Teaches:** Success audio.

---

### Unit 53: Death Sound
**Builds:** Player death.
**Teaches:** Failure audio.

---

### Unit 54: Level Start
**Builds:** Ready tune.
**Teaches:** Fanfare.

---

### Unit 55: Fruit Sound
**Builds:** Bonus collection.
**Teaches:** Bonus audio.

---

### Unit 56: Extra Life
**Builds:** 1-up sound.
**Teaches:** Reward audio.

---

### Unit 57: MOD Music
**Builds:** Title music.
**Teaches:** MOD replay.

---

### Unit 58: Intermission Music
**Builds:** Cut-scene music.
**Teaches:** Scene music.

---

### Unit 59-63: Audio Polish
**Builds:** Balance and variety.
**Teaches:** Audio refinement.

---

### Unit 64: Phase 4 Polish
**Builds:** Complete audio.

---

## Phase 5: Presentation (Units 65-80)

### Unit 65: Title Screen
**Builds:** Attractive start.
**Teaches:** Title design.

---

### Unit 66: Demo Mode
**Builds:** AI plays attract.
**Teaches:** Attract mode.

---

### Unit 67: High Scores
**Builds:** Best scores.
**Teaches:** Score table.

---

### Unit 68: Name Entry
**Builds:** Enter name.
**Teaches:** Text input.

---

### Unit 69: Ghost Names
**Builds:** Show personalities.
**Teaches:** Character display.

---

### Unit 70: Instructions
**Builds:** How to play.
**Teaches:** Onboarding.

---

### Unit 71: Copper Effects
**Builds:** Gradient backgrounds.
**Teaches:** Copper polish.

---

### Unit 72: Smooth Animation
**Builds:** BOB animation.
**Teaches:** Animation polish.

---

### Unit 73-79: Visual Polish
**Builds:** Refinements.
**Teaches:** Quality.

---

### Unit 80: Phase 5 Polish
**Builds:** Complete presentation.

---

## Phase 6: Features (Units 81-96)

### Unit 81: Two-Player Mode
**Builds:** Alternating turns.
**Teaches:** Multiplayer.

---

### Unit 82: Simultaneous Mode
**Builds:** Two players at once.
**Teaches:** Co-op.

---

### Unit 83: Speed Options
**Builds:** Game speed selection.
**Teaches:** Options.

---

### Unit 84: Starting Level
**Builds:** Begin at higher level.
**Teaches:** Difficulty options.

---

### Unit 85: Practice Mode
**Builds:** Safe practice.
**Teaches:** Learning mode.

---

### Unit 86: AI Visualisation
**Builds:** Show ghost targets.
**Teaches:** Debug mode.

---

### Unit 87: Statistics
**Builds:** Career stats.
**Teaches:** Long-term tracking.

---

### Unit 88-95: Polish
**Builds:** Refinements.
**Teaches:** Quality.

---

### Unit 96: Phase 6 Polish
**Builds:** Complete features.

---

## Phase 7: Optimisation (Units 97-112)

### Unit 97: Frame Rate
**Builds:** Solid 50fps.
**Teaches:** Performance.

---

### Unit 98: Blitter Efficiency
**Builds:** Fast tile drawing.
**Teaches:** Blitter optimisation.

---

### Unit 99: AI Efficiency
**Builds:** Fast pathfinding.
**Teaches:** AI optimisation.

---

### Unit 100-104: Balance
**Builds:** Fair difficulty.
**Teaches:** Game balance.

---

### Unit 105-108: Bug Fixes
**Builds:** Fix issues.
**Teaches:** Debugging.

---

### Unit 109-111: Polish
**Builds:** Final refinements.
**Teaches:** Quality.

---

### Unit 112: Phase 7 Complete
**Builds:** Stable game.

---

## Phase 8: Release (Units 113-128)

### Unit 113-116: ADF Creation
**Builds:** Bootable disk.
**Teaches:** Distribution.

---

### Unit 117-120: Testing
**Builds:** Thorough testing.
**Teaches:** QA.

---

### Unit 121-124: Final Polish
**Builds:** Last fixes.
**Teaches:** Release prep.

---

### Unit 125-127: Documentation
**Builds:** Manual concept.
**Teaches:** Documentation.

---

### Unit 128: Release
**Builds:** Final release.
**Teaches:** Shipping.

---

## Version History

- **1.0 (2026-01-18):** Initial 128-unit outline created.
