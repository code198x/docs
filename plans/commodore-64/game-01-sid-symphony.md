# SID Symphony: 64-Unit Outline

**Game:** C64 Game 1: SID Symphony
**Units:** 64
**Concept:** Rhythm game - notes scroll across three tracks, hit the correct key when notes reach the hit zone. Guitar Hero on the C64.

**Commercial Quality Target:** A game that could have sold for £9.99 on cassette in 1986. Polished, replayable, impressive to show friends.

**Design Principle:** "Show First, Explain Later" - Scaffold provides working code immediately; theory follows experience.

---

## The Finished Game

Before detailing the units, here's what the learner builds:

### Core Gameplay
- Three note tracks (high, mid, low) corresponding to three SID voices
- Notes scroll right-to-left toward a hit zone
- Player presses Z/X/C (or joystick positions) to hit notes
- Timing matters: Perfect, Good, Miss ratings
- Combo system rewards consecutive hits
- Health/performance meter - too many misses ends the song

### Content
- 5 complete songs of varying difficulty
- 3 difficulty levels per song (Easy/Normal/Hard)
- Practice mode (slow speed, no fail)
- Career mode (unlock songs by completing previous)
- Endless mode (procedurally generated patterns)

### Audio
- Full SID music (not just beeps - actual composed tracks)
- Note sounds match the music when hit correctly
- Miss sounds (dissonant buzz)
- Voice synthesis for "Perfect!" "Miss!" callouts
- Sound effects layered on top of music

### Visuals
- Custom character set for notes, tracks, UI
- Animated hit zone (pulsing to beat)
- Screen flash on perfect hits
- Sprite-based effects for combos
- Colour cycling backgrounds
- Smooth note scrolling

### Polish
- Title screen with animated logo
- Attract mode (demo playback)
- High score table with name entry
- Options screen (difficulty, sound test)
- Pause functionality
- Credits sequence

---

## Engagement Milestones

| Milestone | Unit |
|-----------|------|
| First visible + audible output | 1 |
| First interactivity (trigger sounds) | 1 |
| First rhythm gameplay | 2 |
| First "game feel" (scoring, feedback) | 6 |
| Complete playable game | 16 |

---

## Phase 1: Foundation (Units 1-16)

*Goal: A working rhythm game with one song. Playable from start to finish.*

*By the end of this phase, the learner has built a complete, if simple, game. They understand the SID chip fundamentals, basic 6510 assembly, and the core game loop pattern. The game is playable and winnable/losable.*

---

### Unit 1: Hello SID

**Learning Objectives:**
- Run a working C64 program with sound AND visuals
- Trigger sounds by pressing keys
- See immediate feedback on screen
- Experience the SID chip from minute one

**Concepts Introduced:**
- Scaffold approach (working code provided)
- Memory-mapped I/O
- SID chip overview (three voices)
- Screen memory basics

**Scaffold Provides:**
- BASIC stub (10 SYS 2064)
- Screen layout with three tracks and hit zones
- SID configured with three distinct voices
- Keyboard reading for Z/X/C keys
- Visual feedback when keys pressed

**What the Learner Does:**
- Runs the scaffold - sees tracks, hears nothing yet
- Presses Z - voice 1 plays, track 1 flashes
- Presses X - voice 2 plays, track 2 flashes
- Presses C - voice 3 plays, track 3 flashes
- Changes SID frequency values, hears pitch change
- Changes screen colours, sees immediate result

**What the Learner Sees:**
Three horizontal tracks on screen with a hit zone on the left. Pressing Z/X/C triggers different notes and flashes the corresponding track. Interactive from the first moment.

**Technical Details:**
- SID base: $D400
- Screen memory: $0400
- Colour RAM: $D800
- Z/X/C checked via CIA keyboard matrix

---

### Unit 2: Notes Appear

**Learning Objectives:**
- Display notes that scroll across the screen
- Understand character-based animation
- See the basic rhythm game pattern
- Notes sync to a simple beat

**Concepts Introduced:**
- Character movement (erase, draw, move)
- Beat timing with frame counting
- Note data structure basics
- Right-to-left scrolling

**Code Written:**
```
- Add note spawning on beat
- Notes appear at right edge of track
- Move notes left each frame
- Notes disappear at left edge
- Simple test pattern (4 notes, repeating)
```

**What the Learner Sees:**
Notes scroll from right to left across the three tracks in time with a simple beat. They can press keys when notes reach the hit zone - the SID sounds match. It feels like a game already.

**Technical Details:**
- Note character placed on screen
- X position decremented each frame
- Notes spawn from song data
- 25 frames per beat at 120 BPM (PAL)

---

### Unit 3: Making It Your Own

**Learning Objectives:**
- Customise the SID sounds by modifying waveforms and ADSR
- Change the visual appearance with different colours
- Learn by doing - modify values and experience the results
- Produce a uniquely-sounding version of the game

**Concepts Introduced:**
- SID voice registers through hands-on modification
- ADSR envelopes by hearing the differences
- Waveform selection by trying each one
- Colour RAM customisation

**Code Written:**
```
- Customisation section at top of code
- VOICE1_WAVE, VOICE2_WAVE, VOICE3_WAVE constants
- VOICE_ATTACK, VOICE_DECAY, VOICE_SUSTAIN, VOICE_RELEASE
- TRACK_COLOUR constants for each track
- BORDER_COLOUR, BACKGROUND_COLOUR
```

**What the Learner Sees:**
The game runs with different sounds and colours. Each voice has a distinct timbre. The screen has a custom colour scheme. Multiple "Try This" sections guide experimentation.

**Technical Details:**
- Voice register offsets (+7 per voice)
- Waveform bits: triangle=$11, sawtooth=$21, pulse=$41, noise=$81
- ADSR registers: Attack/Decay=$D405, Sustain/Release=$D406
- Colour RAM at $D800, screen at $0400
- Border at $D020, background at $D021

---

### Unit 4: Custom Graphics

**Learning Objectives:**
- Design custom characters for the game
- Switch VIC-II to use custom charset
- Create note, track, and hit zone graphics
- Professional visual appearance

**Concepts Introduced:**
- Character ROM and RAM
- 8 bytes per character definition
- Character memory pointer ($D018)
- 8x8 pixel grid design

