# BBC Micro — Toolchain Research

Research notes behind the BBC Micro toolchain choice. This is a **find-toolchain
output**, not a Docker build: it records the 6502/BBC assembler and emulator
landscape and explains why the platform is scaffolded onto **Asm198x** (build)
and **Emu198x** (capture), and where the gaps are.

> **Honest status, up front.** The build path (Asm198x 6502) is solid; the
> capture path (Emu198x BBC core) exists but its capture parity is the
> integration gate; and the **output container is an open gate** — Asm198x emits
> a flat `.bin` for BBC today, with real BBC containers (`.ssd`/`.dsd`/`.uef`)
> still on the roadmap. Read § Output containers before assuming a learner can
> boot the artefact on hardware or in any emulator.

## Decision

| Job | Tool | Confidence |
|-----|------|-----------|
| Assemble | Asm198x, 6502 backend | High — 6502 is done and validated |
| Capture | Emu198x, `machine-acorn-bbc-micro` core | Medium — core exists; capture parity pending |
| Package | Asm198x flat `.bin` (interim) → `.ssd`/`.uef` (roadmap) | Low — container work not started |

## Why Asm198x is the assembler

The 6502 is the BBC's CPU, and Asm198x's **6502 backend is opcode-complete and
dialect-validated**: it is checked byte-identical against the reference 6502
assemblers the curriculum already uses (acme for C64, ca65 for NES). The BBC adds
no new CPU work — it is the same NMOS 6502 instruction set as the C64 and NES, so
the existing, proven backend covers it directly. See the Asm198x CPU roadmap,
which lists 6502 (C64, NES) as ✅ done:
[`../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md`](../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md).

Choosing Asm198x over the third-party BBC assemblers (below) follows the
dev-tooling-migration decision: launch platforms migrate off Docker per-platform,
and **new platforms start on the new tooling** rather than acquiring a Docker
image that would only need retiring later.
[`../../../../decisions/code198x-dev-tooling-migration.md`](../../../../decisions/code198x-dev-tooling-migration.md).

The one BBC-specific axis is **dialect convention**, not instruction coverage:
BBC source written in period style uses `&` for hex and reaches the machine
through MOS calls (`OSWRCH`, `OSBYTE`, …). Asm198x source uses its own dialect
conventions; the curriculum will settle the exact BBC source style when the first
unit is written.
<!-- TODO: confirm the Asm198x invocation/flags for a BBC 6502 target (org address, output path) against the asm198x CLI once a BBC target label is wired up. -->

## Emu198x core status

A BBC core exists in Emu198x: **`machine-acorn-bbc-micro`**. For the curriculum
it must reach **capture parity** — reliable headless screenshot and video
capture of a running program — which is the integration gate before BBC units can
be verified to the DoD bar.

- Emulator development and bugs are handled in the dedicated Emu198x session and
  filed as issues on `emu198x/emu198x`, not fixed from Code198x.
- Capture (screenshot/video) moves to Emu198x for all platforms; there is no BBC
  Docker capture script to migrate from, so the BBC starts clean on Emu198x.

<!-- TODO: confirm the BBC core's current capture status (screenshot + video) and the MCP/scriptable surface for headless capture, against the Emu198x session / its docs. -->
<!-- TODO: note BBC ROM requirements for the emulator — MOS (OS 1.20) ROM + BBC BASIC ROM — and where they are sourced, mirroring the C64/Amiga ROM-symlink arrangement. -->

## Output containers (the open gate)

This is the honest weak point. Asm198x's fused assemble step emits the platform's
final image, but BBC containers are **not yet implemented** — for non-launch
platforms it currently emits a **flat `.bin`**. The Asm198x packaging decision
records flat `.bin` as the default and treats per-platform containers as scoped,
prioritised work (the C64 `.prg` and Spectrum `.sna` gaps are called out as
highest-leverage because they block retiring the *launch* Docker images; the BBC
is not a launch platform, so its containers sit behind those).
[`../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md`](../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md) § Output containers per platform.

BBC container formats that will eventually be needed (reference library
§Known Unknowns lists the format landscape):

| Container | Use | Status |
|-----------|-----|--------|
| `.ssd` | Single-sided DFS disc image | Roadmap — not emitted |
| `.dsd` | Double-sided DFS disc image | Roadmap — not emitted |
| `.uef` | Cassette tape image (also a general tape/disc carrier) | Roadmap — not emitted |
| flat `.bin` | Raw image at `org` | Interim — what Asm198x emits today |

Two ways to close the gap (the umbrella dev-tooling decision owns the choice,
exactly as it does for the C64/Spectrum gaps):

1. **Asm198x emits the container** — add a `.ssd`/`.uef` serializer to the fused
   step.
2. **Emu198x loads flat** — have the BBC core load a flat `.bin` at `org` (and a
   tape/loader path), so no container is needed for the in-browser/emulator
   learner runtime.

Until one of these lands, a BBC artefact is a flat binary: fine for an emulator
that can load at an address, not yet a double-clickable disc/tape image.
<!-- TODO: once decided, record which path the BBC takes (Asm198x container vs Emu198x flat-load) and update reference.md's Toolchain table. -->

## Third-party tools (reference only)

Not used in the pipeline — listed so the landscape is documented and so
contributors know what the community standard tools are if a behaviour needs
cross-checking.

| Tool | Kind | Note |
|------|------|------|
| **BeebAsm** | Cross-assembler | The de-facto modern 6502 cross-assembler for BBC work; can emit `.ssd` directly. Useful as a *reference* for container output and BBC source idioms. |
| **b-em** | Emulator | Long-standing, accurate BBC/Master emulator (Linux/cross-platform). |
| **BeebEm** | Emulator | The classic Windows BBC emulator; widely used, good DFS/tape support. |
| **MAME** | Emulator | Has BBC drivers; useful for cross-checking edge-case hardware behaviour. |

These are consulted, not shipped — the layered-reference rule treats other
people's emulators/tools as the implementation-precedent layer, not a fact
source.

## Open questions

- Exact Asm198x BBC target invocation and `org` convention (see TODO above).
- Emu198x BBC capture parity status (see TODO above).
- Output-container path decision: Asm198x serializer vs Emu198x flat-load.
- BBC source dialect conventions for the curriculum (hex notation, MOS-call
  symbol names / equates file).
