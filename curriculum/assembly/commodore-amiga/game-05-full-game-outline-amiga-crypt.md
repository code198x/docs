# Amiga Game 5: Crypt - Full 128-Unit Outline

**Platform:** Commodore Amiga
**Game:** Crypt
**Units:** 128 (8 phases × 16 units)
**Concept:** Flip-screen top-down dungeon exploration. Navigate interconnected rooms, collect keys and treasures, avoid monsters, find the exit. Smooth 50fps with Copper-enhanced room transitions and sampled audio.

---

## Overview

Crypt introduces multi-room architecture on the Amiga. After single-screen games (shooter, Frogger, breakout, platformer), learners manage persistent world state across many screens using efficient Blitter room rendering and Copper-timed transitions.

**Key Learning Goals:**
- Room data structures and transitions
- Persistent state management
- Inventory systems
- Enemy AI with room awareness
- Blitter tile rendering for rooms
- Copper colour splits for visual variety

---

## Phase 1: Room Foundation (Units 1-16)

### Unit 1: Dungeon Room
**Builds:** Single room with walls and floor using Blitter tiles.
**Teaches:** Blitter tile rendering.
**Code pattern:**
```asm
; Room data: 20x14 tiles (16x16 pixels each)
; Screen: 320x224 active area (256 for gameplay + HUD)
TILE_FLOOR  equ 0
TILE_WALL   equ 1
TILE_DOOR   equ 2

room_00:
    dc.b 1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1   ; Top wall with door
    dc.b 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1   ; Floor
    dc.b 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    dc.b 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    dc.b 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    dc.b 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2   ; Side doors
    dc.b 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2
    dc.b 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    dc.b 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    dc.b 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    dc.b 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    dc.b 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    dc.b 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    dc.b 1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1   ; Bottom wall with door

draw_room:
    lea     room_00,a0
    lea     screen,a1
    move.w  #14-1,d7            ; 14 rows

.row_loop:
    move.w  #20-1,d6            ; 20 columns
    move.l  a1,a2               ; Save row start

.col_loop:
    moveq   #0,d0
    move.b  (a0)+,d0            ; Get tile index
    bsr     draw_tile           ; Draw 16x16 tile at a1
    add.l   #2,a1               ; Next tile column (16 pixels = 2 bytes)
    dbf     d6,.col_loop

    ; Move to next row
    move.l  a2,a1
    add.l   #SCREEN_WIDTH*16,a1 ; 16 pixel rows down
    dbf     d7,.row_loop
    rts

draw_tile:
    ; D0 = tile index, A1 = screen destination
    ; Look up tile graphics and Blitter copy
    lsl.w   #8,d0               ; ×256 for tile size (16×16 = 256 bytes/plane)
    lea     tile_graphics,a3
    add.l   d0,a3

    ; Wait for Blitter
.wait:
    btst    #6,$dff002
    bne.s   .wait

    ; Set up Blitter copy
    move.l  a3,$dff050          ; Source A
    move.l  a1,$dff054          ; Destination D
    move.w  #SCREEN_WIDTH-2,$dff064  ; D modulo
    move.w  #0,$dff062          ; A modulo
    move.w  #$09f0,$dff040      ; BLTCON0: D=A
    move.w  #0,$dff042          ; BLTCON1
    move.w  #(16<<6)|1,$dff058  ; BLTSIZE: 16 rows, 1 word
    rts
```
**If it doesn't work:** Room not drawing? Check Blitter DMA enabled. Wrong tiles? Verify tile index calculation.

---

### Unit 2: Tile Graphics
**Builds:** Design floor, wall, door tiles.
**Teaches:** Tile graphics.

---

### Unit 3: Player BOB
**Builds:** Player as Blitter Object.
**Teaches:** BOB in tile world.

---

### Unit 4: 4-Way Movement
**Builds:** Top-down movement.
**Teaches:** Cardinal direction control.
**Code pattern:**
```asm
PLAYER_SPEED    equ 2
player_x:       dc.w 160
player_y:       dc.w 112
player_dir:     dc.w 0      ; 0=up, 1=down, 2=left, 3=right

update_player:
    move.w  $dff00c,d0      ; JOY1DAT

    ; Check up (bit 8)
    btst    #8,d0
    beq.s   .not_up
    sub.w   #PLAYER_SPEED,player_y
    move.w  #0,player_dir
.not_up:

    ; Check down (bit 0)
    btst    #0,d0
    beq.s   .not_down
    add.w   #PLAYER_SPEED,player_y
    move.w  #1,player_dir
.not_down:

    ; Check left (bit 9)
    btst    #9,d0
    beq.s   .not_left
    sub.w   #PLAYER_SPEED,player_x
    move.w  #2,player_dir
.not_left:

    ; Check right (bit 1)
    btst    #1,d0
    beq.s   .not_right
    add.w   #PLAYER_SPEED,player_x
    move.w  #3,player_dir
.not_right:
    rts
```