**Code Written:**
```
- Copy ROM charset to $3000
- Define note character (arrow or circle)
- Define track line characters
- Define hit zone characters
- Point VIC to custom charset
```

**What the Learner Sees:**
The game looks polished now. Custom note graphics, clean track lines, distinctive hit zone. It looks like a real game, not placeholder graphics.

**Character Designs:**
- Note: solid circle or chevron pointing left
- Track: thin horizontal line
- Hit zone: vertical bar with glow effect
- Perfect/Good/Miss indicators

---

### Unit 5: Hit Detection

**Learning Objectives:**
- Detect when a key press matches a note
- Implement timing windows (Perfect/Good/Miss)
- Play correct SID note on hit
- Remove hit notes from play

**Concepts Introduced:**
- Timing window calculation
- Position-based detection
- Hit vs miss logic
- Note consumption (one input per note)

**Code Written:**
```
- check_hit: find note in hit zone on pressed track
- Calculate timing accuracy
- Perfect: ±2 frames from centre
- Good: ±4 frames
- Miss: key pressed but no note (or too early/late)
- Play SID note on successful hit
```

**What the Learner Sees:**
Pressing the right key at the right time removes the note and plays the sound. Wrong timing or wrong track does nothing. The core gameplay loop works.

**Technical Details:**
- Hit zone spans columns 3-5
- Check note X position against zone
- Track match required
- One note consumed per key press

---

### Unit 6: Scoring and Feedback

**Learning Objectives:**
- Implement score counter
- Award points for hit quality
- Display score on screen
- Visual feedback for hits/misses

**Concepts Introduced:**
- 16-bit score arithmetic
- Binary to decimal display
- Screen flash effects
- Colour feedback (flash on hit)

**Code Written:**
```
- score_lo, score_hi: 16-bit counter
- add_score: Perfect=100, Good=50
- display_score: show 6 digits
- Flash border/track on hit quality
- "PERFECT" or "GOOD" text flash
```

**What the Learner Sees:**
Score at top of screen increases on hits. Perfect hits flash brighter than good hits. The game provides satisfying feedback. Players want to hit perfects.

**Technical Details:**
- Score display at row 0
- Border colour flash: $D020
- Use BCD or division for display
- Max score 65535 (16-bit)

---

### Unit 7: Miss Handling

**Learning Objectives:**
- Detect notes that pass unhit
- Provide negative feedback for misses
- Track miss count
- Balance punishment vs reward

**Concepts Introduced:**
- Implicit misses (note left zone)
- Explicit misses (wrong key)
- Negative audio feedback
- Miss visual effect

**Code Written:**
```
- Check notes past hit zone (x < 3)
- Play miss sound (noise burst)
- Flash track red briefly
- Increment miss counter
- Track "fell through" notes
```

**What the Learner Sees:**
Notes that scroll past unhit trigger a harsh buzz and red flash. Pressing the wrong key also gives feedback. Mistakes feel like mistakes.

**Technical Details:**
- Miss sound: noise waveform, fast decay
- Track flash: red colour briefly
- Miss counter for health calculation

---

### Unit 8: Health System

**Learning Objectives:**
- Implement health/performance meter
- Health increases on hits, decreases on misses
- Display as bar graph
- Game ends when health depletes

**Concepts Introduced:**
- Clamped value (0-64 range)
- Bar graph with custom characters
- Game over condition
- Win/lose stakes

**Code Written:**
```
- health: value 0-64
- modify_health: Perfect+4, Good+2, Miss-8
- display_health: 8-character bar
- check_game_over: health==0 ends song
- Start at 32 (half full)
```

**What the Learner Sees:**
Health bar at bottom grows with hits, shrinks with misses. If it empties, the song ends in failure. Stakes are real now - the game can be lost.

**Technical Details:**
- Custom chars for full/half/empty bar
- 8 characters × 8 states = 64 levels
- Game over triggers immediately at 0

---

### Unit 9: Song Data

**Learning Objectives:**
- Design data format for songs
- Create first complete song
- Calculate memory requirements
- Balance difficulty with musicality

**Concepts Introduced:**
- Beat/track/note format
- Song length and structure
- End-of-song marker
- Musical composition basics

**Code Written:**
```
- Song data structure: beat, track, SID note
- First song: 64 beats, ~30 notes
- Musical pattern that sounds good
- End marker ($FF)
- Song length constant
```

**Data Format:**
```
; Beat 0: note on track 2
; Beat 4: note on track 1
; Beat 8: note on track 3
; etc.

song_data:
    !byte 0, 2, $24    ; beat, track, note
    !byte 4, 1, $30    ; beat, track, note
    !byte 8, 3, $18    ; beat, track, note
    ...
    !byte $FF          ; end marker
```

**What the Learner Sees:**
A complete song plays from start to finish. Notes appear on beat, player hits them, song progresses. First real musical experience.

---

### Unit 10: Song Playback

**Learning Objectives:**
- Play song from data
- Spawn notes at correct time
- Track song position
- Sync gameplay to music

**Concepts Introduced:**
- Song playhead (current beat)
- Note spawning from data
- Beat-to-screen timing
- Look-ahead for scrolling

**Code Written:**
```
- song_position: current beat
- Process song data each beat
- Spawn notes from data
- Handle multiple notes per beat
- Track song progress
```

**What the Learner Sees:**
Complete song plays with proper timing. Notes spawn exactly when they should. The rhythm feels right - hit notes to play the tune.

**Technical Details:**
- Look ahead: spawn notes 35 columns before hit zone
- Multiple notes can spawn on same beat
- Song playhead increments each beat

---

### Unit 11: Song End and Results

**Learning Objectives:**
- Detect end of song
- Display results screen
- Show final score and statistics
- Allow replay

**Concepts Introduced:**
- End-of-song detection
- Results calculation (percentage)
- State transition
- Replay logic

**Code Written:**
```
- Detect song end (all beats processed, all notes resolved)
- Clear screen for results
- Display: score, perfects, goods, misses
- Calculate and show percentage
- Wait for key, restart song
```

**What the Learner Sees:**
Song ends, results appear showing performance breakdown. Press key to play again. Complete game loop works.

