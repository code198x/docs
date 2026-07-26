# Exodus (rung-2 Blitter puzzle) — Brief

**Title (working):** ***Exodus*** — name reclaimed 2026-06-12 (the `exodus` module; was provisionally "Flock")
**System / Track:** Commodore Amiga / assembly
**Position:** Rung 2 — the Blitter game (copy + masked cookie-cut blit), after the rung-1 sprite crosser. See [amiga-assembly-lineup.md](../../../../decisions/amiga-assembly-lineup.md).
**Scope:** indicative ~16 units across two build arcs; counts illustrative, not a target (per [curriculum-structure.md](../../../../decisions/curriculum-structure.md)).
**Constraint position:** period-faithful — see Section 5.
**Status:** **resuming** — theme decided; brief revision (endpoint-first Stage 1) is the next step

> **RESUMED 2026-06-12 — theme decided: *Exodus*, reclaimed.** The game is a **migration through
> hostile terrain**: a band of walkers led to safety by a god-hand that **carves through rock and
> raises causeways over water** — the verbs *are* the theme (a raised path through the water is the
> name made literal). The sheep references and pastoral framing throughout this draft are
> **placeholder prose pending the Stage-1 brief revision**, which re-themes the sections and answers
> "The Finish" ([specifications/brief.md](../../../../specifications/brief.md) §9) per
> [endpoint-first-authoring.md](../../../../decisions/endpoint-first-authoring.md): brief → prototype
> (winnability gate + human playtest, with the prototype discovery log running) → decompose →
> author.
>
> **Per-unit-plan superseded (2026-06-12).** The desk-mapped `per-unit-plan.md` this draft promised
> is not written and won't be: under endpoint-first, the prototype's commit history and discovery
> log drive the decomposition, and the fate of the 16 shipped CPU-drawn units is decided *at
> decomposition, with evidence* — not mapped speculatively first. The shipped units stay live and
> untouched until then.

> **(Superseded banner, kept for lineage)** *PARKED 2026-06-11 — theme and name on hold.* The
> mechanic design stood; the "Flock" name and sheep theme had moved to the rung-1 crosser, leaving
> theme/name undecided. Resolved above.

---

## Section 1: Pedagogical Role

Teach the Amiga **Blitter** — block copy and masked (cookie-cut) blits — as the chip that both *draws* the game and *is* the player's verb, so the reader leaves able to move and reshape graphics with the Amiga's defining co-processor instead of the CPU.

This is the foundation every later Amiga assembly game builds on: once you can copy and cookie-cut through the Blitter, hardware sprites (Signal), Copper splits and Paula samples (Shatter Point), and scrolling worlds (later) each add *one* thing on top of a Blitter you already own.

---

## Section 2: Classic Ancestors

- **Lemmings** (DMA Design, 1991) — the canonical "a flock of witless autonomous creatures walks into danger; save them by reshaping their route." The Amiga flagship of the genre.
- **Populous** (Bullfrog, 1989) — the no-avatar god-hand: you never *are* a character, you act on the *world* and the people respond. Also Amiga-born.
- **Frogger** (Konami / Sega, 1981) — the deterministic road-crossing beat that the late-game traffic hazard borrows.

(The original Exodus reached for *The Lost Vikings*; that direct-control, distinct-cast design was set aside — see Section 3 — and is parked for a possible sequel.)

---

## Section 3: Remix Unit

*Same tropes, new core mechanic.* Lemmings' tropes are preserved — a vulnerable autonomous flock, lethal terrain, "get them all to the exit" — but the mechanic is new in two ways: the player's **only** verbs are **two Blitter operations on the terrain** (cookie-cut to carve it away, copy to raise it up), and they are committed in a **plan-then-release** freeze, not Lemmings' real-time scramble. You shape the land, then let the flock loose and watch your plan succeed or fail. The Blitter isn't decoration on the puzzle; the Blitter *is* the puzzle's verb.

---

## Section 4: Core Experience

