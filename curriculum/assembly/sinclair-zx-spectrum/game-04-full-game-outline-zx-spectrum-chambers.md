# ZX Spectrum Game 4: Chambers - Full 128-Unit Outline

**Platform:** Sinclair ZX Spectrum
**Game:** Chambers
**Units:** 128 (8 phases × 16 units)
**Concept:** Flip-screen top-down exploration polished to commercial quality. Navigate rooms, collect items, avoid enemies, find the exit. In the Atic Atac tradition - the Spectrum's signature exploration genre.

---

## Overview

Chambers teaches multi-room game architecture and persistent state management. After single-screen games in Games 1-3, learners now build a world of interconnected rooms where the player's progress persists across screens.

**Key Learning Goals:**
- 4-way top-down movement
- Room data structures and transitions
- Persistent state (collected items stay collected)
- Inventory systems
- Enemy chase AI
- Key/door mechanics
- Attribute-based room theming

---

## Phase 1: Room Foundation (Units 1-16)

### Unit 1: Single Room Display
**Builds:** Draw a room from tile data.
**Teaches:** Tile-based room rendering.
**Code pattern:**
```z80
; Room data: 32×24 characters (actually 32×22 playable + borders)
; Each byte is a tile type: 0=floor, 1=wall, 2=door, etc.
ROOM_WIDTH  equ 32
ROOM_HEIGHT equ 22

room_data:
    ; Room 0 data - 32×22 = 704 bytes
    defb 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
    defb 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1
    ; ... (20 more rows)
    defb 1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1

draw_room:
    ld hl,room_data
    ld de,$4000         ; Screen start
    ld b,ROOM_HEIGHT

.row_loop:
    push bc
    ld b,ROOM_WIDTH

.tile_loop:
    ld a,(hl)           ; Get tile type
    call draw_tile
    inc hl
    inc de
    djnz .tile_loop

    ; Move to next screen row (skip to next char line)
    ; ... address calculation
    pop bc
    djnz .row_loop
    ret
```
**If it doesn't work:** Room garbled? Check screen address calculation between rows. Missing tiles? Verify tile drawing routine.

---

### Unit 2: Tile Graphics
**Builds:** UDG tiles for floor, walls, doors.
**Teaches:** User Defined Graphics.
**Code pattern:**
```z80
; UDG definitions - 8 bytes each
; Located at UDG area (typically $FF58 or custom location)
tile_graphics:
    ; Tile 0: Floor (empty/dotted)
    defb %00000000
    defb %00000000
    defb %00010000
    defb %00000000
    defb %00000000
    defb %00000001
    defb %00000000
    defb %00000000

    ; Tile 1: Wall (solid brick pattern)
    defb %11111111
    defb %10000100
    defb %10000100
    defb %11111111
    defb %11111111
    defb %00100001
    defb %00100001
    defb %11111111

    ; Tile 2: Door (vertical bars)
    defb %10101010
    defb %10101010
    defb %10101010
    defb %10101010
    defb %10101010
    defb %10101010
    defb %10101010
    defb %10101010
```
**If it doesn't work:** Wrong graphics? Check UDG pointer address. Corrupted? Verify 8 bytes per character.

---

### Unit 3: Room Attributes
**Builds:** Colour the room using attributes.
**Teaches:** Attribute area usage for rooms.
**Code pattern:**
```z80
; Attribute area: $5800-$5AFF
; Set room colours - walls one colour, floor another
ATTR_FLOOR equ %00000111    ; White on black
ATTR_WALL  equ %01000110    ; Yellow on black, bright
ATTR_DOOR  equ %01000010    ; Red on black, bright

colour_room:
    ld hl,room_data
    ld de,$5800         ; Attribute start
    ld b,ROOM_HEIGHT

.row_loop:
    push bc
    ld b,ROOM_WIDTH

.tile_loop:
    ld a,(hl)           ; Get tile type
    call get_tile_attr  ; Returns attribute in A
    ld (de),a
    inc hl
    inc de
    djnz .tile_loop

    pop bc
    djnz .row_loop
    ret

get_tile_attr:
    cp 0
    jr nz,.not_floor
    ld a,ATTR_FLOOR
    ret
.not_floor:
    cp 1
    jr nz,.not_wall
    ld a,ATTR_WALL
    ret
.not_wall:
    ld a,ATTR_DOOR
    ret
```
**If it doesn't work:** Wrong colours? Check attribute byte format (FBPPPIII). All same colour? Verify tile type comparison.