**Technical Details:**
- Track perfects/goods/misses separately
- Percentage = (perfects + goods) / total * 100
- Results: SCORE, PERFECTS, GOODS, MISSES, ACCURACY

---

### Unit 12: Combo System

**Learning Objectives:**
- Track consecutive hits
- Implement score multiplier
- Break combo on miss
- Display combo prominently

**Concepts Introduced:**
- Combo counter
- Multiplier tiers
- Combo break feedback
- Risk/reward design

**Code Written:**
```
- combo: consecutive hits
- max_combo: best this song
- multiplier: 1x at 0, 2x at 10, 3x at 25, 4x at 50
- Score multiplied by current multiplier
- Combo resets to 0 on any miss
```

**What the Learner Sees:**
Combo counter climbs with each hit. Score multiplier increases at thresholds. Missing breaks the combo dramatically. Consistency is rewarded.

**Multiplier Tiers:**
- 0-9 hits: 1x
- 10-24 hits: 2x
- 25-49 hits: 3x
- 50+ hits: 4x

---

### Unit 13: Title Screen

**Learning Objectives:**
- Create title screen state
- Display game title
- Start game on key press
- Simple state machine

**Concepts Introduced:**
- Game states (TITLE, PLAYING, RESULTS)
- State machine pattern
- State dispatch
- Title screen design

**Code Written:**
```
- game_state: TITLE=0, PLAYING=1, RESULTS=2
- Title screen layout with "SID SYMPHONY"
- "PRESS FIRE TO START"
- Fire key → transition to PLAYING
- Clean state initialisation
```

**What the Learner Sees:**
Game starts at title screen with logo. Press fire to start playing. After results, press fire to return to title. Complete game flow.

**Technical Details:**
- State values: TITLE=0, PLAYING=1, RESULTS=2
- Dispatch: compare state, jump to handler
- Clean reset when entering PLAYING

---

### Unit 14: Game Over Screen

**Learning Objectives:**
- Handle health-depleted game over
- Different from successful completion
- Restart or return to title
- Distinct feedback for failure

**Concepts Introduced:**
- Win vs lose states
- Game over presentation
- Restart options
- Failure feedback

**Code Written:**
```
- game_over state when health==0
- Display "GAME OVER"
- Show score achieved
- Option to retry or return to title
- Distinct from results screen
```

**What the Learner Sees:**
Health depletes, "GAME OVER" appears with sad feedback. Score shown but marked as failed. Press to retry or return to title.

---

### Unit 15: Sound Polish

**Learning Objectives:**
- Distinct sounds for hit qualities
- Miss sound design
- Menu sounds
- Audio feedback completeness

**Concepts Introduced:**
- Sound design vocabulary
- Positive vs negative sounds
- UI sounds
- Audio polish

**Code Written:**
```
- perfect_sound: bright, high, satisfying
- good_sound: positive but lesser
- miss_sound: harsh buzz
- menu_sounds: select, confirm
- All events have audio feedback
```

**What the Learner Sees:**
Every action has appropriate sound. Perfect hits sound amazing. Misses sound harsh. Menu navigation clicks. Complete audio experience.

---

### Unit 16: Phase 1 Complete

**Learning Objectives:**
- Polish complete experience
- Fix remaining issues
- Playtest and tune
- Celebrate completion

**Concepts Introduced:**
- Integration testing
- Balance tuning
- Polish pass
- Milestone celebration

**Code Written:**
```
- Final bug fixes
- Difficulty balance (hit windows, health values)
- Visual consistency check
- Timing verification
- First song fully tuned
```

**What the Learner Sees:**
Complete, polished rhythm game. Title screen, gameplay with scoring and health, results or game over, restart loop. One song, fully playable. Hand it to a friend and watch them play SID Symphony.

**Phase 1 Checkpoint:**
The learner has built a working rhythm game. They understand SID sound, screen graphics, keyboard input, and game loop structure. The game is playable and fun. Everything from here builds on this foundation.

---

## Phase 2: Expansion (Units 17-32)

*Goal: Multiple songs, difficulty levels, game modes. A game with real content and variety.*

*By the end of this phase, the game has 5 songs, 3 difficulty levels, career mode, practice mode, endless mode, and advanced combo system. It's a game people would actually want to play multiple times.*

---

### Unit 17: Song Selection Screen

**Learning Objectives:**
- Create a menu system
- Display list of available songs
- Handle cursor movement
- Transition between game states

**Concepts Introduced:**
- Menu state management
- Cursor position tracking
- Key repeat delay
- State machine pattern

**Code Written:**
```
- menu_state: which menu screen is active
- song_list: array of song metadata
- draw_menu: display song names with cursor
- menu_input: up/down to move, fire to select
- transition_to_game: load selected song, switch state
```

**What the Learner Sees:**
A song selection screen lists available songs (currently just one). Cursor highlights selection. Press fire to play. The game has structure beyond just playing.

---

### Unit 18: Song 2 - Composing for SID

**Learning Objectives:**
- Understand basic music composition for games
- Create a song with different character than Song 1
- Use different SID voices effectively
- Balance difficulty with musicality

**Concepts Introduced:**
- Musical keys and scales
- Tempo and feel
- Voice assignment for melody/harmony/bass
- Note density for difficulty

**Code Written:**
```
- Song 2 data: ~40 notes, different tempo
- Distinct melodic feel (major key, upbeat)
- Use different waveform combinations
- Add to song_list array
```

**What the Learner Sees:**
Song selection now shows two songs. Song 2 plays noticeably differently - different music, different feel, similar difficulty.

**Composition Notes:**
- Song 1: 120 BPM, minor key, steady
- Song 2: 130 BPM, major key, bouncy
- Both introduce mechanics gently

---

### Unit 19: Difficulty Levels

**Learning Objectives:**
- Implement difficulty selection
- Modify game parameters based on difficulty
- Understand difficulty as content multiplier
- Add difficulty to UI

**Concepts Introduced:**
- Difficulty parameters (timing window, note density)
- Easy: wider windows, fewer notes
- Hard: tight windows, more notes
- UI for difficulty selection

**Code Written:**
```
- difficulty: 0=Easy, 1=Normal, 2=Hard
- timing_window: varies by difficulty
- Difficulty selection on song menu
- Display selected difficulty
```

