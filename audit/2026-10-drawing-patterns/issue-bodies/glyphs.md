Parent: https://github.com/code198x/docs/issues/121

Turn existing pattern-loading setup into components a reader can use to install and replace characters, then show one shared glyph changing everywhere it appears. This is the first character strand of the recommended batch.

## Scope

- Unexpanded PAL VIC-20 high-resolution RAM characters, MSX1 Graphics I, and Game Boy DMG tiles with an explicit LCD-off baseline.
- Include/init/install-range/select-code/replace-glyph calls; source row/plane encoding, slot limits, original data, tables, bank/base alignment and ownership.
- Demonstrate two screen cells sharing a glyph: changing the name entry affects one instance; replacing the picture affects both. Keep character numbers, row bytes, screen placement and colours distinct.
- Reuse VIC-20 work in draft samples#133/website#871 if approved and merged; do not duplicate it or merge it through this issue. Reuse MSX and DMG pattern/region setup without transferring execution evidence across machines.
- Show CPU-visible character RAM versus ported VRAM versus DMG 2bpp/LCD access, MSX grouped colours, and VIC colour/multicolour bits. A live update queue is a later variant, not an implicit LCD-off capability.
- Maths connection: bitmap grids, powers of two, row-major indexing and local-to-cell coordinates. Reuse the Spectrum Crates explanation of converting a sketch into bytes without requiring that course.

## Acceptance

- [ ] Three callable maintained components, complete callers and explanatory code/data replace embedded setup as the primary library surface.
- [ ] Independent pattern memory and visible output checks cover range/slot edges, invalid counts, neighbour preservation and shared-glyph effects; a broken row/plane/slot control fails.
- [ ] Asset, scratch, code and upload work costs distinguish replacing a glyph from changing a screen entry.

Fixed-ROM PET/Aquarius fonts are comparison material, not software-writable glyph ports. General proportional/scaled text and full glyph caching are separate work.

## Existing material

- [MSX region setup](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/msx/patterns/assembly/rendering/tile-region/demo.asm)
- [DMG region setup](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/nintendo-game-boy/patterns/assembly/rendering/tile-region/demo.asm)
- [Pending VIC-20 source](https://github.com/code198x/code-samples/pull/133)

## Shared delivery bar

Keep actual reusable code in code-samples and include it on the website with CodeFromFile. Supply include/init/call examples, original or appropriately licensed data, inputs/outputs, bounds, state, register/stack effects, memory/bank/interrupt/video ownership and incompatible neighbours. Preserve useful BASIC/Forth/AMOS/Blitz routes rather than treating assembly as the only legitimate implementation.

Verify the named machine/mode/toolchain independently: compare appropriate destination memory and visible output, preserve neighbours/guards, cover boundaries and deliberate faulty controls. Existing reset fixtures or pattern readbacks do not prove stock-OS loading, live-display timing or another machine's port. State what was built, executed or remains proposed.

Explain code size, scratch/asset/table memory, bytes/words/VRAM transactions and scaling of work. Measure representative aligned/unaligned, small/large and worst-case workloads before claiming speed or a frame budget. Keep the maths locally understandable; link existing Maths for Games explanations where useful and record missing explanations rather than pretending they exist.
