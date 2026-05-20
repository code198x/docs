# Code Like It's 198x - Documentation

This repository contains curriculum specifications, platform references, and content creation workflows for the Code Like It's 198x project.

## What Is This Project?

Code Like It's 198x teaches **retro raster-era hardware-craft game development through the canon**. Learners build real games on vintage platforms using the same techniques developers used in the 1980s and 1990s. Every game in the curriculum is inspired by canonical traditions of the era but ships as its own original design.

The methodology is being established on the **ZX Spectrum** first — Shadowkeep (assembly) and Volume 1 of the BASIC track ship for the October 2026 launch. **Commodore 64, NES, and Amiga** are the next three platforms to come online once the Spectrum spine is validated, with twelve further retro systems mapped as pre-methodology drafts.

No emulation wrappers. No modern engines. No high-level languages. Direct hardware access, assembly language, and the satisfaction of making a 40-year-old machine do something impressive.

## What this is, and what it isn't

Code Like It's 198x is a **bounded craft tradition**, not a universal games-development curriculum.

**This is:** retro raster-era hardware-craft game development through the canon. 8-16-bit-era home computers and consoles. Raster-display, framebuffer-based, hardware-constrained, single-machine programming. Cartridge / disk / tape media. Approximately 1977-1995.

**This isn't:** modern engine-mediated development (Unity / Unreal / Godot). Mobile or Steam-era indie. 3D-first hardware (PlayStation / N64 and beyond). Vector-display tradition (Vectrex). Cloud / always-online / live-service game development.

The methodology was developed for Spectrum, C64, NES, and Amiga, and generalises cleanly across 11+ retro platforms (Apple II, Atari 8-bit, Game Boy, SNES, Sega Master System, Mega Drive, BBC Micro, Dragon). It strains at the edges — Atari 2600 at the earliest, PSX/N64 at the latest — and breaks honestly outside its domain. Real boundaries are a feature. Within them, the curriculum teaches a defined craft tradition with depth and rigour.

## How The Curriculum Works

Each platform has a sequence of games, ordered by complexity:

- **Games** are complete, playable projects (8-80+ units each, depending on canonical depth)
- **Units** are 60-120 minute sessions producing working results
- **Skills compound** through the sequence — Game 1 teaches fundamentals, later games produce commercial-quality work
- **Inspired-by-not-clones** — every game references a canonical tradition (Atic Atac, Manic Miner, Elite, Lords of Midnight, etc.) but ships as its own design with its own name and identity

See [specifications/curriculum.md](specifications/curriculum.md) for the full model.

## Repository Structure

```
docs/
├── platforms/                      # System-first: each platform has its world here
│   ├── sinclair-zx-spectrum/       # Active: reference.md + assembly.md + basic.md + games/
│   ├── commodore-64/               # Deferred Game 1: reference.md + *-skeleton.md
│   ├── commodore-amiga/            # Deferred Game 1: reference.md + *-skeleton.md
│   ├── nintendo-entertainment-system/  # Deferred Game 1: reference.md + assembly-skeleton.md
│   └── {12 far-future platforms}/  # Pre-methodology drafts (assembly-skeleton.md)
│
├── decisions/                      # Binding policy records (~17 files)
├── specifications/                 # Cross-cutting format/structure specs
├── tracker/                        # Live state, plans, status
├── infrastructure/                 # Docker, capture pipeline, Astro, investigation briefs
├── emulators/                      # Emulator references
├── vault/                          # Encyclopedia (people / companies / games / techniques)
├── log.md                          # Append-only event log
└── index.md                        # Top-level navigation map
```

See [index.md](index.md) for a full file-by-file map.

## Key Documents

| Document | Purpose |
|----------|---------|
| [specifications/curriculum.md](specifications/curriculum.md) | The games model, unit structure, pedagogical approach |
| [specifications/unit.md](specifications/unit.md) | Technical formatting for unit files |
| [specifications/vault.md](specifications/vault.md) | Encyclopedia of people, companies, games, techniques |
| [specifications/pattern-library.md](specifications/pattern-library.md) | Reusable code patterns by platform |
| [specifications/content-creation-workflow.md](specifications/content-creation-workflow.md) | End-to-end content creation process |

