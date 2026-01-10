# Ink War v2 Archive

**Archived:** 2026-01-09
**Reason:** Curriculum restructure - no playable game by Unit 16

## What This Was

Units 1-16 focused heavily on display theory:
- Units 1-4: Screen Memory (detailed memory layout)
- Units 5-8: Attribute System (byte structure, grid mapping)
- Units 9-12: Z80 Basics (registers, LD, arithmetic, jumps)
- Units 13-16: First Display (clear screen, board drawing)

## Why It Was Archived

By Unit 16, learners had only a display demonstration - no interactivity, no gameplay. This doesn't match the SID Symphony model where Unit 16 delivers a complete, playable game.

The restructured curriculum (v3) delivers a playable two-player game by Unit 16, with AI added in Phase 2.

## Contents

- `/units/` - MDX unit files (unit-01.mdx through unit-16.mdx)
- `/code-samples/` - Assembly code for each unit

## Lessons Learnt

1. Front-loading theory delays the reward of a playable game
2. Z80 instruction units work better integrated with gameplay
3. Two-player first, AI second - human opponent enables immediate testing
4. Match the SID Symphony phase structure: Foundation = playable game
