# Spectrum BASIC visual-pass cleanup — Part B handoff

Status as of this checkpoint. All work is committed locally in the relevant
repos but **nothing is pushed** — the `code-samples` branch is well ahead of
`origin/main`.

## What's done (committed, not pushed)

In `code-samples`:

- **Title-screen + visual fixes** (`9ba9574`, `fa3047a`, `10ca641`, `94bb512`):
  overlaps/edge-wraps fixed on four titles; Three in a Row attribute-clash fixed
  by enlarging cells; Sonar grid rebuilt as a spaced grid (lines in gutter cells);
  the three "passed-over" games finished.
- **Part A — consistent renumber** (`c89d14d` Reflex, `03dba24` the rest):
  Reflex, Bright Spark, Cipher, Locksmith, Sonar, Yearfall now have **one clean
  10-step scheme across all their units**, so consecutive-unit diffs reflect
  genuine content, not renumber noise. Each verified running in Emu198x. Reflex
  also lost its dead centering subroutine (it crashed on fall-through).
- **Centering wired up** (`37e6f7a`): the layer-2 centering subroutine (line
  9000), previously dead in every game, now renders the `*** TITLE ***` lines
  (title + result screens) via `LET a$ = "...": LET y = <row>: GO SUB 9000`.
  Applied to the 11 `***`-style games; the sub now prints `BRIGHT`. Lucky Number
  (INVERSE banner) and Quiz Master (red title) left alone — different styles.

## Owed: a single MDX sync (do it LAST, after all numbering is final)

The renumber changed line numbers but only `.bas` was touched. The curriculum
**MDX prose references line numbers heavily** (1–3 per unit, e.g. Cipher unit-06
says *"Line 160 `RESTORE`… Line 170 FOR loop"* — now lines 190/200). So the prose
is stale across every renumbered game. Decision: **sync once, after Part B**, so
the big three's prose isn't synced twice.

The sync must: (1) remap line-number references per game's old→new map; (2) handle
the unit **renames** from Part B (Hi-Lo 06→07 etc., Touchdown similar); (3) add
**new prose** for the inserted units. The old→new maps can be recomputed from the
git pre-renumber finals + current (positional), same as the relabel step below.
MDX lives in `website/src/content/curriculum/sinclair-zx-spectrum/basic/`.

## Part B — the big three (NOT started; design below is ready to run)

Principle (agreed with Steve): **each big feature becomes a subroutine, introduced
in one focused unit, then inherited by every later unit** — building on the
`GO SUB` concept the centering sub just taught. Flag software concepts as natural
naming moments arise (representation, graceful failure, persistent state, …),
one sentence at the moment the idea bites — never a lecture.

### Hi-Lo (10 → 11 units) — fully designed

| Unit | Introduces | Concept to name |
|------|-----------|-----------------|
| 01–05 | number game (unchanged) | — |
| **06 The Cards** | 4 suit UDGs + card-drawing subroutine + INVERSE header + draw current / face-down / reveal — replaces the number display | **representation** (data vs display) |
| 07 feedback | flash + beep "Correct!" on the card screen | — |
| 08 gameover | wrong → GAME OVER screen instead of `STOP` | **graceful failure** |
| 09 best | best-streak tracking (`B:` in header) + rating messages | **persistent state** |
| 10 titled | intro title screen (rules, press-any-key) | — |
| 11 final | suit-symbol logo flourish | — (proper small polish unit) |

Derive units 06–10 by removing later features from the current final
(`unit-10/hi-lo.bas`, which is the complete card game). **Wrinkle:** the card
screen uses an INVERSE header bar, not the centred `GO SUB 9000` title, so the
centering sub is present in 01–05, drops out in 06–09, and returns at unit-10
(titled) with the intro screen — a clean consequence of the display redesign, not
a bug. Atomic: 06–11 must all be card-based together.

### Touchdown (13 → 14 units)

New unit **"The View"** after unit-12, pulling the 3 UDGs (lander/exhaust/
explosion) + stars + terrain + the graphical lander rendering into one
subroutine-based unit. Units after inherit it. Design concept: **polish** ("the
physics didn't change; how it feels did"). Same atomic approach.

### Three in a Row (stays 11 units)

No new unit (decision record: "visual quality within existing structure"). Make
the DRAW board a `draw-board` subroutine introduced at unit-01 (`board.bas`,
where the board is established) and evolved in place, so the board doesn't appear
whole in the final. Needs a close look at the existing unit-01 board before
deciding how to evolve it.

## Mechanism + throwaway tooling (rebuild as needed)

For each big-three game: recover the pre-renumber final from git
(`git show ba8f20c~1:<final-path>`), **relabel** the current final back to old
numbers (positional zip of old/current line numbers — content fixes & centering
changed text but not line count or order, so it rides along), restructure / insert
units, then **union-renumber** all units onto one 10-step scheme, then verify each
runs in Emu198x.

Two small Python scripts did this in `/tmp` (ephemeral — rebuild from these specs):

- `relabel_to_old.py <git_old_final> <current_final>` — maps current→old line
  numbers positionally, rewrites leading numbers + `GO TO`/`GO SUB`/`RESTORE`
  references, asserts equal line count.
- `renum_union.py <files…>` — builds ONE mapping from the union of all line
  numbers across the given unit files, segments on gaps ≥100 (subroutine/DATA
  blocks keep their hundred base), assigns clean 10-step, applies to every file,
  remaps references. A line present in only some units leaves a reserved gap in
  the others.

## Verify

Per game after restructure: off-step check (all line numbers % 10 == 0), small
consecutive-unit diffs, and **load each unit in Emu198x and run it** (the MCP
server `emu198x-spectrum`; reset hard → run 200 → load → run → screenshot).