---

### Unit 4: Player Sprite
**Builds:** Player character displayed.
**Teaches:** Sprite on tiled background.
**Code pattern:**
```z80
player_x:   defb 128    ; Pixel position
player_y:   defb 88
player_char:defb 144    ; UDG character code

; Player sprite - 8×8 UDG
player_gfx:
    defb %00111100
    defb %01111110
    defb %11011011
    defb %11111111
    defb %11111111
    defb %01100110
    defb %01100110
    defb %00100100

draw_player:
    ; Convert pixel to screen address
    ld a,(player_y)
    ld b,a
    ld a,(player_x)
    ld c,a
    call get_screen_addr    ; Returns HL = screen address

    ; Draw player character
    ld de,player_gfx
    ld b,8
.draw_loop:
    ld a,(de)
    ld (hl),a
    inc de
    inc h               ; Next pixel row
    djnz .draw_loop
    ret
```
**If it doesn't work:** Player not visible? Check screen address calculation. Wrong position? Verify pixel-to-address conversion.

---

### Unit 5: Player Movement
**Builds:** 4-way keyboard movement.
**Teaches:** Top-down movement.
**Code pattern:**
```z80
PLAYER_SPEED equ 2

update_player:
    ; Clear old position
    call clear_player

    ; Check keys
    ld bc,$fbfe         ; Row: Q-T
    in a,(c)
    bit 0,a
    jr nz,.not_q
    ; Q = up
    ld a,(player_y)
    sub PLAYER_SPEED
    ld (player_y),a
.not_q:

    ld bc,$fdfe         ; Row: A-G
    in a,(c)
    bit 0,a
    jr nz,.not_a
    ; A = left
    ld a,(player_x)
    sub PLAYER_SPEED
    ld (player_x),a
.not_a:

    ; ... O = down, P = right

    ; Draw at new position
    call draw_player
    ret
```
**If it doesn't work:** Not responding? Check keyboard port addresses. Wrong direction? Verify bit numbers for keys.

---

### Unit 6: Wall Collision
**Builds:** Player can't walk through walls.
**Teaches:** Tile collision detection.
**Code pattern:**
```z80
; Check if position contains a wall
check_collision:
    ; Convert pixel position to tile position
    ; tile_x = player_x / 8, tile_y = player_y / 8
    ld a,(player_x)
    srl a
    srl a
    srl a               ; /8
    ld c,a              ; C = tile X

    ld a,(player_y)
    srl a
    srl a
    srl a               ; /8
    ld b,a              ; B = tile Y

    ; Calculate offset in room data
    ; offset = tile_y * 32 + tile_x
    ld h,0
    ld l,b
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl
    add hl,hl           ; * 32
    ld b,0
    add hl,bc           ; + tile_x

    ; Add room data base
    ld de,room_data
    add hl,de

    ; Check tile type
    ld a,(hl)
    cp 1                ; Wall?
    ret                 ; Z flag = collision
```
**If it doesn't work:** Walking through walls? Check division by 8. Wrong tile checked? Verify offset calculation.

---

### Unit 7: Smooth Movement
**Builds:** Player stops at wall, doesn't jitter.
**Teaches:** Movement with collision response.
**Code pattern:**
```z80
try_move:
    ; Save current position
    ld a,(player_x)
    ld (old_x),a
    ld a,(player_y)
    ld (old_y),a

    ; Apply movement
    call get_input
    call apply_movement

    ; Check collision
    call check_collision
    jr nz,.no_collision

    ; Collision! Restore position
    ld a,(old_x)
    ld (player_x),a
    ld a,(old_y)
    ld (old_y),a

.no_collision:
    ret
```

---

