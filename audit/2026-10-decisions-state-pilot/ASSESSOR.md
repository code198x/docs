# Assessor notes: first match and saved answers

All actual learner outcomes remain **not observed**. These are expected answers,
not learner results.

1. For 49, 50, 79, 80 and 81 the messages are Keep trying, Pass, Pass, High score
   and High score. Done follows each chain. Scores are whole numbers 0–100.
2. Broad-first chooses Pass at 80. Every score >= 80 also meets >= 50. Separate
   IF tests can run both matching bodies; a chain chooses the first match.
3. Any whole score 80–100 exposes the fault. Lower values match both policies;
   passing those alone cannot settle the high-score boundary.
4. The stored pairs are (4, not assigned), (4, TRUE), (9, TRUE). A fresh test is
   FALSE after the change. Assign tooLow = guess < 7 again to store FALSE.
5. An earlier answer can record an event for later use. A comparison assignment
   stores its current value, not a rule that follows later operand changes.
6. Restored lives leave gameOver TRUE, so the IF still chooses Game over. Reset
   gameOver to FALSE at the new-game boundary. Resetting before a later reader
   handles the event could erase it. A latched flag is not inherently a bug.
7. Accept a consistent flag whose meaning and reset boundary are stated and
   whose two-session trace follows them. A current-condition flag needs refresh;
   an event latch can deliberately retain its answer until handled/reset.

Spectrum evidence uses numeric comparison results 0/1 and separate IF/GO TO
statements to implement dispatch. It is a target contrast, not native execution
of pseudocode ELSE IF or proof of every language's truth representation.
