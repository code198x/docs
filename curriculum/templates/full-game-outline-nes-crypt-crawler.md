# NES Game 5: Crypt Crawler - Full 128-Unit Outline

**Platform:** Nintendo Entertainment System
**Game:** Crypt Crawler
**Units:** 128 (8 phases × 16 units)
**Concept:** Flip-screen top-down dungeon exploration. Navigate interconnected rooms, collect keys and treasures, avoid monsters, find the exit. The ancestor to Zelda-style adventure games.

---

## Overview

Crypt Crawler introduces multi-screen world architecture on NES. After single-screen games (shooter, platformer, breakout, Pac-Man), learners manage persistent world state across many rooms using the PPU's nametable efficiently.

**Key Learning Goals:**
- Room data structures and transitions
- Persistent state across rooms
- Inventory systems with PPU display
- Enemy AI with room awareness
- Efficient nametable updates for room changes
- Top-down movement and collision

---

## Phase 1: Room Foundation (Units 1-16)

### Unit 1: Dungeon Room
**Builds:** Single room with walls and floor using background tiles.
**Teaches:** Nametable layout for rooms.
**Code pattern:**
```asm
; Room data: 16x15 metatiles (each metatile = 2x2 tiles = 16x16 pixels)
; Screen is 256x240, leaving room for HUD at top
; Room area: 256x240 - 16 pixels HUD = 256x224 = 16x14 metatiles

METATILE_FLOOR  = 0
METATILE_WALL   = 1
METATILE_DOOR   = 2

room_00:
    .byte 1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1   ; Top wall with door
    .byte 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1   ; Floor row
    .byte 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    .byte 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    .byte 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    .byte 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2   ; Side doors
    .byte 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2
    .byte 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    .byte 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    .byte 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    .byte 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    .byte 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    .byte 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    .byte 1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1   ; Bottom wall with door

draw_room:
    ; Set PPU address to start of room area (after HUD)
    lda #$20
    sta $2006
    lda #$40            ; Row 2 (after HUD rows)
    sta $2006

    ; Draw room using metatiles
    ldx #0              ; Room data index
@row_loop:
    ldy #0              ; Column counter
@col_loop:
    lda room_00,x
    jsr draw_metatile_top_row
    inx
    iny
    cpy #16
    bne @col_loop

    ; ... continue for all rows
    rts
```
**If it doesn't work:** Room garbled? Check PPU address and timing. Wrong tiles? Verify metatile lookup.

---

### Unit 2: Metatile System
**Builds:** 2×2 tile metatiles for efficient room design.
**Teaches:** Metatile patterns.
**Code pattern:**
```asm
; Each metatile is 4 tiles arranged 2x2
; Metatile data: top-left, top-right, bottom-left, bottom-right
metatile_data:
    ; Metatile 0: Floor
    .byte $00, $00, $00, $00
    ; Metatile 1: Wall
    .byte $01, $02, $03, $04
    ; Metatile 2: Door
    .byte $05, $06, $07, $08
    ; etc...

draw_metatile_top_row:
    ; A = metatile index
    asl
    asl                 ; ×4 for 4 bytes per metatile
    tay
    lda metatile_data,y
    sta $2007           ; Top-left
    lda metatile_data+1,y
    sta $2007           ; Top-right
    rts

draw_metatile_bottom_row:
    asl
    asl
    tay
    lda metatile_data+2,y
    sta $2007           ; Bottom-left
    lda metatile_data+3,y
    sta $2007           ; Bottom-right
    rts
```

---

### Unit 3: Player Sprite
**Builds:** Player character as sprite.
**Teaches:** Top-down player display.

---

