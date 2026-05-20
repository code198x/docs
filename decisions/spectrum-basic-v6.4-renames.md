# Decision: Spectrum BASIC v6.4 — Inspired-By Rename Pass

## The decision

Apply [inspired-by-not-clones-naming.md](inspired-by-not-clones-naming.md) retroactively to Spectrum BASIC v6.3. Eleven games currently using canonical / trademarked / generic-mechanic names get renamed to inspired-by working-draft replacements.

**Cut A applied** — rename all 11, not just active trademarks. Loses some computer-history specificity ("Wumpus" is *how* CS history names that mechanic) but gains cross-track consistency with [spectrum-assembly-track.md](spectrum-assembly-track.md).

## Why

Three reasons:

1. **Cross-track consistency.** Spectrum Assembly commits to inspired-by-not-clones for all 44 entries. BASIC inconsistency would create two different patterns across the same project.
2. **Legal cleanliness.** Active trademarks (Pong, Pac-Man, Asteroids, Frogger, Battleship, Mastermind, Magic 8-Ball) make literal use of those names legally fraught even at non-commercial scale.
3. **Pedagogical clarity.** When a curriculum unit says "build Pac-Man" the learner copies. When it says "build a maze-pursuit game in the Pac-Man tradition" the learner *designs*. The rename forces the second framing in every unit's prose.

## The 11 renames

| Slot | v6.3 name | v6.4 name | Why this name |
|------|-----------|-----------|---------------|
| 3 | Magic 8-Ball | **Oracle Stone** | Two words. Divination + object — captures mystical-answer feel without the trademark toy |
| 9 | Hangman | **Cipher** | Single noun. Puzzle-of-deduction; loses the gallows imagery |
| 11 | Mastermind | **Locksmith** | Single noun. Code-breaking metaphor — the player picks the lock |
| 12 | Battleship | **Sonar** | Single noun. The grid-search-by-coordinate captured in one evocative word |
| 13 | Tic-Tac-Toe | **Three in a Row** | Three words but rhythmic. Pure mechanic-name |
| 14 | Hunt the Wumpus | **The Caverns** | Two words. Atmosphere-led — the cave dwarfs the creature |
| 15 | Hammurabi | **Yearfall** | Single compound. Year-by-year resource decline |
| 18 | Pong | **Volley** | Single noun. The headline IS the name (already "Volley" in v6.3 dual-name) |
| 20 | Asteroids | **Drift** | Single noun. Inertia / momentum in one word |
| 21 | Frogger | **Quickstep** | Single compound. Timing under threat; light foot watching cars |
| 22 | Pac-Man | **The Hungry Maze** | Three words. Inverts pursuit — the maze is hungry, the player feeds it |

All marked **first-draft, needs-workshop**. Names may want refinement after living with them.

## What this means

### In the BASIC curriculum spec

The eight V1 games (October ship) become: Banner, Lucky Number, **Oracle Stone**, Reflex, Dice Roller, Bright Spark, Hi-Lo, Descent. Three of the eight V1 games are renamed from v6.3 (slot 3 Magic 8-Ball → Oracle Stone). Existing built games (Lucky Number, Bright Spark) keep their names — they already followed the convention.

The full 32-game lineup lives in [spectrum-basic-32-games.md](spectrum-basic-32-games.md); current-state summary in [[spectrum-basic]].

### In existing MDX content

Any in-progress unit MDX files referencing v6.3 canonical names need rename:
- Slot 3 Magic 8-Ball content (if any drafted) → Oracle Stone
- Slots 9-15, 18, 20-22 — none built yet (per [[spectrum-basic-games-progress]])

The [[spectrum-basic-games-progress]] memory entry needs update for v6.4 renames.

### In per-game design vocabulary

The v6.3 design concept progression (headline + industry term) carries forward unchanged:

- Slot 3: still "Chance (RND-selection)"
- Slot 22: still "Pursuit (Chase AI)"

Only the *game name* changes. The design concept teaching is unchanged.

### In vault references

Per-game vault threads (which reference canonical games as legends) carry forward unchanged. *Oracle Stone* still references the Mattel Magic 8-Ball toy as canonical antecedent in its vault thread. *The Hungry Maze* still references Pac-Man (Namco 1980) as canonical antecedent. The vault distinguishes "the curriculum game" from "the canonical reference" cleanly.

## Drift triggers

- **Per-unit prose using v6.3 names** in any in-progress or new BASIC unit content.
- **MDX files at v6.3 slot paths** with v6.3 names — these need rename if migration happens.
- **Marketing copy** describing the BASIC games using v6.3 canonical names ("learn to code Pong!" — should be "learn to code Volley!").
- **Vault entries** conflating the curriculum game with the canonical antecedent.

## Status

Active. Captured 2026-05-19. Descends from [inspired-by-not-clones-naming.md](inspired-by-not-clones-naming.md) (the parent convention). Companion to [[spectrum-assembly]] (same convention applied to Assembly).

Anchored in [[spectrum-basic]] (the current-state memory entry).

The existing [spectrum-basic-32-games.md](spectrum-basic-32-games.md) has been updated with the renamed lineup. The curriculum spec doc (`docs/platforms/sinclair-zx-spectrum/basic.md`) needs a v6.4 changelog entry — pending.
