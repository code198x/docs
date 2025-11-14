# Lesson 003: Keyboard Triggers ⚡ PLAYABLE

**Arc:** First Sound
**Position:** Lesson 3 of 3 in arc
**Type:** Playable Milestone
**Estimated Completion:** 70-80 lines of assembly

## Learning Objectives

- Read keyboard matrix via CIA #1
- Map keyboard keys to musical notes
- Implement real-time keyboard scanning
- Create interactive sound control
- Build first playable Phase 1 program

## Prerequisites

**From Previous Lessons:**
- L1: SID initialization
- L2: Frequency tables and note playback

**Assembly Knowledge:**
- Data tables
- Conditional branching
- Bit manipulation

## Key Concepts Introduced

### CIA #1 Keyboard Matrix
Keyboard is 8x8 matrix scanned via CIA #1 ports. Write to $DC00 (column select), read from $DC01 (row data).

### Real-Time Input Loop
Main loop continuously scans keyboard, triggers notes immediately when keys pressed.

### Key-to-Note Mapping
Map convenient keys (A/S/D/F/G/H/J/K) to musical scale (C/D/E/F/G/A/B/C).

### Non-Blocking Input
Unlike BASIC GET, assembly can check keyboard without waiting - essential for real-time gameplay.

## Code Pattern

```asm
        * = $0801
        .byte $0c,$08,$0a,$00,$9e,$20,$32,$30,$36,$34,$00,$00,$00

        * = $0810

; Frequency table for C-major scale (C4-C5) - A440 PAL tuning
freq_lo: !byte $67, $89, $ed, $3b, $13, $45, $da, $ce
freq_hi: !byte $11, $13, $15, $17, $1a, $1d, $20, $22
; C4=$1167, D4=$1389, E4=$15ED, F4=$173B, G4=$1A13, A4=$1D45, B4=$20DA, C5=$22CE

; Keyboard scan codes for A/S/D/F/G/H/J/K
; (Simplified - actual scan codes)
key_row: !byte $01, $01, $01, $02, $02, $02, $03, $03
key_col: !byte $02, $05, $07, $02, $05, $07, $02, $05
num_keys = 8

init:   jsr clear_sid
        jsr setup_cia

main:   ldx #$00        ; Key index

scan:   ; Select column for this key
        lda key_col,x
        sta $dc00

        ; Read row
        lda $dc01
        and key_row,x
        bne next_key    ; Key not pressed

        ; Key pressed - play note!
        jsr play_note

next_key:
        inx
        cpx #num_keys
        bne scan
        jmp main        ; Loop forever

play_note:
        ; X register = key index
        lda freq_lo,x
        sta $d400
        lda freq_hi,x
        sta $d401
        lda #$11        ; Triangle + gate on
        sta $d404
        rts

clear_sid:
        lda #$00
        ldx #$00
cls:    sta $d400,x
        inx
        cpx #$1d
        bne cls
        lda #$09        ; Quick attack
        sta $d405
        lda #$00        ; Fast release
        sta $d406
        lda #$0f
        sta $d418
        rts

setup_cia:
        lda #$ff        ; All columns output
        sta $dc02
        lda #$00        ; All rows input
        sta $dc03
        rts
```

## Hardware Interaction

**Chips Involved:**
- **SID** - Sound output
- **CIA #1** - Keyboard scanning at $DC00-$DC0F

**CIA #1 Keyboard Registers:**
- `$DC00` - Data Port A (column select, write)
- `$DC01` - Data Port B (row read, read)
- `$DC02` - Data Direction A (set to $FF for output)
- `$DC03` - Data Direction B (set to $00 for input)

**Keyboard Matrix (simplified):**
```
        Col 0  Col 1  Col 2  ...
Row 0:  DEL    RETURN CRSR→
Row 1:  3      W      A      ...
Row 2:  5      R      D      F
Row 3:  7      Y      G      H
...
```

**Key Scan Pattern:**
```
1. Write column bit to $DC00 (e.g., %11111101 for column 1)
2. Read row bits from $DC01
3. Check if specific row bit is clear (0 = pressed)
4. Repeat for each column
```

**PAL vs NTSC:**
These frequency values are for **PAL systems** (985,248 Hz clock). NTSC systems use a 1,022,727 Hz clock (~3.8% faster), requiring different values for the same pitch. For NTSC frequency tables, see the [SID Chip reference in the Vault](/vault/sid-chip) or multiply PAL values by 1.038.

## Common Pitfalls

1. **Wrong CIA data direction:** Must set $DC02/$DC03 for input/output
2. **Inverted logic:** Bit=0 means pressed, bit=1 means not pressed
3. **Multiple keys:** Scan all keys every frame to support multiple presses
4. **ADSR too slow:** Use fast attack/release for responsive feel
5. **No note-off:** Previous note keeps playing, causing conflicts

## Extension Ideas

- Add second octave (shift key modifier)
- Record and playback note sequence
- Display which note is playing on screen
- Add velocity (time between scans affects volume)
- Multiple voices (chord mode)

## Builds Toward

**In This Tier:**
- L4: Pre-recorded melodies (next arc)
- L5: Timing and rhythm system
- L6-7: Rhythm matching game

**In Next Tier:**
- Joystick control replaces keyboard
- Graphics + sound coordination

## Quick Reference

**CIA #1 Setup:**
```asm
setup_keyboard:
        lda #$ff        ; Port A = output (columns)
        sta $dc02
        lda #$00        ; Port B = input (rows)
        sta $dc03
        rts
```

**Scan Single Key:**
```asm
; Check if 'A' key pressed (row 1, col 2)
check_a:
        lda #%11111011  ; Select column 2 (bit 2 = 0)
        sta $dc00
        lda $dc01       ; Read rows
        and #%00000010  ; Check row 1 (bit 1)
        beq a_pressed   ; If 0, key is down
        rts
a_pressed:
        ; Handle key press
        rts
```

**Fast ADSR for Responsive Sound:**
```asm
        lda #$09        ; Attack=0, Decay=9 (fast)
        sta $d405
        lda #$00        ; Sustain=0, Release=0 (instant)
        sta $d406
```

**Multiple Key Scanning Loop:**
```asm
scan_all:
        ldx #$00        ; Key counter
loop:   lda columns,x   ; Get column mask
        sta $dc00
        lda $dc01       ; Read row
        and rows,x      ; Check specific row
        beq key_down
        inx
        cpx #num_keys
        bne loop
        rts
```

## Playable Milestone

**This lesson delivers the first playable interactive program:**
- Press keys A-K → hear musical scale C-C
- Immediate sound response
- Can play simple melodies by ear
- Foundation for rhythm game mechanics (L6-7)
