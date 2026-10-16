# Counted-loop assessor notes

No learner has completed this trial. The model/native results establish selected
technical behaviour, not educational effectiveness. Keep this sheet apart from
the prompts. Record first predictions, explanations, help and repairs separately.
Do not coach the first attempt or turn the exercise into a score.

1. 2 TO 2 visits 2 once; 3 TO 2 visits nothing; 0 TO 2 visits 0, 1, 2 three times.
   The difference counts gaps for a non-empty ascending range. Include both
   endpoints to count values; an empty range still has zero visits.
2. Begin, 2, 3, 4, Finished. With end 1, only Begin and Finished appear.
   The counter body's absence does not remove the following line.
3. With Finished inside, the non-empty output is Begin, 2, Finished, 3,
   Finished, 4, Finished. For the empty range only Begin remains. The original
   outside version prints Finished once for either range. Trace the marker
   boundary rather than counting spaces in the source.
4. 0 TO 4 visits five values. Repair it to 0 TO 3, giving 0, 1, 2, 3. Starting
   at 1 would also yield four visits with end 4, but would violate this task's
   required starting value. A different correct program still needs to meet
   the stated rule.
5. The intended totals after visits are 1, 3, 6. Resetting inside gives 1, 2, 3:
   before the second addition the reset erases the earlier 1. Initialise before
   the loop, then let each visit keep the growing total. Returning the desired
   final answer by hard-coding 6 does not explain the accumulating rule.
6. One answer is SHOW Ready, FOR n = -1 TO 1, SHOW n, END, SHOW Done, with
   quotes around the two messages and each instruction on its own line. For
   the empty variation, choose a start past its end, such as 2 TO 1. Record
   both complete traces. The three-visit observation covers only that range;
   zero visits tests whether the body and continuation are understood.

The optional BASIC page describes three dots inside FOR/NEXT and one sound
after NEXT. Sound is supplementary: its visible dots and heading still work
when muted. Do not infer that every BASIC dialect or assembly counter has the
same entry rule, variable lifetime or post-loop value as this notation.

A useful hint, after recording an attempt, is to draw a box around the body and
list counter values before tracing its lines. Ask for another boundary case
without supplying its answer. Independent reasoning, a useful counterexample
and a repair explained in the learner's own words are stronger evidence than
repeating the lesson's displayed list.
