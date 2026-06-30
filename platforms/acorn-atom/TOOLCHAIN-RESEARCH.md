# Acorn Atom — Toolchain Research

Research notes behind the Acorn Atom toolchain choice. This is a **find-toolchain
output**, not a Docker build: it records the 6502/Atom assembler and emulator
landscape and explains why the platform is scaffolded onto **Asm198x** (build)
and **Emu198x** (capture), and where the gaps are.

> **Honest status, up front.** The build path (Asm198x 6502) is solid; the
> capture path (Emu198x Atom core) is **in active development — fixes in flight**
> in the Emu198x session, so it is not yet a ready dependency; and the **output
> container is an open gate** — Asm198x emits a flat `.bin` for the Atom today,
> with real Acorn containers still on the roadmap. Read § Emu198x core status and
> § Output containers before assuming a learner can run the artefact.

## Decision

| Job | Tool | Confidence |
|-----|------|-----------|
| Assemble | Asm198x, 6502 backend | High — 6502 is done and validated |
| Capture | Emu198x, `machine-acorn-atom` core | **Low/Medium — core is being actively fixed right now; not yet capture-ready** |
| Package | Asm198x flat `.bin` (interim) → Acorn tape/disk container (roadmap) | Low — container work not started |

## Why Asm198x is the assembler

The 6502 is the Atom's CPU, and Asm198x's **6502 backend is opcode-complete and
dialect-validated**: it is checked byte-identical against the reference 6502
assemblers the curriculum already uses (acme for C64, ca65 for NES). The Atom adds
no new CPU work — it is the same NMOS 6502 instruction set as the C64 and NES, so
the existing, proven backend covers it directly. See the Asm198x CPU roadmap,
which lists 6502 (C64, NES) as done:
[`../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md`](../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md).

Choosing Asm198x over the third-party Atom assemblers (below) follows the
dev-tooling-migration decision: launch platforms migrate off Docker per-platform,
and **new platforms start on the new tooling** rather than acquiring a Docker
image that would only need retiring later.
[`../../../../decisions/code198x-dev-tooling-migration.md`](../../../../decisions/code198x-dev-tooling-migration.md).

The one Atom-specific axis is **dialect convention**, not instruction coverage:
Atom source written in period style uses `#` for hex (the *opposite* of the 6502
immediate-mode `#`) and reaches the machine through COS routines and the
memory-mapped MC6847. Asm198x source uses its own dialect conventions; the
curriculum will settle the exact Atom source style when the first unit is written.
<!-- TODO: confirm the Asm198x invocation/flags for an Atom 6502 target (org address, output path) against the asm198x CLI once an Atom target label is wired up. -->

## Emu198x core status

An Atom core exists in Emu198x: **`machine-acorn-atom`** — and it is **being
actively fixed right now** in the dedicated Emu198x session. Document it as *in
active development / fixes in flight*, not "ready" and not "absent". Reaching
**capture parity** — reliable headless screenshot and video capture of a running
program — is the integration gate before Atom units can be verified to the DoD
bar.

- Emulator development and bugs are handled in the Emu198x session and filed as
  issues on `emu198x/emu198x`, not fixed from Code198x.
- Capture (screenshot/video) moves to Emu198x for all platforms; there is no Atom
  Docker capture script to migrate from, so the Atom starts clean on Emu198x.

<!-- TODO: track the machine-acorn-atom fix work to completion in the Emu198x session, then confirm the core's capture status (screenshot + video) and the MCP/scriptable surface for headless capture. -->
<!-- TODO: note Atom ROM requirements for the emulator — Atom BASIC ROM + COS ROM — and where they are sourced, mirroring the C64/Amiga ROM arrangement. -->

## Output containers (the open gate)

This is the honest weak point. Asm198x's fused assemble step emits the platform's
final image, but Acorn Atom containers are **not yet implemented** — for
non-launch platforms it currently emits a **flat `.bin`**. The Asm198x packaging
decision records flat `.bin` as the default and treats per-platform containers as
scoped, prioritised work (the C64 `.prg` and Spectrum `.sna` gaps are highest-leverage
because they block retiring the *launch* Docker images; the Atom is not a launch
platform, so its containers sit behind those).
[`../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md`](../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md) § Output containers per platform.

Atom container formats that will eventually be relevant:

| Container | Use | Status |
|-----------|-----|--------|
| Atom cassette image (CUTS-format tape; commonly carried in `.uef`, also `.tap`/`.atm`) | Load a saved program from "tape" | Roadmap — not emitted <!-- TODO: confirm which Atom tape/image format(s) the Emu198x atom core loads (.uef / .atm / .tap) and pick the curriculum target. --> |
| `.atm` | Atom in-memory file/cassette block format used by Atom emulators | Roadmap — not emitted |
| flat `.bin` | Raw image at `org` | Interim — what Asm198x emits today |

Two ways to close the gap (the umbrella dev-tooling decision owns the choice,
exactly as it does for the C64/Spectrum gaps):

1. **Asm198x emits the container** — add an Atom tape/image serializer to the
   fused step.
2. **Emu198x loads flat** — have the Atom core load a flat `.bin` at `org` (and a
   tape/loader path), so no container is needed for the emulator learner runtime.

Until one of these lands, an Atom artefact is a flat binary: fine for an emulator
that can load at an address, not yet a loadable cassette/disk image.
<!-- TODO: once decided, record which path the Atom takes (Asm198x container vs Emu198x flat-load) and update reference.md's Toolchain table. -->

## Third-party tools (reference only)

Not used in the pipeline — listed so the landscape is documented and so
contributors know the community standard tools if a behaviour needs cross-checking.

| Tool | Kind | Note |
|------|------|------|
| **Atomulator** | Emulator | The best-known dedicated Acorn Atom emulator. Useful as a *reference* for Atom behaviour and tape/image formats. <!-- TODO: confirm Atomulator's current availability, platforms, and the image formats it loads. --> |
| **MAME** | Emulator | Has Acorn Atom drivers; useful for cross-checking edge-case hardware behaviour. <!-- TODO: confirm MAME's Atom driver name/status. --> |
| **BeebAsm** | Cross-assembler | A modern 6502 cross-assembler from the BBC world; can be a *reference* for 6502 source idioms (not Atom-specific output). |

These are consulted, not shipped — the layered-reference rule treats other
people's emulators/tools as the implementation-precedent layer, not a fact source.

## Open questions

- Exact Asm198x Atom target invocation and `org` convention (see TODO above).
- `machine-acorn-atom` capture parity status once the in-flight fixes land (see
  TODO above).
- Output-container path decision: Asm198x serializer vs Emu198x flat-load, and
  which Atom tape/image format to target.
- Atom source dialect conventions for the curriculum (`#` hex notation, COS-call
  symbol names / equates file).
