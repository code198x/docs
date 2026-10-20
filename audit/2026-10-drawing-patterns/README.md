# Drawing patterns: from a dot to a font

**Inventory and proposed delivery order, 20 October 2026.** This audit covers all 30 systems in the current probe registry. It does not commission every port, change the curriculum lineup or merge the pending native-region batch.

We have useful drawing code already. The missing piece is a discoverable set of routines which readers can take into their own games: pixels, spans and shapes; glyphs and fonts; placement and layout; then the faster or richer alternatives which each machine makes worthwhile.

## What exists

- Spectrum has a verified **address helper**, fixed-cell character/string printing, masked/positioned object routines, BASIC PLOT/DRAW/CIRCLE teaching, and a substantial UDG lesson in Crates. An address helper is not a plot/read routine; large seven-segment digits are not a scalable font engine.
- Amiga has a maintained, recorded **hardware line** routine and CPU/blitter block paths. Older game code contains pixel reading, byte-aligned rectangles and HUD digits. AMOS and Blitz already teach/use drawing commands; their runtime facilities deserve reusable treatment alongside assembly, not replacement by it.
- BBC Micro has verified masked and pixel-positioned object code. This is useful substrate for bitmap fonts, not an existing arbitrary-position string API.
- Several other systems already upload original tile/glyph patterns inside diagnostics. That is extraction material, not a standalone install/replace/animate-font component with a published contract.
- The centring pattern is explicitly **illustrative**, with a printer supplied elsewhere. General proportional text, scaling/rotation and a maintained ellipse/filled-curve family were not found in the inspected source. This is a scoped inventory finding, not a claim about hardware capability or undiscovered legacy branches.