### Unit 8: Room Exit Detection
**Builds:** Detect when player reaches edge/door.
**Teaches:** Transition triggers.

---

### Unit 9: Multiple Rooms
**Builds:** Store multiple room layouts.
**Teaches:** Room array structure.
**Code pattern:**
```z80
; Room pointers table
NUM_ROOMS equ 16

room_pointers:
    defw room_00, room_01, room_02, room_03
    defw room_04, room_05, room_06, room_07
    defw room_08, room_09, room_10, room_11
    defw room_12, room_13, room_14, room_15

current_room: defb 0

get_room_address:
    ld a,(current_room)
    add a,a             ; * 2 for word offset
    ld hl,room_pointers
    ld c,a
    ld b,0
    add hl,bc
    ld e,(hl)
    inc hl
    ld d,(hl)           ; DE = room address
    ret
```

---

### Unit 10: Room Connections
**Builds:** Define which rooms connect where.
**Teaches:** Map connectivity.
**Code pattern:**
```z80
; Each room has 4 exit links: north, south, east, west
; $FF = no exit
room_exits:
    ; Room 0: North=4, South=$FF, East=1, West=$FF
    defb 4, $ff, 1, $ff
    ; Room 1: North=5, South=$FF, East=2, West=0
    defb 5, $ff, 2, 0
    ; ... etc for all rooms
```

---

### Unit 11: Room Transitions
**Builds:** Move between rooms smoothly.
**Teaches:** Screen transitions.
**Code pattern:**
```z80
change_room:
    ; A = direction (0=N, 1=S, 2=E, 3=W)
    push af

    ; Get exit for current room
    ld hl,room_exits
    ld a,(current_room)
    add a,a
    add a,a             ; * 4
    ld c,a
    ld b,0
    add hl,bc

    pop af
    ld c,a
    ld b,0
    add hl,bc           ; Point to correct exit

    ld a,(hl)
    cp $ff              ; No exit?
    ret z

    ; Change to new room
    ld (current_room),a

    ; Reposition player at opposite edge
    ; ... based on direction
    call draw_room
    ret
```
**If it doesn't work:** Wrong room? Check offset calculation. Player in wall? Set entry position correctly for direction.

---

### Unit 12: Entry Positions
**Builds:** Player appears at correct position when entering.
**Teaches:** Transition positioning.

---

### Unit 13: Room Theming
**Builds:** Different rooms have different colour schemes.
**Teaches:** Attribute variety.

---

### Unit 14: HUD Area
**Builds:** Status bar showing lives, keys, etc.
**Teaches:** Reserved screen area.

---

### Unit 15: Sound - Footsteps
**Builds:** Sound when player moves.
**Teaches:** Movement audio feedback.

---

### Unit 16: Phase 1 Polish
**Builds:** Basic room exploration working.

---

## Phase 2: Items and Inventory (Units 17-32)

### Unit 17: Collectible Items
**Builds:** Items placed in rooms.
**Teaches:** Item placement data.
**Code pattern:**
```z80
; Item structure: room, x, y, type, collected
MAX_ITEMS equ 32

item_data:
    ; Item 0: Key in room 3 at position 64,48
    defb 3, 64, 48, ITEM_KEY, 0
    ; Item 1: Treasure in room 7
    defb 7, 128, 96, ITEM_TREASURE, 0
    ; ... more items
```

---

### Unit 18: Item Drawing
**Builds:** Display items in current room.
**Teaches:** Conditional rendering.

---

### Unit 19: Item Collection
**Builds:** Player picks up items by touching.
**Teaches:** Item collision.

---

### Unit 20: Collection Persistence
**Builds:** Collected items stay collected.
**Teaches:** State persistence.

---

### Unit 21: Inventory System
**Builds:** Track what player carries.
**Teaches:** Inventory data structure.
**Code pattern:**
```z80
; Simple inventory - just counts of each item type
ITEM_KEY      equ 0
ITEM_TREASURE equ 1
ITEM_FOOD     equ 2
NUM_ITEM_TYPES equ 3

inventory:
    defs NUM_ITEM_TYPES, 0  ; Start with 0 of each

add_to_inventory:
    ; A = item type
    ld hl,inventory
    ld c,a
    ld b,0
    add hl,bc
    inc (hl)            ; Increment count
    ret

check_inventory:
    ; A = item type, returns count in A
    ld hl,inventory
    ld c,a
    ld b,0
    add hl,bc
    ld a,(hl)
    ret
```