**What the Learner Sees:**
Each song now shows Easy/Normal/Hard options. Easy gives more time to hit notes and is more forgiving. Hard punishes sloppy timing.

**Difficulty Parameters:**
| Parameter | Easy | Normal | Hard |
|-----------|------|--------|------|
| Perfect window | ±4 frames | ±2 frames | ±1 frame |
| Good window | ±8 frames | ±4 frames | ±2 frames |
| Health loss | -4 | -8 | -12 |

---

### Unit 20: Note Patterns for Difficulty

**Learning Objectives:**
- Generate difficulty variants from base song
- Thin notes for Easy, densify for Hard
- Keep musical integrity across difficulties
- Store variants efficiently

**Concepts Introduced:**
- Algorithmic pattern modification
- Note filtering (keep every Nth note)
- Note insertion (add off-beats)
- Variant storage strategies

**Code Written:**
```
- generate_easy: remove notes on weak beats
- generate_hard: add notes on off-beats
- Store as separate data or generate on load
- Maintain base pattern as Normal
```

**What the Learner Sees:**
Playing the same song on Easy has noticeably fewer notes. Hard has notes filling in gaps. The song remains recognisable but challenge varies dramatically.

---

### Unit 21: Song 3 - Faster Tempo

**Learning Objectives:**
- Handle faster scroll speeds
- Ensure hit detection works at high speed
- Compose for speed while remaining playable
- Test difficulty scaling at tempo

**Concepts Introduced:**
- Tempo ceiling (human reaction limits)
- Note anticipation at high speed
- Visual clarity at fast scroll
- Frame-rate concerns

**Code Written:**
```
- Song 3 data: 150 BPM, energetic
- Adjust scroll calculation for speed
- Verify hit detection at 1-frame windows
- Balance note density for playability
```

**What the Learner Sees:**
Song 3 scrolls faster, demands quicker reactions. The game tests speed now, not just rhythm accuracy. Easy mode on Song 3 ≈ Normal mode on Song 1.

---

### Unit 22: Combo Visuals

**Learning Objectives:**
- Provide visual feedback for combo status
- Create escalating visual intensity
- Use colour and sprites for emphasis
- Reward streaks viscerally

**Concepts Introduced:**
- Colour cycling tied to game state
- Hardware sprites for effects
- Border colour as feedback
- Escalating visual feedback

**Code Written:**
```
- Border colour shifts with combo tier
- Large combo number display
- Sprite explosion on multiplier increase
- "Fire" effect sprite at high combos
- All effects disable on combo break
```

**What the Learner Sees:**
As combo builds, the border shifts through colours, numbers grow large, sprites add visual flair. Breaking a 50+ combo is visually devastating as all the effects disappear. The combo feels important.

---

### Unit 23: Practice Mode

**Learning Objectives:**
- Implement alternate game mode
- Allow failure-free play for learning
- Provide speed adjustment
- Section loop for difficult parts

**Concepts Introduced:**
- Game mode as parameter
- Speed scaling (0.5x, 0.75x, 1x)
- Section markers in song data
- No-fail flag

**Code Written:**
```
- practice_mode: boolean flag
- speed_multiplier: affects scroll rate
- If practice_mode: health never depletes
- Speed selection in menu
- Can restart from last section marker
```

**What the Learner Sees:**
Practice mode in menu. Songs play slower and don't end on empty health. Learners can work through difficult sections without frustration.

---

### Unit 24: Song 4 - Syncopation

**Learning Objectives:**
- Compose with off-beat emphasis
- Challenge assumed rhythm patterns
- Provide visual cues for syncopation
- Test rhythm reading skills

**Concepts Introduced:**
- Syncopation in music
- Off-beat note placement
- Visual beat indicators
- Rhythm complexity

**Code Written:**
```
- Song 4 data: emphasis on off-beats
- Add beat marker visual (pulse on downbeat)
- Note patterns that contradict visual beat
- Test syncopation across difficulties
```

**What the Learner Sees:**
Song 4 feels different - notes land between expected beats. The visual beat marker helps but hands want to follow eyes, not ears. A new kind of challenge.

---

### Unit 25: Career Mode Structure

**Learning Objectives:**
- Implement progression system
- Lock content behind achievement
- Save and display progress
- Create sense of advancement

**Concepts Introduced:**
- Unlock conditions
- Progress persistence (in memory for now)
- Achievement thresholds
- Career menu UI

**Code Written:**
```
- song_unlocked: array of booleans
- unlock_condition: minimum score or completion
- Song 1 always unlocked
- Check unlock after results
- Career menu shows locked/unlocked status
```

**What the Learner Sees:**
Career mode shows songs 2-5 locked initially. Completing Song 1 unlocks Song 2. Progress creates motivation to continue. A reason to play beyond high scores.

---

### Unit 26: Song 5 - The Challenge

**Learning Objectives:**
- Compose a demanding finale song
- Use all SID capabilities learned so far
- Create memorable musical moments
- Balance difficulty with fairness

**Concepts Introduced:**
- Extended song length
- Dynamic difficulty within song
- Climactic sections
- Reward for mastery

**Code Written:**
```
- Song 5 data: 2+ minutes, 100+ notes
- Uses all three voices prominently
- Difficulty ramps within song
- Climactic ending section
```

**What the Learner Sees:**
Song 5 is clearly the boss. Longer, denser, more demanding. Completing it on Hard is a real achievement. The SID output is impressive.

---

### Unit 27: Joystick Support

**Learning Objectives:**
- Read joystick input
- Map joystick to three-track input
- Let player choose control scheme
- Handle both simultaneously

**Concepts Introduced:**
- CIA joystick reading
- Direction to track mapping
- Input method selection
- Control scheme UI

**Code Written:**
```
- read_joystick: check directions
- Map: up=track1, fire=track2, down=track3
- control_scheme: keyboard or joystick
- Selection in options
- Both can work simultaneously
```

**What the Learner Sees:**
Options menu includes control scheme. Joystick works as alternative to keyboard. Some players prefer one or the other.

**Joystick Mapping:**
- Up: Track 1 (high voice)
- Fire: Track 2 (mid voice)
- Down: Track 3 (low voice)

---

### Unit 28: Endless Mode - Procedural Generation

