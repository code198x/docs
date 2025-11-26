# SID Symphony: Bonus Units (9-16) — Overview

**Game:** SID Symphony (C64)
**Date:** 2025-11-25
**Status:** Planned (not yet designed in detail)

## Structure

**Core Game (Units 1-8):** Build a complete, playable rhythm game
**Bonus Units (Units 9-16):** Polish, depth, and advanced features (optional)

Bonus units are self-contained enhancements. Learners can pick and choose based on interest. Each adds value independently.

---

## Bonus Unit Summary

| Unit | Title | What It Adds | Core Teaching |
|------|-------|--------------|---------------|
| 9 | Sound Design | Waveforms, filters, bum notes | SID depth, audio feedback |
| 10 | Timing Windows | Perfect/Good/Late grades | Precision detection |
| 11 | Combo System | Score multipliers | Game balance, rewards |
| 12 | Visual Juice | Screen effects, colour feedback | Game feel |
| 13 | Song Selection | Menu with multiple songs | Menu systems |
| 14 | Difficulty Modes | Easy/Normal/Hard options | Configuration patterns |
| 15 | High Scores | Top 5 leaderboard | Sorting, text input |
| 16 | The Final Mix | Full polish, attract mode | Shipping mindset |

---

## Unit 9: Sound Design

**Goal:** Make the SID sing properly.

**What changes:**
- Track-specific waveforms (pulse for track 1, sawtooth for track 2, triangle for track 3)
- Filter sweep on successful hits (cutoff frequency ramps up/down)
- Dissonant "bum note" on misses (wrong frequency, quick decay)
- Tuned ADSR envelopes for punchier, more musical sound

**Core teaching:**
- SID filter registers ($D415-$D418)
- Waveform selection bits
- Audio as feedback mechanism

**The "Aha" moment:** The game sounds like music now, not just beeps.

---

## Unit 10: Timing Windows

**Goal:** Reward precise timing.

**What changes:**
- Define timing zones based on note position when hit:
  - Perfect: columns 1-2 (centre of hit zone)
  - Good: columns 0 or 3 (edges)
  - Late: column 4 (just outside, grace period)
- Different point values: Perfect=15, Good=10, Late=5
- Brief text flash showing grade ("PERFECT!", "GOOD", "LATE")
- Perfect hits might get bonus effects (brighter flash, different sound)

**Core teaching:**
- Multi-threshold detection
- Signed arithmetic for "near miss" detection
- Feedback granularity

**The "Aha" moment:** Timing matters. You start trying for Perfects.

---

## Unit 11: Combo System

**Goal:** Reward sustained excellence.

**What changes:**
- Multiplier starts at 1x
- Every 10 consecutive hits, multiplier increases (2x, 3x, 4x)
- Any miss resets multiplier to 1x
- Score = base points × multiplier
- Display current multiplier on screen

**Core teaching:**
- Reward curves and pacing
- Multiplication in 6502 (shift-and-add)
- Balance tuning

**The "Aha" moment:** That 4x multiplier is precious. You play more carefully to protect it.

---

## Unit 12: Visual Juice

**Goal:** Make hits feel impactful.

**What changes:**
- Screen border flashes on big combos (10+, 20+, etc.)
- Hit zone pulses briefly on any hit (colour change for 2-3 frames)
- Crowd meter colour cycles when high (celebration effect)
- Miss causes brief screen shake or colour inversion
- Subtle but transformative for "feel"

**Core teaching:**
- Border colour register ($D020)
- Rapid colour RAM updates
- "Game feel" and feedback loops
- Less is more — restraint in effects

**The "Aha" moment:** Same mechanics, but now it *feels* amazing.

---

## Unit 13: Song Selection

**Goal:** Replayability through content.

**What changes:**
- Three songs of varying difficulty
- Menu screen: song list with cursor
- Up/down to highlight, SPACE to select
- Display song name, difficulty (stars), approximate length
- Return to menu after game over/victory

**Core teaching:**
- Menu state management
- Cursor/selection handling
- Multiple data sets (song pointers)
- Content as value

**The "Aha" moment:** It's not one game — it's a collection. You have favourites.

---

## Unit 14: Difficulty Modes

**Goal:** Accessibility and challenge.

**What changes:**
- Easy: slower note speed (NOTE_SPEED=6), wider hit zone (10 columns)
- Normal: as designed (NOTE_SPEED=4, 8-column zone)
- Hard: faster notes (NOTE_SPEED=2), narrower zone (5 columns)
- Setting on song select or separate options screen
- Difficulty affects score (Easy=0.5x, Normal=1x, Hard=2x base)

**Core teaching:**
- Constants as variables
- Configuration patterns
- Difficulty as design
- Accessibility matters

**The "Aha" moment:** Your friend who's "bad at games" can play Easy. You can challenge yourself on Hard.

---

## Unit 15: High Scores

**Goal:** Persistence and competition.

**What changes:**
- Track top 5 scores in memory (resets on power off)
- After game over/victory, check if score qualifies for table
- If yes, prompt for 3-letter initials (A-Z selection)
- Display high score table on title screen
- Scores are per-song or global (design choice)

**Core teaching:**
- Simple sorting algorithm (insertion sort)
- Text/character input handling
- Data display and formatting
- Memory as persistence (limited)

**The "Aha" moment:** Your initials on the screen. You want to beat your own score.

---

## Unit 16: The Final Mix

**Goal:** Ship it.

**What changes:**
- Animated title screen (colour cycling text, maybe simple animation)
- Smooth transitions between states (fade to black, wipe effects)
- Attract mode: if idle on title for 30 seconds, show AI playing demo
- Final code cleanup and organisation
- Comments, structure, pride in the codebase

**Core teaching:**
- Polish as discipline
- Attract mode / demo playback
- Transition effects
- "Done" is a feature
- Shipping mindset

**The "Aha" moment:** This isn't a learning project anymore. This is a game you'd put on a disk and share.

---

## Dependencies

Most bonus units are independent, but some light dependencies exist:

- Unit 11 (Combos) benefits from Unit 10 (Timing Windows) but doesn't require it
- Unit 14 (Difficulty) is easier after Unit 13 (Song Selection) for UI
- Unit 16 (Final Mix) assumes most other units are done

Recommended order: 9 → 10 → 11 → 12 → 13 → 14 → 15 → 16

But learners can skip around based on interest.

---

## Presentation on Website

```
SID Symphony

Units 1-8: Build the Game ✓
  [list of core units]

Units 9-16: Polish the Game (Bonus)
  [list of bonus units, marked as optional]
```

Bonus units could be visually distinct (different colour, "BONUS" tag) to signal they're extra content for motivated learners.

---

## Future Considerations

If bonus units prove popular, could add more:

- Unit 17+: Two-player mode
- Disk loading for more songs
- Custom character graphics
- Sprite-based notes
- Raster interrupt effects

But 16 units (8 core + 8 bonus) is a complete, satisfying package.
