Parent: https://github.com/code198x/docs/issues/121

Carry the pixel/span/box interfaces beyond the first three bitmap machines while keeping each layout and colour contract visible. Region-copy setup already establishes useful modes but does not supply general primitive routines.

## Scope and groups

1. Atom and Electron: reuse verified bitmap/draft setup with their own addresses, RAM configuration and execution; no timing transfer from BBC.
2. CPC MODE 1: packed colour bits, read/modify/write and partial-byte preservation; compare wider spans with individual pixels.
3. Oric HIRES: six data bits, required pixel/control bits and serial colour-attribute ownership; never turn an arbitrary drawing byte into an attribute silently.
4. Atari 800XL and 5200: explicitly selected ANTIC modes, display lists, screen-counter boundaries and matching CPU tables; do not apply XL execution evidence to the console.
5. C64: choose bitmap versus character-backed drawing explicitly; VIC bank, screen/colour data and CPU memory mapping are owned resources.
6. Amiga: CPU plane writes and appropriate blitter-assisted spans/fills, with Chip RAM, plane count, masks, alignment, DMA/ownership and completion contracts.

Start each group with an explicit per-mode scope and complete caller. Add higher-level geometry only after its backend is qualified. The existing Electron draft remains separately reviewed.

## Acceptance

- [ ] Each delivered backend records model/mode, addressing and stored colour semantics, neighbour/tail preservation and all bit/plane phases it supports.
- [ ] Complete memory/native-pixel checks and failing controls execute independently per machine; unsupported modes remain explicitly unqualified.
- [ ] Maths links explain packing/division, masks, plane/colour representation, screen coordinates and aspect ratio where useful.
- [ ] Work, memory and timing comparisons name their workloads and access policies; no blanket fastest backend claim.

## Existing material

- [Existing bitmap family](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/cross-platform/patterns/rendering/bitmap-regions/README.md)
- [Oric/ANTIC/Amiga contracts](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/cross-platform/patterns/rendering/region-architectures/README.md)

## Shared delivery bar

Keep actual reusable code in code-samples and include it on the website with CodeFromFile. Supply include/init/call examples, original or appropriately licensed data, inputs/outputs, bounds, state, register/stack effects, memory/bank/interrupt/video ownership and incompatible neighbours. Preserve useful BASIC/Forth/AMOS/Blitz routes rather than treating assembly as the only legitimate implementation.

Verify the named machine/mode/toolchain independently: compare appropriate destination memory and visible output, preserve neighbours/guards, cover boundaries and deliberate faulty controls. Existing reset fixtures or pattern readbacks do not prove stock-OS loading, live-display timing or another machine's port. State what was built, executed or remains proposed.

Explain code size, scratch/asset/table memory, bytes/words/VRAM transactions and scaling of work. Measure representative aligned/unaligned, small/large and worst-case workloads before claiming speed or a frame budget. Keep the maths locally understandable; link existing Maths for Games explanations where useful and record missing explanations rather than pretending they exist.