**Learning Objectives:**
- Generate note patterns algorithmically
- Follow musical rules for coherent patterns
- Create unlimited content
- Balance randomness with playability

**Concepts Introduced:**
- Procedural generation basics
- Beat grid constraints
- Probability distributions
- Seed-based randomness

**Code Written:**
```
- generate_note: decide if note appears on beat
- Probability increases with level
- Notes placed on beat grid
- Track selection weighted
- Infinite loop mode (no song end)
```

**What the Learner Sees:**
Endless mode generates notes forever. Patterns feel musical (mostly on beats) but unpredictable. High score is only goal.

---

### Unit 29: Endless Mode - Difficulty Curve

**Learning Objectives:**
- Implement dynamic difficulty
- Increase challenge over time
- Track level/progress in endless
- Balance for long sessions

**Concepts Introduced:**
- Dynamic difficulty adjustment
- Level as time survived
- Speed increase over time
- Density increase over time

**Code Written:**
```
- endless_level: increases with time
- Speed scales with level
- Note density scales with level
- Display current level
- Level up fanfare
```

**What the Learner Sees:**
Endless mode starts easy, gets progressively harder. Level number tracks progress. Eventually becomes impossible but that's the point. Competing for how long you survive.

---

### Unit 30: Statistics Tracking

**Learning Objectives:**
- Track persistent statistics
- Display lifetime achievements
- Create long-term goals
- Show progression over time

**Concepts Introduced:**
- Aggregate statistics
- 32-bit counters for large values
- Statistics display screen
- Progress visualisation

**Code Written:**
```
- total_notes_hit: lifetime counter
- total_perfects: lifetime counter
- best_combo: highest ever achieved
- games_played: session counter
- stats_screen: display all statistics
```

**What the Learner Sees:**
Statistics screen shows lifetime totals: notes hit, perfects, best combo, songs completed. A sense of overall progress beyond individual songs.

---

### Unit 31: ADSR Sound Design

**Learning Objectives:**
- Refine sound design using ADSR
- Create distinct sounds per track
- Improve miss feedback
- Professional audio polish

**Concepts Introduced:**
- ADSR deep dive
- Track-specific timbres
- Layered sound design
- Audio polish pass

**Code Written:**
```
- Track 1: bright, percussive (fast attack/decay)
- Track 2: warm, sustained (slow attack)
- Track 3: bass, punchy (medium attack, low sustain)
- Miss: harsh noise with fast decay
- All sounds refined for "feel"
```

**What the Learner Sees:**
The three tracks sound distinctly different. Hitting notes feels more satisfying. The SID is being used more expressively.

---

### Unit 32: Phase 2 Complete

**Learning Objectives:**
- Playtest complete content
- Balance difficulty curve across songs
- Verify all modes integrate properly
- Fix integration bugs

**Concepts Introduced:**
- System integration testing
- Balance tuning
- Player experience flow
- Bug prioritisation

**Code Written:**
```
- Playtest session with notes
- Adjust note patterns for balance
- Verify career unlock flow
- Fix any issues found
- Document known issues
```

**What the Learner Sees:**
The complete game with all content. Everything works together. Five songs, three difficulties, multiple modes. Ready for polish.

**Phase 2 Checkpoint:**
The game now has substantial content: 5 songs × 3 difficulties = 15 distinct challenges, plus endless mode for infinite play. Career mode provides progression. Practice mode helps learning. The game is feature-complete but not yet polished.

---

## Phase 3: Polish (Units 33-48)

*Goal: Make it feel professional. Visual effects, sound design, and user experience polish.*

*By the end of this phase, the game looks and sounds professional. Every interaction has feedback. The experience is cohesive and polished.*

---

### Unit 33: Title Screen Design

**Learning Objectives:**
- Design an impactful title screen
- Create logo with custom characters
- Establish visual identity
- Plan menu navigation

**Concepts Introduced:**
- Logo design on character grid
- Colour palette selection
- Visual hierarchy
- Brand identity

**Code Written:**
```
- Title screen character layout
- "SID SYMPHONY" logo in custom chars
- Menu options: Start, Options, High Scores
- Colour scheme matching game aesthetic
```

**What the Learner Sees:**
A proper title screen with large logo, clear menu options, cohesive colours. Looks like a commercial game.

---

### Unit 34: Title Screen Animation

**Learning Objectives:**
- Animate static elements
- Create visual interest
- Loop animations smoothly
- Add title music

**Concepts Introduced:**
- Frame-based animation
- Colour cycling techniques
- Music loop structure
- Attention management

**Code Written:**
```
- Logo shimmer animation
- Background colour cycling
- Pulsing menu cursor
- Short music loop on title
- Transition effects to menu
```

**What the Learner Sees:**
The title screen moves and breathes. Logo shimmers, colours cycle, music plays. The game feels alive even before playing.

---

### Unit 35: Attract Mode

**Learning Objectives:**
- Implement auto-play demonstration
- Record or script gameplay
- Return to title on input
- Showcase game features

**Concepts Introduced:**
- Demo playback system
- Attract mode timing
- Input interrupt
- Feature showcase

**Code Written:**
```
- attract_mode: plays Song 1 automatically
- Scripted or perfect-play input
- Timer to cycle through songs
- Any key returns to title
- Cycle: Title → Attract → Title
```

**What the Learner Sees:**
Leave the game idle and it plays itself, showing off gameplay. Perfect for shop displays or impressing friends. Commercial quality feature.

---

### Unit 36: Hit Zone Animation

**Learning Objectives:**
- Animate the hit zone to the beat
- Provide rhythmic visual feedback
- Enhance timing feel
- Create urgency

**Concepts Introduced:**
- Beat-synced animation
- Expansion/contraction effect
- Colour pulse
- Visual metronome

**Code Written:**
```
- hit_zone_anim: pulse on each beat
- Expand slightly on downbeat
- Colour intensity follows beat
- Performance indicator (changes with health)
```

**What the Learner Sees:**
The hit zone pulses in time with the music, expanding on each beat. It helps feel the rhythm and provides a visual metronome.

---

### Unit 37: Perfect Hit Effects

**Learning Objectives:**
- Create satisfying hit feedback
- Layer multiple effect types
- Make perfects feel special
- Reward accuracy dramatically

