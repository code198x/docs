# Brief Template — Spectrum BASIC Volume 1

**Version:** 1.0
**Last Updated:** 2026-05-25
**Purpose:** Lightweight brief format for Spectrum BASIC Volume 1 games. These are 3–9 topic programs at Usborne bar — direct canon ports, single phase, no multi-arc trajectory. The full brief spec (`brief.md`) applies to assembly games and larger BASIC games (V2–V4); this template captures only what a V1 game needs.

Derived from the full brief specification (`brief.md`) by dropping sections that don't apply to single-phase, small-scope, direct-canon BASIC games.

---

## Header

```markdown
# {Game Name} — Brief

**Title (working):** {confirmed or working title}
**System / Track:** Sinclair ZX Spectrum / BASIC
**Position:** Volume 1, Game {N} of 8
**Headline concept:** {player-facing name} — {one-line description}
**Embedded concept:** {name} — {one-line description}
**Topics:** {count, e.g. "9 topics, ~10–15 hours"}
**Constraint position:** period-faithful
**Status:** {draft | active}
```

All V1 games are **period-faithful** — only techniques present in 1982–85 magazine type-ins and Usborne listings.

---

## Section 1: Pedagogical Role

**One sentence.** What the learner can do after this game that they couldn't before — and what later games depend on.

---

## Section 2: Classic Ancestors

**1–2 named real-era games or traditions.** V1 games are direct canon: magazine type-ins, Usborne listings, toy ports with home-computer history. Name the specific ancestor, not "games like this."

---

## Section 3: Core Experience

**One or two sentences.** What playing this game feels like. V1 games are short-session — the experience should be describable in one breath.

---

## Section 4: Visual Direction

**Bullets.** V1 games are text-mode with colour. No sprites, no UDGs (those arrive in V3–V4). Visual ambition is about colour as communication — BORDER, INK, PAPER, BRIGHT carrying meaning.

- What the screen looks like during play
- How colour carries gameplay information (not decoration)
- Magazine-screenshot test: describe one screenshot that would work in a 1983 magazine listing page

---

## Section 5: Audio Direction

**Bullets.** V1 audio is BEEP only — single-channel, short tones. No music compositions, no multi-voice.

- What events get sound
- How sound carries meaning (directional, proximity, success/failure)
- What's deliberately silent

---

## Section 6: Anti-goals

**Bullets.** What this game will not do. V1 games are tiny — the anti-goals prevent a 9-topic game from trying to be a 32-topic game.

---

## Section 7: Topic Progression

**Numbered list.** The operational backbone. Each entry names:

- **Topic title** — what the learner does
- **New BASIC concept(s)** — one or two per topic, maximum
- **What the program does at this point** — the working result
- **Approximate program size** — lines of BASIC
- **Polish beat** — the small "how does this feel?" moment woven in

Every topic produces a working, runnable program. The progression must read as a gradual build from the smallest possible program to the finished game, with one new concept per topic.

The Lucky Number topic list in `basic.md` is the canonical exemplar for this section.

---

## Section 8: Ship Test

**Checklist.** What has to be true for this game to ship.

- [ ] Every topic's code compiles and runs on a 48K Spectrum (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] One new BASIC concept per topic — no topic introduces two major ideas
- [ ] Gradual progression — a reader can follow from topic 1 to final topic without gaps
- [ ] British English throughout (exception: "program")
- [ ] Screenshots show the actual running program, not mockups
- [ ] Code samples in `/code-samples/`, not inline
- [ ] Magazine voice — warm, technical, never condescending

---

## Section 9: Pattern Library Extractions

**Bullets.** What reusable techniques this game surfaces. V1 techniques are simple — distance-driven feedback, directional BEEP, INPUT loops — but they're the vocabulary later games build on.

---

## Section 10: Vault Tie-ins

**Bullets.** Which vault entries this game's curriculum references — ancestors, hardware, people.

---

## Sections Not Used

The following full-brief sections are dropped for V1 BASIC games:

- **Remix Unit** (§3 in full spec) — V1 games are direct canon, not remixes.
- **Constraint Position detail** (§5 in full spec) — all V1 games are period-faithful; no per-phase variation.
- **Level Design Direction** (§8 in full spec) — V1 games don't have levels.
- **Polish Direction** (§9 in full spec) — polish is woven into the topic progression (§7 above), not a separate concern.
- **Phase Trajectory** (§11 in full spec) — V1 games are single-phase.
- **Risks** (optional in full spec) — V1 games are small enough that risk management is "write it and see."

---

## Anchored In

- [`specifications/brief.md`](brief.md) — full brief spec (assembly and larger BASIC games)
- [`decisions/spectrum-basic-32-games.md`](../decisions/spectrum-basic-32-games.md) — the 32-game lineup
- [`platforms/sinclair-zx-spectrum/basic.md`](../platforms/sinclair-zx-spectrum/basic.md) — curriculum spec with per-game topic lists
