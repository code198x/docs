# First AMOS and Blitz execution routes

Proceed from accepted opening audit and docs #94 / website #766. Use existing
FS-UAE 3.2.35 and local firmware/Workbench inputs; acquire missing language tools
only after the dependency approval required by the umbrella AGENTS.md.

1. Record installed emulator version/binary hash, selected local ROM and OS image
   identities, and the six-line/three-line source identities. Keep media and local
   library paths out of public evidence; use hashes and distribution identifiers.
2. Pin the proposed language inputs: official AMOS repository at
   533b4b1f5acd604814513f78e02c7b4796cb0531 and AmiBlitz v3.13.0b release archive
   (13,835,564 bytes; upstream SHA-256
   e728b213f9e45cb2a2098dd41c9d3ea7d4810ff363725f9a75810bd09e788b3e).
   Request approval before downloading/unpacking these missing test dependencies.
3. Prepare an isolated FS-UAE A1200/PAL configuration with 2 MiB chip RAM and
   8 MiB fast RAM, local Kickstart/Workbench 3.1 and a task-owned tools drive.
   Use copies/read-only source media; bound logs and each run. Confirm the OS
   boots and the named IDE starts; record actual versions and controls.
4. For each maintained unit-1 greeting: load/enter actual source, run/compile,
   observe output, change words and rerun, provoke an unclosed-quote syntax error,
   repair it and observe the recovered result. Retain captures and action records;
   do not label an unsuccessful attempt a pass. Stop after two failed approaches
   to the same blocker and reduce scope.
5. Write `audit/2026-10-amiga-greetings/REPORT.md`, input identities, observation
   records, validation and hashes. Correct only the proven setup/first-unit claims
   in the website, if the route is qualified; keep original Blitz/Ted and AmiBlitz
   variants distinct. If a dependency or runtime blocks qualification, report the
   exact boundary and complete unaffected evidence work without inventing a run.
6. Verify changed pages with the existing build and bounded wide/narrow checks;
   commit/push draft PRs and update #94/#766/#116. Inspect and clean task processes,
   media copies, worktrees and helpers after evidence/commits are retained.

No whole-course compatibility, retro-hardware timing, learner effectiveness,
VoiceOver, physical-touch or redistribution permission is inferred. A running
Workbench is not a language-runtime pass. No change to emulator code is planned.

## Observed deviation

AMOS automatically closes the missing quote, so the negative case became a
trailing plus with no right operand; actual error and recovery were observed.
AmiBlitz reached PED and Compiling, then computer use lost the emulator window.
Stop retries, retain incomplete evidence and leave #94/#766 open; ship only the
proven AMOS setup correction for review. Screenshots were visually inspected in
the session but not retained as files; manual observations are labelled as such.