### Unit 4: 4-Way Movement
**Builds:** Move in cardinal directions.
**Teaches:** Top-down controls.
**Code pattern:**
```asm
PLAYER_SPEED = 2

player_x:       .byte 128
player_y:       .byte 120
player_dir:     .byte 0     ; 0=up, 1=down, 2=left, 3=right

update_player:
    lda controller
    and #BUTTON_UP
    beq @not_up
    lda player_y
    sec
    sbc #PLAYER_SPEED
    sta player_y
    lda #0
    sta player_dir
@not_up:

    lda controller
    and #BUTTON_DOWN
    beq @not_down
    lda player_y
    clc
    adc #PLAYER_SPEED
    sta player_y
    lda #1
    sta player_dir
@not_down:

    lda controller
    and #BUTTON_LEFT
    beq @not_left
    lda player_x
    sec
    sbc #PLAYER_SPEED
    sta player_x
    lda #2
    sta player_dir
@not_left:

    lda controller
    and #BUTTON_RIGHT
    beq @not_right
    lda player_x
    clc
    adc #PLAYER_SPEED
    sta player_x
    lda #3
    sta player_dir
@not_right:
    rts
```

---

### Unit 5: Wall Collision
**Builds:** Can't walk through walls.
**Teaches:** Tile-based collision.
**Code pattern:**
```asm
; Check collision at pixel position
; Returns: A = metatile type at position (0 = floor/walkable)
check_tile_collision:
    ; Convert pixel to metatile coordinates
    ; X position / 16 = metatile column
    lda player_x
    lsr
    lsr
    lsr
    lsr
    sta temp_col

    ; Y position / 16 = metatile row (accounting for HUD)
    lda player_y
    sec
    sbc #16             ; Subtract HUD height
    lsr
    lsr
    lsr
    lsr
    sta temp_row

    ; Look up in current room data
    lda temp_row
    asl
    asl
    asl
    asl                 ; ×16 for room width
    ora temp_col
    tax
    lda current_room_data,x
    rts

; Check before moving
check_player_collision:
    jsr check_tile_collision
    cmp #METATILE_WALL
    beq @blocked
    clc                 ; Can move
    rts
@blocked:
    sec                 ; Blocked
    rts
```

---

### Unit 6: Room Transitions
**Builds:** Walking off screen changes room.
**Teaches:** Screen transitions.
**Code pattern:**
```asm
current_room:   .byte 0

; Room connections: north, south, west, east
; $FF = no exit
room_connections:
    ; Room 0
    .byte 1, $FF, $FF, 2     ; North=room 1, East=room 2
    ; Room 1
    .byte $FF, 0, 3, $FF     ; South=room 0, West=room 3
    ; etc...

check_room_transition:
    ; Check top edge
    lda player_y
    cmp #24             ; Top of room area
    bcs @not_north
    ; Going north
    ldx current_room
    lda room_connections,x  ; North connection
    cmp #$FF
    beq @blocked_north
    sta current_room
    lda #200            ; Enter from bottom
    sta player_y
    jsr load_room
    rts
@blocked_north:
    lda #24
    sta player_y
@not_north:

    ; Check bottom edge
    lda player_y
    cmp #208
    bcc @not_south
    ; Going south
    ; ... similar logic

@not_south:
    ; Check left and right edges similarly
    rts
```
**If it doesn't work:** Wrong room? Check connection table indexing. Stuck at edge? Verify boundary values.

---

### Unit 7: Room Data Loading
**Builds:** Load room from pointer table.
**Teaches:** Data-driven rooms.

---

### Unit 8: Multiple Rooms
**Builds:** 4 connected rooms.
**Teaches:** World layout.

---

### Unit 9: HUD Display
**Builds:** Health, keys, score at top.
**Teaches:** Status display.

---

### Unit 10: Collectible Items
**Builds:** Treasures in rooms.
**Teaches:** Item placement.

---

### Unit 11: Item Collection
**Builds:** Walking over collects item.
**Teaches:** Collection mechanics.

---

### Unit 12: Persistent State
**Builds:** Items stay collected.
**Teaches:** State persistence.
**Code pattern:**
```asm
; Track collected items per room
; Bit flags: 8 items per room maximum
MAX_ROOMS = 16
room_item_flags:
    .res MAX_ROOMS, 0

; Mark item as collected
; X = room number, A = item bit
collect_item:
    ora room_item_flags,x
    sta room_item_flags,x
    rts

; Check if item collected
; X = room number, A = item bit
; Returns: Z flag set if already collected
is_item_collected:
    and room_item_flags,x
    rts
```

---

### Unit 13: Score System
**Builds:** Points for treasure.
**Teaches:** Score tracking.

---

### Unit 14: Lives System
**Builds:** Multiple lives.
**Teaches:** Life tracking.

