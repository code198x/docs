# Lesson 004: Amiga Quiz

**Arc:** Knowledge Base
**Position:** Lesson 1 of 3 in arc
**Type:** Standard
**Estimated Completion:** 25 lines of code

## Learning Objectives

- Use Data and Read statements
- Track scoring across questions
- Loop through quiz questions
- Restore to reset data pointer

## Key Concepts Introduced

### Data Statements
Data stores lists of values. Unlike C64 BASIC, AMOS doesn't need line numbers for Data.

### Read Command
Read retrieves next value from Data in order. Can mix strings and numbers.

### Restore
Restore resets the data pointer to start, allowing multiple reads through same data.

## Code Pattern

```amos
score=0

For q=1 To 3
  Read question$,answer$
  
  Print question$
  Input response$
  
  If response$=answer$ Then
    Add score,1
    Print "Correct!"
  Else
    Print "Wrong! Answer: "+answer$
  End If
  
  Wait 100
  Cls
Next q

Print "Final Score: ";score;"/3"

Data "Capital of UK?","London"
Data "Amiga CPU?","68000"
Data "RAM type for graphics?","Chip"
```

## Quick Reference

- `Data value1,value2,...` - Store values
- `Read variable` - Get next data value
- `Restore` - Reset data pointer
- `For...Next` - Loop structure
- Data doesn't need line numbers in AMOS

---

**Version:** 1.0
**Created:** 2025-10-24
