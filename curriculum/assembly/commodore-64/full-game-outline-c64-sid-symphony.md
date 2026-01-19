# C64 Game 6: SID Symphony - Full 128-Unit Outline

**Platform:** Commodore 64
**Game:** SID Symphony
**Units:** 128 (8 phases × 16 units)
**Concept:** Rhythm game where notes scroll horizontally across three tracks (one per SID voice). Hit the correct key when notes reach the hit zone. A deep dive into the SID chip through gameplay.

---

## Overview

SID Symphony teaches the SID chip through interactive music. After five action games, learners explore the C64's defining feature - its legendary sound chip. This isn't just playing samples; learners program the SID directly, understanding ADSR envelopes, waveforms, and filters while building a complete rhythm game.

**Key Learning Goals:**
- Deep SID chip mastery (all three voices)
- ADSR envelope programming
- Waveform selection and combination
- Filter control
- Keyboard matrix reading (beyond joystick)
- Precise timing for rhythm gameplay
- Song data structures and sequencing

---

## Phase 1: SID Fundamentals (Units 1-16)

### Unit 1: Single Note
**Builds:** Play one note when key pressed.
**Teaches:** Basic SID register access.
**Code pattern:**
```asm
SID = $d400
SID_FREQ_LO = SID + 0
SID_FREQ_HI = SID + 1
SID_PW_LO = SID + 2
SID_PW_HI = SID + 3
SID_CTRL = SID + 4
SID_AD = SID + 5
SID_SR = SID + 6

play_note:
    ; Set frequency for middle C (approximately)
    lda #$12
    sta SID_FREQ_LO
    lda #$11
    sta SID_FREQ_HI

    ; Set ADSR: Attack=0, Decay=9, Sustain=0, Release=0
    lda #$09
    sta SID_AD
    lda #$00
    sta SID_SR

    ; Gate on with triangle wave
    lda #%00010001      ; Triangle + gate
    sta SID_CTRL
    rts

stop_note:
    ; Gate off
    lda #%00010000      ; Triangle, gate off
    sta SID_CTRL
    rts
```
**If it doesn't work:** No sound? Check SID volume register ($D418) is set. Wrong pitch? Verify frequency values.

---

### Unit 2: SID Volume
**Builds:** Master volume control.
**Teaches:** Volume register.
**Code pattern:**
```asm
SID_VOLUME = $d418

init_sid:
    ; Set master volume to maximum (15)
    ; Lower 4 bits = volume, upper 4 bits = filter routing
    lda #$0f
    sta SID_VOLUME
    rts
```

---

### Unit 3: Frequency Table
**Builds:** Play any note by index.
**Teaches:** Note-to-frequency mapping.
**Code pattern:**
```asm
; Frequency table for one octave (C4-B4)
; Each entry is 16-bit frequency value
freq_table_lo:
    .byte $12,$23,$34,$47,$5b,$71,$89,$a2,$be,$db,$fb,$1c
freq_table_hi:
    .byte $11,$12,$13,$14,$15,$16,$17,$18,$19,$1a,$1b,$1d

play_note_by_index:
    ; X = note index (0-11)
    lda freq_table_lo,x
    sta SID_FREQ_LO
    lda freq_table_hi,x
    sta SID_FREQ_HI

    ; Gate on
    lda #$11
    sta SID_CTRL
    rts
```

---

### Unit 4: Multiple Octaves
**Builds:** Full note range.
**Teaches:** Octave shifting.

---

### Unit 5: Waveforms
**Builds:** Select triangle, sawtooth, pulse, noise.
**Teaches:** Waveform control bits.
**Code pattern:**
```asm
; Control register waveform bits:
; Bit 4 = Triangle
; Bit 5 = Sawtooth
; Bit 6 = Pulse
; Bit 7 = Noise
WAVE_TRIANGLE = %00010000
WAVE_SAWTOOTH = %00100000
WAVE_PULSE    = %01000000
WAVE_NOISE    = %10000000
GATE_ON       = %00000001

set_waveform:
    ; A = waveform constant
    ora #GATE_ON        ; Add gate
    sta SID_CTRL
    rts
```
**If it doesn't work:** No sound with pulse wave? Pulse width must be set (registers 2-3).

---

### Unit 6: ADSR Envelopes
**Builds:** Shape note dynamics.
**Teaches:** Attack, Decay, Sustain, Release.
**Code pattern:**
```asm
; ADSR values (0-15 each)
; Attack/Decay in upper/lower nibbles of $D405
; Sustain/Release in upper/lower nibbles of $D406

; Piano-like: fast attack, medium decay, low sustain
set_piano_envelope:
    lda #$09            ; Attack=0, Decay=9
    sta SID_AD
    lda #$30            ; Sustain=3, Release=0
    sta SID_SR
    rts

; Organ-like: instant attack, full sustain
set_organ_envelope:
    lda #$00            ; Attack=0, Decay=0
    sta SID_AD
    lda #$f0            ; Sustain=15, Release=0
    sta SID_SR
    rts
```

