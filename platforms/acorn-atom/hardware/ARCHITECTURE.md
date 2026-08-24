# Acorn Atom — Architecture

A curriculum-flavoured map of the Acorn Atom: how memory is laid out, what the CPU
is, and how the video and sound hardware work. The aim is the mental model a
learner needs before writing the first unit — not exhaustive chip detail. For
that, follow the citations into the primary reference library.

> **Scaffold doc.** Established facts with citations, plus TODOs where depth is
> still owed. `§` citations refer to the **Atom Technical Manual (Issue 2)** —
> `reference/by-system/acorn-atom/unknown-atom-technical-manual-issue-2.md`
> — and **Atomic Theory and Practice** —
> `reference/by-system/acorn-atom/1980-atomic-theory-and-practice.md`
> — as noted. The Atom is **not** a BBC Micro; do not import BBC facts here. Both
> sources are OCR'd scans, so treat addresses with care.

## CPU

- **MOS 6502 at ~1 MHz.** Standard NMOS 6502 instruction set — the same CPU family
  as the C64 and NES (tech manual: IC22 labelled "6502-1MHz Micro-Processor";
  §Block Diagram).
- **No CPU/video contention trickery to rely on.** The 6502 and the MC6847 VDG
  share the video RAM; the processor is gated to write video RAM during the
  vertical-blanking period (signalled by the peripheral interface) to avoid
  on-screen interference (§Video). This vsync signal also drives the BASIC `WAIT`
  statement (§Video).

