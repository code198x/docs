# Shadowkeep — design-stress: the Warden jeopardy (2026-07-04)

Adversarial pass on the Warden — the fail state added to make the Place a *game*
([a-game-needs-jeopardy.md](../../../../decisions/a-game-needs-jeopardy.md)). Run against the
working prototype (`code-samples/.../shadowkeep/prototype/shadowkeep-warden.asm`): a single
deterministic patrol-freezer on row 11 of the Hall, touch = THE KEEP SLEEPS. Refutation, not
review — every finding is a scenario a bored clever player runs.

**Headline:** the prototype *proves jeopardy is possible* (the Place is losable, verified
headless). But the minimal single-Hall Warden is **not yet a game** — the threat is quarantined
away from the objective. The gold is elsewhere; the Warden is a turnstile you time once. The
good news: the fix is curriculum-*positive*.

## Findings (severity-ordered)

### BREAKS

**B1 — The threat is quarantined from the objective (dominant strategy + tension collapse).**
*Scenario:* The Hall's two coins sit at (col 7, row 2) and (col 21, row 20) — top and bottom
bands. The Warden patrols row 11 (the middle). The other four coins are in rooms 1–2, which have
no Warden at all. Optimal play: collect the four safe coins with zero risk; for the two Hall
coins, stay in the top/bottom bands and cross row 11 exactly once each, waiting until the Warden
is at the far wall (a ~300-frame window on a 30-cell sweep). You never share ground with the
threat while doing the thing the game is about. *Design's answer:* none — the Warden guards a
line, not the gold. *Optimal play is "stand still and wait," which is the Starfield turret-park
in a cloak.* **This is the break: a threat that doesn't contest the objective is décor with a
kill box.**

### BLEEDS

**B2 — Threat density below the era bar (thin).** *Scenario:* Atic Atac roams multiple nasties
*per room* over a health timer; Sabre Wulf fills every screen with beasts; Knight Lore layers
guardians on the day/night curse. This is one patroller in one of three rooms. *Crash/Zzap!
verdict: thin.* The "minimal jeopardy" instinct became "one-room jeopardy," which is a different,
worse thing. *Answer:* none yet.

**B3 — The door is a free escape on the patrol row.** *Scenario:* The east door sits at
(col 31, row 11) — on the Warden's line. With the Warden bearing down, step east through the
door: `check_exit` fires, you're in the Gallery, the Warden is shed mid-approach with no cost.
The one place the Warden could pressure you (the row-11 crossing) is the exact place you can
leave for free. *Answer:* none.

**B4 — Death on room entry, no grace.** *Scenario:* Re-enter the Hall from the Gallery at row 11
(`.west` places you at col 30, row 11 — the patrol row). If the Warden is near the east end, you
materialise onto or beside it → instant THE KEEP SLEEPS with no gather, no telegraph, no input.
The prototype redraws the Warden on entry but never checks for immediate overlap. *Answer:* none.

**B5 — One touch → full title reset, no lives.** *Scenario:* First contact throws you to the
title; all six-coin progress gone. This is *harsher* than the lineage it cites — Atic Atac gives
you a health bar, not one-hit-to-menu — and it collides with the brief's "forgiving in pass 1"
and with discoverability (the first death, which should teach, instead erases the session).
*Answer:* none in Arc 1; the lives economy (allies-as-lives) is deferred to the Waking revisit —
which leaves Arc 1 with the harshest possible loss.

**B6 — No curve (boredom).** *Scenario:* Minute 10 = minute 1. The single route is learned in
~30 seconds; every subsequent run is the same ~90-second solved puzzle, and there's no score to
chase. *Answer:* none — but pass-1 scope may accept a flat curve if B1–B4 are fixed; escalation
is a later-arc / playtest concern.

### BLEMISHES

**B7 — The Warden rests on the door cell.** At col 31 it reverses (col 32 reads the wrapped
wall). Cosmetically it sits in the doorway — which actually reads as *guarding the door*. Keep;
noted only so it isn't mistaken for a bug later.

## Closed holes (strengths — the decompose must not regress these)

- **The gather beat** (80 frames before it moves) — you read the board before the threat starts.
  Closed, keep (it's Gloaming's lesson, reused).
- **Deterministic, memorisable patrol** — genuinely *not* Gloaming's hunting draught; it walks a
  route you time, Sabre-Wulf-wise. This closes the "feels like the draught again" risk. Keep the
  determinism — the fix for B1 is *placement and density*, not randomness.
- **Two-mover engine reuse** — the Warden is the thief's save/restore/draw with its own buffer.
  Closed (after the proposal-clobber bug fix); it's the buffer discipline the course teaches.

## What the minimal design actually needs to be a game

1. **A Warden in every room the player must clear** — data-driven, one per room, the *same*
   two-mover code instantiated from a table (exactly like the torch and gold systems already
   are). Fixes B1 (threat where the objective is), B2 (density), and the dead air in one move.
2. **Gold on contested ground** — place coins so reaching them means entering a patrol's reach.
   Pure level-design; turns "wait for the far sweep" into "read the route, take the gap." Fixes
   the want-against-threat the loop currently lacks.
3. **Entry + first-death fairness** — clear the entry cell of the patrol (or a per-room gather),
   and soften the loss below one-hit-to-title (a small lives buffer, or respawn at the room
   entrance). This one needs a *design decision*, not a patch: reconcile with the deferred
   allies-as-lives economy (a plain lives counter now may pre-empt it).

Findings 1–2 are the difference between "losable" and "a game." Crucially, the fix is
**curriculum-positive**: a Warden-per-room is the engine's own generalisation lesson ("a second
mover is data, like the lamps in Gloaming"), not new technique or budget.

## Gating

- **Must be answered in the design before Stage 2 (decompose into units):** B1, B2, B3, B4 —
  they change the *shape* (per-room wardens, gold placement, entry handling), so they must be
  settled before any unit is cut.
- **Needs a design decision before decompose:** B5 (lives vs the deferred allies economy).
- **Can wait for playtest / later arcs:** B6 (curve).

## To the prototype discovery log

- Confirm the row-11 crossing window empirically once wardens are per-room (does the timing stay
  fair when several patrol at once?).
- Does a *following* Warden (crosses doors with the thief) read as fairer or nastier than
  per-room wardens? Only hands can say.
