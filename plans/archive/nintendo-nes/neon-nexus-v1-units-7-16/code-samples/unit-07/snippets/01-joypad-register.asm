;──────────────────────────────────────────────────────────────
; JOYPAD REGISTER
;──────────────────────────────────────────────────────────────
; The NES controllers connect via $4016 (player 1) and $4017 (player 2).
;
; Reading buttons is a two-step process:
;   1. Write 1 then 0 to $4016 (strobe) to latch the button state
;   2. Read $4016 eight times — each read returns one button
;
; The buttons come out in this order:
;   A, B, Select, Start, Up, Down, Left, Right

JOYPAD1 = $4016

; Button bit positions (after reading into a single byte)
BTN_A      = %00000001
BTN_B      = %00000010
BTN_SELECT = %00000100
BTN_START  = %00001000
BTN_UP     = %00010000
BTN_DOWN   = %00100000
BTN_LEFT   = %01000000
BTN_RIGHT  = %10000000
