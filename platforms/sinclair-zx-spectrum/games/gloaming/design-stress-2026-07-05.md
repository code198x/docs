# Gloaming (Module 1) — design-stress pass, 2026-07-05

Adversarial refutation of the **shipped Module 1** game — the ZX Spectrum assembly
first game, whose antagonist is the hunting *draught*. Verified against the shipped
code, not the brief: `code-samples/.../gloaming/unit-20/steps/step-02.asm` (identical
logic to the canonical cut `prototype/gloaming-m1.asm`; unit-21 is that build packaged
as `step-01.sna`). Constants confirmed: `DRAUGHT_SPEED 16`, `PLAYER_REPEAT 6`,
`GATHER 120`, `LIVES 3`, `LOCK 25`, 8 fixed lamps, one draught.

**Standing verdict up front:** Gloaming clears the *a-game-needs-jeopardy* bar and the
winnability gate. The fail state is genuinely reachable (idle player is hunted down —
`m1-probe`, green), the win is reachable (`m1-won`, green), and both are driven by
scripted run. **No BREAKS-level defect exists** — no dominant strategy that never
loses, no soft-lock, no unwinnable state. What survives the attack is **two fairness
edges (BLEEDS)** in the contact/collision logic and a cluster of by-design thinness
(BLEMISH / open-question) items. The two BLEEDS matter beyond Gloaming because the
same seek-step + attribute-collision engine is the declared parent of Shadowkeep's
Warden ("Gloaming's draught grown up") — the bugs will be inherited unless caught here.

---

## Findings (severity-ordered)

### BLEEDS-1 — Death beats victory on the tie frame

**Scenario.** A player lights the **eighth (final) lamp** while on their **last life**
with the draught orthogonally adjacent. On that single frame: `player_step` lights the
lamp (`lit_count` → 8), then — same frame — `draught_step` steps onto the player and
calls `lose_life`, which with `lives==1` sets `STATE_LOSE`. The player sees **NIGHT
FALLS** despite having satisfied the win condition that very frame.

**Confirmed in code.** `play_step` (step-02.asm ~L137–164) runs `player_step` →
`draught_step` → *then* the win check. The `ret nz` after `draught_step` (L146) fires
the moment the state flips to LOSE, so the `lit_count == NUM_LAMPS` test (L148) never
runs. Ordering is: player move, draught move, win — death is resolved before victory
is even asked.

**Design's current answer.** None. The ordering is implicit, not a considered
tie-break.

**Why it bites.** It directly inverts the game's own thesis. The player *completed the
objective* and is handed the loss ending. It is rare (needs the last lamp lit while
cornered on the last life) but fully constructible, and it is exactly the high-drama
moment the game is built around — the last lamp under pressure.

**Suggested direction (one).** Check the win *before* `draught_step`, or hoist the
`lit_count == 8` test to the top of `play_step` so a completed objective always wins
the frame it completes.

---

### BLEEDS-2 — A harmless wall-bump becomes lethal while the draught phases through the wall

**Scenario.** The player holds a direction **into a wall or building face** — normally
a no-op bump (they stay put). On the frame the draught is transiting *that exact wall
cell* (it ignores walls and routes through the buildings), the bump resolves as a
**life loss** instead of a bounce. Concrete: player at (9,6) holding LEFT into building
1's face at (8,6); the draught cuts diagonally through building 1 toward the player and
occupies (8,6) that frame → the player dies from pressing into a wall they can see is
solid brick. Corners against the border are the same trap.

**Confirmed in code.** `wall_at` (L1028) bit-tests the target cell's *attribute*.
While the draught occupies a cell, `draw_draught` has written `DRAUGHT_ATTR`
(`%01000101`) there — **bit 3 (WALL_BIT) is clear** — so `wall_at` returns "not wall".
In `player_step` `.pmove` (L541–561) the wall veto (`ret nz`) is therefore skipped, and
control falls through to the draught-contact test (`tcol/trow == draught` → `lose_life`).
So a bump into a draught-occupied wall cell is priced as a contact.

