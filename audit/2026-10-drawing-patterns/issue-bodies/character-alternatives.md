Parent: https://github.com/code198x/docs/issues/121

Give PET, Aquarius, ZX80 and ZX81 useful native drawing/text routines with honest limits. A coarse cell/block composition is valuable on its own and must not be marketed as a general high-resolution pixel API.

## Scope

- PET 40-column and Aquarius: installed-ROM glyph selection, direct screen codes versus printed character codes, coarse shapes and bounded text placement/layout. Preserve Aquarius colour planes and cell-zero/border behaviour; do not invent PET per-cell colour RAM.
- ZX80/ZX81: establish a stock display-file/text/block-graphics baseline with refresh/ROM/RAM ownership explicit. A RAM-only map-query fixture proves no high-resolution display mode.
- Treat stock glyphs, semigraphics/coarse coordinates and separately researched advanced display/expansion variants as distinct choices. Do not make high-resolution extensions a compulsory baseline.
- PET/Aquarius draft region captures use original diagnostic font ROMs. Reuse that evidence honestly; add stock-font observations where the new claim needs them without redistributing restricted firmware.
- Jupiter Ace remains a writable-character/Forth port in the glyph queue, not a fixed-ROM example.
- Maths connections: grids, coarse resolution, discrete approximations and mapping a logical coordinate to one or several character cells.

## Acceptance

- [ ] Native text/coarse drawing components have explicit character repertoire, bounds, layout, display ownership and complete callable examples.
- [ ] Independent visible-output checks establish the stock-font or documented original-font configuration actually claimed, including border/refresh effects and rejection cases.
- [ ] Capability limits and costs are stated beside useful alternatives; no empty bitmap API whose implementation silently does nothing.

A high-resolution kit, custom ROM or expansion-specific renderer needs its own agreed configuration and verification, not inference from these baselines.

## Existing material

- [Current 30-system capability evidence](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/docs/capability-coverage.json)
- [Pending PET/Aquarius regions](https://github.com/code198x/code-samples/pull/133)

## Shared delivery bar

Keep actual reusable code in code-samples and include it on the website with CodeFromFile. Supply include/init/call examples, original or appropriately licensed data, inputs/outputs, bounds, state, register/stack effects, memory/bank/interrupt/video ownership and incompatible neighbours. Preserve useful BASIC/Forth/AMOS/Blitz routes rather than treating assembly as the only legitimate implementation.

Verify the named machine/mode/toolchain independently: compare appropriate destination memory and visible output, preserve neighbours/guards, cover boundaries and deliberate faulty controls. Existing reset fixtures or pattern readbacks do not prove stock-OS loading, live-display timing or another machine's port. State what was built, executed or remains proposed.

Explain code size, scratch/asset/table memory, bytes/words/VRAM transactions and scaling of work. Measure representative aligned/unaligned, small/large and worst-case workloads before claiming speed or a frame budget. Keep the maths locally understandable; link existing Maths for Games explanations where useful and record missing explanations rather than pretending they exist.
