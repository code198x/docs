# Brief Specification

**Version:** 1.0
**Last Updated:** 2026-05-13
**Purpose:** Format specification for game design briefs. A brief is the strategic design document for a single game in the Code198x curriculum — what it is, what it teaches, what each phase ships, and what it costs to authors and learners.

---

## Overview

A brief is **the source of truth for a game's design intent**. It is written before unit MDX or code-samples work begins and is referenced throughout authoring. The brief is reviewable as a standalone artefact; a reader who has never seen the game should leave the brief able to predict what every phase ships and how each unit fits.

A brief is **not** an implementation document. Per-phase or per-unit detail lives elsewhere (the existing `knowledge/curriculum/shadowkeep-phase-1-design.md` is the pattern: a sibling design doc that follows from the brief). The brief is strategic; design docs are operational.

**Key principles:**

- **Multi-disciplinary from the brief downward.** Per [`real-retro-games`](../decisions/real-retro-games.md), the brief carries first-class fields for visuals, audio, level design, and polish alongside code-led concerns. A brief that names code targets but leaves visual/audio/level/polish sketchy is not a complete brief.
- **Per-phase commitments.** Per [`phase-boundaries`](../decisions/phase-boundaries.md), each phase declares both what's new (incremental) and what revisits earlier work (spiral, per [`spiral-and-incremental`](../decisions/spiral-and-incremental.md)). Each phase end ships a complete game at the relevant commercial bar.
- **Constraint position explicit.** Per [`constraint-position`](../decisions/constraint-position.md), each brief declares which 1980s the game inhabits — period-faithful, period-possible, or modern scene.
- **British English throughout** (exception: "program" for computer programs, per [`british-english`](../decisions/british-english.md)).
- **Magazine voice.** Warm, technical, opinionated, never condescending. See `docs/specifications/writing-voice.md`.

---

## File Location

```
docs/platforms/{system}/games/{game-slug}/brief.md
docs/platforms/{system}/games/{game-slug}/brief.md
```

One brief per game. The brief is a versioned spec document, sitting alongside the platform-level curriculum doc.

---

## Header

Every brief opens with the same six-field header, in this order:

```markdown
# {Game Name} — Brief

**Title (working):** {confirmed or working title}
**System / Track:** {platform name} / {assembly | BASIC}
**Position:** Game {N} of {4 for assembly tracks; up to 16 for BASIC tracks}
**Target unit count:** {256 for assembly Game 1–4; varies for BASIC per `revamp.md`}
**Constraint position:** {period-faithful | period-possible | modern scene} — see Section 5
**Status:** {draft | active | superseded}
```

---

## Section 1: Pedagogical Role

**One sentence.** The game's job in the curriculum. What must a reader be able to do after finishing this game that they couldn't before?

A pedagogical role is *what subsequent games depend on*. Game 1 establishes foundational skills that Games 2, 3, and 4 build on; the brief names that foundation explicitly.

**Example (Shadowkeep):**
> Teach the ZX Spectrum's attribute system as the entirety of game logic — every gameplay rule is a bit-test on a single attribute byte — so the reader leaves with the platform's defining hardware feature as a working tool.

**Common failure:** Listing every skill the game touches. The pedagogical role is the *one* compounding skill the next game depends on. Itemise everything in Section 13 (Pattern Library extractions); summarise the load-bearing skill here.

---

## Section 2: Classic Ancestors

**2–3 named real era games.** Concrete commercial references, not "platformers in general."

The ancestors situate the brief. A reader who knows the references should be able to predict the game's shape from the names alone.

For modern-era games where the ancestors are obscure, link to vault entries.

**Example (Shadowkeep):**
> *Atic Atac* (Ultimate, 1983) and *Sabre Wulf* (Ultimate, 1984). Both are top-down, multi-room, find-the-thing-and-escape adventures from the 1984 Ultimate bar.

**Common failure:** Listing inspirations the actual game doesn't resemble. If the brief names *R-Type* as an ancestor, the gameplay must read as *R-Type*-shaped to a reader who knows *R-Type*. Don't reach for prestige references that don't fit.

