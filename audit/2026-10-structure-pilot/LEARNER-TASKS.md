# Structure: learner tasks

Use the Structure pages. Work on paper or in a text document; you do not need to
learn a target language first. Predict before opening a page's answer. Ask for a
hint if needed, and let the observer record it before helping.

1. **Find the boundaries.** A list holds `[8]`. Which of indices 0, 1 and 2 select
   an item in this notation? Append 13, then answer again. What are the length
   and valid indices of `[]`? Explain what a FOR EACH loop would display for it.
2. **Trace two loops.** Write the output order for rows 1–2 and columns 1–3,
   with the column loop inside the row loop. How many lines appear? What changes
   if the loops are exchanged? Explain which quantity changes fastest.
3. **Change a shared job.** In unit 2, change the divider's dashes to stars.
   Predict how many screen dividers change. Then suppose only the middle one
   should change: explain why changing that one shared definition is insufficient.
4. **Separate a copy from its result.** Start with `n = 4`. Call the unit 3
   double job with `LET result = double(n)`, then call it with
   `LET n = double(n)`. Record caller n, local n and returned result for each
   call. What would change if the job printed its answer instead of returning it?
5. **Diagnose a total.** A program starts total at zero, then for every price in
   `[4, 7, 2]` runs `LET total = price`. It should add the prices. Predict the
   actual final value and the intended one. Repair one line, then test an empty
   list, a one-item list and the original list. Explain why one item can hide the bug.
6. **Make a small job.** Define a job that takes a numeric value and returns that
   value plus three without printing or changing the caller's variable. Choose
   zero and a negative input. Write a caller that keeps the old value and stores
   the returned result separately. Explain what the caller can rely on.

Optional connections:

- Follow Write the repeated job once. Identify where execution resumes after
  each of its two GO SUB calls. Read the explanation without running the game.
  Explain why that RETURN is not the same as RETURN followed by an expression.
- Follow the assembly debugger connection in unit 4. Find an observation made
  before the repair. You can inspect the explanation without learning registers
  first; record running or stepping the program separately if you do it.

Record which task needed a hint and which explanation remained unclear. Do not
include a child's name or personal details in shared observations.
