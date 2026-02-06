# Phase 6: Resonance

**Game:** Exodus (Amiga Game 1)
**Units:** 81-96
**Theme:** Sound and music -- Paula's four channels of sampled audio
**68000 Focus:** Paula registers, DMA audio, CIA timer interrupts, data-driven sequencing
**Hardware:** Paula ($DFF0A0-$DFF0DF), CIA-B timer ($BFD400+), INTENA/INTREQ
**Status:** Planned

---

## Overview

The Amiga's audio is fundamentally different from every other platform in the curriculum. No synthesis -- Paula plays raw sampled audio. Every sound is a recording: a real kick drum, a real guitar, a real voice. Four DMA channels play four samples simultaneously with independent pitch and volume control. Set the registers, enable the channel, and Paula handles everything.

Phase 6 starts with individual sound effects -- dig, build, explode, arrive -- then builds a MOD player for four-channel tracker music. The MOD format (created by Karsten Obarski for the Amiga) stores note/instrument/effect data in patterns. A CIA timer interrupt triggers row advancement at a stable tempo. Music plays automatically during gameplay.

The challenge: sound effects and music compete for the same four channels. A priority system steals a channel from music for an important effect, then restores the music state. This is how every Amiga game balances audio.

---

## Prerequisites from Phase 5

- Complete visual system with Copper effects
- Copper list structure in Chip RAM
- DMA timing awareness
- Game loop with frame timing

---

## Unit Progression

| Unit | Title | New 68000 Concept | Game Addition |
|------|-------|-------------------|---------------|
| 81 | Paula Architecture | Register map, 4 DMA channels, 8-bit signed samples | Understanding the chip |
| 82 | Sound Effect: Dig | Sample pointer, length, period, volume, DMA trigger | First real sound |
| 83 | Sound Effect Library | Parameterised routine (sample, period, volume) | Build, redirect, explode, arrive, die |
| 84 | Replace Placeholder Sounds | Integrate crafted samples throughout | Cohesive audio |
| 85 | MOD File Format | Patterns, instruments, sequence table | Music data structure |
| 86 | MOD Player (Basic) | Read pattern, set Paula registers per row | **Background music** |
| 87 | CIA Timer for Tempo | CIA-B timer interrupt triggers row advance | Rock-solid timing |
| 88 | Title Music | Full 4-channel MOD, atmospheric theme | Atmosphere |
| 89 | In-Game Music | Looping level theme, lighter texture | Gameplay backdrop |
| 90 | Music per Theme | Different MOD per level theme | Variety |
| 91 | SFX over Music | Channel steal with priority, state save/restore | No ugly cutoff |
| 92 | SFX Mixing | Multiple effects on available channels | Rich audio |
| 93 | Victory Jingle | Short celebratory phrase | Punctuation |
| 94 | Failure Sound | Descending phrase | Feedback |
| 95 | Ambient Sounds | Wind, water, creature chatter | Atmosphere |
| 96 | Integration + Audio Balance | Volume levels, channel allocation | Sounds great |

---

## Key Teaching Moments

### Paula Registers (Unit 82)

Each Paula channel has 5 registers:

```asm
; Play a sample on channel 0
    lea sample_data,a0
    move.l a0,$DFF0A0   ; AUD0LC: sample start address
    move.w #sample_len/2,$DFF0A4 ; AUD0LEN: length in words
    move.w #428,$DFF0A6  ; AUD0PER: period (428 = ~8287 Hz, middle C)
    move.w #64,$DFF0A8   ; AUD0VOL: volume (0-64)

    ; Enable audio channel 0 DMA
    move.w #$8201,$DFF096 ; DMACON: set bit 0 (AUD0) + bit 9 (master)
```

Lower period = higher pitch. Volume 0-64 (not 0-255). Samples must be in Chip RAM (first 512KB) because Paula uses DMA. The CPU is free once the channel is triggered.

### MOD Format (Unit 85)

A MOD file contains:
- **Song name** (20 bytes)
- **Instrument definitions** (31 instruments: name, length, finetune, volume, loop)
- **Song length and sequence** (which patterns play in which order)
- **Pattern data** (64 rows x 4 channels: note period + instrument + effect per cell)
- **Sample data** (raw 8-bit signed PCM)

