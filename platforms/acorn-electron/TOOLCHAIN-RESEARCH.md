# Acorn Electron — Toolchain Research

Short, because the Electron's toolchain is **the same 6502 / Asm198x story as the
BBC Micro**. This records the few Electron-specific points and the honest gaps.
Read the BBC sibling first if you want the full reasoning:
[`../bbc-micro/TOOLCHAIN-RESEARCH.md`](../bbc-micro/TOOLCHAIN-RESEARCH.md).

> **Honest status, up front.** The build path (Asm198x 6502) is solid and needs
> no Electron-specific work — it is literally the same 6502 backend the BBC, C64
> and NES use. The capture path (Emu198x Electron core) **exists** —
> `machine-acorn-electron` is in the Emu198x workspace — and its capture parity is
> the integration gate. The **output container is an open gate**: Asm198x emits a
> flat `.bin`, with real Acorn containers (`.uef` tape; ADFS for the Plus 3) on
> the roadmap.

## Decision

| Job | Tool | Confidence |
|-----|------|-----------|
| Assemble | Asm198x, 6502 backend | High — 6502 is done and validated; no new work for the Electron |
| Capture | Emu198x, `machine-acorn-electron` core | Medium — the core exists; capture parity pending |
| Package | Asm198x flat `.bin` (interim) → `.uef`/ADFS (roadmap) | Low — container work not started |

## Why Asm198x is the assembler (same as the BBC)

The Electron's CPU is the 6502A — the same NMOS 6502 instruction set as the BBC,
C64 and NES. Asm198x's 6502 backend is opcode-complete and dialect-validated
(checked byte-identical against acme and ca65). The Electron adds **no new CPU
work** — the existing, proven backend covers it directly. The Asm198x CPU roadmap
lists 6502 as ✅ done:
[`../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md`](../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md).

The one Electron-specific axis is **dialect/idiom**, not instruction coverage —
and it leans the same way as the BBC, only harder: Electron source must reach the
machine through MOS calls (`OSWRCH`, `OSBYTE`, …) because the BBC's direct
hardware registers (6522 VIAs, 6845) **do not exist** behind the single ULA. Code
that pokes BBC hardware will assemble fine but not run.
<!-- TODO: confirm the Asm198x invocation/flags for an Electron 6502 target (org address, output path) — expected identical to the BBC target — once a target label is wired up. -->

## Emu198x core status

An Electron core **exists** in the Emu198x workspace: **`machine-acorn-electron`**
(with a matching `runtime-acorn-electron` and `emu198x-acorn-electron`), sitting
alongside the BBC's `machine-acorn-bbc-micro`. The crate carries `bios_boot` and
`tape_load` tests, so boot and tape paths are at least scaffolded.

For the curriculum the core must reach **capture parity** — reliable headless
screenshot and video capture of a running program — which is the integration gate
before Electron units can be verified to the DoD bar.

- Emulator development and bugs are handled in the dedicated Emu198x session and
  filed as issues on `emu198x/emu198x`, not fixed from Code198x.
- Capture moves to Emu198x for all platforms; there is no Electron Docker capture
  script to migrate from, so the Electron starts clean on Emu198x.

<!-- TODO: confirm the Electron core's current capture status (screenshot + video) and the MCP/scriptable surface for headless capture, against the Emu198x session / its docs. -->
<!-- TODO: note Electron ROM requirements for the emulator — OS 1.00 ROM (unique to the Electron) + BBC BASIC ROM — and where they are sourced, mirroring the BBC/C64 ROM-symlink arrangement. -->

## Output containers (the open gate)

Same honest weak point as the BBC. Asm198x's fused assemble step emits the
platform's final image, but Acorn containers are **not yet implemented** — for
non-launch platforms it currently emits a **flat `.bin`**. The Asm198x packaging
decision records flat `.bin` as the default and lists only the C64 `.prg` and
Spectrum `.sna` containers as prioritised gaps (because they block retiring the
*launch* Docker images); the Electron, like the BBC, sits behind those.
[`../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md`](../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md) § Output containers per platform.

Electron container formats that will eventually be needed:

| Container | Use | Status |
|-----------|-----|--------|
| `.uef` | Cassette tape image (the Electron's default storage; BBC-compatible tape format) | Roadmap — not emitted |
| ADFS disc image | Plus 3 floppy (ADFS, **not** the BBC's DFS `.ssd`) | Roadmap — not emitted |
| flat `.bin` | Raw image at `org` | Interim — what Asm198x emits today |

Note the Electron's container needs diverge slightly from the BBC's: the
Electron's default medium is **cassette** (`.uef`), and its disc filing system is
**ADFS** (Plus 3), not the BBC's DFS — so a BBC `.ssd` serializer would not serve
the Electron unchanged.

Two ways to close the gap (the umbrella dev-tooling decision owns the choice):

1. **Asm198x emits the container** — add a `.uef`/ADFS serializer to the fused step.
2. **Emu198x loads flat** — have the Electron core load a flat `.bin` at `org`
   (and a tape/loader path), so no container is needed for the emulator learner
   runtime.

Until one lands, an Electron artefact is a flat binary: fine for an emulator that
can load at an address, not yet a tape/disc image.
<!-- TODO: once decided, record which path the Electron takes (Asm198x container vs Emu198x flat-load) and update reference.md's Toolchain table. -->

## Third-party tools (reference only)

Not used in the pipeline — listed so the landscape is documented.

| Tool | Kind | Note |
|------|------|------|
| **BeebAsm** | Cross-assembler | The de-facto modern 6502 cross-assembler for BBC/Electron work; useful as a *reference* for source idioms and container output. |
| **Elkulator** | Emulator | The classic dedicated **Acorn Electron** emulator; useful for cross-checking Electron-specific ULA/contention behaviour. |
| **MAME** | Emulator | Has an Electron driver; useful for cross-checking edge-case hardware behaviour. |

These are consulted, not shipped — the layered-reference rule treats other
people's emulators/tools as the implementation-precedent layer, not a fact source.

## Open questions

- Exact Asm198x Electron target invocation and `org` convention (expected to match
  the BBC; see TODO above).
- Emu198x Electron capture parity status (see TODO above).
- Output-container path decision: Asm198x serializer (`.uef`/ADFS) vs Emu198x
  flat-load.
- Electron source dialect conventions for the curriculum (hex notation, MOS-call
  equates) — expected to align with the BBC's.
