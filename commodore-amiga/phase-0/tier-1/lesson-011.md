# Lesson 011: Music Player

**Arc:** Paula Audio
**Position:** Lesson 2 of 2 in arc
**Type:** Synthesis (Music Application)
**Estimated Completion:** 50 lines of code

## Learning Objectives

- Use Music Bank for multi-channel music
- Create interactive music player
- Master tempo and music control
- Combine sound with visual feedback

## Key Concepts Introduced

### Music Bank
Music Bank loads and plays music. AMOS music files contain note patterns for all 4 channels, creating full compositions.

### Music Commands
`Music number` plays music from bank. `Music Stop` stops playback. `Music number` is tempo in 50Hz units.

### Music Variables
`Music()` returns playback status. `Music(0)` = current position, `Music(1)` = playing? (0/1).

### Audio Visualization
Combine Paula audio with screen effects. Update display based on music status for visual feedback.

## Code Pattern

```amos
Screen Open 0,320,256,16,Lowres
Curs Off: Flash Off: Cls 0

' Note: Would normally load music bank
' Music Bank Load "music.abk"

Locate 8,8: Print "MUSIC PLAYER"
Locate 10,6: Print "1-5: Play Track"
Locate 11,6: Print "S: Stop"
Locate 12,6: Print "Q: Quit"

track=0

Do
  k$=Upper$(Inkey$)

  If k$>="1" and k$<="5" Then
    track=Val(k$)
    Music track
  End If

  If k$="S" Then Music Stop
  If k$="Q" Then Exit

  ' Visual feedback
  If Music(1) Then
    Ink 2: Locate 14,10
    Print "Playing Track ";track
  Else
    Ink 1: Locate 14,10
    Print "Stopped       "
  End If

  Wait Vbl
Loop

Music Stop
Wait Key
```

## Quick Reference

- `Music Bank Load "file"` - Load music bank
- `Music number` - Play music track
- `Music Stop` - Stop playback
- `Tempo number` - Set tempo (50=1 second)
- `Music(0)` - Current position
- `Music(1)` - Playing? (0/1)

---

**Version:** 1.0
**Created:** 2025-10-24