---

### Unit 5: Wall Collision
**Builds:** Can't walk through walls.
**Teaches:** Tile collision.
**Code pattern:**
```asm
; Check tile at pixel position
; Input: D0 = X, D1 = Y
; Output: D0 = tile type
get_tile_at:
    ; Convert to tile coordinates
    lsr.w   #4,d0               ; X / 16
    lsr.w   #4,d1               ; Y / 16

    ; Look up in current room
    mulu    #20,d1              ; row × width
    add.w   d0,d1               ; + column
    lea     current_room_data,a0
    moveq   #0,d0
    move.b  (a0,d1.w),d0
    rts

check_wall:
    ; Check player's four corners
    move.w  player_x,d0
    move.w  player_y,d1
    bsr     get_tile_at
    cmp.w   #TILE_WALL,d0
    beq.s   .blocked
    ; Check other corners...
    moveq   #0,d0               ; Clear = can move
    rts
.blocked:
    moveq   #1,d0               ; Blocked
    rts
```

---

### Unit 6: Room Transitions
**Builds:** Exit room loads new room.
**Teaches:** Screen transitions.

---

### Unit 7: Copper Transition
**Builds:** Smooth fade between rooms.
**Teaches:** Copper fades.
**Code pattern:**
```asm
; Fade out current room, load new, fade in
transition_room:
    ; Fade out
    move.w  #15,d7              ; 16 steps
.fade_out:
    bsr     wait_vblank
    bsr     darken_palette
    dbf     d7,.fade_out

    ; Load new room (screen is black)
    bsr     load_room
    bsr     draw_room

    ; Fade in
    move.w  #15,d7
.fade_in:
    bsr     wait_vblank
    bsr     brighten_palette
    dbf     d7,.fade_in
    rts

darken_palette:
    ; Reduce each colour component
    lea     copper_palette,a0
    move.w  #15,d6              ; 16 colours
.loop:
    move.w  (a0),d0
    ; Reduce R
    move.w  d0,d1
    and.w   #$0f00,d1
    beq.s   .skip_r
    sub.w   #$0100,d1
.skip_r:
    ; Similar for G, B...
    move.w  d1,(a0)+
    dbf     d6,.loop
    rts
```

---

### Unit 8: Multiple Rooms
**Builds:** 4 connected rooms.
**Teaches:** Room connections.

---

### Unit 9: HUD Display
**Builds:** Health, keys, score.
**Teaches:** Status display.

---

### Unit 10: Item Collection
**Builds:** Treasures to collect.
**Teaches:** Collection mechanics.

---

### Unit 11: Persistent State
**Builds:** Items stay collected.
**Teaches:** State management.

---

### Unit 12: Score System
**Builds:** Points for treasure.
**Teaches:** Scoring.

---

### Unit 13: Lives System
**Builds:** Multiple lives.
**Teaches:** Life tracking.

---

### Unit 14: Sound - Steps
**Builds:** Footstep sounds.
**Teaches:** Movement audio.

---

### Unit 15: Sound - Collect
**Builds:** Pickup sound.
**Teaches:** Feedback audio.

---

### Unit 16: Phase 1 Polish
**Builds:** Basic exploration.

---

## Phase 2: Enemies and Combat (Units 17-32)

### Unit 17: Enemy BOBs
**Builds:** Monster sprites.
**Teaches:** Multi-BOB management.

---

### Unit 18: Patrol AI
**Builds:** Enemies patrol paths.
**Teaches:** Patrol behaviour.

---

### Unit 19: Chase AI
**Builds:** Enemies pursue player.
**Teaches:** Chase behaviour.
**Code pattern:**
```asm
; Simple chase: move toward player
update_chaser:
    ; A0 = enemy data pointer
    move.w  ENEMY_X(a0),d0
    move.w  player_x,d1
    cmp.w   d0,d1
    beq.s   .check_y
    bgt.s   .move_right
    subq.w  #1,ENEMY_X(a0)
    bra.s   .check_y
.move_right:
    addq.w  #1,ENEMY_X(a0)

.check_y:
    move.w  ENEMY_Y(a0),d0
    move.w  player_y,d1
    cmp.w   d0,d1
    beq.s   .done
    bgt.s   .move_down
    subq.w  #1,ENEMY_Y(a0)
    bra.s   .done
.move_down:
    addq.w  #1,ENEMY_Y(a0)
.done:
    rts
```