---

### Unit 22: Inventory Display
**Builds:** Show inventory in HUD.
**Teaches:** Status display.

---

### Unit 23: Locked Doors
**Builds:** Some doors require keys.
**Teaches:** Conditional passage.

---

### Unit 24: Door Opening
**Builds:** Keys consumed when opening doors.
**Teaches:** Item usage.

---

### Unit 25: Coloured Keys/Doors
**Builds:** Red key for red door, etc.
**Teaches:** Item matching.

---

### Unit 26: Food/Health
**Builds:** Food restores health.
**Teaches:** Consumables.

---

### Unit 27: Health System
**Builds:** Player has health that depletes.
**Teaches:** Health tracking.

---

### Unit 28: Treasure Collection
**Builds:** Collect all treasures to win.
**Teaches:** Victory conditions.

---

### Unit 29: Item Respawning
**Builds:** Some items return after time.
**Teaches:** Timed respawns.

---

### Unit 30: Sound - Collection
**Builds:** Sound when picking up items.
**Teaches:** Collection feedback.

---

### Unit 31: Sound - Door Open
**Builds:** Sound when door unlocks.
**Teaches:** Action feedback.

---

### Unit 32: Phase 2 Polish
**Builds:** Working inventory system.

---

## Phase 3: Enemies (Units 33-48)

### Unit 33: Enemy Data
**Builds:** Enemy placement per room.
**Teaches:** Enemy data structures.
**Code pattern:**
```z80
; Enemy: room, x, y, type, state, direction
MAX_ENEMIES equ 24

enemy_data:
    ; Enemy in room 2
    defb 2, 100, 80, ENEMY_GHOST, 0, DIR_RIGHT
    defb 2, 180, 120, ENEMY_GHOST, 0, DIR_LEFT
    ; ... more enemies
```

---

### Unit 34: Enemy Drawing
**Builds:** Display enemies in current room.
**Teaches:** Multi-sprite rendering.

---

### Unit 35: Patrol Movement
**Builds:** Enemies walk back and forth.
**Teaches:** Simple AI patterns.
**Code pattern:**
```z80
update_patrol:
    ; Move in current direction
    ld a,(ix+ENEMY_DIR)
    cp DIR_RIGHT
    jr nz,.try_left

    ; Move right
    ld a,(ix+ENEMY_X)
    add a,ENEMY_SPEED
    ld (ix+ENEMY_X),a
    cp 240              ; Edge?
    ret c
    ld a,DIR_LEFT       ; Turn around
    ld (ix+ENEMY_DIR),a
    ret

.try_left:
    ; Move left
    ld a,(ix+ENEMY_X)
    sub ENEMY_SPEED
    ld (ix+ENEMY_X),a
    cp 16               ; Edge?
    ret nc
    ld a,DIR_RIGHT
    ld (ix+ENEMY_DIR),a
    ret
```

---

### Unit 36: Chase AI
**Builds:** Enemies move toward player.
**Teaches:** Chase behaviour.
**Code pattern:**
```z80
update_chase:
    ; Move X toward player
    ld a,(player_x)
    ld b,a
    ld a,(ix+ENEMY_X)
    cp b
    jr z,.check_y
    jr c,.move_right

.move_left:
    sub ENEMY_SPEED
    ld (ix+ENEMY_X),a
    jr .check_y

.move_right:
    add a,ENEMY_SPEED
    ld (ix+ENEMY_X),a

.check_y:
    ; Similar for Y axis
    ld a,(player_y)
    ld b,a
    ld a,(ix+ENEMY_Y)
    cp b
    ret z
    jr c,.move_down

.move_up:
    sub ENEMY_SPEED
    ld (ix+ENEMY_Y),a
    ret

.move_down:
    add a,ENEMY_SPEED
    ld (ix+ENEMY_Y),a
    ret
```
**If it doesn't work:** Not chasing? Check player position is being read. Stuck? May need diagonal movement.

