# Lesson 010: Beep Composer

**Arc:** Sound Lab
**Position:** Lesson 1 of 2 in arc
**Type:** Standard
**Estimated Completion:** 15 lines of code

## Learning Objectives

- Introduction to SID chip programming
- Generate musical notes using POKE
- Understand frequency, waveform, and ADSR basics
- Create simple melodies

## Prerequisites

**From Previous Lessons:**
- POKE command for hardware control (L7-8)
- Loops for sequences (L1-6)

**BASIC Knowledge:**
- POKE command
- FOR/NEXT loops
- Delays for timing

## Key Concepts Introduced

### SID Chip
The Sound Interface Device (SID) is the C64's legendary sound chip. It has 3 independent voices, each with waveform, frequency, and volume control.

### Frequency Values
Musical notes have specific frequencies. Higher frequency = higher pitch. Frequencies are 16-bit values (0-65535) stored in two registers.

### Waveform Selection
Different waveforms create different tones: triangle (soft), sawtooth (bright), pulse (hollow), noise (percussion). Value 17 = triangle wave.

### ADSR Envelope
Attack, Decay, Sustain, Release control how notes start, hold, and end. Think of it as the "shape" of the sound over time.

## Code Pattern

```basic
10 REM Play middle C note
20 POKE 54296,15          :REM Volume to max
30 POKE 54272,0:POKE 54273,32  :REM Frequency (middle C)
40 POKE 54277,0:POKE 54278,240 :REM ADSR envelope
50 POKE 54276,17          :REM Triangle wave on
60 FOR D=1 TO 500:NEXT D  :REM Duration
70 POKE 54276,16          :REM Sound off
```

## Hardware Interaction

**Chips Involved:**
- **SID** (6581/8580) - Sound Interface Device

**Memory Addresses (Voice 1):**
- `54272-54273` ($D400-$D401) - Frequency (lo/hi bytes)
- `54276` ($D404) - Waveform control
- `54277-54278` ($D405-$D406) - ADSR envelope
- `54296` ($D418) - Master volume (0-15)

**Waveform Values:**
- `17` - Triangle wave (soft, mellow)
- `33` - Sawtooth wave (bright, buzzy)
- `65` - Pulse wave (hollow, reedy)
- `129` - Noise (percussion, effects)
- `16` - Gate off (stop sound)

## Common Pitfalls

1. **No volume:** Forgetting POKE 54296,15 means silence
2. **16-bit frequencies:** Need two POKEs for each frequency (lo byte, hi byte)
3. **Gate control:** Bit 0 must be 1 for sound on, 0 for off (17=on, 16=off)
4. **Forgetting ADSR:** Poor envelope = clicks and pops
5. **Voice interference:** If another program used SID, need to initialize fully

## Extension Ideas

- Play a scale (C, D, E, F, G, A, B)
- Create simple melody (Mary Had a Little Lamb)
- Try different waveforms (sawtooth, pulse, noise)
- Add rhythm variation (short and long notes)
- Keyboard control (keys play different notes)

## Builds Toward

**In This Tier:**
- L11: Sound effects library for games

**In Next Tier:**
- Multi-voice music (L24-28)
- Non-blocking music during gameplay (L26)
- Complex sound effects (L27)

## Quick Reference

**SID Voice 1 Registers:**
```
54272 ($D400) - Frequency low byte
54273 ($D401) - Frequency high byte
54274 ($D402) - Pulse width low (for pulse wave)
54275 ($D403) - Pulse width high
54276 ($D404) - Control register (waveform + gate)
54277 ($D405) - Attack/Decay
54278 ($D406) - Sustain/Release
```

**Musical Note Frequencies (approximate):**
```
Middle C: 8372  (POKE 54272,84:POKE 54273,32)
D:        9398  (POKE 54272,182:POKE 54273,36)
E:       10548  (POKE 54272,52:POKE 54273,41)
F:       11176  (POKE 54272,168:POKE 54273,43)
G:       12544  (POKE 54272,0:POKE 54273,49)
A:       14080  (POKE 54272,0:POKE 54273,55)
B:       15804  (POKE 54272,188:POKE 54273,61)
```

**See Reference:**
`/docs/SID-QUICK-REFERENCE.md` (if it exists) for complete frequency table

**Simple Note Pattern:**
```basic
10 POKE 54296,15          :REM Volume
20 POKE 54277,0:POKE 54278,240 :REM ADSR
30 POKE 54272,FL:POKE 54273,FH :REM Frequency
40 POKE 54276,17          :REM On
50 FOR D=1 TO 500:NEXT D  :REM Duration
60 POKE 54276,16          :REM Off
```
