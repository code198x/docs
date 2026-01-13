;──────────────────────────────────────────────────────────────
; MAIN LOOP
;──────────────────────────────────────────────────────────────
; The main loop waits for VBlank (signalled by NMI), then runs
; game logic. This ensures we update the game 60 times per
; second (NTSC) in perfect sync with the display.

main_loop:
    ; Wait for NMI to set the ready flag
    lda #$00
    sta nmi_ready           ; Clear the flag

@wait_for_nmi:
    lda nmi_ready           ; Check flag
    beq @wait_for_nmi       ; Loop until NMI sets it

    ; NMI has fired - we're now in VBlank
    ; This is where we would:
    ; 1. Update PPU (palettes, nametable, etc.)
    ; 2. Transfer sprite data via DMA
    ; 3. Set scroll position
    ;
    ; After VBlank ends, we run game logic:
    ; - Read controller input
    ; - Update game state
    ; - Prepare data for next frame

    jmp main_loop
