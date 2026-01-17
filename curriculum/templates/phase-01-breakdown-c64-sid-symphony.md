# Phase 1 Breakdown: C64 SID Symphony

**Game:** SID Symphony (Game 1)
**Phase:** 1 of 8 (128-unit structure)
**Units:** 1-16
**Theme:** Assembly Fundamentals + First Sound

---

## Phase 1 Overview

By the end of Phase 1, learners will:
- Have a working SID synthesiser (one voice, keyboard controlled)
- Understand `lda`, `sta`, and basic addressing modes
- Know how to read and write to hardware registers
- Be able to diagnose "silent SID" problems

**Phase 1 Output:** Press keys 1-8, hear notes. Change waveform with function keys.

---

## Unit Progression

### Unit 1: Your First Sound
**Time:** 45 minutes
**Builds on:** Nothing — this is the start

**What happens:**
- Type complete working program (20 lines)
- Run it, hear continuous tone
- Experiment: change waveform byte, hear difference

**Key code:**
```asm
        lda #$21
        sta $d404       ; Sawtooth + gate
```

**Concepts introduced (not explained):**
- Assembly syntax exists
- `lda` and `sta` do something
- Hex numbers like `$d404`
- The SID lives at `$d4xx`

**Output:** Continuous sawtooth tone plays.

**Deferred to later:** Everything else.

---

### Unit 2: The BASIC Stub
**Time:** 60 minutes
**Builds on:** Unit 1's working program

**What happens:**
- Explain the `!byte` line they typed blindly
- Why we need it (BASIC loads and runs our code)
- What `*= $0801` means (where code lives)
- What `*= $080d` means (where our code starts)

**Key revelation:**
```asm
*= $0801
!byte $0c,$08,$0a,$00,$9e,$32,$30,$36,$31,$00,$00,$00
; This is: 10 SYS 2061
; It tells BASIC to jump to our machine code at $080d
```

**Concepts explained:**
- Memory addresses (where things live)
- BASIC and machine code relationship
- The `*=` directive (origin)

**Output:** Same as Unit 1 (no visible change — this unit is understanding).

**Experiment:** Change `$080d` to `$0900`, update the SYS number. Still works? Yes — code can live anywhere.

---

### Unit 3: LDA and STA
**Time:** 60 minutes
**Builds on:** Unit 2's memory model

**What happens:**
- Explain the two most important instructions
- `lda` = "Load Accumulator" (put a value in A)
- `sta` = "Store Accumulator" (copy A to memory)
- The accumulator is a register — a tiny piece of fast memory inside the CPU

**Key code dissected:**
```asm
        lda #$0f        ; Put the value $0f into A
        sta $d418       ; Copy A to address $d418
```

**The # matters:**
```asm
        lda #$0f        ; Load the VALUE $0f (immediate)
        lda $0f         ; Load FROM ADDRESS $0f (zero page)
```