Reuse these concrete sources: [spectrum-address](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/sinclair-zx-spectrum/patterns/assembly/rendering/bitmap-addressing/bitmap-addressing.inc#L9), [spectrum-char](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/sinclair-zx-spectrum/patterns/assembly/rendering/character-printing/characters.inc#L2), [spectrum-shape-lesson](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/sinclair-zx-spectrum/basic/basic-reference/unit-12.mdx#L3), [spectrum-udg-lesson](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/sinclair-zx-spectrum/basic/crates/unit-01-draw-a-wooden-crate.mdx#L57), [amiga-line](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/commodore-amiga/patterns/assembly/rendering/blitter-line-draw/line.inc#L1), [amiga-read-box](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/commodore-amiga/assembly/exodus/unit-07/exodus.asm#L203), [amiga-amos-lesson](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/commodore-amiga/amos/meet-amos/unit-09.mdx#L35), [amiga-blitz-shapes](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/commodore-amiga/blitz/meet-blitz/unit-07/shapes.bb2#L8), [bbc-positioned](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/bbc-micro/patterns/assembly/rendering/pre-shifted-sprites/draw.inc#L1), [c64-charset](https://github.com/code198x/code-samples/blob/8555ae938d09db9e22c26deabfb355341904ff9c/commodore-64/assembly/sid-symphony/unit-04/symphony.asm#L177), [centred-sketch](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/patterns/cross-platform/rendering/centre-text-on-a-character-screen.mdx#L16).

## Status means evidence, not a capability ceiling

| Mark | Meaning |
| --- | --- |
| R | Maintained reusable pattern with recorded execution for its named configuration |
| A | Address calculation only; no pixel write/read implied |
| L | Lesson/game/runtime example; extraction and a standalone contract still needed |
| S | Asset loading or display setup inside a caller |
| P | Probe demonstrates only the stated output |
| D | Executed draft work in samples #133 / website #871, still unmerged |
| I | Explicitly illustrative listing |
| G | No complete reusable family found in the inspected source; not “impossible on this machine” |

A region or sprite can be R while pixels or text remain G. A successful assembly or CPU-RAM map query does not establish graphics. No new emulator runs or benchmarks were performed for this audit. Existing configuration-specific records were inspected and linked; their limits remain in force.

## All 30 systems

“Shapes” distinguishes existing teaching from a complete primitive API. “Curves/fills” does not imply that a BASIC CIRCLE example provides ellipses or general filled polygons. See the per-system notes for the selected mode and the [evidence ledger](evidence.md) for code and execution records.

| System | Pixels/read | Lines/spans | Boxes | Curves/fills | Grid characters/font | Pixel text | Layout/scale | Region |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| acorn-atom | G | G | G | G | G | G | G | R |
| acorn-bbc-micro | G | G | G | G | G | G (R substrate) | G | R |
| acorn-electron | G | G | G | G | G | G | G | D |
| amstrad-cpc | G | G | G | G | G | G | G | R |
| atari-2600 | G | G | G | G | G | G | G | G |
| atari-5200 | G | G | G | G | G | G | G | G |
| atari-7800 | G | G | G | G | G | G | G | G |
| atari-800xl | G | G | G | G | G | G | G | R |
| coleco-colecovision | G | G | G | G | S | G | G | R |
| commodore-amiga | L | R/L | L | L runtime | L | L aligned/runtime | L runtime | R |
| commodore-c64 | G | G | G | G | L | G | G | G |
| commodore-pet | G | G | G | G | D | G | G | D |
| commodore-vic-20 | G | G | G | G | D | G | G | D |
| dragon | G | G | G | G | G | G | G | R |
| jupiter-ace | G | G | G | G | P | G | G | G |
| mattel-aquarius | G | G | G | G | D | G | G | D |
| memotech-mtx | G | G | G | G | S | G | G | R |
| microsoft-msx1 | G | G | G | G | S | G | G | R |
| nintendo-game-boy | G | G | G | G | S | G | G | R |
| nintendo-nes | G | G | G | G | S | G | G | G |
| oric | G | G | G | G | G | G | G | R |
| sega-game-gear | G | G | G | G | S | G | G | R |
| sega-master-system | G | G | G | G | S | G | G | R |
| sega-sg-1000 | G | G | G | G | S | G | G | R |
| sinclair-zx-spectrum | A/L | L | L | L | R/L | G (R substrate) | R digits / I layout (no scaling) | G |
| sinclair-zx80 | G | G | G | G | P | G | G | G |
| sinclair-zx81 | G | G | G | G | P | G | G | G |
| sord-m5 | G | G | G | G | S | G | G | R |
| spectravideo-svi-328 | G | G | G | G | S | G | G | R |
| tatung-einstein | G | G | G | G | S | G | G | R |

Default-branch native-region coverage is **17/30**. Four more separately executed regions (Electron, PET, VIC-20, Aquarius) remain in [samples #133](https://github.com/code198x/code-samples/pull/133) / [website #871](https://github.com/code198x/website/pull/871), making **21/30 including the draft batch**. This inventory does not authorise merging it. Remaining region ports continue under [docs #117](https://github.com/code198x/docs/issues/117); do not open a second queue for those same ports.

## Machine choices and costs

### acorn-atom

**Inspected path:** 256×192 mono bitmap region. A scanline layout and RAM allocation are already established; add bounded read/modify/write and spans rather than treating whole-tile copying as a plotter.

**Gap:** Pixel/readback and spans; software font extraction. Sources: [probe-acorn-atom](evidence.md#probe-acorn-atom), [region-acorn-atom](evidence.md#region-acorn-atom), [record-acorn-atom](evidence.md#record-acorn-atom). Tracking: [#127](https://github.com/code198x/docs/issues/127), [#124](https://github.com/code198x/docs/issues/124), [#125](https://github.com/code198x/docs/issues/125), [#126](https://github.com/code198x/docs/issues/126), [#131](https://github.com/code198x/docs/issues/131).

### acorn-bbc-micro

**Inspected path:** MODE 4 bitmap; positioned masked objects. Cell-interleaved scanlines; phase tables trade RAM for less shifting; bitmap bytes and OS colour/graphics coordinates are separate contracts.

**Gap:** Pixel/readback/spans/boxes first; adapt existing masked objects into text. Sources: [probe-acorn-bbc-micro](evidence.md#probe-acorn-bbc-micro), [region-acorn-bbc-micro](evidence.md#region-acorn-bbc-micro), [record-acorn-bbc-micro](evidence.md#record-acorn-bbc-micro), [bbc-positioned](evidence.md#bbc-positioned). Tracking: [#122](https://github.com/code198x/docs/issues/122), [#124](https://github.com/code198x/docs/issues/124), [#125](https://github.com/code198x/docs/issues/125), [#126](https://github.com/code198x/docs/issues/126), [#131](https://github.com/code198x/docs/issues/131).

### acorn-electron

**Inspected path:** MODE 4 bitmap, draft region. Same cell-style layout idea as BBC, separate ULA/ownership and timing evidence; 512-byte scanline tables in the draft are a space choice.

**Gap:** Extract pixel/span backend after the first batch. Sources: [probe-acorn-electron](evidence.md#probe-acorn-electron), [region-acorn-electron](evidence.md#region-acorn-electron), [record-acorn-electron](evidence.md#record-acorn-electron). Tracking: [#127](https://github.com/code198x/docs/issues/127), [#124](https://github.com/code198x/docs/issues/124), [#125](https://github.com/code198x/docs/issues/125), [#126](https://github.com/code198x/docs/issues/126), [#131](https://github.com/code198x/docs/issues/131).

### amstrad-cpc

**Inspected path:** MODE 1 packed bitmap region. Two bytes per eight-pixel cell; interleaved colour bits and non-linear scanlines require correct read/modify/write and neighbour preservation.

**Gap:** Packed-colour pixel/span backend; fixed-width software fonts. Sources: [probe-amstrad-cpc](evidence.md#probe-amstrad-cpc), [region-amstrad-cpc](evidence.md#region-amstrad-cpc), [record-amstrad-cpc](evidence.md#record-amstrad-cpc). Tracking: [#127](https://github.com/code198x/docs/issues/127), [#124](https://github.com/code198x/docs/issues/124), [#125](https://github.com/code198x/docs/issues/125), [#126](https://github.com/code198x/docs/issues/126), [#131](https://github.com/code198x/docs/issues/131).

### atari-2600

**Inspected path:** TIA playfield bar and frame kernel probe. The selected path emits scanlines, not a writable persistent framebuffer; visible-kernel cycles and object/playfield limits dominate.

**Gap:** Native scanline/playfield drawing study and bounded text kernel. Sources: [probe-atari-2600](evidence.md#probe-atari-2600). Tracking: [#130](https://github.com/code198x/docs/issues/130), [#131](https://github.com/code198x/docs/issues/131).

### atari-5200

**Inspected path:** ANTIC mode 8 bitmap probe. Probe is a coarse four-colour bitmap and explicit display list, not a general graphics API; reuse ANTIC ideas with this machine’s own execution.

**Gap:** Choose and verify bitmap pixel/span mode; character-mode alternative. Sources: [probe-atari-5200](evidence.md#probe-atari-5200). Tracking: [#127](https://github.com/code198x/docs/issues/127), [#124](https://github.com/code198x/docs/issues/124), [#125](https://github.com/code198x/docs/issues/125), [#126](https://github.com/code198x/docs/issues/126), [#131](https://github.com/code198x/docs/issues/131).

### atari-7800

**Inspected path:** MARIA display-list object probe. Object headers, zones and DMA data layout are the demonstrated path; drawing cost includes list/bandwidth limits, not only CPU plot cost.

**Gap:** Bounded MARIA character/object composition and drawing contract. Sources: [probe-atari-7800](evidence.md#probe-atari-7800). Tracking: [#130](https://github.com/code198x/docs/issues/130), [#131](https://github.com/code198x/docs/issues/131).

### atari-800xl

**Inspected path:** ANTIC F monochrome bitmap region. Screen counter 4 KB boundary and display-list addresses must agree with CPU tables; character modes are separate alternatives.

**Gap:** Pixel/span extraction; separate writable-character mode example. Sources: [probe-atari-800xl](evidence.md#probe-atari-800xl), [region-atari-800xl](evidence.md#region-atari-800xl), [record-atari-800xl](evidence.md#record-atari-800xl). Tracking: [#127](https://github.com/code198x/docs/issues/127), [#124](https://github.com/code198x/docs/issues/124), [#125](https://github.com/code198x/docs/issues/125), [#126](https://github.com/code198x/docs/issues/126), [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

### coleco-colecovision

**Inspected path:** TMS-family Graphics I pattern/name region. Installed patterns and grouped colour data are separate from name writes. Port wiring/latch ownership and access timing are machine-specific; Graphics II pixel work needs its own mode/bank contract.

**Gap:** Extract pattern/font uploads; then mode-specific bitmap-like editing. Sources: [probe-coleco-colecovision](evidence.md#probe-coleco-colecovision), [region-coleco-colecovision](evidence.md#region-coleco-colecovision), [record-coleco-colecovision](evidence.md#record-coleco-colecovision). Tracking: [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

### commodore-amiga

**Inspected path:** CPU bitplanes; blitter copy/line; hardware/software objects. Planes, Chip RAM, alignment, DMA and blitter ownership matter. Byte-aligned digit drawing is not arbitrary pixel text; AMOS/Blitz already expose useful higher-level shapes.

**Gap:** Extract bounded CPU pixels/spans; retain verified line backend; software font family. Sources: [probe-commodore-amiga](evidence.md#probe-commodore-amiga), [region-commodore-amiga](evidence.md#region-commodore-amiga), [record-commodore-amiga](evidence.md#record-commodore-amiga), [amiga-line](evidence.md#amiga-line), [amiga-read-box](evidence.md#amiga-read-box), [amiga-digits](evidence.md#amiga-digits), [amiga-amos-shapes](evidence.md#amiga-amos-shapes), [amiga-amos-lesson](evidence.md#amiga-amos-lesson), [amiga-blitz-shapes](evidence.md#amiga-blitz-shapes), [amiga-amos-text](evidence.md#amiga-amos-text). Tracking: [#127](https://github.com/code198x/docs/issues/127), [#124](https://github.com/code198x/docs/issues/124), [#125](https://github.com/code198x/docs/issues/125), [#126](https://github.com/code198x/docs/issues/126), [#131](https://github.com/code198x/docs/issues/131).

### commodore-c64

**Inspected path:** Character screen, hardware sprites; lesson charset copy. VIC bank and character-base alignment, CPU ROM mapping, IRQ state and 2 KB character-set allocation need explicit ownership. Bitmap is a separate path.

**Gap:** Extract custom charset/character animation; later bitmap pixels/spans. Sources: [probe-commodore-c64](evidence.md#probe-commodore-c64), [c64-charset](evidence.md#c64-charset). Tracking: [#127](https://github.com/code198x/docs/issues/127), [#124](https://github.com/code198x/docs/issues/124), [#125](https://github.com/code198x/docs/issues/125), [#126](https://github.com/code198x/docs/issues/126), [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

### commodore-pet

**Inspected path:** 40-column fixed-ROM character screen, draft region. No per-cell colour RAM in this selected configuration. Diagnostic font replacement is a fixture input, not software-redefinable stock glyphs.

**Gap:** Installed-ROM glyph selection, text layout and honest coarse graphics. Sources: [probe-commodore-pet](evidence.md#probe-commodore-pet), [region-commodore-pet](evidence.md#region-commodore-pet), [record-commodore-pet](evidence.md#record-commodore-pet). Tracking: [#129](https://github.com/code198x/docs/issues/129), [#126](https://github.com/code198x/docs/issues/126), [#131](https://github.com/code198x/docs/issues/131).

### commodore-vic-20

**Inspected path:** Unexpanded PAL RAM characters, draft region. Writable glyphs share scarce RAM with game data/screen. One glyph change affects all instances; colour bit 3 changes pixel interpretation.

**Gap:** Standalone character install/replace first. Sources: [probe-commodore-vic-20](evidence.md#probe-commodore-vic-20), [region-commodore-vic-20](evidence.md#region-commodore-vic-20), [record-commodore-vic-20](evidence.md#record-commodore-vic-20). Tracking: [#123](https://github.com/code198x/docs/issues/123), [#131](https://github.com/code198x/docs/issues/131).

### dragon

**Inspected path:** PMODE 4 monochrome bitmap region. Linear rows simplify addresses; whole-byte spans can avoid repeated pixel operations; 6809 calling/stack and display setup remain specific.

**Gap:** Pixel/readback/spans/boxes first. Sources: [probe-dragon](evidence.md#probe-dragon), [region-dragon](evidence.md#region-dragon), [record-dragon](evidence.md#record-dragon). Tracking: [#122](https://github.com/code198x/docs/issues/122), [#124](https://github.com/code198x/docs/issues/124), [#125](https://github.com/code198x/docs/issues/125), [#126](https://github.com/code198x/docs/issues/126), [#131](https://github.com/code198x/docs/issues/131).

### jupiter-ace

**Inspected path:** Forth printed cell box; byte-map CPU fixture. The existing box is text, not a rectangle rasteriser. A writable-character candidate needs its own display-contention and Forth/RAM ownership example.

**Gap:** Character definitions/placement and native text contracts. Sources: [probe-jupiter-ace](evidence.md#probe-jupiter-ace). Tracking: [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

### mattel-aquarius

**Inspected path:** Fixed-ROM screen/colour planes, draft region. Foreground/background nibbles and border tied to cell zero. Diagnostic font ROM is not a software upload facility.

**Gap:** Fixed-ROM composition/text layout and border ownership. Sources: [probe-mattel-aquarius](evidence.md#probe-mattel-aquarius), [region-mattel-aquarius](evidence.md#region-mattel-aquarius), [record-mattel-aquarius](evidence.md#record-mattel-aquarius). Tracking: [#129](https://github.com/code198x/docs/issues/129), [#126](https://github.com/code198x/docs/issues/126), [#131](https://github.com/code198x/docs/issues/131).

### memotech-mtx

**Inspected path:** TMS-family Graphics I pattern/name region. Installed patterns and grouped colour data are separate from name writes. Port wiring/latch ownership and access timing are machine-specific; Graphics II pixel work needs its own mode/bank contract.

**Gap:** Extract pattern/font uploads; then mode-specific bitmap-like editing. Sources: [probe-memotech-mtx](evidence.md#probe-memotech-mtx), [region-memotech-mtx](evidence.md#region-memotech-mtx), [record-memotech-mtx](evidence.md#record-memotech-mtx). Tracking: [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

### microsoft-msx1

**Inspected path:** TMS-family Graphics I pattern/name region. Installed patterns and grouped colour data are separate from name writes. Port wiring/latch ownership and access timing are machine-specific; Graphics II pixel work needs its own mode/bank contract.

**Gap:** Extract pattern/font uploads; then mode-specific bitmap-like editing. Sources: [probe-microsoft-msx1](evidence.md#probe-microsoft-msx1), [region-microsoft-msx1](evidence.md#region-microsoft-msx1), [record-microsoft-msx1](evidence.md#record-microsoft-msx1). Tracking: [#123](https://github.com/code198x/docs/issues/123), [#131](https://github.com/code198x/docs/issues/131).

### nintendo-game-boy

**Inspected path:** DMG 2bpp tiles/background map; LCD-off region. Pattern upload is separate from name entries; VRAM access policy and shared glyph instances matter. LCD-off room loading is not a live update queue.

**Gap:** Standalone tile install/replace first; later bounded live transfers. Sources: [probe-nintendo-game-boy](evidence.md#probe-nintendo-game-boy), [region-nintendo-game-boy](evidence.md#region-nintendo-game-boy), [record-nintendo-game-boy](evidence.md#record-nintendo-game-boy). Tracking: [#123](https://github.com/code198x/docs/issues/123), [#131](https://github.com/code198x/docs/issues/131).

### nintendo-nes

**Inspected path:** CHR assets, PPU nametables/OAM in NROM callers. Existing cartridge assets do not prove writable CHR RAM. Mapper/CHR-ROM versus CHR-RAM choice, VBlank budget and attribute granularity must be named.

**Gap:** Explicit font asset/CHR-RAM variant, then queued updates. Sources: [probe-nintendo-nes](evidence.md#probe-nintendo-nes), [nes-assets](evidence.md#nes-assets). Tracking: [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

### oric

**Inspected path:** HIRES six-pixel bitmap region. Pixel bytes must preserve bit 6; serial attribute columns affect following pixels. Text-character RAM is a separate mode/path, not the HIRES bitmap.

**Gap:** Safe six-bit plot/read/span backend; separate character definitions. Sources: [probe-oric](evidence.md#probe-oric), [region-oric](evidence.md#region-oric), [record-oric](evidence.md#record-oric). Tracking: [#127](https://github.com/code198x/docs/issues/127), [#124](https://github.com/code198x/docs/issues/124), [#125](https://github.com/code198x/docs/issues/125), [#126](https://github.com/code198x/docs/issues/126), [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

### sega-game-gear

**Inspected path:** Mode 4 pattern/name-table region with viewport crop. Four-plane tile encoding, palette entries, logical map versus viewport and port/latch ownership; no native per-pixel framebuffer API supplied.

**Gap:** Reusable pattern loading and safe replacement; pixel edits through tile staging. Sources: [probe-sega-game-gear](evidence.md#probe-sega-game-gear), [region-sega-game-gear](evidence.md#region-sega-game-gear), [record-sega-game-gear](evidence.md#record-sega-game-gear). Tracking: [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

### sega-master-system

**Inspected path:** Mode 4 pattern/name-table region. Four-plane tile data and two-byte name entries; upload size/access budget differs from changing a name entry.

**Gap:** Pattern/font install and timed replacement; descriptor-aware text. Sources: [probe-sega-master-system](evidence.md#probe-sega-master-system), [region-sega-master-system](evidence.md#region-sega-master-system), [record-sega-master-system](evidence.md#record-sega-master-system). Tracking: [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

### sega-sg-1000

**Inspected path:** TMS-family Graphics I pattern/name region. Installed patterns and grouped colour data are separate from name writes. Port wiring/latch ownership and access timing are machine-specific; Graphics II pixel work needs its own mode/bank contract.

**Gap:** Extract pattern/font uploads; then mode-specific bitmap-like editing. Sources: [probe-sega-sg-1000](evidence.md#probe-sega-sg-1000), [region-sega-sg-1000](evidence.md#region-sega-sg-1000), [record-sega-sg-1000](evidence.md#record-sega-sg-1000). Tracking: [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

### sinclair-zx-spectrum

**Inspected path:** Interleaved bitmap; fixed-cell software text; BASIC UDGs. Verified address calculation is not pixel writing. Attributes cover 8×8 cells; masked shifts and clipping can support text without pretending colour is per pixel.

**Gap:** Bounded pixel/read/span/box family first; later pixel-positioned glyphs. Sources: [probe-sinclair-zx-spectrum](evidence.md#probe-sinclair-zx-spectrum), [spectrum-address](evidence.md#spectrum-address), [spectrum-char](evidence.md#spectrum-char), [spectrum-shape-lesson](evidence.md#spectrum-shape-lesson), [spectrum-udg-lesson](evidence.md#spectrum-udg-lesson), [spectrum-segments](evidence.md#spectrum-segments), [spectrum-positioned](evidence.md#spectrum-positioned). Tracking: [#122](https://github.com/code198x/docs/issues/122), [#124](https://github.com/code198x/docs/issues/124), [#125](https://github.com/code198x/docs/issues/125), [#126](https://github.com/code198x/docs/issues/126), [#131](https://github.com/code198x/docs/issues/131).

### sinclair-zx80

**Inspected path:** ROM text output; software-generated display. Selected examples print cells and query CPU RAM. Preserve display-file/refresh ownership; do not infer a bitmap or writable font from a RAM-only proof.

**Gap:** Stock glyph/coarse composition and display-aware text; research advanced variants separately. Sources: [probe-sinclair-zx80](evidence.md#probe-sinclair-zx80). Tracking: [#129](https://github.com/code198x/docs/issues/129), [#126](https://github.com/code198x/docs/issues/126), [#131](https://github.com/code198x/docs/issues/131).

### sinclair-zx81

**Inspected path:** ROM text output; software-generated display. Cell/block graphics and any high-resolution extension have different resolution, RAM and refresh obligations; neither follows from the query fixture.

**Gap:** Stock glyph/coarse composition; separately qualify advanced display variants. Sources: [probe-sinclair-zx81](evidence.md#probe-sinclair-zx81). Tracking: [#129](https://github.com/code198x/docs/issues/129), [#126](https://github.com/code198x/docs/issues/126), [#131](https://github.com/code198x/docs/issues/131).

### sord-m5

**Inspected path:** TMS-family Graphics I pattern/name region. Installed patterns and grouped colour data are separate from name writes. Port wiring/latch ownership and access timing are machine-specific; Graphics II pixel work needs its own mode/bank contract.

**Gap:** Extract pattern/font uploads; then mode-specific bitmap-like editing. Sources: [probe-sord-m5](evidence.md#probe-sord-m5), [region-sord-m5](evidence.md#region-sord-m5), [record-sord-m5](evidence.md#record-sord-m5). Tracking: [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

### spectravideo-svi-328

**Inspected path:** TMS-family Graphics I pattern/name region. Installed patterns and grouped colour data are separate from name writes. Port wiring/latch ownership and access timing are machine-specific; Graphics II pixel work needs its own mode/bank contract.

**Gap:** Extract pattern/font uploads; then mode-specific bitmap-like editing. Sources: [probe-spectravideo-svi-328](evidence.md#probe-spectravideo-svi-328), [region-spectravideo-svi-328](evidence.md#region-spectravideo-svi-328), [record-spectravideo-svi-328](evidence.md#record-spectravideo-svi-328). Tracking: [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

### tatung-einstein

**Inspected path:** TMS-family Graphics I pattern/name region. Installed patterns and grouped colour data are separate from name writes. Port wiring/latch ownership and access timing are machine-specific; Graphics II pixel work needs its own mode/bank contract.

**Gap:** Extract pattern/font uploads; then mode-specific bitmap-like editing. Sources: [probe-tatung-einstein](evidence.md#probe-tatung-einstein), [region-tatung-einstein](evidence.md#region-tatung-einstein), [record-tatung-einstein](evidence.md#record-tatung-einstein). Tracking: [#128](https://github.com/code198x/docs/issues/128), [#131](https://github.com/code198x/docs/issues/131).

## Recommended first batch

Two small strands, six systems. This is the selected recommendation for review, not an implementation started by this audit.

1. **Pixels, spans and boxes: Spectrum 48K, BBC Micro MODE 4, Dragon 32 PMODE 4.** Supply bounded set/clear/XOR/read, horizontal/vertical spans, and outlined/filled rectangles. Reuse Spectrum addressing and the BBC/Dragon bitmap/layout knowledge already present. These compare Z80, 6502 and 6809 and interleaved versus linear layouts without starting with packed-colour complexity. Keep coordinates, clipping/rejection, endpoint rules, colour ownership and stack/state explicit.
2. **Install and replace glyphs: unexpanded PAL VIC-20, MSX1 Graphics I, Game Boy DMG.** Extract the existing setup into callable routines: include/init/install/select/replace, then show one glyph shared by multiple cells changing in place. Compare CPU-visible character RAM, port-addressed VRAM and LCD-off tile access. MSX colours are grouped; Game Boy uses 2bpp tile rows; VIC-20 colour/mode bits are separate. Preserve fixed-ROM PET/Aquarius contrasts without inventing a font upload facility.

Each strand needs a small complete caller, inspectable original glyph/picture data, precise inputs/outputs, memory/register/interrupt ownership, failure cases, independent memory/native-pixel checks, and at least one deliberate faulty control. Show work counts and storage costs first. Measure relevant workloads before claiming speed: compare a partial-byte edge with an aligned span, and a name-entry change with glyph replacement affecting many cells. Report tool/model/mode and display-access policy; a blanked reset run is not a live-display timing result.

After these, general lines and curves can reuse a span/pixel backend; text can reuse masked/shifted object code. CPC packed pixels, Oric serial attributes, Atari ANTIC layouts, Amiga plane/blitter variants and constrained character/video systems remain explicit follow-ups. Do not require every shape to be built by repeatedly calling the slowest pixel routine.

## Maths for Games connections

- [maths-unit-06](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/craft/maths-for-games/unit-06.mdx#L1) — Coordinates, origin, axes and translating a point: use for pixel placement and screen/world conversion.
- [maths-unit-07](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/craft/maths-for-games/unit-07.mdx#L1) — Distances and right triangles: use for endpoint differences and radius/distance questions.
- [maths-unit-08](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/craft/maths-for-games/unit-08.mdx#L1) — Sine/cosine and direction: useful comparison for sampling circles, rather than pretending trig is the only rasterisation method.
- [maths-unit-09](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/craft/maths-for-games/unit-09.mdx#L1) — Radians: useful when a drawing example actually accepts angles or arcs.
- [maths-unit-11](https://github.com/code198x/website/blob/0441deeb55c76ad6f0ea61cc722e753c7cb7b300/src/content/curriculum/craft/maths-for-games/unit-11.mdx#L1) — Fixed-point and rounding: connect integer stepping, accumulated error and scaling choices.

Those five are **existing authored units**. The current overview lists transformations/3D as planned topics; that does not mean matrix transforms or scalable fonts are taught already.

Track the missing drawing explanations explicitly: gradients and incremental line error; inclusive/exclusive edges; symmetry and midpoint circle/ellipse decisions; clipping; area and span filling; glyph-local versus screen coordinates; nearest-neighbour scaling; advance width versus bitmap width; and logical circles versus non-square display pixels. Explain a decision with a picture or small worked example, then link to the implementation which makes the rounding/memory/runtime cost visible.

Add reciprocal links where both pages exist and the connection helps a reader. Keep the routines locally understandable; Maths for Games is support, not a compulsory course before plotting a point. A diagram or interactive experiment can help explain the maths but cannot replace the actual reusable implementation. New explanations are backlog candidates, not existing coverage or a commitment to a whole new game sequence.

## Backlog reconciliation

Existing umbrella [docs #117](https://github.com/code198x/docs/issues/117) remains the library expansion tracker. [Drawing tracker #121](https://github.com/code198x/docs/issues/121) is its native sub-issue, with ten family-sized child issues. The two implementation pilots are [#122](https://github.com/code198x/docs/issues/122) and [#123](https://github.com/code198x/docs/issues/123); [#131](https://github.com/code198x/docs/issues/131) connects their maths explanations. Existing [website #802](https://github.com/code198x/website/issues/802) owns editorial imagery, not drawing routines. Closed correctness/evidence work (including samples #90 and website #690) stays completed; useful verified code is reused rather than reopened. Vectrex proposal/qualification issues docs #4/#6 concern a system outside this 30-system registry and are not duplicated here.

All 10 docs issues, 7 samples issues and 282 website issues (open and closed) were inspected through a complete listing below the 3,000-result limit, plus docs #117's body/comments and the pending region PRs. Title/body searches were followed by reading overlapping issue bodies; a keyword hit was not treated as a duplicate automatically. The new issues track missing routine contracts, algorithms, extraction, explanation or verification, not one ticket per missing matrix square. See [issues.md](issues.md) for created and reused tracking.

## Revisions and reproducibility

- code-samples default branch inspected at `8555ae938d09db9e22c26deabfb355341904ff9c`.
- website default branch inspected at `0441deeb55c76ad6f0ea61cc722e753c7cb7b300`.
- code-samples pending character-region source at `15f3b795e75e88c505bf47b020c3aa6555414643`; draft status checked on 20 October 2026.
- website pending character-region source at `cf5ef651166ec993a4feb5bc65c5153d307ff4b5`; draft status checked on 20 October 2026.

[Machine-readable inventory](inventory.json), [matrix CSV](matrix.csv), [source ledger](evidence.json) and [readable evidence](evidence.md) retain the findings. The source ledger names exact paths, revisions, first relevant lines and content hashes. Candidate searches inspected 1,892 sample text files and 755 authored curriculum/pattern files, then read the actual candidates and selected execution records. Comments, “font” mentions, and a shape-shaped block of printed Xs do not establish a reusable routine.

The validator is retained beside the audit, with collection boundaries and counts. It checks all 30 registry IDs, exact Git objects/source hashes, source URLs, coverage counts and the issue reconciliation. It does not rerun emulator evidence or promote implementation status.