---

### Unit 15: Sound - Collect
**Builds:** Item pickup sound.
**Teaches:** APU feedback.

---

### Unit 16: Phase 1 Polish
**Builds:** Basic exploration working.

---

## Phase 2: Enemies and Combat (Units 17-32)

### Unit 17: Static Enemies
**Builds:** Monsters in rooms.
**Teaches:** Enemy placement.

---

### Unit 18: Enemy Sprites
**Builds:** Multiple enemy sprites.
**Teaches:** Sprite management.

---

### Unit 19: Patrol AI
**Builds:** Enemies walk patterns.
**Teaches:** Patrol behaviour.

---

### Unit 20: Chase AI
**Builds:** Enemies pursue player.
**Teaches:** Chase behaviour.

---

### Unit 21: Wall-Aware AI
**Builds:** Enemies avoid walls.
**Teaches:** AI collision.

---

### Unit 22: Player Damage
**Builds:** Touching enemies hurts.
**Teaches:** Damage mechanics.

---

### Unit 23: Health System
**Builds:** Health bar instead of instant death.
**Teaches:** Health tracking.

---

### Unit 24: Invincibility Frames
**Builds:** Brief immunity after hit.
**Teaches:** I-frames.

---

### Unit 25: Player Attack
**Builds:** Sword swing attack.
**Teaches:** Melee combat.
**Code pattern:**
```asm
player_attacking:   .byte 0
attack_timer:       .byte 0
attack_hitbox_x:    .byte 0
attack_hitbox_y:    .byte 0

player_attack:
    ; Check if already attacking
    lda player_attacking
    bne @done

    ; Check A button
    lda controller_press
    and #BUTTON_A
    beq @done

    ; Start attack
    lda #1
    sta player_attacking
    lda #10             ; Attack duration
    sta attack_timer

    ; Set hitbox based on facing direction
    lda player_dir
    cmp #0              ; Up
    bne @not_up
    lda player_x
    sta attack_hitbox_x
    lda player_y
    sec
    sbc #16
    sta attack_hitbox_y
    jmp @done
@not_up:
    ; ... other directions

@done:
    rts

update_attack:
    lda player_attacking
    beq @done

    ; Check hitbox vs enemies
    jsr check_attack_hit

    ; Decrement timer
    dec attack_timer
    bne @done
    lda #0
    sta player_attacking

@done:
    rts
```

---

### Unit 26: Attack Animation
**Builds:** Sword swing sprites.
**Teaches:** Attack visuals.

---

### Unit 27: Enemy Defeat
**Builds:** Killing enemies.
**Teaches:** Combat resolution.

---

### Unit 28: Enemy Types
**Builds:** Different monster behaviours.
**Teaches:** Enemy variety.

---

### Unit 29: Ranged Enemies
**Builds:** Enemies that shoot.
**Teaches:** Enemy projectiles.

---

### Unit 30: Boss Enemy
**Builds:** Large boss monster.
**Teaches:** Boss design.

---

### Unit 31: Combat Sounds
**Builds:** Attack, hit, death sounds.
**Teaches:** Combat audio.

---

### Unit 32: Phase 2 Polish
**Builds:** Complete combat.

---

## Phase 3: Keys and Puzzles (Units 33-48)

### Unit 33: Key Items
**Builds:** Keys to find.
**Teaches:** Key mechanics.

---

### Unit 34: Locked Doors
**Builds:** Doors requiring keys.
**Teaches:** Lock mechanics.

---

### Unit 35: Coloured Keys
**Builds:** Red, blue, green keys.
**Teaches:** Key matching.

---

### Unit 36: Inventory Display
**Builds:** Show held keys.
**Teaches:** Inventory UI.

---

### Unit 37: Health Potions
**Builds:** Restorative items.
**Teaches:** Consumables.

---

### Unit 38: Weapon Upgrades
**Builds:** Better swords.
**Teaches:** Equipment.

---

### Unit 39: Push Blocks
**Builds:** Moveable blocks.
**Teaches:** Puzzle objects.

---

### Unit 40: Pressure Plates
**Builds:** Floor switches.
**Teaches:** Triggers.

---

