# BBC Micro — Architecture

A curriculum-flavoured map of the BBC Model B: how memory is laid out, what the
CPU is, and how the video and sound hardware work. The aim is the mental model a
learner needs before writing the first unit — not exhaustive chip detail. For
that, follow the citations into the primary reference library.

> **Scaffold doc.** Established facts with citations, plus TODOs where depth is
> still owed. All `§` citations refer to
> `reference/by-system/bbc-micro/bbc-micro-reference.md`
> unless noted.

## CPU

- **MOS 6502A at 2 MHz.** Standard NMOS 6502 instruction set — the same CPU
  family as the C64 and NES (§System Architecture).
- **Uncontended.** The 6502 runs at a flat 2 MHz no matter the screen mode,
  because the 6845 video controller reads screen RAM in the half of each cycle
  the CPU isn't using. This is a defining BBC trait: unlike the Spectrum and C64,
  the CPU never slows for video (§System Architecture, §Emulation Notes).
- **Exception — the 1 MHz bus.** Accesses to external 1 MHz-bus I/O (the FRED and
  JIM pages) and the serial ACIA sync to a 1 MHz clock, costing roughly one extra
  cycle (§System Architecture).

Hex is written with a leading `&` throughout BBC documentation (`&FE40`), where
the C64/NES world uses `$`.

For the instruction set and addressing modes, see
[`../language/6502-quick-reference.md`](../language/6502-quick-reference.md).

## Memory map

The 6502 sees a 64 KB address space. Model B layout (§Memory Map):

| Range | Size | Use |
|-------|------|-----|
| `&0000`–`&00FF` | 256 B | Zero page (OS + language workspace) |
| `&0100`–`&01FF` | 256 B | 6502 stack |
| `&0200`–`&02FF` | 256 B | OS vectors + workspace |
| `&0300`–`&07FF` | 1.25 KB | OS / language workspace (VDU vars, sound, BASIC vars) |
| `&0800`–`&0DFF` | 1.5 KB | Sound, buffers, soft keys, font, NMI |
| `&0E00`–`&7FFF` | up to ~28.5 KB | **User program + screen RAM** (screen size varies by MODE) |
| `&8000`–`&BFFF` | 16 KB | **Paged (sideways) ROM/RAM** — one bank at a time |
| `&C000`–`&FBFF` | 15 KB | **MOS ROM** (the OS) |
| `&FC00`–`&FCFF` | 256 B | FRED — 1 MHz bus I/O |
| `&FD00`–`&FDFF` | 256 B | JIM — 1 MHz bus paging window |
| `&FE00`–`&FEFF` | 256 B | **SHEILA** — internal hardware registers |
| `&FF00`–`&FFFF` | 256 B | MOS jump table + 6502 vectors |

Key consequences for curriculum code:

- **Screen RAM sits at the top of user RAM and moves with the MODE.** MODE 0–2
  use 20 KB from `&3000`; MODE 3 uses 16 KB from `&4000`; MODE 4–5 use 10 KB from
  `&5800`; MODE 6 uses 8 KB from `&6000`; MODE 7 uses 1 KB from `&7C00`
  (§Screen Modes). Read `HIMEM` (`OSBYTE &84`) and `OSHWM` (`OSBYTE &83`) for the
  current top/bottom of user RAM rather than hard-coding (§Memory Map).
- **Hardware I/O lives in page `&FE` (SHEILA).** The 6845, Video ULA, the two
  6522 VIAs, ROM select, and floppy controller are all here (§SHEILA).

### Sideways ROM (concept)

The 16 KB window at `&8000`–`&BFFF` is **bank-switched**: the ROM-select register
at `&FE30` chooses which of up to 16 "sideways" banks is visible. BBC BASIC, the
filing systems (DFS/ADFS), and utilities all live in sideways banks and coexist
through this scheme. On the B+/Master some banks are **sideways RAM**, allowing
loadable ROM images (§Sideways ROM Paging). For curriculum purposes the takeaway
is: BASIC and the OS are ROM, the user program and screen share the RAM below
`&8000`.
<!-- TODO: add a learner-level worked example of selecting a sideways bank if any unit needs it; full header/service-call mechanism is in reference §Sideways ROM Paging. -->

## Video

BBC video is a **two-chip** design: the 6845 handles raster *timing and
addressing*, and the Acorn Video ULA turns the fetched bytes into *pixels* and
holds the palette (§Video Hardware).

### 6845 CRT controller

- Generates horizontal/vertical timing, addresses screen RAM, and drives the
  cursor. It does **not** generate pixels (§6845 CRTC).
