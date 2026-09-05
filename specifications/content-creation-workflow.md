# Content creation workflow

Use [the charter](../PROJECT.md) as the direction, [curriculum design](curriculum.md) for teaching responsibilities and [the brief](brief.md) for a game's concrete promise. Work in the repository that owns each file.

## 1. Establish context and evidence

Read the actual catalogues, lessons, samples and relevant system design material. Identify what is implemented, specified or merely proposed. Inspect source indexes before individual sources. Research technical and historical claims with precise primary citations where possible.

Check available assemblers, language environments, emulators and execution integrations. Name unsupported or unverified paths. Do not promise validation because a repository exists.

Public writing cites original publications or relevant public pages. Private research notes and unavailable local source locations are not public citations. Do not commit confidential working notes or third-party source collections.

## 2. Agree the specification

Prepare the game's experience, teaching, target, assets, runnable stages and verification plan. Resolve substantive conflicts with the charter explicitly. Compare existing choices before replacing them. A suggested lineup or possible module is not an adopted decision.

For the current Spectrum work, agree the game specifications before developing lesson prose. A focused prototype can answer a design or performance question without committing to a full course.

## 3. Prove the endpoint and plan the teaching route

Build and play a representative finished endpoint before deriving a long lesson sequence. Check rules, content, endings or the repeatable play cycle, and responsiveness. Use human playtesting for clarity and enjoyment, as well as scripted checks for correctness.

Then decompose it into teachable, runnable stages. The discovery order need not be the teaching order. Preserve an intentional naive approach where experiencing its limit teaches the upgrade; do not force readers to repeat the author's accidental mistakes.

Keep useful observations and faults as evidence with the project. They are not new curriculum policy. Update the brief when findings change the design, and obtain agreement for a substantive scope change.

## 4. Author and verify

Write units to [the unit specification](unit.md). Explain both mechanism and purpose. Maintain the source and asset sequence, and produce captures from the corresponding code.

Validate changes with the actual build/load path. Exercise boundaries, unusual input and regressions. Inspect pictures and motion, listen to audio, and check the design in play. Where behaviour surprises, consider code, emulator, hardware-variant and documentation faults as hypotheses.

Record proposed design, source-checked facts, successful builds, execution observations and hardware observations separately. Include versions, model, initial state and input sequence sufficient to repeat a result. Neither compilation nor emulator accuracy claims guarantee original-hardware compatibility.

## 5. Integrate and finish

Connect the lesson to existing shared explanations, Vault entries and patterns. Create missing context only where it is useful and adequately sourced. A pattern should retain assumptions, limitations and machine-specific details, and link back to its complete-game application.

Check the whole game through its normal rules: start, representative play, success and failure where applicable, restart and repeated sessions. Script useful end-to-end checks through real logic. Setups that shorten a test must be identified and must not bypass the behaviour being claimed. Retain manual playtesting as separate evidence.

Check instructions, controls, pause behaviour where appropriate, accessible feedback, packaging, credits, asset permissions and a way to report problems. Completeness is relative to agreed scope, not a commercial comparator.

## 6. Publish and maintain

Run relevant checks from the owning repositories. The website's package scripts and CI define its current build checks; sample Makefiles and capture/proof manifests define program verification. Fix failures or state concrete limitations rather than claiming a blanket pass.

Coordinate changes across docs, website and code-samples so links, samples and downloads refer to compatible versions. Commit in each owning repository. Build outputs are published from reproducible builds; preserve existing tracked outputs until their replacement build/download path has been verified.

Update catalogue availability only when supported by content and verification. Neither a written plan nor a successful isolated capture makes a module complete. Publication follows the user's authorised workflow; sending community announcements is a separate communication action.

When intent changes, edit the relevant current guide rather than appending another contradictory decision. Explain the reason in the pull request. Preserve historical context in Git; retain working research only when it can change a future implementation, explanation or correction.
