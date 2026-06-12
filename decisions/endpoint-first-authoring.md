# Decision: the endpoint comes first — build the game, then author the route

**Status:** Active. Applies from the game-2 wave (Exodus onward).
**Date:** 2026-06-12.

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

## Drift triggers

- Authoring unit 1 of a game whose win state has never been reached.
- "We'll design the ending when we get there."
- A brief whose Finish section is unanswered while units are being written.
- A prototype "too rough to playtest" that units are nonetheless being derived from —
  the prototype must pass the winnability gate *and* a human pass before decomposition.
