# Lesson 007: Rainbow Border

**Arc:** Visual Creation
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 10 lines of code

## Learning Objectives

- Introduction to hardware programming with POKE
- Control the VIC-II chip directly for visual effects
- Create animated colour cycling
- Understand memory-mapped hardware

## Prerequisites

**From Previous Lessons:**
- Variables and loops (L1)
- Basic program structure (L1-6)

**BASIC Knowledge:**
- FOR/NEXT loops
- Variables
- GOTO for continuous loops

## Key Concepts Introduced

### POKE Command
POKE writes a value directly to a memory address: `POKE 53280,3` sets memory location 53280 to value 3. This is direct hardware control.

### Memory-Mapped Hardware
The C64's chips are controlled by writing to specific memory addresses. Address 53280 controls border colour because the VIC-II chip watches that location.

### Colour Values
The C64 has 16 colours numbered 0-15: 0=black, 1=white, 2=red, 3=cyan, 4=purple, 5=green, 6=blue, 7=yellow, 8=orange, etc.

### Animation Through Loops
Changing a colour repeatedly creates animation. This is your first hardware-based visual effect!

## Code Pattern

```basic
10 C=0
20 POKE 53280,C
30 C=C+1
40 IF C>15 THEN C=0
50 FOR D=1 TO 50:NEXT D
60 GOTO 20
```

## Hardware Interaction

**Chips Involved:**
- **VIC-II** - Video Interface Chip, controls all graphics

**Memory Addresses:**
- `53280` ($D020) - Border colour
- `53281` ($D021) - Background colour

**Colour Values:**
```
0=Black    4=Purple   8=Orange    12=Dark Grey
1=White    5=Green    9=Brown     13=Light Green
2=Red      6=Blue    10=Light Red 14=Light Blue
3=Cyan     7=Yellow  11=Dark Grey 15=Light Grey
```

## Common Pitfalls

1. **Invalid colour values:** Only 0-15 are valid colours (16+ wrap around)
2. **POKE wrong address:** 53280 is border; 53281 is background (easy to confuse)
3. **Too fast animation:** Need delay loop or FOR/NEXT to make animation visible
4. **Forgetting cycle reset:** Colours go 0-15 then must reset to 0

## Extension Ideas

- Cycle background colour too (53281)
- Cycle both in opposite directions
- Create colour patterns (red → orange → yellow)
- Add speed control (change delay duration)
- Synchronize with sound effects (preview L10)

## Builds Toward

**In This Tier:**
- L8: Screen memory - more complex POKEing
- L9: Interactive graphics with GET and POKE
- L10-11: POKE for sound (SID chip)

**In Next Tier:**
- Sprite control (POKE to sprite registers)
- Screen colour effects during gameplay

## Quick Reference

**VIC-II Colour Registers:**
- `POKE 53280,C` - Border colour
- `POKE 53281,C` - Background colour (main screen)
- `POKE 646,C` - Text colour (for PRINT)

**C64 Colour Chart:**
See `/docs/VIC-II-QUICK-REFERENCE.md` for complete colour reference

**Delay Loop Pattern:**
```basic
100 FOR D=1 TO 50:NEXT D  :REM Short delay
200 FOR D=1 TO 200:NEXT D :REM Longer delay
```

**Animation Loop Pattern:**
```basic
10 C=0             :REM Start value
20 POKE 53280,C    :REM Apply to hardware
30 C=C+1           :REM Increment
40 IF C>15 THEN C=0 :REM Wrap around
50 [DELAY]         :REM Visible timing
60 GOTO 20         :REM Repeat
```
