# VIC-20 Toolchain Research

**Purpose:** Record the assembler/emulator landscape for the VIC-20 and the
decision to scaffold onto the family's own tooling. This is research, not a build
spec — it explains *why* the toolchain table in [reference.md](reference.md)
points where it does, and it is honest about the gaps.

**Bottom line:** Build on **Asm198x** (6502, opcode-complete and
dialect-validated), capture on **Emu198x** (`machine-commodore-vic-20` core).
The one open item is the **`.prg` output container**, which the VIC-20 shares
with the C64 — Asm198x emits a flat `.bin` today.

---

## The 6502 assembler landscape

The VIC-20's CPU is a stock MOS 6502 — the same programmer-visible core as the
C64's 6510, the NES's 2A03, the Apple II, and the BBC Micro. Any 6502 assembler
can target it; the platform-specific part is not the opcodes but the **output
container** (a CBM `.prg`) and the **memory layout** (where code may load given
the ~5 KB RAM and the moving screen — see
[hardware/ARCHITECTURE.md](hardware/ARCHITECTURE.md)).

Established third-party 6502 assemblers (kept for reference only, not the build
target):

| Tool | Notes |
|------|-------|
| **ACME** | The assembler the C64 curriculum used via Docker (`acme -f cbm` → `.prg`). Directly applicable to the VIC-20 — same CPU, same `.prg` container. |
| **cc65 / ca65 + ld65** | The NES curriculum's assembler+linker. ca65 has a VIC-20 target and a `vic20.cfg` linker config in the cc65 distribution. |
| **VICE (`xvic`)** | The de-facto reference emulator for the VIC-20; the yardstick for "does it behave like real hardware". Reference only — capture is Emu198x. |

These are the validation yardsticks, not the shipping toolchain.

## Why Asm198x is the target

Per the dev-tooling-migration decision
([`../../../../decisions/code198x-dev-tooling-migration.md`](../../../../decisions/code198x-dev-tooling-migration.md)),
Code198x builds move onto **Asm198x**. The VIC-20 inherits this from day one
rather than being wired to the third-party Docker path first and migrated later.

- **6502 is done.** Asm198x's 6502 core is complete and **validated
  byte-identical against ACME and ca65** — the exact tools a VIC-20 corpus would
  otherwise use. The source-compatible dialect stance means existing `.asm`
  sources assemble unchanged; if one needs editing, that is an Asm198x
  compatibility bug to log, not a curriculum change.
- **Single binary, cross-platform.** No per-platform Docker image, no dead-OS
  emulation tax that period assemblers carried.

See the Asm198x CPU roadmap
([`../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md`](../../../../Asm198x/asm198x/decisions/packaging-and-cpu-roadmap.md)):
6502 is `✅ done`.

## Emu198x core status

A **`machine-commodore-vic-20` core exists** in Emu198x. Capture (headless
screenshot, video, input scripting, MCP) is the same surface the other cores
expose. Per the migration decision, the per-unit gate is **capture parity**:
that the specific shots a unit needs (timing, input scripting, the exact frame)
come out right on this core.

- **Integration gate, not a capability gate.** As with the launch platforms, the
  remaining work is wiring — confirming this core captures what VIC-20 units
  actually need — not building a core from nothing.
- Emulator-side work (core bugs found while authoring) is filed as issues on
  Emu198x, not fixed from the Code198x side. <!-- TODO: confirm machine-commodore-vic-20 capture parity (input scripting + boot timing) against a real first program before cutting a unit over -->

## Output container — the one real gap

The VIC-20 uses the **`.prg`** format, identical in shape to the C64: a 2-byte
little-endian load address prefixed to the flat image (the `acme -f cbm`
convention). This is the *good news* container-wise — it is the format closest to
something Asm198x already nearly emits, and it is shared with a launch platform.

But it is **not emitted yet.** Per the Asm198x packaging roadmap, the CLI's
output dispatch emits hunk-exe (Amiga) and `.nes` (NES); **C64 and Spectrum fall
through to a flat `.bin`**, and the VIC-20 sits with the C64 on the `.prg` side
of that gap:

| Platform | Container | Asm198x today |
|----------|-----------|---------------|
| C64 | `.prg` | flat `.bin` ⏸ gap |
| **VIC-20** | **`.prg`** | **flat `.bin` ⏸ gap (shares the C64 fix)** |

The fix is small and self-contained — prepend the 2-byte load address to the
flat image — and it is **the same fix as the C64's**, so closing the C64 `.prg`
gap closes the VIC-20's too. Alternatively the gap can close on the **Emu198x
side** (load a flat image at `org`); that sub-choice is owned by the umbrella
dev-tooling-migration decision, not chosen here. See the Asm198x roadmap
§ "Output containers per platform".

**Honest status:** opcodes ready; container shared-with-C64 and pending. Until
`.prg` emission (or Emu198x flat-load) lands, a VIC-20 build produces a flat
binary that needs the load address handled out of band.

## Summary

| Concern | Status |
|---------|--------|
| 6502 opcodes (Asm198x) | ✅ complete, ACME/ca65-validated |
| Emu198x VIC-20 core | ✅ exists; capture parity = per-unit integration gate |
| `.prg` output container | ⏸ gap — flat `.bin` today; shares the C64 `.prg` fix |
| Third-party tools (ACME, cc65/ca65, VICE) | reference / validation only |
