;──────────────────────────────────────────────────────────────
; CHECKING A SINGLE BUTTON
;──────────────────────────────────────────────────────────────
; Use AND with a bit mask to test if a specific button is pressed.

    ; Check if Up is pressed
    lda buttons
    and #BTN_UP             ; Isolate the Up bit
    beq @not_pressed        ; Branch if zero (not pressed)

    ; Up is pressed — do something
    dec player_y            ; Move player up

@not_pressed:
    ; Continue with other checks...

; The AND instruction sets the zero flag if the result is zero.
; BEQ (branch if equal) branches when the zero flag is set.
