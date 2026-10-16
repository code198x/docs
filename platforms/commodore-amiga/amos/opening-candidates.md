# AMOS opening game candidates

**Status: bank-or-risk opening direction agreed.** Build towards a solo dice
game in which a player approaches a limit, chooses when to bank, and risks losing
the current unbanked total by going over. A short session target gives each
choice a purpose. The [game brief](../games/bank-or-risk/brief.md) defines the
provisional native trial and the [course brief](course-brief.md) places it in a
gentle beginner route.

The full AMOS track can grow towards substantial games. This review chooses an
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
| Take-away, not selected | Two local players remove one or two counters; the last taker wins | Few changing values and no moving graphics or opponent | Its small implementation does not establish a compelling game. The fixed rule can become exhausted quickly and offers too little jeopardy for the intended opening. |
| Three-choice contest | Choose one of three symbols against a computer choice | Validated input, computer selection, result branches and replay | Distinct simultaneous-choice play, but random selection and several branches could dominate the opening. |
| Bank-or-risk, selected direction | Roll towards a visible limit, bank or risk another roll, and meet a short session target | Random selection, addition, comparisons, input, repetition and values with different lifetimes, taught separately | Choosing whether to expose earned points to an increasing risk differs from watching frequencies. A session target must justify the risk; balance and teaching pace require a native trial. |

Novelty is not the objective. A familiar game can still be a distinct choice for
this curriculum. Repeating an idea from elsewhere requires a stated reason;
repeating a programming concept through a different game is expected.

## Selected direction and comparison

The [first-game brief](../games/bank-or-risk/brief.md) provisionally uses one
six-sided die, a limit of 10, five rounds and a target of 30 secured points.
Exactly 10 banks automatically; going over loses that round's unbanked points.
There are no cards, dealer, money or opponent. The Blackjack/Pontoon comparison
concerns the decision to continue near a limit, not an adopted card ruleset.

The nearest inspected activities are the authored Spectrum
[Dice Roller](../../sinclair-zx-spectrum/games/dice-roller/brief.md) and retained
C64 [Tally brief](../../commodore-64/games/tally/brief.md). Those explore counts
and frequencies of die results. They do not ask players to bank an accumulating
total or risk losing it. Shared random-number concepts do not repeat the game.

Increasing risk alone is insufficient if safe play always meets the target.
The [exact rules analysis](../games/bank-or-risk/rules-analysis.md) checks the
provisional target and shows why the current session need can change the choice
at the same round total. The recommended tuning permits recovery after a bust
and compares safe, moderately risky and more aggressive play. Native play must
still judge the balance and whether the decision is fun.

The course starts with a tiny runnable message, saves it early, and introduces
one roll, accumulation and the limit before building a round. Banking and
repetition create a small complete round; later stages add secured score, round
count and target. Presentation and result sound enter through explained stages.
No animation, arrays, collision or computer strategy is needed for this opening.

The game direction is agreed. Numerical balance, native implementation,
replacement lesson boundaries and learner effectiveness remain to be established.
No other game is retired and no later AMOS lineup is selected.
