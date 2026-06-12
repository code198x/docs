# Design Stress — Exodus (rung-2 Blitter puzzle)

**Run:** 2026-06-12, against `brief.md` (resumed revision), per the `/design-stress` skill.
**Stance:** refutation. Findings are falsifiable scenarios, ordered by severity.

---

## Findings

### BREAKS

**B1 — The trapped walker is a soft-lock in the core loop.**
*Scenario:* carve a pit (or any concave shape) on the route; a walker drops in and
ping-pongs between its walls forever. It is not home (win requires *all* sheep at the gate)
and not lost (no hazard in the pit) — the level can never end. The player carved the trap
*with the game's own headline verb*, so this is reachable on level one.
*Design's current answer:* none. The pattern extraction mentions "commit and reset", but
nothing ends a stuck release.
*One direction:* an abandon control during release ("call it") that scores the stragglers as
lost and returns to plan — Lemmings' bomber existed for exactly this reason.

**B2 — Retry semantics are undefined, and the wrong default ruins the loop.**
*Scenario:* the player makes four careful edits, releases, and one sheep drowns. "Instant
retry" triggers — and if retry wipes the plan, they re-click four edits from memory to change
one. Repeat per iteration. The design *depends* on iteration (deterministic levels, all-survive
wins) while the loop, read literally, punishes it.
*Design's current answer:* "instant retry keeps it light" — intent right, mechanics unstated.
*One direction:* retry returns to **plan phase with the edit list intact and editable** —
which implies edits live as a data list replayed onto restored terrain (and that architecture
gives B3's undo nearly for free).

**B3 — No undo in the plan phase: a misclick spends the scarcest resource.**
*Scenario:* mouse-driven, single-click commits a carve, budget of ~4. One slip of the pointer
burns 25% of the level's resource with no recourse except a full reset (re-doing every other
edit). On a 1985 joystick game this was survivable; on a mouse game it's a misclick tax on
the exact input device chosen for precision.
*Design's current answer:* none (reset only).
*One direction:* plan-phase undo over the edit list (see B2); grid-snapped edit placement
shrinks the misclick space further (see L1).

### BLEEDS

**D1 — The stated emotion and the actual structure disagree.**
*Scenario:* the brief's core experience is loss-aversion — "sick when one ambles off a cliff."
But with all-survive wins, free instant retry, and full determinism, a death costs *one
keypress*. The first release per level is held-breath; every subsequent release is
engineering verification. The game's real texture is Incredible-Machine-style iteration —
which is a *good* texture, but it isn't the one the brief designs feel around.
*Design's current answer:* partially named (Risk 1, "might play flat"), but framed as a
pacing risk, not an emotional-thesis mismatch.
*One direction:* choose the emotion. Either embrace iteration (tension = elegance: par
scores, edits-remaining as the brag — which also answers the missing go-again hook), or give
loss a cost that survives retry (flock persistence across levels — riskier, threatens
unwinnable campaigns). Decide at Stage 1; the prototype tests the choice.

**D2 — Repeated release-watching with no speed control.**
*Scenario:* a 30–60s amble across the screen, watched 4–6 times per level while iterating
(D1), with intervention forbidden by anti-goal. Minutes of dead air per level, all of it
deterministic re-runs of footage the player has already seen.
*Design's current answer:* none.
*One direction:* a fast-forward during release — period-true (Lemmings shipped one) and
trivial under a frame-locked loop.

**D3 — Raise can entomb or wall in.**
*Scenario:* raise terrain on the flock's start cluster (they exist on-field during planning)
— release; everyone is inside a stone block. Or wall off the gate. Both reachable with one
edit, both dead states answered only by reset.
*Design's current answer:* none.
*One direction:* forbid edits within the start zone, the gate zone, and any creature
footprint — three rectangle tests during plan-phase clicks.

**D4 — Raise-bridging pressure on every level design.**
*Scenario:* any hazard whose width ≤ the raise budget is not a hazard, it's a toll. "Just
bridge it" must lose to the budget on every level or the raise verb deletes the puzzle.
*Design's current answer:* implicit (budgets "bite" per ship test) — but not stated as a
level-design law.
*One direction:* a level-design rule in the revision: every hazard is priced against its
cheapest bridge, and at least one hazard per late level must be *unbridgeable on budget*
(forcing the carve/route answer).

**D5 — Content volume vs the era bar.**
*Scenario:* a 1991 reviewer scores it: "charming, over in an afternoon — five levels."
Lemmings shipped 120; budget-label puzzlers shipped 20+. The bar is budget-label, and 5–7 is
below even that.
*Design's current answer:* "roughly five to seven" with no framing.
*One direction:* make levels pure data from the prototype onward (terrain + budgets + spawns
as a level row — the escalation-as-data pattern at full size); then the level count is a
content dial, not a code cost, and can rise post-playtest without touching the curriculum.

### BLEMISHES

- **P1 — Fatal fall height is undefined.** If absent, carving is risk-free verticality; if
  present, it's a hidden rule that kills (Lemmings telegraphed by splat). Decide, then
  telegraph.
- **P2 — Off-screen-bottom is undefined.** Carve through the floor: where do they go?
  (Recommend: off-screen = lost, visibly.)
- **P3 — Walker–walker collision is undefined.** Recommend Lemmings ghosts (no collision) —
  anything else creates emergent jams the planner can't plan for.
- **P4 — Plan vs release phase must be unmistakable.** Cheapest period-true tell: a Copper
  tint shift on the sky between phases.
- **P5 — Active-verb visibility.** The pointer should *be* the brush preview (footprint +
  verb shape under the cursor) — which is also the feel answer The Finish needs.

---

## Closed holes (the brief's strengths — the prototype must not regress these)

- **Determinism is an anti-goal-level law** ("plan-then-release cannot survive dice") —
  closes the whole class of unfair-reveal complaints.
- **Plan-phase-static creatures** close most mid-state edit horrors (no carve-under-a-
  walking-sheep cases — edits and motion never coexist, except via D3's start-zone gap).
- **No-real-time-intervention is held loosely** with the reconsideration trigger named —
  the right epistemic posture for the design's biggest unknown.
- **The verb ramp** (carve → raise → both → tighter → dynamic hazard) is a clean
  one-new-idea-per-level curve.
- **The agency risk is named in the brief itself** (Risk 2) — the un-briefed Exodus's
  failure mode is being watched for.

## Open questions → prototype discovery log

1. Does the reveal carry tension on the *first* release of each level (the only one D1 leaves
   it)? This is Risk 1, sharpened.
2. Are floating raises (unsupported platforms) allowed? Trivialises cliffs if yes; demands
   support rules if no. Prototype both for an afternoon.
3. Grid size for edits (8px vs 16px) — feel vs blit-alignment pedagogy (word-aligned carving
   needs no barrel shifter: Arc 1 simplicity, and a later "unaligned blits" unit).
4. Release duration at amble speed — the number D2's fast-forward is tuned against.
5. The go-again hook (The Finish): par-under-budget score? Edits-remaining tally? Decided in
   Stage 1, tested in the prototype.

## Gates

**Must have design answers in the Stage-1 brief revision (gate Stage 2):** B1, B2, B3, D1
(the emotion decision), D3 (the zone rule — one sentence).
**Adopt as rules now, verify in prototype:** D2 (fast-forward), D4 (the bridge-pricing law),
P2, P3.
**Playtest-time:** D5 (level count dial), P1, P4, P5, and all five open questions.
