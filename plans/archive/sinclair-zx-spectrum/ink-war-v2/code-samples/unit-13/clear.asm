; Unit 13: Clear Screen Routine
; Building a reusable clear screen subroutine
;
; Every game needs to clear the screen. Let's build a proper routine.

    org 32768

start:
    ; Set border to blue
    ld a, 1
    out ($fe), a

    ; ========================================
    ; First: Show a messy screen to clear
    ; ========================================

    ; Fill screen with a pattern
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), %10101010       ; Checkerboard pattern
    ldir

    ; Set random-looking coloured attributes
    ld hl, $5800
    ld b, 0                  ; 256 iterations (first part)
colour_loop1:
    ld a, b
    and %00000111            ; Keep low 3 bits for ink
    or %01000000             ; Add BRIGHT
    ld c, a
    ld a, b
    rrca
    rrca
    rrca
    and %00111000            ; Paper from rotated value
    or c                     ; Combine
    ld (hl), a
    inc hl
    djnz colour_loop1

    ; Continue for remaining 512 bytes
    ld b, 0
colour_loop2:
    ld a, b
    xor l                    ; Mix with position
    and %01111111
    ld (hl), a
    inc hl
    djnz colour_loop2

    ld b, 0
colour_loop3:
    ld a, b
    xor h
    and %01111111
    ld (hl), a
    inc hl
    djnz colour_loop3

    ; Wait to show the mess
    ld b, 100
delay1:
    halt
    djnz delay1

    ; ========================================
    ; Now clear it properly
    ; ========================================

    call clear_screen
    call clear_attributes

    ; Draw a simple yellow bar to prove clear worked
    ; Use attributes only (ink colour on cleared pixels)
    ld hl, $5800 + (11 * 32) + 10   ; Row 11, col 10
    ld b, 12
    ld a, %01110000          ; Bright white paper (shows as white block)

draw_bar:
    ld (hl), a
    inc hl
    djnz draw_bar

    ; Second bar below
    ld hl, $5800 + (12 * 32) + 10
    ld b, 12
    ld a, %01000110          ; Bright yellow paper

draw_bar2:
    ld (hl), a
    inc hl
    djnz draw_bar2

    ; Hold on final state
hold:
    jr hold

; ============================================
; Subroutine: Clear screen memory
; Fills $4000-$57FF with zeros (all pixels off)
; ============================================
clear_screen:
    push af
    push bc
    push de
    push hl

    ld hl, $4000            ; Start of screen memory
    ld (hl), 0              ; Set first byte to zero
    ld de, $4001            ; Destination = start + 1
    ld bc, 6143             ; 6144 - 1 bytes to copy
    ldir                    ; Copy (HL) to (DE), repeat BC times

    pop hl
    pop de
    pop bc
    pop af
    ret

; ============================================
; Subroutine: Clear attributes
; Sets all attributes to white ink on black paper
; ============================================
clear_attributes:
    push af
    push bc
    push de
    push hl

    ld hl, $5800            ; Start of attributes
    ld (hl), %00111000      ; White paper, black ink
    ld de, $5801
    ld bc, 767              ; 768 - 1 bytes
    ldir

    pop hl
    pop de
    pop bc
    pop af
    ret

; ============================================
; Subroutine: Clear all (screen + attributes)
; Convenience routine combining both
; ============================================
clear_all:
    call clear_screen
    call clear_attributes
    ret

    end start
