# C64 Game 5: Catacombs - Full 128-Unit Outline

**Platform:** Commodore 64
**Game:** Catacombs
**Units:** 128 (8 phases × 16 units)
**Concept:** Flip-screen top-down dungeon exploration. Navigate interconnected rooms, collect keys and treasures, avoid monsters, find the exit. In the tradition of classic C64 explorers like Atic Atac and Gauntlet.

---

## Overview

Catacombs introduces multi-room game architecture. After single-screen games (shooter, platformer, maze, breakout), learners now manage persistent world state across many screens. This is the foundation for larger adventure games.

**Key Learning Goals:**
- Room data structures and transitions
- Persistent state (items stay collected)
- Inventory systems
- Enemy AI with room awareness
- Character set graphics for dungeon tiles
- Multi-screen world design

---

## Phase 1: Room Foundation (Units 1-16)

### Unit 1: Dungeon Room
**Builds:** Single room with walls and floor using character graphics.
**Teaches:** Custom character set for dungeon tiles.
**Code pattern:**
```asm
; Character set: wall, floor, door tiles
; Screen codes for room layout
!to "catacombs.prg", cbm
* = $0801
    !byte $0c,$08,$0a,$00,$9e,$32,$30,$36,$34,$00,$00,$00

* = $0810
start:
    jsr setup_charset
    jsr draw_room
    jmp *               ; Wait for now

; Room data: 40x25 screen codes
room_01:
    !byte 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1  ; Top wall (first half)
    !byte 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1  ; Top wall (second half)
    !byte 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1  ; Row with floor
    ; ... etc for 25 rows

CHAR_WALL  = 1
CHAR_FLOOR = 0
CHAR_DOOR  = 2

draw_room:
    ldx #0
    ldy #0
@loop:
    lda room_01,x
    sta $0400,x         ; Screen RAM
    lda #1              ; White
    sta $d800,x         ; Colour RAM
    inx
    cpx #250            ; First 250 chars
    bne @loop
    ; Continue for rest of screen...
    rts
```
**If it doesn't work:** Garbage on screen? Check character set is copied to correct location. Wrong colours? Verify colour RAM writes.

---

### Unit 2: Custom Character Set
**Builds:** Design wall, floor, door characters.
**Teaches:** Character graphics design.
**Code pattern:**
```asm
; Copy custom charset to $3000
setup_charset:
    ; Point VIC to charset at $3000
    lda $d018
    and #$f0
    ora #$0c            ; Charset at $3000
    sta $d018

    ; Copy ROM charset first (for letters/numbers)
    sei
    lda #$33
    sta $01             ; Enable char ROM
    ldx #0
@copy_rom:
    lda $d000,x
    sta $3000,x
    lda $d100,x
    sta $3100,x
    inx
    bne @copy_rom
    lda #$37
    sta $01             ; Restore normal memory
    cli

    ; Now add custom tiles
    ldx #0
@copy_custom:
    lda custom_chars,x
    sta $3000,x         ; Overwrite first chars
    inx
    cpx #32             ; 4 characters × 8 bytes
    bne @copy_custom
    rts

custom_chars:
    ; Char 0: Floor (dots pattern)
    !byte %00000000
    !byte %00100010
    !byte %00000000
    !byte %10001000
    !byte %00000000
    !byte %00100010
    !byte %00000000
    !byte %10001000

    ; Char 1: Wall (solid brick)
    !byte %11111111
    !byte %10001000
    !byte %11111111
    !byte %00100010
    !byte %11111111
    !byte %10001000
    !byte %11111111
    !byte %00100010

    ; Char 2: Door (archway)
    !byte %01111110
    !byte %11000011
    !byte %11000011
    !byte %11000011
    !byte %11000011
    !byte %11000011
    !byte %11000011
    !byte %11111111

    ; Char 3: Key
    !byte %00011000
    !byte %00100100
    !byte %00011000
    !byte %00001000
    !byte %00001000
    !byte %00011100
    !byte %00001000
    !byte %00000000
```
**If it doesn't work:** Charset not showing? Check $D018 bank selection. Garbled characters? Verify ROM banking sequence.

---

