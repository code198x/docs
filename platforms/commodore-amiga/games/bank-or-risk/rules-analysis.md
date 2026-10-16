# Bank or risk rules analysis

The proposed five-round, 90-point challenge makes the choice between banking and
rolling matter under an ideal die. The same current total can call for different
choices depending on the points still needed. Native play must establish whether
this is enjoyable and whether losing the challenge after one bust is too severe.

## Method

Run from the documentation repository:

```sh
python3 platforms/commodore-amiga/games/bank-or-risk/rules_check.py
```

Executed with Python 3.14.3. The checker uses only the standard library. Exact
rational arithmetic enumerates the six outcomes of each possible roll, with
cached state values rather than random sampling. The state is rounds remaining,
points still needed and current total. Positive die values bound the recursion;
banking, reaching 21 or busting consumes a round.

At each decision, the target policy compares the chance of eventual success
after banking with the mean of the chances following the six roll outcomes. It
chooses the larger probability. The comparison policy always banks at 16 or
above. Displayed percentages are rounded to six decimal places.

This assumes independent equally likely outcomes. It checks proposed game rules,
not AMOS execution, random-number quality, keyboard behaviour, saving or learner
understanding. No language runtime is implemented by this checker.

## Results

| Check | Result |
| --- | --- |
| Every active total 0–20 against die values 1–6 | All 126 combinations match the expected next-roll bust count. |
| Current total 15 | No outcome busts. |
| Current totals 16, 17, 18, 19, 20 | Respectively 1, 2, 3, 4, 5 outcomes out of 6 bust. |
| Five rounds, bank at 16 or above, target 80 | Success probability exactly 1; this target would not require risking a bust. |
| Five rounds, bank at 16 or above, target 90 | Success probability 34.893448%. |
| Five rounds, maximise target success, target 90 | Success probability 76.795746%. |
| Two rounds remaining, current total 16, need 30 | Banking gives 100%; rolling gives 83.333333%. |
| Two rounds remaining, current total 16, need 39 | Banking gives 0%; rolling gives 47.511105%. |
| Four rounds remaining, need 90 | Impossible: their maximum is 84. A bust in the proposed challenge therefore ends contention. |
| No rounds remaining, need zero or one | Equality succeeds; a remaining shortfall fails without an extra round. |

These probabilities compare mathematical policies, not observed player win
rates. The optimal target policy is not an introductory prerequisite. Learners
can reason about possible next results without deriving the solver.

## Negative controls and remaining checks

Boundary fixtures distinguish a live total of 20, a perfect total of 21 and a
bust total of 22. A second high-end case reaches 26 and awards zero. The checker
rejects two deliberately incorrect classifiers: one treats equality with 21 as
a bust; the other awards the displayed bust total as points. Thus a green check
cannot come solely from accepting whichever result the classifier returns.

The checker passed, and Ruff check and format verification passed. The native
prototype still needs the full [brief's acceptance run](brief.md), including
score/round updates, input release, result stability, replay, quit and fresh
save/reopen. Neither the model nor the two mutations establish those outcomes.

Use play observations to adjust the target and round count together. Raising
the number of rounds without reconsidering the target could remove the need to
risk anything. If the one-bust consequence dominates play, compare a setting
that permits recovery while retaining meaningful banking decisions before
committing to lessons.
