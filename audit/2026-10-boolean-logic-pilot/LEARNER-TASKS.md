# Boolean conditions learner tasks

Read [Truth Tables](https://code198x.com/foundations/truth-tables/) and its three
units using the proposed version supplied for this trial. No machine or previous
course is required. Here TRUE/FALSE are Boolean values, shown as 1/0 in tables.
AND requires both, OR accepts either or both, XOR accepts exactly one, and NOT
turns a Boolean answer round. These examples are notation to reason about.

Keep each prediction answer closed until you have made your prediction. Use
paper, words or a table; you can ask for help and there is no score or time target.

1. Before reading the combined table, predict AND, OR and XOR when both inputs
   are true. Then list all four input pairs and check every result. Which row
   distinguishes OR from XOR?
2. Compare A, A AND A and A OR A for A false and A true. Do repeated conditions
   always make a guard harder or easier to pass? If both inputs come from testing
   the same unchanged score > 0, which pairs in a general two-input table can
   occur?
3. The jumping guard is button AND onGround AND NOT stunned. Predict its passing
   row. Modify it by removing NOT, then identify the rows where its result
   changes. Explain what the mistake would mean for the player.
4. Make both columns for NOT (A OR B) and (NOT A) AND (NOT B). Explain what equal
   columns establish. Would they tell you how long either expression takes on
   a machine, or whether evaluating an operand can report an error?
5. Diagnose a renamed guard. The current values are dead TRUE and finished FALSE,
   but separately stored flags still say alive TRUE and unfinished TRUE. Compare
   NOT (dead OR finished) with alive AND unfinished. Explain what must be repaired
   before the second guard can stand for the first.
6. Create two different-looking guards for the same rule: continue only while
   the game is neither paused nor finished. Use these two Boolean inputs, give
   the four-row table, and explain why both guards agree. Supply one deliberately
   wrong alternative and identify a row that exposes it.

Optional connections, after the core tasks:

- Follow the link from unit 3 to the BASIC lesson Keep guessing. Find its separate
  lower/upper range checks. Compare which values they reject with the single
  condition g < 1 OR g > 10. Leave the separate whole-number check in place.
  This is a reading comparison; running the complete game is optional. Return
  to the table lesson afterwards.
- Follow the Game State Machine pattern link. Find the transition table and
  explain which transition wins if death and a new Pause press happen together.
  How is that policy different from proving two expressions have equal Boolean
  results? The pattern uses its own illustrative notation. Return when finished.

Tell the observer where a word, table or link left you guessing. A wrong
prediction followed by an explanation is useful evidence; copying a correct
column alone does not show what you understood.
