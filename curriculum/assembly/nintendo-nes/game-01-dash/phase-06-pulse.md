# Phase 6: Pulse

**Game:** Dash (NES Game 1)
**Units:** 81-96
**Theme:** Sound and music -- the five APU channels
**6502 Focus:** APU register architecture, timer-driven music playback, subroutine parameter patterns, channel management
**Hardware:** APU ($4000-$4017) -- 2 pulse, triangle, noise, DMC channels
**Status:** Planned

---

## Overview

The NES APU has five channels, each with a distinct character: two pulse waves for melody and harmony (with duty cycle control for tonal variety), a triangle wave for bass (always the same timbre, no volume control), a noise channel for percussion, and a DMC channel for low-quality samples. Together they produce that unmistakable NES sound.

Phase 6 starts with individual channels and crafted sound effects, then builds a pattern-based music engine that runs in the NMI handler. Music plays at rock-solid 60Hz timing -- the NMI is the metronome. Sound effects steal channels from music temporarily, with a priority system that restores the music voice when the effect ends.

The APU runs independently once registers are set -- no CPU cost for sustained notes. The music engine's per-frame cost is reading one row of pattern data and writing a few registers. Even with the VBlank budget pressure from scrolling and seam loading, music fits comfortably.

---

## Prerequisites from Phase 5

- NMI handler with established VBlank update pattern
- VBlank budget awareness
- Title screen ready for music
- Complete visual system

---

## Unit Progression

| Unit | Title | New 6502 Concept | Game Addition |
|------|-------|------------------|---------------|
| 81 | APU Architecture | Register map ($4000-$4017), 5 channel structure | Understanding the chip |
| 82 | Pulse Channel Deep Dive | Duty cycle, timer, length counter, envelope | Shaped melody notes |
| 83 | Sound Effect Library | Parameterised routine (channel, freq, envelope, sweep) | Jump, land, collect, hurt, die |
| 84 | Replace Placeholder Sounds | Integrate crafted SFX throughout game | Cohesive audio |
| 85 | Triangle Channel | Bass notes, linear counter, no volume control | Foundation tone |
| 86 | Noise Channel | Short bursts for percussion: snare, hi-hat feel | Rhythm |
| 87 | Title Music (Pulse Melody) | Note table, sequence data, NMI playback | Atmosphere |
| 88 | Two-Channel Harmony | Pulse 1 melody + Pulse 2 counter-melody | Rich sound |
| 89 | Full 4-Channel Music | Triangle bass + noise drums + two pulses | **Proper soundtrack** |
| 90 | Pattern-Based Music Engine | Pattern table, row sequencer, tempo control | Reusable engine |
| 91 | In-Game Music | Looping level theme, distinct from title | Gameplay atmosphere |
| 92 | Music Stops for Events | State-controlled playback, clean channel release | Dynamic audio |
| 93 | SFX over Music | Channel stealing with priority, restore after | No ugly cutoff |
| 94 | DMC Channel | Sample playback for drum hits or voice | Sampled sounds |
| 95 | Level-Complete Jingle | Short celebratory phrase | Punctuation |
| 96 | Integration + Audio Balance | Volume, tempo, SFX/music coexistence | Sounds great |

---

## Key Teaching Moments

### Pulse Channel (Unit 82)

Each pulse channel has four registers:

```asm
; Pulse 1 registers
; $4000: DDLC VVVV  (duty, length halt, constant volume, volume/envelope)
; $4001: EPPP NSSS  (sweep enable, period, negate, shift)
; $4002: TTTT TTTT  (timer low 8 bits)
; $4003: LLLL LTTT  (length counter load, timer high 3 bits)

; Play a middle C on Pulse 1 with 50% duty
    lda #%10111111      ; Duty 50%, constant volume, max volume
    sta $4000
    lda #$00            ; No sweep
    sta $4001
    lda #$FD            ; Timer low (middle C ≈ $1FD)
    sta $4002
    lda #$01            ; Timer high, length counter
    sta $4003
```

The duty cycle shapes the tone: 12.5% is thin and reedy (good for arpeggios), 25% is bright, 50% is full and hollow (good for melody), 75% sounds like inverted 25%. Four tones from one parameter.

### The NMI as Metronome (Unit 90)

The NMI fires every frame (60Hz NTSC, 50Hz PAL). The music engine runs inside the NMI handler:

1. Decrement the current note's duration counter
2. If zero, advance to the next row in the pattern
3. Read note/instrument/effect for each channel
4. Write APU registers

One row of pattern data per tick. Tempo = how many NMI frames per row. Tempo 6 means one row every 6 frames = 10 rows per second at 60Hz. The NMI guarantees timing accuracy regardless of game logic complexity.

### SFX Priority (Unit 93)

Sound effects steal a music channel temporarily. The SFX system saves the current music state for that channel, plays the effect, then restores the music state when the effect ends. Priority levels prevent a low-priority effect from interrupting a high-priority one. Common pattern: Pulse 2 is the "steal" channel. Music continues on Pulse 1, Triangle, and Noise; only the harmony drops briefly during effects.

---

## 6502 Concepts Introduced

1. APU register architecture -- 4 registers per channel, bit field layout (Unit 81)
2. Duty cycle selection -- bits 6-7 of $4000 (Unit 82)
3. Note frequency table -- pre-calculated timer values for each musical note (Unit 87)
4. Pattern data format -- note + duration pairs, pattern pointers (Unit 90)
5. Tempo via frame counting -- ticks per row in NMI handler (Unit 90)
6. Channel state save/restore -- SFX priority system (Unit 93)
7. DMC register setup -- sample address, length, frequency (Unit 94)

---

## Hardware

### APU Channel Registers

| Channel | Registers | Purpose | Introduced |
|---------|-----------|---------|------------|
| Pulse 1 | $4000-$4003 | Melody (duty, envelope, sweep, timer) | Unit 82 |
| Pulse 2 | $4004-$4007 | Harmony (same structure as Pulse 1) | Unit 88 |
| Triangle | $4008-$400B | Bass (linear counter, timer, no volume) | Unit 85 |
| Noise | $400C-$400F | Percussion (envelope, mode, period) | Unit 86 |
| DMC | $4010-$4013 | Samples (frequency, address, length) | Unit 94 |
| Status | $4015 | Channel enable bits (write) / status (read) | Unit 81 |
| Frame Counter | $4017 | Sequencer mode (4-step or 5-step) | Unit 81 |

---

## Game State at Phase End

After Unit 96:

- **Crafted SFX** -- jump, land, collect, hurt, die, spring, checkpoint, level complete
- **4-channel music engine** -- pattern-based, running in NMI
- **Title music** -- atmospheric 4-channel theme
- **In-game music** -- looping level theme
- **Level-complete jingle** -- celebratory short phrase
- **SFX priority system** -- effects steal channels from music, restore after
- **DMC samples** -- drum hits or voice clips
- **Tempo control** -- adjustable ticks per row

The APU sings. Music runs automatically during gameplay with no main loop coordination.

---

## What Carries to Phase 7

- **Music engine** -- plays during combat and boss encounters
- **SFX system** -- enemy and boss sound effects integrated
- **Channel management** -- boss encounters may use special audio cues
- **NMI budget** -- music + scrolling + OAM fit together

---

**Version:** 1.0
**Last Updated:** 2026-02-06
