# Oracle — Brief

**Title (working):** Oracle
**System / Track:** Commodore 64 / BASIC
**Position:** Volume 1, Game 2 of 8
**Headline concept:** Chance — the machine surprises you
**Embedded concept:** Suspense — the pause before the reveal
**Topics:** 6 topics, ~6–8 hours
**Constraint position:** period-faithful
**Status:** draft

Format: [`specifications/brief-basic-v1.md`](../../../../specifications/brief-basic-v1.md)

---

## 1. Pedagogical Role

Teach randomness as a game ingredient: `RND` chooses, a string array (`DIM A$`) holds the choices, and `RND` used as an *index* turns a number into an authored answer — the selection machinery that gives every later game in the volume its variety. The learner leaves knowing that "the computer chose" means "I wrote the choices and the machine picked one" -- and that a deliberate pause before a result is a thing you *build*, not a thing that happens.

---

## 2. Classic Ancestors

- **Magic 8-Ball** (Mattel, 1950) — the original fortune-telling toy. Shake it, turn it over, read the answer in the little window. Twenty pre-written responses, picked at random. The whole trick is the illusion of wisdom drawn from a bounded set of answers — exactly what a string array and `RND` do.
- **Fortune-teller type-ins** — a staple of early Commodore magazines and listings books. *Compute!'s Gazette* and dozens of C64 type-ins published variants where the program pretends to know your future and the player pretends to believe it.

---

## 3. Core Experience

Ask the Oracle a yes/no question and press RETURN. The screen settles, a soft tone hums while the machine *thinks* — a deliberate beat of suspense, the colour shifting with its mood — and then the answer arrives. Ask again; the answers vary. Short, silly, and endlessly repeatable — the kind of program you pass around a room.

---

## 4. Visual Direction

- Clear the screen with `PRINT CHR$(147)` before each consultation so the answer gets the screen to itself — no scrollback, no clutter. This is the C64's "home and clear."
- Colour is the Oracle's **mood**, not decoration. The background carries it: `POKE 53281,n` sets the screen colour, and the answer's colour (written into colour RAM, or set with a `CHR$` colour code before the `PRINT`) is chosen to match the *kind* of answer — a calm blue for a "yes", a hot red for a "no", a murky purple for a "maybe". The player reads the mood before they read the words.
- A title — `THE ORACLE` — framed in its own colour at the top, so the screen looks like a place you go to ask a question, not a `READY.` prompt with text under it.
- Magazine-screenshot test: a single C64 listing-page photo — the cleared blue screen, the question echoed at the top, and the Oracle's answer centred and colour-washed below it. It should read, at a glance, as "this program has a mood," the way a *Compute!'s Gazette* type-in screenshot sold its program before you typed a line.

---

## 5. Audio Direction

