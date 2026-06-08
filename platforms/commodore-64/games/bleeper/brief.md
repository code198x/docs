# Bleeper — Brief

**Title (working):** Bleeper
**System / Track:** Commodore 64 / BASIC
**Position:** Volume 1, Game 5 of 8
**Headline concept:** Memory — hold and reproduce a growing sequence
**Embedded concept:** Escalation — each round raises the load
**Topics:** 6–7 topics, ~8–10 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach that an array can store and grow an ordered sequence, that the SID at 54272 speaks a note when you POKE its registers, and that `GET` reads the player's echo a key at a time so it can be compared against the stored pattern — so the learner arrives at Safe Cracker with arrays-as-data, the SID as a voice, and compare-the-echo input as working tools.

---

## 2. Classic Ancestors

- **Simon** (Milton Bradley / Ralph Baer, 1978) — the electronic memory game. Four coloured pads, each with its own tone. The device plays a growing sequence; the player repeats it. The mechanic: short-term memory tested against an ever-lengthening chain.
- **Simon type-ins** — published in nearly every home-computer magazine. The universal first "real game" for BASIC: colour, sound, input, and a difficulty curve built into the mechanic. On the C64 the type-in earned its keep by reaching the SID directly through POKE.

---

## 3. Core Experience

Four colour panels. The C64 plays a tone-and-flash sequence; you repeat it from the keyboard. Each round it adds one more step. How far can you hold? Short sessions, instant restart, and the pull to beat the length you held last time.

---

## 4. Visual Direction

- Four colour panels — solid blocks POKEd into screen RAM (1024) with their colour set in colour RAM (55296). Red, cyan, green, yellow stay distinct on a PAL C64.
- The active panel **flashes** during playback: brighten or swap its colour-RAM value for a beat, then restore it. The flash and the tone fire together so the panel "speaks."
- Colour is identity, not decoration — each panel's colour is the thing the player memorises alongside its pitch.
- When the player echoes, flash the panel under their key too, so their input is mirrored on screen.
- Magazine-screenshot test: a single frame on a Commodore-magazine listing page — four bold colour blocks on the blue C64 screen, one lit brighter than the rest mid-sequence, a short score line above. Unmistakably "type this in and play it tonight."

---

## 5. Audio Direction

This is the audio-forward game of the volume — the one where the SID earns its keep.

- **A distinct tone per panel.** Four pitches, one per colour, played by POKEing the SID registers from 54272 — set the voice frequency, the waveform/ADSR, gate on, gate off. A single voice is plenty; the player learns the four notes by ear and can replay the sequence on sound alone.
- **The sequence plays back** through the SID as each panel flashes — tone and flash locked together.
- **A failure tone.** A low, harsh note when the echo is wrong. Brief and clear, not punishing.
- Deliberately silent between rounds — the four panel tones plus the failure note are the whole audio vocabulary. Three-voice SID music is an anti-goal; that's a later game's job.

---

## 6. Anti-goals

- No three-voice SID music — one voice, four notes, a failure tone. Composition belongs to a later volume, not a primer-adjacent game.
- No high-score table, no SAVE/LOAD of bests — the sequence length you reach *is* the score, shown at game over. The escalation is the depth.
- No difficulty settings — the sequence grows by one each round, calibrated to human short-term memory (~7 items). No configuration to tune.
- No sprites, no custom characters — panels are POKEd colour blocks in screen and colour RAM.
- Keep it small — a Simon mechanic needs reusable panel-draw and flash-and-tone code, but the finished game stays a tight type-in, not a sprawling listing.

---

## 7. Topic Progression

1. **Light and bleep one panel.** POKE a block of screen RAM (1024) to draw one panel and set its colour in colour RAM (55296). Brighten it for a beat with a `FOR` delay, then restore it — the flash. Set up the SID at 54272 (volume, ADSR, waveform) and play one note: POKE the frequency, gate on, hold, gate off. The flash and the tone fire together. **New:** POKEing a colour block, the flash via colour-RAM swap, the SID note (54272…). **Program:** ~16 lines. **Polish beat:** how long should the flash and tone last? Long enough to register, short enough to feel snappy.

2. **Four panels, four notes.** Draw all four panels across the screen, each its own colour. Give each a distinct SID pitch. A short routine takes a panel number (1–4) and does the flash-and-tone for that panel — the reusable heart of the game, called with `GOSUB`. **New:** `GOSUB`/`RETURN` for a reusable flash-and-tone block, a per-panel note table. **Program:** ~24 lines. **Polish beat:** which four pitches? Spread them so the ear tells them apart — a pleasing set of intervals, not four notes crammed together.