### Unit 3: Player Character
**Builds:** Player displayed as sprite.
**Teaches:** Sprite in character-based game.
**Code pattern:**
```asm
player_x:   !byte 160   ; Screen position
player_y:   !byte 140
player_room: !byte 0    ; Current room index

setup_player:
    ; Enable sprite 0
    lda #1
    sta $d015

    ; Set sprite pointer
    lda #(player_sprite/64)
    sta $07f8

    ; Position sprite
    lda player_x
    sta $d000
    lda player_y
    sta $d001

    ; Colour
    lda #1              ; White
    sta $d027
    rts

update_player_sprite:
    lda player_x
    sta $d000
    lda player_y
    sta $d001
    rts
```

---

### Unit 4: Player Movement
**Builds:** 4-way joystick movement.
**Teaches:** Top-down movement.
**Code pattern:**
```asm
PLAYER_SPEED = 2

read_joystick:
    lda $dc00           ; Joystick port 2
    sta joy_state
    rts

update_player:
    lda joy_state
    lsr                 ; Bit 0 = up
    bcs @not_up
    lda player_y
    sec
    sbc #PLAYER_SPEED
    sta player_y
@not_up:
    lda joy_state
    lsr
    lsr                 ; Bit 1 = down
    bcs @not_down
    lda player_y
    clc
    adc #PLAYER_SPEED
    sta player_y
@not_down:
    lda joy_state
    lsr
    lsr
    lsr                 ; Bit 2 = left
    bcs @not_left
    lda player_x
    sec
    sbc #PLAYER_SPEED
    sta player_x
@not_left:
    lda joy_state
    lsr
    lsr
    lsr
    lsr                 ; Bit 3 = right
    bcs @not_right
    lda player_x
    clc
    adc #PLAYER_SPEED
    sta player_x
@not_right:
    jsr update_player_sprite
    rts
```
**If it doesn't work:** Not moving? Check joystick port (CIA $DC00). Moving wrong direction? Joystick bits are active low.

---

### Unit 5: Wall Collision
**Builds:** Player can't walk through walls.
**Teaches:** Character-based collision.
**Code pattern:**
```asm
; Check if position is walkable
; Input: X = screen X (pixels), Y = screen Y (pixels)
; Output: Carry set if blocked
check_collision:
    ; Convert pixel to character position
    txa
    lsr
    lsr
    lsr                 ; /8 for char column
    sta temp_col

    tya
    lsr
    lsr
    lsr                 ; /8 for char row
    sta temp_row

    ; Calculate screen address
    lda temp_row
    asl
    tax
    lda screen_row_lo,x
    sta $fb
    lda screen_row_hi,x
    sta $fc

    ldy temp_col
    lda ($fb),y         ; Get screen code

    cmp #CHAR_WALL
    beq @blocked
    clc                 ; Clear = walkable
    rts
@blocked:
    sec                 ; Set = blocked
    rts

; Screen row address table
screen_row_lo:
    !byte <$0400, <$0428, <$0450, <$0478, <$04a0
    !byte <$04c8, <$04f0, <$0518, <$0540, <$0568
    ; ... etc for 25 rows
screen_row_hi:
    !byte >$0400, >$0428, >$0450, >$0478, >$04a0
    ; ... etc
```
**If it doesn't work:** Walking through walls? Check pixel-to-char conversion. Stuck? Verify collision checked before position update.

---

### Unit 6: Door Detection
**Builds:** Standing on door tile detected.
**Teaches:** Tile type checking.

---

### Unit 7: Room Transitions
**Builds:** Walking through door changes room.
**Teaches:** Screen transitions.
**Code pattern:**
```asm
; Door data: which room each door leads to
; Format: door_x, door_y, target_room, entry_x, entry_y
room_01_doors:
    !byte 19, 0, 1, 19, 23    ; North door → room 1, enter from south
    !byte 39, 12, 2, 1, 12    ; East door → room 2, enter from west
    !byte $ff                  ; End marker

check_door_transition:
    ; Get current char position
    lda player_x
    lsr
    lsr
    lsr
    sta temp_col
    lda player_y
    lsr
    lsr
    lsr
    sta temp_row

    ; Check against door list for current room
    jsr get_room_doors
@check_loop:
    ldy #0
    lda (door_ptr),y    ; Door X
    cmp #$ff
    beq @no_door        ; End of list

    cmp temp_col
    bne @next_door

    iny
    lda (door_ptr),y    ; Door Y
    cmp temp_row
    bne @next_door

    ; Found matching door - transition!
    iny
    lda (door_ptr),y    ; Target room
    sta player_room

    iny
    lda (door_ptr),y    ; Entry X (char)
    asl
    asl
    asl
    sta player_x

    iny
    lda (door_ptr),y    ; Entry Y (char)
    asl
    asl
    asl
    sta player_y

    jsr load_room
    rts

@next_door:
    ; Advance to next door entry (5 bytes)
    clc
    lda door_ptr
    adc #5
    sta door_ptr
    bcc @check_loop
    inc door_ptr+1
    jmp @check_loop

@no_door:
    rts
```
**If it doesn't work:** Not transitioning? Check door coordinates match tile position. Wrong room? Verify door data table.

