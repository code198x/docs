# Lesson 009: Colour Clash

**Arc:** Character Graphics
**Position:** Lesson 3 of 3 in arc
**Type:** Synthesis (Demonstration)
**Estimated Completion:** 60 lines of code

## Learning Objectives

- Experience Spectrum's attribute system firsthand
- Understand colour clash (8×8 character block limitations)
- Create simple drawing tool
- Learn creative workarounds for colour constraints

## Key Concepts Introduced

### Attribute System
Colours apply to 8×8 pixel blocks, not individual pixels. This is the famous "colour clash" - can't have multi-colour graphics within one character block.

### ATTR Function
ATTR (row,col) reads the attribute byte for a character position. Contains INK, PAPER, BRIGHT, FLASH info.

### Drawing Tool
Interactive program using INKEY$ to move cursor and draw with different colours.

## Code Pattern

```basic
10 LET x=128: LET y=88
20 IF INKEY$="q" THEN LET y=y+8
30 IF INKEY$="a" THEN LET y=y-8
40 IF INKEY$="o" THEN LET x=x-8
50 IF INKEY$="p" THEN LET x=x+8
60 IF INKEY$="SPACE" THEN PLOT x,y
70 GO TO 20
```

## Quick Reference

- `ATTR (row,col)` - Read attribute at position
- `INKEY$` - Read keyboard (empty string if no key)
- Attributes: 32×24 grid of 8×8 pixel blocks
- Colour clash: Constraint that inspired monochrome sprite art

**Creative Solutions:**
- Use monochrome graphics (single INK colour per block)
- Design around 8×8 grid
- Embrace the limitation as aesthetic

---

**Version:** 1.0
**Created:** 2025-10-24
