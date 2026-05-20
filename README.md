# Code Like It's 198x - Documentation

This repository contains curriculum specifications, platform references, and content creation workflows for the Code Like It's 198x project.

## What Is This Project?

Code Like It's 198x teaches **retro raster-era hardware-craft game development through the canon**. Learners build real games on vintage platforms — Commodore 64, ZX Spectrum, Amiga, NES — using the same techniques developers used in the 1980s and 1990s. Every game in the curriculum is inspired by canonical traditions of the era but ships as its own original design.

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
/
├── curriculum/                    # Game sequences and curricula
│   ├── commodore-64-curriculum.md
│   ├── sinclair-zx-spectrum-curriculum.md
│   ├── commodore-amiga-curriculum.md
│   ├── nintendo-nes-curriculum.md
│   ├── assembly/                  # Future platform assembly stubs
│   │   ├── sega-mega-drive/
│   │   ├── atari-st/
│   │   ├── bbc-micro/
│   │   └── ...
│   ├── basic/                     # BASIC curricula and stubs
│   │   ├── commodore-64/
│   │   ├── sinclair-zx-spectrum/
│   │   ├── commodore-amiga/
│   │   ├── bbc-micro/
│   │   └── ...
│   ├── patterns/                  # Reusable code patterns
│   └── reference/                 # Planning and reference docs
│
├── platforms/                     # Platform-specific references
│   ├── commodore-64/              # Hardware refs, quick guides
│   ├── sinclair-zx-spectrum/
│   ├── commodore-amiga/
│   └── nintendo-entertainment-system/
│
├── specifications/
│   ├── curriculum.md               # How curricula work
│   ├── unit.md                     # How to format unit files
│   ├── brief.md                    # Per-game brief format
│   ├── pattern-library.md          # Pattern library structure
│   ├── vault.md                    # Vault entry structure
│   ├── information-architecture.md
│   └── content-creation-workflow.md
├── decisions/                      # Binding decision records
├── infrastructure/                 # Docker, capture pipeline, Astro
├── log.md                          # Append-only event log
└── index.md                        # Top-level navigation
```

## Key Documents

| Document | Purpose |
|----------|---------|
| [specifications/curriculum.md](specifications/curriculum.md) | The games model, unit structure, pedagogical approach |
| [specifications/unit.md](specifications/unit.md) | Technical formatting for unit files |
| [specifications/vault.md](specifications/vault.md) | Encyclopedia of people, companies, games, techniques |
| [specifications/pattern-library.md](specifications/pattern-library.md) | Reusable code patterns by platform |
| [specifications/content-creation-workflow.md](specifications/content-creation-workflow.md) | End-to-end content creation process |

## Platform Status

### Assembly Curricula (Main)

| Platform | Language | Curriculum | Status |
|----------|----------|------------|--------|
| ZX Spectrum | Z80 Assembly | [44 entries / 6 volumes / ~2,396 units](decisions/spectrum-assembly-track.md) | v0.3 track structure locked; Shadowkeep (Game 1) commits 64 units across 4 arcs; **Arcs 1-2 ship October 2026** |
| Commodore 64 | 6510 Assembly | [16 games, ~1,536 units](curriculum/commodore-64-curriculum.md) | Game sequence defined; pre-methodology (concept locked) |
| NES | 6502 Assembly | [16 games, ~1,536 units](curriculum/nintendo-nes-curriculum.md) | Game sequence defined; pre-methodology (concept locked) |
| Amiga | 68000 Assembly | [16 games, ~2,048 units](curriculum/commodore-amiga-curriculum.md) | Game sequence defined; pre-methodology (concept locked) |

### BASIC Gateway Curricula (Optional)

| Platform | Language | Curriculum | Status |
|----------|----------|------------|--------|
| ZX Spectrum | Sinclair BASIC | [32 games / 4 volumes](curriculum/basic/sinclair-zx-spectrum/) | v6.4 lineup (11 games renamed under inspired-by-not-clones convention); **Volume 1 (8 games) ships October 2026** |
| Commodore 64 | BASIC V2 | [8 games, 512 units](curriculum/basic/commodore-64/) | Game sequence defined; pre-methodology |
| Amiga | AMOS/Blitz BASIC | [16 games](curriculum/basic/commodore-amiga/) | Game sequence defined; pre-methodology |

### Future Platforms (Stub Curricula)

Stub curricula have been created for future platforms. See:
- [curriculum/assembly/](curriculum/assembly/) - Assembly stubs (Mega Drive, Atari ST, BBC Micro, SNES, etc.)
- [curriculum/basic/](curriculum/basic/) - BASIC stubs (BBC BASIC, Locomotive, STOS/GFA, MSX-BASIC)
- [curriculum/reference/future-platforms-complete.md](curriculum/reference/future-platforms-complete.md) - Full platform roadmap

The methodology has been pressure-tested for generalisation across additional retro platforms — see [`docs/tracker/methodology-generalisation-survey.md`](tracker/methodology-generalisation-survey.md) for the full check (11 systems clean, 2 strain at edges, 2 break honestly outside domain). Future platform expansion remains post-October work and awaits Spectrum methodology validation through shipped games.

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
