;──────────────────────────────────────────────────────────────
; PPU VRAM ACCESS
;──────────────────────────────────────────────────────────────
; The PPU has its own 16KB address space, separate from the CPU.
; Access it through PPUADDR ($2006) and PPUDATA ($2007).
;
; Writing to PPU memory:
;   1. Read PPUSTATUS to reset the address latch
;   2. Write high byte of address to PPUADDR
;   3. Write low byte of address to PPUADDR
;   4. Write data to PPUDATA (address auto-increments)
;
; IMPORTANT: Only write during VBlank! Writing while the PPU
; is rendering causes glitches and corruption.

; Example: Write palettes to $3F00
load_palette:
    bit PPUSTATUS           ; Reset address latch
    lda #$3F                ; High byte of $3F00
    sta PPUADDR
    lda #$00                ; Low byte of $3F00
    sta PPUADDR

    ; Now write 32 bytes of palette data
    ldx #0
@loop:
    lda palette_data, x     ; Load palette byte
    sta PPUDATA             ; Write to PPU (address auto-increments)
    inx
    cpx #32
    bne @loop
    rts