**Concepts Introduced:**
- Screen flash technique
- Sprite burst effects
- Sound punctuation
- Feedback layering

**Code Written:**
```
- perfect_hit_effect: all effects combined
- Border flash (white, 2 frames)
- Sprite starburst at note position
- Sound "punch" (quick noise burst)
- Score popup animation
```

**What the Learner Sees:**
A perfect hit triggers a cascade of feedback: flash, sparkle, sound, animated score. It feels amazing. Perfects become the goal.

---

### Unit 38: Good Hit Effects

**Learning Objectives:**
- Differentiate feedback tiers
- Make good feel okay, not great
- Motivate improvement
- Maintain consistency

**Concepts Introduced:**
- Tiered feedback design
- Subtle vs dramatic effects
- Positive but lesser reward
- Comparison feedback

**Code Written:**
```
- good_hit_effect: subset of perfect
- Smaller sprite effect
- No screen flash
- Softer sound
- Score popup (smaller)
```

**What the Learner Sees:**
Good hits still get feedback, but noticeably less than perfect. The difference motivates chasing perfects without punishing goods.

---

### Unit 39: Miss Effects

**Learning Objectives:**
- Provide negative feedback appropriately
- Make misses feel bad (not annoying)
- Don't over-punish
- Reset expectations

**Concepts Introduced:**
- Negative feedback design
- Brevity of punishment
- Screen shake technique
- Sound dissonance

**Code Written:**
```
- miss_effect: brief negative feedback
- Track "crack" sprite
- Screen shake (1-2 frames)
- Dissonant sound burst
- Combo counter breaks visually
```

**What the Learner Sees:**
Misses feel like mistakes - brief shake, harsh sound, combo breaks. But it's over quickly and doesn't dwell. Punishment is immediate and brief.

---

### Unit 40: Background Visuals

**Learning Objectives:**
- Add dynamic background
- Use raster effects for colour
- Keep performance stable
- Enhance atmosphere

**Concepts Introduced:**
- Raster splits for backgrounds
- Colour cycling patterns
- Performance budgeting
- Atmosphere through visuals

**Code Written:**
```
- background_anim: colour cycling pattern
- Raster interrupt for colour splits
- Simple starfield or gradient
- Intensity follows music/combo
- Performance monitoring
```

**What the Learner Sees:**
The background isn't static black anymore. Colour shifts and patterns add depth. At high combos, background intensifies.

---

### Unit 41: Voice Callouts

**Learning Objectives:**
- Implement SID voice synthesis
- Create short speech samples
- Trigger appropriately
- Mix with music

**Concepts Introduced:**
- SID vocal synthesis basics
- Sample triggering
- Volume mixing
- Appropriate frequency

**Code Written:**
```
- say_perfect: synthesize "PERFECT"
- say_miss: synthesize "MISS"
- Trigger on notable events
- Only on milestones (not every hit)
- Mix level below music
```

**What the Learner Sees:**
On significant events (first perfect, combo milestone, miss after long streak), a robotic voice announces it. Adds personality.

---

### Unit 42: Advanced SID - Filters

**Learning Objectives:**
- Understand SID filter architecture
- Use filter for sound design
- Create sweep effects
- Tie filter to gameplay

**Concepts Introduced:**
- Low-pass, band-pass, high-pass
- Filter cutoff and resonance
- Sweep automation
- Filter as expression

**Code Written:**
```
- Configure SID filter
- Filter sweep on perfect hits
- Filter linked to combo (brighter at high combo)
- Muffled sound when health low
```

**What the Learner Sees:**
Sound becomes richer. Perfects have a sweep effect. High combos sound brighter. Low health sounds muffled. The SID is more expressive.

---

### Unit 43: Sound Effects Layer

**Learning Objectives:**
- Design complete SFX set
- Mix effects with music
- Cover all interactions
- Consistent audio design

**Concepts Introduced:**
- SFX inventory
- Voice allocation for SFX
- Mix balance
- Audio feedback completeness

**Code Written:**
```
- Menu sounds (select, confirm, back)
- UI sounds (pause, unpause)
- Feedback sounds (all refined)
- Victory/failure jingles
- All sounds balanced in mix
```

**What the Learner Sees:**
Every interaction has appropriate sound. Menus blip, confirmations click, victory plays a fanfare. Complete audio experience.

---

### Unit 44: Results Screen Polish

**Learning Objectives:**
- Create satisfying results display
- Animate score reveal
- Show achievements
- Celebrate success

**Concepts Introduced:**
- Score count-up animation
- Star rating system
- New high score celebration
- Detailed breakdown

**Code Written:**
```
- Animated score count (ticks up)
- Star rating (1-5 based on performance)
- "NEW HIGH SCORE" flash
- Detailed stats breakdown
- Continue options clear
```

**What the Learner Sees:**
Results screen is an event - score ticks up, stars appear, new records celebrated. It feels like an achievement even on modest scores.

---

### Unit 45: High Score Table

**Learning Objectives:**
- Implement persistent high scores
- Create name entry system
- Display leaderboard
- Rank scores correctly

**Concepts Introduced:**
- High score data structure
- Name entry UI
- Score insertion/sorting
- Display formatting

**Code Written:**
```
- high_scores: array of 10 entries
- Name entry: letter selection system
- Insert new score in sorted position
- Display formatted table
- Highlight new entry
```

**What the Learner Sees:**
High score table shows top 10 with names. Beating a score prompts name entry. New entries highlighted. A reason to replay.

---

### Unit 46: Options Screen

**Learning Objectives:**
- Create options menu
- Implement configurable settings
- Save preferences
- Sound test feature

**Concepts Introduced:**
- Settings persistence
- Toggle and slider UI
- Sound test mode
- User preferences

**Code Written:**
```
- Options menu structure
- Difficulty default setting
- Sound/music volume controls
- Control scheme selection
- Sound test (preview all songs)
```

**What the Learner Sees:**
Options screen allows customisation: difficulty, volume, controls. Sound test lets players preview songs. Player has control.

---

### Unit 47: Pause Functionality

**Learning Objectives:**
- Implement mid-game pause
- Handle pause state correctly
- Provide pause menu
- Resume cleanly

**Concepts Introduced:**
- Game state preservation
- Pause overlay
- Music pause/resume
- Countdown resume