---

### Unit 8: Multiple Rooms
**Builds:** 4 connected rooms.
**Teaches:** Room data organisation.

---

### Unit 9: Room Loading
**Builds:** Load room from data table.
**Teaches:** Data-driven rooms.
**Code pattern:**
```asm
; Room pointer table
room_pointers_lo:
    !byte <room_00, <room_01, <room_02, <room_03
room_pointers_hi:
    !byte >room_00, >room_01, >room_02, >room_03

load_room:
    ; Get pointer to room data
    ldx player_room
    lda room_pointers_lo,x
    sta $fb
    lda room_pointers_hi,x
    sta $fc

    ; Copy room to screen
    ldy #0
@loop:
    lda ($fb),y
    sta $0400,y
    iny
    bne @loop
    inc $fc
    ldx #0
@loop2:
    lda ($fb),y
    sta $0500,x
    iny
    inx
    cpx #232            ; Remaining bytes (1000-256-256-256)
    bne @loop2

    ; Apply colours based on tile type
    jsr colour_room
    rts
```

---

### Unit 10: Treasure Items
**Builds:** Collectible treasures in rooms.
**Teaches:** Item placement.

---

### Unit 11: Item Collection
**Builds:** Walking over item collects it.
**Teaches:** Collection mechanics.
**Code pattern:**
```asm
; Item states: 0 = not collected, 1 = collected
; Stored per-room to allow persistent state
MAX_ITEMS_PER_ROOM = 8
item_states:
    !fill 16 * MAX_ITEMS_PER_ROOM, 0    ; 16 rooms × 8 items

check_item_pickup:
    ; Get character at player position
    jsr get_player_char
    cmp #CHAR_TREASURE
    bne @not_treasure
    cmp #CHAR_KEY
    bne @not_key

@not_treasure:
@not_key:
    rts

collect_item:
    ; Mark item as collected
    lda player_room
    asl
    asl
    asl                 ; ×8 for items per room
    clc
    adc current_item_index
    tax
    lda #1
    sta item_states,x

    ; Remove from screen
    jsr get_player_screen_addr
    lda #CHAR_FLOOR
    sta ($fb),y

    ; Add to inventory/score
    jsr add_to_inventory
    rts
```

---

### Unit 12: Persistent State
**Builds:** Collected items stay collected when returning.
**Teaches:** State persistence.

---

### Unit 13: Score Display
**Builds:** Score shown on screen.
**Teaches:** HUD overlay.

---

### Unit 14: Lives Display
**Builds:** Lives shown as icons.
**Teaches:** Life tracking.

---

### Unit 15: Sound - Collect
**Builds:** Sound when collecting item.
**Teaches:** SID feedback.

---

### Unit 16: Phase 1 Polish
**Builds:** Basic exploration working.

---

## Phase 2: Enemies and Combat (Units 17-32)

### Unit 17: Static Enemies
**Builds:** Monsters placed in rooms.
**Teaches:** Enemy placement.

---

### Unit 18: Enemy Sprites
**Builds:** Enemies as sprites.
**Teaches:** Multi-sprite management.
**Code pattern:**
```asm
MAX_ENEMIES = 4         ; Sprites 1-4 for enemies

enemy_x:    !fill MAX_ENEMIES, 0
enemy_y:    !fill MAX_ENEMIES, 0
enemy_type: !fill MAX_ENEMIES, 0
enemy_active: !fill MAX_ENEMIES, 0

setup_enemies:
    ; Enable sprites 1-4
    lda $d015
    ora #%00011110
    sta $d015

    ; Set sprite pointers
    lda #(enemy_sprite_1/64)
    sta $07f9
    sta $07fa
    sta $07fb
    sta $07fc

    ; Set colours
    lda #2              ; Red
    sta $d028
    sta $d029
    sta $d02a
    sta $d02b
    rts

update_enemy_sprites:
    ldx #0
@loop:
    lda enemy_active,x
    beq @skip

    ; Update sprite position
    txa
    asl                 ; ×2 for sprite register offset
    tay
    lda enemy_x,x
    sta $d002,y         ; Sprite 1+ X positions
    lda enemy_y,x
    sta $d003,y         ; Sprite 1+ Y positions

@skip:
    inx
    cpx #MAX_ENEMIES
    bne @loop
    rts
```