## Platform Status

### Assembly Curricula

| Platform | Language | Status |
|----------|----------|--------|
| ZX Spectrum | Z80 | **Active.** [44 entries / 6 volumes / ~2,396 units](decisions/spectrum-assembly-track.md). Shadowkeep (Game 1) commits 64 units across 4 arcs; **Arcs 1-2 ship October 2026**. See [platforms/sinclair-zx-spectrum/assembly.md](platforms/sinclair-zx-spectrum/assembly.md). |
| Commodore 64 | 6510 | **Deferred post-October.** Lightweight skeleton at [platforms/commodore-64/assembly-skeleton.md](platforms/commodore-64/assembly-skeleton.md). Awaits Spectrum methodology validation. |
| NES | 6502 | **Deferred post-October.** Lightweight skeleton at [platforms/nintendo-entertainment-system/assembly-skeleton.md](platforms/nintendo-entertainment-system/assembly-skeleton.md). |
| Amiga | 68000 | **Deferred post-October.** Lightweight skeleton at [platforms/commodore-amiga/assembly-skeleton.md](platforms/commodore-amiga/assembly-skeleton.md). |

### BASIC Gateway Curricula

| Platform | Language | Status |
|----------|----------|--------|
| ZX Spectrum | Sinclair BASIC | **Active.** [32 games / 4 volumes](platforms/sinclair-zx-spectrum/basic.md), v6.4 inspired-by-not-clones names. **Volume 1 (8 games) ships October 2026.** |
| Commodore 64 | BASIC V2 | **Pre-methodology draft.** [platforms/commodore-64/basic-skeleton.md](platforms/commodore-64/basic-skeleton.md). |
| Amiga | AMOS/Blitz BASIC | **Pre-methodology draft.** [platforms/commodore-amiga/basic-skeleton.md](platforms/commodore-amiga/basic-skeleton.md). |
| BBC Micro | BBC BASIC | **Pre-methodology draft.** [platforms/bbc-micro/basic-skeleton.md](platforms/bbc-micro/basic-skeleton.md). |
| Amstrad CPC | Locomotive BASIC | **Pre-methodology draft.** [platforms/amstrad-cpc/basic-skeleton.md](platforms/amstrad-cpc/basic-skeleton.md). |
| MSX | MSX BASIC | **Pre-methodology draft.** [platforms/msx/basic-skeleton.md](platforms/msx/basic-skeleton.md). |
| Atari ST | STOS/GFA BASIC | **Pre-methodology draft.** [platforms/atari-st/basic-skeleton.md](platforms/atari-st/basic-skeleton.md). |

### Far-future platforms

Twelve additional platforms have pre-methodology assembly drafts under `platforms/{system}/assembly-skeleton.md` — Acorn Archimedes, Amstrad CPC, Atari 8-bit, Atari ST, BBC Micro, Game Boy, MSX, Sega Master System, Sega Mega Drive, SNES, TurboGrafx-16, Vectrex. All await Spectrum methodology validation before any methodology investment.

The methodology has been pressure-tested for generalisation — see [tracker/methodology-generalisation-survey.md](tracker/methodology-generalisation-survey.md) for the full check (11 systems clean, 2 strain at edges, 2 break honestly outside domain). Coverage strategy and tier commitment in [tracker/coverage-strategy.md](tracker/coverage-strategy.md).

## Related Repositories

This documentation repository is one of three:

- **docs** (this repo) - Specifications and references
- **website** - Astro site serving the curriculum
- **code-samples** - Compiled, tested code for each unit

## Contributing

All units must:

1. Align with the curriculum specification
2. Compile and run on the target platform
3. Include verified screenshots
4. Use British English (except "program" for computer programs)

See [specifications/content-creation-workflow.md](specifications/content-creation-workflow.md) for the full process.