**Code Written:**
```
- Pause on P key or fire (configurable)
- Pause menu: Resume, Restart, Quit
- Music pauses (not stops)
- 3-2-1 countdown on resume
- Full state preserved
```

**What the Learner Sees:**
Pressing pause freezes game with overlay. Menu offers options. Resuming has countdown to prepare. Professional pause system.

---

### Unit 48: Polish Pass

**Learning Objectives:**
- Playtest complete game
- Fix visual inconsistencies
- Tune final balance
- Document polish notes

**Concepts Introduced:**
- Polish playtest methodology
- Detail attention
- Final tuning
- Quality bar

**Code Written:**
```
- Fix any visual glitches found
- Tighten timing feel
- Adjust colours for CRT
- Final difficulty balance
- Performance verification
```

**What the Learner Sees:**
Subtle improvements throughout. Everything feels slightly tighter, cleaner, more polished. The 90% to 100% quality jump.

**Phase 3 Checkpoint:**
The game looks and sounds professional. Every interaction has feedback. Menus are polished, effects are satisfying, audio is complete. It feels like a commercial product.

---

## Phase 4: Mastery (Units 49-64)

*Goal: Commercial quality finish. Optimisation, advanced techniques, and professional packaging.*

*By the end of this phase, the game is truly complete: optimised, feature-rich, and ready for distribution. The learner has skills matching professional C64 developers.*

---

### Unit 49: Code Review and Architecture

**Learning Objectives:**
- Review complete codebase
- Identify architectural improvements
- Document code structure
- Plan optimisation targets

**Concepts Introduced:**
- Code review practices
- Technical debt identification
- Documentation standards
- Optimisation planning

**Code Written:**
```
- Full code review with notes
- Document memory map
- Identify hot paths for optimisation
- Clean up naming inconsistencies
- Add code comments where needed
```

**What the Learner Sees:**
No visible change, but codebase is cleaner. Comments explain complex sections. Architecture documented.

---

### Unit 50: Memory Optimisation

**Learning Objectives:**
- Reduce memory footprint
- Compress data efficiently
- Remove redundant code
- Free RAM for future use

**Concepts Introduced:**
- Data compression techniques
- Dead code elimination
- Memory layout optimisation
- RAM budgeting

**Code Written:**
```
- Compress song data
- Optimize character set (remove unused)
- Eliminate dead code paths
- Consolidate redundant routines
- Document final memory map
```

**What the Learner Sees:**
Same game, smaller size. More RAM free. Important for distribution.

---

### Unit 51: CPU Optimisation - Hot Paths

**Learning Objectives:**
- Profile code performance
- Optimise critical loops
- Reduce cycle counts
- Maintain headroom

**Concepts Introduced:**
- Profiling techniques
- Cycle counting
- Loop unrolling
- Lookup tables vs calculation

**Code Written:**
```
- Identify hot loops (note update, hit detection)
- Unroll critical loops
- Replace calculations with lookups
- Verify cycle counts
- Document performance budget
```

**What the Learner Sees:**
Game feels slightly smoother. More room for effects. Professional optimisation practice.

---

### Unit 52: Stable Raster Timing

**Learning Objectives:**
- Achieve perfect raster stability
- Handle worst-case scenarios
- Eliminate all tearing
- Professional visual quality

**Concepts Introduced:**
- Double-buffering concepts
- Raster timing edge cases
- Worst-case budgeting
- Visual polish standard

**Code Written:**
```
- Verify raster sync under load
- Handle many-note scenarios
- Test all songs at all difficulties
- Fix any remaining tearing
- Document timing budget
```

**What the Learner Sees:**
Rock-solid visuals. No tearing ever, even at peak note density. Professional quality.

---

### Unit 53: Advanced SID - Multi-Speed

**Learning Objectives:**
- Update SID faster than frame rate
- Create richer sound
- Implement per-frame effects
- Professional audio quality

**Concepts Introduced:**
- Multi-speed SID updates
- Timer interrupt for audio
- Sub-frame sound changes
- Professional sound design

**Code Written:**
```
- Timer interrupt for SID (2x per frame)
- More detailed envelope shapes
- Vibrato effect (pitch wobble)
- Pitch slides between notes
- Professional SID sound quality
```

**What the Learner Sees:**
Music sounds noticeably richer. Notes have subtle life. Professional SID audio.

---

### Unit 54: Advanced SID - Ring Modulation

**Learning Objectives:**
- Understand ring modulation
- Create metallic and bell tones
- Use oscillator sync
- Expand sonic palette

**Concepts Introduced:**
- Ring modulation theory
- Sync oscillators
- Bell and metallic sounds
- Creative sound design

**Code Written:**
```
- Ring mod for bell sounds
- Sync for hard-edged tones
- Use in specific songs (Song 5)
- New SFX using ring mod
- Full SID capability demonstrated
```

**What the Learner Sees:**
New sounds not possible before. Metallic hits, bell tones, complex timbres. The SID's full potential.

---

### Unit 55: Sprite Multiplexing Introduction

**Learning Objectives:**
- Understand why 8 sprites isn't enough
- Implement basic multiplexing
- More visual effects possible
- Professional effect quality

**Concepts Introduced:**
- Sprite multiplexing concept
- Raster interrupt for sprites
- Sorted sprite lists
- More than 8 sprites on screen

**Code Written:**
```
- Basic sprite multiplexer
- More simultaneous effect sprites
- Perfect hit creates multiple bursts
- Combo effects more elaborate
- Up to 16 sprites visible
```

**What the Learner Sees:**
More visual effects than seemed possible. Multiple simultaneous explosions. Professional effect density.

---

### Unit 56: Loading Screen

**Learning Objectives:**
- Create professional load experience
- Design loading screen
- Loading music/animation
- Set expectations

**Concepts Introduced:**
- Load-time experience
- Loading screen design
- Progress indication
- First impression

**Code Written:**
```
- Loading screen image
- Loading music (short loop)
- Simple animation during load
- Progress bar if possible
- Professional first impression
```

**What the Learner Sees:**
Loading isn't blank screen anymore. Art, music, animation. Professional presentation.

---

### Unit 57: Tape/Disk Optimisation

**Learning Objectives:**
- Understand storage media
- Optimise load time
- Implement save functionality
- Professional distribution

