# Decision: Inspired-By, Not Clones — Naming Convention

## The decision

Every game in the Code198x curriculum is *inspired by* canonical Spectrum / arcade / textbook games, not a clone of them. The named legends and games in lineup tables are *references for tradition*, not titles to recreate. Each curriculum game ships with its own name, characters, art, and design identity.

This convention applies across both tracks (Spectrum BASIC, Spectrum Assembly) and across all platforms (C64, NES, Amiga when their tracks design). Shadowkeep is the worked example — inspired by Atic Atac / Knight Lore / Sabre Wulf, but its own keep with its own hooded thief and its own atmosphere. Not a remake.

## Why

Three reasons:

1. **Shippability.** A "Pac-Man clone" isn't a shippable game. A pursuit-AI maze chase game with its own name is. The curriculum's commercial-bar spine requires every game to be a genuine shippable artefact, not a derivative.
2. **Pedagogical depth.** When the curriculum says "this is a Pac-Man clone," the learner builds Pac-Man. When it says "this is inspired by Namco's Chase AI tradition," the learner has to *design* a pursuit game — making real design choices, not following the trail of an existing product.
3. **Legal cleanliness.** Active trademarks (Pong, Pac-Man, Asteroids, Frogger, Battleship, Mastermind, etc.) make literal clones legally fraught even at non-commercial scale. Inspired-by naming sidesteps this entirely.

## The 10 principles

1. **Length: 1-3 words, prefer 1.** Single nouns and compound words carry better than phrases.
2. **Inspired-by, not clones.** Original — references canon but is its own.
3. **British-English flavour.** *Keep* not castle, *woodland* not forest, *lane* not road, *tarmac* not asphalt.
4. **Era-appropriate.** Sounds like it could have appeared in CRASH 1986. Avoid modern abbreviations, internet-speak, ironic register.
5. **Register matches game.** Atmosphere/adventure → evocative-fantasy; action → kinetic/action-led; simulation → setting-led/descriptive; puzzle/abstract → mechanic-led/experience-led.
6. **Compound words welcome.** Shadowkeep, Stonefall, Thornwood — two short words made one carry well.
7. **Mood + matter.** Best names carry both atmosphere AND a hint of mechanic (Shadowkeep = mood "shadow" + matter "keep").
8. **No trademark collision.** Brief check that no active product uses the name.
9. **Pronounceable on first read.** Avoid clever spellings.
10. **Specificity.** Names suggest the game's distinctness, not a generic placeholder.

Two-word phrasal names acceptable when compounds don't land (*Night Patrol*, *Tail Chase*, *Brick Bash* from BASIC v6.3 are precedents).

## What this means

### In briefs and curriculum docs

When naming a new game, follow the convention. Reference canonical games as *traditions* and *legends*, never as titles to copy. Use phrases like "in the [Legend Name] tradition," "inspired by [Canonical Game]," "Game N descends from [Canonical Game]'s technique vocabulary."

### In MDX prose

Per-unit prose can name canonical games when discussing techniques or traditions (e.g., "the masked-sprite technique Ultimate pioneered in Atic Atac"). But the curriculum game being taught is always named by its own inspired-by name, never the canonical reference.

### In marketing

Marketing copy follows the same rule. "Shadowkeep is a multi-room adventure in the Atic Atac tradition." Not: "Shadowkeep is a Spectrum Atic Atac clone."

### When canon and original align

Some legacy names in the curriculum (Hangman, Tic-Tac-Toe) are mechanic-names, not trademarks. The convention's principle #2 ("inspired-by, not clones") drives the rename regardless — see [spectrum-basic-v6.4-renames.md](spectrum-basic-v6.4-renames.md) for Cut A application (rename all 11 canonically-named BASIC games, not just active trademarks).

## Drift triggers

If discussion or copy shows any of these patterns, stop and re-read this decision:

1. **A curriculum game named after a real product** (e.g., "Pong," "Pac-Man," "Battleship") in any new game spec or unit.
2. **A unit's MDX prose framing the curriculum game AS the canonical game** (e.g., "In this unit you'll build Pac-Man" rather than "you'll build a maze-pursuit game in the Pac-Man tradition").
3. **Marketing copy describing a curriculum game as a "clone" or "remake"** of any commercial title.
4. **Vault entries treating curriculum games as alternative titles for canonical games.** They're different artefacts.
5. **A new game proposal that picks a name based on the canonical title rather than the design** (e.g., "Pyong" for a Pong-inspired game).

## Status

Active. Captured 2026-05-19. Descends from [real-retro-games.md](real-retro-games.md) (multi-disciplinary commitment) and the inspired-by framing already present in [shadowkeep-32-unit-commitment.md](shadowkeep-32-unit-commitment.md). Consolidates the principle into a binding rule applicable to both Spectrum BASIC and Spectrum Assembly track design.

Anchored in [[spectrum-assembly]] (current-state Assembly summary) and [[spectrum-basic]] (current-state BASIC summary).