- **A "thinking" tone.** While the Oracle ponders, hold a soft single voice on the SID (voice 1 at the base of the chip's registers, `54272`): set a low-ish frequency, a gentle waveform, gate it on for the length of the pause, then gate it off. One voice, one quiet hum — the sound that says "something is coming."
- **A tone on the answer.** A single, clearer note when the answer appears — a different pitch from the thinking hum, so the ear hears the switch from *waiting* to *revealed*.
- **Silence around the reveal.** Nothing else makes a sound. Gating the thinking tone *off* a beat before the answer tone fires makes the answer land harder. The quiet is part of the suspense.

---

## 6. Anti-goals

- **No real intelligence.** The Oracle picks from a fixed list. No parsing of the question, no keyword matching — the question is ignored entirely; only the ceremony of asking matters.
- **No scoring, no tracking.** No count of questions asked, no history, no persistent state. Each consultation stands alone.
- **No real-time input.** One question, one answer. No joystick, no live loop, no clock — those arrive in Reflex (Game 3) and Rover (Game 7).
- **No three-voice SID music.** A single thinking tone and a single answer tone. Multi-voice composition belongs to Bleeper and later.
- Keep it small — roughly 20–30 lines of BASIC at the finish. The depth is the *feel* of the pause, not the line count.

---

## 7. Topic Progression

1. **Ask the Oracle.** `INPUT "ASK YOUR QUESTION";Q$` — the machine waits for the player to type. Then `PRINT "THE ORACLE SAYS... YES"`. The answer is always YES. Tiny, but the shape is there: ask, then answer. **New:** reinforcement of `INPUT`/`PRINT` from the primer; `PRINT CHR$(147)` to clear the screen first. **Program:** ~4 lines. **Polish beat:** write the prompt in the Oracle's voice — "SPEAK, MORTAL" feels different from "TYPE YOUR QUESTION."

2. **The Oracle chooses.** Replace the one fixed answer with one of two, picked at random. `R = INT(RND(1)*2)+1`, then `ON R GOTO` two lines — one prints YES, one prints NO. Run it several times: different answers, same question. The learner wrote *both* answers, but the player doesn't know which is coming. That gap is **Chance**. **New:** `RND(1)` for a random number; `ON…GOTO` to branch on it. **Program:** ~8 lines. **Polish beat:** make the two answers feel like opposites with personality — "WITHOUT DOUBT" against "ABSOLUTELY NOT" beats a bare YES/NO.

3. **A list of answers.** Two answers run dry fast. Store many in a string array: `DIM A$(8)`, then fill it — `A$(1)="THE SIGNS POINT TO YES"`, `A$(2)="DO NOT COUNT ON IT"`, and so on. Now pick one with `RND` used as an *index*: `R = INT(RND(1)*8)+1 : PRINT A$(R)`. One `PRINT` line now speaks any of eight answers. The Oracle starts to feel like it has a personality. **New:** string arrays (`DIM A$(N)`); `RND` as an index into an array. **Program:** ~14 lines. **Polish beat:** write at least one answer that makes people laugh — the funny ones are the ones people remember and re-run for.

4. **The Oracle thinks.** The answer appears instantly — too fast for something wise. Add a thinking pause: a delay loop (`FOR T=1 TO 800:NEXT`) with the SID's thinking tone gated on for its duration, then gated off, *then* the answer. The pause builds **suspense** — the embedded concept. The answer means more because you waited for it. **New:** a deliberate timing pause; the SID single voice at `54272` as a "thinking" tone. **Program:** ~20 lines. **Polish beat:** how long should the Oracle think? Too short feels fake, too long feels broken — find the beat where the player leans in.

5. **Mood in colour.** The Oracle should *look* like it feels something. Give each answer a mood — yes / no / maybe — and shift the colour to match before it prints: `POKE 53281,n` for the background, a colour for the answer text. A calm answer comes up blue, a hard "no" comes up red, an uncertain one comes up purple. The player reads the mood before the words. **New:** colour RAM / `POKE 53281` as expression — colour carrying meaning, not decoration. **Program:** ~26 lines. **Polish beat:** does the colour *agree* with the answer? A cheerful colour under a grim answer breaks the spell — match the wash to the words.

6. **Ask again.** Right now the program runs once and stops; the player has to RUN it again. Close the loop: after the answer, `PRINT CHR$(147)` and `GOTO` back to the question. One sitting, many questions — the Oracle becomes something you *consult*, not something you run. **New:** the ask-again loop with `GOTO`. **Program:** ~28–30 lines. **Polish beat:** clear the screen on the way round so each consultation starts clean — the ceremony resets, and the next answer gets the stage to itself.

---

## 8. Ship Test

- [ ] Every topic's code runs on a PAL C64 (emulator + real hardware)
- [ ] Every topic produces a working, runnable result
- [ ] One new BASIC concept per topic — no topic introduces two major ideas
- [ ] The `DIM A$` / `RND`-as-index pattern is clear — the learner can add more answers by extending the array
- [ ] The thinking pause and SID tone create genuine suspense (test: does the player lean in before the reveal?)
- [ ] At least 8 answers in the final version, with a mix of yes / no / maybe / funny
- [ ] Colour carries the Oracle's mood — the wash matches the kind of answer, not chosen at random
- [ ] Gradual progression — a reader can follow from topic 1 to the ask-again loop without gaps
- [ ] British English throughout (exception: "program")
- [ ] Screenshots show the actual running program, not mockups
- [ ] Code samples in `/code-samples/`, not inline
- [ ] Magazine voice — warm, technical, never condescending

---

## 9. Pattern Library Extractions

- **basic** — array-driven random selection: `DIM A$(N)`, fill it, then `R = INT(RND(1)*N)+1 : PRINT A$(R)`. The pattern for choosing from a set of authored content with one `PRINT` line. The learner's first encounter with "data structure as a substitute for branching" — the inverse of the Spectrum Oracle's chained-`IF`, and the shape every later game's variety leans on.
- **basic** — the suspense beat: a timed pause with a SID tone before a result. Building anticipation through deliberate timing and sound, used by every game with a moment of revelation (Safe Cracker's crack, Dropzone's touchdown, any result screen).
- **basic** — colour as state: `POKE 53281` and colour RAM chosen to *mean* something (mood here; feedback later in Safe Cracker). The first time colour carries information, not decoration.

---

## 10. Vault Tie-ins

- **Magic 8-Ball** (Mattel, 1950) — the fortune-telling toy as cultural ancestor.
- **Fortune-teller type-ins** — *Compute!'s Gazette* and Commodore listings-book programs in the tradition.
- **Chance and randomness in game design** — the design principle that random selection from authored content creates the *illusion* of intelligence.
- **The SID chip (6581/8580)** — the single-voice "thinking" tone is the learner's first deliberate use of the SID's register block at `54272`, set up for Bleeper's multi-note sequences later in the volume.
