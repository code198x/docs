Parent: https://github.com/code198x/docs/issues/121

Extend usable glyph drawing into text a game can place, measure and size deliberately. Preserve small fixed-width text as the cheap alternative rather than making every UI use a full layout engine.

## Scope

- Measure strings and centre/align them with an existing draw contract; replace or complete the explicitly illustrative centring pattern.
- Separate bitmap width, advance, spacing and baseline; add proportional widths, wrapping/newlines, unsupported glyph policy and overflow handling with bounded inputs.
- Add integer enlargement first, then bounded nearest-neighbour size changes, flips and rotation as separately measured variants. Large predesigned seven-segment digits are not evidence of generic scaling.
- Hardware character grids can use precomposed larger glyphs/multiple cells or prebuilt banks where practical; arbitrary placement/size may need software bitmap or sprite/tile staging. State which path is actually supplied.
- Compare pre-rendered sizes, tables/caches and runtime transforms: source/destination reads, code, temporary memory, quality and display-access budget.
- Maths connection: advance sums, integer division/rounding, scale factors, sampling, translation and rotation; transformations in the Maths overview are planned, not existing lessons.

## Acceptance

- [ ] Measurement and rendering agree on widths, line breaks, origins and empty/unsupported input; no unsigned centring underflow.
- [ ] Scaled/transformed variants state size/range limits and pass independent geometry/pixel expectations, including clipped edges and non-square-pixel presentation.
- [ ] Fixed-width, precomposed and runtime variants have honest workload-specific cost comparisons and reusable callers.

No mandatory Unicode/shaping system or general UI engine is implied; choose an explicit byte/character repertoire for the first implementation.

## Existing material

- [Illustrative centring pattern](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/patterns/cross-platform/rendering/centre-text-on-a-character-screen.mdx)
- [Large digit routine](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/sinclair-zx-spectrum/patterns/basic/seven-segment-digits.bas)

## Shared delivery bar

Keep actual reusable code in code-samples and include it on the website with CodeFromFile. Supply include/init/call examples, original or appropriately licensed data, inputs/outputs, bounds, state, register/stack effects, memory/bank/interrupt/video ownership and incompatible neighbours. Preserve useful BASIC/Forth/AMOS/Blitz routes rather than treating assembly as the only legitimate implementation.

Verify the named machine/mode/toolchain independently: compare appropriate destination memory and visible output, preserve neighbours/guards, cover boundaries and deliberate faulty controls. Existing reset fixtures or pattern readbacks do not prove stock-OS loading, live-display timing or another machine's port. State what was built, executed or remains proposed.

Explain code size, scratch/asset/table memory, bytes/words/VRAM transactions and scaling of work. Measure representative aligned/unaligned, small/large and worst-case workloads before claiming speed or a frame budget. Keep the maths locally understandable; link existing Maths for Games explanations where useful and record missing explanations rather than pretending they exist.
