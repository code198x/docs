# Commodore VIC-20 BASIC v2

**Purpose:** Curriculum-flavoured overview of the VIC-20's built-in BASIC.
**Audience:** Lesson designers writing VIC-20 BASIC units.
**Facts cite:** the **VIC-20 Programmer's Reference Guide** and `vic20-reference.md`
§18 (`reference/by-system/commodore-vic20/`).

> **Scaffold.** Established facts with citations; deeper specifics carry `TODO`s
> to confirm against the library before a unit ships.

---

## It is the same BASIC v2 as the C64

The VIC-20 runs **Commodore BASIC v2.0** — the Microsoft 6502 BASIC that ships,
byte-for-byte the same dialect, in the C64's ROM (`vic20-reference.md` §18). For
the curriculum this is a gift: **the C64 BASIC knowledge transfers directly.**
Loops, variables, `PRINT`, `INPUT`, `GOTO`/`GOSUB`, `DATA`/`READ`, string and
maths functions — all identical. A learner who has done the C64 BASIC volume
already knows the language; the VIC-20 changes only *the machine underneath it*.

What is shared with the C64:

- The BASIC ROM lives at **$C000–$DFFF** and calls the KERNAL through the jump
  table at the top of ROM (`vic20-reference.md` §18).
- Programs are stored line-by-line, each line prefixed by a 16-bit link to the
  next line and a 16-bit line number; tokenisation is the same Commodore scheme.
- The **two-significant-characters** variable rule (below).

What differs is **not the language** but the hardware it pokes (screen size,
colours, sound, and especially the memory layout — see
[`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md)).

## No graphics or sound keywords — everything is POKE/PEEK

BASIC v2 has **no dedicated graphics or sound commands** (no `SPRITE`, `SOUND`,
`PLOT`, `CIRCLE` — those came on later Commodore BASICs or via the Super Expander
cartridge). On the VIC-20 you drive the hardware by `POKE`ing the VIC chip
registers and `PEEK`ing them back (`vic20-reference.md` §18). Common idioms:

```basic
10 POKE 36879, 8       : REM screen + border colour (register $900F)
20 POKE 36878, 15      : REM master volume = 15 (register $900E)
30 POKE 36876, 200     : REM start a note on voice 3 (soprano, $900C)
40 POKE 36869, 255     : REM custom characters at $1C00 (register $9005)
```

(Register addresses in decimal here because that is what `POKE` takes;
$9000 = 36864. The full register map is in
[`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) and `vic20-reference.md`
§6.) This makes VIC-20 BASIC an unusually direct teacher: there is no abstraction
between the keyword and the chip — you write to the hardware and watch it respond.

> Note the **volume / aux-colour share a byte** ($900E): change volume with
> `POKE 36878,(PEEK(36878) AND 240) OR V` so you do not clobber the auxiliary
> colour. Period games books often got this wrong. (`vic20-reference.md` §8.)

## The variable-naming gotcha

Like all Commodore BASIC, **only the first two characters of a variable name are
significant.** `SCORE` and `SCREEN` are the *same* variable (`SC`); `LIVES` and
`LIMIT` collide on `LI`. Long descriptive names are legal but silently alias —
a real source of "impossible" bugs in learner programs. Teach short, distinct
names, or names whose first two characters are unique. <!-- TODO: confirm the exact 2-char rule wording and any reserved-keyword-in-name caveat against the Programmer's Reference Guide BASIC chapter -->

## The memory constraint shows up immediately

The unexpanded VIC-20 gives BASIC just **3583 bytes** (`vic20-reference.md` §1,
§4). A BASIC program plus its variables plus the screen share the low memory, so
programs must stay small — and any custom-character work has to lower the
top-of-BASIC pointers to carve out room below $1FFF. State the target memory
configuration per unit, as period type-in listings always did
([`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md) covers the
expansion-relocation behaviour). <!-- TODO: decide and record the BASIC track's target memory configuration (unexpanded vs +3K vs +8K) once a track plan exists -->

## Lineup and state

Per [Content model](../../specifications/content-model.md),
the authoritative lineup and shipped-state for this track live in the catalogue,
not in this prose doc:

- **Lineup + state:** `website/src/content/modules/commodore-vic-20/basic.yaml`
  <!-- TODO: create the VIC-20 BASIC module catalogue when the track is planned; this file does not exist yet -->
- **Hardware + language facts:** this folder's [`reference.md`](reference.md),
  [`hardware/ARCHITECTURE.md`](hardware/ARCHITECTURE.md), and the primary
  reference library.

## See also

- [reference.md](reference.md) — platform entry point.
- [hardware/ARCHITECTURE.md](hardware/ARCHITECTURE.md) — memory map, the moving screen, VIC registers.
- [../commodore-64/basic.md](../commodore-64/basic.md) — the C64 BASIC track (same BASIC v2; transferable).
- `reference/by-system/commodore-vic20/vic20-reference.md` §18 — BASIC + KERNAL.
