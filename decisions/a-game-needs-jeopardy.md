# Decision: a game needs jeopardy

**Status:** Active (Steve, 2026-07-04). Curriculum-wide principle; first application is Shadowkeep.

## The principle

**A game is not a game without jeopardy.** A way to lose — a fail state the player can
actually reach — is constitutive, not decorative. Without it an experience may be a toy, a
walking simulator, or an explorable *place*, but it is not a *game*, and we do not ship it
calling itself one.

This is not a new idea to the curriculum — it is the idea the curriculum already *teaches*.
Gloaming's Phase D turns on it: unit 15 ends with "a completable toy — walk, light, warm, an
ending," and unit 16 opens with the indictment ("a chore-list with no antagonist") and the
lesson stated plainly — **a game needs a way to lose.** The Long Night spends ten units
deepening that antagonist. A learner reaches the end of the Spectrum assembly on-ramp having
internalised this. The course must hold itself to what it teaches.

## Why it binds now — Shadowkeep

Shadowkeep Arc 1 ("The Place") shipped as a deliberately **threat-free** exploration game —
the brief: *"forgiving in pass 1 (exploration, not threat — threat is a later revisit
module)"*, and *"The Place stands complete regardless"* (2026-06-12). It is winnable (collect
all gold → THE KEEP STANDS) but it **cannot be lost**: a sweep of all sixteen units finds no
enemy, no lives, no hazard, no fail state. Unit 16 nonetheless calls it *"a complete,
finishable game."* Under this principle, that claim is false, and the tension is at its
sharpest precisely because Shadowkeep now follows *The Long Night*: the learner arrives from a
five-watch siege into a keep with nothing to fear.

**This decision overrides the brief's "exploration, not threat / The Place stands complete"
line.** Shadowkeep must carry jeopardy to ship as a game.

## What changes (and what doesn't)

- **The jeopardy is already designed** — no invention required. The "inhabitants" revisit
  vision (*The Waking*, 2026-06-12) settled the threat in principle: a **curse**, not combat
  (the explore-and-avoid / no-combat anti-goal holds) — *caught, you join the sleepers,
  frozen mid-stride.* Two candidate shapes, both with engine lineage: **the Warden** (a
  deterministic cell-patrol freezer — "Gloaming's draught grown up"; touch = stasis) and **the
  briar** (static curse-tiles, denser in deeper rooms). "Hold back the dark" is already the
  brief's own pitch line.
- **Decouple the jeopardy from the full revisit.** The *minimum* to make Shadowkeep a game is
  a threat and a lose state — start with one curse shape (recommend the Warden: direct engine
  lineage, most readable, connects to what the learner just built). The richer *Waking*
  content (unfreezing NPCs, the puzzle-dependency graph, allies-as-lives) remains a later
  revisit; it is the *elaboration*, not the requirement.
- **The Place's exploration/atmosphere identity is not discarded** — the light-and-shadow
  system, the room graph, the sense-of-place pedagogy all stand. Jeopardy is *added to* them,
  not swapped for them. Knight Lore, the stated mood archetype, has guardians *and* mood.

## The bar this restores

The per-game **winnability gate** already requires each game be driven to its win state by a
scripted run *and* its loss path exercised the same way. A game with no loss path passes the
gate only vacuously. This principle closes that gap: "where the game can be lost" is not
optional — the game must *have* a loss to exercise.

## Drift triggers

- *"It's a complete, finishable game"* said of something with no fail state — it is finishable,
  not losable, and that is the tell. Ask: how does the player *lose*?
- *"Exploration/atmosphere is the whole point; threat would spoil it"* — Knight Lore is the
  counter-example the brief itself cites: atmosphere and jeopardy coexist, and the jeopardy is
  what makes the atmosphere *matter*.
- *"Threat is the next module's job"* — deferring the fail state defers the game. The next
  module may deepen jeopardy; it may not be where jeopardy first *exists*.

## Next steps (Shadowkeep, pending approval of approach)

Follow the proven Gloaming flow, not a straight edit of shipped units: **prototype** the curse
threat on the Shadowkeep engine → **/design-stress** it → **decompose** into a jeopardy
sub-phase (and reconcile the Place's units + the "complete game" framing) → **re-gate** with
win *and* loss scripts in `capture/`. The brief and
[shadowkeep-four-arc-framing.md](shadowkeep-four-arc-framing.md) get amended to match.