A slow, held-breath puzzle: read the field, spend your rationed carves and raises to shape a safe route from the flock to the gate, then release the sheep and watch them amble — relieved when the last one trots home, sick when one ambles off a cliff you forgot to fence. The texture is *plan and reveal*, not twitch; the tension is loss-aversion ("don't lose one"), not reflex.

---

## Section 5: Constraint Position

**Period-faithful.** Blitter copy and masked cookie-cut blits are the Amiga's everyday bread and butter — used in every commercial game of the era; *Lemmings* and *Populous* are period-faithful proof. Position is consistent across both arcs.

- **In active use:** the **Blitter** (channel copy + masked/cookie-cut blits via `BLTCON0/1`, `BLTxPT`, `BLTSIZE`, `BLTxMOD`, masking and minterms); **bitplanes** (the playfield the Blitter operates on); the **Copper** (the sky gradient and playfield setup); **Paula** SFX — tones, not samples.
- **Deliberately avoided** (each reserved for its own rung): **hardware sprites** — the flock and any vehicles are drawn as *blits*, not sprites (sprites are Signal's new rung); **scrolling** — levels are single-screen (scrolling is a later game); **sampled Paula instruments** — audio stays light (sampling is Shatter Point's rung); **AGA** — this is OCS/A500 period hardware.

---

## Section 6: Visual Direction

- **Palette strategy.** OCS bitplanes, a small, confident pastoral palette: a Copper-gradient sky (already built), field green, water blue, earth/cliff brown, sheep white, road grey. Few colours, used cleanly — charm over spectacle.
- **The Blitter is the look.** Terrain is a bitplane the Blitter carves and rebuilds; the flock is a handful of small **masked-blit** sheep (16×16, a gentle 2-frame amble). Cookie-cut masking is what stops the sheep being white rectangles — so the headline technique is visible in every frame.
- **Per-screen richness.** One screen should read instantly as a *place*: a green field, a winding river or a cliff edge, a gate standing open, and your little flock clustered at the start. When you carve a ramp or drop a stone bridge, the change is plainly *yours*.
- **Visual identity.** Cosy, legible, hand-tended countryside — not epic, not gritty. The player should smile at the sheep.
- **Magazine-screenshot test.** A green field under a soft Copper sky: five white sheep ambling toward an open gate, crossing a freshly-raised stone bridge over a blue stream while a just-carved ramp leads down a brown cliff. Readable at a glance, unmistakably a game.

---

## Section 7: Audio Direction

- **Title.** A short, gentle pastoral jingle — Paula tones, not sampled instruments (sampling is reserved for Shatter Point).
- **In-game.** Silence-led, by design: the field is quiet, which makes the SFX land. (A period-valid choice — many puzzle games shipped quiet.)
- **SFX scope.** A soft "baa" as the flock moves; a satisfying *thunk* when a Blitter edit lands (carve / raise); a small splash or tumble when a sheep is lost (the sad beat); a contented bleat-and-gate-clunk when the last sheep is home.
- **Integration.** A couple of Paula channels, no mixing complexity — light enough that it never becomes the lesson.

---

## Section 8: Level Design Direction

- **Scale.** Single-screen, self-contained levels; a finished game of roughly five to seven. No scrolling — the whole puzzle is visible, which is exactly what plan-then-release needs.
- **Pacing (the verb ramp).** Carve alone → raise alone → both together → both under a tighter budget → the road (a *dynamic* hazard, solvable by geometry **or** timing) → optionally a territorial hazard (area-denial). Each level teaches one new idea, then combines.
- **Signposting.** Entirely visual: the flock is where they start, the open gate is where they go, hazards *are* the terrain (water you can see, a cliff edge, a road with traffic). The carve/raise budget shows as a row of icons.
- **Difficulty curve.** Level one is a near-gift — one carve opens a ramp to the gate — teaching the contract (shape the land, release, they flow). Difficulty comes from tighter budgets and hazards that interact, never from twitch.
- **Onboarding.** The first release is the teacher: the player shapes one edit, lets the flock go, and *sees* cause and effect. The held-breath reveal is the tutorial.

