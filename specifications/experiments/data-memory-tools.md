# Data, memory and small development tools

**Status:** Source-reviewed progression and proposed follow-up work. The first bounded improvement is authored locally in Crates unit 07: a representation trace, ownership explanation and storage calculation. No converter, compression system or changed game program is claimed. Scope remains Spectrum, C64, NES and Amiga.

This applies the [recurring progression map](../recurring-progressions.md), [asset specification](../graphics-and-audio.md) and [audio progression](audio-progression.md). The [profiling plan](profiling-progression.md) owns measurement practice. We introduce a tool when a repeated, understood task needs it; there is no new generic asset pipeline or prerequisite tool-language course.

## Three representations, sometimes the same bytes

**Authoring representation** makes editing convenient: a room drawn with symbols, a pixel grid, named animation frames or a musical phrase. **Stored representation** is the file or embedded data we ship. **Runtime representation** is what the game and hardware consume: decoded cells, pointers and counters, aligned sprite blocks, PPU tiles or DMA-readable sample bytes.

They may coincide. A directly embedded sample can be ready for hardware; a textual map can need decoding. Say whether “stored” means bytes in a source file, an executable, ROM or a media container. An assembly include's text size is not its assembled byte count. A smaller archive does not imply less working RAM or faster random access during play.

For each asset, follow one example all the way through:

`editable source → preparation/validation → stored payload → load/decode/transfer → runtime reader`

Name each reader and writer, the unit of length, its bounds, where the bytes live, and how long they must remain valid. A build script is part of this explanation, not a substitute for it. If a transformation drops information, say what is discarded.

## Actual assets and build paths inspected

