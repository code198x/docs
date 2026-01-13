;──────────────────────────────────────────────────────────────
; NAMETABLE ADDRESS CALCULATION
;──────────────────────────────────────────────────────────────
; The nametable is 32 tiles wide. To calculate an address:
;
;   Address = $2000 + (row × 32) + column
;
; Examples:
;   Position (0,0):   $2000 + 0 + 0 = $2000
;   Position (5,0):   $2000 + 0 + 5 = $2005
;   Position (0,1):   $2000 + 32 + 0 = $2020
;   Position (15,10): $2000 + 320 + 15 = $2000 + $140 + $F = $214F
;
; In practice, sequential writes with auto-increment handle
; most cases. You only need to calculate addresses when jumping
; to specific positions.

; To write a single tile at row 10, column 15:
    bit PPUSTATUS
    lda #$21                ; High byte of $214F
    sta PPUADDR
    lda #$4F                ; Low byte of $214F
    sta PPUADDR
    lda #7                  ; Some tile index
    sta PPUDATA
