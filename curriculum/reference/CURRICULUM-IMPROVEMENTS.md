# Curriculum Improvement Recommendations

**Purpose:** Address identified gaps while maintaining power-of-2 unit counts
**Date:** 2026-01-17
**Status:** Draft for review

---

## Executive Summary

The curriculum model is pedagogically sound but lacks:
1. **Debugging instruction** — virtually absent across all platforms
2. **Unit-level progression documentation** — games specify skills but not how units build
3. **Scaffolding for complex systems** — Games 11+ introduce multiple systems simultaneously
4. **Earlier distribution skills** — compressed at curriculum end

All recommendations maintain the existing power-of-2 unit structure (64/128/256 units per game, phases of 16 units).

---

## Recommendation 1: Integrate Debugging via Phase Structure

### The "Debug Checkpoint" Pattern

Each phase contains 16 units. Reserve units 15-16 of each phase for debugging and verification:

```
Phase N (16 units):
├── Units 1-12: Core content (build the feature)
├── Units 13-14: Integration and polish
└── Units 15-16: Debug Checkpoint
    ├── Unit 15: "What Can Go Wrong" — common errors for this phase's concepts
    └── Unit 16: "Fixing Broken Code" — hands-on debugging exercise
```

This allocates 12.5% of units to debugging without changing totals.

### Debug Checkpoint Content

**Unit 15 ("What Can Go Wrong"):**
- Show 3-5 common mistakes for concepts introduced in units 1-14
- Include screenshots of broken output (what the learner will see if they make this mistake)
- Explain the symptom → cause → fix pattern
- Reference the platform's common errors document

**Unit 16 ("Fixing Broken Code"):**
- Provide intentionally broken code
- Learner must identify and fix 2-3 bugs
- Teaches diagnostic thinking, not just "type this to fix"
- Verify fix by running the corrected program

### Example: C64 Game 1 (SID Symphony, 64 units = 4 phases)

| Phase | Theme | Debug Checkpoint Focus |
|-------|-------|----------------------|
| 1 | SID Fundamentals | Silent SID (wrong registers), decimal mode bugs |
| 2 | Keyboard & Game Loop | Input not responding (CIA conflicts), timing issues |
| 3 | Screen Layout | Wrong colours (VIC-II bank confusion), character set issues |
| 4 | Song Sequencing | Timing drift, note data corruption |

### What This Means for Existing Unit Counts

**No change to totals.** A 64-unit game still has 64 units:
- Before: 64 units of pure construction
- After: 48 units construction + 8 units integration + 8 units debugging

The 8 debugging units (2 per phase) are woven throughout, not added at the end.

---

## Recommendation 2: Document Unit Progression Within Phases

### The Problem

Current curriculum documents specify:
> "Game 1: SID Symphony — 64 units (4 phases). Skills: SID fundamentals, keyboard input, game loop..."

But not:
> "Phase 1, Units 1-4: Set up SID and play a single note. Units 5-8: Add ADSR envelopes..."

### Proposed Phase Documentation Format

For each game, add a phase-by-phase breakdown:

```markdown
### Game 1: SID Symphony (64 units)

#### Phase 1: SID Fundamentals (Units 1-16)
**Learning Goal:** Understand the SID chip and produce sound.

| Units | Focus | Outcome |
|-------|-------|---------|
| 1-2 | SID architecture | Single voice plays a tone |
| 3-4 | Waveforms | Switch between saw, pulse, triangle, noise |
| 5-6 | ADSR envelopes | Notes have attack/decay/sustain/release |
| 7-8 | Three voices | Chords and polyphony |
| 9-10 | Keyboard mapping | Press keys, hear notes |
| 11-12 | Filter basics | Low-pass, high-pass, band-pass |
| 13-14 | Integration | Combine all into playable instrument |
| 15-16 | Debug Checkpoint | Silent SID, wrong frequencies, decimal mode |

**Phase 1 Output:** Learner can press keys and hear filtered, enveloped notes.

#### Phase 2: Game Loop & Timing (Units 17-32)
...
```

### Implementation Path

