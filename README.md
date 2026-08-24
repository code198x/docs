# Code Like It's 198x - Documentation

This repository contains curriculum specifications, platform references, and content creation workflows for the Code Like It's 198x project.

## What Is This Project?

Code Like It's 198x teaches **retro raster-era hardware-craft game development through the canon**. Learners build real games on vintage platforms using the same techniques developers used in the 1980s and 1990s. Every game in the curriculum is inspired by canonical traditions of the era but ships as its own original design.

All **four core platforms — ZX Spectrum, Commodore 64, NES, and Amiga** — ship a complete, finishable on-ramp for the October 2026 launch, each with its full coming-soon game lineup recorded and sequenced (the 2026 lineup replan). Further retro systems get per-system curriculum work when we reach each one.

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
│   ├── sinclair-zx-spectrum/       # Core (live): reference.md + language/ + games/
│   ├── commodore-64/               # Core (live): reference.md + games/
│   ├── commodore-amiga/            # Core (live): reference.md + games/
│   └── nintendo-entertainment-system/  # Core (live): reference.md + games/
│
# Only the four core systems have docs. Others get per-system docs when work
# begins on each. Lineups + state are the website catalogues
# (website/src/content/modules/); rationale is a per-track record under decisions/.
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

**State is the website catalogue** (`website/src/content/modules/<platform>/<track>.yaml` `status:`), not this table — see [State lives in the catalogues](decisions/state-lives-in-catalogues.md). Each core track ships a **live, finishable on-ramp** for the October 2026 launch; the rest of each lineup is recorded and coming-soon.

### Core platforms — assembly

| Platform | CPU | On-ramp (live) | Lineup record |
|----------|-----|----------------|---------------|
| ZX Spectrum | Z80 | Meet the Machine · Gloaming · Shadowkeep Arc 1 | [gentle ramp](decisions/spectrum-assembly-gentle-ramp.md) — 10-game rendering ladder |
| Commodore 64 | 6510 | Meet the Machine · Starfield | [C64 assembly lineup](decisions/c64-assembly-lineup.md) — VIC-II / 6502 ladder |
| NES | 6502 | Meet the Machine | [NES assembly lineup](decisions/nes-assembly-lineup.md) — PPU / 6502 ladder; Dash |
| Amiga | 68000 | Meet the Machine | [Amiga assembly lineup](decisions/amiga-assembly-lineup.md) — custom-chip ladder; Exodus |

### Core platforms — BASIC

| Platform | Language | On-ramp (live) | Lineup record |
|----------|----------|----------------|---------------|
| ZX Spectrum | Sinclair BASIC | 17 games (Volume 1 complete, V2 in progress) | [Spectrum BASIC lineup](decisions/spectrum-basic-lineup.md) |
| Commodore 64 | BASIC V2 | Meet C64 BASIC · 8 First Programs | [Volumes 2–4](decisions/c64-basic-volumes-2-4.md) |
| Amiga | AMOS / Blitz | Meet AMOS · Meet Blitz | [AMOS + Blitz](decisions/amiga-basic-amos-and-blitz.md) — peer paths |

### Beyond the core four

Platforms outside the core four get per-system docs when work begins on each. Next-wave targets are in [decisions/next-tier-first-wave.md](decisions/next-tier-first-wave.md); the wider roadmap is in [tracker/future-expansion-tracks.md](tracker/future-expansion-tracks.md).


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

## Citations to the primary reference library

Paths written as `reference/by-system/...` refer to the project's **primary
source library** — the manuals, datasheets, magazines and service documentation
that hardware facts here are distilled from.

That library is **not public, and will not be made public.** It holds
third-party material the project may hold for reference but may not
redistribute: manufacturer documentation, book and magazine scans, and mirrored
community sites. Keeping it private is what makes holding it legitimate.

These citations are therefore **provenance records, not links.** They name which
document a fact came from so the claim is traceable and auditable, and so a
reader can seek out the same source independently. The facts themselves are
freely reusable — facts are not copyrightable, and this repository is openly
licensed.
