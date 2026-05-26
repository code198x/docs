# Brief Template — Spectrum BASIC

**Version:** 1.0
**Last Updated:** 2026-05-26
**Purpose:** Brief format for all Spectrum BASIC games (Volumes 1–4). Derived from the full brief spec (`brief.md`) by dropping sections that don't apply to single-phase BASIC games. Supersedes `brief-basic-v1.md`, which was the V1-only prototype of this template.

---

## Header

```markdown
# {Game Name} — Brief

**Title (working):** {confirmed or working title}
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume {V}, Game {N} of 32 (slot {S})
**Headline concept:** {player-facing name} — {one-line description}
**Embedded concept:** {name} — {one-line description}
**Topics:** {count, e.g. "9 topics, ~10–15 hours"}
**Constraint position:** period-faithful
**Status:** {draft | active}
```

All BASIC games are **period-faithful** — only techniques present in 1982–93 magazine type-ins, Usborne listings, and BASIC commercial product.

---

## Section 1: Pedagogical Role

**One sentence.** What the learner can do after this game that they couldn't before — and what later games depend on.

---

## Section 2: Classic Ancestors

**1–3 named real-era games or traditions.** Name the specific ancestor, not "games like this." For V1 games these are magazine type-ins and toy ports. For V2–V4 games these may be commercial products or well-known game designs.

---

## Section 3: Core Experience

**One or two sentences.** What playing this game feels like. For short-session games (V1–V2), describable in one breath. For longer games (V3–V4), describe the texture of engagement across a session.

---

## Section 4: Visual Direction

**Bullets.**

- What the screen looks like during play
- How colour carries gameplay information (not decoration)
- V1–V2: text-mode with colour (PRINT AT, INK, PAPER, BRIGHT). No sprites or UDGs.
- V3–V4: UDGs, custom character sets, and PLOT/DRAW graphics enter the vocabulary.
- Magazine-screenshot test: describe one screenshot that would work in a period magazine

---

## Section 5: Audio Direction

**Bullets.** BEEP only — single-channel, short tones. No multi-voice compositions (those belong in the Assembly track).

- What events get sound
- How sound carries meaning (directional, proximity, success/failure)
- What's deliberately silent

---

## Section 6: Level Design Direction

**Optional for V1. Required from V2.**

**Bullets + short paragraph.** How content shapes difficulty and progression within the game.

Topics to cover (omit any that don't apply):

- **Content source** — where the game's data comes from. DATA/READ word lists (Cipher), hand-written questions (Quiz Master), designed puzzle layouts (Crates), procedural generation (Dungeons of Dorin).
- **Difficulty curve** — how the game gets harder. Word length increases (Cipher), categories get obscure (Quiz Master), grid density increases (Sonar), AI improves (Three in a Row).
- **Scale** — how much content the game has. Number of words, questions, levels, or rounds.
- **Pacing** — how long a session lasts and where the peaks are.
- **Onboarding** — what the first round teaches the player about the game's contract.

V1 games skip this section — they have no levels, no content progression, and no designed difficulty curves (difficulty is either inherent in the mechanic or absent).

---

## Section 7: Anti-goals

**Bullets.** What this game will not do. The scope wall — prevents a 10-topic game from trying to be a 30-topic game.

---

## Section 8: Topic Progression

**Numbered list.** The operational backbone. Each entry names:

- **Topic title** — what the learner does
- **New BASIC concept(s)** — one or two per topic, maximum
- **What the program does at this point** — the working result
- **Approximate program size** — lines of BASIC
- **Polish beat** — the small "how does this feel?" moment woven in

Every topic produces a working, runnable program. The progression must read as a gradual build from the smallest possible program to the finished game, with one new concept per topic.

The Lucky Number topic list in `basic.md` is the canonical exemplar for V1. V2–V4 games follow the same gradual shape but at larger scale.

---

## Section 9: Ship Test

**Checklist.** What has to be true for this game to ship.

- [ ] Every topic's code runs on a 48K Spectrum (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] One new BASIC concept per topic — no topic introduces two major ideas
- [ ] Gradual progression — a reader can follow from topic 1 to final topic without gaps
- [ ] British English throughout (exception: "program")
- [ ] Screenshots show the actual running program, not mockups
- [ ] Code samples in `/code-samples/`, not inline
- [ ] Magazine voice — warm, technical, never condescending

V2+ games add:

- [ ] DATA/READ content is correct and complete (no missing entries, no off-by-one)
- [ ] Array dimensions match the data they hold
- [ ] Level/round progression is playable end-to-end

---

## Section 10: Pattern Library Extractions

**Bullets.** What reusable techniques this game surfaces for promotion to the Pattern Library.

---

## Section 11: Vault Tie-ins

**Bullets.** Which vault entries this game's curriculum references — ancestors, hardware, people.

---

## Sections Not Used

The following full-brief sections are dropped for all BASIC games:

- **Remix Unit** (§3 in full spec) — BASIC games are direct canon or canonical genre representatives, not remixes.
- **Constraint Position detail** (§5 in full spec) — all BASIC games are period-faithful; no per-phase variation.
- **Polish Direction** (§9 in full spec) — polish is woven into the topic progression (§8 above), not a separate concern.
- **Phase Trajectory** (§11 in full spec) — BASIC games are single-phase.
- **Risks** (optional in full spec) — BASIC games are small enough that risk management is "write it and see." V4 games that push scope boundaries may add a Risks section as needed.

---

## Anchored In

- [`specifications/brief.md`](brief.md) — full brief spec (assembly games)
- [`specifications/brief-basic-v1.md`](brief-basic-v1.md) — the V1 prototype this template supersedes
- [`decisions/spectrum-basic-32-games.md`](../decisions/spectrum-basic-32-games.md) — the 32-game lineup
- [`platforms/sinclair-zx-spectrum/basic.md`](../platforms/sinclair-zx-spectrum/basic.md) — curriculum spec with per-game details