---

### Unit 20: Wall-Aware AI
**Builds:** Enemies navigate around walls.
**Teaches:** Pathfinding basics.

---

### Unit 21: Player Damage
**Builds:** Enemies hurt player.
**Teaches:** Damage mechanics.

---

### Unit 22: Health System
**Builds:** Health bar.
**Teaches:** Health tracking.

---

### Unit 23: Player Attack
**Builds:** Sword swing.
**Teaches:** Melee combat.

---

### Unit 24: Attack Animation
**Builds:** Sword sprite animation.
**Teaches:** Attack visuals.

---

### Unit 25: Enemy Defeat
**Builds:** Killing enemies.
**Teaches:** Combat resolution.

---

### Unit 26: Enemy Variety
**Builds:** Different monster types.
**Teaches:** Enemy variety.

---

### Unit 27: Ranged Enemies
**Builds:** Shooting monsters.
**Teaches:** Enemy projectiles.

---

### Unit 28: Boss Monster
**Builds:** Large boss enemy.
**Teaches:** Boss design.

---

### Unit 29: Enemy Animation
**Builds:** Animated monsters.
**Teaches:** Multi-entity animation.

---

### Unit 30: Combat Sounds
**Builds:** Attack, hit, death sounds.
**Teaches:** Combat audio.

---

### Unit 31: Death and Respawn
**Builds:** Player death handling.
**Teaches:** Death mechanics.

---

### Unit 32: Phase 2 Polish
**Builds:** Complete combat.

---

## Phase 3: Keys and Inventory (Units 33-48)

### Unit 33: Key Items
**Builds:** Keys to find.
**Teaches:** Key mechanics.

---

### Unit 34: Locked Doors
**Builds:** Doors requiring keys.
**Teaches:** Lock mechanics.

---

### Unit 35: Coloured Keys
**Builds:** Red, blue, green, gold keys.
**Teaches:** Key matching.

---

### Unit 36: Inventory System
**Builds:** Track held items.
**Teaches:** Inventory structure.
**Code pattern:**
```asm
; Inventory structure
MAX_ITEMS       equ 8
inventory:      ds.w MAX_ITEMS  ; Item type (0 = empty)
inventory_count: dc.w 0

add_item:
    ; D0 = item type
    move.w  inventory_count,d1
    cmp.w   #MAX_ITEMS,d1
    bge.s   .full

    lea     inventory,a0
    lsl.w   #1,d1               ; ×2 for word
    move.w  d0,(a0,d1.w)
    addq.w  #1,inventory_count
    bsr     update_inventory_display
    clc
    rts

.full:
    sec                         ; Inventory full
    rts

has_item:
    ; D0 = item type to check
    ; Returns: D0 = 1 if has, 0 if not
    lea     inventory,a0
    move.w  inventory_count,d1
    beq.s   .not_found
.loop:
    cmp.w   (a0)+,d0
    beq.s   .found
    dbf     d1,.loop
.not_found:
    moveq   #0,d0
    rts
.found:
    moveq   #1,d0
    rts
```

---

### Unit 37: Inventory Display
**Builds:** Show inventory on screen.
**Teaches:** Inventory UI.

---

### Unit 38: Health Potions
**Builds:** Restorative items.
**Teaches:** Consumables.

---

### Unit 39: Weapon Upgrades
**Builds:** Better weapons.
**Teaches:** Equipment.

---

### Unit 40: Push Blocks
**Builds:** Moveable blocks.
**Teaches:** Puzzle objects.

---

### Unit 41: Pressure Plates
**Builds:** Floor switches.
**Teaches:** Triggers.

---

### Unit 42: Hidden Passages
**Builds:** Secret walls.
**Teaches:** Secrets.

---

### Unit 43: Trap Floors
**Builds:** Damage tiles.
**Teaches:** Hazards.

---

### Unit 44: Teleporters
**Builds:** Warp points.
**Teaches:** Teleport mechanics.

---

### Unit 45: Boss Key
**Builds:** Special final key.
**Teaches:** Quest items.

---

### Unit 46: Map Item
**Builds:** Reveals dungeon map.
**Teaches:** Map unlock.

---

### Unit 47: Compass Item
**Builds:** Points to objectives.
**Teaches:** Navigation.

---

### Unit 48: Phase 3 Polish
**Builds:** Complete inventory and puzzles.