Hex is written with a leading **`#`** throughout Atom documentation (`#8000`) —
note this collides visually with the 6502's immediate-mode `#`, so read Atom
source carefully (§Memory Map note: "The `#` sign … indicates a hexadecimal
number").

For the instruction set and addressing modes, see
[`../language/6502-quick-reference.md`](../language/6502-quick-reference.md).

## Memory map

The 6502 sees a 64 KB address space. The Atom is heavily I/O- and ROM-mapped in
its upper half, with RAM concentrated low. Confirmed regions (§Memory Map,
§Lower Text Space Extension, §I/O):

| Range | Use | Source confidence |
|-------|-----|-------------------|
| `#0000`–`#03FF` | **Block zero RAM** — zero page, 6502 stack, scratchpad/workspace. "Should not normally be accessed by the user." | Confirmed (§Memory Map) |
| `#0400`–… | Reserved (Eurocard) / low RAM | Partial — OCR |
| `#2800`–`#3BFF` | **Lower text space** RAM expansion (BASIC program RAM when fitted; 2114 chip pairs added in order) | Confirmed (§Lower Text Space Extension) |
| `#8000`–`#9FFF` | **Video RAM / upper text space / graphics space** (unexpanded: `#8000`–`#83FF` is the base 1 KB; higher modes add more 2114 pairs upward) | Confirmed (§Video Graphics Extension) |
| `#9800` | **6522 VIA** base address (optional expansion) | Confirmed ("The base address of the VIA is `#9800`") |
| `#B000` | **INS8255 PPI** (keyboard, loudspeaker, cassette, printer strobe) | Confirmed (§I/O, IC25) |
| `#B400` | Extension / printer / second 6522 region | Partial — OCR (`#B800` also shows a 6522) |
| `#A000` | Utility / extension ROM socket | Partial — OCR (MM52132 ROM) |
| `#C000`–`#FFFF` | **Atom BASIC ROM + COS (OS) ROM**; floating-point ROM socket | Partial — OCR; exact split TODO |

<!-- TODO: line-verify the full memory map (especially the #A000-#FFFF ROM layout and the #B000/#B400/#B800 PIA/VIA split) against the Atom Technical Manual memory-map page (page 20). The OCR of that page is fragmented. The well-known historical Atom map (zero page, COS/BASIC workspace at #02xx-#03xx, BASIC ROM #C000, FP ROM #D000, COS ROM #F000) should be confirmed line-by-line, not assumed. -->

Key consequences for curriculum code:

- **RAM is tiny and split.** The unexpanded Atom has just **1024 bytes** of RAM —
  512 bytes of upper text space plus 512 bytes of video RAM (§Lower Text Space
  Extension). A "minimal system" is populated to about 2 KB (§Power
  Requirements). Everything beyond that is fitted 2114 chip-pair by chip-pair.
- **Program RAM location depends on expansion.** At power-up the Atom checks for
  RAM in the lower text space and uses it for programs if present; otherwise it
  defaults to the upper text space (§Lower Text Space Extension). Don't hard-code
  the program base.
- **Graphics RAM competes with program RAM.** Higher graphics modes are *fitted
  RAM* in the video region — mode 4 (256×192) needs 6 KB of video RAM alone
  (Atomic Theory §11.1). Choosing a mode is a memory-budget decision first.

## Video (MC6847 VDG)

The Atom's display is driven by a Motorola **MC6847 Video Display Generator**
(IC31), a one-chip, memory-mapped video generator — a completely different design
from the BBC's 6845+ULA (§Block Diagram, §Video).

- **Memory-mapped.** "Each dot on the screen shows the information in a
  corresponding piece of memory." The VDG continuously reads the video RAM to
  refresh the picture; the CPU writes new data when the tri-state buffers are
  enabled during blanking (§Video).
- **Clock.** The VDG is fed a **3.58 MHz** frequency from which sync and refresh
  timing are derived; it produces both monochrome and colour output (§Video).
- **Base video RAM.** In the most basic Atom the video RAM is 1024×8 (1 KB), half
  used for a screen of normal characters and half for the upper text space
  (§Video).

### Graphics modes

Atom BASIC exposes **nine graphics modes** via the `CLEAR n` statement, ranging
from coarse-but-cheap to fine-but-RAM-hungry (Atomic Theory §11.1):

| Mode | Resolution (X×Y) | Video RAM |
|------|------------------|-----------|
| 0 | 64 × 48 | 0.5 KB |
| 1a | 64 × 64 | 1 KB |
| 1 | 128 × 64 | 1 KB |
| 2a | 128 × 64 | 2 KB |
| 2 | 128 × 96 | 1.5 KB |
| 3a | 128 × 96 | 3 KB |
| 3 | 128 × 192 | 3 KB |
| 4a | 128 × 192 | 6 KB |
| 4 | 256 × 192 | 6 KB |

- `CLEAR n` clears the screen and puts it into graphics mode *n* (Atomic Theory
  §11.2). Plotting is done with `PLOT k,X,Y` and lines with `MOVE`/`DRAW` (§11.3).
- In the higher modes (1–4) text characters cannot be mixed with graphics the way
  they can in mode 0 (Atomic Theory §11.6).
- Mode 0 (64×48) is the only mode available on a fully unexpanded machine; the
  others need the fitted graphics RAM above (§11.1, cross-ref §Video Graphics
  Extension).

<!-- TODO: confirm the MC6847's native colour set / "semigraphics" modes as exposed by the Atom (the 6847 has its own alphanumeric, semigraphics, and full-graphics modes); map the Atom's CLEAR n modes onto the underlying 6847 modes from the Atom sources, not from generic 6847 datasheets. -->

## Sound (1-bit loudspeaker)

The Atom has **no sound chip**. A loudspeaker is wired to **bit 2 of the 8255
output port**; sound is made by toggling that bit in a timed loop, producing
square-wave tones (Atomic Theory: "The ATOM contains a loudspeaker … connected to
bit 2 of the output port"; the assembler demo "makes a buzzing noise … playing the
random contents of its memory through its internal loudspeaker").

- Expect **single-channel, 1-bit square waves** — beeps and buzzes, not
  multi-voice music.
- `CTRL-G` produces a bleep through the loudspeaker (Atomic Theory). A worked
  example in the book toggles the output line to produce a tone (e.g. ~187 Hz).

<!-- TODO: add a minimal "make a tone" worked example (timed bit-2 toggle loop) once the first Atom sound unit exists; the exact port address (#B002 region of the 8255) should be confirmed from the tech manual I/O section. -->

## I/O (in brief)

- **INS8255 PPI** (`#B000` region) — the Atom's main I/O chip: scans the keyboard
  matrix (via a 4-to-10 line decoder driving matrix rows), drives the loudspeaker
  (bit 2), the cassette interface, and the printer strobe (§I/O).
- **Cassette (CUTS standard)** — saves data as two tones: logical 1 = 2.4 kHz,
  logical 0 = 1.2 kHz, each bit 3.3 ms → **300 bits/second** (§Cassette
  interface). This is the Atom's storage; the curriculum's loadable-artefact path
  is discussed in [`../TOOLCHAIN-RESEARCH.md`](../TOOLCHAIN-RESEARCH.md).
- **6522 VIA** (`#9800`, optional) — general-purpose I/O, parallel printer, and
  user expansion when fitted (§I/O, §VIA).

## See also

- [`../reference.md`](../reference.md) — platform entry doc and toolchain.
- [`../language/6502-quick-reference.md`](../language/6502-quick-reference.md) — instruction set + Atom notes.
- [`../basic.md`](../basic.md) — Atom BASIC and its built-in assembler.
- Primary library:
  `reference/by-system/acorn-atom/unknown-atom-technical-manual-issue-2.md`,
  `reference/by-system/acorn-atom/1980-atomic-theory-and-practice.md`.
