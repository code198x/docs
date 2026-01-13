;──────────────────────────────────────────────────────────────
; CLEARING RAM
;──────────────────────────────────────────────────────────────
; Between the two VBlank waits, we clear all RAM to zero.
; This ensures the game starts with a clean state.

    ; Clear RAM while waiting for second VBlank
    ; This ensures we start with a clean state
    lda #$00
@clear_ram:
    sta $0000, x            ; Zero page ($0000-$00FF)
    sta $0100, x            ; Stack area ($0100-$01FF)
    sta $0200, x            ; OAM buffer ($0200-$02FF)
    sta $0300, x            ; General RAM
    sta $0400, x
    sta $0500, x
    sta $0600, x
    sta $0700, x            ; Last page of RAM
    inx                     ; X goes 0→255
    bne @clear_ram          ; Loop until X wraps to 0
