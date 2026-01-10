; Unit 16: Display Test
; Phase 1 finale - bringing everything together
;
; A complete display demonstration showing the game board ready for play

    org 32768

; Board constants
BOARD_TOP    equ 8
BOARD_LEFT   equ 12
BOARD_SIZE   equ 8

; Colours
PLAYER1_ATTR equ %01010000   ; Bright red paper
PLAYER2_ATTR equ %01001000   ; Bright blue paper
EMPTY_ATTR   equ %00111000   ; White paper
BORDER_ATTR  equ %01000000   ; Bright black

; Score display positions
SCORE1_ROW   equ 2
SCORE1_COL   equ 4
SCORE2_ROW   equ 2
SCORE2_COL   equ 24

start:
    ; Initialise display
    call clear_screen
    call clear_attributes

    ld a, 0
    out ($fe), a             ; Black border

    ; Draw title area - red bar for Player 1
    ld hl, $5800 + (SCORE1_ROW * 32) + SCORE1_COL
    ld b, 6
    ld a, PLAYER1_ATTR
title1_loop:
    ld (hl), a
    inc hl
    djnz title1_loop

    ; Blue bar for Player 2
    ld hl, $5800 + (SCORE2_ROW * 32) + SCORE2_COL
    ld b, 6
    ld a, PLAYER2_ATTR
title2_loop:
    ld (hl), a
    inc hl
    djnz title2_loop

    ; Draw the game board
    call draw_board

    ; Animate filling the board to show it working
    call animate_game

    ; Hold final display
hold:
    jr hold

; ============================================
; Animate a sample game being played
; ============================================
animate_game:
    push af
    push bc
    push de
    push hl

    ; Starting positions array
    ; Format: row, column, player (1 or 2)
    ld ix, moves
    ld b, 20                 ; Number of moves

animate_loop:
    push bc

    ; Get move data
    ld a, (ix+0)             ; Row (0-7)
    ld d, a
    ld a, (ix+1)             ; Column (0-7)
    ld e, a
    ld a, (ix+2)             ; Player

    ; Calculate attribute address
    push af                  ; Save player

    ; Calculate: $5800 + ((BOARD_TOP + row) * 32) + (BOARD_LEFT + col)
    ld a, d
    add a, BOARD_TOP         ; Absolute row (8-15)
    ld l, a
    ld h, 0
    ; HL = row, now multiply by 32
    add hl, hl               ; HL * 2
    add hl, hl               ; HL * 4
    add hl, hl               ; HL * 8
    add hl, hl               ; HL * 16
    add hl, hl               ; HL * 32

    ; Add column
    ld a, e
    add a, BOARD_LEFT
    add a, l
    ld l, a

    ; Add base address
    ld bc, $5800
    add hl, bc               ; HL = attribute address

    ; Set colour based on player
    pop af
    cp 1
    jr nz, player2_colour
    ld a, PLAYER1_ATTR
    jr set_colour
player2_colour:
    ld a, PLAYER2_ATTR
set_colour:
    ld (hl), a

    ; Advance to next move
    inc ix
    inc ix
    inc ix

    ; Delay between moves
    push bc
    ld b, 8
delay:
    halt
    djnz delay
    pop bc

    pop bc
    djnz animate_loop

    pop hl
    pop de
    pop bc
    pop af
    ret

; Move data: row, column, player
moves:
    defb 0, 0, 1             ; Player 1 top-left
    defb 7, 7, 2             ; Player 2 bottom-right
    defb 0, 1, 1
    defb 7, 6, 2
    defb 1, 0, 1
    defb 6, 7, 2
    defb 1, 1, 1
    defb 6, 6, 2
    defb 2, 0, 1
    defb 5, 7, 2
    defb 2, 1, 1
    defb 5, 6, 2
    defb 3, 3, 1
    defb 4, 4, 2
    defb 3, 4, 1
    defb 4, 3, 2
    defb 0, 7, 1
    defb 7, 0, 2
    defb 2, 5, 1
    defb 5, 2, 2

; ============================================
; Draw the game board
; ============================================
draw_board:
    push af
    push bc
    push de
    push hl

    ; Draw border
    ld hl, $5800 + ((BOARD_TOP - 1) * 32) + (BOARD_LEFT - 1)
    ld b, 10
    ld a, BORDER_ATTR
border_top:
    ld (hl), a
    inc hl
    djnz border_top

    ld hl, $5800 + ((BOARD_TOP + BOARD_SIZE) * 32) + (BOARD_LEFT - 1)
    ld b, 10
    ld a, BORDER_ATTR
border_bottom:
    ld (hl), a
    inc hl
    djnz border_bottom

    ld hl, $5800 + (BOARD_TOP * 32) + (BOARD_LEFT - 1)
    ld d, BOARD_SIZE
border_sides:
    ld (hl), BORDER_ATTR
    ld bc, 9
    add hl, bc
    ld (hl), BORDER_ATTR
    ld bc, 23
    add hl, bc
    dec d
    jr nz, border_sides

    ; Draw empty board
    ld hl, $5800 + (BOARD_TOP * 32) + BOARD_LEFT
    ld d, BOARD_SIZE

board_rows:
    push hl
    ld e, BOARD_SIZE

board_cols:
    ld (hl), EMPTY_ATTR
    inc hl
    dec e
    jr nz, board_cols

    pop hl
    ld bc, 32
    add hl, bc
    dec d
    jr nz, board_rows

    pop hl
    pop de
    pop bc
    pop af
    ret

; ============================================
; Clear screen
; ============================================
clear_screen:
    push af
    push bc
    push de
    push hl

    ld hl, $4000
    ld (hl), 0
    ld de, $4001
    ld bc, 6143
    ldir

    pop hl
    pop de
    pop bc
    pop af
    ret

; ============================================
; Clear attributes
; ============================================
clear_attributes:
    push af
    push bc
    push de
    push hl

    ld hl, $5800
    ld (hl), %00000000
    ld de, $5801
    ld bc, 767
    ldir

    pop hl
    pop de
    pop bc
    pop af
    ret

    end start
