# Lesson 010: Paula Sound

**Arc:** Paula Audio
**Position:** Lesson 1 of 2 in arc
**Type:** Standard
**Estimated Completion:** 25 lines of code

## Learning Objectives

- Understand Paula audio chip (4 channels)
- Play sound samples with Sam Play
- Control volume and channel selection
- Experience Amiga's distinctive sound

## Key Concepts Introduced

### Paula Audio Chip
Paula provides 4 independent 8-bit PCM channels. Each channel can play different samples simultaneously at different pitches.

### Sam Play Command
Sam Play plays sound samples. `Sam Play channel,sample` where channel is 0-3, sample is loaded sample number.

### Sample Banks
AMOS includes built-in samples (1-40). Sam Bank loads external sample banks. Samples are 8-bit signed PCM.

### Volume Control
Vol controls playback volume per channel. `Vol channel,volume` where volume is 0-64.

## Code Pattern

```amos
' AMOS includes 40 built-in samples
Screen Open 0,320,256,2,Lowres
Curs Off: Cls 0

Locate 5,10: Print "PAULA SOUND DEMO"
Locate 7,8: Print "Press keys 1-4"

Do
  k$=Inkey$

  ' Channel 0 (left)
  If k$="1" Then Sam Play 0,1

  ' Channel 1 (right)
  If k$="2" Then Sam Play 1,5

  ' Channel 2 (left)
  If k$="3" Then Sam Play 2,10

  ' Channel 3 (right)
  If k$="4" Then Sam Play 3,15

  If k$=" " Then Exit
Loop

Wait Key
```

## Quick Reference

- `Sam Play channel,sample` - Play sample on channel (0-3)
- `Vol channel,volume` - Set volume (0-64)
- `Sam Stop channel` - Stop playback
- Built-in samples: 1-40
- 4 channels: 0,2=left, 1,3=right

**Chips Used:** Paula (4-channel 8-bit PCM audio)

---

**Version:** 1.0
**Created:** 2025-10-24
