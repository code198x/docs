# Phase 6: Waveform

**Game:** Starfield (C64 Game 1)
**Units:** 81–96
**Theme:** Full SID soundtrack and rich sound design
**6510 Focus:** SID register architecture, ADSR envelope shaping, filter control, CIA timer-driven music playback
**Hardware:** Complete SID chip ($D400–$D41C), CIA timer interrupts
**Status:** Planned

---

## Overview

The SID chip defined a generation of game audio. Phase 6 doesn't just add "music" — it teaches what makes the SID *the SID*. Three independent voices with proper ADSR envelopes. A resonant multi-mode filter. Ring modulation and oscillator sync. These aren't features other 8-bit chips have — the SID is closer to an analogue synthesiser than a beeper.

Phase 1 used two SID voices for sound effects (laser and explosion). Phase 6 takes full ownership: a crafted sound effect library replaces the placeholder sounds, a three-voice music engine plays during the title screen, and the filter — the SID's most distinctive feature — adds character to explosions and music alike.

The 6510 focus is timer-driven playback. Music needs consistent tempo regardless of game logic load. A CIA timer interrupt fires at a fixed rate (typically 50Hz for PAL), advancing the music sequencer independently of the main game loop.

---

## Prerequisites from Phase 5

- Raster interrupt framework — the CIA timer interrupt runs alongside raster IRQs
- VIC-II memory configuration — understanding hardware register architecture transfers to SID
- Fixed-point math — frequency calculations for musical notes
- Self-modifying code — useful for optimised register updates

---

## Unit Progression

| Unit | Title | New 6510 Concept | Game Addition |
|------|-------|-----------------|---------------|
| 81 | SID Architecture Deep Dive | Register map ($D400–$D41C), 3-voice structure | Understanding the chip |
| 82 | ADSR Envelopes | Attack-Decay-Sustain-Release values and timing curves | Shaped sounds |
| 83 | Waveform Types | Triangle, sawtooth, pulse, noise — selection and character | Tonal variety |
| 84 | Sound Effect Library | Parameterised routine (waveform, freq, ADSR, sweep) | Varied SFX |
| 85 | Replace All Sounds | Integrate crafted SFX throughout the game | Cohesive audio |
| 86 | Title Music (2 Voices) | Note table (frequency values), sequence data, playback routine | Atmosphere |
| 87 | Three-Voice Music | Voice 3 bass or counter-melody, interleaved playback | Full SID richness |
| 88 | CIA Timer Music | CIA timer 1 interrupt for stable tempo | Rock-solid playback |
| 89 | Music Stops on Game Start | State-controlled playback, clean voice release | Clean transitions |
| 90 | Game Over Jingle | Short descending phrase | Punctuation |
| 91 | Wave Complete Jingle | Short ascending phrase | Achievement |
| 92 | High Score Jingle | Celebratory phrase, distinct from others | Distinction |
| 93 | SID Filter | Low-pass/high-pass/band-pass ($D418), cutoff ($D415/$D416), resonance ($D417) | SID character |
| 94 | Filter Sweeps | Dynamic cutoff frequency during sound effects | **That SID sound** |
| 95 | Sound Priority | Voice stealing with priority queue, don't cut music | No ugly cutoff |
| 96 | Integration + Audio Balance | Volume, filter routing, voice allocation audit | Sounds great |

---

## Key Teaching Moments

### ADSR Envelopes (Unit 82)

Most 8-bit chips have on/off sounds. The SID has proper ADSR envelopes: Attack (how quickly the sound reaches full volume), Decay (how quickly it drops to the sustain level), Sustain (the held volume), Release (how quickly it fades after the gate closes). Two register bytes control all four stages. The difference between a beep and a musical note is ADSR.

### The Note Table (Unit 86)

