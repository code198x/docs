# Acorn Electron — Architecture

A curriculum-flavoured map of the Electron, written as a **diff against the BBC
Micro**. The BBC architecture doc is the baseline; read it first for the parts
the two machines share:
[`../../bbc-micro/hardware/ARCHITECTURE.md`](../../bbc-micro/hardware/ARCHITECTURE.md).
This doc covers what the Electron does *differently* — and its centrepiece, the
**ULA contention model**, has no BBC equivalent.

> **Scaffold doc.** Established facts with citations, plus TODOs where
> Electron-specific depth is still owed. All `§` citations refer to the shared BBC
> reference
> [`bbc-micro-reference.md`](../../../../../reference/by-system/bbc-micro/bbc-micro-reference.md)
> unless noted — its **§Acorn Electron Differences** section is the primary source
> for Electron-specific facts.

## The one big idea: a single ULA

Everything that makes the Electron different from the BBC comes from one
cost-reduction decision. Where the BBC spreads its hardware across many chips —
the 6845 CRT controller, the Video ULA, two 6522 VIAs, the SN76489 sound
generator, and a cassette interface — the Electron **collapses all of it into a
single custom ULA** mapped at SHEILA `&FE00`–`&FE0F`, plus paged-ROM control at
`&FE05` (§SHEILA, §Acorn Electron Differences).

The consequences ripple outward:

- The ULA shares the DRAM bus with the CPU → **memory contention** (below).
- There is **no 6522 VIA** (System or User) and **no User Port** → BBC
  register-poking code fails; extension is via the rear edge connector only.
- The sound generator is gone → **one tone channel, no noise**.
- The original ULA has **no teletext** → no standard MODE 7.

## CPU

- **MOS 6502A, nominally 2 MHz.** The same NMOS 6502 instruction set as the BBC,
  C64 and NES (§Family Overview). For the instruction set and addressing modes,
  see [`../language/6502-quick-reference.md`](../language/6502-quick-reference.md).
- **ULA-contended — this is the defining trait.** The ULA fetches display data
  from the same DRAM the CPU executes from, so the CPU is **slowed during display
  fetch**. Effective speed depends on the screen MODE (§Acorn Electron
  Differences):

  | MODE group | Effective CPU speed | Why |
  |------------|--------------------|-----|
  | MODE 0–3 | **~1 MHz** | High-bandwidth modes — the ULA reads a lot of display RAM, contending heavily |
  | MODE 4–7 | **~2 MHz** | Lower-bandwidth modes — less contention |

  This is the **opposite** of the BBC's design. On the BBC the 6845 reads video
  RAM in the half-cycle the 6502 isn't using, so the CPU runs at a flat 2 MHz
  regardless of MODE; on the Electron the ULA steals cycles, and the amount
  depends on the MODE you chose. Loop timing that holds on the BBC will *not* hold
  on the Electron (§Acorn Electron Differences, and contrast BBC §System
  Architecture).
  <!-- TODO: confirm finer contention detail against the reference library / OS 1.00 docs — e.g. whether contention pauses the CPU only during the active display period (so it speeds up in vertical blank), and exact cycle costs. The library gives the MODE 0-3 ≈ 1 MHz / MODE 4-7 ≈ 2 MHz split but not a per-cycle model. -->

Hex is written with a leading `&` throughout (`&FE00`), as on the BBC.

## Memory map

The 6502 sees the same 64 KB address space, and the broad zero-page / stack / OS
workspace / user-RAM / sideways-ROM / MOS / SHEILA layout follows the BBC
(see the BBC [`ARCHITECTURE.md` § Memory map](../../bbc-micro/hardware/ARCHITECTURE.md)).
The Electron-specific points:

- **32 KB DRAM, single configuration** — there is one memory layout, not the
  BBC's Model A/B split (§Acorn Electron Differences, §Family Overview).
- **The ULA contends for this DRAM** during display — the same RAM is doing double
  duty as program memory and frame buffer, which is *why* the contention exists.
- **SHEILA is almost empty.** Page `&FE` holds only the ULA at `&FE00`–`&FE0F`
  (plus paged-ROM control at `&FE05`). The BBC's `&FE40` System VIA, `&FE60` User
  VIA, `&FE00`/`&FE01` 6845, and `&FE20`/`&FE21` Video ULA registers **are not
  there** (§SHEILA — the Electron column marks only `&00`–`&0F`).
- **Sideways ROM paging** works as on the BBC (paged 16 KB window at
  `&8000`–`&BFFF`), and the Electron actually leans on it harder: the firm-key
  (function-key) strings live in sideways ROM rather than RAM, because RAM is so
  contended (§Acorn Electron Differences).
  <!-- TODO: confirm the exact Electron user-RAM top/bottom per MODE (HIMEM/OSHWM values) against the reference library; screen RAM still sits at the top of user RAM and moves with the MODE as on the BBC, but the Electron's per-MODE figures should be confirmed rather than copied from the BBC. -->

