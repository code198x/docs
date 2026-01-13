;──────────────────────────────────────────────────────────────
; NAMETABLE ADDRESS
;──────────────────────────────────────────────────────────────
; The nametable is a 32×30 grid of tile indices at $2000.
; To write to it, we set the PPU address and write tile indices.

    bit PPUSTATUS           ; Reset PPU address latch

    ; Set PPU address to nametable 0 ($2000)
    lda #$20
    sta PPUADDR             ; High byte first
    lda #$00
    sta PPUADDR             ; Then low byte

    ; Now any write to PPUDATA goes to the nametable
    lda #5                  ; Tile index 5
    sta PPUDATA             ; Write to position (0,0)

; After each PPUDATA write, the address auto-increments.
; With PPUCTRL bit 2 = 0, it increments by 1 (horizontal).
; With PPUCTRL bit 2 = 1, it increments by 32 (vertical).
