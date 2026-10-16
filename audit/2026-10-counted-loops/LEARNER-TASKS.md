# Counted-loop learner tasks

Use the proposed Doing It Again lesson. We use notation to trace on paper.
SHOW displays a value or quoted text. FOR visits whole-number counter values,
adding one each time. The end is included; a start past the end gives no visits.
The body lies between FOR and END. Keep the counter and bounds unchanged here.
No machine, required earlier course, score or time target is needed.

Attempt these before revealing the lesson answers or reading the assessor sheet.
Record predictions and any help. Use a list, words or a trace.

1. List the values visited by 2 TO 2, 3 TO 2 and 0 TO 2. How many visits does
   each give? Why is subtracting the start from the end not always the count?
2. Trace this program, including the order of every displayed line:

   ```text
   SHOW "Begin"
   FOR n = 2 TO 4
     SHOW n
   END
   SHOW "Finished"
   ```

   Replace 4 with 1. Which lines still display something?
3. Move SHOW Finished just before END, keeping the quotes. Predict both versions
   for 2 TO 4 and 2 TO 1. Explain why indentation helps you read a loop but does
   not replace its END marker.
4. A program should display four counter values starting at zero. Its author
   wrote 0 TO 4. Diagnose the mismatch and repair the range without changing
   the starting value. Give the exact output values.
5. LET puts a value into a variable. The right side is calculated first.
   Starting with total 0, a loop visits 1, 2 and 3 and uses
   LET total = total + n each time. Predict the final total. What if
   LET total = 0 also runs at the start of every body visit? Explain the first
   point where the states differ and how to repair it.
6. Create a short program that displays Ready once, the counter values -1, 0, 1
   in that order, and Done once. Give an empty-range variation that displays
   only the two messages. Explain why a successful three-visit trace alone
   would not establish the empty-range behaviour.

Optional: follow Give the answer a rhythm. Read Describe the repetition once
and locate the sound after NEXT. How many dots and sounds does its described
three-visit version produce? Running the complete BASIC program is optional;
its instructions introduce the target's own syntax. Return to Foundations.

Tell the observer where the wording or notation left you guessing. A wrong
prediction followed by an explanation is useful. Copying a correct answer alone
is not evidence of independent understanding.
