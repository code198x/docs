# Game loops and machine ownership

The first expansion supplies a reusable frame wait or frame-clock consumer and a complete visible caller for each core system. A BBC Model B example keeps MOS ownership intact. The Electron runs the same MOS-facing source with its own OS/BASIC record; MODE 6 provides a common text display without pretending the display hardware is the same.

The source implementation is [samples PR #109](https://github.com/code198x/code-samples/pull/109), based on verified input readers and existing lesson/caller techniques. Existing pattern URLs are improved rather than replaced. New BBC/Electron entries and one comparison page extend discovery to machines with actual patterns, without promoting their curriculum tiers. Parent work remains [#117](https://github.com/code198x/docs/issues/117); the inventory is [PR #118](https://github.com/code198x/docs/pull/118).

## Contracts

| Configuration | Boundary and owner | State and missed time |
| --- | --- | --- |
| PAL C64 | Main waits for a fresh raster bit-8 transition; caller takes over IRQ/CIA resources | No persistent wait state; lost boundaries are not counted or replayed |
| 48K PAL Spectrum | ROM IM1 services FRAMES; main accepts one low-byte sample | Two state bytes; gap must be under 256 frames; delta does not automatically replay simulation |
| A500 OCS PAL, Kickstart 1.3 | Main owns and polls a new VERTB request after clearing pending work | Latch is not a counter; another consumer must not acknowledge the same request |
| NTSC NROM NES | NMI increments a byte; main consumes a captured clock value | Three state bytes; under-256-frame gap; ISR and main resource ownership are explicit |
| BBC Model B | MOS OSBYTE 19; keep the MOS IRQ path running | Five-byte wrapper, no private wait state; keyboard and text use MOS services |
| Acorn Electron | Same MOS-facing executable and MODE 6 loader, separately tested | Same API does not establish the same loading or workload duration |

Helper code sizes with Asm198x 0.0.64 are C64 11 bytes, Spectrum 37, Amiga 18, NES 27 and MOS wrapper 5. Spectrum/NES sizes include their clock initialisation helpers; state bytes and all callers/ROM services are excluded. They are storage measurements, not comparable runtime benchmarks. Contention, ROM work, DMA and interrupt load affect the budget.

## Native execution

Every positive case uses ordinary native frame advancement and real key/controller events. There are no positive host writes to synthesize the update result. Each caller updates once, then optionally performs a deliberately excessive CPU workload. Release input restores the original workload. Clock consumers record missed announcements; polling waits deliberately wait anew.

| Configuration | Normal updates in 30 native frames | Slow workload | Recovered | Unpaced updates in 10 frames |
| --- | ---: | ---: | ---: | ---: |
| C64 | 30 | 8 | 30 | 973 |
| Spectrum | 30 | 9 | 30 | 1322 |
| Amiga | 30 | 5 | 30 | 3421 |
| NES | 30 | 11 | 30 | 1086 |
| BBC Micro | 30 | 10 | 30 | 191 |
| Electron | 30 | 5 | 30 | 100 |

The slow workloads differ across CPUs. These observations demonstrate the loop policy under overload, not a machine ranking, frame-budget benchmark or claim about typical games.

The same normal-rate guard rejects each unpaced negative control. Writable-RAM callers temporarily replace wait_frame with a return. The NES cartridge correctly rejects ROM pokes, so its negative control assembles a same-sized caller with the wait call replaced by three NOPs. Screenshots are captured before intervention. The source recipe records source/observer/tool/firmware hashes and exact startup semantics; firmware is not distributed.

Spectrum checks snapshot startup and an independent fresh-ROM TAP load. Amiga cold-boots its ADF. NES starts from cartridge reset. The Acorn examples type a generated numbered BASIC loader, reserve the executable above HIMEM and compare installed executable bytes while excluding only their declared three mutable state bytes. The check waits for byte installation with a bounded timeout rather than assuming both BASIC implementations finish at the same delay.

The normal-rate guard checks a bounded range around the requested window; the observed values above are retained results. The byte clocks cannot distinguish a gap of exactly 256 frames from no change. No unlimited catch-up, exact CPU-time cost, original-hardware or whole-emulator conformance claim follows.

## C64 startup finding

The tested C64 MCP startup accepts --load but leaves the PRG unimported. Its existing script startup path imports the same file, and the caller then runs correctly. The recipe uses that real-ROM script import, resumes its booted snapshot in MCP and types RUN. The record states this path rather than claiming direct MCP import. [Emu198x #1858](https://github.com/emu198x/emu198x/issues/1858) tracks the narrower remaining import omission alongside the earlier startup-parity work. No emulator code was changed for this slice.

## Further systems

BBC and Electron demonstrate that selected patterns can arrive before a full track. The Electron shares the MOS implementation because a tested service contract permits it; a shared 6502 alone would not justify reuse.

VIC-20, MSX and Master System remain useful next implementation candidates. The current sources have native binaries/profiles, but this slice does not claim to have loaded and qualified their new loop programs. VIC-20 needs explicit region/RAM and VIA/display ownership. MSX needs a named firmware/model plus BIOS/direct-VDP choices. Master System needs a homebrew cartridge and its own interrupt/VDP/controller contract. CPC464 has an existing qualification proposal and should remain independent of later disk models.

Coordinate those runnable examples and capture paths with [readiness #3](https://github.com/code198x/docs/issues/3), and keep each outcome separate. A build of an emulator is not a passing program test. Do not require their new tracks or all variants before publishing one useful pattern. Future choices can extend the library without changing current system-game priorities.

## Verification recipe

Run `python3 scripts/verify-game-loops.py --help` from code-samples. Provide the native emulator directory, Spectrum executable, existing firmware locations and Build198x. The default matrix covers the core four plus BBC; `--include-electron` adds the independently recorded shared-source run. `--only` selects a single configuration.

Keep complete demo.asm sources, frame.inc contracts, Makefiles and retained verification/results.json files together. The new input readers preserve their existing paths/content from the earlier prototype. The whole loop expansion is additive to those open source/UI/specification PRs; no merge or publication is implied by these notes.