---

### Unit 7: Three Voices
**Builds:** Use all three SID channels.
**Teaches:** Voice register offsets.
**Code pattern:**
```asm
; Voice offsets from SID base
VOICE1 = $d400
VOICE2 = $d407
VOICE3 = $d40e

play_chord:
    ; Voice 1: C
    lda #$12
    sta VOICE1
    lda #$11
    sta VOICE1+1
    lda #$11
    sta VOICE1+4        ; Gate on

    ; Voice 2: E
    lda #$47
    sta VOICE2
    lda #$14
    sta VOICE2+1
    lda #$11
    sta VOICE2+4

    ; Voice 3: G
    lda #$89
    sta VOICE3
    lda #$17
    sta VOICE3+1
    lda #$11
    sta VOICE3+4
    rts
```

---

### Unit 8: Keyboard Matrix
**Builds:** Read keyboard input.
**Teaches:** CIA keyboard scanning.
**Code pattern:**
```asm
CIA1_PA = $dc00
CIA1_PB = $dc01

; Check if specific key is pressed
; Keyboard is 8x8 matrix
check_key_a:
    ; 'A' is row 1 (bit 1), column 2 (bit 2)
    lda #%11111101      ; Select row 1
    sta CIA1_PA
    lda CIA1_PB
    and #%00000100      ; Check column 2
    beq key_pressed     ; Zero = pressed
    ; Not pressed
    rts

key_pressed:
    ; Handle keypress
    rts
```
**If it doesn't work:** All keys detected? Check you're writing to PA before reading PB. Wrong key? Verify row/column mapping.

---

### Unit 9: Key-to-Note Mapping
**Builds:** Piano keyboard layout.
**Teaches:** Key assignment.

---

### Unit 10: Track Display
**Builds:** Three horizontal tracks on screen.
**Teaches:** Screen layout.

---

### Unit 11: Note Sprites
**Builds:** Notes as sprites scrolling left.
**Teaches:** Sprite setup for notes.

---

### Unit 12: Hit Zone
**Builds:** Target area where notes should be hit.
**Teaches:** Timing window.

---

### Unit 13: Basic Scoring
**Builds:** Points for hitting notes.
**Teaches:** Score tracking.

---

### Unit 14: Miss Detection
**Builds:** Notes that pass unhit.
**Teaches:** Miss handling.

---

### Unit 15: Sound - Note Hit
**Builds:** Confirmation sound.
**Teaches:** Feedback audio.

---

### Unit 16: Phase 1 Polish
**Builds:** Basic rhythm game working.

---

## Phase 2: Song System (Units 17-32)

### Unit 17: Note Data Format
**Builds:** Song note storage.
**Teaches:** Music data structures.
**Code pattern:**
```asm
; Note format: timing, track, pitch, duration
; Timing = frames from song start
; Track = 0/1/2 for voice
; Pitch = note index
; Duration = frames to hold

song_1:
    .byte 0, 0, 0, 8      ; Frame 0, track 0, C, 8 frames
    .byte 0, 1, 4, 8      ; Frame 0, track 1, E, 8 frames
    .byte 8, 0, 2, 8      ; Frame 8, track 0, D, 8 frames
    .byte 16, 0, 4, 8     ; etc.
    .byte $ff             ; End marker
```

---

### Unit 18: Note Spawning
**Builds:** Notes appear at right edge.
**Teaches:** Song playback.

---

### Unit 19: Scroll Speed
**Builds:** Notes move at consistent speed.
**Teaches:** Timing calibration.

---

### Unit 20: Multiple Songs
**Builds:** Song selection.
**Teaches:** Song management.

---

### Unit 21: Timing Accuracy
**Builds:** Perfect/Good/OK ratings.
**Teaches:** Timing windows.
**Code pattern:**
```asm
; Timing windows (frames from perfect)
PERFECT_WINDOW = 2
GOOD_WINDOW = 4
OK_WINDOW = 8

check_timing:
    ; A = frames from perfect hit
    cmp #PERFECT_WINDOW
    bcc perfect_hit
    cmp #GOOD_WINDOW
    bcc good_hit
    cmp #OK_WINDOW
    bcc ok_hit
    ; Miss
    jmp miss_note

perfect_hit:
    lda #100
    jmp add_score
good_hit:
    lda #50
    jmp add_score
ok_hit:
    lda #25
    jmp add_score
```

---

