# Decision: Commercial bar

> **Amended 2026-09-05:** [Game quality is relative to the agreed scope](scope-relative-game-quality.md) supersedes the universal commercial bar below. Games must be complete and deliberately finished for their scope; BASIC games need not meet a commercial standard. Applicable progression and verification requirements remain.

## The decision

Every game is built to a **commercially shippable in the era of the system** bar. A learner finishing a game should have built something that could plausibly have shipped on a budget label between 1986 and 1991. Per-game scope is per-brief; there is no universal unit floor.

## Why

Earlier games were technically clean and were small-screen demos rather than complete games: a single-screen platformer with one obstacle, a single-enemy-type vertical shooter, infrastructure with the actual game deferred to a later phase.

Setting the bar at commercial forces every game to be a real game rather than a tech demo with a title screen. It is a commercial bar, not a pedagogical minimum.

## The bar per system

| System | Era bar | Reference points |
|---|---|---|
| NES (1985–90) | Multi-screen scrolling, mapper-driven world, music | Castlevania, Mega Man, Blaster Master |
| C64 (1984–89) | Hubbard-grade SID, fast scrolling, sprite work | Sanxion, Wizball, Uridium, Last Ninja |
| Amiga (1987–91) | Visual showpiece, sampled audio, polish | Lemmings, Speedball II, Shadow of the Beast |
| Spectrum (1984–89) | Bedroom-coder ingenuity, attribute-clash discipline | Knight Lore, Atic Atac, Sabre Wulf |

The endpoint of the curriculum is **mid-tier full-price** — the £7.95 Hewson / Gremlin / Mikro-Gen / Durell tier. Real commercial product, ambitious, not pretending to be Ultimate's absolute top. See [real-retro-games.md](real-retro-games.md) for the multi-disciplinary form of the same bar, and [game-completeness-bar.md](game-completeness-bar.md) for how a game is tested against it.

Per-track lineups are owned by the per-track records under `decisions/`, not by this one.

## Scaffold pattern

Two patterns, chosen per game and recorded in the game's brief.

**Lucky Number scaffold** — a typed-in first unit contains working systems the learner experiences without understanding: a music driver, a scroll engine. The boxes open at scheduled later units.

**Incremental from nothing** — incremental scaffold within phases, spiral progression across them, starting from an empty file. See [spiral-and-incremental.md](spiral-and-incremental.md).

## Definition of Done (per unit)

The bar is operational at unit scale through this checklist. A unit is not shippable until all eight tick:

- [ ] MDX written, in the magazine voice, at a length appropriate to the unit's teaching beat
- [ ] Code listing assembles cleanly with the system's tools
- [ ] Code listing runs correctly on the system's emulator — Fuse for Spectrum, and so on
- [ ] At least one screenshot captured
- [ ] All `<CodeFromFile>` snippets exist in code-samples and assemble
- [ ] "Try this" experiments tested, and they produce the described result
- [ ] "If it doesn't work" troubleshooting reflects failure modes encountered in testing
- [ ] All cross-references resolve to real content — vault entries, pattern-library entries and other units must exist, or be catalogued as required

**Real hardware is not a shipping gate.** Available hardware is limited to a C64 with an Ultimate-II+ and a Spectrum Next, so a hardware gate would block `complete` on two of the four systems outright and apply unevenly across the others. Cycle-accurate emulation is the standing guarantee that the binary is real: the code targets real machines and assembles to a real-hardware image. Where a brief's ship test lists a real-hardware step, it does not gate. Revisit when hardware and capacity allow.

## Definition of Done (per game) — the winnability gate

Mechanics verify at unit scale; games only verify end to end. Before the module that makes a game winnable is marked `complete` — and again after any change to its mechanics, level data or tuning:

- [ ] **The game has been driven to its win state by a scripted emulator run.** Real inputs through the real game logic. Engineered setups are fine — poke a counter, park a hazard — but bypassing the logic is not. The script lives in the game's `capture/` directory so the run is repeatable and diffable.
- [ ] **The loss path has been exercised the same way**, where the game can be lost. Both endings seen and heard, not just the happy one.

For multi-arc games this applies per arc: each arc ships a winnable game.

What this catches that unit-scale checks structurally cannot: untraversable geometry, win conditions that never fire, resets that leak state between attempts, death cascades, and ending flows that snap past before they land.

The scripted run is the floor, not the ceiling. It proves the game *finishes*; only hands on a real pad prove it *feels* right, and human playtest stays a separate per-game follow-up.

## Drift triggers

- A game spec that looks like a single-screen demo, or infrastructure-only with the real game in the next phase.
- *"The mechanics are all individually verified, the game is obviously completable."* Dash's were, and it was not: the right half of its level had never been reached, because a spike gap was one pixel wider than its jump. Run the script.
- *"The win run is too hard to choreograph."* That is information about the game, not about the gate. If a deterministic script cannot reach the win, look hard at whether a player can.

## Status

Active. The bar and both Definitions of Done are live for every game.