**Design's current answer.** None. The draught's wall-phasing (intended, "stone means
nothing to it") silently strips the wall bit from whatever cell it stands on, and the
collision code trusts that bit as the sole source of truth.

**Why it bites.** It is an input that is safe 99% of the time turning lethal on hidden
state, at the wall — precisely where a player hugs geometry to round a building. The
wall still *looks* solid; the death reads as unfair/random. It is more reachable than
BLEEDS-1 because wall-hugging near the buildings is routine play.

**Suggested direction (one).** Test the wall bit against the *map*, not the live
screen — e.g. keep the wall-veto reading a cell's true terrain (a separate flag byte,
or re-derive from the building table) so the draught's transient repaint can't unmask a
wall. Cheapest local fix: in `.pmove`, when the target equals the draught's cell, treat
it as blocked-and-safe (bump, no life lost) rather than contact — walking *into* the
draught over open ground still costs a life, but a wall you couldn't have entered anyway
shouldn't.

---

## By-design thinness (BLEMISH)

### BLEMISH-1 — Movement keys are undiscoverable without the manual

The title screen prints **PRESS SPACE** (start is discoverable) but nothing teaches
**QAOP**. A learner who built the game knows the keys; a cold player handed the `.sna`
(the brief invokes an "Itch.io-adjacent bar," §9) cannot find them from the screen. The
game's stated signposting principle — "colour temperature does it all, no tutorial
text" — covers *goals* (cold = to-do, warm = done) but not *controls*.
*Direction:* one line of key hint on the title, or accept it as curriculum-only and
drop the standalone-artefact framing for Module 1.

### BLEMISH-2 — The third lap is identical to the first

By anti-goal, everything is deterministic: same layout, same 8 lamps, same draught
path. Module 1 is over in ~10–20 s, so there is no "minute ten"; replay is the *same
content* with the only variable being how many embers you keep (`best_lives` pips). For
a first finished game this is defensible and the depth lives in Module 2 — but as a
standalone game the go-again hook is thin, and once you win with 3 lives it is
exhausted (best is maxed, never resets).

### BLEMISH-3 — The climax depends on route order the design doesn't control

Tension is real only when the draught is near the lamp you're lighting. A player who
lights the wisp-side lamps *last* gets a climax; one who lights them *first* finishes in
calm, the wisp trailing far behind — an anticlimactic win with no design nudge toward
the tense ordering. Fixed layout + player-chosen route = variable, sometimes-absent
final beat.

### BLEMISH-4 — Era bar: judged as a 1983 release, Module 1 is a type-in, not a Jetpac