Paths here are relative to [code-samples](https://github.com/code198x/code-samples). Source inspection establishes the current design, not a new successful build or target run.

| Project | Authoring → stored → runtime evidence | Next useful question |
|---|---|---|
| Spectrum Crates | `sinclair-zx-spectrum/basic/crates/teaching/unit-07/snippets/step-01-edits.bas` contains eight DATA strings; the loader fills `g(8,8)` and stores the player separately. Unit 08 adds checks and prevents play after invalid loading. | Why keep the starting map while runtime state changes? Why do 64 cells not mean a 64-byte BASIC array? |
| Spectrum Night Patrol | The existing unit 07 lesson explains a phase record: pose, visible count, change count, signed cell changes. Teaching verification includes `build.py`, `audit.py` and `check.py`. | Follow a prepared record into the reader; distinguish number of visible cells from number of changes. Do not assume a verification script is already a learner-facing exporter. |
| Spectrum Meteor Storm | `sinclair-zx-spectrum/assembly/meteor-storm/assets.py` emits `assets.inc` for named checkpoints from 24-bit rows, eight shifts and deterministic event data. The renderer consumes four bytes per row. | Host preparation avoids runtime shifts by spending storage. The script currently writes multiple checkpoints: a beginner converter should not unexpectedly regenerate the whole course. |
| C64 Starfield | `commodore-64/assembly/starfield/unit-04/steps/step-01.asm` places ship data at `$2000` and bullet data at `$2040`; the Makefile builds cumulative steps with Asm198x's ACME dialect and PRG output. | Separate the 63-byte sprite picture from the 64-byte address block and the selected VIC bank/pointer. |
| NES Dash | `nintendo-entertainment-system/assembly/dash/unit-14/dash.asm` embeds two-plane tile rows. Twenty-two tiles use 352 bytes, with `.res 8192 - 352` padding the CHR segment. The Makefile uses Asm198x's ca65 dialect to produce the ROM. | Used tile payload, padded cartridge section and runtime PPU access are different budgets. This checkpoint does not load a PNG directly. |
| Amiga Flock | `commodore-amiga/assembly/flock/unit-11/flock.asm` puts sprites and an eight-byte waveform in `section data,data_c`; AUD0LEN is four words. Its Makefile assembles a hunk executable, then invokes Build198x to master an ADF. | Disk/container size differs from loaded Chip RAM; a live DMA pointer requires the sample storage to remain valid. |

A bounded generator check in this pass ran `assets(1)` without writing files and
matched the existing `checkpoints/draw-ship/assets.inc` exactly: 512 sprite bytes.
This verifies that conversion/output pair, not target execution or all checkpoints.

Musical phrases in Starfield/Dash/Flock provide later small data formats: pitch or period, duration, rest and loop/stop markers. They need locally defined meanings, not one imposed byte format. Animation can reuse a frame definition plus a small order/duration table before any general animation editor is justified.

### Tool capability boundaries

The inspected Build198x README and CLI source implement image conversion, beeper phrase output and ADF mastering. The local `build198x --help` executable confirms those three command families. Its README documents newer ADF operations more broadly than that installed help; pin the build and check the chosen subcommand before writing a lesson recipe.

Image outputs documented in the inspected source are Spectrum screen data, C64 screen formats and Amiga ILBM. This is **not** evidence of a generic sprite/map/animation exporter or NES CHR converter. The beeper tool produces phrase data/assembly and an audition WAV, not a complete player. ADF mastering packages an executable; it does not make its runtime allocations or DMA placement correct. Do not invent compression or packing commands from the wider project ambition.

Meteor Storm's Python script is a concrete generator, but its existence does not establish validation, a round-trip importer or a supported GUI. Keep any new teaching converter beside the consuming sample and give it one input/output contract. Move reusable functionality into a family tool only when a real second consumer justifies it.

## Staged learning through existing projects

| Stage | Motivation and prerequisites | Small solution / exercise | Observable result and later application |
|---|---|---|---|
| Literal values | A first shape, room cell or cue must exist. Need numbers, coordinates and one direct output operation. | Inspect a single embedded row or note; change one value and predict the result. Use the existing introductory graphics/audio lessons. | The learner connects value to output and restores the baseline. No exporter yet. |
| Names and structures | Repeated magic values obscure what is being changed. Need variables/constants and a routine contract. | Name width, height or a note; describe one record’s fields and units. Use Crates’ alphabet, Meteor Storm’s object records, Starfield sprite constants and Flock sound parameters. | Explain a count versus an index and a byte count versus a word count. Changing a name's value has a predictable scope. |
| Small formats | Several rows, frames or notes must be read consistently. Need loops and indexing. | Crates units 07–08: trace a row, then diagnose malformed input. Later trace Dash's two bitplanes or a phrase's rest/terminator. | Reader and writer agree on ordering, bounds and termination. “Zero” can mean a real value, a rest or a terminator only under an explicit format contract. |
| Shared definitions | Repetition wastes editing effort or storage. Need one working definition and stable identifiers. | Reuse a tile/frame, then change an animation/order table without copying the image; reuse two musical patterns in an order. | Compare changed output and bytes. Discuss the consequence of editing a shared definition; sharing data does not require shared mutable playback state. |
| Conversion | Hand-encoding understood data is repetitive or error-prone. Need the complete small output format first. | Extend Crates with a proposed eight-row text-to-BASIC-DATA converter; later show one Meteor Storm row becoming eight prepared shifts. Follow with a Starfield pixel-grid export or Dash two-plane tile export only in their own game contexts. | Inspect exact output and the consuming reader, rebuild deterministically, and diagnose an old generated file. Keep original source editable and generated output clearly named. |
| Validation | A wrong dimension, symbol, range or placement can silently damage output. Need valid examples and the reader’s bounds. | Validate before writing final output; report file, row/column or record, actual value and expected constraint. Use Crates unit 08's existing fault cases as the first fixture set. | A malformed input leaves no plausible half-built asset. A restored valid input produces the expected semantic state. |
| Constraint-led optimisation | A measured storage or transfer limit is exceeded. Need a budget and a working uncompressed baseline. | Compare raw data with shared definitions or a simple run-length representation for a selected map. Include decoder, working buffer and load time. | Choose on total cost. Retain raw data if compression makes the required update late or complicates access without a useful saving. No mandatory compressor in v1. |

## Memory and movement ledger

For each comparison record **payload bytes, padding/alignment, tables/pointers, decoder code, permanent runtime storage, temporary storage, peak overlap, and preparation/transfer time**. Include interrupt/stack space when drawing the memory map. Do not add ROM payload to RAM allocations as though they occupy the same address space.

- **Crates:** eight by eight means 64 symbols/cells. A hypothetical one-byte-per-cell encoding has a 64-byte grid payload, but the actual BASIC numeric array has its own representation and metadata. Player coordinates are separate. DATA remains the reset source; `g` is mutable; `m$`, `b$` and loop variables are temporary loading state. The improvement in unit 07 teaches this without requiring an exact BASIC memory audit.
- **Meteor Storm:** one 24×16 monochrome image has 48 raw pixel bytes if tightly stored. The current generator emits `8 shifts × 16 rows × 4 bytes = 512 bytes` per image. Three such tables use 1,536 assembled bytes, excluding events and other state. This spends memory to remove shifting from play; it is not compression. Confirm runtime placement from the assembled map before claiming the whole game fits.
- **Starfield:** a 24×21 single-colour sprite has `24 × 21 / 8 = 63` picture bytes, addressed in 64-byte blocks. Two blocks reserve 128 bytes. Explain the selected VIC memory bank, sprite-pointer location and CPU/VIC visibility, not just an address divisible by 64.
- **Dash:** an 8×8 two-bitplane tile occupies 16 bytes; 22 tiles occupy 352 bytes. The inspected ROM reserves 8,192 CHR bytes, so fewer used tiles need not shrink this cartridge image. CHR-ROM is not a mutable CPU drawing buffer. Later CHR-RAM loading needs explicit transfer work and a safe PPU-access schedule.
- **Flock:** the inspected eight-byte waveform is four audio words. The data must be accessible to Paula in Chip RAM and appropriately aligned for its word-based DMA access. Keep it alive while DMA uses it; a new CPU-side pointer does not by itself transfer hardware ownership. Count sample duplication, attack/loop storage and prepared buffers separately from the ADF file.

Hardware anchors checked in the reference library: Commodore, *Commodore 64 Programmer’s Reference Guide*, sprite-definition/pointer discussion, pp. 132–134; public NESdev PPU pattern-table research, “Pattern tables” (two planes and 16-byte tiles); Commodore-Amiga, *Amiga Hardware Reference Manual*, second edition, chapters 2 and 5 (chip access, audio location/length/DMA); Sinclair, *ZX Spectrum BASIC Programming*, chapters 6, 8 and 12. Source code establishes these games' layouts; hardware references establish the access restrictions. Verify exact alignment/address masks and clocked transfer limits for the selected machine before a new exporter emits addresses.

## Lifetimes, deadlines and tests

Start with one buffer and a clear reader/writer. Later, draw a timeline: prepare inactive data, validate it, publish it at a safe boundary, let the reader finish, then reuse the old storage. An asynchronous transfer can outlive the routine that started it. Explain DMA completion or playback end before recycling its source. Teach double buffering only after this conflict has been observed; two buffers consume memory and still need an ownership protocol.

Load/decode at room entry or a title transition when that fits the game. For work required during play, bound each transfer and define what happens if the next chunk is not ready. A smaller packed asset can add decode latency, require both packed and unpacked forms at once, or make random cell access expensive. Compare copy time, decode time and hardware transfer time separately. Keep guest timing distinct from host exporter duration.

Use tests matched to the promised property:

- Known input → exact expected small output for a stable, deterministic encoder; inspect at least one row by hand.
- Invalid input → a useful diagnostic and no replaced valid output. Include dimensions, unknown symbols, out-of-range fields and missing references.
- Decode/consume → expected game state, not merely a matching screenshot. Crates player coordinates and the underlying floor/target must both survive.
- Repeat build → matching output for a deterministic contract; record tool version and inputs when generation uses parameters or seeds.
- **Round trip only when intended:** a lossless reversible map encoding can require `decode(encode(source))` to preserve its semantic contents. Pixel quantisation, deduplication, discarded comments, lossy sample conversion or a screen-image exporter need their own stated guarantees, not a blanket promise to recreate the original authoring file.

Keep fixtures tiny and errors visible. A converter can validate dimensions and symbols without proving a puzzle is solvable or an arrangement sounds good. Separate format validity, hardware validity and creative/gameplay judgement.

## First local improvement and next bounded work

**Authored now:** Spectrum Crates `unit-07-read-the-room-from-a-map.mdx` adds the three-representation table, a trace of P at row 6/column 3, a question about grid-plus-player state, and the 64-cell versus hypothetical 64-byte distinction. It explains reset-data lifetime and decoding before play, links to unit 08 validation and Night Patrol's prepared changes, and leaves the program unchanged. This is a lesson improvement, not a new converter implementation or execution claim.

**Implemented tool exercise:** the optional converter and unit-08 investigation below now cover this first authoring → generation → consumption boundary. Further exporters remain proposals tied to a demonstrated game need.

Then expose Meteor Storm’s 48-to-512-byte preparation trade-off in unit 02; Starfield’s sprite block budget beside its first sprite data; Dash’s payload-versus-CHR-segment budget beside unit 14; and Flock’s sample lifetime/word-length ledger beside unit 11. Add animation or music pattern reuse after the reader has one working frame/phrase. Compression, streaming and generic format support remain later, constraint-led work. Bright Spark remains first in the previously agreed implementation queue; this small prose improvement does not start a competing engine project.


## Crates converter implementation

C04b was accepted to continue:
`code-samples/sinclair-zx-spectrum/basic/crates/teaching/tools/` contains
`map_to_data.py`, the known-valid `room.txt`, a small standard-library test file,
and usage/format/failure documentation. It targets unit 08's single room at
DATA lines 8000–8070, not a generic asset pipeline.

The whole input is validated before output generation; a completed temporary
file replaces the output. Invalid input leaves a previous output unchanged,
so the README explicitly warns that its existence does not mean the latest
edit succeeded. Input/output identity is rejected, including aliases to the
same file. No trimming, symbol substitution, solvability claim or round trip
is introduced. Four host test groups passed on 22 September 2026, covering
exact existing DATA, text endings, format and count failures, combined symbols,
and command-line failure safety. A direct CLI conversion also succeeded.

The BASIC consumer and all game checkpoints remain unchanged.

## Crates generated-data investigation

C04c adds an optional section to Crates unit 08, linked from unit 07's three
representations. Learners compare all eight generated lines with the accepted
room, predict what a rejected X does to existing output, and explain why the
unchanged consumer can still run that old room. The repair deliberately moves P
from column 3 to column 4: successful generation alone does not update the
program in the Spectrum. Learners replace the DATA, check movement/restart,
then restore the original authoring map through the same chain.

A folded hint identifies the file boundary; a separate explanation follows the
prediction opportunity. The final question connects offline conversion with
Night Patrol unit 07's preparation inside the running game without equating
their timing or implementation. No converter redesign or generic pipeline is
introduced. `teaching/tools/verify_consumer.py` reproduces the consumer checks
using the existing ROM-entry and read-only grid/display verifier. Four consumer cases passed on 22 September 2026 in native Emu198x Spectrum
0.24.0, 48K PAL: original, stale, changed and restored DATA. Each checks grid,
player, display, a move and restart; tokenised non-map program lines are unchanged.
`teaching/tools/consumer-results.json` records source/converter/emulator hashes.
Four host converter test groups and the 2,468-page website build also pass.
Browser inspection confirms the optional section and folded hint render. This is
configuration-specific emulator evidence, not original-hardware or learner testing.



## Game data and Foundations review

R4b covers Crates07, Flock03/15 and Foundations From Source to Silicon04. Crates distinguishes authoring strings, DATA and the numeric grid with separate player coordinates; its new prediction traces `+` through the temporary floor value to target code 2. The supplied map remains unchanged and validation remains the following lesson. Source SHA-256 `47ebd03e7ded60bfe28319a61fe96d0535dee6f07b26b3f79d14deb22bd541e7` matches the retained loader checkpoint evidence.

Flock03 retains runtime sprite packing, but its summary now qualifies the two-phase beam wait. Its snippet includes the source's beam mask. The cooldown explanation states that the one-to-zero update returns without sampling input. A source-derived host trace gives ten accepted hops at updates 0, 7, …, 63: first-to-tenth spans nine intervals, distinct from ten full intervals. The exercise now respects the 0–240 top-coordinate bounds rather than asking a 16-pixel sprite to traverse 256 rows. Source SHA-256: `755152516e790388e08f3ec0e8457823390d3baaf22d1565d1bb96cd1238ee83`.

Flock15's explanation and source/snippet comments distinguish the wrapping main-loop counter from an independent power-on clock. The unmixed 16-bit (7,9,8) cycle was re-enumerated: 65,535 non-zero states, low-three-bit zero 8,191 times and each other pattern 8,192. These are not frequency claims for the frame-mixed game. The revised source is SHA-256 `fc13daa0532b485661d2c35c057dd048d81e765318767f8d2d85472e105c2537`; Asm198x 0.0.58 rebuilt its hunk executable byte-identically to the maintained `flock`. No instruction/data or disk changes were required.

Foundations04 retains the corrected tool/portability explanation, asks for a decision before revealing the answer, and connects an unfamiliar crate fault to the earlier diagnosis method. Adjacent unit 05 still contradicts these principles in its universal timing and assembly claims; R4d owns that bounded follow-up. This review does not certify the rest of that module.

No new native game run, PAL timing measurement, listening review, original-hardware check or learner trial is claimed. The numeric checks are host models of inspected source. Crates and Flock03 game sources are unchanged; only comments changed in Flock15.

Local validation passes: isolated-output Astro build (2,468 pages), diff whitespace and 16 browser combinations (four pages, 390/1280px, light/dark). New explanations open by keyboard, code includes render and no page-level horizontal overflow appears. Representative mobile/desktop screenshots were inspected. The diagnosis link resolves. These are local rendering checks, not publication or a full accessibility audit.
