# Decision: An NES "Meet the Machine" primer as a console-generalisation probe

> **STATUS: Accepted 2026-06-08.** Build a Nintendo Entertainment System
> "Meet the Machine" assembly primer (module 0) — **primer only, not the
> Nightshade flagship.** Its purpose is to prove the gentle-ramp curriculum
> generalises from home computers to a **cartridge console**, the one platform
> family it hasn't been tested on.

## Relationship to the launch spec (the broader rule it bends)

[october-2026-launch-spec.md](october-2026-launch-spec.md) (2026-06-03 amendment)
says focus is **sequenced, not widened** — Spectrum + C64 are the two committed
platforms; NES and Amiga defer wholesale. This decision is a **deliberate, scoped
exception, not a reversal**:

- It is **post-launch work** — it does not touch the October critical path, which
  is already healthy (Spectrum assembly + BASIC V1/V2 done; C64 assembly opening
  done; C64 BASIC V1 shipped *beyond* the C64 commitment).
- It is **primer-scope only.** NES does **not** become a third launch platform.
  The Nightshade flagship and the rest of the NES lineup stay deferred /
  coming-soon, exactly as before.

## Why NES, why now, why only the primer

- **The CPU transfers for free.** The NES 2A03 is the same 6502 family as the
  C64's 6510. The just-shipped C64 primer's CPU half — registers, addressing,
  branches, `ADC`/`SBC`, the stack, 16-bit-by-hand — carries over almost
  wholesale. This is the cheapest on-ramp to any new platform we will ever get,
  and a live demonstration of the Asm198x/ISA thesis: *cover a CPU once, light up
  every machine that uses it.*
- **It tests the real open question.** Everything shipped is home computers. A
  console's *machine half* is genuinely different — graphics live behind the PPU
  (VBlank-gated, not directly addressable), colour is palettes + attribute
  tables, updates run from the NMI, tile shapes come from CHR ROM. Whether the
  one-idea-per-unit ramp survives that ceremony is precisely what
  [methodology-generalisation](../tracker/methodology-generalisation-survey.md)
  asks. The primer answers it at low cost.

## The key design choice (the generalisation finding)

The NES has no two-line "first visible win" — the simplest result (fill the
screen with a colour by writing palette `$3F00`) sits behind the iNES header,
reset vector, and PPU warm-up. The ramp is preserved by providing that ceremony
as a **typed-once harness / black box that later units open up** — the same
pattern the C64 primer used for the BASIC `SYS` stub and the "stage light"
colour write, and the commercial-bar "scaffold you don't understand yet" pattern.
Each unit then makes *one meaningful change* on top of the harness. **The finding
the probe produces:** the methodology generalises to consoles, but leans harder
on the provided-harness scaffold because the machine demands ceremony the home
computer didn't.

## Scope

~15 units (count flexes at authoring time, per
[curriculum-structure.md](curriculum-structure.md)), adapting the C64 primer
spine: the CPU half maps near 1:1; the machine half (PPU window, palettes +
attributes, controller at `$4016`, the NMI/VBlank model, CHR pattern tables) is
re-authored for the console. Toolchain: `ca65` + `ld65 -C nes.cfg`
(`code198x/nintendo-entertainment-system` image), NROM. Status is tracked only in
the catalogue per [state-lives-in-catalogues.md](state-lives-in-catalogues.md).

## Outcome (shipped 2026-06-08)

The probe shipped at **17 units** — the C64 primer's 15 plus **two net-new units
the console demanded**: *Where the Shapes Come From* (CHR pattern tables — the
C64 leans on a ROM font, the NES makes you draw the atom) and *The Machine Has a
Heartbeat* (the NMI/VBlank frame loop — a home computer has no equivalent). The
finding the probe set out to produce, confirmed concretely:

- **The CPU half transferred almost verbatim.** Units 1–4, 8, 11–17 (registers,
  bytes, memory, test-and-branch, indexing, loop, stack, arithmetic, bits,
  16-bit, the no-safety-net mindset) re-skinned from the C64 primer with only the
  output path changed — the same 6502.
- **The machine half is where the methodology had to bend, and it held.** The
  gentle ramp survived by leaning harder on the **provided-harness scaffold**: a
  stable, warning-free harness (iNES header + reset + PPU warm-up + a font in CHR)
  with a fall-through tail that paints whatever colour the unit leaves in `A`.
  Units 5–7 then *open the harness up* one panel at a time (PPU window → palette →
  CHR), exactly the "scaffold you don't understand yet" pattern, and `jsr` stayed
  a clean unit-13 reveal because the harness needed no subroutine.
- **Every unit kept one idea + one verified on-screen result**, captured
  headlessly through `emu198x-nes --script` (including the NMI heartbeat proven by
  two differing frames, and the joypad proven with a scripted button-hold).

Net: the methodology generalises to a cartridge console, at the cost of ~2 extra
units of ceremony and a heavier reliance on the typed-once harness — which is the
honest price of a machine that gives you nothing for free.