The brief claims the Ultimate single-screen lineage (Jetpac/Pssst/Cookie). Those had
assembly/fuel/waves/scoring; Module 1 is one slow chaser, 8 pickups, ~15 s. Crash/YS
would call the standalone artefact *slight* (Pac-Man with a single ghost and no maze
constraint on the ghost). This is honest as *scope* ("a tiny finished game beats a
sprawling unfinished one") — but the Jetpac/Itch framing over-sells Module 1's
standalone heft. Module 2 is what actually earns the lineage.

---

## Closed holes (attacks the design already answers)

- **Park-and-hold / camping (the Starfield turret-park):** *closed.* The draught homes
  on the player's current cell every 16 frames and always closes Chebyshev distance
  (`draught_step` L690–747), so standing still is death — the menace probe `m1-probe`
  asserts exactly this and is green. Optimal play is active routing, not camping.
- **Respawn cascade (Dash's three-deaths-in-three-frames):** *closed, and explicitly
  tuned.* `lose_life` (L822–855) recoils the draught to its far corner (28,4) and resets
  its timer on every life lost; the code comment records the fix ("leaving it beside the
  respawn made a catch strip every life in seconds"). A catch buys a whole fresh chase.
- **Respawn onto a hazard:** *closed.* Start (15,11) is never a wall, lamp, or the
  draught's corner; respawn is always a safe cell.
- **Lit progress lost on death:** *closed.* Being caught on a lit lamp restores
  `LAMP_LIT` via `restore_under`; `lit_count` is untouched by `lose_life`. Deaths never
  cost objective progress.
- **Two movers corrupting one cell's save/restore buffer:** *closed by construction.*
  The player vetoes stepping onto the draught (L551–561 → `lose_life`) and the draught
  refuses to step onto the player (L748–761 → `lose_life`), so the two nine-byte buffers
  (`under_lamp`, `under_draught`) never point at the same cell. Mutual exclusion holds.
- **Free wall-pass while the draught phases a wall:** *closed* — the unmasked wall bit
  (see BLEEDS-2) does **not** let the player walk through; the draught-contact test
  catches it. (It converts to a lethal bump instead — that's the BLEEDS-2 defect, not a
  pass-through.)
- **Unwinnable / blocked lamp:** *closed.* All 8 lamps sit in open cobble outside the
  buildings, 4-connected-reachable; the draught chases the player and never camps a
  lamp, and occupies only one cell — no lamp can be permanently denied.
- **Soft-lock:** *closed.* Module 1 has no walling/spending mechanic (the tendril is
  Module 2). Every terminal state (WIN/LOSE) has a SPACE exit; the player can always
  move.
- **HUD corruption:** *closed.* The player is confined to rows 2–22 (wall veto at rows
  1/23), the draught only chases into that band, so neither ever writes the HUD row 0.
- **Ending-skip / accidental restart:** *closed.* `LOCK 25` gates SPACE on every screen
  transition (win → title → new game each dwell 0.5 s); playtest logged the lock as
  invisible (the pass condition for an input lock).

---

## Open questions (only a playtest can settle)

1. **Is the jeopardy experientially real for a *competent* player, or only for a naive
   one?** The player is 2.67× faster than the draught (pace 6 vs 16) and there is one
   greedy chaser on an open board, so a player who has internalised the speed edge can
   keep the draught trailing and win near-deterministically. The fail state is reachable
   (idle loses; the last-lamp approach carries *some* risk), so the gate passes — but
   whether the mid-game ever produces a genuine "will I make it?" beat rests entirely on
   one human playtest ("It works for me, it's not TOO hard," 2026-07-02, prototype-log).
   No systematic *optimising-player* probe exists. This is the thing to watch, not a
   defect: the baseline confession (finding #5, "won first time, zero challenge") was the
   pre-fix 8×/non-hunting draught; the current build is materially harder, but "gentle by
   design" and "thin to the point of decorative" are one playtest apart.
2. **Does the first death teach the rule?** The lives are red embers in the top-right HUD;
   when the wisp touches you an ember vanishes and you jump to centre. Whether a first-time
   player *connects* "the cyan thing touched me → that red pip top-right went out" without
   text is unverified.
3. **BLEEDS-2 reachability in real hands:** how often does a real player actually hold
   into a building face on the frame the draught transits it? Constructible for certain;
   frequency is a play question.

---

## Gate recommendation: fix-before-next-game vs wait-for-playtest

**Fix (or explicitly rule on) before building the next game — BLEEDS-1 and BLEEDS-2.**
Both are cheap, local, genuine correctness bugs in the contact/collision core. The
decisive reason is propagation: `a-game-needs-jeopardy.md` names Shadowkeep's Warden as
"Gloaming's draught grown up" — same seek-step mover, same attribute-byte collision.
Ship these bugs and Shadowkeep inherits both: a Warden that freezes you on the frame you
collect the last gold (BLEEDS-1 → "curse beats win") and that catches you when you press
into a wall it happens to be phasing (BLEEDS-2). Fixing them in Gloaming fixes the
pattern before it multiplies. BLEEDS-1 in particular is worth a decision even if the fix
is "accept it," because it is a curriculum artefact teaching the win/lose state machine —
the frame-ordering choice should be deliberate and documented, not incidental.

**Wait for playtest — everything else.** Open-question 1 (thin jeopardy) is already
playtest-accepted for a *first* game and the gate is green; re-open it only if a fresh
optimising-player probe says the mid-game is inert. BLEMISH-1..4 are framing/scope
calls, not defects — settle them when Module 1's standalone-vs-curriculum positioning is
next revisited, not on the critical path to the next game.