### Unit 22: Combo System
**Builds:** Consecutive hits build multiplier.
**Teaches:** Combo mechanics.

---

### Unit 23: Health/Life Bar
**Builds:** Misses reduce health.
**Teaches:** Failure state.

---

### Unit 24: Visual Feedback
**Builds:** Flash on hit/miss.
**Teaches:** Player feedback.

---

### Unit 25: Voice Assignment
**Builds:** Each track uses different voice.
**Teaches:** Multi-voice coordination.

---

### Unit 26: Voice Instruments
**Builds:** Different sound per track.
**Teaches:** Voice personalisation.

---

### Unit 27: Background Music
**Builds:** Song plays as you play.
**Teaches:** Music synchronisation.

---

### Unit 28: Auto-Play Notes
**Builds:** Unhit notes play automatically.
**Teaches:** Musical continuity.

---

### Unit 29: Difficulty Levels
**Builds:** Note density options.
**Teaches:** Difficulty design.

---

### Unit 30: Practice Mode
**Builds:** Slower speed, no fail.
**Teaches:** Learning mode.

---

### Unit 31: Song Progress Bar
**Builds:** Show position in song.
**Teaches:** Progress display.

---

### Unit 32: Phase 2 Polish
**Builds:** Complete song system.

---

## Phase 3: SID Deep Dive (Units 33-48)

### Unit 33: Pulse Width
**Builds:** Variable pulse width for rich tones.
**Teaches:** PWM.
**Code pattern:**
```asm
; Pulse width: 12-bit value in registers 2-3
; $800 = 50% duty (square wave)
; Lower values = thinner sound
set_pulse_width:
    ; Set to 50% duty cycle
    lda #$00
    sta SID_PW_LO
    lda #$08
    sta SID_PW_HI
    rts
```

---

### Unit 34: Pulse Width Modulation
**Builds:** Animate pulse width.
**Teaches:** PWM effects.

---

### Unit 35: SID Filter Basics
**Builds:** Low-pass filter.
**Teaches:** Filter registers.
**Code pattern:**
```asm
SID_FC_LO = $d415       ; Filter cutoff low (bits 0-2)
SID_FC_HI = $d416       ; Filter cutoff high (bits 3-10)
SID_RES_FILT = $d417    ; Resonance and filter routing
SID_MODE_VOL = $d418    ; Filter mode and volume

enable_lowpass:
    ; Set cutoff frequency
    lda #$00
    sta SID_FC_LO
    lda #$40            ; Mid cutoff
    sta SID_FC_HI

    ; Route voice 1 through filter, resonance=8
    lda #$81            ; Res=8, filter voice 1
    sta SID_RES_FILT

    ; Enable low-pass, volume=15
    lda #$1f            ; Low-pass + vol 15
    sta SID_MODE_VOL
    rts
```

---

### Unit 36: Filter Sweep
**Builds:** Animate filter cutoff.
**Teaches:** Filter modulation.

---

### Unit 37: High-Pass and Band-Pass
**Builds:** Other filter modes.
**Teaches:** Filter variety.

---

### Unit 38: Resonance
**Builds:** Filter resonance control.
**Teaches:** Resonance effect.

---

### Unit 39: Combined Waveforms
**Builds:** Mix waveforms.
**Teaches:** Waveform combination.

---

### Unit 40: Ring Modulation
**Builds:** Ring mod between voices.
**Teaches:** Ring mod effect.
**Code pattern:**
```asm
; Ring modulation: Voice 1 modulated by Voice 3 frequency
; Set bit 2 of voice 1 control register
enable_ring_mod:
    ; Set voice 3 to low frequency (modulator)
    lda #$10
    sta VOICE3
    lda #$01
    sta VOICE3+1

    ; Voice 1: triangle + ring mod
    lda #%00010101      ; Triangle + ring mod + gate
    sta VOICE1+4
    rts
```

---

### Unit 41: Hard Sync
**Builds:** Sync voice to another.
**Teaches:** Sync effect.

---

### Unit 42: Instrument Presets
**Builds:** Predefined instruments.
**Teaches:** Sound design.

---

### Unit 43: Per-Note Instruments
**Builds:** Different sounds per track.
**Teaches:** Track variety.

---

### Unit 44: Vibrato
**Builds:** Pitch wobble effect.
**Teaches:** Frequency modulation.

---

### Unit 45: Portamento
**Builds:** Pitch slides.
**Teaches:** Glide effect.

---

### Unit 46: Arpeggios
**Builds:** Fast note cycling.
**Teaches:** Arpeggio technique.

---

### Unit 47: SID Visualisation
**Builds:** Show waveforms on screen.
**Teaches:** Visual feedback.

---

### Unit 48: Phase 3 Polish
**Builds:** Rich SID sound palette.

