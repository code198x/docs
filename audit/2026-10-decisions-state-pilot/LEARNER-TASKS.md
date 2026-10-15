# Learner tasks: first match and saved answers

Use Decisions overview and units 2–3. Work on paper with the teaching notation;
keep the assessor sheet separate. A helper should record observations without
coaching. Earlier modules are optional support, not required attendance.

1. Trace the score chain for 49, 50, 79, 80 and 81. Record the chosen message
   and what happens after END. State the numeric domain used in this example.
2. Put the broad score >= 50 condition first. Predict the result for 80, then
   explain why no qualifying high score reaches the later branch. Compare this
   with two separate IF tests for the same score.
3. Create a score of your own that separates the two chain orders. Explain why
   a score below 50 cannot expose that particular ordering mistake. If one run
   passes, what further cases would you want to inspect?
4. Trace guess = 4, tooLow = guess < 7, then guess = 9. Record both values after
   each assignment. Compare IF tooLow with a fresh guess < 7, then modify the
   program to make both tests agree on the current guess.
5. Explain a reason to keep an earlier answer instead of refreshing it. Decide
   whether changing guess should change every flag automatically.
6. Start with zero lives and gameOver set by that event. Restore three lives
   without resetting the flag. Predict the next IF gameOver, then show the
   explicit new-game reset. Why could resetting on every update lose an event?
7. Create a small yes/no event flag with a stated starting value, an event that
   raises it, a later use and a reset boundary. Trace two consecutive sessions,
   including a session where the event never occurs. Keep the rule testable.

Record the learner's own words, revisions and hints requested. Leave unaided
completion, timing, retention and transfer unknown until observed. Optional
support links lead back to values and arithmetic; no machine setup is required.