1. Start with Game 1 for each platform (highest priority — first impression)
2. Expand to Games 2-6 (foundation games)
3. Complete Games 7-16 as they're developed

This doesn't change unit counts — it documents what each unit accomplishes.

---

## Recommendation 3: Scaffolded Introduction of Complex Systems

### The Problem

Game 11 (Dungeon Crawl) introduces simultaneously:
- Multi-room architecture
- Inventory system
- NPC dialogue
- Quest framework
- Combat system
- Disk I/O

This is 6 complex systems in one game, even with 128 units.

### Proposed Solution: Phased System Introduction

Structure Game 11's 8 phases to introduce one system per phase:

```markdown
### Game 11: Dungeon Crawl (128 units = 8 phases)

| Phase | Units | System Focus | Builds On |
|-------|-------|--------------|-----------|
| 1 | 1-16 | Room architecture | Single room, tile collision |
| 2 | 17-32 | Multi-room navigation | Room transitions, map data |
| 3 | 33-48 | Inventory system | Pick up items, equip, use |
| 4 | 49-64 | Combat system | Enemies, health, damage |
| 5 | 65-80 | NPC dialogue | Text display, branching choices |
| 6 | 81-96 | Quest framework | Objectives, tracking, completion |
| 7 | 97-112 | Disk I/O & saves | Save game state, load progress |
| 8 | 113-128 | Integration & polish | Full dungeon with all systems |
```

**Key principle:** Each phase introduces ONE major system. Integration happens in the final phase.

### Earlier Distribution Skills Introduction

Move distribution concepts earlier in the curriculum:

| Game | Distribution Skill | Notes |
|------|-------------------|-------|
| 6 | Understand PRG file structure | "What happens when you LOAD?" |
| 7-8 | Loading sequences conceptually | Visual understanding of load process |
| 10 | Simple Kernal file read | Read high score from disk |
| 11 | Full save/load system | Complete disk I/O |
| 16 | Advanced (fast loaders) | Builds on Games 10-15 foundation |

This spreads distribution across 6 games instead of compressing into Games 11 and 16.

---

## Recommendation 4: Progressive Debugging Complexity

### Debugging Skill Progression

As games increase in complexity, so should debugging instruction:

| Games | Debugging Focus | Tools/Techniques |
|-------|----------------|------------------|
| 1-4 | Symptom recognition | "Screen is black = VIC-II bank wrong" |
| 5-8 | Register inspection | Monitor commands, memory dumps |
| 9-12 | Timing debugging | Raster timing, interrupt conflicts |
| 13-16 | System debugging | Multi-component interaction bugs |

### Platform-Specific Debugging Tools

Each platform's Debug Checkpoints should introduce its debugging ecosystem:

**C64:**
- Game 2: VICE monitor basics (`m`, `d`, `r` commands)
- Game 5: Breakpoints and single-stepping
- Game 9: Raster debugging (seeing where time goes)
- Game 13: Memory watch and change detection

**ZX Spectrum:**
- Game 2: Fuse debugger basics
- Game 5: Attribute debugging (colour clash diagnosis)
- Game 9: Timing analysis
- Game 13: Bank switching debugging (128K)

**Amiga:**
- Game 2: WinUAE debugger basics
- Game 5: Copper list debugging
- Game 9: Blitter timing analysis
- Game 13: DMA conflict diagnosis

**NES:**
- Game 2: FCEUX debugger basics
- Game 5: PPU debugging (nametable viewer)
- Game 9: Sprite overflow diagnosis
- Game 13: Mapper debugging (bank state)

---

## Recommendation 5: Link Curriculum to Error Documentation

### Current State

Excellent error documentation exists:
- `/docs/platforms/commodore-64/advanced/6510-COMMON-ERRORS.md`
- `/docs/platforms/commodore-64/basic-v2/C64-COMMON-ERRORS.md`

But these are **reference documents**, not **curriculum-integrated**.

### Proposed Integration

**In Debug Checkpoint units, explicitly reference error documents:**

