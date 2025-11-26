# Curriculum Specification

**Version:** 2.0
**Last Updated:** 2025-11-25
**Purpose:** Defines the structure, philosophy, and content model for all platform curricula.

---

## Overview

"Code Like It's 198x" teaches retro game development through complete, playable games. Each platform has a sequence of games ordered by complexity. Learners build real games from the first unit, with skills compounding through the sequence.

### The Problem with Phases and Tiers

The original curriculum model used:
- 8 phases × 16 tiers × 32 lessons = 4,096 lessons per platform
- Rigid structure that didn't scale across platforms of different complexity
- Abstract lesson progression disconnected from tangible outcomes

This produced technically correct but lifeless content - lessons that taught concepts in isolation rather than building toward something the learner cared about.

### The Games Model

The new model organises learning around complete games:
- Each platform has a sequence of games, ordered by complexity
- Each game contains 8, 16, or 32 units (powers of 2)
- Each unit is 60-120 minutes and produces a working intermediate result
- Skills compound naturally as games increase in sophistication

Learners always know what they're building and why. The game provides context; the units provide pacing.

---

## Unit Structure

### Unit Count Per Game

Games contain 8, 16, or 32 units depending on complexity:

| Units | Power | Typical Use |
|-------|-------|-------------|
| 8 (2³) | Standard | 8-bit games, simple 16-bit games |
| 16 (2⁴) | Extended | Complex 16-bit games, early 32-bit |
| 32 (2⁵) | Deep | Late 32-bit, 3D engines |

Most 8-bit platform games use 8 units. The constraint forces focus - if a game concept needs more than 8 units on a simple platform, it's probably too ambitious for that point in the sequence.

### Unit Duration and Outcome

Each unit is:
- **60-120 minutes** of focused work
- **Self-contained** - produces a working, runnable result
- **Incremental** - builds on the previous unit's code

The learner never types for an hour only to see an error message. Every unit ends with something that works, even if incomplete.

### Unit Naming

**Full format:** `[Platform] Game N: [Name], Unit M`
- Example: "C64 Game 1: SID Symphony, Unit 3"

**Shorthand:** `[Platform]-[Game]-[Unit]`
- Example: "C64-01-03"

**Reference in Pattern Library/Vault:**
- "Introduced in C64 Game 1: SID Symphony, Unit 3"
- "See C64-01-03 for initial implementation"

---

## Games Per Platform

Platforms vary enormously in complexity. A ZX81 curriculum shouldn't be the same size as a PlayStation curriculum. The number of games scales with platform depth:

| Platform Size | Equivalent Lessons | Games | Examples |
|---------------|-------------------|-------|----------|
| Micro | ~512 | 2-4 | ZX81, VIC-20 |
| Small | ~2,048 | 6-8 | Atari 2600, Game Boy |
| Standard | ~4,096-8,192 | 12-16 | C64, ZX Spectrum, NES |
| Large | ~8,192-16,384 | 16-24 | Amiga, Mega Drive |
| Massive | ~16,384-32,768 | 24-48 | PlayStation, Saturn |

"Equivalent lessons" is a rough guide for scoping, not a target. A platform has enough games when a learner completing them all could produce commercial-quality work for that platform.

### Ordering Games

Games are strictly ordered by complexity. Early games:
- Use fewer hardware features
- Have simpler game logic
- Produce results quickly

Later games:
- Combine multiple techniques
- Require deeper hardware understanding
- Approach commercial quality

A learner should be able to start at Game 1 with zero assembly knowledge and finish the final game with skills matching professional developers of that platform's era.

---

## Game 1: The Platform Hook

Every platform's first game showcases its killer feature - the thing that made people buy that machine. This creates immediate emotional investment and demonstrates why this platform matters.

| Platform | Killer Feature | Game 1 Concept |
|----------|----------------|----------------|
| Commodore 64 | SID sound chip | SID Symphony - rhythm game where you perform music |
| ZX Spectrum | Ingenuity despite constraints | Platformer with beeper music |
| NES | Tile-based PPU | Arena action built from tiles |
| Amiga | Custom chips (Copper/Paula) | Audiovisual showcase |

Game 1 should:
- Produce impressive output early (Unit 1-2 should already feel special)
- Be completable in 8 units
- Teach fundamental platform concepts through the game's needs
- Leave the learner wanting to build more

Game 1 is not a tutorial. It's a statement: "This is what this machine can do. Now let's learn how."

---

## Pedagogical Approach

The teaching style is modelled on 1980s British programming books: Usborne, INPUT magazine, the Home Computer Course. These materials taught through complete programs with rich visual annotation. The program was the lesson.

### Program-First Teaching

Every unit centres on a working program. Concepts are introduced when the program needs them, not in abstract isolation.

**Not this:**
> "Now we will learn about collision detection. Collision detection determines when two objects overlap..."

**This:**
> "The notes need to know when they've been hit. Here's how we detect the player pressing the right key at the right moment..."

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

If a unit can't be completed in 60-120 minutes, it's too big. Split it.

---

## Voice and Tone

### The Magazine Voice

The framing borrows from 1980s British gaming magazines - Your Sinclair, ZZAP!64, Crash. Irreverent, enthusiastic, occasionally conspiratorial. The reader is a co-conspirator, not a student.

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

## BASIC Gateway (Optional)

Some platforms have an accessible high-level language - BASIC, AMOS, Forth. For these platforms, an optional BASIC track provides a gentler entry point before assembly.

### When to Include a BASIC Gateway

Include if the platform has:
- A built-in or widely-available high-level language
- Historical use for hobbyist/learning development
- The ability to produce immediate visual/interactive results

| Platform | Gateway Language | Include? |
|----------|------------------|----------|
| Commodore 64 | BASIC V2 | Yes |
| ZX Spectrum | Sinclair BASIC | Yes |
| Amiga | AMOS BASIC | Yes |
| NES | None | No - assembly only |

### Scope

The BASIC track is:
- **1-2 games maximum** - enough to learn fundamentals, not a complete curriculum
- **Separate from the main sequence** - Game 1 in assembly is still Game 1
- **Optional** - learners can skip directly to assembly if preferred

BASIC games should demonstrate both the language's capabilities and its limitations. By the end, learners should understand why assembly exists without being told BASIC is bad.

### Not a Prerequisite

The assembly curriculum assumes no BASIC knowledge. A learner starting at Game 1 (assembly) should not feel they've missed something by skipping BASIC.

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
- "C64-08-05 covers the optimised version"

Units introduce techniques. Patterns provide the reference implementation. The Vault provides the history.

---

## Platform Curriculum Files

This specification defines how curricula work. The actual game sequences live in platform-specific files:

- `/docs/curriculum/commodore-64-curriculum.md`
- `/docs/curriculum/sinclair-zx-spectrum-curriculum.md`
- `/docs/curriculum/commodore-amiga-curriculum.md`
- `/docs/curriculum/nintendo-nes-curriculum.md`

Each platform curriculum file contains:

1. **Platform overview** - The platform's killer feature and teaching focus
2. **Game sequence** - Numbered list of games with brief descriptions
3. **Game details** - For each game: name, unit count, concept, skills taught
4. **BASIC gateway** (if applicable) - Separate section for BASIC track games

Platform curriculum files should be concise. They list what exists, not why the model works - that's this document's job.

---

## Version History

- **2.0 (2025-11-25):** Complete rewrite. Replaced phases/tiers/lessons model with games model.
- **1.0 (2025-01-15):** Original specification using 4,096 lessons per platform.