3. **A fixed three-step sequence.** Play a hard-coded sequence of three panels — call the flash-and-tone routine three times in order, with a pause between each. The machine performs; the player just watches and listens. **New:** sequencing calls with timed pauses, reading a fixed list of steps. **Program:** ~26 lines. **Polish beat:** the gap between steps — too tight and the steps blur, too slack and it drags. Find the rhythm.

4. **Store it in an array.** Move the sequence into a numeric array (`DIM S(N)`). A `FOR` loop walks the array and flashes-and-bleeps the panel each slot names. The sequence is now *data*, not code — the program plays whatever the array holds. **New:** numeric arrays as an ordered sequence, a playback `FOR` loop driven by array contents. **Program:** ~28 lines. **Polish beat:** watch a longer stored sequence play back cleanly — the playback should feel identical whether it's three steps or ten.

5. **Grow it by one each round.** Each round, append a new random panel to the array: `S(N) = INT(RND(1)*4)+1`, bump the length, replay the whole sequence from the start. The chain lengthens by one every round, exactly like the toy. **New:** `RND` to pick a panel, growing the array by one each round, the round loop. **Program:** ~30 lines. **Polish beat:** watch it get longer. At what length does holding it in your head start to slip?

6. **Read the player's echo.** After the sequence plays, read the player's repeat a key at a time with `GET` — wait for a key, map it to a panel (keys 1–4), flash-and-bleep that panel so the input is mirrored. Compare each press to the stored array. A correct echo of the whole sequence advances to the next round; a wrong press ends it with the failure tone. **New:** `GET` in a wait loop, mapping keys to panels, comparing input against the array. **Program:** ~34 lines. **Polish beat:** flash the panel as the player presses it — it should feel like playing an instrument, their echo answering the machine's.

7. **Score and escalate.** On a wrong press, clear the panels and show the length reached: `PRINT "YOU HELD "; N-1` — the sequence length is the score. Add a "PRESS A KEY TO PLAY AGAIN" prompt that loops back to a fresh sequence. Tidy the title and number the panels (1–4) so the player knows which key is which. The learner now owns a complete C64 Simon — the SID, an array, and live input working together. **New:** length-as-score, the game-over and replay flow, a titled screen with numbered panels. **Program:** ~36 lines. **Polish beat:** is the game-over respectful? "YOU HELD 8" acknowledges the achievement; "WRONG" doesn't.

---

## 8. Ship Test

- [ ] Every topic's code runs on a PAL C64 (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] One new BASIC concept per topic — no topic introduces two major ideas
- [ ] Gradual progression — a reader can follow from topic 1 to final topic without gaps
- [ ] Four panels are visually distinct — identifiable from across the room
- [ ] The flash is unmistakable — the active panel reads as lit against the others
- [ ] Each panel has a distinct, memorable SID tone; the failure tone is unmistakable
- [ ] Sequence playback is timed right — quick enough to be exciting, slow enough to follow
- [ ] Player echo via `GET` validates correctly — right presses continue, a wrong press ends the round
- [ ] Difficulty scales naturally — the sequence grows by one each round toward the ~7-item memory limit
- [ ] British English throughout (exception: "program")
- [ ] Screenshots show the actual running program, not mockups
- [ ] Code samples in `/code-samples/`, not inline
- [ ] Magazine voice — warm, technical, never condescending

---

## 9. Pattern Library Extractions

- **basic** — array-as-sequence: `DIM S(N)`, append with `S(N)=INT(RND(1)*4)+1`, replay with a `FOR` loop over the array. A numeric array used as an ordered data structure. Used in every game that records a history or replays a pattern.
- **framework** — `GOSUB`/`RETURN` subroutines: a single flash-and-tone block called for any panel, the C64's tool for avoiding code duplication. Cross-platform concept.
- **audio** — distinct-tone-per-object via the SID: each panel POKEs its own frequency into 54272, building an audio vocabulary the player memorises. The pattern behind every game where sound identifies an object or action — and the first real use of the SID in the volume.
- **input** — compare-the-echo with `GET`: read input a key at a time and validate each press against stored data. The pattern behind every game that checks the player's response against an expected sequence.
- **rendering** — colour-RAM flash: brighten or swap a block's colour-RAM value for a beat, then restore it. The simplest C64 animation — change a property briefly, then revert. Cross-platform concept.

---

## 10. Vault Tie-ins

- **Simon** (Milton Bradley / Ralph Baer, 1978) — the electronic memory game as direct ancestor.
- **Ralph Baer** — inventor of Simon (and the Brown Box / Magnavox Odyssey). Person entry.
- **The SID 6581/8580** — the chip that gave the C64 its voice; the hardware this game first reaches through POKE at 54272.
- **Short-term memory in game design** — the principle that ~7 items is the human limit, and games calibrated to it feel challenging but fair.
