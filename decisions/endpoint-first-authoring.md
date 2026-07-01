# Decision: the endpoint comes first — build the game, then author the route

**Status:** Active. Applies from the game-2 wave (Exodus onward) **and retroactively to the
five shipped launch on-ramp games** — see the 2026-07-01 amendment.
**Date:** 2026-06-12.

> **AMENDED 2026-07-01 — extended retroactively to the launch games, as *validate-and-repair*.**
> The original scope ("game-2 wave onward") is widened: the five shipped, forward-authored launch
> on-ramp games — **Gloaming, Shadowkeep, Starfield, Dash, Flock** — are brought to the endpoint-first
> bar before October. This reverses the forward-authoring debt the § *Why* describes, rather than
> only avoiding it on new games.
>
> **Altitude: validate-and-repair, not from-scratch re-author.** Build the missing piece — the
> winnable, playtested prototype — and let it prove or break the *existing* route; then re-author
> only the units the prototype disproves. Endpoint-first applied as **rescue**: keep the prose that
> survives contact with a working game; fix the Dash-class geometry/tuning bugs the gate catches.
> **Pivot to full re-author only where a game genuinely doesn't work** — where the built game can't
> be made winnable/coherent by repair. That judgement is made *with the prototype in hand*, not
> speculatively.
>
> **Guardrails (binding on this amendment):**
> - **Never regress the launch.** Each shipped game stays live and marked `complete` until its
>   rebuilt version passes the winnability gate *and* the 8-item DoD. A rebuild replaces the old game
>   only when the new one is provably better. Worst case is "we shipped what we already had," never
>   "we tore down five games and ran out of clock."
> - **Never more than one launch game in-flight at a time.** Sequential, not parallel — "done" does
>   not become "in-progress on a deadline" across the whole slate.
> - **Prove the pipeline once before committing to five.** No endpoint-first rebuild of a *launch*
>   game has been done (Exodus, the intended first, is parked), so per-game cost is unknown. Start
>   with **Gloaming** (smallest game, most mature tooling, partial win captures already present),
>   time it end-to-end, then size the remaining four against a real number rather than hope.

## The decision

From the game-2 wave (Exodus onward): a game's complete, winnable, playtested build exists
**before** unit authoring begins. The brief designs the endpoint ("The Finish" section,
[specifications/brief.md](../specifications/brief.md) §9); a prototype proves it (the
winnability gate in [commercial-bar-revamp.md](commercial-bar-revamp.md), plus a human
playtest); the unit sequence is then derived backwards from the working game.

The working order per game:

1. **Brief** — answers "The Finish" (the endpoint, designed).
2. **Prototype** — build the complete game to the winnability gate; playtest it; tune it
   (the endpoint, *real*).
3. **Decompose** — derive the unit sequence backwards from the working game, keeping the
   genuine discoveries as the confessions they were.
4. **Author** — each unit walks a verified route; no unit ever needs a retrofit.

## Why

All four first games were authored forward — units accumulated until a game was declared —
and every one needed retrofit units to make the declaration true (Gloaming unit 21,
Starfield unit 17, Dash unit 17, Flock's polish pass). Dash needed its level geometry
*fixed*: the spike gap was one pixel wider than the jump, so the published route led to a
destination nobody had visited. Forward authoring publishes a route to an unvisited
destination.

The Lucky Number scaffold pattern (chosen for Cadence / Nightshade / Exodus in
[commercial-bar-revamp.md](commercial-bar-revamp.md) § Pattern) already implies this order:
unit 1's typed-in working systems must exist to be typed in.

## What this does not change

- **Honest confessions remain first-class.** Discoveries now happen during the prototype —
  where fixing is cheapest — and are *narrated* where they pedagogically belong, which is
  how Flock's phantom-vblank story already works (hit before unit 12, taught in unit 12).
- **Incremental construction, spiral progression, and the per-unit DoD are untouched** —
  this sequences the work, not the teaching.
- **No fixed unit counts** — decomposition produces however many units the route needs.

## Inputs to the flow

Each stage's inputs, so nothing gets improvised mid-game. Most are existing project
layers; two are **new conventions this record creates**, marked ✦.

**1. Brief (the endpoint, designed)** — the platform's lineup record (which rung, what
technique budget); classic ancestors and **period magazines** as primary sources for the
genre's shipping conventions; the layered hardware-reference canon (what the machine can
do, with provenance); "The Finish" (§9); deprecation pairs (what this game does the
"before" way on purpose); the pattern library (named reuses in, expected extractions out).
The brief spec carries its own inputs note — see
[specifications/brief.md](../specifications/brief.md).

✦ **The design-stress pass** — the `/design-stress` skill attacks the revised brief before
any prototype work: dominant strategies, tension collapses, unwinnable states, verb
exploits, the boredom test. Its `BREAKS`-severity findings gate Stage 2; its open
questions seed the prototype discovery log. It runs again against the playable prototype.

**2. Prototype (the endpoint, real)** — Emu198x (runtime, capture, queries); the
assemblers; Build198x for asset conversion; the winnability gate (win *and* loss scripts,
checked into `capture/`); the playtest sheet and a human pass; the design-stress re-run.

✦ **The prototype discovery log** — `docs/platforms/{system}/games/{slug}/prototype-log.md`,
kept *as the prototype is built*: every bug hit, dead end taken, surprise found, with
enough detail to re-tell. Under endpoint-first this is the only place confession material
gets generated — by authoring time the route is solved — so the log is what keeps the
units as honest as Flock's. It feeds the confessions, the "If It Doesn't Work" sections,
and the blog.

✦ **Commit-sized teachable increments** — the prototype is built in commit-sized steps
that each add one teachable idea, so its git log is the decomposition's first draft.
(This is the project's existing coding cadence applied with intent: the prototype's
history is itself an artefact.)

**3. Decompose (the route)** — the prototype's construction history; the discovery log
(deciding *where* each confession is taught); the unit spec; the scaffold pattern chosen
in the brief (incremental vs Lucky Number); phase boundaries.

**4. Author (the telling)** — the unit spec and magazine voice; Vale; the capture
pipeline, with the win script reused as capture choreography; the per-unit DoD;
screenshot verification.

**5. Post-ship (the compounding)** — pattern extractions (brief §13); vault tie-ins
(§14); `docs/log.md`; blog material from the discovery log.

**Learner feedback (decided 2026-06-12):** from October, learner feedback arrives via
**Discord** (community, real-time) and **GitHub Discussions** (durable, searchable).
Routing rule: Discord is ephemeral — anything actionable (a stuck point, a suspected
bug, a tuning complaint) gets promoted to a Discussion or an issue so it lands in the
durable ledger; confirmed code bugs go to issues as ever. Standing both up — the server,
the Discussions surface, and a "where to get help" pointer in every getting-started
page — is a pre-launch checklist item.

## Drift triggers

- Authoring unit 1 of a game whose win state has never been reached.
- "We'll design the ending when we get there."
- A brief whose Finish section is unanswered while units are being written.
- A prototype "too rough to playtest" that units are nonetheless being derived from —
  the prototype must pass the winnability gate *and* a human pass before decomposition.
- A prototype built without its discovery log — if the log is empty at decomposition
  time, the confession material is already lost.