---

## Section 3: Remix Unit

**One phrase + one sentence.** Which transformation does this game perform on its ancestors?

Four categories:

- **Same verb, new container** — the gameplay verb is the ancestor's, but the setting/world differs (*Boulder Dash*'s "dig and run from physics" relocated to a new context).
- **Same tropes, new core mechanic** — the genre tropes are preserved (e.g., platformer with collectibles), but the mechanical foundation is novel (e.g., grappling-hook movement replaces jumping).
- **Same aesthetic constraint, alien genre** — the look and sound feel 1985, but the gameplay is alien to the era.
- **Same feel, different era's vocabulary** — period-tight controls combined with modern structural ideas (roguelite runs, metroidvania gating).

Pick one category; then state the specific move in a sentence.

**Example (Shadowkeep):**
> *Same tropes, new core mechanic.* The Atic Atac top-down keep-exploration tropes are preserved (hooded figure, multi-room layout, find-and-escape, environmental hazards) — but the mechanic is "every game rule is a bit-test on the screen attribute byte." No sprites for hazards, no separate collision tables, no map editor. The screen *is* the map; the attribute byte *is* the rule.

**Common failure:** Picking no transformation at all (a clone) or several at once (no clear identity). If the remix unit doesn't fit cleanly into one of the four categories, the design isn't sharp enough yet.

---

## Section 4: Core Experience

**One or two sentences.** What playing this game feels like — both moment-to-moment and across a session.

For games with a tight gameplay loop (twitch reflex, repeated action), name the **core verb** — the every-second action.

For slower-paced games (exploration, puzzle, narrative), describe the **texture of engagement** — what the player is doing across longer arcs, not what they press every second.

**Example (twitch — hypothetical platformer):**
> Jump from platform to platform, timing each leap against the rhythm of moving hazards.

**Example (slow — Shadowkeep):**
> Walk the keep one cell at a time, reading the colour-coded rules off the screen before stepping forward.

**Common failure (twitch framing on slow games):** Forcing a single moment-to-moment verb when the game's interest is in spatial/exploratory engagement. If you can't write a clean "every second the player does X" sentence, you have a slow-paced game; describe the texture instead.

---

## Section 5: Constraint Position

Declares which era-period techniques the game uses, per [`constraint-position`](../decisions/constraint-position.md):

- **Period-faithful** — only techniques common in commercial era games.
- **Period-possible** — techniques that existed in the era but were rare in commercial product.
- **Modern scene** — techniques the hardware allowed but that were codified later (typically the 2010s onwards).

If the position varies by phase, declare here that it varies and defer per-phase detail to Section 11.

After the position declaration, list:

- **Hardware features in active use** — what this game uses on the platform.
- **Hardware features deliberately avoided** — what the game doesn't use, and what game/phase the avoided features are reserved for.

**Example (Shadowkeep):**
> **Period-faithful.** Phase 1 (vertical slice) uses only techniques common in commercial 1984–87 Spectrum product. Position is consistent across all phases of the existing 16-unit Arc 1 spine; period-possible and modern-scene techniques are reserved for later arcs.
>
> **In active use:** attribute memory ($5800–$5AFF), bitmap memory ($4000–$57FF) for the hero sprite, port `$FE` (keyboard + beeper), IRQ-driven update loop.
> **Deliberately avoided:** 128K bank switching (Phase 7 territory), AY-3-8912 (Phase 7), software pixel scrolling (Game 2 territory), contended-memory mastery (Game 2).

**Common failure:** Declaring period-faithful but using modern-scene techniques in a unit without realising it. Cross-check against the platform reference page in `docs/platforms/` if uncertain.

---

## Section 6: Visual Direction

**Bullets + one or two paragraphs.** First-class per [`real-retro-games`](../decisions/real-retro-games.md). The brief names visual ambition explicitly; the design doc (if any) goes deeper.

