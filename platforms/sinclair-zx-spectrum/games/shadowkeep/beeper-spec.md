# Shadowkeep — Beeper Composition Spec

Companion to [brief.md](brief.md) (§7 Audio) and [per-unit-plan.md](per-unit-plan.md). The composition spec for the Shadowkeep title theme on the 48K Spectrum's beeper — **the target for sub-arc 1.4 (The Keep Has a Voice)** of the cell-based Place. Still current: the beeper title theme survives the re-pace unchanged (audio was never part of the relocated rendering engine).

## Vital statistics

| | |
|---|---|
| **Title** | *Shadowkeep* (title theme) |
| **Length** | 30-60 seconds, looping. Long enough to register a full melody; short enough that listening through it isn't a chore. |
| **Tempo** | 100-120 BPM (suggestion). Slower than Cadence — the keep is solemn, not driving. |
| **Time signature** | 4/4 (or 3/4 if it suits). |
| **Key** | D minor (suggested — dark, dramatic, minor-mode for the haunted setting). Override if a different key inspires. |
| **Voice** | One. The Spectrum 48K beeper is monophonic — bit 4 of port `$FE`, on or off, that's it. No harmony, no chords. |
| **Reference tracks** | *Manic Miner* title ("In the Hall of the Mountain King"); *Jet Set Willy* title; *Sabre Wulf* title; *Underwurlde* loader; *The Hobbit* opening tones. Listen on real beeper output, not the better-than-real emulator output, to calibrate. |

## What beeper music actually is

The Spectrum's beeper is a single bit. To produce a tone, you toggle that bit at a steady rate — a 1kHz square wave is 1000 toggles per second. Pitch is the toggle rate; loudness is fixed (the Spectrum has one volume: on). All "music" is monophonic square-wave melody with no envelope, no decay, no harmony.

What the beeper *can* do, with care:
- A clear, hummable melody
- Surprisingly expressive timing (a held note vs a staccato note vs a rest)
- Rhythm via note-length variation
- "Polyphony illusion" via fast alternation between two pitches (used in advanced Spectrum music; out of Phase 1 scope)

What it can't do:
- Chords
- Bass + melody
- Volume changes
- Smooth transitions

So compose for melody alone. The melody has to carry everything — rhythm, mood, identity — on its own.

## Structure (suggestion)

| Section | Bars | Duration (≈) | Mood |
|---|---|---|---|
| **Statement** | 8 | 0:00 – 0:16 | Establish the theme. The melody you want the listener humming. |
| **Variation** | 8 | 0:16 – 0:32 | Same chord movement, different melody. Shows the theme has range. |
| **Bridge / darken** | 4 | 0:32 – 0:40 | Lower register, shift to suggest danger or descent. |
| **Return** | 4 | 0:40 – 0:48 | Restate the opening, brought back. |
| **(loop)** | | | Returns to bar 1 cleanly. |

Total: 24 bars, ~48 seconds at 110 BPM. Adjust as composition demands.

## Mood directives

- **Statement:** the keep, before the dark. A theme that sounds dignified. Slow, deliberate. Could almost be a procession.
- **Variation:** the same world from a different angle. Lifts slightly — hope, or curiosity.
- **Bridge:** the shadows. Lower notes, longer durations. Something is wrong.
- **Return:** the resolve. The hero accepts the task. A definitive cadence (yes, Cadence's title is doing double duty here too).

## Reference tracks (please listen)

On Spectrum — emulators or real iron with proper beeper output:

- **Manic Miner title** (Matthew Smith, 1983) — the gold standard for beeper melody. Already nearly out of the platform's range.
- **Jet Set Willy title** (Smith, 1984) — slower, more atmospheric. Closer to Shadowkeep's mood than MM.
- **Sabre Wulf title** (Ultimate, 1984) — short loop, strong identity. Models the "<60 seconds, instantly recognisable" target.
- **Underwurlde loader** (Ultimate, 1984) — uses every trick the beeper allows.
- **The Hobbit** opening (Melbourne House, 1982) — sparse, evocative, pre-Manic-Miner beeper writing.

If composition stalls, listen to one of these *all the way through* — not as inspiration but as calibration. The bar isn't "music" — the bar is "music a 1984 beeper-only program could deliver."

## Submission format

Two streams of bytes per note: pitch and duration.

**Pitch** is a delay constant. Lower = higher pitch. Convert from desired frequency:

```
delay = 437,500 / frequency
```

(approximate, depends on the inner-loop timing of the music driver — driver implementer will calibrate the constant.)

**Duration** is in driver ticks at the music tempo. Quantise to:
- Whole note: 64 ticks
- Half: 32
- Quarter: 16
- Eighth: 8
- Sixteenth: 4
- Dotted variants: add half (e.g. dotted quarter = 24)

**Rest** is pitch byte `$00`. The beeper bit stays low; silence.

**Loop marker:** `$FF, $FF` returns the pointer to the start of the data.

```z80
; Example: opening four notes of Manic Miner-style melody
; D minor: D, F, A, D
beeper_data:
    .byte 88, 16    ; D5, quarter note
    .byte 74, 16    ; F5, quarter
    .byte 66, 16    ; A5, quarter
    .byte 44, 32    ; D6, half
    .byte 0, 16     ; rest
    ; ... continues ...
    .byte $FF, $FF  ; loop
```

## A short note table to compose against

Calibrated for the simple 48K Spectrum beeper driver. Approximate values; driver implementer will fine-tune.

| Note | Octave 4 | Octave 5 | Octave 6 |
|---|---|---|---|
| C  | 167 | 84  | 42 |
| C# | 158 | 79  | 40 |
| D  | 149 | 75  | 37 |
| D# | 140 | 70  | 35 |
| E  | 132 | 66  | 33 |
| F  | 125 | 63  | 31 |
| F# | 118 | 59  | 30 |
| G  | 111 | 56  | 28 |
| G# | 105 | 53  | 26 |
| A  | 99  | 50  | 25 |
| A# | 94  | 47  | 23 |
| B  | 88  | 44  | 22 |

Octaves 4-5 are the sweet spot for beeper — high enough to be tonal, low enough to be musical. Octave 3 sounds like a buzzy growl. Octave 6 is shrill but useful for accents. Outside this range, the Spectrum beeper sounds wrong.

## Tempo at the driver

The driver runs from a tick counter incremented by an interrupt or polling loop. At ~50 Hz frame rate, 16 ticks per quarter note gives 187 BPM (too fast). For 110 BPM target, use ~27 ticks per quarter, or scale all the duration units accordingly.

Driver implementer will fix the tick-to-tempo mapping when the music driver is written (Unit 14). Compose with the abstract durations above; the tempo is locked when the driver lands.

## Submission

Three artefacts when done:

1. The pattern data, in the byte-pair format shown.
2. A two-line summary: "Theme begins on D minor, modulates briefly to F major in the bridge, returns home."
3. Optional: a `.wav` export of how it sounds in your head, even if you have to sing it. Useful when checking the driver matches your intent.

## Scope discipline

Title theme is the single composition target for Phase 1. **In-game music is deliberately not in scope** — Atic Atac and Manic Miner shipped without it, and the in-game silence is part of the period feel. The in-game soundscape is beeper SFX (door opens, key pickup, hazard hit, death, victory) — those are designed alongside the music driver in Unit 14, not composed in advance.

If a strong in-game melody emerges as a stretch goal during Phases 2-4, fold it in then. Phase 1 keeps the silence honest.
