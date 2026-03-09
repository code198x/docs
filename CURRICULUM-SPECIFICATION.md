# Curriculum Specification

**Version:** 3.0
**Last Updated:** 2026-03-09
**Purpose:** Defines the structure, philosophy, and content model for all platform curricula.

---

## Overview

"Code Like It's 198x" teaches retro game development through complete, playable games. Each platform has a short sequence of games ordered by complexity. Learners build real games from the first unit, with skills compounding through the sequence.

Every game in the curriculum is inspired by a commercially released title from the platform's era. Learners don't build toy examples — they build games that look and feel like the ones that defined these machines. The progression from game 1 to game 4 should be visible in screenshots alone.

### Why Games, Not Lessons

The original curriculum model used abstract phases, tiers, and lessons — 4,096 per platform. This produced technically correct but lifeless content: lessons that taught concepts in isolation rather than building toward something the learner cared about.

The games model fixes this. Each platform has four assembly games, each one a real project that a reader would want to play. Concepts are introduced when the game needs them, not in abstract isolation. A learner always knows what they're building and why.

### The No-Repetition Rule (Primary Systems)

Across the four primary platforms (Spectrum, C64, NES, Amiga), no two games share a genre. If the Spectrum has a platformer, no other primary platform does. If the C64 has a shoot 'em up, that genre is taken.

This rule applies strictly to the first four systems. Future systems may repeat genres where the hardware genuinely demands it — a Game Boy platformer teaches different lessons from a Spectrum platformer, and by the time both exist, the curriculum has enough variety that repetition won't feel lazy.

For the primary four, the rule exists because:

1. **Every game teaches something only that platform can teach.** A platformer on the Spectrum (Manic Miner, attribute-based collision) is a fundamentally different lesson from a platformer on the NES (Super Mario Bros, tile-based scrolling). But with only four games per platform, spending one on a genre another platform already covers wastes a slot.

2. **It forces better choices.** The constraint pushes each platform toward the genres that defined it, rather than defaulting to the same safe picks across all four.

### Real Hardware Compatibility

Every game in the curriculum — assembly and BASIC — produces a binary that runs on real hardware. This is not a capstone feature; it is a baseline requirement. If the code assembles, it runs on the machine. The emulators are cycle-accurate specifically so that this guarantee holds.

---

## Assembly Track

### Four Games Per Platform

Each primary platform (ZX Spectrum, Commodore 64, NES, Amiga) has four assembly games. The number four is deliberate:

- **It's achievable.** A complete platform is ~1,400 units. At one unit per day, that's under four years — ambitious but realistic for a solo author, faster with contributions.
- **It's a power of two.** Unit numbering, phase structure, and content division work cleanly.
- **Every game earns its place.** No filler, no "learn loops with Snake." Each game is one that would make someone click through to read.
- **It preserves genres.** Sixteen genres across four platforms leaves dozens available for future systems.

### Game Slots

Each slot has a role in the progression:

| Slot | Units | Role |
|------|-------|------|
| Game 1 | 128 | **Accessible entry.** The platform's killer feature, immediately. Looks like a real game from unit 1. |
| Game 2 | 256 | **Signature technique.** The hard thing that defines mastery on this platform. |
| Game 3 | 512 | **Ambitious commercial-quality.** A game that would have been sold in shops. |
| Game 4 | 512 | **Capstone.** Everything at mastery, plus platform distribution and production techniques. |

Total per platform: 1,408 units. Total across four platforms: 5,632 units.

### Phase Structure

Games are subdivided into phases — named milestones that give structure to long builds. Phase count and size follow powers of two:

| Game Units | Phases | Units per Phase |
|------------|--------|-----------------|
| 128 | 8 | 16 |
| 256 | 8 | 32 |
| 512 | 16 | 32 |

Each phase has a name (thematic, not numbered) and ends with a visible milestone — a new mechanic working, a new area playable, a new hardware feature integrated.

---

## The Four Platforms

### ZX Spectrum

**Killer feature:** The attribute system — 256 bytes of colour define what the player sees.

