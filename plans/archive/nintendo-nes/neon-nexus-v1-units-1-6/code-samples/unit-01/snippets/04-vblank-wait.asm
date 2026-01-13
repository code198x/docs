;──────────────────────────────────────────────────────────────
; WAITING FOR VBLANK
;──────────────────────────────────────────────────────────────
; The PPU needs time to warm up. We wait for two VBlank
; periods before the PPU is ready to use.

    ; Wait for first VBlank
    ; The PPU needs time to warm up after power-on
@vblank_wait_1:
    bit PPUSTATUS           ; Read PPU status
    bpl @vblank_wait_1      ; Loop until bit 7 (VBlank) is set

    ; ... (clear RAM here - see next snippet) ...

    ; Wait for second VBlank
    ; After this, the PPU is fully ready
@vblank_wait_2:
    bit PPUSTATUS
    bpl @vblank_wait_2
