;──────────────────────────────────────────────────────────────
; TRIGGERING SOUNDS IN GAME EVENTS
;──────────────────────────────────────────────────────────────
; Call the sound routines when game events happen.

; In collect_item:
.proc collect_item
    ; ... score update code ...

    jsr play_collect_sound  ; Play collect sound!

    ; ... respawn item code ...
    rts
.endproc

; In lose_life:
.proc lose_life
    dec lives
    lda #1
    sta lives_dirty

    jsr play_hit_sound      ; Play hit sound!

    ; ... rest of lose_life code ...
    rts
.endproc

; Simple pattern: call the appropriate sound routine
; when the event happens. The update_sound routine
; handles the rest automatically each frame.
