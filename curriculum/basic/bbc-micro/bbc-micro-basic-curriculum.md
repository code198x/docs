# BBC Micro BASIC Curriculum

**Status:** Future — Stub Entry
**Priority:** High
**Language:** BBC BASIC

---

## Why BBC BASIC?

BBC BASIC is widely considered **the best 8-bit BASIC dialect**:

- Structured programming (PROC/FN, REPEAT/UNTIL, multi-line IF)
- Named procedures and functions with local variables
- Inline assembler built into the language
- Fast interpreter — notably quicker than CBM BASIC
- Excellent documentation from the BBC Computer Literacy Project

## Language Features

| Feature | BBC BASIC | Comparison |
|---------|-----------|------------|
| Procedures | `DEF PROC` / `ENDPROC` | C64 BASIC lacks this |
| Functions | `DEF FN` with local vars | Far more powerful |
| Loops | `REPEAT/UNTIL`, `FOR/NEXT` | Structured loops |
| Conditionals | Multi-line `IF/THEN/ELSE/ENDIF` | Not single-line only |
| Assembler | `[` `]` inline assembly | Unique feature |
| Sound | `SOUND`, `ENVELOPE` | Sophisticated |
| Graphics | `DRAW`, `PLOT`, `MOVE`, `GCOL` | Turtle-style + modes |

## Curriculum Approach (Proposed)

**Track:** BASIC Gateway
**Games:** 8-16 (matching Tier 2 platform status)
**Units per game:** 4-12

Would teach structured BASIC programming:
1. Variables, input/output
2. Procedures and functions
3. Graphics modes and colours
4. Sound and envelopes
5. File operations
6. Inline assembly introduction

## Sample Game Progression

| # | Game | Units | Skills |
|---|------|-------|--------|
| 1 | Number guessing | 4 | Input, conditions, loops |
| 2 | Text adventure | 8 | Procedures, data structures |
| 3 | Graphics demo | 4 | Graphics modes, DRAW/PLOT |
| 4 | Breakout clone | 8 | Animation, collision |
| 5 | Platform game | 12 | Sprites, scrolling |
| 6 | Sound demo | 4 | SOUND, ENVELOPE |
| 7 | Arcade shooter | 12 | Full game techniques |
| 8 | Capstone | 16 | Everything combined |

## Toolchain

| Tool | Purpose |
|------|---------|
| BeebEm | Emulator with BASIC environment |
| b2 | Modern emulator |
| BASIC Editor | External editing |

## Resources

- [BBC BASIC Manual](http://www.bbcbasic.co.uk/bbcbasic/manual/)
- [BBC Micro User Guide](https://stardot.org.uk/mirrors/www.bbcdocs.com/filebase/essentials/BBC%20Microcomputer%20User%20Guide.pdf)
- [Stardot Forums](https://stardot.org.uk/forums/)

---

*This is a stub entry for a future curriculum. Content will be developed when this platform is prioritised.*
