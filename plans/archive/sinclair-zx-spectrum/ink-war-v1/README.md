# Ink War v1 Archive

**Archived:** 2026-01-09
**Reason:** Content structure mismatch with 64-unit curriculum

## What This Was

A compressed 16-unit version of Ink War that attempted to build the complete game in 16 units. The structure jumped straight into gameplay without the foundational teaching specified in the curriculum.

## Why It Was Archived

The 64-unit curriculum (documented in `/docs/plans/sinclair-zx-spectrum/game-01-ink-war.md`) specifies:

- **Phase 1 (Units 1-16):** Display Foundation - screen memory, attributes, Z80 basics
- **Phase 2 (Units 17-32):** Game Mechanics - input, turns, core gameplay
- **Phase 3 (Units 33-48):** AI and Polish - computer opponent, sound
- **Phase 4 (Units 49-64):** Presentation - menus, options, release

The archived content covered:

| Archived Unit | Topic | Curriculum Location |
|---------------|-------|---------------------|
| Unit 01 | The Board | Phase 1, Unit 14 |
| Unit 02 | The Cursor | Phase 2, Unit 20 |
| Unit 07 | Simple AI | Phase 3, Unit 35 |
| Unit 12 | Title Screen | Phase 4, Unit 50 |

This skipped all foundational teaching about the Spectrum's display system.

## Contents

- `units/` - Original 16 MDX unit files
- `code-samples/` - Original assembly code for each unit

## Potential Reuse

The assembly code may contain useful snippets for the rewritten curriculum, particularly:
- Attribute manipulation routines
- Cursor movement logic
- AI decision code
- Board drawing routines

However, the pedagogical structure needs complete rewrite.
