; Unit 10: Load and Store
; Demonstrates the LD instruction in all its forms
;
; LD moves data between registers, memory, and immediate values
; It's the most common Z80 instruction

    org 32768

start:
    call clear_screen
    call fill_screen

    ld a, 0
    out ($fe), a        ; Black border

    ; ========================================
    ; LD register, immediate value
    ; ========================================
    ld a, 7             ; A = 7
    ld b, 24            ; B = 24 (row count)
    ld c, 32            ; C = 32 (column count)
    ld d, 0             ; D = 0
    ld e, 0             ; E = 0

    ; ========================================
    ; LD register pair, immediate value
    ; ========================================
    ld hl, $5800        ; HL = attribute start
    ld de, $5801        ; DE = attribute start + 1
    ld bc, 767          ; BC = count

    ; ========================================
    ; LD register, register
    ; ========================================
    ld a, b             ; A = B (copy B to A)
    ld d, e             ; D = E
    ld h, l             ; H = L (makes HL point to $0000!)

    ; Reset HL for our demo
    ld hl, $5800

    ; ========================================
    ; LD (memory), register - Store to memory
    ; ========================================
    ld a, %00000010     ; Red attribute
    ld (hl), a          ; Store A at address HL
    inc hl              ; Move pointer

    ld a, %00000100     ; Green attribute
    ld (hl), a          ; Store A at address HL
    inc hl

    ld a, %00000001     ; Blue attribute
    ld (hl), a
    inc hl

    ; ========================================
    ; LD register, (memory) - Load from memory
    ; ========================================
    ld hl, $5800        ; Point to first attribute
    ld a, (hl)          ; A = value at $5800 (red)
    ; A now contains %00000010

    ; ========================================
    ; LD (address), A - Store A at fixed address
    ; ========================================
    ld a, %00000110     ; Yellow
    ld ($5803), a       ; Store at specific address
    ld ($5804), a       ; And another
    ld ($5805), a       ; And another

    ; ========================================
    ; LD A, (address) - Load A from fixed address
    ; ========================================
    ld a, ($5800)       ; Load from fixed address
    ; A now contains the red attribute again

    ; ========================================
    ; LD (HL), immediate - Store value at HL
    ; ========================================
    ld hl, $5806
    ld (hl), %00000101  ; Store cyan directly

    ; ========================================
    ; LDIR - Block copy (special LD)
    ; ========================================
    ; Copy a pattern across the screen

    ld hl, $5800        ; Source
    ld de, $5820        ; Destination (row 1)
    ld bc, 32           ; Copy 32 bytes (one row)
    ldir                ; Copy BC bytes from HL to DE

    ; Create gradient effect using multiple LDs
    ld hl, $5840        ; Row 2
    ld b, 32            ; 32 columns
    ld c, 0             ; Colour counter

gradient:
    ld a, c             ; A = column (0-31)
    and %00000111       ; Keep low 3 bits (0-7)
    or %01000000        ; Add BRIGHT
    ld (hl), a          ; Store attribute
    inc hl
    inc c
    djnz gradient

    ; Wait for key
wait_key:
    xor a
    in a, ($fe)
    cpl
    and $1f
    jr z, wait_key
    ret

clear_screen:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), 0
    ldir
    ret

fill_screen:
    ld hl, $4000
    ld de, $4001
    ld bc, 6143
    ld (hl), $ff
    ldir
    ret

    end start
