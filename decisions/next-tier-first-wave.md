# Decision: the "next" tier — first wave (six machines)

> **STATUS: Accepted 2026-06-10.** Promotes six machines from `planned` to
> `next` in the systems data (`website/src/content/systems/*.yaml`). "Next" =
> **committed to bring to the on-ramp bar after the core four**, distinct from
> `planned` (real page, no commitment) and `edge` (harder to teach).

## The six

| Machine | CPU | Why | Reach | Emu198x core |
|---|---|---|---|---|
| Amstrad CPC | Z80 | UK + huge in France/Spain; strong demoscene | UK/FR/ES | **needs building** |
| MSX | Z80 | The international standard; massive homebrew | JP/Brazil/ES/ME | ✅ `machine-msx` |
| BBC Micro | 6502 | Education icon (apt for us); pivotal | UK | ✅ `machine-acorn-bbc-micro` |
| Commodore VIC-20 | 6502 | The C64's predecessor; shares tooling | US/UK | ✅ `machine-commodore-vic-20` |
| Sega Master System | Z80 | Adds a *console*; big in Europe + Brazil | EU/Brazil | ✅ `machine-sega-master-system` |
| Atari ST | 68000 | The Amiga's sibling/rival; music & Europe | US/EU | **needs building** |

## Why these

- **CPU leverage (compounding).** All six reuse a CPU we already teach — Z80
  (Spectrum), 6502 (C64/NES), 68000 (Amiga). Asm198x is CPU-keyed (cover a CPU,
  every machine using it lights up) and Emu198x cores are per-chip, so this is
  the cheapest, highest-quality expansion: zero new CPUs.
- **Diversity.** Real geographic spread (UK, France, Spain, Japan, Brazil) and a
  console (Master System) alongside home computers — serving the project's
  cultural/geographic scope axis, not just the Anglosphere.

## "Next" is emulation-gated, not just curriculum

A machine is only genuinely "next-ready" when there is a **capture-ready Emu198x
core** for it — the curriculum is authored *against* the emulator (headless
type → run → capture). So promoting to `next` carries an Emu198x dependency:

- **Cores exist (4):** MSX, BBC Micro, VIC-20, Master System — but existence ≠
  capture-ready; each needs a **maturity check** (boots, runs a typed program,
  screenshots/video clean) before curriculum work starts.
- **Cores to build (2):** **Amstrad CPC** and **Atari ST**. (ST is 68000, so it
  leverages the Amiga work, but its own chips — Shifter, MMU, MFP — are new.)

This is **Emu198x-session work**, tracked from the Launch board but executed in
the Emu198x project, not Code198x.

## Second wave (still `planned` for now)

Iconic but more work or a new CPU — promote later: **Nintendo Game Boy**
(handheld, Sharp LR35902), **Sega Mega Drive** (68000 console), **Acorn
Archimedes** (first ARM machine), **Sharp X68000** (68000, cult Japanese).

## Drift triggers

- **Promoting a machine to `next` without an Emu198x-core plan.** Curriculum
  readiness alone isn't "next" — the capture pipeline needs the core. Pair every
  `next` promotion with its emulation-readiness status.
- **Widening `next` for novelty over leverage.** Prefer machines that reuse a CPU
  we teach (Z80/6502/68000) before ones that need a new core, unless the cultural
  case is overwhelming.