---

### Unit 19: Patrolling Enemies
**Builds:** Enemies walk back and forth.
**Teaches:** Simple patrol AI.
**Code pattern:**
```asm
enemy_dir:  !fill MAX_ENEMIES, 0    ; 0=up, 1=down, 2=left, 3=right
enemy_timer: !fill MAX_ENEMIES, 0

update_enemy_patrol:
    ldx #0
@loop:
    lda enemy_active,x
    beq @next

    ; Move based on direction
    lda enemy_dir,x
    cmp #0
    beq @move_up
    cmp #1
    beq @move_down
    cmp #2
    beq @move_left
    jmp @move_right

@move_up:
    dec enemy_y,x
    ; Check wall collision
    jsr check_enemy_wall
    bcc @next
    ; Hit wall - reverse
    lda #1
    sta enemy_dir,x
    jmp @next

@move_down:
    inc enemy_y,x
    jsr check_enemy_wall
    bcc @next
    lda #0
    sta enemy_dir,x
    jmp @next

@move_left:
    dec enemy_x,x
    jsr check_enemy_wall
    bcc @next
    lda #3
    sta enemy_dir,x
    jmp @next

@move_right:
    inc enemy_x,x
    jsr check_enemy_wall
    bcc @next
    lda #2
    sta enemy_dir,x

@next:
    inx
    cpx #MAX_ENEMIES
    bne @loop
    rts
```

---

### Unit 20: Chase AI
**Builds:** Enemies move toward player.
**Teaches:** Basic chase behaviour.
**Code pattern:**
```asm
update_enemy_chase:
    ldx #0
@loop:
    lda enemy_type,x
    cmp #ENEMY_CHASER
    bne @next

    ; Move toward player
    lda enemy_x,x
    cmp player_x
    beq @check_y
    bcc @move_right_chase
    ; Move left
    dec enemy_x,x
    jmp @check_y
@move_right_chase:
    inc enemy_x,x

@check_y:
    lda enemy_y,x
    cmp player_y
    beq @next
    bcc @move_down_chase
    ; Move up
    dec enemy_y,x
    jmp @next
@move_down_chase:
    inc enemy_y,x

@next:
    inx
    cpx #MAX_ENEMIES
    bne @loop
    rts
```
**If it doesn't work:** Not chasing? Check enemy type matches ENEMY_CHASER. Vibrating? Add movement delay timer.

---

### Unit 21: Player-Enemy Collision
**Builds:** Touching enemy hurts player.
**Teaches:** Sprite collision.

---

### Unit 22: Death and Respawn
**Builds:** Player dies and respawns at room entrance.
**Teaches:** Death handling.

---

### Unit 23: Enemy Animation
**Builds:** Enemies have animation frames.
**Teaches:** Sprite animation.

---

### Unit 24: Shooting Enemies
**Builds:** Some enemies fire projectiles.
**Teaches:** Enemy projectiles.

---

