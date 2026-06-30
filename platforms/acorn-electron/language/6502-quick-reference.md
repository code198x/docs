# 6502 Quick Reference (Acorn Electron)

**Purpose:** point to the shared 6502 reference and record the few
Electron-specific differences that matter when writing Electron assembly lessons.
**Audience:** curriculum designers writing Acorn Electron assembly lessons.

> **Scaffold doc.** The 6502 core and the MOS OS-call interface are the **same as
> the BBC Micro**, so they are not repeated here — this doc is a thin Electron
> overlay. TODOs mark depth still owed.

## The shared core — read the BBC doc

The Electron's CPU is the **MOS 6502A** — the same standard NMOS 6502 the BBC,
C64 and NES use. The instruction set, registers, addressing modes, instruction
groups, and the **MOS OS-call interface** (`OSWRCH`, `OSRDCH`, `OSBYTE`,
`OSWORD`, `OSCLI`, `OSFILE`, the `VDU` control codes, the `&`-for-hex convention,
and the minimal program shape) are documented once, in the BBC sibling:

→ [`../../bbc-micro/language/6502-quick-reference.md`](../../bbc-micro/language/6502-quick-reference.md)

Everything there applies to the Electron **except** the differences below. A
learner who has written BBC assembly already knows Electron assembly.

## What's different on the Electron

### Timing is MODE-dependent (and slower)

The instruction *encodings* and the per-instruction cycle *counts* are identical
to the BBC — but the wall-clock time those cycles take is not. The ULA contends
for RAM, so the effective CPU clock depends on the screen MODE (reference §Acorn
Electron Differences):

- **MODE 0–3:** effectively ~1 MHz (1 cycle ≈ 1 µs) — heavy contention.
- **MODE 4–7:** effectively ~2 MHz (1 cycle ≈ 0.5 µs) — like the BBC.

So a cycle-counted delay loop or raster-timed effect that works on the BBC's flat
2 MHz will run at roughly **half speed** in MODE 0–3 on the Electron, and at full
speed in MODE 4–7. Timing-sensitive code must account for the chosen MODE. See
[`../hardware/ARCHITECTURE.md`](../hardware/ARCHITECTURE.md) § CPU for the
contention model.
<!-- TODO: if an Electron unit needs exact cycle/µs figures, add a timing table once the per-cycle contention model is confirmed (see the ARCHITECTURE TODO) — the library gives the MODE-group split, not a per-cycle cost. -->

### MOS is OS 1.00, and there's less hardware behind it

The everyday MOS calls (`OSWRCH`, `OSRDCH`, `OSBYTE` read/write, `OSWORD`,
`OSCLI`) are **source-compatible** with the BBC, so string printing, key reading,
mode setting and file access transfer (reference §Acorn Electron Differences). Two
cautions:

- **No direct hardware registers.** The BBC's 6522 VIAs and 6845 do not exist
  behind the ULA, so any code that bypasses MOS to poke `&FE40` (System VIA),
  `&FE60` (User VIA) or the 6845 will not work. On the Electron, going through MOS
  is mandatory, not just good practice.
- **Hardware-specific OSBYTEs may no-op or error.** Calls that assume BBC-only
  hardware can return errors or do nothing on OS 1.00. Test rather than assume.
  <!-- TODO: list the specific OSBYTE/OSWORD calls that differ or no-op on OS 1.00 (sound, User Port, any 6522-dependent timer calls) against the reference library or an OS 1.00 reference, once a unit needs them. -->

### Sound: one channel, no noise

The MOS `SOUND` call exists, but the underlying hardware is a single tone channel
with no noise (reference §Acorn Electron Differences) — so multi-channel music and
noise effects written for the BBC's SN76489 will not reproduce. See
[`../hardware/ARCHITECTURE.md`](../hardware/ARCHITECTURE.md) § Sound and
[`../basic.md`](../basic.md).

## Minimal shape of an Electron assembly program

Identical to the BBC: set an origin, define MOS-call equates (`OSWRCH = &FFEE`,
…), do the work via `JSR` to MOS, return to BASIC with `RTS` (Electron machine
code is typically reached with `CALL` from BBC BASIC — see [`../basic.md`](../basic.md)).

<!-- TODO: add a complete, buildable hello-world (.asm) under
     code-samples/acorn-electron/assembly/ and reference it via CodeFromFile,
     once the Asm198x Electron target invocation is confirmed (see TOOLCHAIN-RESEARCH.md).
     Expected to be identical to the BBC hello-world since MOS calls match. -->

## See also

- [`../../bbc-micro/language/6502-quick-reference.md`](../../bbc-micro/language/6502-quick-reference.md) — the shared 6502 instruction set and MOS calls (the source of truth).
- [`../hardware/ARCHITECTURE.md`](../hardware/ARCHITECTURE.md) — the ULA contention model, MODE support, sound.
- [`../basic.md`](../basic.md) — BBC BASIC on the Electron and its inline 6502 assembler.
- Primary library:
  [`bbc-micro-reference.md`](../../../../../reference/by-system/bbc-micro/bbc-micro-reference.md)
  (§Acorn Electron Differences; §Vectored OS Calls, §OSBYTE/OSWORD Reference for the shared calls).