Topics to cover (omit any that don't apply):

- **Palette strategy** — how the colour budget is allocated. For Spectrum, the attribute table. For C64, sprite multiplexing and FLI/IFLI choices. For NES, the per-tile palette assignments. For Amiga, the bitplane budget.
- **Sprite ambition** — frame count, animation budget, dimensional choices (8×8 / 16×16 / multi-character).
- **Per-room or per-screen visual richness target** — what a single screen of this game should *feel like* visually.
- **Visual identity** — what makes this game look like *this game* and not a generic example.
- **Magazine-screenshot test** — describe a screenshot from the game that would be magazine-worthy in the era. If you can't, the visual direction isn't ambitious enough.

**Common failure:** Treating visual direction as decoration applied after code. The visual ambition shapes what the code must do; it's primary, not secondary.

---

## Section 7: Audio Direction

**Bullets + one or two paragraphs.** First-class per `real-retro-games`.

Topics:

- **Title music** — composition style, length, key, reference tracks.
- **In-game music** — present or deliberately absent (some era games shipped silent in-game; that's a valid choice if declared).
- **SFX scope** — what events get sound, what doesn't.
- **Sound integration** — how music and SFX coexist (interleaving on a single channel, voice sharing on AY/SID, etc.).
- **Per-phase if the audio grows** — Phase 1 might ship title-only beeper; Phase 7 might add AY in-game music.

A separate composition spec document may live in `docs/platforms/{system}/games/{game}/{audio}-spec.md` (precedent: `shadowkeep-beeper-spec.md`).

**Common failure:** "Beeper title theme" as the entire audio section. That's the answer to "what music?", not the answer to "what's the audio direction?". Describe the *intent* and *texture*.

---

## Section 8: Level Design Direction

**Bullets + one or two paragraphs.** First-class per `real-retro-games`.

Topics:

- **Scale** — room/screen/level count at full game endpoint, and at each phase boundary if it grows.
- **Pacing** — early game eases the player in; mid game tests them; late game pushes them. Name the curve.
- **Signposting** — how the game communicates rules, goals, and progress without prose.
- **Difficulty curve** — onboarding strategy (early forgiveness) vs peak difficulty (1980s-bar, see `docs/decisions/real-retro-games.md` and the difficulty discussion in `docs/log.md`).
- **Onboarding** — what the first five minutes teach the player about the game's contract.

**Common failure:** Stating scale without naming the pacing strategy. "50 rooms" tells you size, not whether the player is bored at room 20 or losing because room 49 spiked unfairly.

---

## Section 9: Polish Direction

**Bullets + one or two paragraphs.** First-class per `real-retro-games`.

Topics:

- **Title screen** — visual ambition, music, what it teaches the player about the game's tone.
- **Attract mode** — present or absent; if present, what it shows.
- **Options** — what the player can configure (controls, difficulty, sound on/off).
- **Ending** — what happens when the player wins; what happens when the player loses.
- **Accessibility** — control remapping, colour-blind considerations, frame-rate considerations.
- **"Shippable" criteria** — what would have to be true for this game to ship on Itch.io alongside contemporary indie work (per the aspirational Itch.io bar discussed in `docs/log.md`).

**Common failure:** Deferring all polish concerns to "the final phase." Polish work compounds; per `phase-boundaries`, every phase ends at a shippable artefact at its bar, which means each phase carries appropriate polish for its scope.

---

## Section 10: Anti-goals

**Bullets.** What the game explicitly will not do.

Anti-goals are the scope wall. They serve two purposes:

- **Defining what the game *isn't*** — sharpens what it *is*.
- **Preventing scope creep** — when a future session is tempted to add a feature, the anti-goals are the first place to check.

Examples of anti-goals worth declaring:

- Mechanics deliberately not included ("no character class choice", "no combat", "no weapons").
- Techniques reserved for other games or phases ("no software pixel scrolling — that's Game 2 territory").
- Genre conventions deliberately omitted ("no save/load in Phase 1 — Atic Atac had none").

**Common failure:** Treating anti-goals as a TODO list of things to add later. An anti-goal is permanent for the scope it covers ("never in this game" or "not until Phase N"). If it's "we'll add this later," that belongs in Section 11 (phase trajectory), not here.

---

## Section 11: Phase Trajectory

**Table + per-phase paragraphs.** The operational backbone of the brief.

Each phase declares:

- **Phase number and unit count** (power of 2, per `curriculum-structure.md`).
- **What's new** — incremental additions for the phase (per `spiral-and-incremental`).
- **What revisits earlier work** — the spiral declaration (per `spiral-and-incremental`).
- **Constraint position for the phase** — only if it differs from the game-level declaration in Section 5.
- **Phase-end deliverable** — the complete game that exists at phase end at the relevant commercial bar (per `phase-boundaries`).

**Example (Shadowkeep Phase 3):**
> *Phase 3: Animation and life (8 units).*
> *New:* 2-frame walking cycle, wandering shadow enemies (1–2 types), in-game beeper SFX layer.
> *Revisits:* Movement (now interleaved with animation timing), beeper driver (now handles SFX overlay), hero sprite (now multi-frame, with palette implications).
> *Constraint position:* period-faithful (unchanged).
> *Phase-end deliverable:* a 9-room Shadowkeep with animated hero and wandering enemies; *Sabre Wulf*-tier dynamic adventure at small scale.

**Common failures:**

- Naming techniques but not the resulting game. The deliverable is required.
- Naming only "what's new" without "what revisits." The spiral is required if the curriculum is spiral; pure-incremental phases are valid but rare and should be declared as such.
- Phase boundaries where the game is "almost playable" or "playable except for X." Reread `phase-boundaries`.

---

## Section 12: Ship Test (Multi-axis)

**Per-phase pass criteria across the five disciplines.**

The ship test is what a phase has to clear to count as shipped. It runs at phase ends, not unit ends (per `phase-boundaries`).

Five axes:

- **Code:** assembles cleanly, runs on emulator and real hardware, passes the Definition of Done (see `docs/tracker/revamp.md`).
- **Visuals:** meets the phase's visual ambition; magazine-screenshot test passed.
- **Audio:** music and SFX present per phase plan, mixed cleanly.
- **Level design:** playable end-to-end; difficulty curve appropriate; signposting clear.
- **Polish:** title/attract/options/ending appropriate to the phase's scope; no soft-locks, no crashes.

For each phase, the brief names the specific pass criteria across all five axes.

**Common failure:** A single-sentence "ship test" that says "it works on real hardware." That's the code axis only. The multi-axis test is what makes the multi-disciplinary commitment operational.

---

## Section 13: Pattern Library Extractions

**Bullets, grouped by technique category.** What reusable techniques this game surfaces for promotion to the Pattern Library, per [`pattern-library`](../decisions/pattern-library.md).

Categories (matching the existing library structure):

- **ai** — enemy behaviour, pathfinding, decision logic.
- **audio** — music drivers, SFX engines, voice management.
- **framework** — state machines, room engines, multi-mode runtimes.
- **input** — keyboard/joystick handling, key remapping.
- **physics** — collision, gravity, movement.
- **rendering** — sprite drawing, attribute writes, scrolling.
- **assembly** / **basic** — language-specific patterns where useful.

For cross-platform patterns (techniques that genuinely transcend the platform), note the cross-platform potential explicitly.

**Example (Shadowkeep):**
> - **framework** — incremental scaffold pattern (Unit 1 starts from nothing, each unit adds one mechanic). Cross-platform.
> - **framework** — multi-room engine (room pointer table, N/S/E/W connection tables, current-room state byte). Cross-platform.
> - **rendering** — attribute-byte read/write as a primary game-state mechanism. Spectrum-specific in implementation; the design principle (encode all cell state in one byte readable with one instruction) generalises.
> - **input** — port `$FE` half-row keyboard scanning with active-low bit tests.
> - **audio** — single-voice beeper melody driver (tick-counter timing, byte-pair pattern, port `$FE` bit 4 toggle).

**Common failure:** Listing every technique the game uses. The extraction list is *reusable* techniques specifically — work that earns its place in the Pattern Library because future games will want it. Game-specific mechanics don't belong here.

---

## Section 14: Vault Tie-ins

**Bullets.** Which vault entries this game's curriculum references — and which need to exist (or be expanded) for cross-references to resolve.

Per the Definition of Done in `docs/tracker/revamp.md`, every unit's cross-references must resolve. The Vault Tie-ins section names the entries this game depends on so that vault completeness work can prioritise.

Three categories of tie-in:

- **Direct ancestors** — the games named in Section 2.
- **Hardware references** — platform reference pages for the chips, ports, and memory the game uses.
- **People and studios** — developers, publishers, and notable individuals whose work this game references.

**Example (Shadowkeep):**
> - *Atic Atac* (Ultimate, 1983) — direct ancestor.
> - *Sabre Wulf* (Ultimate, 1984) — secondary ancestor.
> - Ultimate Play the Game — studio entry.
> - ZX Spectrum attribute system reference (hardware page).
> - ZX Spectrum beeper / port `$FE` reference (hardware page).
> - *Manic Miner* (Software Projects, 1983) — beeper-music precedent ("In the Hall of the Mountain King").

**Common failure:** Listing every game that vaguely inspired the design. Vault tie-ins are *operational* — they drive vault completeness work. If a tie-in won't appear in a curriculum unit's prose, it doesn't belong here.

---

## Optional: Risks

A brief may include a Risks section after Section 14 if the brief is for a game that's particularly novel, technically challenging, or scoped at the edge of what authoring can deliver. Not all briefs need this; the Shadowkeep design doc has one because the multi-room engine spike is a real design risk.

Format: numbered bullets, each with the risk and a mitigation thought.

If the brief skips this section, particularly novel risks can live in a sibling design doc (`docs/platforms/{system}/games/{game}/{phase}-design.md`) rather than the brief itself.

---

## Brief Quality Checklist

A brief is ready to anchor authoring when:

- [ ] All 14 required sections are present.
- [ ] Section 1 (pedagogical role) is one sentence and names the load-bearing skill, not a list.
- [ ] Section 2 (ancestors) names 2–3 specific games, with vault links if obscure.
- [ ] Section 3 (remix unit) fits cleanly into one of the four categories.
- [ ] Sections 6–9 are written with the same care as Sections 1–5 (multi-disciplinary commitment).
- [ ] Section 11 (phase trajectory) declares techniques + revisits + deliverable per phase.
- [ ] Section 12 (ship test) covers all five axes per phase.
- [ ] All cross-references in Section 14 resolve to real vault content (or are catalogued in `docs/tracker/lesson-references.md` as required).
- [ ] British English throughout (except "program").
- [ ] Magazine voice — `docs/specifications/writing-voice.md` standards apply.

---

## Anchored In

- [`decisions/real-retro-games`](../decisions/real-retro-games.md) — multi-disciplinary commitment that makes Sections 6–9 first-class.
- [`decisions/phase-boundaries`](../decisions/phase-boundaries.md) — phase-end commercial bar; gates Section 12.
- [`decisions/constraint-position`](../decisions/constraint-position.md) — three-tier taxonomy used in Section 5.
- [`decisions/spiral-and-incremental`](../decisions/spiral-and-incremental.md) — within/across phase progression; structures Section 11.
- [`decisions/curriculum-structure`](../decisions/curriculum-structure.md) — per-game scope (256 units assembly; per-`revamp.md` for BASIC).
- [`decisions/pattern-library`](../decisions/pattern-library.md) — what Section 13 feeds into.

---

## Changelog

- **v1.0 (2026-05-13):** Initial specification. Replaces the implicit 10-section format that existed in working memory and produced the Shadowkeep brief pressure-test. Adds Sections 6–9 (visual / audio / level / polish direction) as first-class fields, renames Section 4 from "Core verb" to "Core experience", restructures Sections 11 and 12 to reflect phase-boundary gating and spiral-progression declarations.