### Unit 25: Player Weapon
**Builds:** Fire button shoots.
**Teaches:** Player projectile.
**Code pattern:**
```asm
bullet_active: !byte 0
bullet_x:      !byte 0
bullet_y:      !byte 0
bullet_dir:    !byte 0
player_facing: !byte 3  ; Last movement direction

fire_bullet:
    lda bullet_active
    bne @done           ; Already have bullet

    ; Spawn at player position
    lda player_x
    sta bullet_x
    lda player_y
    sta bullet_y
    lda player_facing
    sta bullet_dir
    lda #1
    sta bullet_active

    ; Enable bullet sprite
    lda $d015
    ora #%00100000      ; Sprite 5
    sta $d015

    jsr sound_shoot

@done:
    rts

update_bullet:
    lda bullet_active
    beq @done

    ; Move bullet
    lda bullet_dir
    cmp #0
    beq @up
    cmp #1
    beq @down
    cmp #2
    beq @left
    ; Right
    lda bullet_x
    clc
    adc #4
    sta bullet_x
    jmp @check

@up:
    lda bullet_y
    sec
    sbc #4
    sta bullet_y
    jmp @check
; ... etc

@check:
    ; Check wall collision
    jsr check_bullet_wall
    bcs @destroy

    ; Check enemy collision
    jsr check_bullet_enemy
    bcs @hit_enemy

    ; Update sprite
    lda bullet_x
    sta $d00a           ; Sprite 5 X
    lda bullet_y
    sta $d00b           ; Sprite 5 Y
    jmp @done

@hit_enemy:
    jsr kill_enemy
@destroy:
    lda #0
    sta bullet_active
    lda $d015
    and #%11011111      ; Disable sprite 5
    sta $d015

@done:
    rts
```

---

### Unit 26: Enemy Defeat
**Builds:** Shooting enemy destroys it.
**Teaches:** Combat resolution.

---

### Unit 27: Enemy Respawn
**Builds:** Enemies return when re-entering room.
**Teaches:** Room reset logic.

---

### Unit 28: Different Enemy Types
**Builds:** Multiple enemy behaviours.
**Teaches:** Entity variety.

---

### Unit 29: Boss Enemy
**Builds:** Large enemy guarding key area.
**Teaches:** Boss design.

---

### Unit 30: Health System
**Builds:** Player has health, not instant death.
**Teaches:** Health mechanics.

---

### Unit 31: Sound - Combat
**Builds:** Sounds for shooting, hits, death.
**Teaches:** Combat audio.

---

### Unit 32: Phase 2 Polish
**Builds:** Complete combat system.

---

## Phase 3: Inventory and Keys (Units 33-48)

### Unit 33: Inventory System
**Builds:** Track collected items.
**Teaches:** Inventory data structure.
**Code pattern:**
```asm
; Inventory slots
INV_SIZE = 8
inventory:      !fill INV_SIZE, 0   ; Item type (0 = empty)
inventory_count: !byte 0

add_to_inventory:
    ; A = item type to add
    pha
    ldx inventory_count
    cpx #INV_SIZE
    bcs @full           ; Inventory full

    pla
    sta inventory,x
    inc inventory_count
    jsr update_inventory_display
    rts

@full:
    pla
    ; Play "inventory full" sound
    rts

remove_from_inventory:
    ; A = item type to remove
    ldx #0
@find:
    cmp inventory,x
    beq @found
    inx
    cpx inventory_count
    bne @find
    ; Not found
    rts

@found:
    ; Shift remaining items down
    lda #0
    sta inventory,x
@shift:
    inx
    cpx inventory_count
    bcs @done_shift
    lda inventory,x
    sta inventory-1,x
    jmp @shift
@done_shift:
    dec inventory_count
    jsr update_inventory_display
    rts
```

---

### Unit 34: Inventory Display
**Builds:** Show inventory on screen.
**Teaches:** HUD design.

---

### Unit 35: Key Items
**Builds:** Keys that unlock doors.
**Teaches:** Key mechanics.

---

### Unit 36: Locked Doors
**Builds:** Doors requiring matching key.
**Teaches:** Lock mechanics.
**Code pattern:**
```asm
; Door data includes key requirement
; Format: door_x, door_y, target_room, entry_x, entry_y, key_required
; key_required: 0=none, 1=red, 2=blue, 3=green, 4=gold

check_locked_door:
    ; Get key requirement for this door
    ldy #5
    lda (door_ptr),y
    beq @unlocked       ; No key required

    ; Check inventory for matching key
    tax                 ; Key type
    ldy #0
@check_inv:
    cpy inventory_count
    bcs @locked         ; Don't have key

    lda inventory,y
    cmp key_types,x     ; Compare to required key item type
    beq @have_key
    iny
    jmp @check_inv

@have_key:
    ; Remove key from inventory
    lda key_types,x
    jsr remove_from_inventory
    jsr sound_unlock

@unlocked:
    clc                 ; Can pass
    rts

@locked:
    jsr sound_locked
    sec                 ; Cannot pass
    rts
```

---

