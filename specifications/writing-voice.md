# Writing Voice

The editorial voice across all Code198x content. Formal principles are in [content-creation-workflow.md](content-creation-workflow.md); this captures the lived experience of applying them.

## The voice

**Magazine-class, not academic.** Specifically: the British 80s gaming press — *Crash*, *Zzap!64*, *Your Sinclair*, *ACE*, *The One*, *Computer + Video Games*. Warm, technical, opinionated, sometimes funny, written by enthusiasts for enthusiasts. Lloyd Mangram's tone, not a textbook author's.

The reader is curious, possibly young, possibly returning to coding after years away. Trust them to be smart. Don't assume they already know what a register is. Don't talk down to them either. It's the same balance the magazines hit: a 14-year-old in 1986 could read *Crash* and learn what a sprite was without feeling lectured.

**Never:** "highbrow academic bullshit" (per the brief). No passive voice walls of text. No "as we discussed in the previous chapter." No tutorial-mill robotic prose.

**Always:** the reader is a participant, not an audience. We're explaining something we love to someone who might love it too.

## Core qualities

- **Hardware intimacy**: show the register, the memory address, the signal. Don't hide behind abstractions.
- **Game-first pedagogy**: every concept taught through building a game. No isolated theory.
- **Honest about difficulty**: don't pretend it's easy. Acknowledge the learning curve.
- **Encouraging experimentation**: "try changing this value and see what happens" is a legitimate teaching tool.

## Language rules

- **British English** throughout: colour, learnt, centre, behaviour
- **Exception**: "program" not "programme" (for computer programs)
- Enforced by the `check-spelling` skill, which scans for American spellings. Run it before publishing.
- **No nostalgia tourism**: focus on skills and hardware, not "remember when" feelings
- **No modern engine references**: zero tolerance for Unity, Unreal, Godot, GameMaker

## Anti-patterns

- Dense academic walls of text
- Slick startup aesthetic
- Gaudy vaporwave
- "Remember when" nostalgia framing
- Condescending simplification ("don't worry about this for now")
- Tutorial-mill robotic prose ("In this lesson, we will learn how to...")
- Over-explaining what the reader can see for themselves
- Hedging ("might possibly perhaps consider...")

## Reference reads

When stuck on a section, read a paragraph of:

- A *Crash* game review — the rhythm of opinion + technical detail
- An Oli Frey-era *Crash* hardware feature — explaining a chip without dumbing it down
- A *Zzap!64* type-in introduction — warm but expectant
- An old Usborne computer book — the "you can do this" framing for kids and adults alike

If your sentence sounds like a Wikipedia article, rewrite it.

## Tonal calibration by track

- **Assembly tracks** — *Crash* / *Zzap!64* hardware features. Technical, opinionated, treats the chip as a character. Aimed at 16+ year olds and serious returners.
- **BASIC track** — Usborne 1984 confidence-builder, *with* magazine wit. Aimed at kids, beginners, people-who-haven't-coded-in-years. Same voice, gentler ramp. Confidence over depth. (See [spectrum-basic-lineup.md](../decisions/spectrum-basic-lineup.md) for the BASIC scope decisions that drive this calibration.)
- **Foundations** — the gentlest setting in the family, because it is the only shelf whose reader has never written a line of code. Usborne again, but further along that dial than the BASIC track: shorter sentences, one idea to a paragraph, nothing held in the reader's head across a page. There is no machine and no language to be curious about yet, so the interest has to come from the idea itself being clear. Confidence over completeness. **The audience test has two halves, and they pull against each other.** A primary school teacher or a parent with no background could pick a unit up and teach from it in an hour; and an adult reading it alone for themselves never feels talked down to. Simple is not the same as simplified-for-children. The way to satisfy both is to respect the reader's intelligence and assume none of their knowledge: plain words, no baby-talk, no "don't worry, this bit is easy". Natural and approachable, with room for some personality and a joke where one is genuinely there; the line is that the humour never carries the explanation and never makes the reader the butt of it.
- **Vault** — magazine retrospective. Like a *Retro Gamer* feature but tighter. Treats games and people as worth caring about.

### Writing for a reader who has never programmed

Foundations only. The tells that a unit has drifted off this setting:

- **Two ideas in one sentence.** Split it. A subordinate clause after an em dash is usually a second sentence that has not been let go.
- **A metaphor carrying the explanation.** A metaphor can decorate a point already made plainly. It cannot make the point. The reader has nothing to check it against.
- **An aside that is true but not needed here.** Correctness is not a reason to include something. Anything that does not serve the unit's one idea is an obstacle, however accurate.
- **Explaining the same thing twice** in different words, in case the first landed badly. Pick the better one.
- **A word the reader would have to look up**, where a shorter one would do.
- **A universal claim about languages, propped up by three examples.** "Every language has a word for X. BASIC says this, Python says that, C says the other." Three examples from one family is not a survey, and this is the sentence a course about what is universal reaches for most readily. Two got through here: every language keeps text and numbers apart (Perl, Tcl, awk, Lua, PHP and JavaScript convert between them freely), and every language has a word for output (assembly has none — you put the bytes where the screen will find them, which is where one arm of this curriculum leads). Say what varies and what does not, or make the claim smaller.
- **The passive voice.** "The ideas are written in pseudocode" hides who is doing it; "we write each idea in pseudocode" does not. The house voice already rules out passive walls of text, but it slips in here more than anywhere else, where the writing keeps reaching for the neutral and impersonal. Name the actor: the computer, the program, you, we.
- **A narrator who says "I".** "Take my word for it", "you could have told me". The voice on this shelf is *we* or nobody; a single "I" in one unit makes it read as a different author, because it was. Two got through in Truth Tables.
- **A count written in words, across a unit boundary.** "Two units from now it saves you a headache" was true until a unit was inserted between them. The renumbering check reads `**Unit N**` and cannot see a number spelt out. Name the unit, `Unit 7`, or say *later* and leave the count out.
- **A punchline ending.** A section that closes on a line whose job is to sound good — "it was special to us", "it does not have opinions". The reader is not here to be impressed by the prose. Close on the point, or on what to do next.

The test is the reader, not the word count, but the counts are a useful smell: a unit here reads closer to 400 words than 800. If it is much longer, it is usually carrying an aside or saying something twice.

## Three quality criteria

Every unit must meet all three:

1. **It Works Fast** — immediate visible/audible feedback, creates something impressive
2. **It's Real** — hardware connection visible, honest about limitations
3. **It's Clear** — focused concept, builds logically, invites experimentation

## Visual identity

Platform-specific branding:
- **C64**: blue
- **Spectrum**: rainbow
- **NES**: red
- **Amiga**: orange