---

### Unit 37: Wall-Aware AI
**Builds:** Enemies don't walk through walls.
**Teaches:** AI collision.

---

### Unit 38: Enemy-Player Collision
**Builds:** Touching enemy hurts player.
**Teaches:** Damage collision.

---

### Unit 39: Enemy Types
**Builds:** Different enemy behaviours.
**Teaches:** Entity variety.

---

### Unit 40: Ghost Enemies
**Builds:** Enemies that pass through walls.
**Teaches:** Type-specific behaviour.

---

### Unit 41: Ranged Enemies
**Builds:** Enemies that shoot projectiles.
**Teaches:** Enemy projectiles.

---

### Unit 42: Projectile System
**Builds:** Manage enemy bullets.
**Teaches:** Projectile pooling.

---

### Unit 43: Enemy Respawning
**Builds:** Enemies return when room re-entered.
**Teaches:** Room reset.

---

### Unit 44: Boss Enemy
**Builds:** Special powerful enemy.
**Teaches:** Boss design.

---

### Unit 45: Combat System
**Builds:** Player can attack enemies.
**Teaches:** Combat mechanics.

---

### Unit 46: Weapon Items
**Builds:** Sword or projectile pickup.
**Teaches:** Weapon system.

---

### Unit 47: Sound - Enemy Damage
**Builds:** Sound when hitting/being hit.
**Teaches:** Combat feedback.

---

### Unit 48: Phase 3 Polish
**Builds:** Complete enemy system.

---

## Phase 4: World Design (Units 49-64)

### Unit 49: Map Layout
**Builds:** 16+ room interconnected map.
**Teaches:** World design.

---

### Unit 50: Room Variety
**Builds:** Different room shapes and layouts.
**Teaches:** Level variety.

---

### Unit 51: Themed Areas
**Builds:** Different attribute colours for zones.
**Teaches:** Area theming.

---

### Unit 52: Secret Rooms
**Builds:** Hidden passages.
**Teaches:** Secret design.

---

### Unit 53: Traps
**Builds:** Environmental hazards.
**Teaches:** Trap design.

---

### Unit 54: Moving Hazards
**Builds:** Timing-based obstacles.
**Teaches:** Hazard timing.

---

### Unit 55: Teleporters
**Builds:** Instant transport between rooms.
**Teaches:** Non-linear navigation.

---

### Unit 56: One-Way Doors
**Builds:** Doors that only open from one side.
**Teaches:** Progression gates.

---

### Unit 57: Switches
**Builds:** Buttons that open doors elsewhere.
**Teaches:** Remote triggers.

---

### Unit 58: Pushable Blocks
**Builds:** Blocks player can push.
**Teaches:** Puzzle elements.

---

### Unit 59: Multiple Floors
**Builds:** Staircases between levels.
**Teaches:** Vertical world.

---

### Unit 60: Mini-Map
**Builds:** Show explored rooms.
**Teaches:** Map display.

---

### Unit 61: Save Points
**Builds:** Restore progress from checkpoints.
**Teaches:** Save system.

---

### Unit 62: Game Timer
**Builds:** Time limit adds pressure.
**Teaches:** Time mechanics.

---

### Unit 63: Score System
**Builds:** Points for items and enemies.
**Teaches:** Scoring.

---

### Unit 64: Phase 4 Polish
**Builds:** Complete world.

---

## Phase 5: Audio (Units 65-80)

### Unit 65: Sound System
**Builds:** Beeper sound management.
**Teaches:** Audio architecture.

---

### Unit 66-70: Sound Effects
**Builds:** Full SFX set (walk, hit, collect, door, death).
**Teaches:** Sound design.

---

### Unit 71: Title Music
**Builds:** Beeper music for title.
**Teaches:** Spectrum music.

---

### Unit 72: In-Game Music
**Builds:** Background music during play.
**Teaches:** Game music.

---

### Unit 73: Area Themes
**Builds:** Different music for zones.
**Teaches:** Musical variety.

