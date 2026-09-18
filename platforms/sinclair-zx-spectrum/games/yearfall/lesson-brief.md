# Yearfall — teaching progression

**Status:** The native game is accepted and the user authorised lesson development.
Thirteen lessons use eleven independently runnable checkpoints. The local lesson
preview remains subject to review; publication has not been authorised.

**Endpoint:** `code-samples/sinclair-zx-spectrum/basic/yearfall/prototype/yearfall.bas`
at samples commit `03afc02`. The finished checkpoint is byte-identical. Preserve
separate buying/selling, explicit cost/proceeds, editable food and planting,
fed-worker limits, yearly accounting, traveller offers and decade continuation.
Stock 48K PAL Sinclair BASIC, deliberate silence and no real-time deadline.

## Central idea

A proposed allocation is separate from committed resources. A valid plan can
still make future years difficult. Teach the accounting before adding input,
then connect the order of a year with the choices visible on screen.

## Runnable progression

| Lesson | Checkpoint | Result and local explanation |
|---|---|---|
| 1. Read the settlement | `ledger` | New nine-line program: named resources, character positions, GO SUB/RETURN and deliberate STOP. |
| 2. Feed the people | `food` | Inspect a food proposal, whole rations, capping, string warnings and a grain balance; STOP. |
| 3. Share the grain | `seed` | Food and seed share stock; fed-worker and land limits reject impossible plans; STOP. |
| 4. Resolve a harvest | `harvest` | Commit one valid plan, draw a complete report and STOP; random yield but no growth yet. |
| 5. Edit an allocation | `editor` | F edits food; digit validation, deletion, cancellation, release gate, Space commitment and R/Q. Planting stays fixed at 100. One year only. |
| 6. Plan before committing | `planner` | P edits planting, affordable starting proposals and visibly invalid drafts. One year only. |
| 7. Carry the year forward | `years` | Growth, retained resources, repeated years, cumulative deaths and ten-year/empty endings. Land stays fixed. |
| 8. Buy and sell land | `trade` | Separate controls, one signed internal proposal, market price, ownership and explicit spending/proceeds. |
| 9. Read a shortage | Reuse `trade` | Worked resource trace; distinguish closing a shortfall from securing the next year. No new program. |
| 10. Welcome travellers | `visitors` | Scheduled offers before planning, explicit fee/food requirement, acceptance/refusal and report accounting. Ten-year ending retained. |
| 11. Keep ruling | `continued` | Decade reviews and C continuation preserve the settlement, history and next visit. |
| 12. Invite the ruler | `finished` | Accepted title and S/Q entry; complete endpoint without economy changes. |
| 13. Keep the settlement | Reuse `finished` | SAVE with LINE 10, exported TAP, fresh load and end-to-end recovery checks. Program saving is not campaign persistence. |

The first listing is a new program; do not instruct the reader to add every line.
Each later source transition has exact additions, replacements and deletions,
ordinary changed-line listings and complete source. Short checkpoints show their
full listing directly. The manifest reconstructs every source from those edits.

## Worked checks and temporary rules

The food example tries 179 grain: 59 complete rations, one potential death and
181 remaining before seed. Planting 100 with food for forty fails the worker
limit even when the grain budget fits. Single-year checkpoints intentionally
lack later growth or continuation; state those limits in the lesson.

The shortage fixture uses 60 people, 220 grain, 100 acres and price eight. Set
planting to 100 to expose the sixty-grain shortfall; default planning would
otherwise reduce planting to forty. Selling seven and planting ninety-three
leaves three grain, with possible post-harvest balances 189–468. At the poorest
yield, the next population of 63 needs all 189 for food, leaving no seed budget.
The lesson labels the direct ROM setup commands as an experiment, not normal
play. No public capture comes from altered game-state fixtures.

The traveller example is from the accepted prototype's seeded run: five people
cost thirty grain, taking 737 to 707; population 66 becomes 71 and annual food
becomes 213. The welcome does not pay that food. A four-digit editor limits
arbitrarily large settlements; thirty-year evidence is not an indefinite-play
claim.

## Verification and site integration

Enter every checkpoint in a fresh 48K ROM using keyword keys, record a TAP with
auto-start at ten, and load it in a separate process. Audit literal targets,
transition reconstruction, unchanged token bytes, tape checksums and evidence
hashes. Run the complete accepted-prototype suite against the independently
entered finished checkpoint. Record ordinary ROM diagnostic commands separately
from legal game input; observe memory without direct writes.

Check food/seed limits, input and held keys, incomplete-stage behaviour, report
accounting, reset/quit, land directions, the worked shortage, accepted/declined
travellers, finite intermediate endings and the final continued run. Execution
of intermediate stages is not independent learner acceptance.

The local preview places Yearfall beside The Caverns in Hidden worlds, extends
the group description to lasting decisions, preserves numeric identities and
redirects six old topics on canonical and legacy paths. The overview and thirteen
lessons require production, browser, keyboard and accessibility checks before
review. The prepared What's New entry stays a draft.

Language sources: Steven Vickers, edited by Robin Bradbeer, *ZX Spectrum BASIC
Programming*, second edition (1983), chapters 2–3, 5, 7–9, 11, 13–16, 18 and 20.
The maintained primary-source extract was checked for INT, randomness, keyboard
polling and tape semantics; learner pages cite the public manual chapters.

Implementation and evidence: [teaching implementation](lessons.md).
