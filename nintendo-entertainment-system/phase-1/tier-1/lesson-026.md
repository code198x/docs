# Lesson 026: Number-to-Tiles Conversion

**Arc:** Scoring System
**Position:** Lesson 2 of 4 in arc
**Type:** Standard
**Estimated Completion:** 80 lines of assembly

## Learning Objectives
- Convert binary numbers to decimal digits
- Create digit tiles in CHR-ROM
- Implement division by 10 algorithm
- Prepare scores for nametable display

## Key Concepts
**Digit Extraction** - Divide by 10 repeatedly to get ones, tens digits
**Tile Indexing** - Digit 0 = tile $30, digit 1 = tile $31, etc.
**ASCII Offset** - NES tiles follow ASCII: '0' = $30, '9' = $39

## Code Pattern
```asm6502
.segment "ZEROPAGE"
temp_score: .res 1      ; Working copy of score
digit_tens: .res 1      ; Tens digit (0-9)
digit_ones: .res 1      ; Ones digit (0-9)

.segment "CODE"
; Convert score (0-99) to two decimal digits
ScoreToDigits:
    ; A = score to convert
    STA temp_score

    ; Extract tens digit (divide by 10)
    LDX #0              ; Tens counter
:   LDA temp_score
    CMP #10
    BCC @done_tens      ; Branch if < 10
    SBC #10             ; Subtract 10 (carry already set)
    STA temp_score
    INX
    JMP :-

@done_tens:
    STX digit_tens      ; Store tens digit

    ; Ones digit = remainder
    LDA temp_score
    STA digit_ones

    RTS

; Convert digit to tile index
DigitToTile:
    ; A = digit (0-9)
    ; Returns: A = tile index ($30-$39)
    CLC
    ADC #$30            ; ASCII/tile offset
    RTS
```

## Digit Tiles in CHR-ROM

```asm
.segment "CHARS"
; Background pattern table (tiles $00-$FF)
; ... other tiles ...

; Tile $30: '0'
.byte $3C,$66,$66,$66,$66,$66,$3C,$00  ; Plane 0
.byte $3C,$66,$66,$66,$66,$66,$3C,$00  ; Plane 1

; Tile $31: '1'
.byte $18,$38,$18,$18,$18,$18,$7E,$00
.byte $18,$38,$18,$18,$18,$18,$7E,$00

; Tiles $32-$39: '2'-'9' (similar 8×8 digit designs)
```

## Division by 10 Algorithm

```
Example: Convert 47 to digits

Start: temp_score = 47, tens = 0

Loop 1: 47 >= 10? Yes
        47 - 10 = 37
        tens = 1

Loop 2: 37 >= 10? Yes
        37 - 10 = 27
        tens = 2

Loop 3: 27 >= 10? Yes
        27 - 10 = 17
        tens = 3

Loop 4: 17 >= 10? Yes
        17 - 10 = 7
        tens = 4

Loop 5: 7 >= 10? No
        Done: tens = 4, ones = 7
```

## Quick Reference
### Conversion Pattern
```asm6502
; Score -> Digits
JSR ScoreToDigits   ; digit_tens, digit_ones set

; Tens digit -> Tile
LDA digit_tens
JSR DigitToTile     ; Returns tile index in A

; Ones digit -> Tile
LDA digit_ones
JSR DigitToTile
```

### Tile Indices
```
'0' = $30
'1' = $31
'2' = $32
...
'9' = $39
```

---

**Version:** 1.0
**Created:** 2025-10-27