Musical notes map to SID frequency values. Middle C is $1CD6 (16-bit value split across two registers). A lookup table of 96 notes (8 octaves × 12 semitones) lets the music engine play any note with a single table index. This is the same approach professional C64 music drivers (like those by Rob Hubbard) use — data-driven sequences indexing into a frequency table.

### CIA Timer Interrupts (Unit 88)

Music needs consistent tempo. The game loop's timing varies with enemy count, collision checks, and raster effects. Solution: a separate interrupt source. CIA timer 1 can generate an IRQ at a programmable rate — set it to fire at 50Hz (PAL) or 60Hz (NTSC), and the music sequencer advances at a rock-solid tempo regardless of what the game is doing. This runs alongside the raster interrupt, not instead of it.

### The Filter (Unit 93)

The SID's resonant filter is its most distinctive feature. Low-pass cuts high frequencies (warm, muffled). High-pass cuts low frequencies (thin, bright). Band-pass keeps only a range (nasal, vocal). Resonance boosts frequencies around the cutoff point. The filter is controlled by three registers: cutoff frequency ($D415/$D416), resonance + voice routing ($D417), and mode + volume ($D418). When you sweep the cutoff during an explosion, you get *that* C64 sound.

### Voice Stealing (Unit 95)

With three voices shared between music and sound effects, playing a laser sound means temporarily stealing a voice from the music. A priority system determines which voice to steal (typically the one playing the least important musical part) and restores it when the effect ends. Poor voice stealing is why some C64 games have music that glitches when you shoot. Good voice stealing is invisible.

---

## 6510 Concepts Introduced

1. SID register map — 29 registers across 3 voices + filter + volume (Unit 81)
2. ADSR envelope parameters — 4-bit values packed into two registers (Unit 82)
3. Waveform selection — control register bits 4–7 select wave type (Unit 83)
4. Note frequency table — 16-bit values for 96 musical notes (Unit 86)
5. Music sequencer — pattern data, note duration, sequence pointer (Unit 86)
6. CIA timer interrupt — programmable timer alongside raster IRQ (Unit 88)
7. Filter registers — cutoff, resonance, routing, mode (Unit 93)
8. Voice stealing — priority-based voice allocation between music and SFX (Unit 95)

---

## Hardware Registers

### New in Phase 6

| Register | Purpose | Introduced |
|----------|---------|-----------|
| `$D400`–`$D414` | Full voice register map (3 voices × 7 registers) | Unit 81 |
| `$D415`/`$D416` | Filter cutoff frequency (lo/hi) | Unit 93 |
| `$D417` | Filter resonance (bits 4–7) + voice routing (bits 0–2) | Unit 93 |
| `$D418` | Volume (bits 0–3) + filter mode (bits 4–6) | Unit 93 |
| `$DC04`/`$DC05` | CIA1 timer A (low/high byte) | Unit 88 |
| `$DC0D` | CIA1 interrupt control register | Unit 88 |
| `$DC0E` | CIA1 control register A (start/stop timer) | Unit 88 |

---

## Game State at Phase End

After Unit 96:

- **Three-voice title music** — melodic, atmospheric, distinctly C64
- **Crafted sound effects** — laser, explosion, collect, shield break, death — all shaped with ADSR
- **Filter sweeps** — explosions and power-up sounds use the SID filter for character
- **CIA-timed playback** — music tempo is independent of game logic load
- **Jingles** — game over, wave complete, high score — each musically distinct
- **Voice stealing** — sound effects play over music without audible glitches
- **Volume balance** — SFX and music coexist at appropriate levels

The game sounds as good as it looks. The SID is fully utilised.

---

## What Carries to Phase 7

- **CIA timer interrupts** — Phase 7's sprite multiplexing uses precise timing
- **Interrupt management** — multiple interrupt sources (raster + CIA) coexist
- **SID sound system** — boss encounters need dramatic audio cues
- **Voice management** — boss warning siren uses the priority system

---

**Version:** 1.0
**Last Updated:** 2026-02-06