---

## Phase 4: World Design (Units 49-64)

### Unit 49: Dungeon Layout
**Builds:** 16-room dungeon.
**Teaches:** World design.

---

### Unit 50: Critical Path
**Builds:** Required route.
**Teaches:** Level flow.

---

### Unit 51: Optional Areas
**Builds:** Bonus rooms.
**Teaches:** Exploration rewards.

---

### Unit 52: Difficulty Progression
**Builds:** Harder areas.
**Teaches:** Difficulty curve.

---

### Unit 53: Zone Themes
**Builds:** Different visual areas.
**Teaches:** Visual variety.

---

### Unit 54: Boss Room
**Builds:** Final challenge.
**Teaches:** Climax design.

---

### Unit 55: Multiple Floors
**Builds:** Stairs between levels.
**Teaches:** Multi-floor.

---

### Unit 56-58: Floors 2-3
**Builds:** Additional dungeon levels.
**Teaches:** Expanded world.

---

### Unit 59: Warp Zones
**Builds:** Shortcuts.
**Teaches:** Fast travel.

---

### Unit 60: Save System
**Builds:** Save progress.
**Teaches:** Persistence.

---

### Unit 61: Copper Zone Palettes
**Builds:** Different colours per area.
**Teaches:** Copper theming.

---

### Unit 62: Animated Tiles
**Builds:** Water, torches.
**Teaches:** Tile animation.

---

### Unit 63: Environmental Hazards
**Builds:** Lava, water pits.
**Teaches:** Hazard variety.

---

### Unit 64: Phase 4 Polish
**Builds:** Complete dungeon world.

---

## Phase 5: Audio (Units 65-80)

### Unit 65: Sound System
**Builds:** Paula sample manager.
**Teaches:** Audio architecture.

---

### Unit 66-70: Sound Effects
**Builds:** Footsteps, attack, collect, hurt, door.
**Teaches:** SFX variety.

---

### Unit 71: Music - Title
**Builds:** Title MOD.
**Teaches:** MOD replay.

---

### Unit 72: Music - Dungeon
**Builds:** Exploration music.
**Teaches:** Game music.

---

### Unit 73: Music - Boss
**Builds:** Boss battle music.
**Teaches:** Boss atmosphere.

---

### Unit 74: Music - Victory
**Builds:** Win music.
**Teaches:** Success audio.

---

### Unit 75-78: Zone Music
**Builds:** Different music per area.
**Teaches:** Musical variety.

---

### Unit 79: Audio Balance
**Builds:** Volume levels.
**Teaches:** Audio mixing.

---

### Unit 80: Phase 5 Polish
**Builds:** Complete audio.

---

## Phase 6: Presentation (Units 81-96)

### Unit 81: Title Screen
**Builds:** Start screen.
**Teaches:** Title design.

---

### Unit 82: Story Intro
**Builds:** Brief narrative.
**Teaches:** Story context.

---

### Unit 83: Instructions
**Builds:** How to play.
**Teaches:** Onboarding.

---

### Unit 84: Map Screen
**Builds:** Dungeon map.
**Teaches:** Map display.

---

### Unit 85: Pause/Inventory
**Builds:** Pause menu.
**Teaches:** Pause UI.

---

### Unit 86: High Scores
**Builds:** Best times.
**Teaches:** Score tracking.

---

### Unit 87: Game Over
**Builds:** Death screen.
**Teaches:** Failure handling.

---

### Unit 88: Victory Screen
**Builds:** Win celebration.
**Teaches:** Success display.

---

### Unit 89: Credits
**Builds:** Attribution.
**Teaches:** Credits.

---

### Unit 90-95: Visual Polish
**Builds:** Copper effects, transitions.
**Teaches:** Presentation polish.

---

### Unit 96: Phase 6 Polish
**Builds:** Complete presentation.

---

## Phase 7: Optimisation (Units 97-112)

### Unit 97: Frame Rate
**Builds:** Solid 50fps.
**Teaches:** Performance.

---

### Unit 98: Blitter Efficiency
**Builds:** Fast room drawing.
**Teaches:** Blitter optimisation.

---

### Unit 99: Room Load Speed
**Builds:** Quick transitions.
**Teaches:** Load optimisation.

---

### Unit 100: Memory Layout
**Builds:** Efficient organisation.
**Teaches:** Memory planning.

---

### Unit 101-104: Balance
**Builds:** Fair difficulty.
**Teaches:** Game balance.

---

### Unit 105-108: Bug Fixes
**Builds:** Find and fix.
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
