# Lesson 006: Data Bank

**Arc:** Knowledge Base
**Position:** Lesson 3 of 3 in arc
**Type:** Synthesis (Complete Game)
**Estimated Completion:** 60 lines of code

## Learning Objectives

- Use Dim to create arrays
- Load arrays from Data
- Implement search functionality
- Complete quiz system with categories

## Key Concepts Introduced

### Arrays (Dim)
Dim creates arrays. `Dim question$(20)` creates 20 string variables: question$(0) to question$(19).

### Zero-Based Indexing
AMOS arrays start at index 0 by default (unlike C64 BASIC which starts at 1).

### Loading Arrays
Read Data into arrays for flexible manipulation and random access.

### Array Search
Loop through array checking each element against search term.

## Code Pattern

```amos
Dim question$(10),answer$(10)
count=0

' Load questions
For i=0 To 9
  Read q$,a$
  If q$="END" Then Exit
  question$(i)=q$
  answer$(i)=a$
  Add count,1
Next i

' Quiz using arrays
For i=0 To count-1
  Print question$(i)
  Input response$
  If response$=answer$(i) Then
    Print "Correct!"
  End If
Next i

Data "Question 1","Answer 1"
Data "Question 2","Answer 2"
Data "END","END"
```

## Quick Reference

- `Dim array$(size)` - Create array
- `array$(index)` - Access element
- Arrays start at index 0
- Use count variable to track how many elements loaded

---

**Version:** 1.0
**Created:** 2025-10-24
