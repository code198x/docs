# Lesson 005: Knowledge Master

**Arc:** Knowledge Base
**Position:** Lesson 2 of 3 in arc
**Type:** Standard
**Estimated Completion:** 35 lines of code

## Learning Objectives

- Create menu systems for categories
- Use procedures for quiz sections
- Track high scores across attempts
- Master Restore for data reuse

## Key Concepts Introduced

### Menu-Driven Programs
Present options, get choice, branch to appropriate procedure.

### High Score Tracking
Keep best score in variable across multiple quiz attempts.

### Procedure Organisation
Use separate procedures for each quiz category. Clean code structure.

## Code Pattern

```amos
highscore=0

Do
  Cls
  Locate 5,10: Print "KNOWLEDGE MASTER"
  Locate 8,8: Print "1. History"
  Locate 10,8: Print "2. Science"
  Locate 12,8: Print "3. Quit"
  
  Input choice
  
  If choice=1 Then HistoryQuiz
  If choice=2 Then ScienceQuiz
  If choice=3 Then Exit
Loop

Procedure HistoryQuiz
  Restore HistoryData
  score=0
  ' Quiz loop here
  If score>highscore Then highscore=score
End Proc

#HistoryData:
Data "Question 1","Answer 1"
Data "Question 2","Answer 2"
```

## Quick Reference

- `Restore LabelName` - Reset to specific data section
- `#LabelName:` - Label for data sections
- Procedures for menu organization
- Exit to break from Do...Loop

---

**Version:** 1.0
**Created:** 2025-10-24