---

### Unit 74: Sound Priority
**Builds:** Important sounds override others.
**Teaches:** Audio priority.

---

### Unit 75: Death Jingle
**Builds:** Sound when player dies.
**Teaches:** Failure feedback.

---

### Unit 76: Victory Fanfare
**Builds:** Sound for winning.
**Teaches:** Success audio.

---

### Unit 77: Low Health Warning
**Builds:** Audio cue for danger.
**Teaches:** Status audio.

---

### Unit 78: Boss Music
**Builds:** Tense music for boss.
**Teaches:** Boss atmosphere.

---

### Unit 79: Audio Polish
**Builds:** Volume balance.
**Teaches:** Audio mixing.

---

### Unit 80: Phase 5 Polish
**Builds:** Complete audio.

---

## Phase 6: Features (Units 81-96)

### Unit 81: Title Screen
**Builds:** Attractive presentation.
**Teaches:** Title design.

---

### Unit 82: Instructions
**Builds:** How to play screen.
**Teaches:** Onboarding.

---

### Unit 83: High Score Table
**Builds:** Top scores.
**Teaches:** Score persistence.

---

### Unit 84: High Score Entry
**Builds:** Name entry.
**Teaches:** Text input.

---

### Unit 85: Difficulty Settings
**Builds:** Easy/Normal/Hard.
**Teaches:** Difficulty options.

---

### Unit 86: Lives System
**Builds:** Multiple lives.
**Teaches:** Life tracking.

---

### Unit 87: Continue System
**Builds:** Continue after game over.
**Teaches:** Continues.

---

### Unit 88: Password System
**Builds:** Level passwords.
**Teaches:** Save codes.

---

### Unit 89: Pause Menu
**Builds:** In-game pause.
**Teaches:** Pause implementation.

---

### Unit 90: Inventory Screen
**Builds:** Full inventory view.
**Teaches:** Inventory UI.

---

### Unit 91: Map Screen
**Builds:** World map view.
**Teaches:** Map UI.

---

### Unit 92: Credits Screen
**Builds:** Attribution.
**Teaches:** Credits design.

---

### Unit 93: Multiple Endings
**Builds:** Different endings based on completion.
**Teaches:** Ending variety.

---

### Unit 94: Bonus Content
**Builds:** Unlockable extras.
**Teaches:** Rewards.

---

### Unit 95: Speedrun Timer
**Builds:** Track completion time.
**Teaches:** Timer display.

---

### Unit 96: Phase 6 Polish
**Builds:** Complete features.

---

## Phase 7: Optimisation (Units 97-112)

### Unit 97: Frame Rate
**Builds:** Consistent performance.
**Teaches:** Optimisation.

---

### Unit 98: Room Transitions
**Builds:** Fast, smooth transitions.
**Teaches:** Transition speed.

---

### Unit 99: Memory Layout
**Builds:** Efficient data organisation.
**Teaches:** Memory planning.

---

### Unit 100-104: Balancing
**Builds:** Fair difficulty, item placement.
**Teaches:** Game balance.

---

### Unit 105-108: Bug Fixing
**Builds:** Find and fix issues.
**Teaches:** Debugging.

---

### Unit 109-111: Polish
**Builds:** Visual consistency.
**Teaches:** Final polish.

---

### Unit 112: Phase 7 Complete
**Builds:** Stable game.

---

## Phase 8: Release (Units 113-128)

### Unit 113-116: Presentation
**Builds:** Loading screen, packaging.
**Teaches:** Distribution prep.

---

### Unit 117-120: Testing
**Builds:** Emulator and hardware tests.
**Teaches:** Quality assurance.

---

### Unit 121-124: Final Polish
**Builds:** Easter eggs, final fixes.
**Teaches:** Release preparation.

---

### Unit 125-127: Documentation
**Builds:** Manual concept.
**Teaches:** Documentation.

---

### Unit 128: Release
**Builds:** Final release.
**Teaches:** Shipping a game.

---

## Version History

- **1.0 (2026-01-18):** Initial 128-unit outline created.