```markdown
## Unit 16: Fixing Broken Code

The code below has three bugs. Before looking at the fixes, try to
identify them yourself.

**Hint:** Review the [Zero Page Conflicts](/docs/platforms/commodore-64/advanced/6510-COMMON-ERRORS.md#1-zero-page-conflicts-with-kernalbasic)
and [Decimal Mode](/docs/platforms/commodore-64/advanced/6510-COMMON-ERRORS.md#3-decimal-mode-not-disabled-by-default)
sections if you're stuck.
```

**In error documents, back-reference curriculum:**

```markdown
### 3. Decimal Mode (Not Disabled by Default!)

**Curriculum Reference:** First encountered in C64 Game 1, Phase 1, Unit 15.
Revisited in Game 3, Phase 2 (calculation-heavy collision code).
```

This creates bidirectional linking between learning and reference.

---

## Recommendation 6: "Broken Code Gallery" Supplement

### Concept

Create a supplementary resource showing common broken states:

```
/docs/debugging/
├── commodore-64/
│   ├── broken-code-gallery.md
│   ├── screenshots/
│   │   ├── silent-sid.png
│   │   ├── sprite-not-visible.png
│   │   ├── wrong-colours.png
│   │   ├── flickering-multiplex.png
│   │   └── ...
│   └── diagnosis-flowcharts/
│       ├── no-sound.md
│       ├── no-sprites.md
│       └── ...
├── sinclair-zx-spectrum/
├── commodore-amiga/
└── nintendo-entertainment-system/
```

### Broken Code Gallery Format

```markdown
## Silent SID

**Screenshot:**
![Silent SID - no waveform indicator](screenshots/silent-sid.png)

**Symptoms:**
- Program runs but no sound
- No errors displayed

**Common Causes (check in order):**
1. Voice gate not set (`$D404` bit 0 = 0)
2. Volume register zero (`$D418` = 0)
3. ADSR sustain zero (note starts and immediately ends)
4. Wrong voice register offset (+7 per voice, not +1)

**Diagnosis:**
```asm
; Check SID volume
LDA $D418
BEQ VolumeZero  ; Volume is off

; Check voice 1 gate
LDA $D404
AND #$01
BEQ GateOff     ; Gate not set
```

**Fix:**
```asm
; Ensure volume is set
LDA #$0F
STA $D418

; Ensure gate is set (along with waveform)
LDA #$21        ; Pulse + gate
STA $D404
```
```

### Integration with Curriculum

Debug Checkpoint units reference the gallery:

> "If your SID is silent, check the [Silent SID](/docs/debugging/commodore-64/broken-code-gallery.md#silent-sid) diagnosis guide."

---

## Implementation Priority

| Priority | Recommendation | Effort | Impact |
|----------|---------------|--------|--------|
| **1** | Debug Checkpoints in phases | Medium | High — addresses critical gap |
| **2** | Phase documentation for Games 1-6 | Medium | High — improves onboarding |
| **3** | Broken Code Gallery (C64 first) | Low | Medium — visual debugging aid |
| **4** | Link curriculum ↔ error docs | Low | Medium — connects resources |
| **5** | Scaffolded system introduction | Medium | Medium — smooths difficulty curve |
| **6** | Earlier distribution skills | Low | Low — minor improvement |

---

## Example: Revised C64 Game 1, Phase 1

### Before (Implicit)

> Phase 1: SID Fundamentals (Units 1-16)
> Skills: SID voices, ADSR, waveforms

### After (Explicit)