---

## Phase 4: Content (Units 49-64)

### Unit 49-54: Songs 1-6
**Builds:** Six complete songs.
**Teaches:** Content creation.

---

### Unit 55-58: Songs 7-10
**Builds:** Four more songs.
**Teaches:** Variety.

---

### Unit 59: Song Editor Basics
**Builds:** Create custom songs.
**Teaches:** Editor mode.

---

### Unit 60: Song Save/Load
**Builds:** Save custom songs.
**Teaches:** Data persistence.

---

### Unit 61: Difficulty Variants
**Builds:** Easy/Medium/Hard per song.
**Teaches:** Difficulty curves.

---

### Unit 62: Unlock System
**Builds:** Unlock songs through play.
**Teaches:** Progression.

---

### Unit 63: Statistics
**Builds:** Track best scores.
**Teaches:** Score tracking.

---

### Unit 64: Phase 4 Polish
**Builds:** Complete song library.

---

## Phase 5: Presentation (Units 65-80)

### Unit 65: Title Screen
**Builds:** Attractive start.
**Teaches:** Title design.

---

### Unit 66: Song Select
**Builds:** Choose song to play.
**Teaches:** Menu design.

---

### Unit 67: Results Screen
**Builds:** Post-song statistics.
**Teaches:** Results display.

---

### Unit 68: High Scores
**Builds:** Per-song best scores.
**Teaches:** Score tables.

---

### Unit 69: Instructions
**Builds:** How to play.
**Teaches:** Tutorial.

---

### Unit 70: Visual Themes
**Builds:** Different colour schemes.
**Teaches:** Visual variety.

---

### Unit 71-74: Track Visuals
**Builds:** Animated backgrounds.
**Teaches:** Visual polish.

---

### Unit 75: Note Effects
**Builds:** Particle effects on hit.
**Teaches:** Hit feedback.

---

### Unit 76-78: Polish
**Builds:** Visual refinements.
**Teaches:** Quality.

---

### Unit 79: Credits
**Builds:** Attribution.
**Teaches:** Credits.

---

### Unit 80: Phase 5 Polish
**Builds:** Complete presentation.

---

## Phase 6: Advanced Features (Units 81-96)

### Unit 81: Two-Player Mode
**Builds:** Split keyboard play.
**Teaches:** Multiplayer.

---

### Unit 82: Battle Mode
**Builds:** Competitive scoring.
**Teaches:** Versus mode.

---

### Unit 83: Endless Mode
**Builds:** Procedural notes.
**Teaches:** Endless play.

---

### Unit 84: Speed Modes
**Builds:** 1x, 1.5x, 2x speed.
**Teaches:** Speed options.

---

### Unit 85: Modifier Options
**Builds:** Hidden notes, sudden.
**Teaches:** Challenge mods.

---

### Unit 86: Jukebox Mode
**Builds:** Listen to songs.
**Teaches:** Music player.

---

### Unit 87: SID Info Display
**Builds:** Show register values.
**Teaches:** Educational mode.

---

### Unit 88-90: Extra Songs
**Builds:** Additional content.
**Teaches:** More songs.

---

### Unit 91-95: Polish
**Builds:** Refinements.
**Teaches:** Quality.

---

### Unit 96: Phase 6 Polish
**Builds:** Complete features.

---

## Phase 7: Optimisation (Units 97-112)

### Unit 97: Frame Rate
**Builds:** Consistent timing.
**Teaches:** Performance.

---

### Unit 98: Input Latency
**Builds:** Minimal key response time.
**Teaches:** Input timing.

---

### Unit 99: Audio Sync
**Builds:** Perfect music sync.
**Teaches:** Timing precision.

---

### Unit 100-104: Balance
**Builds:** Fair difficulty.
**Teaches:** Game balance.

---

### Unit 105-108: Bug Fixes
**Builds:** Fix issues.
**Teaches:** Debugging.

---

### Unit 109-111: Polish
**Builds:** Final refinements.
**Teaches:** Quality.

---

### Unit 112: Phase 7 Complete
**Builds:** Stable game.

---

## Phase 8: Release (Units 113-128)

### Unit 113-116: Final Content
**Builds:** Complete song list.
**Teaches:** Content completion.

---

### Unit 117-120: Testing
**Builds:** Thorough testing.
**Teaches:** QA.

---

### Unit 121-124: Final Polish
**Builds:** Last fixes.
**Teaches:** Release prep.

---

### Unit 125-127: Documentation
**Builds:** Instructions.
**Teaches:** Documentation.

---

### Unit 128: Release
**Builds:** Final release.
**Teaches:** Shipping.

---

## Version History

- **1.0 (2026-01-18):** Initial 128-unit outline created.
