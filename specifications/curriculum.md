# Curriculum Specification

**Version:** 4.1
**Last Updated:** 2026-03-18
**Purpose:** Defines the structure, philosophy, and content model for all platform curricula.

---

## Overview

"Code Like It's 198x" teaches game design through retro game development. The platforms and languages are the medium — the real subject is the craft of making games.

Every game in the curriculum is a complete, playable project inspired by a commercially released title from the platform's era. Learners don't build toy examples — they build games that look and feel like the ones that defined these machines.

A learner who completes any track — BASIC, assembly, or any future language — can make games. Not just retro games. Games. The vintage hardware is the first workshop. The craft is portable.

---

## Game Design as the Primary Subject

Every game teaches two things in parallel:

1. **A universal game design concept** — feedback, tension, physics, AI, pattern recognition, procedural generation. These concepts apply to any platform, any language, any era. They are the curriculum's organising principle.

2. **A platform-specific implementation** — the commands, hardware registers, or language features that bring the design concept to life on a particular machine.

The design concepts are defined once and shared across all platforms and tracks. A learner doing C64 assembly learns *feedback* through VIC-II colour registers and SID voices. A learner doing Spectrum BASIC learns *feedback* through INK/PAPER and BEEP. A learner doing both recognises the same pattern implemented with different tools. Repetition across tracks is reinforcement, not redundancy.

### Core Design Concepts

These are taught across the curriculum, each introduced by a specific game and reinforced by later ones:

| Design concept | What the learner understands |
|---------------|------------------------------|
| **Feedback** | The game communicates through colour, sound, and display — not just text |
| **Tension** | Time pressure, scarcity, and escalation create engagement |
| **Pattern** | Recognise, reproduce, extend — the basis of difficulty curves |
| **The game loop** | Input → update → draw, running continuously — the universal heartbeat |
| **Content vs logic** | Separate what varies from what's fixed — the basis of data-driven design |
| **Structure** | Reusable pieces, organised code — programs you can change and extend |
| **Timing** | Frame-rate independence — the game behaves consistently regardless of load |
| **Information design** | The screen communicates meaning — colour as data, layout as language |
| **Physics** | Objects obey rules that feel right — collision, momentum, weight |
| **Opponent behaviour** | Simple rules produce emergent challenge — AI that feels intelligent |
| **Visual identity** | A world built from designed pieces — authored feel, consistent aesthetic |
| **Mechanics as meaning** | When the game system IS the experience, not a simulation of something else |
| **Character** | A sprite that feels alive — animation, weight, personality through movement |
| **Performance** | When design exceeds hardware, optimise — the bridge to lower-level thinking |
| **Procedural generation** | The computer as co-creator — systems that produce surprise |
| **Living worlds** | Autonomous agents, atmosphere, emergent narrative |

Each platform curriculum maps these concepts to specific games. The mapping varies by platform — a Spectrum BASIC game about feedback looks different from a C64 assembly game about feedback — but the concept is the same.

### Graphics from Day One

Every track uses the platform's graphics capabilities from the first game. Pixel-level drawing (PLOT/DRAW on the Spectrum, sprite registers on the C64, PPU writes on the NES) appears in Game 1 as part of the starter program or initial setup. It is formally taught within the first few games, not deferred to a later "graphics" game.

The learner's first program should look like a real game, not a text exercise. Character-cell workarounds, ASCII art, and text-only output are not acceptable when the hardware can draw. The machine can draw. We teach that from the start.

### Every Game Teaches Both Tracks

When writing unit content for any platform, name the design patterns explicitly alongside the programming concepts:

- "You just added a border colour change. That's *feedback* — the game telling the player something without words."
- "The countdown creates *tension*. Remove it and the game still works, but it stops being exciting."
- "These two lines — move toward the player, avoid walls — are *AI*. Simple rules that create the illusion of intelligence."

The learner builds vocabulary for game design at the same time as they build vocabulary for programming. Both are skills. Both transfer.

---

## Programming Craft

The code samples in this curriculum are not throwaway examples. They are models of how to write well-structured, high-quality code — code that happens to be a game. A learner who studies these samples should absorb good habits by example, not just learn what works.

### Principles

**Clear structure.** Every program has logical sections with a visible organisation. Subroutines do one thing. Related code is grouped together. A reader can find their way around without reading every line. In BASIC this means well-chosen line number ranges and section comments. In assembly it means labelled blocks, consistent entry/exit conventions, and documented register usage.

**Meaningful names.** Variable names, labels, and subroutines are chosen for clarity within the constraints of the language. In Sinclair BASIC, `n` is the secret number, `g` is the guess, `c` is the count — not arbitrary letters. In assembly, labels like `draw_sprite`, `check_collision`, and `game_over` describe what the code does. Naming is the first act of documentation.

