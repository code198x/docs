# Decision: every lesson can assemble and run in the page

## The decision

A lesson offers the **write → assemble → run** loop in the page, as a
**sandbox that follows the build instructions rather than replacing them**.

1. **The local toolchain stays the taught path.** A unit still tells the reader
   to install Asm198x and run it, because a build step existing at all is the
   thing being taught. The sandbox sits *after* those instructions, introduced
   as a second way, never as the way.
2. **It is a component, not a page.** Every lesson gets it, so it is designed
   once — an editable source, an assemble action, and a machine — and applied
   per unit by naming a source file and a system.
3. **The reader's own source is what runs.** Editing the listing and pressing
   assemble produces a tape, and the machine loads it through its real ROM. It
   is the same assembler the lesson tells the reader to install, producing the
   same bytes, so the page is the toolchain rather than a simulation of it.
4. **It loads lazily.** The assembler is fetched on first interaction, not on
   page load, so a reader who never touches it pays nothing.

## Why after the instructions, and not instead

A unit's first idea is that there is a build step now. A page that quietly
assembles for the reader teaches the opposite — the reader never installs
anything, and the idea passes them by.

But a reader who edits two characters, presses assemble, and watches the
machine load the tape they just made has *seen* the step happen, which prose
does not achieve. Performing the step reinforces it; hiding it does not. The
order is what keeps both: instructions first, sandbox second.

It also makes existing content work. Units already say things like *change the
2, assemble and run again* — an instruction the page currently cannot honour.
With a sandbox above it, that becomes something the reader has been handed the
means to do.

## What it is built from

Published packages, not a bespoke build:

- **`@asm198x/z80`** — the assembler as wasm, split by CPU architecture so a
  Spectrum lesson carries no 6502 tables. 159 KB gzipped against 480 KB for the
  full build. `tape()` produces the same bytes as `asm198x --tapbas`.
- **`@emu198x/zx-spectrum`** — the machine, with its firmware bundled under the
  permission recorded in Emu198x's test-rom-policy. 121 KB gzipped.

A page with both is roughly 280 KB gzipped, of which 159 KB arrives only if the
reader assembles something.

Per-system packages follow the same shape. The NES and Game Boy need no
firmware at all — their cartridge *is* the program — so they are simpler than
the Spectrum rather than harder. The C64 and Amiga cannot bundle firmware and
are out of scope until that is solved, per Emu198x's roadmap scoping of WASM to
firmware-permission systems.

## Tape, not snapshot

The sandbox hands the machine a tape and lets the ROM load it. A snapshot skips
the boot and leaves the system variables zeroed, so a program in one cannot
call a ROM routine — see
[`198x/decisions/spectrum-lessons-load-from-tape.md`](https://github.com/198x/198x/blob/main/decisions/spectrum-lessons-load-from-tape.md).
Loading costs 1.6 seconds against 17.6 on real hardware, measured, and buys a
machine that behaves.

## Open: what happens when the reader hangs the machine

A local assembler answers a mistake with a line number. In the page, a reader
can also write something that assembles cleanly and then locks the Spectrum up
— which the current *When it's wrong, see why* sections do not cover, because
until now they could not happen here.

A reset control is the cheap answer and is what the first implementation
carries. It is not the good one: a machine that has just hung is the most
teachable moment in the unit, and throwing it away to get back to a prompt
wastes it. Revisit once there is a unit whose lesson is precisely that.

## Related

- [`endpoint-first-authoring.md`](endpoint-first-authoring.md) — showing the outcome before the work
- [`incremental-code-samples.md`](incremental-code-samples.md) — the one-concept rule the sandbox must not undercut
- [`198x/decisions/spectrum-lessons-load-from-tape.md`](https://github.com/198x/198x/blob/main/decisions/spectrum-lessons-load-from-tape.md) — why a tape