### Unit 37: Coloured Keys
**Builds:** Red, blue, green, gold keys.
**Teaches:** Key variety.

---

### Unit 38: Key Placement
**Builds:** Keys hidden throughout dungeon.
**Teaches:** Puzzle design.

---

### Unit 39: Health Potions
**Builds:** Collectible health restore.
**Teaches:** Consumable items.

---

### Unit 40: Weapon Upgrades
**Builds:** Better weapons to find.
**Teaches:** Equipment system.

---

### Unit 41: Treasure Value
**Builds:** Different treasures worth different points.
**Teaches:** Scoring variety.

---

### Unit 42: Secret Walls
**Builds:** Hidden passages.
**Teaches:** Secret discovery.

---

### Unit 43: Switches and Triggers
**Builds:** Step on switch to open door.
**Teaches:** Trigger mechanics.

---

### Unit 44: Traps
**Builds:** Floor traps that hurt player.
**Teaches:** Hazard variety.

---

### Unit 45: Map Item
**Builds:** Find map to reveal dungeon layout.
**Teaches:** Map unlock.

---

### Unit 46: Compass Item
**Builds:** Shows direction to exit.
**Teaches:** Navigation aids.

---

### Unit 47: Sound - Items
**Builds:** Sounds for keys, potions, treasures.
**Teaches:** Item audio.

---

### Unit 48: Phase 3 Polish
**Builds:** Complete inventory system.

---

## Phase 4: World Design (Units 49-64)

### Unit 49: Dungeon Layout
**Builds:** 16-room dungeon map.
**Teaches:** Level design.

---

### Unit 50: Room Variety
**Builds:** Different room shapes and sizes.
**Teaches:** Visual variety.

---

### Unit 51: Themed Areas
**Builds:** Crypt, caves, temple sections.
**Teaches:** Thematic zones.

---

### Unit 52: Difficulty Progression
**Builds:** Harder enemies deeper in dungeon.
**Teaches:** Difficulty curve.

---

### Unit 53: Critical Path
**Builds:** Required route through dungeon.
**Teaches:** Level flow.

---

### Unit 54: Optional Areas
**Builds:** Bonus rooms with extra treasure.
**Teaches:** Exploration rewards.

---

### Unit 55: Boss Room
**Builds:** Final challenge room.
**Teaches:** Climax design.

---

### Unit 56: Exit and Victory
**Builds:** Reaching exit wins game.
**Teaches:** Win condition.

---

### Unit 57: Multiple Floors
**Builds:** Stairs between dungeon levels.
**Teaches:** Multi-level design.

---

### Unit 58: Floor 2 Design
**Builds:** Second floor layout.
**Teaches:** Expanded world.

---

### Unit 59: Floor 3 Design
**Builds:** Third floor (hardest).
**Teaches:** Expert design.

---

### Unit 60: Warp Points
**Builds:** Shortcuts between floors.
**Teaches:** Fast travel.

---

### Unit 61: Save Points
**Builds:** Checkpoints restore progress.
**Teaches:** Progress saving.

---

### Unit 62: Room Colour Themes
**Builds:** Different colours per zone.
**Teaches:** Visual theming.

---

### Unit 63: Special Rooms
**Builds:** Treasure vaults, boss lairs.
**Teaches:** Unique spaces.

---

### Unit 64: Phase 4 Polish
**Builds:** Complete dungeon world.

---

## Phase 5: Audio (Units 65-80)

### Unit 65: Sound System
**Builds:** SID sound manager.
**Teaches:** Audio architecture.

---

### Unit 66: Footstep Sounds
**Builds:** Walking creates steps.
**Teaches:** Movement audio.

---

### Unit 67: Door Sounds
**Builds:** Open, locked, unlock sounds.
**Teaches:** Interaction audio.

---

### Unit 68: Combat Sounds
**Builds:** Attack, hit, death sounds.
**Teaches:** Action audio.

---

### Unit 69: Item Sounds
**Builds:** Pickup, use sounds.
**Teaches:** Feedback audio.

---

### Unit 70: Ambient Sounds
**Builds:** Dungeon atmosphere.
**Teaches:** Environmental audio.

---

### Unit 71: Music - Title
**Builds:** Title screen music.
**Teaches:** SID composition.

---

### Unit 72: Music - Dungeon
**Builds:** In-game music.
**Teaches:** Game music.

