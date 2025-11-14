# Lesson 001: Your First Note

**Arc:** First Sound
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 30-40 lines of assembly

## Learning Objectives

- Set up C64 memory map and BASIC stub for assembly programs
- Initialise SID chip registers
- Generate first sound from SID voice 1
- Understand memory-mapped hardware in assembly
- Write first complete 6502 assembly program

## Prerequisites

**From Previous Lessons:**
Phase 0 complete (BASIC fundamentals, hardware concepts, SID basics from L10-11)

**Assembly Knowledge:**
- None required - first assembly lesson
- BASIC SYS command understanding helpful

## Key Concepts Introduced

### BASIC Stub
Assembly programs need a BASIC stub to launch them. This is a tokenized BASIC line (e.g., `10 SYS 2064`) that jumps to our machine code.

### Memory Map Initialisation
Assembly programs start at $0801 (2049) with BASIC stub, then machine code begins at $0810 (2064). This is standard C64 convention.

### SID Chip Registers
SID has 29 registers starting at $D400. Each voice has 7 registers controlling frequency, waveform, and envelope.

### Memory-Mapped Hardware
SID registers are memory addresses. Writing to $D400 controls SID, just like POKE in BASIC.

## Code Pattern

```asm
        * = $0801       ; BASIC start

        ; BASIC stub: 10 SYS 2064
        .byte $0c,$08,$0a,$00,$9e,$20,$32,$30,$36,$34,$00,$00,$00

        * = $0810       ; Machine code start

init:   lda #$00        ; Clear SID registers
        ldx #$00
clear:  sta $d400,x
        inx
        cpx #$1d        ; 29 SID registers
        bne clear

        ; Set frequency for middle C (261.63 Hz)
        lda #$11        ; Low byte
        sta $d400       ; Voice 1 frequency low
        lda #$11        ; High byte
        sta $d401       ; Voice 1 frequency high

        ; Set waveform and gate
        lda #$11        ; Triangle wave + gate on
        sta $d404       ; Voice 1 control

        ; Set ADSR envelope
        lda #$08        ; Attack/Decay
        sta $d405
        lda #$f0        ; Sustain/Release
        sta $d406

        ; Set volume
        lda #$0f        ; Maximum volume
        sta $d418       ; Volume register

loop:   jmp loop        ; Infinite loop (note continues)
```

## Hardware Interaction

**Chips Involved:**
- **SID (6581/8580)** - Sound Interface Device at $D400-$D41C

**SID Voice 1 Registers:**
- `$D400` - Frequency low byte
- `$D401` - Frequency high byte
- `$D402` - Pulse width low byte
- `$D403` - Pulse width high byte
- `$D404` - Control register (waveform, gate, test, ring mod, sync)
- `$D405` - Attack/Decay
- `$D406` - Sustain/Release

**Global SID Registers:**
- `$D418` - Volume (bits 0-3) and filter routing

**Frequency Calculation:**
Middle C (261.63 Hz) = frequency value $1111 (4369 decimal)
Formula: `frequency_value = (note_hz * 16777216) / clock_speed`

## Common Pitfalls

1. **Forgetting BASIC stub:** Without it, LOAD won't work properly
2. **Wrong memory addresses:** SID starts at $D400, not $D000
3. **Missing volume:** $D418 must be non-zero or no sound
4. **Gate bit not set:** Bit 0 of $D404 must be 1 to start note
5. **SID not cleared:** Previous values in registers can cause issues
6. **Infinite loop missing:** Without `jmp loop`, the program continues into random memory, likely crashing. The infinite loop keeps the program running so the note continues.
7. **PAL vs NTSC frequency mismatch:** Frequency values differ between PAL (985248 Hz) and NTSC (1022727 Hz) machines. Using PAL frequencies on NTSC C64 results in sharp notes.
8. **Multiple waveforms selected:** Setting multiple waveform bits (e.g., triangle + sawtooth) creates unpredictable results. Select only one waveform per voice.

## Extension Ideas

- Change frequency values to hear different pitches
- Try different waveforms ($11=triangle, $21=sawtooth, $41=pulse, $81=noise)
- Adjust ADSR values to change note shape
- Add note-off (clear gate bit after delay)

## Builds Toward

**In This Tier:**
- L2: Frequency tables and note calculation
- L3: Keyboard input for interactive control
- L4-5: Note sequences and timing
- L6-7: Complete rhythm game

**In Next Tier:**
- Sprites and graphics (Tier 2)
- Multiple sound channels simultaneously

## Quick Reference

**6502 Instructions Introduced:**
- `LDA #$nn` - Load accumulator immediate
- `STA $aaaa` - Store accumulator absolute
- `LDX #$nn` - Load X register immediate
- `INX` - Increment X register
- `CPX #$nn` - Compare X register
- `BNE label` - Branch if not equal
- `JMP label` - Jump to label

**SID Voice Control Register ($D404):**
```
Bit 0: Gate (1=on, 0=off)
Bit 1: Sync
Bit 2: Ring modulation
Bit 3: Test
Bit 4: Triangle waveform
Bit 5: Sawtooth waveform
Bit 6: Pulse waveform
Bit 7: Noise waveform
```

**Common Note Frequencies (A440 PAL tuning):**
```
Middle C: $1167 (261.63 Hz)
D:        $1389 (293.66 Hz)
E:        $15ED (329.63 Hz)
F:        $173B (349.23 Hz)
G:        $1A13 (392.00 Hz)
A:        $1D45 (440.00 Hz)
```

**Assembler:**
Use ACME assembler (or KickAssembler/CA65):
```bash
acme -f cbm -o sid-note.prg lesson-001.asm
x64sc sid-note.prg
```
