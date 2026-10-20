Parent: https://github.com/code198x/docs/issues/117

Cover the drawing gamut across the current 30-system inventory: pixel read/write, spans and shapes, native characters and fonts, pixel-positioned text, layout and transformations. Preserve useful hardware differences and costs instead of imposing one framebuffer API on every machine.

## Inventory findings

Source inspection pins samples `8555ae938d09db9e22c26deabfb355341904ff9c` and website `0441deeb55c76ad6f0ea61cc722e753c7cb7b300`; the separately executed character-region work remains unmerged in samples#133/website#871. Default-branch native regions cover 17 systems; four draft ports make 21 including pending work. A map-query CPU fixture or asset-loading loop is not a primitive/font library.

Reuse Spectrum addressing/fixed-cell printing/UDG teaching, BBC positioned masked objects, Amiga hardware line/copy and game/runtime font/shape code, C64 charset lesson code, and existing tile uploads. Complete reusable ellipse/fill and arbitrary-position/proportional/transformed font families were not found in the inspected source.

## Recommended first batch

1. Bounded pixels/readback, spans and outlined/filled boxes on Spectrum 48K, BBC Micro MODE 4 and Dragon 32 PMODE 4.
2. Custom-glyph install/select/replace on unexpanded PAL VIC-20, MSX1 Graphics I and Game Boy DMG, including one glyph changing in multiple cells.

These six systems exercise Z80, 6502, 6809, CPU-visible bitmap/character RAM, ported VRAM and LCD access. Keep packed colours, serial attributes, fixed-ROM glyphs, software video, TIA kernels and MARIA lists visible in follow-up groups. This selects a recommendation and files work; it does not implement or publish the batch, merge pending PRs or change the curriculum lineup.

## Maths for Games

Reuse authored coordinates, triangles, direction/trig/radians and fixed-point units. Track missing explanations for incremental error, symmetry, clipping/fill edges, glyph-local coordinates, advance widths and scaling/sampling. Use real numeric/pixel examples and reciprocal links where helpful; do not make a whole maths course a prerequisite or call planned transformations existing coverage.

## Completion and boundaries

- [ ] All 30 IDs have source-linked evidence and explicit gaps, separating reusable/recorded code, lesson fragments, setup/probes, sketches and executed draft work.
- [ ] Family-sized child issues link back here, reuse existing work and retain model/mode/ownership/resource constraints.
- [ ] The bounded first batch and its independent correctness, negative-control, usability and cost checks are reviewable.
- [ ] Later geometry, fonts/layout/transforms and native alternative paths are tracked without one issue per missing matrix cell.
- [ ] Maths explanations connect to actual routines; new explanations remain proposals until authored and checked.

Overall library expansion remains docs#117. Existing region expansion and imagery tracking are reused; Vectrex's existing outside-this-registry proposals are not duplicated. Performance claims require named workloads and measurements; a green build is not machine execution or a frame budget.



## Shared delivery bar

Keep actual reusable code in code-samples and include it on the website with CodeFromFile. Supply include/init/call examples, original or appropriately licensed data, inputs/outputs, bounds, state, register/stack effects, memory/bank/interrupt/video ownership and incompatible neighbours. Preserve useful BASIC/Forth/AMOS/Blitz routes rather than treating assembly as the only legitimate implementation.

Verify the named machine/mode/toolchain independently: compare appropriate destination memory and visible output, preserve neighbours/guards, cover boundaries and deliberate faulty controls. Existing reset fixtures or pattern readbacks do not prove stock-OS loading, live-display timing or another machine's port. State what was built, executed or remains proposed.

Explain code size, scratch/asset/table memory, bytes/words/VRAM transactions and scaling of work. Measure representative aligned/unaligned, small/large and worst-case workloads before claiming speed or a frame budget. Keep the maths locally understandable; link existing Maths for Games explanations where useful and record missing explanations rather than pretending they exist.

## Child issues

- [ ] [Build bounded pixel, span and box routines on Spectrum, BBC Micro and Dragon](https://github.com/code198x/docs/issues/122) — recommended first batch
- [ ] [Extract custom-glyph install and replacement on VIC-20, MSX1 and Game Boy](https://github.com/code198x/docs/issues/123) — recommended first batch
- [ ] [Add clipped lines, circles, ellipses and span-filled shapes](https://github.com/code198x/docs/issues/124)
- [ ] [Draw fixed-width bitmap text at arbitrary pixel positions](https://github.com/code198x/docs/issues/125)
- [ ] [Build text measurement, proportional layout and scaled-glyph variants](https://github.com/code198x/docs/issues/126)
- [ ] [Extend primitive backends to packed, attributed, ANTIC and planar displays](https://github.com/code198x/docs/issues/127)
- [ ] [Extend font and pattern loading across the remaining writable-character paths](https://github.com/code198x/docs/issues/128)
- [ ] [Cover fixed-ROM and software-display drawing without inventing bitmap capabilities](https://github.com/code198x/docs/issues/129)
- [ ] [Define reusable drawing contracts for TIA kernels and MARIA display lists](https://github.com/code198x/docs/issues/130)
- [ ] [Connect drawing patterns to Maths for Games with worked geometry explanations](https://github.com/code198x/docs/issues/131) — supports the first batch and later geometry/fonts
