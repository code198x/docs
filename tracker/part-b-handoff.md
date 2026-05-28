# Spectrum BASIC visual-pass cleanup — Part B handoff

**Part B is DONE** (all three big-three games restructured + verified). The only
remaining item is the single MDX sync (below). All work is committed locally in
the relevant repos but **nothing is pushed** — the `code-samples` branch is well
ahead of `origin/main`.

Part B commits (code-samples, local): `a75b338` Hi-Lo, `f9d9898` Touchdown,
`39e14d1` Three in a Row.

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

The sync must, per game: (1) remap line-number references to the new `.bas`;
(2) handle the **count + structure changes** below; (3) add **new prose** for
inserted/repurposed units. The website also holds the unit YAML
(`src/content/units/sinclair-zx-spectrum/basic/<game>.yaml`) — the **source of
truth for counts** — which must move 10→11 (Hi-Lo), 13→14 (Touchdown). MDX lives
in `website/src/content/curriculum/sinclair-zx-spectrum/basic/`.

Part-B-specific sync work:

- **Hi-Lo (10→11):** new unit-06 page "The Cards"; pages 07–11 carry the names
  feedback/gameover/best/titled/hi-lo but their prose was the *number* game —
  rewrite for the card screen. Count 10→11.
- **Touchdown (13→14):** new unit-13 page "The View" (graphics); unit-14 is the
  old final's prose. Count 13→14.
- **Three in a Row (stays 11):** no count change; prose for units 01–10 must
  describe the **DRAW board** (was the text board), and the symbol-introduction
  story (X at 02, O at 04); unit-11 prose now = score + replay + title icon only.
- **Part A games** (Reflex, Bright Spark, Cipher, Locksmith, Sonar, Yearfall):
  line-number references stale from the renumber — remap to current `.bas`.

## Part B — the big three (DONE — as-built below)

Principle (agreed with Steve): **each big feature becomes a subroutine, introduced
in one focused unit, then inherited by every later unit** — building on the
`GO SUB` concept the centering sub just taught. Flag software concepts as natural
naming moments arise (representation, graceful failure, persistent state, …),
one sentence at the moment the idea bites — never a lecture.

### Hi-Lo (10 → 11 units) — DONE (committed `a75b338`, not pushed)

As built — each unit is one `.bas`, named for its lesson:

| Unit | File | Introduces | Concept named | +lines vs prev |
|------|------|-----------|---------------|----------------|
| 01–05 | (unchanged) | number game | — | — |
| **06** | `the-cards.bas` | 4 suit UDGs + card subroutines + INVERSE header + draw current / face-down / reveal — replaces the number display | **representation** (data vs display) | (the big swap) |
| 07 | `feedback.bas` | border flash + visible "Correct!" | — | +4 |
| 08 | `gameover.bas` | wrong → GAME OVER screen + play-again loop (was `STOP`) | **graceful failure** | +11 |
| 09 | `best.bas` | best-streak tracking (`B:` in header) + rating messages | **persistent state** | +8 |
| 10 | `titled.bas` | intro title screen (rules, press-any-key) | — | +7 |
| 11 | `hi-lo.bas` | suit-symbol logo flourish | — (small polish unit) | +1 |

Derived units 06–10 by stripping features from the complete card game (was
`unit-10/hi-lo.bas`, moved verbatim to `unit-11/hi-lo.bas` = the master). Generated
with `/tmp/gen_hilo.py` (include-sets + per-unit overrides on the master's line
numbers, so surviving lines keep their numbers — diffs are purely additive). The
old number-game files (`unit-06/feedback`, `07/gameover`, `08/best`, `09/titled`)
were removed.

**Correction to the original plan:** the centring subroutine drops out at unit-06
(the INVERSE header replaces the centred title) and returns at **unit-08**, not 10
— the GAME OVER screen needs a centred title (`GO SUB 9000`), so 9000 first
reappears there. The intro screen (unit-10) is its second consumer.

All six units verified running in Emu198x (cards render, S-only vs S+B header,
green Correct! with pause, red GAME OVER with centred title + loop, intro, intro+
flourish).

**MDX sync owed for Hi-Lo:** count 10→11; new page for unit-06 "The Cards"
(representation); unit pages 07–11 carry forward but their prose must be rewritten
for the card screen (the old 07–09 prose was the number game); line-number
references re-checked against the new `.bas`.

### Touchdown (13 → 14 units) — DONE (committed `f9d9898`, not pushed)

The final unit turned the whole text lander graphical in one go (UDGs, INVERSE
dashboard, stars, terrain, lander sprite) **and** added its polish. Split it:

- **unit-13 `the-view.bas`** — the graphical game: UDGs + INVERSE dashboard +
  stars + terrain + lander sprite + block-graphic fuel bar. Outcomes still STOP.
- **unit-14 `touchdown.bas`** — the master verbatim (moved from unit-13). Adds
  the intro lander illustration (110), exhaust plume (480), and play-again loop
  (730 STOP → loop, +740/+750).

The 13→14 diff is +4 lines / 1 modify. The rendering stayed **inline**, not a
subroutine — the lander is drawn once per loop from one place, so the handoff's
"subroutine-based" framing didn't fit; inline matches the master. The 12→13 jump
(text → graphics) is the deliberate "give it the arcade look" lesson; learners
see full programs via `CodeFromFile`, so its git-diff noise is not learner-facing.
Both verified in Emu198x.

Pre-existing, left alone (out of restructure scope): the explosion UDG (146) is
defined but never used.

### Three in a Row (stays 11 units) — DONE (committed `39e14d1`, not pushed)

The DRAW board (PLOT/DRAW grid + cyan X + red O) appeared whole in the final,
replacing the text board (digits + `---+---+---`) all at once. Now graphical from
unit-01:

- **unit-01** establishes the DRAW grid; the **X** joins at unit-02 (player), the
  **O** at unit-04 (computer). Generated with `/tmp/gen_tiar.py` — the DRAW board
  fits the same line range (150-240) the text board used, so each unit's verified
  logic is untouched; X gated from unit-02, O from unit-04.
- Messages moved row 10 → row 18 (clear of the bigger grid). unit-01 gained a
  `STOP` so its board demo doesn't fall into the centring sub.
- **unit-11** rebuilt on unit-10's numbering: title-screen icon, persistent W/L/D
  score, and play-again loop land in gap line numbers, so the 10→11 diff is just
  those (no board change).

Decision: **no subroutine** — the decision record says "visual quality within
existing structure", and the board redraw is already once-per-turn from the loop
top, so converting to a sub added nothing. Kept inline. Verified in Emu198x
(board renders across units; full game reaches outcome + score + replay).

Pre-existing quirks, left alone (out of scope): (1) the AI checks win and block in
the **same** per-line pass, so a block on an earlier win-line can pre-empt a win on
a later one — minor strategic imperfection. (2) units 09–10's **draw** outcome has
no `STOP`/loop, so a full-board draw falls into the 9000 sub → "RETURN without
GOSUB". Rare (needs a drawn game) and pre-existing; flag for the cleanup/MDX pass.

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