| # | Genre | Inspired by | Units | Teaches |
|---|-------|------------|-------|---------|
| 1 | Single-screen platformer | Manic Miner / Jet Set Willy | 128 | Attributes as game mechanic, gravity, collision, animation, level data |
| 2 | Horizontal scrolling shmup | R-Type / Zynaps | 256 | Software pixel scrolling (no hardware support), contended memory timing, boss patterns |
| 3 | Isometric adventure | Knight Lore / Head Over Heels | 512 | Isometric projection, depth sorting, puzzles, 128K AY music, bank switching |
| 4 | Capstone | Late-era commercial release | 512 | 128K/48K dual-mode, turbo tape loader, +3 disk support, loading screens |

**Visual journey:** coloured blocks on a single screen → smooth scrolling through alien landscapes → isometric 3D rooms → polished commercial product.

**Why these games:** Manic Miner is the Spectrum. Everyone who owned one either played it or typed it in. R-Type on the Spectrum proves the impossible — software pixel scrolling on hardware with no scroll registers. Knight Lore invented the isometric adventure genre on this machine. The capstone ships a product that could sit on a shop shelf next to Ocean and Ultimate releases.

### Commodore 64

**Killer feature:** The SID sound chip — three voices, filters, ring modulation. And hardware sprites.

| # | Genre | Inspired by | Units | Teaches |
|---|-------|------------|-------|---------|
| 1 | Wave-based space shooter | Katakis / Galaga | 128 | Sprites, SID sound effects, wave patterns, collision, power-ups |
| 2 | Stealth-puzzle | Impossible Mission | 256 | Large scrolling rooms, search mechanics, speech synthesis, SID atmosphere |
| 3 | Run 'n' gun | Turrican | 512 | 8-way scrolling, sprite multiplexing, grappling hook physics, vehicle sections |
| 4 | Capstone | Creatures / Mayhem in Monsterland | 512 | Fast loader, direct 1541 drive programming, demo-scene effects (FLD, DYCP), 6581/8580 detection, dual distribution (D64 + tape) |

**Visual journey:** sprites shooting on a starfield → atmospheric rooms with speech → Turrican-scale scrolling action → demo-scene polish and professional loading.

**Why these games:** Katakis is sprites + SID from frame one — the C64 doing what it does best. Impossible Mission is the machine at its most atmospheric ("Stay a while. Stay forever."). Turrican is the peak — everything the VIC-II and SID can do, combined. The capstone adds the craft that separated bedroom coders from commercial studios: fast loaders, demo-scene effects, and distribution on physical media.

### Nintendo Entertainment System

**Killer feature:** The PPU — tile-based graphics that make 52 colours look like millions.

| # | Genre | Inspired by | Units | Teaches |
|---|-------|------------|-------|---------|
| 1 | Scrolling platformer | Super Mario Bros | 128 | PPU setup, nametables, OAM sprites, scrolling, controller input, physics |
| 2 | Top-down adventure | Legend of Zelda | 256 | Screen transitions, inventory, combat, HUD, battery-backed SRAM saves |
| 3 | Metroidvania | Metroid / Castlevania III | 512 | MMC3 mapper, scanline counter, large connected world, ability gating, backtracking |
| 4 | Capstone | Late-era NES showcase | 512 | Advanced MMC3, CHR animation, DMC audio samples, NTSC/PAL compatibility |

**Visual journey:** scrolling platformer world → overworld with dungeons → massive interconnected map → everything the NES can do.

**Why these games:** Super Mario Bros defines the NES. The Legend of Zelda proves it's not just a platformer machine and introduces battery saves. Metroid shows what bank switching enables — a world too large for the cartridge to hold at once. The capstone pushes the hardware to Kirby's Adventure levels of visual and audio polish.

### Commodore Amiga

**Killer feature:** Three custom chips — Agnus (DMA, Copper, Blitter), Denise (video), Paula (audio, interrupts) — working in concert.