**Concepts explained:**
- Registers (A is the first one they'll learn)
- Immediate addressing (`#`)
- Absolute addressing (no `#`)

**Output:** Same tone, but now they understand HOW it plays.

**Experiment:**
```asm
        lda #$08        ; Half volume
        sta $d418
```
Quieter! The value in A ends up at $d418, which is the volume register.

---

### Unit 4: The SID's Address Map
**Time:** 60 minutes
**Builds on:** Unit 3's understanding of `lda`/`sta`

**What happens:**
- Map out voice 1's registers
- Each register has a purpose
- Writing to an address changes SID behaviour

**SID Voice 1 Map:**
```
$d400 - Frequency low byte
$d401 - Frequency high byte
$d402 - Pulse width low
$d403 - Pulse width high
$d404 - Control (waveform + gate)
$d405 - Attack / Decay
$d406 - Sustain / Release
```

**Concepts explained:**
- Memory-mapped I/O (hardware at addresses)
- 16-bit values split across two bytes (frequency)
- Register purpose

**Output:** Same tone, but learner can now predict what changing each register does.

**Experiment:** Build a "register explorer" — show current values on screen, change them, hear results.

---

### Unit 5: Frequency and Notes
**Time:** 60 minutes
**Builds on:** Unit 4's register map

**What happens:**
- Frequency = how fast the waveform oscillates
- Higher number = higher pitch
- C64 frequency formula (simplified)
- Note table: which values make which notes

**Key code:**
```asm
; Middle C (C4) = frequency value $1168
        lda #$68
        sta $d400       ; Low byte
        lda #$11
        sta $d401       ; High byte
```

**Note table (one octave):**
```
C4  = $1168    G4  = $195c
C#4 = $1238    G#4 = $1a9c
D4  = $1318    A4  = $1bf0
D#4 = $1408    A#4 = $1d60
E4  = $1508    B4  = $1ee8
F4  = $161c    C5  = $22d0
F#4 = $1740
```

**Concepts explained:**
- 16-bit numbers (low byte + high byte)
- Little-endian (low byte first)
- Lookup tables

**Output:** Play a specific note by changing frequency values.

**Experiment:** Type in different frequency values, hear the scale.

---

### Unit 6: ADSR Envelopes
**Time:** 60 minutes
**Builds on:** Unit 5's frequency control

**What happens:**
- Notes need shape, not just on/off
- ADSR = Attack, Decay, Sustain, Release
- Two registers pack four values

**ADSR explained:**
```
Attack:  How fast the note reaches full volume
Decay:   How fast it drops to sustain level
Sustain: Volume while key is held
Release: How fast it fades after key released
```

**Register packing:**
```asm
; $d405 = Attack (high nibble) + Decay (low nibble)
; $d406 = Sustain (high nibble) + Release (low nibble)

        lda #$09        ; Attack=0, Decay=9
        sta $d405
        lda #$a0        ; Sustain=10, Release=0
        sta $d406
```

**Concepts explained:**
- Nibbles (4-bit values)
- Packing two values in one byte
- How envelope shapes sound

**Output:** Notes now have character — sharp attack, slow decay.

**Experiment:**
- `#$f0` attack/decay = slow swell
- `#$00` attack/decay = instant hit
- `#$0f` sustain/release = long fade

---

### Unit 7: The Gate Bit
**Time:** 60 minutes
**Builds on:** Unit 6's envelopes

**What happens:**
- The gate bit triggers the note
- Gate ON = Attack/Decay/Sustain
- Gate OFF = Release
- This is how you play notes, not just drones

**The control register ($d404):**
```
Bit 0: Gate (1 = note on, 0 = note off)
Bit 4: Triangle wave
Bit 5: Sawtooth wave
Bit 6: Pulse wave
Bit 7: Noise
```

**Playing a note:**
```asm
        lda #$21        ; Sawtooth + gate ON
        sta $d404       ; Note starts (attack begins)

        ; ... wait ...

        lda #$20        ; Sawtooth + gate OFF
        sta $d404       ; Note releases
```

**Concepts explained:**
- Bit manipulation (conceptual — no AND/OR yet)
- How envelope and gate interact
- Why continuous tone = gate always on

**Output:** Notes that start and stop properly.

**Experiment:** Toggle gate rapidly — hear the envelope restart each time.

---

### Unit 8: Simple Delay Loop
**Time:** 60 minutes
**Builds on:** Unit 7's gate control

**What happens:**
- Need to wait between gate on/off
- Introduce delay loops
- First look at `dex` and `bne`

**Delay loop:**
```asm
delay:
        ldx #$00        ; X = 0 (counts 256 times)
wait:   dex             ; X = X - 1
        bne wait        ; If X != 0, loop back
        rts             ; Return when done
```

**Concepts explained:**
- X register (another register like A)
- `dex` = decrement X
- `bne` = branch if not equal (to zero)
- Subroutines and `rts`

**Output:** Can now play a note for a controlled duration.

**Experiment:** Change `#$00` to `#$80` — half the delay. Shorter note.

---

### Unit 9: Keyboard Input
**Time:** 75 minutes
**Builds on:** Unit 8's timing control

**What happens:**
- Read the keyboard via KERNAL
- `$ffe4` (GETIN) returns key pressed
- Map keys to frequencies

**Reading a key:**
```asm
        jsr $ffe4       ; Call KERNAL GETIN
        cmp #$00        ; Was a key pressed?
        beq no_key      ; No — skip
        ; A now contains the key code
```

**Concepts explained:**
- KERNAL ROM routines
- `jsr` = jump to subroutine
- `cmp` = compare
- `beq` = branch if equal

**Output:** Press a key, see its code on screen.

**Experiment:** Map keys 1-8 to notes C through C (one octave).

---

### Unit 10: Playing Notes from Keys
**Time:** 75 minutes
**Builds on:** Unit 9's keyboard input

**What happens:**
- Combine everything: key → frequency → gate → sound
- Lookup table for key-to-frequency mapping
- Complete playable instrument

**Key processing:**
```asm
main_loop:
        jsr $ffe4           ; Get key
        cmp #$00
        beq main_loop       ; No key — keep waiting

        ; Key pressed — look up frequency
        sec
        sbc #$31            ; Convert '1'-'8' to 0-7
        asl                 ; Multiply by 2 (16-bit values)
        tax                 ; X = table offset

        lda freq_table,x    ; Low byte
        sta $d400
        lda freq_table+1,x  ; High byte
        sta $d401

        lda #$21            ; Gate on
        sta $d404

        jsr delay           ; Hold note

        lda #$20            ; Gate off
        sta $d404

        jmp main_loop

freq_table:
        !word $1168, $1318, $1508, $161c  ; C D E F
        !word $195c, $1bf0, $1ee8, $22d0  ; G A B C
```

**Concepts explained:**
- Lookup tables with indexing
- `asl` = shift left (multiply by 2)
- Indexed addressing (`lda table,x`)

**Output:** Press 1-8, hear C major scale.

---

### Unit 11: Waveform Selection
**Time:** 60 minutes
**Builds on:** Unit 10's playable keyboard

**What happens:**
- Add function keys to change waveform
- F1=triangle, F3=sawtooth, F5=pulse, F7=noise
- Store current waveform in a variable

**Waveform switching:**
```asm
check_waveform:
        cmp #$85            ; F1?
        bne not_f1
        lda #$10            ; Triangle
        sta waveform
        rts
not_f1:
        cmp #$86            ; F3?
        ; ... etc ...

waveform:
        !byte $20           ; Default: sawtooth
```

**Concepts explained:**
- Variables (memory locations with names)
- Multiple comparisons
- Storing state

**Output:** Full synthesiser — 8 notes, 4 waveforms.

---

### Unit 12: Visual Feedback
**Time:** 60 minutes
**Builds on:** Unit 11's complete synthesiser

**What happens:**
- Show current note on screen
- Show current waveform
- Simple character output

**Screen output:**
```asm
        lda #$01            ; 'A'
        sta $0400           ; Top-left of screen
```

**Concepts explained:**
- Screen memory ($0400-$07e7)
- PETSCII codes
- Visual feedback loop

**Output:** Screen shows which note and waveform are active.

---

### Unit 13: Code Organisation
**Time:** 60 minutes
**Builds on:** Unit 12's working synthesiser

**What happens:**
- Refactor into subroutines
- `init_sid`, `play_note`, `read_key`, `update_screen`
- Cleaner main loop

**Organised structure:**
```asm
main:
        jsr init_sid
        jsr init_screen
main_loop:
        jsr read_key
        beq main_loop       ; No key
        jsr process_key
        jmp main_loop
```

**Concepts explained:**
- Code organisation
- Subroutine design
- Why this matters for larger programs

**Output:** Same functionality, cleaner code.

---

### Unit 14: Integration and Polish
**Time:** 60 minutes
**Builds on:** Unit 13's organised code

**What happens:**
- Add title screen
- Instructions display
- Volume control (+ and -)
- Complete Phase 1 program

**Output:** Polished one-voice synthesiser with:
- Title screen
- Key instructions
- 8 notes (1-8)
- 4 waveforms (F1/F3/F5/F7)
- Volume control (+/-)
- Visual feedback

---

### Unit 15: What Can Go Wrong
**Time:** 60 minutes
**Builds on:** All previous units

**What happens:**
- Common Phase 1 bugs catalogued
- Screenshots of broken output
- Symptom → cause → fix patterns

**Bug 1: Silent SID**
```
Symptom: Program runs, no sound
Check 1: Volume register ($d418) — is it 0?
Check 2: Gate bit — is it set?
Check 3: ADSR sustain — is it 0?
```

**Bug 2: Wrong Notes**
```
Symptom: Notes play but pitches are wrong
Check 1: Frequency bytes swapped? (low/high reversed)
Check 2: Using wrong table offset?
Check 3: Table data correct?
```

**Bug 3: Notes Don't Stop**
```
Symptom: Sound continues after key released
Check 1: Gate bit cleared? ($20, not $21)
Check 2: Release value not zero?
```

**Bug 4: Keyboard Not Responding**
```
Symptom: No response to key presses
Check 1: GETIN called correctly? (jsr $ffe4)
Check 2: Comparing to correct key codes?
Check 3: Stuck in wrong loop?
```

**Concepts explained:**
- Systematic debugging approach
- Reading symptoms
- Most common errors for each concept learned

**Output:** Debugging reference for Phase 1 concepts.

---

### Unit 16: Fixing Broken Code
**Time:** 60 minutes
**Builds on:** Unit 15's debugging knowledge

**What happens:**
- Three broken programs provided
- Learner must find and fix bugs
- Hands-on debugging practice

**Exercise 1: Silent SID**
```asm
; This should play a note. It doesn't. Why?
start:
        cld
        lda #$00            ; <-- Bug here
        sta $d418
        lda #$68
        sta $d400
        lda #$11
        sta $d401
        lda #$00
        sta $d405
        lda #$f0
        sta $d406
        lda #$21
        sta $d404
loop:   jmp loop
```
**Fix:** Volume is 0. Change `lda #$00` to `lda #$0f`.

**Exercise 2: Note Won't Stop**
```asm
; Note plays but never stops
play_note:
        lda #$21
        sta $d404
        jsr delay
        lda #$21            ; <-- Bug here
        sta $d404
        rts
```
**Fix:** Gate not cleared. Second `lda #$21` should be `lda #$20`.

**Exercise 3: Wrong Frequencies**
```asm
; Should play C-D-E, plays garbage
freq_lo: !byte $68, $18, $08
freq_hi: !byte $11, $13, $15

play:
        ldx note_index
        lda freq_hi,x       ; <-- Bug here
        sta $d400
        lda freq_lo,x       ; <-- Bug here
        sta $d401
```
**Fix:** High/low swapped. Low byte goes to $d400, high to $d401.

**Phase 1 Complete.**

---

## Phase 1 Summary

| Unit | Focus | Key Concept | Output |
|------|-------|-------------|--------|
| 1 | First sound | — | Tone plays |
| 2 | BASIC stub | Memory addresses | Understanding |
| 3 | LDA/STA | Registers, addressing | Understanding |
| 4 | SID map | Memory-mapped I/O | Register explorer |
| 5 | Frequency | 16-bit values | Play specific notes |
| 6 | ADSR | Nibbles, envelopes | Shaped notes |
| 7 | Gate | Bit flags | Notes start/stop |
| 8 | Delay | Loops, X register | Timed notes |
| 9 | Keyboard | KERNAL, comparisons | Read keys |
| 10 | Key→Note | Tables, indexing | Playable scale |
| 11 | Waveforms | Variables, state | 4 waveforms |
| 12 | Display | Screen memory | Visual feedback |
| 13 | Organisation | Subroutines | Clean code |
| 14 | Polish | Integration | Complete synth |
| 15 | Debug theory | Symptom analysis | Debug reference |
| 16 | Debug practice | Hands-on fixing | Fixed programs |

**Phase 1 Result:** Working one-voice synthesiser + ability to debug common SID problems.

**Phase 2 Preview:** Add voices 2 and 3. Filters. Polyphony.

---

## Time Budget

| Units | Time Each | Total |
|-------|-----------|-------|
| Unit 1 | 45 min | 45 min |
| Units 2-8 | 60 min | 420 min |
| Units 9-10 | 75 min | 150 min |
| Units 11-14 | 60 min | 240 min |
| Units 15-16 | 60 min | 120 min |
| **Total** | — | **975 min (16.25 hours)** |

At ~1 hour per unit average, Phase 1 takes approximately **16 sessions**.

---

**Version:** 1.0
**Last Updated:** 2026-01-17