The player reads one row per tick. For each channel: if there's a new note, look up the instrument's sample address and base period, apply the note, and write to Paula. Effects (volume slide, arpeggio, portamento) modify registers between rows. Four channels, four instruments playing simultaneously.

### CIA Timer Interrupt (Unit 87)

The CIA-B timer provides a stable tempo independent of the display:

```asm
; Set up CIA-B Timer A for music tempo
; BPM 125 = 50 ticks per second (PAL)
; Timer value = system clock / ticks_per_second
    move.b #<timer_value,$BFD400  ; TALO
    move.b #>timer_value,$BFD500  ; TAHI
    move.b #$11,$BFD E00          ; CRA: start timer, continuous
    move.w #$A000,$DFF09A        ; INTENA: enable CIA-B interrupt
```

When the timer fires, the interrupt handler advances the music by one tick. Multiple ticks per row (typically 6) give control over tempo. The handler reads the next note when the tick counter expires, writes to Paula, and returns. Music is automatic and timing-accurate.

---

## 68000 Concepts Introduced

1. Paula register architecture -- LC, LEN, PER, VOL per channel (Unit 81)
2. DMA audio triggering -- DMACON channel enable bits (Unit 82)
3. Parameterised playback routine -- sample/period/volume as parameters (Unit 83)
4. MOD pattern data parsing -- packed note/instrument/effect format (Unit 85)
5. CIA timer setup -- timer value, control register, interrupt enable (Unit 87)
6. Interrupt handler -- save registers, process, acknowledge, restore (Unit 87)
7. Channel priority system -- save/restore music state during SFX (Unit 91)
8. `INTENA`/`INTREQ` -- interrupt enable and acknowledge registers (Unit 87)

---

## Hardware

### Paula Audio Registers (per channel)

| Register | Offset | Purpose | Introduced |
|----------|--------|---------|------------|
| AUDxLC | +$00 | Sample start address (long) | Unit 82 |
| AUDxLEN | +$04 | Sample length in words | Unit 82 |
| AUDxPER | +$06 | Period (pitch: lower = higher) | Unit 82 |
| AUDxVOL | +$08 | Volume (0-64) | Unit 82 |

Channel base addresses: AUD0 = $DFF0A0, AUD1 = $DFF0B0, AUD2 = $DFF0C0, AUD3 = $DFF0D0

### CIA-B Timer

| Register | Address | Purpose | Introduced |
|----------|---------|---------|------------|
| TALO/TAHI | $BFD400/$BFD500 | Timer A low/high byte | Unit 87 |
| CRA | $BFD E00 | Timer A control | Unit 87 |
| ICR | $BFD D00 | Interrupt control | Unit 87 |

### Interrupt Control

| Register | Address | Purpose | Introduced |
|----------|---------|---------|------------|
| INTENA | $DFF09A | Interrupt enable (write set/clear) | Unit 87 |
| INTREQ | $DFF09C | Interrupt request (read/acknowledge) | Unit 87 |

---

## Game State at Phase End

After Unit 96:

- **Crafted SFX** -- dig, build, redirect, explode, arrive, die, footstep
- **MOD player** -- 4-channel pattern-based music engine
- **CIA-timed tempo** -- rock-solid playback independent of display
- **Title music** -- atmospheric 4-channel theme
- **In-game music** -- looping level themes per terrain type
- **Victory jingle** -- short celebratory phrase on level complete
- **SFX priority** -- effects steal channels, restore music after
- **Ambient audio** -- wind, water, creature sounds
- **Volume balance** -- SFX and music coexist cleanly

Paula sings. Four channels of sampled audio with real instruments and real impact.

---

## What Carries to Phase 7

- **Music engine** -- plays during complex puzzle sequences
- **SFX system** -- new effects for advanced abilities and cascading events
- **CIA timer pattern** -- reused for gameplay timing
- **Audio DMA awareness** -- factors into Blitter scheduling budget

---

**Version:** 1.0
**Last Updated:** 2026-02-06
