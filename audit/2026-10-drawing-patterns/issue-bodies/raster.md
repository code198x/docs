Parent: https://github.com/code198x/docs/issues/121

Extend drawing coverage to Atari 2600 and 7800 using the graphics paths their existing probes actually exercise. A persistent framebuffer-style plot API is not the starting assumption.

## Scope

- Atari 2600: playfield/object data, coarse shapes and a bounded text/glyph display kernel. Separate picture data generation from cycle-sensitive visible-line emission.
- Atari 7800: MARIA objects, display-list headers/zones, graphics data and placement. Define which pieces can be callable helpers and which belong to frame/list ownership.
- Reuse the existing bar/object probes as observation and setup seeds; they are not general primitives or text renderers.
- First produce a small native drawing design and verified caller per machine before promising every shape/size operation. State object/playfield granularity, colours, slot/list/data limits and failure behaviour.
- Maths connections: raster position, quantisation, mirroring/repetition, local-to-object coordinates and a per-line/frame work budget.

## Acceptance

- [ ] Both native designs identify reusable data/routines, register/list/kernel ownership and unsupported operations honestly.
- [ ] A bounded caller per machine executes visible output and appropriate timing/list/guard controls; deliberately broken data or kernel/list placement is detected.
- [ ] CPU code/data size, scanline cycles or DMA/list workload are measured for the named configuration; avoid transfer of bitmap-backend or other-console evidence.

A general engine, emulator rewrite or complete game is not the initial deliverable. Investigate actual emulator defects separately if the caller exposes one.

## Existing material

- [TIA picture probe](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/atari-2600/patterns/assembly/capabilities/input-drawing-sound/picture.inc)
- [MARIA picture probe](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/atari-7800/patterns/assembly/capabilities/input-drawing-sound/picture.inc)

## Shared delivery bar

Keep actual reusable code in code-samples and include it on the website with CodeFromFile. Supply include/init/call examples, original or appropriately licensed data, inputs/outputs, bounds, state, register/stack effects, memory/bank/interrupt/video ownership and incompatible neighbours. Preserve useful BASIC/Forth/AMOS/Blitz routes rather than treating assembly as the only legitimate implementation.

Verify the named machine/mode/toolchain independently: compare appropriate destination memory and visible output, preserve neighbours/guards, cover boundaries and deliberate faulty controls. Existing reset fixtures or pattern readbacks do not prove stock-OS loading, live-display timing or another machine's port. State what was built, executed or remains proposed.

Explain code size, scratch/asset/table memory, bytes/words/VRAM transactions and scaling of work. Measure representative aligned/unaligned, small/large and worst-case workloads before claiming speed or a frame budget. Keep the maths locally understandable; link existing Maths for Games explanations where useful and record missing explanations rather than pretending they exist.
