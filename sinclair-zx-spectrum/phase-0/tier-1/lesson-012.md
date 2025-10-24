# Lesson 012: Character Movement

**Arc:** Moving Sprites
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 25 lines of code

## Learning Objectives

- Move characters with PRINT AT
- Use INKEY$ for keyboard input
- Erase previous character position
- Create smooth character movement

## Key Concepts Introduced

### Character Sprites
Use PRINT AT to position characters as simple sprites. Print space to erase previous position.

### INKEY$ Polling
Check INKEY$ each frame to read keyboard. Empty string means no key pressed.

### Movement Pattern
1. Store old position
2. Get input and update position
3. Erase old position (print space)
4. Draw new position

## Code Pattern

```basic
10 LET x=15: LET y=10
20 LET ox=x: LET oy=y
30 IF INKEY$="q" THEN LET y=y-1
40 IF INKEY$="a" THEN LET y=y+1
50 IF INKEY$="o" THEN LET x=x-1
60 IF INKEY$="p" THEN LET x=x+1
70 PRINT AT oy,ox;" "
80 PRINT AT y,x;"@"
90 GO TO 20
```

## Quick Reference

- `INKEY$` - Read key (or empty if none)
- QAOP keys: Classic Spectrum control scheme
- Print space to erase character
- Store old position before moving

---

**Version:** 1.0
**Created:** 2025-10-24
