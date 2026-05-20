# Commodore 64 Track — Lightweight Skeleton

**STATUS: Post-October work, lightweight only.** Per `docs/decisions/october-2026-launch-spec.md`, C64 / Cadence is deferred. This skeleton is *no-commit* — North Star, volume themes, candidate game lineup only. No per-game scope, no naming lock-in, no tech-tree detail. The Spectrum Assembly methodology (per [`decisions/spectrum-assembly-track.md`](../decisions/spectrum-assembly-track.md)) is build-untested; this skeleton awaits Spectrum's first shipped games for validation before becoming a full track structure.

Captured 2026-05-19 alongside [nes-track-skeleton.md](nes-track-skeleton.md) and [amiga-track-skeleton.md](amiga-track-skeleton.md) for cross-platform methodology check.

## North Star

The C64 teaches the *commercial 8-bit game in its fullest form*. Where Spectrum taught what you can do with bytes, attribute clash, and a beeper, **C64 teaches what you can do when the hardware is *generous***: 8 hardware sprites, true multi-color graphics, a 3-voice SID synthesiser with filters and envelopes, raster interrupts for split-screen tricks, and 64K to spend. The same legends crossed both platforms (Crow, Braybrook at Hewson; later Smith, Galway, Hubbard) but C64's design vocabulary is *different*. Hardware sprites change masking and Y-sort. SID is a completely different audio paradigm from beeper or AY. Multi-color graphics change pixel-art constraints. Disk loading replaces tape conventions.

Cadence (Game 1, concept locked per [revamp.md](revamp.md)) is the canonical demonstration.

## Volume themes (working-draft)

| Volume | Theme | What it teaches |
|--------|-------|-----------------|
| **V1** *The Hardware Speaks* | Foundational | Hardware sprites, SID basics, raster — what makes the C64 not-a-Spectrum |
| **V2** *Speed and Density* | Real-time arcade | Uridium / Hewson tradition — smooth scrolling, dense art |
| **V3** *The Multi-color World* | Visual mastery | IK+ / Last Ninja / Cinemaware presentation |
| **V4** *Systems and Stories* | Depth | Paradroid / Impossible Mission / RPG / strategy |

## Candidate games (~16, working-draft)

Names are stand-ins for inspired-by-not-clones renames. Canonical references named for tradition only; per-game design follows after Spectrum validates the methodology.

| # | Working name / placeholder | Canonical tradition |
|---|----------------------------|---------------------|
| 1 | **Cadence** (concept locked) | TBD per concept doc |
| 2 | [Hover-Droid Action] | Paradroid (Braybrook / Hewson 1985) |
| 3 | [Cave Physics] | Boulder Dash C64 |
| 4 | [Power-Up Shooter] | Wizball (Sensible / Hewson 1987) |
| 5 | [Smooth-Scroll Shooter] | Uridium (Braybrook / Hewson 1986) |
| 6 | [Iso Adventure-Combat] | The Last Ninja (System 3 1987) |
| 7 | [Beat-em-up] | IK+ (Maclean / System 3 1987) |
| 8 | [Cinematic Strategy] | Defender of the Crown (Cinemaware 1986) |
| 9 | [Exploration Platformer] | Impossible Mission (Epyx 1984) |
| 10 | [Action Platformer] | Turrican (Trenz / Rainbow Arts 1990) |
| 11 | [3D Strategic] | The Sentinel (Crammond 1986) |
| 12 | [Point-and-Click Adventure] | Maniac Mansion (LucasArts 1987) |
| 13 | [Single-Screen Platformer] | Pitfall II (Activision 1984) |
| 14 | [Atmospheric Horror-Action] | Forbidden Forest (Cosmi 1983) |
| 15 | [Trading / Space] | Elite C64 port (1985) |
| 16 | [Economic Sim] | M.U.L.E. (Ozark 1983) |

Plus possible additions: Pinball Construction Set (Budge), Cauldron II C64, Bruce Lee (Datasoft), Aztec Challenge (Cosmi).

## Methodology generalisation check (Spectrum → C64)

| Spectrum element | Translates to C64? |
|------------------|---------------------|
| **Trunk Layers 1-4** (foundations / sprite / world / inhabitants) | Yes, with hardware-sprite caveat — Layer 2 (The Sprite) teaches hardware sprites first, software sprites secondarily |
| **Branch A** (Adventure Depth) | Yes — Last Ninja, Impossible Mission, RPGs |
| **Branch B** (Platformer) | Yes — Turrican, Bruce Lee, Pitfall II |
| **Branch C** (Scrolling and Density) | Yes — C64 has hardware scrolling, different teaching |
| **Branch D** (Real-World Sim) | Yes — sport/sim games |
| **Branch E** (True 3D) | Yes — Elite, Sentinel, Mercenary |
| **Branch F** (Cross-cutting Specials) | Yes — parser, iso, procedural |
| **Branch G** (Audio Hardware) | **Different content** — SID replaces AY+128K. Would be a C64-specific Branch G (or "Branch G: SID"). |
| **Three cross-cutting axes** (Design / Engineering Practices / Production Craft) | Yes; Engineering Practices content is 6502-specific (different from Z80 LDIR/T-state idioms) |
| **Layer model (L0 / L+1 / L+3 / L+4)** | Different — C64 has no native-vs-128K layer split. Possible L+1 = REU expansion / cartridge variants. L+4 (Next equivalent) = C64 Reloaded / Mini, C128 variants |
| **Naming convention (inspired-by, not clones)** | Yes — applies universally |
| **Tier hierarchy** | Yes — tier per platform |

**Methodology generalises conceptually; content per axis is C64-specific.** No major framework gaps; the structure transfers. Per-platform variation lives in Branch G (audio), Engineering Practices (CPU), and layer model (no L+1 128K parallel exists).

## What this skeleton does NOT commit to

- Per-game scope / unit budget
- Final naming (the placeholders are stand-ins)
- Tech-tree per-game position
- Cross-game prerequisite seeding
- Cut hierarchy
- Build order or timeline

These follow after Spectrum's first games ship and the methodology is build-validated.

## Status

Skeleton — captured 2026-05-19. Post-October work. No commitment. Awaits Spectrum methodology validation (post Shadowkeep Arc 1 ship, ~Aug 2026 at earliest) before becoming a full track structure document.