---

## Section 9: Polish Direction

- **Title screen.** "FLOCK", a sheep or two, the soft sky. Tone-setting: cosy and inviting.
- **Attract mode.** Optional/deferred; if present, a hands-off level solving itself.
- **Options.** Minimal — SFX on/off. Controls are point-and-act: **mouse primary (decided
  2026-06-12)** — period-true for the genre (Lemmings is the Amiga mouse game), and the rung's
  second new lesson: quadrature counters in `JOY0DAT`, the left button on CIA PRA, and the
  pointer as **hardware sprite 0** (Flock's technique re-cast as the cursor). Left button
  carves/raises; a key or right button toggles verb. Joystick-pointer support is a "Try this",
  not shipped scope.
- **Ending.** Per level: gate clunks shut, sheep saved tally, instant retry on loss. Game end: a short "all flocks safe" beat — warm, brief, no epic.
- **Loss feel.** A lost sheep is a small, legible, slightly comic-tragic moment — never punishing UI, just a quiet "oh no". Instant retry keeps it light.
- **Shippable criteria.** Plays cleanly start to finish, no soft-locks; the carve/raise feel is crisp; the reveal reads. Would sit happily beside contemporary cosy indie puzzlers.

---

## Section 10: Anti-goals

- **No direct control of the sheep.** You are the hand above, never an on-screen avatar. The whole design dies if the player steers a sheep.
- **No hardware sprites.** All moving graphics — sheep, vehicles — are Blitter blits. Sprites are Signal's rung.
- **No scrolling.** Single-screen levels. Scrolling is a later game.
- **No sampled Paula music.** Light tone-and-SFX audio only; sampling is Shatter Point's rung.
- **No hunting/roaming predator AI.** If a predator appears, it is *territorial* (fixed den, trigger radius, deterministic) — area-denial, not pursuit. A wolf that hunts in earnest wants real-time play and pathfinding: sequel scope.
- **No random hazards.** Road traffic (and any territorial threat) is deterministic and visible during planning — plan-then-release cannot survive dice.
- **No real-time intervention after release.** You commit your plan, then watch. (Held loosely — reconsider only if play feel demands it.)
- **No open world / simulation.** The living, tended world is the sequel (see below).

---

## Section 11: Build Trajectory

Two build arcs, indicative unit counts (per [curriculum-structure.md](../../../../decisions/curriculum-structure.md) — counts firm up at build time; the cap is one new technique per unit, not a unit total). Each arc ends in a complete, playable game at the commercial bar.

**Arc 1 — The hand that carves.**
*New:* the Blitter as renderer (bitplane playfield, Copper sky), the flock as masked cookie-cut blits, autonomous walker behaviour (walk / turn / fall / terrain-collide — salvaged from the existing build), the **carve** verb (cookie-cut terrain away), the plan-then-release loop, the gate/win, the carve budget.
*Revisits:* —
*Deliverable:* a one-verb game — carve ramps and breaches to route the flock down cliffs and through banks to the gate, across a small set of carve-only levels. Already a real, finishable game.

**Arc 2 — The hand that builds.**
*New:* the **raise** verb (Blitter copy terrain in — stepping-stones, plank bridges, steps, fences), the river hazard, the road (deterministic traffic, drawn as blits; solvable by bridging/tunnelling **or** by timing the release), an optional territorial hazard, title screen + light Paula SFX, the saved/lost tally.
*Revisits:* carve (now combined with raise in the same level), the budget (now two resources), plan-then-release (now planning around a dynamic hazard).
*Deliverable:* the full Flock — carve *and* raise under budget across fields, rivers, cliffs and a road, every sheep home; a complete cosy puzzle game.

*(Per-unit mapping is **superseded** — see the 2026-06-12 banner: decomposition follows the
prototype under endpoint-first; no speculative `per-unit-plan.md` is written.)*

---

## Section 12: Ship Test (Multi-axis)

Per arc, all five axes must pass (verification is emulator-based — real-hardware verification is currently suspended per [commercial-bar-revamp.md](../../../../decisions/commercial-bar-revamp.md)).

**Arc 1**
- **Code:** all units assemble (vasm); the carve verb is a correct masked cookie-cut blit; plan-then-release runs without lock-ups; passes the Definition of Done.
- **Visuals:** sheep render as clean masked blits (no rectangle fringing); carve visibly reshapes the bitplane; magazine-screenshot test met for a carve-only field.
- **Audio:** carve *thunk*, move *baa*, lost-sheep beat present.
- **Level design:** the carve-only levels are solvable, the budget bites, level one onboards in one edit.
- **Polish:** gate/win, instant retry, no soft-locks.

**Arc 2**
- **Code:** raise verb is a correct Blitter copy; road traffic is deterministic and frame-stable; both verbs share one budget correctly.
- **Visuals:** raised terrain tiles seamlessly; the road reads; title screen done.
- **Audio:** raise *thunk*, title jingle, home bleat-and-clunk.
- **Level design:** carve+raise levels solvable under budget; the road level offers a genuine geometry-or-timing choice; difficulty crests at a pace the player can read.
- **Polish:** saved/lost tally, end beat, SFX toggle; the whole game plays start-to-finish.

---

## Section 13: Pattern Library Extractions

- **rendering** — Blitter block copy (channel setup, `BLTSIZE`, modulos). The Amiga's foundational graphic move. Amiga-specific.
- **rendering** — masked (cookie-cut) blit: drawing a non-rectangular sprite over a background via a mask channel and minterms. *The* Amiga moving-graphic technique. Amiga-specific in implementation; the principle (mask-then-composite) generalises.
- **framework** — plan-then-release state machine (edit phase ↔ simulation phase, with commit and reset). Cross-platform.
- **physics** — autonomous walker (walk / turn-at-wall / fall-with-gravity / terrain-collision against a bitplane). Cross-platform.
- **framework** — rationed-action budget (a small pool of player edits as the puzzle constraint). Cross-platform.
- **ai** (optional) — territorial proximity hazard (fixed position, trigger radius, deterministic lunge). Cross-platform.

---

## Section 14: Vault Tie-ins

- *Lemmings* (DMA Design, 1991) — direct ancestor *(vault entry needed)*.
- *Populous* (Bullfrog, 1989) — the god-hand ancestor *(vault entry needed)*.
- *Frogger* (Konami / Sega, 1981) — the road-crossing beat *(vault entry needed)*.
- DMA Design — studio entry *(needed)*.
- Bullfrog — studio entry *(needed)*.
- Amiga Blitter hardware reference — the copy/cookie-cut registers and minterms (hardware page).
- Amiga Copper reference — sky gradient / playfield setup (hardware page).
- Paula reference — light, for the SFX layer (hardware page).

---

## Optional: Risks

1. **Plan-then-release might play flat.** The reveal could feel passive where it should feel tense. *Mitigation:* prototype the release-and-reveal on one carve-only level first; if it's dull, try slow-real-time or pause-to-act before committing the arc. (Flagged as a held-loosely decision with the user.)
2. **"Is it a game?" — agency.** This is the exact test the un-briefed Exodus failed. *Mitigation:* the two verbs + finite budget + all-survive *are* the agency; pressure-test this brief against that question before authoring.
3. **Re-scope reconciliation.** The existing 16 units are CPU-drawn with no Blitter and no player verb. *Mitigation:* salvage the walker AI and rendering structure where the prototype's route matches; the call is made at decomposition with the working game in hand (endpoint-first), not desk-mapped first.
4. **Determinism for dynamic hazards.** Roads (and any territorial threat) must be deterministic and visible at plan time, or plan-then-release breaks. *Mitigation:* fixed, looping, on-screen-during-planning traffic; no RNG in hazards.
5. **Scope creep.** Roads and predators are seductive. *Mitigation:* the road is the one dynamic hazard; predators, if any, are territorial-only; the hunter, the open world, and the epic "lead a people" tone are all explicitly the sequel's — *Exodus* lives again as the big game later.