---

### Unit 73: Music - Boss
**Builds:** Tense boss music.
**Teaches:** Boss atmosphere.

---

### Unit 74: Music - Victory
**Builds:** Completion fanfare.
**Teaches:** Victory audio.

---

### Unit 75: Music - Death
**Builds:** Game over music.
**Teaches:** Failure audio.

---

### Unit 76: Zone Music
**Builds:** Different music per area.
**Teaches:** Musical variety.

---

### Unit 77: Sound Priority
**Builds:** Important sounds don't get cut.
**Teaches:** Audio management.

---

### Unit 78: Volume Balance
**Builds:** Music vs SFX levels.
**Teaches:** Audio mixing.

---

### Unit 79: Audio Polish
**Builds:** Final audio tweaks.
**Teaches:** Audio refinement.

---

### Unit 80: Phase 5 Polish
**Builds:** Complete audio.

---

## Phase 6: Presentation (Units 81-96)

### Unit 81: Title Screen
**Builds:** Attractive start screen.
**Teaches:** Title design.

---

### Unit 82: Story Intro
**Builds:** Brief backstory.
**Teaches:** Narrative context.

---

### Unit 83: Instructions
**Builds:** How to play.
**Teaches:** Onboarding.

---

### Unit 84: High Scores
**Builds:** Top scores display.
**Teaches:** Score persistence.

---

### Unit 85: Name Entry
**Builds:** Enter initials.
**Teaches:** Text input.

---

### Unit 86: Map Screen
**Builds:** Show dungeon layout.
**Teaches:** Map display.

---

### Unit 87: Pause Menu
**Builds:** In-game pause.
**Teaches:** Pause implementation.

---

### Unit 88: Game Over
**Builds:** Death screen.
**Teaches:** Failure handling.

---

### Unit 89: Victory Screen
**Builds:** Completion celebration.
**Teaches:** Success presentation.

---

### Unit 90: Credits
**Builds:** Attribution screen.
**Teaches:** Credits design.

---

### Unit 91: Difficulty Select
**Builds:** Easy/Normal/Hard modes.
**Teaches:** Difficulty options.

---

### Unit 92: Border Effects
**Builds:** Raster colour effects.
**Teaches:** Visual polish.

---

### Unit 93: Screen Transitions
**Builds:** Fade effects between rooms.
**Teaches:** Transitions.

---

### Unit 94: Character Animation
**Builds:** Enhanced player animation.
**Teaches:** Animation polish.

---

### Unit 95: Easter Eggs
**Builds:** Hidden features.
**Teaches:** Secrets.

---

### Unit 96: Phase 6 Polish
**Builds:** Complete presentation.

---

## Phase 7: Optimisation (Units 97-112)

### Unit 97: Frame Rate
**Builds:** Solid 50/60fps.
**Teaches:** Performance.

---

### Unit 98: Collision Optimisation
**Builds:** Faster collision checks.
**Teaches:** Algorithm efficiency.

---

### Unit 99: Room Loading Speed
**Builds:** Fast room transitions.
**Teaches:** Load optimisation.

---

### Unit 100: Memory Layout
**Builds:** Efficient data organisation.
**Teaches:** Memory planning.

---

### Unit 101-104: Balance
**Builds:** Fair difficulty, good pacing.
**Teaches:** Game balance.

---

### Unit 105-108: Bug Fixes
**Builds:** Find and fix issues.
**Teaches:** Debugging.

---

### Unit 109-111: Polish
**Builds:** Final refinements.
**Teaches:** Quality polish.

---

### Unit 112: Phase 7 Complete
**Builds:** Stable game.

---

## Phase 8: Release (Units 113-128)

### Unit 113-116: Disk Creation
**Builds:** D64 image.
**Teaches:** Distribution format.

---

### Unit 117-120: Testing
**Builds:** Emulator and hardware testing.
**Teaches:** Quality assurance.

---

### Unit 121-124: Final Polish
**Builds:** Last adjustments.
**Teaches:** Release preparation.

---

### Unit 125-127: Documentation
**Builds:** Instructions and credits.
**Teaches:** Documentation.

---

### Unit 128: Release
**Builds:** Final release.
**Teaches:** Shipping a game.

---

## Version History

- **1.0 (2026-01-18):** Initial 128-unit outline created, replacing Invader Wave.