- 18 internal registers, written through an address/data pair at SHEILA
  `&FE00`/`&FE01`. From BASIC/MOS, use `VDU 23,0,R,V,…` so it works across the
  Tube (§6845 CRTC).
- **Hardware scrolling** is done by adjusting the display-start registers
  (R12/R13), moving the screen by whole character rows; a wrap-around circuit
  keeps the address inside screen RAM (§Hardware Scrolling).

### The MODE system

`MODE n` selects a resolution/colour/text combination. The headline modes
(§Screen Modes):

| MODE | Resolution | Colours | Text | Screen RAM |
|------|-----------|---------|------|-----------|
| 0 | 640 × 256 | 2 | 80 × 32 | 20 KB |
| 1 | 320 × 256 | 4 | 40 × 32 | 20 KB |
| 2 | 160 × 256 | 16 | 20 × 32 | 20 KB |
| 3 | text only | 2 | 80 × 25 | 16 KB |
| 4 | 320 × 256 | 2 | 40 × 32 | 10 KB |
| 5 | 160 × 256 | 4 | 20 × 32 | 10 KB |
| 6 | text only | 2 | 40 × 25 | 8 KB |
| 7 | teletext | 8 + flash | 40 × 25 | 1 KB |

- **Pixel layout (MODE 0–6)** is character-cell-based: 8 consecutive bytes encode
  one 8-pixel-tall cell, then the next cell to the right (§Screen Modes). This is
  worth a worked diagram in a graphics unit.
- **MODE 7 is teletext, not a bitmap** — see below.
- **More colours costs RAM and resolution.** MODE 2 gives 16 colours but only
  160 px wide; MODE 0 gives crisp 640 px but only 2 colours. Choosing a mode is a
  core early-curriculum decision.

### Palette

The Video ULA holds a 16-entry palette mapping **logical** colours to
**physical** colours. Physical colours 0–7 are black, red, green, yellow, blue,
magenta, cyan, white; 8–15 are flashing pairs. Set entries via `VDU 19` / MOS
rather than poking the ULA (§Video ULA). Note the documented hardware quirk: the
ULA stores `physical EOR 7` internally.

### MODE 7 / teletext (SAA5050)

MODE 7 uses the Mullard **SAA5050** teletext chip. The screen stores **character
codes** (one byte per cell) plus inline **control codes** for colour, flashing,
double-height, and 2×3 "sixel" mosaic graphics — there is no pixel buffer
(§SAA5050 Teletext). It is the cheapest mode (1 KB) and excellent for text UIs
and menus; "graphics" there means blocky mosaics.

## Sound (SN76489)

- TI **SN76489**: three square-wave tone channels + one noise channel, mixed to
  **mono** (§SN76489 Sound Generator).
- **Not memory-mapped.** The chip hangs off the System VIA's slow data bus; you
  write to it by putting a byte on VIA port A and pulsing the addressable latch,
  with interrupts disabled (§SN76489 Sound Generator, §System VIA). For
  curriculum code, **use the MOS sound path** (`SOUND` / `OSWORD &07`, with
  `ENVELOPE` / `OSWORD &08` for envelopes) rather than driving the chip directly.
- Tone frequency is a 10-bit divisor of a 4 MHz clock; volume is a 4-bit
  attenuator (0 = loudest, 15 = silent) (§Frequency Bytes, §Volume Bytes).

<!-- TODO: add a minimal "make a beep" worked example via OSWORD &07 once the first sound unit exists; full register format is in reference §SN76489. -->

## I/O (in brief)

Two 6522 VIAs (§System VIA, §User VIA):

- **System VIA** (`&FE40`–`&FE5F`) — keyboard scan, sound chip, screen-scroll
  control, the 50 Hz vertical-sync interrupt and OS timers.
- **User VIA** (`&FE60`–`&FE6F`) — the parallel printer port and the User Port (a
  general-purpose 8-bit port for add-ons and joysticks).

Most curriculum code touches these only through MOS calls (read a key, time a
frame) rather than directly. Frame timing for games comes from the vertical-sync
event / `OSBYTE &13` (wait for vertical sync).

## See also

- [`../reference.md`](../reference.md) — platform entry doc and toolchain.
- [`../language/6502-quick-reference.md`](../language/6502-quick-reference.md) — instruction set + MOS calls.
- Primary library:
  `reference/by-system/bbc-micro/bbc-micro-reference.md`,
  `reference/by-system/bbc-micro/bbc-micro-advanced-user-guide.md`.
