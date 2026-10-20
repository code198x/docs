Parent: https://github.com/code198x/docs/issues/121

Use the drawing library to make the maths visible, and link the maths back to code a reader can run. Add explanations where the audit found a genuine gap rather than merely adding a pile of related links.

## Existing authored material to reuse

Maths for Games units 6–11 cover placing a point, measuring the triangle, direction through sine/cosine, radians, target angles and fixed-point movement. Its overview lists transformations/3D as planned; do not claim matrices, glyph scaling or raster algorithms are already taught.

## Scope

- Pixel/span/box pilot: origin and axis direction, integer division/remainder, local/screen conversion, inclusive/exclusive intervals, width/height/area and partial-byte edges.
- Geometry follow-up: endpoint deltas/gradients, integer error accumulation, symmetry, midpoint circle/ellipse decisions, clipping, span filling and explicit edge rules.
- Font follow-up: bitmap grids, glyph-local to screen translation, advance versus bitmap width, scale factors, nearest-neighbour sampling/rounding and a bounded rotation comparison when that implementation exists.
- Show how logical circles and square glyphs look with the selected display's pixel aspect; distinguish mathematical coordinates from presentation scaling.
- Add reciprocal links only where both pages exist and help the reader. Create a small worked explanation/diagram or supporting experiment for missing concepts; actual machine-specific reusable code remains the Pattern Library's centre.
- Keep local pattern explanations sufficient to use the routine. Maths for Games is optional support, not a new prerequisite course or automatic new game lineup.

## Acceptance

- [ ] An explicit concept-to-pattern map distinguishes current units from proposed explanations and names the routines/data it illustrates.
- [ ] The first batch includes concrete numeric/pixel examples and useful links to existing coordinate/representation material; later algorithm/transform explanations stay clearly proposed until authored.
- [ ] Worked cases agree with the implementation's origin, edge/rounding and aspect rules; links resolve both ways where authored.
- [ ] Learning and performance explanations agree: for example, span filling need not plot every pixel, and precomputed shifts/sizes exchange memory for work.

## Existing material

- [Place a point](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/craft/maths-for-games/unit-06.mdx)
- [Measure the triangle](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/craft/maths-for-games/unit-07.mdx)
- [Fixed-point movement](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/craft/maths-for-games/unit-11.mdx)
- [Maths overview and planned topics](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/craft/maths-for-games/index.mdx)

## Shared delivery bar

Keep actual reusable code in code-samples and include it on the website with CodeFromFile. Supply include/init/call examples, original or appropriately licensed data, inputs/outputs, bounds, state, register/stack effects, memory/bank/interrupt/video ownership and incompatible neighbours. Preserve useful BASIC/Forth/AMOS/Blitz routes rather than treating assembly as the only legitimate implementation.

Verify the named machine/mode/toolchain independently: compare appropriate destination memory and visible output, preserve neighbours/guards, cover boundaries and deliberate faulty controls. Existing reset fixtures or pattern readbacks do not prove stock-OS loading, live-display timing or another machine's port. State what was built, executed or remains proposed.

Explain code size, scratch/asset/table memory, bytes/words/VRAM transactions and scaling of work. Measure representative aligned/unaligned, small/large and worst-case workloads before claiming speed or a frame budget. Keep the maths locally understandable; link existing Maths for Games explanations where useful and record missing explanations rather than pretending they exist.