```markdown
## Phase 1: SID Fundamentals (Units 1-16)

**Learning Goal:** Understand the SID chip architecture and produce controlled sound.

### Units 1-2: Your First Sound
Set up a SID voice and produce a tone. By the end, pressing RUN produces
a continuous note.

**Key Concepts:**
- SID address range ($D400-$D41C)
- Voice 1 frequency registers ($D400-$D401)
- Waveform selection ($D404)
- Volume control ($D418)

**Output:** A single sustained tone plays.

### Units 3-4: Waveforms
Switch between sawtooth, pulse, triangle, and noise. Hear how each
waveform sounds different.

**Key Concepts:**
- Waveform bits in $D404
- Pulse width registers ($D402-$D403)

**Output:** Program cycles through waveforms on keypress.

### Units 5-6: ADSR Envelopes
Shape notes with attack, decay, sustain, release. Notes now have
character — sharp attacks, slow fades.

**Key Concepts:**
- Attack/Decay register ($D405)
- Sustain/Release register ($D406)
- Gate bit timing

**Output:** Notes fade in and out naturally.

### Units 7-8: Three Voices
Add voices 2 and 3. Play chords. Each voice is independent.

**Key Concepts:**
- Voice register offsets (+7 per voice)
- Voice enable in $D404/$D40B/$D412

**Output:** Three-note chord plays.

### Units 9-10: Keyboard Input
Map keyboard keys to notes. The SID becomes a playable instrument.

**Key Concepts:**
- Keyboard scanning via CIA
- Note frequency table
- Key-to-frequency mapping

**Output:** Press keys, hear corresponding notes.

### Units 11-12: Filter Basics
Add low-pass, high-pass, and band-pass filtering. The SID gains depth.

**Key Concepts:**
- Filter cutoff ($D415-$D416)
- Filter resonance and mode ($D417)
- Voice routing to filter ($D417 bits 0-2)

**Output:** Notes pass through selectable filter.

### Units 13-14: Integration
Combine all elements. Multiple voices, envelopes, filters, keyboard control.

**Output:** Fully playable three-voice filtered synthesiser.

### Units 15-16: Debug Checkpoint

#### Unit 15: What Can Go Wrong

**Silent SID — No Sound At All**
- Symptom: Program runs, no audio
- Cause 1: Volume register ($D418) is zero
- Cause 2: Gate bit not set (waveform plays but no sound starts)
- Cause 3: ADSR sustain is zero (note dies immediately)

![Silent SID Screenshot](screenshots/game-01/silent-sid.png)

**Wrong Frequency — Notes Sound Off**
- Symptom: Notes play but pitches are wrong
- Cause 1: High/low byte reversed in frequency registers
- Cause 2: Using wrong voice offset (+7, not +1)

**Decimal Mode Bug**
- Symptom: Calculations produce strange values
- Cause: CLD not called at program start
- Fix: Add `CLD` as first instruction

See [6510 Common Errors](/docs/platforms/commodore-64/advanced/6510-COMMON-ERRORS.md)
for detailed explanations.

#### Unit 16: Fixing Broken Code

Below is a broken SID program. It should play a note but doesn't.
Find and fix the three bugs.

```asm
; BROKEN CODE - Find the bugs!
*= $0801
!basic_startup

Start:
    ; Bug 1 is somewhere here...
    LDA #$00
    STA $D418       ; Set volume

    LDA #$25
    STA $D400       ; Frequency low
    LDA #$1C
    STA $D401       ; Frequency high

    ; Bug 2 is somewhere here...
    LDA #$00
    STA $D405       ; Attack/Decay
    LDA #$F0
    STA $D406       ; Sustain/Release

    ; Bug 3 is somewhere here...
    LDA #$20
    STA $D404       ; Waveform (sawtooth)

Loop:
    JMP Loop
```

**Hints:**
1. What should the volume be?
2. What ADSR values let you hear the note?
3. What bit starts the note playing?

**Solutions:** (Reveal after attempting)
1. Volume should be $0F, not $00
2. Attack/Decay $00 is fine, but check if it's working with gate
3. Gate bit (bit 0) must be set: $21, not $20

**Phase 1 Complete.** You can produce filtered, enveloped sounds from
all three SID voices via keyboard control, and you can diagnose
silent-SID problems.
```

---

## Summary

These recommendations:

1. **Maintain power-of-2 structure** — no unit count changes
2. **Integrate debugging** — 2 units per phase (12.5% of curriculum)
3. **Document progression** — explicit unit-by-unit outcomes
4. **Scaffold complexity** — one system per phase in complex games
5. **Link resources** — curriculum ↔ error docs ↔ broken code gallery

The result: learners build games AND learn to fix them when things go wrong.

---

**Version:** 1.0
**Author:** Curriculum Review
**Status:** Ready for review