**No magic numbers.** If a value has meaning, it should be readable. When `22528` appears (the Spectrum's attribute file base address), it is explained once and referenced by purpose thereafter. When `20` appears as a countdown duration, the learner knows what it means and why it was chosen. Constants should be self-evident or documented, never mysterious.

**Separation of concerns.** Game logic is separate from display code. Data is separate from the code that reads it. Subroutines handle one responsibility. In BASIC, this means the digit renderer is a GO SUB, not inline code pasted everywhere. In assembly, this means clean interfaces between modules. The principle is the same in every language: code that does one thing is code you can understand, test, and change.

**Boundary handling.** What happens when the player types 0? Or 101? Or presses a key during the title screen? Every game handles edge cases explicitly, and the curriculum calls out *why*: "What happens if we remove this validation? Try it. Type 200. Now you see why the check exists." Correct behaviour at boundaries is not defensive programming — it is the program working as designed.

**Deliberate shortcuts.** Performance constraints on vintage hardware sometimes demand trade-offs: short variable names for speed, unrolled loops, self-modifying code. These are taught as *conscious decisions*, not habits. The curriculum explains what was sacrificed (readability, maintainability) and why (the game needs to run at 50fps). A shortcut without an explanation is not a shortcut — it is a bad habit.

**Verifiable correctness.** Every game should have a clear definition of correct behaviour. The learner should be able to answer: "How do I know this works? What would prove it's broken?" In the curriculum, this manifests as:

- Checkpoints with expected output ("After typing these lines, you should see X")
- Boundary tests ("Try typing 0. The program should reject it")
- Before/after comparisons ("Remove line 720. What happens? Now put it back")

The emulator tooling supports automated verification: loading programs, feeding inputs, and checking outputs against expected results. Every code sample should be verifiable, and the verification should run as part of the content production process.

### The Craft Progresses

Early games (Foundations) have simple structure — a few sections, a few subroutines, single-letter variables. The learner absorbs the basics: organise your code, name things well, handle the edges.

Later games (Skills, Projects) demand more discipline — multiple subroutines calling each other, arrays managing state, display code separated from logic. The learner experiences why structure matters: because without it, a 300-line program is unmaintainable.

Advanced games push into deliberate trade-offs — speed optimisation, machine code helpers, memory management. The learner makes conscious choices about where to sacrifice clarity for performance, and documents those choices.

By the capstone, the learner writes code that is both high-quality *and* performant — not because they never take shortcuts, but because every shortcut is deliberate, documented, and justified. That is the craft of programming.

### Why Games, Not Lessons

The original curriculum model used abstract phases, tiers, and lessons — 4,096 per platform. This produced technically correct but lifeless content: lessons that taught concepts in isolation rather than building toward something the learner cared about.

The games model fixes this. Each platform has sixteen assembly games, each one a real project that a reader would want to play. Concepts are introduced when the game needs them, not in abstract isolation. A learner always knows what they're building and why.

### The No-Repetition Rule (Primary Systems)

Across the four primary platforms (Spectrum, C64, NES, Amiga), no two games share a genre. If the Spectrum has a platformer, no other primary platform does. If the C64 has a shoot 'em up, that genre is taken.

This rule applies strictly to the first four systems. Future systems may repeat genres where the hardware genuinely demands it — a Game Boy platformer teaches different lessons from a Spectrum platformer, and by the time both exist, the curriculum has enough variety that repetition won't feel lazy.

For the primary four, the rule exists because:

1. **Every game teaches something only that platform can teach.** A platformer on the Spectrum (Manic Miner, attribute-based collision) is a fundamentally different lesson from a platformer on the NES (Super Mario Bros, tile-based scrolling). Spending a game slot on a genre another platform already covers wastes the opportunity to teach something unique.

2. **It forces better choices.** The constraint pushes each platform toward the genres that defined it, rather than defaulting to the same safe picks across all four.

### Real Hardware Compatibility

Every game in the curriculum — assembly and BASIC — produces a binary that runs on real hardware. This is not a capstone feature; it is a baseline requirement. If the code assembles, it runs on the machine. The emulators are cycle-accurate specifically so that this guarantee holds.

---

## Assembly Track

### Sixteen Games Per Platform

Each primary platform (ZX Spectrum, Commodore 64, NES, Amiga) has sixteen assembly games. The games are graduated in complexity:

| Games | Units each | Total | Role |
|-------|-----------|-------|------|
| 1-8 | 128 | 1,024 | **Foundation and breadth.** Each game teaches a different genre and a different hardware feature. The platform's killer feature appears in Game 1. |
| 9-14 | 256 | 1,536 | **Depth and ambition.** Longer projects that combine multiple techniques. Commercial-quality results. |
| 15-16 | 512 | 1,024 | **Mastery.** Everything the hardware can do, combined into large-scale projects. |

Total per platform: 3,584 units. All games are subdivided into 16-unit phases.

### Phase Structure

Every game is divided into phases of 16 units. Each phase ends with a visible milestone — a new mechanic working, a new area playable, a new hardware feature integrated.

| Game Units | Phases |
|------------|--------|
| 128 | 8 phases |
| 256 | 16 phases |
| 512 | 32 phases |

### The No-Repetition Rule

Across the four primary platforms, no two games share a genre within the same unit-count tier. With 16 games per platform and 4 platforms, there is room for variety — but the rule ensures each game earns its place by teaching something the hardware does uniquely.

Future systems may repeat genres where the hardware genuinely demands it — a Game Boy platformer teaches different lessons from a Spectrum platformer.

---

## The Four Platforms

Each platform has a killer feature that defines its teaching focus. The detailed game sequences — all 16 games with genres, inspirations, and unit counts — live in the platform-specific curriculum documents (see Platform Curriculum Files below). This section describes what makes each platform worth teaching.

### ZX Spectrum

**Killer feature:** The attribute system — 256 bytes of colour define what the player sees. No other machine makes colour clash a game mechanic.

**Assembly:** 16 games from single-screen maze explorer through scrolling shooters, platformers, and puzzle games to an isometric adventure capstone.

**BASIC:** 16 games teaching game design from absolute zero through to machine code helpers and autonomous NPCs.

### Commodore 64

**Killer feature:** The SID sound chip (three voices, filters, ring modulation) and hardware sprites. The C64 sounds like no other machine.

**Assembly:** 16 games from sprite-based shooters through scrolling platformers, stealth puzzles, and run-and-gun action to demo-scene-quality capstone.

### Nintendo Entertainment System

**Killer feature:** The PPU — tile-based graphics, hardware scrolling, and a sprite system that makes 52 colours look like millions.

**Assembly:** 16 games from side-scrolling platformers through top-down adventures, Metroidvania exploration, and mapper-based large worlds.

### Commodore Amiga

**Killer feature:** Three custom chips — Agnus (DMA, Copper, Blitter), Denise (video), Paula (audio) — working in concert. The Amiga does things no other 16-bit machine can match.

**Assembly:** 16 games from Blitter-driven terrain puzzles through parallax showcases, pseudo-3D racing, and an OCS-to-AGA capstone.

---

## BASIC and High-Level Language Tracks

### Purpose

Some platforms have an accessible high-level language that provides a gentler entry point. These tracks teach both game design and programming fundamentals through complete, playable games.

High-level language games are **not simplified versions of the assembly games.** They are separate projects suited to the language's strengths and the platform's culture. They follow the same game design principles as the assembly track — every game teaches a universal design concept alongside platform-specific programming.

### Which Platforms

| Platform | Language | Games | Units | Why |
|----------|----------|-------|-------|-----|
| ZX Spectrum | Sinclair BASIC | 16 | 336 | How everyone started. Type-in listings, magazine culture. |
| Commodore 64 | BASIC V2 | TBD | TBD | Famously limited, but historically important. POKE teaches memory-mapped I/O. |
| Amiga | AMOS | TBD | TBD | Friendly, immediate, hobbyist. BOBs, Copper, MOD playback accessible from BASIC. |
| Amiga | Blitz Basic | TBD | TBD | Compiled, fast, commercial (Worms, Skidmarks). |
| NES | None | — | — | No high-level language. Assembly from the start. |

The Spectrum BASIC track is fully designed (see platform curriculum doc). Other tracks are planned but not yet detailed.

### Structure (Spectrum BASIC)

The Spectrum BASIC track has 16 games in graduated difficulty:

| Phase | Games | Units each | Total | Purpose |
|-------|-------|-----------|-------|---------|
| Foundations | 1-6 | 8 | 48 | Learn the language and core design patterns |
| Skills | 7-10 | 16 | 64 | Build real-time games with hardware access |
| Projects | 11-14 | 32 | 128 | Ambitious, visually distinctive software |
| Advanced | 15 | 32 | 32 | Complex systems |
| Capstone | 16 | 64 | 64 | A living world |

Other platform BASIC tracks may follow different structures suited to their language and culture.

### Independence Between Tracks

The assembly curriculum assumes no BASIC knowledge. A learner starting at assembly Game 1 should not feel they have missed something by skipping BASIC. The two tracks are independent paths that happen to cover the same platform. A learner who completes both gains reinforcement of the same game design concepts from two different angles.

---

## Unit Structure

### Unit Duration and Outcome

Each unit is:
- **60-120 minutes** of focused work
- **Self-contained** — produces a working, runnable result
- **Incremental** — builds on the previous unit's code

The learner never types for an hour only to see an error message. Every unit ends with something that works, even if incomplete.

### Unit Naming

**Full format:** `[Platform] Game N: [Name], Unit M`
- Example: "Spectrum Game 1: [Name], Unit 3"

**Shorthand:** `[Platform]-[Game]-[Unit]`
- Example: "SPEC-01-03"

**Reference in Pattern Library/Vault:**
- "Introduced in Spectrum Game 1, Unit 3"
- "See SPEC-01-03 for initial implementation"

---

## Pedagogical Approach

The teaching style is modelled on 1980s British programming books: Usborne, INPUT magazine, the Home Computer Course. These materials taught through complete programs with rich visual annotation. The program was the lesson.

### Program-First Teaching

Every unit centres on a working program. Concepts are introduced when the program needs them, not in abstract isolation.

**Not this:**
> "Now we will learn about collision detection. Collision detection determines when two objects overlap..."

**This:**
> "The player needs to know when they've hit a wall. Here's how we check whether the next tile is solid..."

### Visual Density

Units are visually rich:
- Screenshots of expected output at each checkpoint
- The finished result shown before the learner types a line
- Diagrams where they clarify (memory maps, screen layouts)
- Code surrounded by explanation, not buried in prose

The learner should be able to flip through a unit and immediately understand what they're building.

### Wonder-First Framing

Lead with what's exciting, not what's technically accurate.

**Not this:**
> "This lesson covers the SID chip's ADSR envelope registers."

**This:**
> "Let's make the SID sing. By the end of this unit, pressing a key will play a note."

Technical accuracy matters, but it serves the wonder, not the other way around.

### Single-Session Completion

Each unit produces a working result in one sitting. The learner should never:
- Stop mid-unit with broken code
- Wait until "next time" to see something run
- Type for an hour only to see an error

If a unit cannot be completed in 60-120 minutes, it is too big. Split it.

---

## Voice and Tone

### The Magazine Voice

The framing borrows from 1980s British gaming magazines — Your Sinclair, ZZAP!64, Crash. Irreverent, enthusiastic, occasionally conspiratorial. The reader is a co-conspirator, not a student.

**Not this:**
> "In this unit, you will learn to configure the VIC-II sprite registers."

**This:**
> "Don't panic. The BASIC stub is just a magic incantation that launches our machine code. Type it exactly, and we'll explain what it's doing once we're safely in assembly land."

The instruction itself remains precise and thorough. The irreverence is in the framing, not the technical content.

### Honesty About Difficulty

Some things are hard. Say so.

> "Calculating row × 40 in 6502 is a faff. There's no multiply instruction, so we'll use a lookup table. It's not elegant, but it's fast."

Don't pretend everything is easy. Don't apologise for difficulty either. Just acknowledge it and move on.

### British English

Use British spelling throughout:
- colour, grey, centre, organise, learnt

**Exception:** "program" for computer programs (not "programme").

### What to Avoid

- Marketing speak ("amazing", "incredible", "revolutionary")
- Excessive exclamation marks
- Condescension ("As you can see...", "Simply...", "Just...")
- Apologies for the platform ("Unfortunately, the C64 can only...")
- Forced nostalgia ("Back in the day...", "Remember when...")

---

## Standalone Technique Examples

Some techniques benefit from isolated demonstration before integration into a game. The `techniques/` directory provides minimal, focused examples.

### The Three-Level Model

```
Unit (game context)          → "Why do I need this? How does it fit?"
Standalone (isolated demo)   → "How does this technique work on its own?"
Pattern Library (reference)  → "Give me production-ready code to copy"
```

Each level serves a different purpose:
- **Units** teach techniques within game context (game-first pedagogy)
- **Standalone demos** provide isolated reference (50-100 lines, just the technique)
- **Patterns** provide optimised, production-ready implementations

### When to Create Standalone Demos

Create a standalone demo when a technique:
- Is complex enough that seeing it in isolation aids understanding
- Will be reused across multiple games
- Is a likely Pattern Library candidate
- Benefits from experimentation outside game context

**Not everything needs a standalone demo.** Simple techniques (reading a joystick, playing a sound effect) are better taught purely in game context.

### Standalone Demo Requirements

A standalone demo should:
- Be **minimal** — 50-100 lines, absolute maximum 150
- Be **complete** — compile and run without dependencies
- Be **focused** — demonstrate exactly one technique
- **Include comments** — enough to understand without the unit
- **Produce visible output** — show that it works

Example header:
```asm
; =============================================================================
; SPRITE MULTIPLEXING - STANDALONE DEMO
; Demonstrates displaying >8 sprites using raster interrupts
; Full tutorial: C64 Game 3, Unit 12
; =============================================================================
```

---

## Integration with Vault and Pattern Library

Units don't exist in isolation. They link to the Vault for context and the Pattern Library for reusable code.

### The Vault

The Vault is an encyclopedia of people, companies, games, techniques, hardware, events, and culture. Units link to Vault entries when context enriches understanding.

**Inline links:**
> "This sprite multiplexing technique was pioneered by [Andrew Braybrook](/vault/people/andrew-braybrook) in [Uridium](/vault/games/uridium)."

**When to link:**
- The person/game/technique is directly relevant to what's being built
- The link adds context the learner might want to explore
- The reference is specific, not generic

**When not to link:**
- Every unit mentioning sprites doesn't need a VIC-II link
- Forced connections ("This was released the same year as...")
- Links that interrupt the flow of instruction

### The Pattern Library

The Pattern Library contains production-ready code patterns. Units teach concepts; patterns provide copy-paste implementations.

**Reference format:**
> "For a complete, optimised implementation, see [Sprite Multiplexing (Basic)](/patterns/c64/rendering/sprite-multiplexing-basic)."

**Pattern evolution:**
Patterns exist at multiple complexity levels. Reference the appropriate version:
- "C64-01-03 introduces the basic pattern"
- "C64-03-05 covers the optimised version"

Units introduce techniques. Patterns provide the reference implementation. The Vault provides the history.

---

## Scaling to Future Systems

The four primary platforms (Spectrum, C64, NES, Amiga) each have sixteen assembly games. Future systems follow the same model but may vary in size:

| Platform Complexity | Assembly Games | Examples |
|---------------------|---------------|----------|
| Minimal | 4-8 | ZX81, VIC-20, Atari 2600 |
| Standard | 16 | Mega Drive, Atari ST, Game Boy, Master System, BBC Micro |
| Extended | 16+ | Systems with unusual depth or multiple distinct modes |

Future platforms may draw from the reserved genre pool or revisit genres already used by the primary four, where the hardware teaches genuinely different lessons. A Game Boy platformer and a Spectrum platformer are different enough to coexist — the constraint is about avoiding lazy repetition, not mechanical enforcement.

BASIC gateway tracks are added only when the platform has a historically significant high-level language (BBC BASIC, MSX BASIC, etc.).

---

## Platform Curriculum Files

This specification defines how curricula work. The actual game details live in platform-specific files:

- `/docs/platforms/sinclair-zx-spectrum/assembly.md`
- `/docs/platforms/commodore-64/assembly-skeleton.md` (pre-methodology draft)
- `/docs/platforms/nintendo-entertainment-system/assembly-skeleton.md` (pre-methodology draft)
- `/docs/platforms/commodore-amiga/assembly-skeleton.md` (pre-methodology draft)

Each platform curriculum file contains:

1. **Platform overview** — the platform's killer feature and teaching focus
2. **Game sequence** — the sixteen assembly games with descriptions
3. **Game details** — for each game: genre, inspiration, unit count, skills taught, phase names
4. **BASIC gateway** (if applicable) — the four BASIC games

Platform curriculum files should be concise. They list what exists, not why the model works — that's this document's job.

---

## Version History

- **4.1 (2026-03-18):** Added Programming Craft section: code quality principles (clear structure, meaningful names, no magic numbers, separation of concerns, boundary handling, deliberate shortcuts, verifiable correctness) and craft progression from Foundations through capstone. Code samples are models of good practice, not throwaway examples.
- **4.0 (2026-03-18):** Game design as the primary subject. Core design concepts table. "Graphics from Day One" rule. Cross-platform design concept framework. Every game teaches both design and programming.
- **3.0 (2026-03-09):** Major restructure. Introduced no-repetition rule across platforms. Every game inspired by a real commercial release. Real hardware compatibility made a baseline requirement, not a capstone feature.
- **2.1 (2026-01-19):** Added Standalone Technique Examples section (three-level model: units → standalone demos → patterns).
- **2.0 (2025-11-25):** Complete rewrite. Replaced phases/tiers/lessons model with games model.
- **1.0 (2025-01-15):** Original specification using 4,096 lessons per platform.
