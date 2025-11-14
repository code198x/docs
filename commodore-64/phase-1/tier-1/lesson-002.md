# Lesson 002: Frequency Control

**Arc:** First Sound
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 50-60 lines of assembly

## Learning Objectives

- Understand SID frequency calculation
- Build frequency table for musical notes
- Play multiple notes in sequence
- Use data tables in assembly
- Implement note-on/note-off timing

## Prerequisites

**From Previous Lessons:**
- L1: SID initialization and single note

**Assembly Knowledge:**
- LDA/STA for memory access
- Basic loops (INX, CPX, BNE)
- Data tables

## Key Concepts Introduced

### Frequency Tables
Musical notes have fixed frequency relationships. Store pre-calculated SID frequency values in a table for instant lookup.

### Note Calculation
SID frequency formula: `freq = (Hz * 16777216) / clock_speed`
Clock speed: PAL = 985248 Hz, NTSC = 1022727 Hz

### Sequential Playback
Play notes one after another by loading different frequency values from table with timing between notes.

### Note Off
Clear gate bit ($D404 bit 0) to stop note, then set it again for next note.

## Code Pattern

```asm
        * = $0801
        ; BASIC stub
        !byte $0c,$08,$0a,$00,$9e,$20,$32,$30,$36,$34,$00,$00,$00

        * = $0810

; Frequency table (C, E, G major chord)
freq_lo: !byte $11, $61, $f9  ; Low bytes
freq_hi: !byte $11, $15, $18  ; High bytes

init:   jsr clear_sid
        ldx #$00        ; Start at note 0

play:   lda freq_lo,x   ; Get frequency low byte
        sta $d400
        lda freq_hi,x   ; Get frequency high byte
        sta $d401

        lda #$11        ; Triangle + gate on
        sta $d404

        jsr delay       ; Note duration

        lda #$10        ; Triangle + gate off
        sta $d404

        jsr short_delay ; Brief pause

        inx
        cpx #$03        ; 3 notes
        bne play

        jmp init        ; Loop back to start

clear_sid:
        lda #$00
        ldx #$00
cls_loop:
        sta $d400,x
        inx
        cpx #$1d
        bne cls_loop

        lda #$08        ; Set ADSR
        sta $d405
        lda #$f0
        sta $d406
        lda #$0f        ; Set volume
        sta $d418
        rts

delay:  ldy #$20        ; Outer loop
dly1:   ldx #$ff        ; Inner loop
dly2:   dex
        bne dly2
        dey
        bne dly1
        rts

short_delay:
        ldy #$08
sdly1:  ldx #$ff
sdly2:  dex
        bne sdly2
        dey
        bne sdly1
        rts
```

## Hardware Interaction

**Chips Involved:**
- **SID** - Frequency registers for note pitch

**SID Frequency Registers:**
- Voice 1 uses $D400 (low) + $D401 (high) for 16-bit frequency value

**Musical Note Frequencies (PAL, A440 tuning):**
```
Note  Hz       SID Value (hex)
C3    130.81   $08B3
D3    146.83   $09C4
E3    164.81   $0AF6
F3    174.61   $0B9D
G3    196.00   $0D09
A3    220.00   $0EA2
B3    246.94   $106D
C4    261.63   $1167
D4    293.66   $1389
E4    329.63   $15ED
F4    349.23   $173B
G4    392.00   $1A13
A4    440.00   $1D45
B4    493.88   $20DA
C5    523.25   $22CE
```

## Common Pitfalls

1. **16-bit values split wrong:** Must store low/high bytes separately
2. **Table index mismatch:** freq_lo[0] must match freq_hi[0]
3. **Forgetting note-off:** Gate must be cleared then re-set for new note
4. **Timing too fast:** Need sufficient delay to hear notes
5. **X register overflow:** Check loop counter doesn't exceed table size

## Extension Ideas

- Add more notes (full octave C-C)
- Play different melodies (Twinkle Twinkle, Happy Birthday)
- Add second voice playing harmony
- Experiment with different waveforms per note
- Variable note durations from data table

## Builds Toward

**In This Tier:**
- L3: Keyboard triggers notes (interactive)
- L4: Melody playback from longer data
- L5: Rhythm and timing precision
- L6-7: Match-the-rhythm game mechanics

**In Next Tier:**
- Multiple voices simultaneously (chords)
- Background music during gameplay

## Quick Reference

**Frequency Calculation:**
```
SID_freq = (note_Hz * 16777216) / clock_rate
PAL:  clock_rate = 985248 Hz
NTSC: clock_rate = 1022727 Hz
```

**Data Table Pattern:**
```asm
table_lo: !byte $11, $27, $61
table_hi: !byte $11, $13, $15

        ldx #$00        ; Index
        lda table_lo,x  ; Load indexed value
        sta $d400
        lda table_hi,x
        sta $d401
```

**Note On/Off Pattern:**
```asm
note_on:
        lda #$11        ; Waveform + gate=1
        sta $d404

note_off:
        lda #$10        ; Waveform + gate=0
        sta $d404
```

**Timing Loop:**
```asm
delay:  ldy #$20        ; Adjust for duration
outer:  ldx #$ff
inner:  dex
        bne inner
        dey
        bne outer
        rts
```
