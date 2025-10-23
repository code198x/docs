# Lesson 006: Data-Driven Quiz

**Arc:** Knowledge Base
**Position:** Lesson 3 of 3 in arc
**Type:** Synthesis
**Estimated Completion:** 40 lines of code

## Learning Objectives

- Use DATA and READ statements for storing structured information
- Create expandable, data-driven programs
- Separate data from program logic
- Build a complete quiz engine that's easy to modify

## Prerequisites

**From Previous Lessons:**
- String variables and quiz structure (L4)
- Arrays for structured data (L5)
- Loops and conditionals (L1-3)

**BASIC Knowledge:**
- Arrays (DIM)
- String handling
- Program flow control

## Key Concepts Introduced

### DATA Statements
DATA stores information directly in the program: `DATA "LONDON","PARIS","ROME"`. Think of it as a built-in database within your code.

### READ Statement
READ pulls values from DATA statements in order: `READ A$` gets the next item. Pair with RESTORE to start over from the beginning.

### Data-Driven Design
Separating data from logic means you can add 100 quiz questions without changing the quiz engine code. Change DATA, not program logic.

## Code Pattern

```basic
10 DIM Q$(10),A$(10)
20 FOR I=1 TO 5
30 READ Q$(I),A$(I)
40 NEXT I
50 REM Quiz engine
60 FOR I=1 TO 5
70 PRINT Q$(I)
80 INPUT U$
90 IF U$=A$(I) THEN S=S+1:PRINT "YES!"
100 IF U$<>A$(I) THEN PRINT "NO:",A$(I)
110 NEXT I
120 PRINT "SCORE:";S;"/5"
130 END
1000 DATA "CAPITAL OF ENGLAND?","LONDON"
1010 DATA "2+2=?","4"
1020 DATA "COLOUR OF SKY?","BLUE"
```

## Hardware Interaction

**Chips Involved:**
- None - pure BASIC data management

**Memory Addresses:**
- None yet

## Common Pitfalls

1. **DATA type mismatch:** Reading string into numeric variable (or vice versa) causes errors
2. **Out of DATA error:** READ more times than DATA items exist
3. **Forgetting RESTORE:** After reading all DATA, need RESTORE to read again
4. **DATA order matters:** READ pulls sequentially, first READ gets first DATA item

## Extension Ideas

- Add 20+ questions for longer quiz
- Add categories (use DATA to store category tags)
- Randomize question order
- Add multiple choice options (DATA stores all options)
- Save quiz results to high score hall (combine with L5)

## Builds Toward

**In This Tier:**
- L16: Text adventure uses DATA for room descriptions

**In Next Tier:**
- Enemy AI patterns stored in DATA
- Level designs stored in DATA
- Music note sequences in DATA (L25)

**In Next Tier (3):**
- Complete RPG dialogue trees (L42)
- Level design data (L35)
- Inventory item definitions (L41)

## Quick Reference

**DATA/READ Commands:**
- `DATA value1,value2,value3` - Store data in program
- `READ variable` - Pull next DATA value
- `RESTORE` - Reset READ pointer to first DATA
- `RESTORE line#` - Reset to specific DATA line

**Data-Driven Pattern:**
```basic
10 DIM Q$(N),A$(N)  :REM Arrays for data
20 FOR I=1 TO N
30 READ Q$(I),A$(I)  :REM Load from DATA
40 NEXT I
50 REM Now use Q$(I) and A$(I) in program logic
900 REM DATA section at end
1000 DATA "Question 1","Answer 1"
1010 DATA "Question 2","Answer 2"
```

**Best Practices:**
- Put DATA statements at high line numbers (1000+)
- Group related DATA together
- Comment DATA sections clearly
- Keep DATA types consistent within groups
