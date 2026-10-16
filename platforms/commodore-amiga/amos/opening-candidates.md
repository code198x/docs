# AMOS opening game candidates

**Status: source comparison and proposals for discussion.** Recommend a small
take-away game for the first AMOS prototype. Its rules create a choice with one
changing quantity, and the learner can build it before learning moving graphics,
arrays or a computer opponent. The game is not yet selected or implemented.

The [course brief](course-brief.md) describes its proposed teaching stages. The
full AMOS track can grow towards substantial games; this review chooses a gentle
entry rather than a ceiling for the language or machine.

## Comparison scope

Inspected the eight game-track catalogues for the four current systems at website
revision `7412570891a79c0485b3d894cefd4cf74eb924eb`: Spectrum BASIC and assembly,
C64 BASIC and assembly, Amiga AMOS, Blitz and assembly, and NES assembly. Read
the authored overview bodies for Meteor Storm, Bright Spark, Volley, Brick Bash,
Three in a Row, Bleeper, Reflex, Safe Cracker and Flock, plus the relevant retained
briefs and the [Spectrum remaining-course review](../../sinclair-zx-spectrum/basic/course-review.md).

Catalogue proposals expose possible overlap, not agreed future games. An authored
overview establishes its described experience, not execution or learner success.
The recommendation below is a bounded editorial judgement, not proof that no
similar game exists anywhere in the family.

Catalogue sources at the inspected revision:

- [Spectrum BASIC](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/modules/sinclair-zx-spectrum/basic.yaml)
  and [assembly](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/modules/sinclair-zx-spectrum/assembly.yaml).
- [C64 BASIC](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/modules/commodore-64/basic.yaml)
  and [assembly](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/modules/commodore-64/assembly.yaml).
- [Amiga AMOS](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/modules/commodore-amiga/amos.yaml),
  [Blitz](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/modules/commodore-amiga/blitz.yaml)
  and [assembly](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/modules/commodore-amiga/assembly.yaml).
- [NES assembly](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/modules/nintendo-entertainment-system/assembly.yaml).

## Playing experiences already represented

| Family | Positive comparison and status | Consequence for the opening |
| --- | --- | --- |
| Steer under moving objects to collect or avoid them | Authored [Meteor Storm](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/curriculum/sinclair-zx-spectrum/assembly/meteor-storm/index.mdx); inherited AMOS Star Catcher proposal | A falling-object catcher is too close to the existing player activity, even with different art and simpler rules. |
| Return a ball with a paddle | Authored [Volley](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/curriculum/sinclair-zx-spectrum/basic/volley/index.mdx) and [Brick Bash](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/curriculum/sinclair-zx-spectrum/basic/brick-bash/index.mdx); several inherited bat-and-ball proposals | Do not make another paddle game the default AMOS or Blitz opening. |
| Remember and repeat a sequence | Authored [Bright Spark](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/curriculum/sinclair-zx-spectrum/basic/bright-spark/index.mdx) and [Bleeper](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/curriculum/commodore-64/basic/bleeper/index.mdx) | Changing panels, sounds or language would repeat the central game. |
| Guess a hidden value from clues | Authored C64 Safe Cracker and Spectrum Meet BASIC; [Locksmith](../../sinclair-zx-spectrum/games/locksmith/brief.md) uses exact/other-position code clues | Avoid another higher/lower or code-guessing opening. |
| React quickly to a signal | Authored [C64 Reflex](https://github.com/code198x/website/blob/7412570891a79c0485b3d894cefd4cf74eb924eb/src/content/curriculum/commodore-64/basic/reflex/index.mdx) | A reaction test would revisit an existing activity and introduce clock/input measurement. |
| Cross moving lanes | Authored Flock and Quickstep | Avoid a crossing game even though the systems and rendering differ. |
| Place marks to complete a line | Authored [Three in a Row](../../sinclair-zx-spectrum/games/three-in-a-row/brief.md) | A smaller board does not make the proposed activity distinct. |
| Navigate rooms and use objects | Authored Caverns and Shadowkeep; inherited adventure proposals include Thornwood Manor and Dungeon Doors | A one-room point-and-click adventure could differ in play, but object state, selection and puzzle dependencies make it a poor way to simplify this opening. |
| Manipulate a board | Authored Crates; inherited Gridlock descriptions and the proposed Blitz switch puzzle | A shared grid alone is not duplication. Compare the actual move and goal; keep the switch puzzle separate from the AMOS recommendation. |

Existing overlap is not an instruction to remove those games. The agreed default
guides new choices and later reviews; an explicitly chosen revisit can still
serve a useful comparison.

## Shortlist

| Candidate | Complete small game | Initial teaching load | Distinct activity and main risk |
| --- | --- | --- | --- |
| Take-away, recommended | Start with seven counters. Two local players alternate taking one or two; taking the last wins. Offer replay and exit. | Text output, one remaining-count variable, choice input, subtraction, conditions, repetition and a turn value, introduced separately | Players leave a position for each other rather than chase, remember signals or infer a secret. It shares turn-taking with Three in a Row but needs no board or line evaluator. The strategy may become exhausted quickly. |
| Three-choice contest | Choose one of three symbols against a computer choice; each symbol beats one other and draws with itself | Three valid inputs, computer selection, result conditions and replay | Simultaneous-choice prediction differs from the inspected games. Explaining random selection and several result branches could dominate the first project; choosing alone offers limited depth. |
| Bank-or-risk game | Roll to add to a round total; choose to bank or roll again; a designated result loses the unbanked total | Random selection, current total, banked total, decisions, repetition and ending | Choosing when to stop differs from the authored dice-frequency experiments. More interacting quantities make it a better later candidate than the take-away opening. |

Novelty is not the objective. A familiar game can still be a distinct choice for
this curriculum. Repeating an idea from elsewhere requires a stated reason;
repeating a programming concept through a different game is expected.

## Recommended first scope

Use one pile, seven counters, choices 1 or 2, two local players and the last-taker
win rule. Show the active player, remaining count and accepted move in text.
Reject an unavailable take without changing the count or turn. Retain the winner
until a new round or exit is chosen. A learner working alone can enter both
players' choices to investigate the game; a computer opponent can be considered
after the basic game is understood.

Start with text and add a small repeated counter picture when counted drawing
has a purpose. Do not begin with pointer hitboxes, Bobs, animation, collision,
multiple piles or an optimal opponent. Teach useful presentation and a short
result cue in manageable stages rather than making them prerequisites for the
first playable version.

Before committing to lessons, check the exact input and save/reopen route in
AMOS Professional 2.00, play several complete games, and inspect how many new
ideas each stage requires. Check both players taking the last counter, one
counter remaining, an unavailable take, invalid input, repeated actions, replay
and exit. Native execution and human play observations must remain separate
from any claim about a beginner's understanding.

Reject or revise this recommendation if two-player use is unsuitable, the rules
become dull before the teaching is complete, or a trustworthy input route needs
too much explanation. Do not add an opponent or further mechanics solely to
rescue it. Compare the next candidate at the same small scope before increasing
the difficulty. No later AMOS lineup is selected by this recommendation.
