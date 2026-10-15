# Decisions and boundaries: learner tasks

Draft trial prompts. Choose one route; the other routes are not prerequisites.
Predict before running a program or opening its answer. Tell the observer when
you need help with a term, a control or a programming idea.

## Find the explanation

Begin at [Start Here](https://code198x.com/start-here/). Find your chosen route's
lesson below. Explain why you chose that link. The observer can supply the direct
link after recording any difficulty. Later, see whether you can find a useful
shared explanation and return to your lesson without losing your place.

## Foundations: which instructions happen?

Read [Making a Choice](https://code198x.com/foundations/decisions/unit-01/).
For the revised explanation, use the proposed preview until it is published.

1. A program asks for two numbers and shows their sum. Can it give different
   answers while carrying out the same instructions? Explain what changes.
2. Before opening “Check the three cases”, predict whether the `SHOW` runs for
   `guess` values `-1`, `0` and `1`. What value remains in `guess` after the test?
3. Change the condition to `guess = 0`. Predict all three cases again. Explain
   which instruction would now run for zero.
4. Someone says `guess > 0` must be true because the prompt asks for a positive
   number. Give a counterexample and explain the difference between asking for
   a value and checking it.
5. Write three separate tests for a new secret of your choice: below, equal and
   above. Choose one test value for each case and predict the messages. This is
   pseudocode for reasoning, not code to type into a Spectrum.

## BASIC: give a useful clue

Read [Give a useful clue](https://code198x.com/systems/sinclair-zx-spectrum/basic/meet-basic/unit-05-give-a-useful-clue/).
The opening lesson explains numbered lines and keyboard entry if needed. You do
not need Foundations or assembly. Save work you want to retain before clearing
an existing program. This lesson's target keyboard route needs a physical
keyboard; do not assume it has the editable listing from an earlier lesson.

1. Use the complete three-test listing with secret 7. Predict the messages for
   4, 7 and 9 before running each. Which of lines 40, 50 and 60 are tested when
   the guess is 7? Does a true condition stop later numbered lines being tested?
2. Predict and try 0. Does the program reject it as invalid, or compare it with
   the secret? Explain the difference between the prompt and an enforced rule.
3. Change the less-than test to greater-than without changing its message.
   Predict a guess that exposes the error. Run it, explain the conflicting
   messages and repair only that test.
4. Choose a new secret and predict one lower, one equal and one higher guess.
   Run them. Explain why exactly one message should appear in each case.

## Assembly: repair a branch and keep the boundary safe

Read [Find the first wrong step](https://code198x.com/systems/sinclair-zx-spectrum/assembly/meet-assembly/unit-08/).
This is the eighth lesson in the assembly introduction. Earlier assembly lessons
explain the program, source editor and registers; BASIC is not required.

1. Reproduce the supplied left-movement fault. Record something that still
   works, and choose one explanation you can test.
2. Run to the left decision. Predict what loading position into A changes, then
   step. Before the branch, record A, the position byte and Z when shown. Explain
   why a comparison/test and a stored game position are different things.
3. Make the smallest branch repair you think is justified. Reassemble before
   stepping. Check an ordinary left move, then start at position zero and predict
   whether decrementing should happen. Test the boundary too.
4. Someone tests one ordinary move and declares the repair finished. Explain
   which missing case could disprove that claim.
5. Load the second case and investigate it without the first case's repair
   guide. Choose an observation that distinguishes wrong position from wrong
   drawing data. Explain and test a repair, including erasing the old picture.

## Optional connection

[State Machines](https://code198x.com/vault/techniques/state-machine/) develops
conditional behaviour into named game states. Read only as far as is useful.
Find an example of a condition controlling a state change, explain it in your own
words, then return to the lesson. This article is optional depth, not an entry
requirement or a substitute for understanding the three tests above.
