# Decision: An Amiga "Meet the Machine" assembly primer — completing the four foundations

> **STATUS: Accepted 2026-06-08.** Build a Commodore Amiga "Meet the Machine"
> 68000 assembly primer (module 0), so all four launch-family machines
> (Spectrum, C64, NES, Amiga) have the same gentle assembly on-ramp. The
> capture pipeline is de-risked and proven; unit 1 ships.

## Relationship to the launch spec (the rule it bends)

[october-2026-launch-spec.md](october-2026-launch-spec.md) says focus is
**sequenced, not widened** — Spectrum + C64 committed; NES and Amiga defer. The
NES primer was the first recorded scoped exception
([nes-primer-generalisation-probe.md](nes-primer-generalisation-probe.md)). This
is the **second, and a deliberate one**: with it we consciously decide to build
**all four assembly foundations** rather than drift there. It is post-launch
work — it does not touch the October critical path (Spectrum + C64), which is
healthy.

## Why the Amiga, why now

- **It completes the on-ramp set.** Spectrum, C64 and NES each have a "Meet the
  Machine" assembly primer. The Amiga was the only featured machine a learner
  couldn't start on. Four foundations = a real entry point on every featured
  machine, and the Amiga earns its way from `next` to `live` on merit.
- **It is the hardest generalisation test, and the most valuable.** The 68000 is
  a 16/32-bit CPU with a different instruction set and a far larger register
  file; the machine is a custom-chip architecture (Copper, bitplanes, Blitter,
  Paula). If the gentle, one-idea-per-unit ramp survives *this*, the methodology
  is proven across 8-bit home computer, 8-bit console, and 16-bit custom-chip
  workstation-class hardware — every architecture class the curriculum spans.

## The de-risk (done 2026-06-08)

Before authoring, the full pipeline was proven end-to-end:
`vasm` → hunkexe → `xdftool` bootable ADF → `emu198x-amiga --headless --disk`
→ headless screenshot → Read-verify. Confirmed with both an existing program
(the Exodus copper landscape) and a hand-written minimal harness (a red screen).
Kickstart ROMs live in `~/.emu198x/roms/commodore-amiga` (not the stale
`Reference/` path the docs named). The one extra step over the NES — mastering a
bootable ADF — is already wrapped in per-unit `Makefile`s and the
`build-amiga-adf` skill, so a unit's loop is `make` → capture.

## The expected finding (the divergence)

Unlike the NES (whose CPU half re-skinned almost verbatim from the C64 — same
6502), the Amiga primer **re-authors the most of any of the four**: the 68000
CPU half is written from scratch (MOVE, data sizes `.b/.w/.l`, the D0–D7 / A0–A7
register file — none of it transfers at the instruction level), and the machine
half is the custom chipset (the bitmap screen, the Copper, the Blitter). The
*shape* of the ramp holds; the content is new. That cost is the finding, now
measured rather than guessed.

## Scope

~16 units (count flexes), four phases: **what the machine is** (toolchain, MOVE,
sizes, the register file, memory, the bitmap screen, colour + the Copper);
**what it can do** (decisions, input, pointers, counted loops, subroutines);
**rounding out** (arithmetic, bits, the Blitter); **the mindset** (no OS, no
safety net). Toolchain: `vasm` + `xdftool` (`commodore-amiga` image, tagged
`amiga-dev`), captured by `emu198x-amiga`. Status lives only in the catalogue per
[state-lives-in-catalogues.md](state-lives-in-catalogues.md); readiness on the
fleet flips `next → live` when the primer is shippable, per
[system-readiness-lives-in-tier.md](system-readiness-lives-in-tier.md).

## Notes for the future

- **A multi-language Amiga.** Assembly is first, but the Amiga is intended to get
  the richest language story of the family: **AMOS** (its accessible BASIC, with
  François Lionet's offer of help — a more involved toolchain path), **Blitz
  BASIC** (a compiled BASIC module), and **C** (later, via a vbcc/SAS-style
  path). The 8-bit machines lead with BASIC + assembly; the Amiga eventually
  spans four languages.
- **The existing material is not an anchor.** The in-progress Exodus / Signal
  assembly games predate the higher content bar. As with Spectrum and C64, they
  will be re-evaluated and likely rewritten to the new bar; the primer sets that
  bar, and is not constrained by the old game structure.
- **Sound should reach the other assembly primers too.** The Amiga primer is the
  first assembly "Meet the Machine" to teach sound (Paula, unit 18) — the
  Spectrum / C64 / NES primers teach none (sound currently lives only in the
  BASIC courses and the games). Once Paula lands, revisit retrofitting a gentle
  sound unit (Spectrum beeper, C64 SID, NES APU) into those three so all four
  are consistent. Audio is verified by `--audio-capture`, not a screenshot.
