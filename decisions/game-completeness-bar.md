# Decision: The game bar is tested, not declared

**Status: PROPOSED — draft for review, 2026-08-28.** Nothing descends from this yet.

> **Review context, 2026-09-05:** [The adopted scope-relative quality bar](scope-relative-game-quality.md) does not adopt this proposal’s universal commercial-comparator gate. This document remains a proposal.

## The decision

A game is measured against a **named comparator** from its platform's era, at three scales, before its final module is marked `complete`.

The project gates correctness at unit scale and completability at game scale. Neither tests whether the result is a game anyone would have paid for. That is what these checks are, and the property that matters is that each of them can **fail**.

### 1. Census — countable, and cheap

For the game and for its comparator, count what a player meets:

- distinct screens or rooms
- distinct enemy or hazard behaviours (not instances)
- distinct player verbs
- sprite frames of animation for the player
- distinct pieces of music, and distinct sound effects
- distinct level-scale mechanics that change how a screen is played

The numbers need not match — Atic Atac had a team and a year. An order-of-magnitude gap in every column is the measurement of budget scale wearing a full-price label, and it is visible in an afternoon.

### 2. Sitting — the comparator is played, not cited

Someone plays the comparator and then the game, back to back, and writes down what the comparator does that ours does not. That list is the finding, and it is filed with the brief.

Naming Knight Lore in a decision record is not the same as having played it beside the thing being shipped.

### 3. Cold play — does it work without the curriculum

The built artefact goes to someone who has not read the units and is not told anything about it. Then the comparator goes to the same person, in the same session, under the same conditions. Fifteen minutes each, order alternating so the second slot is not always the tired one.

**Watch. Do not ask.** Where someone stops is data; what they say afterwards is politeness.

| Recorded | Ours | Comparator |
|---|---|---|
| Time to first deliberate action — did they work out what to do, unprompted | | |
| Did they start again after dying, without being asked to | | |
| Where they stopped, and what was happening at that moment | | |
| Anything they said out loud, unprompted, verbatim | | |
| Afterwards: what is this game? — one sentence, in their words | | |

Absolute judgements about fun are worth little; comparative ones are worth a great deal, and the comparator is sitting right there. The finding is the difference between the columns.

**What counts as failing.** A player who does not reach a deliberate action inside a couple of minutes has not been given a game they can enter. A player who does not restart after the first death has not been given a reason to. A player who cannot say what the game is has played a demonstration.

None is fatal alone; all three are information. What is not permitted is running the session, seeing the answer, and marking the module complete without recording either the fix or the reason for accepting it.

**Who.** Not the author, and not anyone who has read the units.

### The gate

Before the module that completes a game is marked `complete`:

- [ ] Census recorded for the game and its named comparator
- [ ] Sitting done, and the gap list filed with the brief
- [ ] Cold play run against the comparator, observed rather than surveyed, findings filed
- [ ] The game works as an entry point: the concepts it assumes are declared, and a learner starting here can satisfy them
- [ ] Where a gap is accepted rather than closed, the brief says which, and why

The last item keeps the rest honest. Accepting a gap is legitimate — a curriculum game will never have Ultimate's art budget. Accepting it *silently* is the failure this decision exists to prevent.

## Every game is a door

A learner starts with whichever game they want. No game is a prerequisite for another.

Dependency is between **concepts**, not games. A game declares which concepts it assumes — *pre-shifted movement assumes you have met cell-step movement and felt its limit* — and a learner satisfies that either from a game they have already built or from a short on-ramp inside the game they chose. The prerequisite graph is over concepts; games are entry points into it; a route is one path through it rather than the only path.

### The floor is the primer

A game may assume everything its track's primer teaches, and nothing else.

Every track opens with a teaching module — `meet-the-machine` on the assembly tracks, `meet-basic`, `meet-c64-basic`, `meet-amos`, `meet-blitz`. C64 BASIC runs two, so a primer that grows has precedent.

The primer is the one module that is not a door. It is the floor every door opens onto, which makes the honest phrasing **start with any game you like, after the primer** — and the site should say that rather than implying a learner may begin anywhere at all.

When a game needs a concept the primer does not teach, it either teaches it locally or the primer expands. Expanding is a valid choice, and it is what stops fourteen games carrying fourteen copies of the same on-ramp.

**Promotion rule.** A concept earns a place in the primer when a *second* game needs it and the local teaching would be materially the same content. The first game to need something teaches it locally; the second promotes it.

Without that rule the primer absorbs everything a game might want and grows to the size of a track — too much asked at the door, in the one place it is easiest not to notice.

### Local motivation beats remembered motivation

"Your sprite erased the wall it walked over" lands hard when it happened five units ago and softly when it happened in a different game two months back.

Requiring each game to manufacture its own "before" moment makes the deprecation pair local, and a local pair is tighter. The duplication this costs is what the longer timeline buys.

### What it requires changing

This amends three active decisions:

- [deprecation-pairs.md](deprecation-pairs.md) — the tree rooted in Gloaming becomes a graph over concepts. Naive-first is unchanged; where the "before" half lives changes.
- [spectrum-assembly-gentle-ramp.md](spectrum-assembly-gentle-ramp.md) — the rendering ladder orders concepts, not games, and several games may enter it at different points.
- [spiral-and-incremental.md](spiral-and-incremental.md) — deepening across games needs a concept to deepen from, declared rather than assumed.

Each needs its own amendment before this is adopted.

## What this costs

A game held to this bar is bigger and slower, and a game that is also a door carries its own on-ramp — offset by the primer holding the shared floor.

Three ways to absorb it, mutually exclusive at any given pace:

**Fewer games per track.** Genre breadth gives, and it is currently a primary goal.

**Fewer tracks.** Four systems and eight tracks is wide for one author. Depth on Spectrum and C64 is defensible and least damaging to any individual game.

**A longer timeline.** Keeps breadth and depth, costs years, and leans harder on an acceleration assumption that is already load-bearing.

**Current leaning: the longer timeline**, with the lineup expected to shrink as a consequence rather than as a separate lever. Neither is settled here.

## What it means for the modules already complete

Nothing is retracted. Applying this backwards produces a census and a gap list per game, which is information rather than a rewrite order.

The October artefact is exempt from *content* change until after CRASH! Live. Measuring it is fine; rewriting it two months out is the one move that can break the launch.

## Evidence

Spectrum assembly, units per module: Gloaming 21, The Long Night 11, Shadowkeep 20. The entry game is the largest thing in the track and the flagship is smaller than it.

The unit craft is not the problem — Shadowkeep 17, beeper ambience motivated by a felt absence, is good teaching. The failure is at game scale, which is why unit-scale gates cannot catch it.

## Open questions

- Which comparator per game — named in the brief, or fixed per platform?
- Does the census gate a module, or only inform it? Drafted as a gate; there is an argument for the first pass being informational.
- Cold play needs a person who is not you. Who?
- How large may a primer grow before it is itself too much to ask at the door?
- Entry-point mechanics — how a game declares and offers its prerequisites — deferred.

## Relationship to other decisions

Descends from [commercial-bar-revamp.md](commercial-bar-revamp.md) and [real-retro-games.md](real-retro-games.md). It changes neither bar; it supplies the test both assumed and neither specified.
