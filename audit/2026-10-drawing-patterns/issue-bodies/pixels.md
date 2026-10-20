Parent: https://github.com/code198x/docs/issues/121

A reader should be able to draw or inspect a pixel, draw an axis-aligned span, and outline or fill a box without borrowing an entire game. This is the first bitmap strand of the recommended batch.

## Scope

- Spectrum 48K monochrome bitmap, BBC Micro MODE 4 and Dragon 32 PMODE 4; name colour/attribute ownership separately.
- Set, clear, XOR and read one pixel; horizontal/vertical spans; outlined and filled rectangles. State coordinate origin, endpoint convention, empty/reversed extents, bounds and clipping/rejection policy.
- Reuse the Spectrum pixel_addr helper and the existing BBC/Dragon layout/region knowledge. It is an address helper, not an already implemented plotter.
- Preserve unrelated bits at partial-byte edges. Use whole-byte interiors where useful; do not require each filled rectangle to call plot once per pixel.
- Compare Z80/6502/6809 code, interleaved versus linear rows, tables versus calculation, checked entry versus trusted inner loops, and one pixel versus an aligned span.
- Maths connection: position/origin, integer division/remainder, interval endpoints, width/height and area; link existing Place a point and explain the byte/bit conversion locally.

## Acceptance

- [ ] Three maintained backends and small callers run with all operations and explicit contracts.
- [ ] Border/empty/one-pixel/all-bit-position cases preserve neighbours and independently match expected memory/native output; a deliberately wrong mask/stride is caught.
- [ ] A reader can include/init/call each routine and choose the cheaper path for a stated workload.

General sloped lines, curves, filled polygons, colour-mode ports and a whole game remain follow-ups.

## Existing material

- [Spectrum addressing](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/sinclair-zx-spectrum/patterns/assembly/rendering/bitmap-addressing/bitmap-addressing.inc)
- [Bitmap regions](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/cross-platform/patterns/rendering/bitmap-regions/README.md)

## Shared delivery bar

Keep actual reusable code in code-samples and include it on the website with CodeFromFile. Supply include/init/call examples, original or appropriately licensed data, inputs/outputs, bounds, state, register/stack effects, memory/bank/interrupt/video ownership and incompatible neighbours. Preserve useful BASIC/Forth/AMOS/Blitz routes rather than treating assembly as the only legitimate implementation.

Verify the named machine/mode/toolchain independently: compare appropriate destination memory and visible output, preserve neighbours/guards, cover boundaries and deliberate faulty controls. Existing reset fixtures or pattern readbacks do not prove stock-OS loading, live-display timing or another machine's port. State what was built, executed or remains proposed.

Explain code size, scratch/asset/table memory, bytes/words/VRAM transactions and scaling of work. Measure representative aligned/unaligned, small/large and worst-case workloads before claiming speed or a frame budget. Keep the maths locally understandable; link existing Maths for Games explanations where useful and record missing explanations rather than pretending they exist.