| # | Genre | Inspired by | Units | Teaches |
|---|-------|------------|-------|---------|
| 1 | Terrain puzzle | Lemmings | 128 | Blitter as game mechanic (dig = clear bits, build = set bits), Copper gradients, Paula samples |
| 2 | Parallax showcase | Shadow of the Beast | 256 | Dual playfield mode, multi-layer parallax, Copper per-line effects, hardware scrolling |
| 3 | Pseudo-3D racing | Lotus Turbo Challenge | 512 | Copper per-scanline road rendering, perspective maths, split-screen two-player, Paula engine sound |
| 4 | Capstone | OCS→AGA showcase | 512 | Chipset detection, AGA 256-colour modes, HAM8 title screens, custom disk loading, multi-disk support |

**Visual journey:** bitmap terrain with walking creatures → jaw-dropping parallax layers → pseudo-3D road with split-screen → AGA showcase bridging A500 to A1200.

**Why these games:** Lemmings makes the Blitter a game mechanic — you're not just using the hardware, you're playing with it. Shadow of the Beast made people buy Amigas; dual playfield parallax is the platform's visual signature. Lotus teaches Copper tricks and perspective maths that nothing else in the curriculum covers. The capstone bridges OCS/ECS to AGA, showing the same game running on an A500 and then lighting up on an A1200.

### Genres Reserved for Future Systems

The following genres are available and untouched:

Fighting game, beat 'em up, vertical shmup, turn-based RPG, action RPG, puzzle/falling blocks, racing (top-down), pinball, point-and-click adventure, top-down maze, rhythm/music game, top-down tactical, digging action-puzzle, pattern-action, sports, cinematic platformer, god game, real-time strategy, text adventure (assembly), snake/growth, territory control, droid-takeover, and more.

Future systems (Mega Drive, Atari ST, Game Boy, Master System, BBC Micro, and others) will draw from this pool following the same no-repetition rule.

---

## BASIC Gateway Track

### Purpose

Some platforms have an accessible high-level language that provides a gentler entry point before assembly. The BASIC track teaches programming fundamentals — variables, loops, conditionals, arrays, input handling — through games that are playable and complete.

BASIC games are **not simplified versions of the assembly games.** They are separate, smaller projects suited to the language's strengths and the platform's BASIC culture. They are also **not bound by the no-repetition rule** — the assembly and BASIC tracks serve different audiences with different goals.

### Which Platforms

| Platform | Language | Track? | Why |
|----------|----------|--------|-----|
| ZX Spectrum | Sinclair BASIC | Yes (1 track) | How everyone started. Type-in listings, text adventures, PRINT AT games. |
| Commodore 64 | BASIC V2 | Yes (1 track) | Famously limited, but historically important. POKE teaches memory-mapped I/O. |
| Amiga | AMOS + Blitz Basic | Yes (2 tracks) | AMOS: friendly, immediate, hobbyist. Blitz: compiled, fast, commercial (Worms, Skidmarks). |
| NES | None | No | No BASIC, no gateway. Assembly from the start. |

### Structure

Four games per track, 64 units each. Total per single-track platform: 256 units. The Amiga has two tracks (AMOS + Blitz) for 512 units total — the languages are different enough to justify both.

Each game should be completable in under 500 lines of BASIC/AMOS. Beyond that, the language becomes unwieldy and the learner should move to assembly.

| Slot | Units | Role |
|------|-------|------|
| Game 1 | 64 | **First program.** Immediate results. The game the platform's culture started with. |
| Game 2 | 64 | **Screen interaction.** Direct screen/memory manipulation. Moving things around. |
| Game 3 | 64 | **Hardware access.** Using the platform's unique hardware through BASIC. |
| Game 4 | 64 | **Polished result.** A complete game combining everything. Shows BASIC's limits. |

### BASIC Is Not a Prerequisite

The assembly curriculum assumes no BASIC knowledge. A learner starting at assembly Game 1 should not feel they have missed something by skipping BASIC. The two tracks are independent paths that happen to cover the same platform.

### Spectrum BASIC

Each platform's BASIC track starts where that platform's beginners actually started.