## Video

The Electron's ULA does the whole video job — raster timing, address generation,
and pixel output — that the BBC splits between the 6845 and the Video ULA. There
is no programmable 6845, so the BBC's hardware-scroll-via-6845-registers and
direct CRTC programming do not apply; go through MOS/VDU.

### MODE support

The Electron supports the BBC MODE numbers **0–6** (§Acorn Electron Differences).
The resolution/colour/text characteristics of MODE 0–6 follow the BBC
(see the BBC [§ The MODE system](../../bbc-micro/hardware/ARCHITECTURE.md)), but
with the Electron's two extra consequences:

- **The MODE determines CPU speed** (see the contention table above) — MODE 0–3
  run the CPU at ~1 MHz, MODE 4–7 at ~2 MHz. On the Electron, choosing a MODE is
  choosing a *speed* as well as a resolution.
- **No standard MODE 7 / teletext.** The original Electron ULA has **no teletext
  mode**. Third-party teletext add-ons exist but are not standard (§Acorn Electron
  Differences). This matters: the BBC tree leans on MODE 7 as the cheap (1 KB)
  text-UI mode, and that option is **not available** on a stock Electron. Text UIs
  must use a bitmap text mode (e.g. MODE 6).
  <!-- TODO: confirm the exact per-MODE screen RAM sizes and base addresses on the Electron against the reference library, rather than assuming the BBC's figures. The 32 KB single-config and contention may shift practical choices (e.g. MODE 0-2 at 20 KB leave little room). -->

## Sound

- **One tone channel, no noise.** The Electron's ULA produces a **single tone
  channel at a fixed envelope** and has **no noise channel** — it is not an
  SN76489 (§Acorn Electron Differences). This is markedly simpler than the BBC's
  three-tone-plus-noise SN76489.
- **Driven through the ULA, via MOS.** As on the BBC, do not poke the sound
  hardware directly — use the MOS `SOUND` path. But expect the BBC's multi-channel
  and noise capabilities to be unavailable.
  <!-- TODO: confirm how the MOS SOUND/OSWORD &07 interface behaves on the Electron — which channel(s) are honoured, whether channel 0 (noise) no-ops, and whether ENVELOPE has any effect given the "fixed envelope" hardware — against the reference library or OS 1.00 docs. -->

## I/O

- **No 6522 VIAs, no User Port.** The Electron has neither the System VIA nor the
  User VIA, and no User Port. Extension is via the **rear edge connector** only;
  the Plus 1 expansion adds a parallel printer port (and a Tube), and the Plus 3
  adds an ADFS floppy (§Acorn Electron Differences).
- **Keyboard, timers and frame sync** are handled by the ULA and surfaced through
  MOS, so curriculum code reads keys and waits for vertical sync through the same
  MOS calls as the BBC (`OSBYTE`), even though the underlying hardware differs.
  <!-- TODO: confirm the Electron's vertical-sync / frame-timing MOS path (OSBYTE &13 "wait for vsync" availability) against the reference library; the everyday OSBYTEs are source-compatible but frame timing is worth verifying for game loops. -->

## How it differs from the BBC — summary

| Aspect | BBC Model B | Acorn Electron |
|--------|-------------|----------------|
| Hardware | 6845 + Video ULA + 2× 6522 VIA + SN76489 + cassette IF | **One ULA** at `&FE00`–`&FE0F` |
| CPU timing | Flat 2 MHz, uncontended | **Contended**: ~1 MHz (MODE 0–3), ~2 MHz (MODE 4–7) |
| RAM | 16 KB (A) / 32 KB (B) | 32 KB, single config (contended) |
| Sound | 3 tone + 1 noise (SN76489), mono | **1 tone, no noise** |
| MODE 7 | Yes (SAA5050 teletext) | **No** (not standard) |
| User Port / VIAs | Yes | **No** |
| Default storage | Cassette + optional DFS disc | Cassette (Plus 3 adds ADFS, not DFS) |
| OS | OS 1.20 | **OS 1.00** (source-compatible at OSBYTE/OSWORD) |

## See also

- [`../reference.md`](../reference.md) — platform entry doc and toolchain.
- [`../language/6502-quick-reference.md`](../language/6502-quick-reference.md) — instruction set (points to the BBC) + Electron timing/OS notes.
- BBC baseline:
  [`../../bbc-micro/hardware/ARCHITECTURE.md`](../../bbc-micro/hardware/ARCHITECTURE.md).
- Primary library:
  [`bbc-micro-reference.md`](../../../../../reference/by-system/bbc-micro/bbc-micro-reference.md)
  (§Acorn Electron Differences, §SHEILA, §Family Overview).
