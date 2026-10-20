Parent: https://github.com/code198x/docs/issues/121

Build a reusable geometry family on the pixel/span interfaces, with a readable first implementation and useful alternatives. Existing BASIC/runtime commands and the Amiga hardware line component are reuse material, not missing features to reinvent.

## Scope

- Start with the first bitmap backends; expose algorithms separately enough to compare a CPU rasteriser with the existing Amiga blitter-line backend.
- All-octant integer lines, clipping and explicit endpoint rules; zero-length and horizontal/vertical fast paths.
- Circle and ellipse outlines using symmetry/incremental decisions; filled variants emitting spans. Define radii, zero-radius cases, clipping and integer overflow/range limits.
- Give polygon/region filling a bounded follow-up contract: polygon edge/winding rules or flood-fill seed/workspace/overflow policy must be chosen explicitly; do not present an unbounded recursive fill as finished.
- Compare repeated pixel calls, spans, symmetry, incremental error and trig sampling; include table/code/stack/precision costs. A logical pixel circle may look elliptical with non-square display pixels; document coordinate versus presentation aspect.
- Maths connections: endpoint deltas/gradients, accumulated integer error, distance, symmetry, radii/axes, area and clipping. Existing triangles/trig/radians units support some of this; midpoint and fill/edge rules are new explanations to track.

## Acceptance

- [ ] Lines and circle/ellipse outline/fill routines have explicit bounds and independent reference images for all octants, axes, degenerate sizes and clipped edges.
- [ ] Shared endpoints and filled edges follow one documented convention; adjacent pixels and guards remain intact.
- [ ] Existing Amiga line and BASIC/AMOS/Blitz examples are linked with their actual capabilities, costs and verification limits.
- [ ] A bounded polygon/flood-fill implementation slice is specified before extending beyond span-filled circles/ellipses.

No 3D renderer or bulk curriculum rewrite is commissioned here.

## Existing material

- [Existing hardware line](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/commodore-amiga/patterns/assembly/rendering/blitter-line-draw/line.inc)
- [BASIC graphics teaching](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/sinclair-zx-spectrum/basic/basic-reference/unit-12.mdx)
- [AMOS shapes](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/commodore-amiga/amos/meet-amos/unit-09.mdx)

## Shared delivery bar

Keep actual reusable code in code-samples and include it on the website with CodeFromFile. Supply include/init/call examples, original or appropriately licensed data, inputs/outputs, bounds, state, register/stack effects, memory/bank/interrupt/video ownership and incompatible neighbours. Preserve useful BASIC/Forth/AMOS/Blitz routes rather than treating assembly as the only legitimate implementation.

Verify the named machine/mode/toolchain independently: compare appropriate destination memory and visible output, preserve neighbours/guards, cover boundaries and deliberate faulty controls. Existing reset fixtures or pattern readbacks do not prove stock-OS loading, live-display timing or another machine's port. State what was built, executed or remains proposed.

Explain code size, scratch/asset/table memory, bytes/words/VRAM transactions and scaling of work. Measure representative aligned/unaligned, small/large and worst-case workloads before claiming speed or a frame budget. Keep the maths locally understandable; link existing Maths for Games explanations where useful and record missing explanations rather than pretending they exist.