| # | Game | Teaches |
|---|------|---------|
| 1 | Text adventure | Strings, INPUT, IF/THEN, GOTO/GOSUB. The Spectrum text adventure tradition. |
| 2 | Chase game (PRINT AT) | Grid movement, game loop, simple AI. Magazine type-in style. |
| 3 | Drawing/puzzle game (PLOT, DRAW) | Graphics commands, arrays, colour via ATTR. |
| 4 | Action game with UDGs | User-defined graphics, collision, speed optimisation. Looks like a real type-in. |

### C64 BASIC V2

BASIC V2 has no graphics or sound commands. Everything is POKE. This is the lesson — and the bridge to understanding memory-mapped I/O.

| # | Game | Teaches |
|---|------|---------|
| 1 | Grid strategy game (Battleships / Minesweeper) | PRINT, INPUT, arrays, RND. A real game from line 1, no POKE needed. |
| 2 | Character grid action game | POKE to screen/colour RAM, PEEK for collision. Maze or chase game. |
| 3 | Sprite game | VIC-II sprite registers via POKE. The hard way — and the reason assembly exists. |
| 4 | Music + game | SID registers via POKE. Sound and gameplay combined. |

### AMOS (Amiga)

AMOS exposes Amiga hardware through BASIC commands. BOBs, Copper effects, MOD playback — all accessible. The track progresses from immediate visual results to hardware-aware game design.

| # | Game | Teaches |
|---|------|---------|
| 1 | Bouncing sprites game | BOB commands, movement, collision. AMOS's strength: things on screen immediately. |
| 2 | Mouse-driven game | Point, click, drag. The Amiga has a mouse — use it. |
| 3 | Scrolling game | Hardware scroll commands, parallax. AMOS exposes these directly. |
| 4 | Full game with MOD music | Sample playback, menus, multiple screens. Polished result. |

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

The four primary platforms (Spectrum, C64, NES, Amiga) each have four assembly games. Future systems follow the same model but may vary in size:

| Platform Complexity | Assembly Games | Examples |
|---------------------|---------------|----------|
| Minimal | 2 | ZX81, VIC-20, Atari 2600 |
| Standard | 4 | Mega Drive, Atari ST, Game Boy, Master System, BBC Micro |
| Extended | 4-6 | Systems with unusual depth or multiple distinct modes |

Future platforms may draw from the reserved genre pool or revisit genres already used by the primary four, where the hardware teaches genuinely different lessons. A Game Boy platformer and a Spectrum platformer are different enough to coexist — the constraint is about avoiding lazy repetition, not mechanical enforcement.

BASIC gateway tracks are added only when the platform has a historically significant high-level language (BBC BASIC, MSX BASIC, etc.).

---

## Platform Curriculum Files

This specification defines how curricula work. The actual game details live in platform-specific files:

- `/docs/curriculum/assembly/sinclair-zx-spectrum/sinclair-zx-spectrum-curriculum.md`
- `/docs/curriculum/assembly/commodore-64/commodore-64-curriculum.md`
- `/docs/curriculum/assembly/nintendo-nes/nintendo-nes-curriculum.md`
- `/docs/curriculum/assembly/commodore-amiga/commodore-amiga-curriculum.md`

Each platform curriculum file contains:

1. **Platform overview** — the platform's killer feature and teaching focus
2. **Game sequence** — the four assembly games with descriptions
3. **Game details** — for each game: genre, inspiration, unit count, skills taught, phase names
4. **BASIC gateway** (if applicable) — the four BASIC games

Platform curriculum files should be concise. They list what exists, not why the model works — that's this document's job.

---

## Version History

- **3.0 (2026-03-09):** Major restructure. Reduced from 16 to 4 assembly games per primary platform. Introduced no-repetition rule across platforms. Every game inspired by a real commercial release. BASIC gateway expanded from 1-2 to 4 games per platform. Real hardware compatibility made a baseline requirement, not a capstone feature. Removed physical cartridge/media production from scope.
- **2.1 (2026-01-19):** Added Standalone Technique Examples section (three-level model: units → standalone demos → patterns).
- **2.0 (2025-11-25):** Complete rewrite. Replaced phases/tiers/lessons model with games model.
- **1.0 (2025-01-15):** Original specification using 4,096 lessons per platform.
