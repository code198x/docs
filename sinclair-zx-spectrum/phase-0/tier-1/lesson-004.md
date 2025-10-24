# Lesson 004: Brain Challenge

**Arc:** Knowledge Base
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 20 lines of code

## Learning Objectives

- Use READ and DATA to store information
- Create simple quiz mechanics
- Track scoring with variables
- Loop through multiple questions

## Prerequisites

**From Previous Lessons:**
- L1-3: Variables, INPUT, IF...THEN, loops

**BASIC Knowledge:**
- Basic program structure and conditionals

## Key Concepts Introduced

### DATA Statements
DATA stores lists of values inside your program. Use this for quiz questions, game levels, or any list of information.

### READ Command
READ retrieves the next value from DATA statements in order. Each READ gets one piece of data.

### Multiple DATA Types
DATA can hold numbers and strings mixed together. Read them into appropriate variable types ($ for strings).

### Sequential Access
READ moves through DATA in order. Once you've read to the end, use RESTORE to start over.

## Code Pattern

```basic
10 LET score=0
20 READ q$,a$
30 PRINT AT 10,5;q$
40 INPUT answer$
50 IF answer$=a$ THEN LET score=score+1
60 IF answer$=a$ THEN PRINT AT 12,8;"Correct!"
70 IF answer$<>a$ THEN PRINT AT 12,8;"Wrong!"
80 PAUSE 100
90 CLS
100 GO TO 20
200 DATA "Capital of UK?","London"
210 DATA "2+2?","4"
220 DATA "Red+Blue?","Purple"
```

## Hardware Interaction

**Chips Involved:**
- Z80 CPU (managing DATA pointer, string matching)
- ULA (displaying questions)

**Memory:**
- DATA stored in program memory
- READ pointer tracks current position

## Common Pitfalls

1. **Mismatched READ/DATA:** If READ expects string, DATA must have string
2. **Running out of DATA:** Program crashes if READ has no more DATA
3. **Wrong order:** READ gets DATA in the sequence it appears
4. **Forgetting quotes:** Strings in DATA need quotes if they contain commas

## Extension Ideas

- Add question counter (1 of 10)
- Show final score at end
- Add time limit with timer variable
- Create multiple categories
- Allow multiple choice (A, B, C, D)

## Builds Toward

**In This Tier:**
- L5: Add RESTORE for quiz retries
- L6: Arrays for more complex data storage

**In Next Tier:**
- DATA for level maps (platform games)
- DATA for character definitions (sprites)

## Quick Reference

**Essential Commands:**
- `READ variable` - Get next DATA value
- `DATA value1,value2,...` - Store values in program
- `RESTORE` - Reset READ pointer to start of DATA

**DATA Rules:**
- Can mix numbers and strings
- Strings with commas need quotes: `DATA "Smith, John"`
- Multiple DATA lines combine into one list
- Numbers don't need quotes: `DATA 100,200,300`

**Typical Pattern:**
```basic
10 READ name$,age,score
20 PRINT name$;" is ";age
...
100 DATA "Alice",25,100
110 DATA "Bob",30,95
```

**Error Handling:**
- `OUT OF DATA in line X` means no more DATA available
- Use counter to know when to stop reading

---

**Version:** 1.0
**Created:** 2025-10-24
**Status:** Lesson specification complete
