; Unit 15: Colour the Board
; Adding player colours to show territory control
;
; Red vs Blue - the classic rivalry

    org 32768

; Board constants
BOARD_TOP    equ 8
BOARD_LEFT   equ 12
BOARD_SIZE   equ 8

; Player colours (BRIGHT + PAPER colour)
PLAYER1_ATTR equ %01010000   ; Bright red paper
PLAYER2_ATTR equ %01001000   ; Bright blue paper
EMPTY_ATTR   equ %00111000   ; White paper (unclaimed)
BORDER_ATTR  equ %01000000   ; Bright black

start:
    call clear_screen
    call clear_attributes

    ld a, 0
    out ($fe), a             ; Black border

    ; Draw the initial board
    call draw_board

    ; Demonstrate player colours by filling some cells
    ; This simulates a game in progress

    ; Player 1 (Red) claims some cells
    ld hl, $5800 + (BOARD_TOP * 32) + BOARD_LEFT
    ld (hl), PLAYER1_ATTR    ; Top-left corner

    ld hl, $5800 + (BOARD_TOP * 32) + BOARD_LEFT + 1
    ld (hl), PLAYER1_ATTR

    ld hl, $5800 + ((BOARD_TOP + 1) * 32) + BOARD_LEFT
    ld (hl), PLAYER1_ATTR

    ld hl, $5800 + ((BOARD_TOP + 1) * 32) + BOARD_LEFT + 1
    ld (hl), PLAYER1_ATTR

    ld hl, $5800 + ((BOARD_TOP + 2) * 32) + BOARD_LEFT
    ld (hl), PLAYER1_ATTR

    ; Player 2 (Blue) claims some cells
    ld hl, $5800 + ((BOARD_TOP + BOARD_SIZE - 1) * 32) + BOARD_LEFT + BOARD_SIZE - 1
    ld (hl), PLAYER2_ATTR    ; Bottom-right corner

    ld hl, $5800 + ((BOARD_TOP + BOARD_SIZE - 1) * 32) + BOARD_LEFT + BOARD_SIZE - 2
    ld (hl), PLAYER2_ATTR

    ld hl, $5800 + ((BOARD_TOP + BOARD_SIZE - 2) * 32) + BOARD_LEFT + BOARD_SIZE - 1
    ld (hl), PLAYER2_ATTR

    ld hl, $5800 + ((BOARD_TOP + BOARD_SIZE - 2) * 32) + BOARD_LEFT + BOARD_SIZE - 2
    ld (hl), PLAYER2_ATTR

    ld hl, $5800 + ((BOARD_TOP + BOARD_SIZE - 3) * 32) + BOARD_LEFT + BOARD_SIZE - 1
    ld (hl), PLAYER2_ATTR

    ; Add some more scattered pieces
    ld hl, $5800 + ((BOARD_TOP + 3) * 32) + BOARD_LEFT + 3
    ld (hl), PLAYER1_ATTR

    ld hl, $5800 + ((BOARD_TOP + 4) * 32) + BOARD_LEFT + 4
    ld (hl), PLAYER2_ATTR

    ld hl, $5800 + ((BOARD_TOP + 2) * 32) + BOARD_LEFT + 5
    ld (hl), PLAYER1_ATTR

    ld hl, $5800 + ((BOARD_TOP + 5) * 32) + BOARD_LEFT + 2
    ld (hl), PLAYER2_ATTR

    ; Hold display
hold:
    jr hold

; ============================================
; Draw the game board (8×8 grid)
; ============================================
draw_board:
    push af
    push bc
    push de
    push hl

    ; Draw border frame
    ld hl, $5800 + ((BOARD_TOP - 1) * 32) + (BOARD_LEFT - 1)
    ld b, 10
    ld a, BORDER_ATTR
draw_top_border:
    ld (hl), a
    inc hl
    djnz draw_top_border

    ld hl, $5800 + ((BOARD_TOP + BOARD_SIZE) * 32) + (BOARD_LEFT - 1)
    ld b, 10
    ld a, BORDER_ATTR
draw_bottom_border:
    ld (hl), a
    inc hl
    djnz draw_bottom_border

    ld hl, $5800 + (BOARD_TOP * 32) + (BOARD_LEFT - 1)
    ld d, BOARD_SIZE
draw_side_borders:
    ld (hl), BORDER_ATTR
    ld bc, 9
    add hl, bc
    ld (hl), BORDER_ATTR
    ld bc, 23
    add hl, bc
    dec d
    jr nz, draw_side_borders

    ; Draw empty board cells
    ld hl, $5800 + (BOARD_TOP * 32) + BOARD_LEFT
    ld d, BOARD_SIZE

draw_board_rows:
    push hl
    ld e, BOARD_SIZE

draw_board_cols:
    ld (hl), EMPTY_ATTR
    inc hl
    dec e
    jr nz, draw_board_cols

    pop hl
    ld bc, 32
    add hl, bc
    dec d
    jr nz, draw_board_rows

    pop hl
    pop de
    pop bc
    pop af
    ret

; ============================================
; Clear screen memory
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
