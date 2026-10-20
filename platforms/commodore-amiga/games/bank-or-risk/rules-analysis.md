# Bank or risk tuning analysis

Recommend a **limit of 10, five rounds and a target of 30** for the first native
trial. It preserves the bank-or-roll game, lets a player recover from an opening
bust, and rewards some risk without making more aggressive play automatically
better. The parameters remain provisional until played in AMOS.

## Method and scope

Run from the documentation repository:

```sh
python3 platforms/commodore-amiga/games/bank-or-risk/rules_check.py
```

Executed with Python 3.14.3 using only the standard library. Exact rational
arithmetic enumerates six equally likely independent outcomes for each roll.
Cached states hold rounds remaining, points still needed and current total.
Positive die values bound the recursion; banking, reaching the limit or busting
consumes a round. A target-aware policy chooses the action with the greater
probability of eventually reaching the target.

Three fixed policies bank when the total first reaches a threshold. The safe
threshold is five below the limit: 16 at limit 21, 7 at limit 12 and 5 at limit
10. Before reaching that threshold, a roll cannot bust. The moderate comparison
banks one point higher; the aggressive comparison banks two points higher.
These labels describe the tested policies, not player skill.

Each fixed policy is independently checked by propagating probability forward
through a single round's possible totals, then combining complete round-score
distributions. This path neither calls the outcome classifier nor uses the
target solver's early success/failure pruning. All 21 setting/policy comparisons
agree exactly; all round and session distributions retain probability one.

The target-aware maximum is a mathematical benchmark. The table is not a set of
observed player win rates, a fairness test of AMOS's generator, or evidence that
the game is fun. Percentages are rounded to six decimal places. No Monte Carlo
sampling or native language execution is used.

## Parameter comparison

The recovery column starts from an opening round that has scored zero: secured
score zero and one fewer round available. It reports the best achievable chance
from that state, not the chance that a bust happens or a guarantee of recovery.

| Limit / rounds / target | Safe policy | Moderate policy | Target-aware maximum | Recovery after opening bust |
| --- | --- | --- | --- | --- |
| 21 / 5 / 90 | 34.893448% | 65.713872% | 76.795746% | 0% |
| 21 / 5 / 82 | 98.993951% | 78.316024% | 99.794458% | 5.425918% |
| 21 / 10 / 175 | 66.182465% | 61.832934% | 88.354810% | 12.194311% |
| 12 / 5 / 42 | 76.873255% | 81.939145% | 93.006857% | 32.886704% |
| **10 / 5 / 30** | **80.630706%** | **86.836201%** | **95.320953%** | **60.126571%** |
| 10 / 5 / 32 | 58.463120% | 79.426441% | 89.684813% | 44.604766% |
| 10 / 5 / 35 | 25.369481% | 60.034647% | 74.287406% | 21.941439% |

Reducing the 21-limit target to 82 leaves a nearly automatic win for safe
play, while recovery after a bust is possible but unlikely. Keeping 21 and
doubling the rounds produces a longer challenge with only a modest recovery
chance. Limit 12 is a reasonable alternative, but limit 10 offers more recovery
within the same five rounds and brings the risky decision earlier.

The recommendation is deliberately forgiving. A basic safe policy succeeds
often but not always; banking at 6 instead of 5 improves the outcome without
requiring a full solution of the game. Pushing to 7 reduces success to
77.922639%, so increased risk is not a universal improvement. A beginner can
discover and discuss those consequences without calculating an optimal policy.

Target 32 retains the same rules and a credible recovery chance while making
session decisions more consequential. Keep it as a comparison if native play
finds target 30 too forgiving. It does not require an extra mode or menu now.

## Decisions and round length

With limit 10, two rounds remaining and current total 6:

| Points still needed | Bank now, then choose optimally | Roll now, then choose optimally | Better choice |
| --- | --- | --- | --- |
| 10 | 100% | 76.309615% | Bank |
| 19 | 0% | 18.425309% | Roll |

Both are possible session states under the recommended challenge. The total
alone does not determine the best choice; earlier secured points matter.

At limit 10, totals up to 4 cannot bust next roll. At 5, 6, 7, 8 and 9, the
counts are respectively one through five bust outcomes out of six. Exactly 10
ends the round automatically. This is the same increasing-risk mechanism as the
21-limit version, with smaller totals.

The moderate bank-at-6 policy averages 2.161394 rolls per completed round. The
original safe bank-at-16 policy averages 5.046122. These are counts under named
policies, not elapsed time or measurements of a player's session. Native input,
reading and feedback will determine the actual pace.

## Checks and next review

The checker covers all 258 active-total/die combinations across limits 10, 12
and 21 for next-roll bust risk. It retains the original 21/5/90 maximum as a
regression case and checks target equality, no extra round after exhaustion and
unreachable targets. A safe policy guarantees only 25 at the recommended limit;
it does not guarantee the target of 30.

Boundary fixtures distinguish 9, 10 and 11 at limit 10, including a high bust
of 15 scoring zero. Negative controls reject treating equality as a bust and
awarding the bust total as points. All checks pass, along with Ruff lint and
format checks. These controls and the independent fixed-policy path check model
consistency; they do not establish native input, scoring or reset behaviour.

Use the [game brief](brief.md) for the native acceptance run. Try cautious,
deliberately risky and context-dependent choices, including recovery from a
bust and failure after earlier low banks. Judge whether choices are readable,
whether the recovery feels plausible and whether another attempt is appealing.
Do not treat the mathematical maximum as an expected learner success rate.
