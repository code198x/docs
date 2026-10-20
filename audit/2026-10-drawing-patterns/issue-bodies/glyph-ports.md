Parent: https://github.com/code198x/docs/issues/121

Expand the install/replace-glyph family after the VIC-20/MSX1/DMG pilot, selecting native storage and transfer contracts rather than assuming all UDGs are Spectrum-style eight-byte RAM blocks.

## Scope and groups

- C64: extract retained charset-copy/custom-character lesson code with banking, alignment and interrupt ownership; include shared-glyph animation.
- Other TMS Graphics I targets: ColecoVision, MTX, Einstein, Sord M5, SVI-328 and SG-1000. Reuse the MSX concept while preserving ports, latch ownership, grouped colours and independently executed callers.
- Master System/Game Gear: four-plane patterns, palettes, two-byte name entries and Game Gear viewport; no accidental 1bpp asset transfer.
- NES: explicitly select CHR-ROM asset preparation versus a supported CHR-RAM mapper, bank ownership and VBlank/rendering-off transfer policy. The current NROM assets do not prove a writable-pattern API.
- Jupiter Ace: writable character RAM with Forth/video-memory contention and allocation ownership. Do not group it with fixed-ROM PET/Aquarius.
- Oric and Atari XL: choose a character mode and show its actual character-base/colour policy separately from their current bitmap-region fixtures.

A glyph replacement changes all instances using that pattern. Patterns, name entries, palettes and attributes are separate resources. Optional animation, bank switching and glyph caches need explicit limits and costs rather than being required for the first install call.

## Acceptance

- [ ] Every delivered port includes data encoding, range/alignment limits and a complete install/select/replace caller with visible shared-instance behaviour.
- [ ] Independent pattern-memory/native-output checks cover slot/range/plane boundaries and broken upload controls per system.
- [ ] Transfer, asset and cache costs explain when changing a glyph is cheaper or more expensive than changing screen entries; maths links cover indexing/packing and local-to-cell placement.

This is a grouped coverage queue, not a promise to implement every mode or mapper in one patch. Retain absent ports as gaps until independently checked.

## Existing material

- [C64 retained charset code](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/commodore-64/assembly/sid-symphony/unit-04/symphony.asm)
- [VDP regions and asset setup](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/cross-platform/patterns/rendering/tile-region/README.md)

## Shared delivery bar

Keep actual reusable code in code-samples and include it on the website with CodeFromFile. Supply include/init/call examples, original or appropriately licensed data, inputs/outputs, bounds, state, register/stack effects, memory/bank/interrupt/video ownership and incompatible neighbours. Preserve useful BASIC/Forth/AMOS/Blitz routes rather than treating assembly as the only legitimate implementation.

Verify the named machine/mode/toolchain independently: compare appropriate destination memory and visible output, preserve neighbours/guards, cover boundaries and deliberate faulty controls. Existing reset fixtures or pattern readbacks do not prove stock-OS loading, live-display timing or another machine's port. State what was built, executed or remains proposed.

Explain code size, scratch/asset/table memory, bytes/words/VRAM transactions and scaling of work. Measure representative aligned/unaligned, small/large and worst-case workloads before claiming speed or a frame budget. Keep the maths locally understandable; link existing Maths for Games explanations where useful and record missing explanations rather than pretending they exist.