**Concepts Introduced:**
- Disk vs tape trade-offs
- File organisation
- Save routines
- Distribution formats

**Code Written:**
```
- Optimise file layout for disk
- Implement high score save/load
- Test on real hardware (if possible)
- Create distribution files
- Professional save system
```

**What the Learner Sees:**
High scores persist across sessions. Loads faster. Ready for real distribution.

---

### Unit 58: Two Player Mode

**Learning Objectives:**
- Design two player experience
- Handle dual input
- Create competitive mode
- Expand replayability

**Concepts Introduced:**
- Multiplayer design
- Input mapping for two
- Screen sharing strategies
- Competitive balance

**Code Written:**
```
- Two player mode option
- Split input (keyboard + joystick)
- Shared screen, dual tracks
- Competitive scoring
- Winner determination
```

**What the Learner Sees:**
Two players can compete on same song. Adds social dimension. Significant replay value.

---

### Unit 59: Two Player Polish

**Learning Objectives:**
- Complete two player experience
- Balance for fairness
- Polish multiplayer presentation
- Multiplayer attract mode

**Concepts Introduced:**
- Multiplayer balance
- Winner/loser presentation
- Fairness considerations
- Multiplayer polish

**Code Written:**
```
- Winner celebration
- Loser commiseration
- Balanced scoring for two
- Two player attract mode
- Complete multiplayer experience
```

**What the Learner Sees:**
Two player mode feels complete. Clear winner/loser, fair competition, polished presentation.

---

### Unit 60: Final Song - The Showcase

**Learning Objectives:**
- Compose ultimate demonstration
- Use every SID technique
- Create memorable finale
- Reward completion

**Concepts Introduced:**
- Showcase composition
- All techniques combined
- Hidden content reward
- Memorable experience

**Code Written:**
```
- Song 6: hidden final song
- Unlocked by completing all songs on Hard
- 3+ minutes, uses all SID features
- Most challenging and rewarding
- Technical showcase
```

**What the Learner Sees:**
Completing the game on Hard unlocks a secret final song. It's the ultimate challenge and uses every technique. A reward for mastery.

---

### Unit 61: Credits Sequence

**Learning Objectives:**
- Create professional credits
- Acknowledge work done
- Provide closure
- Original credit music

**Concepts Introduced:**
- Credits scroll technique
- Attribution standards
- Closure experience
- Credit music

**Code Written:**
```
- Scrolling credits screen
- Attribution (learner's name!)
- Original credits music
- Unlocked after any completion
- Professional ending
```

**What the Learner Sees:**
Completing the game shows proper credits. The learner's name is in a game they built. Satisfying closure.

---

### Unit 62: Bug Hunt and Edge Cases

**Learning Objectives:**
- Systematic bug testing
- Edge case handling
- Defensive programming
- Quality assurance

**Concepts Introduced:**
- Bug hunt methodology
- Edge case identification
- Defensive code practices
- QA process

**Code Written:**
```
- Test all paths systematically
- Fix edge cases (key mashing, etc.)
- Add defensive checks
- Memory boundary verification
- Document all issues found/fixed
```

**What the Learner Sees:**
No visible change if bugs were minor. Confidence in stability. Professional quality.

---

### Unit 63: Final Playtest

**Learning Objectives:**
- Fresh perspective playtest
- Final tuning opportunity
- Help text if needed
- Release candidate

**Concepts Introduced:**
- Release candidate concept
- Fresh eyes testing
- Final adjustments
- Sign-off process

**Code Written:**
```
- External playtest if possible
- Tutorial/help if needed
- Final difficulty tweaks
- Any last polish
- Declare release candidate
```

**What the Learner Sees:**
Final version. Everything works. Ready for release.

---

### Unit 64: Packaging and Distribution

**Learning Objectives:**
- Create distribution package
- Document the game
- Archive final build
- Prepare for release

**Concepts Introduced:**
- Distribution formats (D64, TAP, PRG)
- Documentation writing
- Archive practices
- Release process

**Code Written:**
```
- Create D64 disk image
- Create TAP tape image
- Write instruction card
- Box art concept (description)
- Final archive of all source
```

**What the Learner Sees:**
Distributable game files ready to share. Documentation explains how to play. A complete commercial-quality product.

**Phase 4 Checkpoint:**
The game is complete. Optimised, polished, feature-rich, and professionally packaged. It could have sold for £9.99 in 1986. The learner has built a commercial-quality game and learned skills matching professional C64 developers.

---

## Skills Mastery Summary

By completing all 64 units, learners have demonstrated mastery of:

### SID Chip
- All three voices and waveforms
- ADSR envelopes
- Filters (low/band/high pass)
- Ring modulation and sync
- Multi-speed playback
- Voice synthesis

### 6510 Assembly
- Memory architecture
- Raster timing and interrupts
- Keyboard and joystick input
- Data structures
- Optimisation techniques
- Clean code organisation

### Game Development
- Game loop structure
- State machine patterns
- Collision detection
- Scoring and progression systems
- Save/load functionality
- Two player implementation

### Professional Skills
- Playtesting methodology
- Polish and juice design
- Performance optimisation
- Distribution packaging
- Quality assurance

---

## Comparison: 16 Units vs 64 Units

| Aspect | 16-Unit Version | 64-Unit Version |
|--------|-----------------|-----------------|
| Songs | 1 | 6 (5 + secret) + endless |
| Difficulties | 1 | 3 + practice mode |
| Modes | Play only | Career, Practice, Endless, 2P |
| SID Usage | Basic voices | Full: filters, ring mod, multi-speed |
| Visuals | Static | Animated, effects, raster tricks |
| Polish | Minimal | Title, attract, credits, options |
| Save | None | High scores persist |
| Distribution | PRG file | Full package with docs |
| Commercial viable? | No | Yes |
| Time investment | 16-32 hours | 64-128 hours |

---

## Version History

- **2.0 (2026-01-12):** Complete restructure following "scaffold first, explain later" approach. Interactive from Unit 1. Visual+audio output from first moment. Theory (Unit 3) follows experience.
- **1.0 (2025-01-07):** Initial 64-unit outline (theory-first approach, blank screens in Units 1-4, interactivity at Unit 11).
