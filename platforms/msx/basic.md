# MSX-BASIC

MSX-BASIC is the BASIC built into every MSX, in ROM, ready the moment the machine
powers on. It is a **Microsoft BASIC** — specifically an extended Microsoft BASIC
v4.5 — so if you have met Commodore BASIC, GW-BASIC, or BBC BASIC's Microsoft
cousins, the bones will feel familiar. What sets MSX-BASIC apart is how much of the
hardware it exposes as first-class language: graphics, sprites, music, and
joysticks are all built-in keywords, not POKE incantations.

> **Source of truth:**
> `reference/by-system/msx/sony-msx-basic-programming-reference-manual.md`
> (the Sony MSX-BASIC Programming Reference Manual) and
> `reference/by-system/msx/msx-reference.md` §13.
> Specifics this skeleton has not yet pinned down are flagged `TODO`.

## Where it sits among Microsoft BASICs

Microsoft wrote BASIC interpreters for nearly every 8-bit machine of the era, and
MSX-BASIC is a close, well-equipped member of that family — it tracks **GW-BASIC**
closely (the PC's Microsoft BASIC) while adding the MSX's graphics, sound, and
input statements. Compared with the **Commodore 64's BASIC V2** (a deliberately
stripped-down Microsoft BASIC with no graphics or sound keywords at all),
MSX-BASIC is generous: you can draw, animate sprites, and play music without ever
reaching for `PEEK`/`POKE`. Compared with the **ZX Spectrum's Sinclair BASIC**
(not a Microsoft BASIC), the syntax conventions differ — MSX uses standard
Microsoft idioms like `&H` hex literals and type-suffixed variables.

The practical upshot for the curriculum: MSX-BASIC is a *comfortable* first BASIC.
Much of what needs hardware pokes elsewhere is a keyword here.

## Numbers, variables, and literals

- **Numeric types:** integer (16-bit signed), single-precision (4-byte), and
  double-precision (8-byte BCD, ~14 digits) — the default declared type is double.
- **Type suffixes:** `%` integer, `!` single, `#` double, `$` string. Variable
  names may be any length, but **only the first two characters are significant**.
- **Literals:** hex `&H7F`, octal `&O77`, binary `&B0110`.
- **Strings:** up to 255 characters.
- **Operators:** the usual arithmetic plus `\` (integer division) and `MOD`;
  bitwise `AND`, `OR`, `XOR`, `NOT`, `EQV`, `IMP` on 16-bit two's-complement
  values.

(`msx-reference.md` §13.)

> **Curriculum note — variable naming.** Because only the first two characters are
> significant, `SCORE` and `SCREEN`-style long names that collide in their first
> two letters are the *same* variable. This bites learners; keep example variable
> names distinct in their first two characters. (Compare the C64's same-2-char
> rule and the Spectrum's single-letter string-variable rule — each platform has
> its own naming trap.)

## Graphics keywords

MSX-BASIC drives the VDP directly through statements:

| Keyword | Does |
|---------|------|
| `SCREEN n` | Select screen mode (0 text, 1 default graphics, 2 hi-res, 3 multicolour; 4–12 on MSX2+) |
| `COLOR fg, bg, border` | Set foreground / background / border colour |
| `PSET (x,y)` / `PRESET (x,y)` | Plot / unplot a pixel |
| `LINE (x1,y1)-(x2,y2)` | Draw a line (or, with `,B`/`,BF`, a box / filled box) |
| `CIRCLE (x,y),r` | Draw a circle |
| `PAINT (x,y)` | Flood-fill |
| `DRAW "..."` | Turtle/macro drawing language |
| `SPRITE$(n)` / `PUT SPRITE` | Define and place hardware sprites |
| `VPOKE addr,v` / `VPEEK(addr)` | Write / read VRAM directly |
| `VDP(n) = v` | Write a VDP register |
| `BASE(n)` | The VRAM base address of table type *n* for the current mode |

(`msx-reference.md` §13; full per-keyword syntax in the Sony BASIC manual.)

## Sound keywords

| Keyword | Does |
|---------|------|
| `PLAY "..."` | Play music written in MML (Music Macro Language) — notes, octaves, lengths, tempo across the three PSG channels |
| `SOUND reg, val` | Write a PSG register directly (low-level) |
| `BEEP` | The 1-bit click sound |

`PLAY` is the high-level route (write a tune as a string); `SOUND` gives direct
control of the AY-3-8910's registers when you want it. (`msx-reference.md` §13.)

<!-- TODO: add a short worked PLAY MML example and a SOUND register example when the
     first BASIC sound unit is written; cite the Sony BASIC manual's PLAY/SOUND
     pages. -->

## Input keywords

| Keyword | Does |
|---------|------|
| `STICK(n)` | Joystick direction (0 = centred, 1–8 = compass) for cursor keys (0) or joystick ports (1/2) |
| `STRIG(n)` | Trigger button state |
| `PAD(n)` / `PDL(n)` | Touchpad / paddle |
| `INKEY$` | Read a key without waiting |

(`msx-reference.md` §13.)

## How it differs from other BASICs (quick list)

- **Graphics and sound are keywords**, not POKEs — unlike C64 BASIC V2.
- **Microsoft idioms throughout** — `&H` hex, type suffixes, `DEFINT`/`DEFDBL`,
  `ON ERROR ... RESUME` — unlike Sinclair BASIC.
- **Direct VDP/VRAM access from BASIC** via `VPOKE`/`VPEEK`/`VDP()` — you can mix
  high-level statements with low-level pokes when you need to.
- **`CALL <name>` extensions** let cartridges (disk, MSX-MUSIC, kanji ROM) add new
  statements — a hook you will see in MSX2-era code (`msx-reference.md` §15.1).

## Errors

MSX-BASIC reports numbered errors (test with `ERR` after `ON ERROR`), e.g. `1 NEXT
without FOR`, `5 Illegal function call`, `9 Subscript out of range`, `13 Type
mismatch`. The full table is in `msx-reference.md` §13.

## See also

- `reference/by-system/msx/sony-msx-basic-programming-reference-manual.md`
  — the full BASIC reference (per-keyword syntax)
- [hardware/ARCHITECTURE.md](./hardware/ARCHITECTURE.md) — the VDP and PSG that the
  graphics and sound keywords drive
- [reference.md](./reference.md) — the platform entry point
