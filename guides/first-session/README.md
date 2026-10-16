# First session guide pack

The [public pack](https://code198x.com/try/) offers a bounded first session for
someone exploring alone or sharing an activity with children or students.

- [Make a greeting with BASIC](https://code198x.com/try/spectrum-basic/).
- [Change the border with assembly](https://code198x.com/try/spectrum-assembly/).
- [Parents and teachers](https://code198x.com/try/parents-and-teachers/): preparation,
  hints and expected results, separate from the learner activities.
- [Session sheet](https://code198x.com/try/session-sheet/): print from the browser.
- [Optional feedback](https://code198x.com/try/feedback/).

Use the [draft invitation](invitation.md) when inviting potential learners and
[session observation notes](session-observations.md) when someone tries it.
No learner session has been recorded. The wider umbrella issues remain open.
Pause expansion until these first sessions produce observations; repair confirmed
blockers as they arise.

## Ownership

The website owns the public prose under `src/pages/try/` and its shared
`FirstSessionLayout.astro`. Start Here and Teaching link into the pack.
The lessons and maintained sample repository continue to own runnable code and
detailed teaching. Keep public instructions there rather than maintaining a
second copy in this docs repository. Git retains the reviewed content draft.

Use the existing site layouts, tokens and geometry. The print rules apply only
to the guide. The browser's print dialogue can print or save a PDF; there is no
separately maintained PDF edition. A print sheet is not an offline emulator or
a replacement for the linked lesson.

## Adding activities after the first trials

Keep the entry guide short. As choices grow, group them by what readers want to
make or investigate, then show the machine, language and tools each uses. Offer
a small starting selection with a route to the full list. Do not rank languages
as compulsory beginner-to-advanced steps or make programming experience the
only way to choose.

Each activity needs a visible result, knowledge assumed, equipment/access needs,
a named published lesson and maintained samples. Give it a bounded core: predict,
run or trace, change, explain, and keep the result. Include a stopping point,
optional depth, a next lesson and companion notes with hints and recovery.
Record the execution configuration separately from learner observations.

Use descriptive stable addresses rather than positions in a numbered pack.
Future machines, paper activities and game-making investigations can share these
responsibilities without copying Spectrum controls or imposing a fixed worksheet
length. Shared preparation and feedback remain separate; add only the new
activity's requirements and answers to the companion notes.

Add an activity to the public selection only when its entry, result, saving and
recovery steps and links have been checked. Publish no empty routes or promised
activities. If a published activity becomes unusable, explain the problem and
offer a working route while it is repaired.

## Verification

The [publication record](PUBLICATION.md) retains the production, browser and print
checks and their limits. The [native Safari follow-up](../../audit/2026-10-first-session-operability/REPORT.md)
adds a bounded desktop observation, with VoiceOver, physical touch and save/reopen
still unqualified. The earlier `review/live-links.json` and
`review/anchor-navigation-harness-failure.json` record the content draft's link
review; they do not qualify the later public pack or a learner session.

Before changing the public activities, repeat the affected run/save path, check
keyboard operation and narrow layouts, and inspect printed output if the sheet
changes. A technical check is not a learner trial. Use observed problems to file
issues under the original epic rather than expanding the pack speculatively.
