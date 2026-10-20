Parent: https://github.com/code198x/docs/issues/121

A glyph bitmap should be usable away from the character grid. Extract a text-specific component from existing masking/shifting/clipping work rather than cloning those routines into another renderer.

## Scope

- Initial bitmap examples: Spectrum 48K, BBC Micro MODE 4 and Amiga one-plane CPU/blitter choices where justified.
- Fixed-width glyph definition/lookup and a bounded character/string draw call at pixel x/y, including every horizontal bit phase and byte/word crossing.
- Opaque and masked/transparent drawing contracts, clipping at all edges, missing-glyph handling and explicit colour/attribute ownership.
- Distinguish a character cell, glyph-local pixels, destination pixels and advance. Existing Spectrum character printing is fixed-grid; Amiga game digits are byte-aligned. Neither is a complete arbitrary-position text API.
- Maths connection: translation, quotient/remainder and bit phase, clipping intervals and local/screen coordinates. Keep baseline/origin clear before adding typography features.
- Compare shifting at draw time with pre-shifted assets, scratch buffering and word/blitter alignment; show how one extra destination byte changes cost.

## Acceptance

- [ ] A reusable glyph/string API with include/init/call examples works at all supported phases and screen edges.
- [ ] Independent memory/pixel oracles test background preservation, clipping, empty/unsupported characters and deliberate incorrect-shift/stride controls.
- [ ] Existing aligned printing and masked sprite paths remain linked alternatives; no universal speed claim or full-game composition requirement.

Proportional layout, wrapping, scaling and rotation are separate variants, not prerequisites for the first fixed-width implementation.

## Existing material

- [Spectrum character printing](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/sinclair-zx-spectrum/patterns/assembly/rendering/character-printing/characters.inc)
- [Spectrum positioned object code](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/sinclair-zx-spectrum/patterns/assembly/rendering/pre-shifted-sprites/draw.inc)
- [BBC positioned object code](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/bbc-micro/patterns/assembly/rendering/pre-shifted-sprites/draw.inc)

## Shared delivery bar

Keep actual reusable code in code-samples and include it on the website with CodeFromFile. Supply include/init/call examples, original or appropriately licensed data, inputs/outputs, bounds, state, register/stack effects, memory/bank/interrupt/video ownership and incompatible neighbours. Preserve useful BASIC/Forth/AMOS/Blitz routes rather than treating assembly as the only legitimate implementation.

Verify the named machine/mode/toolchain independently: compare appropriate destination memory and visible output, preserve neighbours/guards, cover boundaries and deliberate faulty controls. Existing reset fixtures or pattern readbacks do not prove stock-OS loading, live-display timing or another machine's port. State what was built, executed or remains proposed.

Explain code size, scratch/asset/table memory, bytes/words/VRAM transactions and scaling of work. Measure representative aligned/unaligned, small/large and worst-case workloads before claiming speed or a frame budget. Keep the maths locally understandable; link existing Maths for Games explanations where useful and record missing explanations rather than pretending they exist.