### Unit 41: Hidden Passages
**Builds:** Secret walls.
**Teaches:** Secrets.

---

### Unit 42: Trap Floors
**Builds:** Damage tiles.
**Teaches:** Floor hazards.

---

### Unit 43: Moving Platforms
**Builds:** Platforms over pits.
**Teaches:** Moving objects.

---

### Unit 44: Switch Doors
**Builds:** Hit switch to open.
**Teaches:** Remote triggers.

---

### Unit 45: Boss Key
**Builds:** Special key for boss room.
**Teaches:** Quest items.

---

### Unit 46: Map Item
**Builds:** Find the map.
**Teaches:** Map reveal.

---

### Unit 47: Compass Item
**Builds:** Points to objectives.
**Teaches:** Navigation aid.

---

### Unit 48: Phase 3 Polish
**Builds:** Complete puzzles.

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
**Builds:** Bonus treasure rooms.
**Teaches:** Exploration rewards.

---

### Unit 52: Difficulty Progression
**Builds:** Harder deeper in.
**Teaches:** Difficulty curve.

---

### Unit 53: Visual Themes
**Builds:** Different area looks.
**Teaches:** Visual variety.

---

### Unit 54: Boss Room
**Builds:** Final challenge.
**Teaches:** Climax design.

---

### Unit 55: Multiple Floors
**Builds:** Stairs between levels.
**Teaches:** Multi-floor design.

---

### Unit 56: Floor 2
**Builds:** Second dungeon level.
**Teaches:** Expanded world.

---

### Unit 57: Floor 3
**Builds:** Final floor.
**Teaches:** Expert area.

---

### Unit 58: Warp Zones
**Builds:** Shortcuts.
**Teaches:** Fast travel.

---

### Unit 59: Save System
**Builds:** Password or battery save.
**Teaches:** Progress save.

---

### Unit 60: Room Palettes
**Builds:** Different colours per zone.
**Teaches:** Palette swapping.

---

### Unit 61: Animated Tiles
**Builds:** Water, torches.
**Teaches:** Background animation.

---

### Unit 62: Environmental Hazards
**Builds:** Lava, spikes, water.
**Teaches:** Hazard variety.

---

### Unit 63: NPC Characters
**Builds:** Helpful characters.
**Teaches:** NPC design.

---

### Unit 64: Phase 4 Polish
**Builds:** Complete dungeon world.

---

## Phase 5: Audio (Units 65-80)

### Unit 65: Sound System
**Builds:** APU management.
**Teaches:** Audio architecture.

---

### Unit 66-70: Sound Effects
**Builds:** Walk, attack, collect, hurt, door sounds.
**Teaches:** SFX variety.

---

### Unit 71: Music - Title
**Builds:** Title theme.
**Teaches:** NES music.

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
**Builds:** Win fanfare.
**Teaches:** Success audio.

---

### Unit 75-78: Music Zones
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
**Builds:** Dungeon map view.
**Teaches:** Map display.

---

### Unit 85: Inventory Screen
**Builds:** Pause menu items.
**Teaches:** Inventory UI.

---

### Unit 86: High Scores
**Builds:** Best times/scores.
**Teaches:** Score tracking.

---

### Unit 87: Password System
**Builds:** Continue codes.
**Teaches:** Passwords.

---

### Unit 88: Game Over
**Builds:** Death screen.
**Teaches:** Failure handling.

---

### Unit 89: Victory Screen
**Builds:** Win celebration.
**Teaches:** Success display.

---

### Unit 90: Credits
**Builds:** Attribution.
**Teaches:** Credits design.

---

### Unit 91-95: Polish
**Builds:** Visual refinements.
**Teaches:** Presentation polish.

---

### Unit 96: Phase 6 Polish
**Builds:** Complete presentation.

---

## Phase 7: Optimisation (Units 97-112)

### Unit 97: Frame Rate
**Builds:** Solid 60fps.
**Teaches:** Performance.

---

### Unit 98: Sprite Limits
**Builds:** Handle 8-per-line.
**Teaches:** NES constraints.

---

### Unit 99: Room Load Speed
**Builds:** Fast transitions.
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

### Unit 113-116: ROM Creation
**Builds:** NES ROM file.
**Teaches:** ROM format.

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
