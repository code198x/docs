# Spacewar! pilot evidence and review limits

**Status: working evidence record, 18 October 2026.** This records the revised draft's basis and outstanding checks; it does not establish human sign-off or publication readiness. [The charter](../../PROJECT.md) and existing evidence standards govern the work. The study is [study.md](study.md).

## Source register

| ID | Source and locator | Evidence role and limits |
|---|---|---|
| S1 | D. J. Edwards and J. M. Graetz, “PDP-1 Plays at Spacewar,” *Decuscope* 1(1), April 1962; [Wheels transcription](https://www.wheels.org/spacewar/decuscope.html), paragraphs beginning “Planned and programmed,” “Also displayed” and “Mr. Russell also said” | Contemporary participant account plus editorial voice. The mirror reports pp. 2–4; that pagination has not been independently checked against the original issue and is not asserted as verified in the study. No attendance count or empirical survival statistic is adopted. |
| S2 | J. M. Graetz, “Spacewar! Real-Time Capability of the PDP-1,” *DECUS Proceedings 1962*, copyright 1963, printed pp. 37–39; [scan](https://bitsavers.computerhistory.org/pdf/dec/decus/confProceedings/DECUS_1962.pdf#page=39), PDF pages 39–41 | Contemporary description of one development state; precise rule/credit locators below. Text layer inspected. Browser screenshot retrieval failed and a direct download timed out; no figure has been reproduced or visually validated from this source. |
| S3 | J. M. Graetz, “The Origin of Spacewar,” *Creative Computing* 7(8), August 1981; [annotated transcription](https://www.masswerk.at/spacewar/SpacewarOrigin.html), sections I–III | Participant recollection. The transcription combines the magazine text and the Fall 1983 *Computer Museum Report* reprint, with later editor notes. Use named article sections, keep testimony attributed and distinguish editor notes from Graetz. The large 1983 PDF and a Smithsonian transcript lead could not be retrieved; neither is claimed as read. |
| S4 | Steve Russell, interview by Al Kossow, 9 August 2008; [CHM transcript](https://archive.computerhistory.org/resources/access/text/2012/08/102746453-05-01-acc.pdf), pp. 14–16; title page reference X4970.2009 | Late participant recollection, including uncertainty. Controls: pp. 15–16. Pace and parameter preferences: p. 14. Recollection does not prove every early controller's construction or all players' preferences. |
| S5 | Stewart Brand, “Spacewar: Fanatic Life and Symbolic Death Among the Computer Bums,” *Rolling Stone*, 7 December 1972; [Wheels transcription](https://www.wheels.org/spacewar/stone/rolling_stone.html), opening Stanford scene, “The Hackers” and “Spacewar” | Contemporary reporting of a later scene and embedded interviews. Its PDP-10 variant is not the 1962 reference edition. The mirror has an inconsistent event-notice date relative to a search-indexed scan; the draft does not assert the event's exact day. Its rhetoric is not adopted as a neutral account of all computing communities. |
| S6 | Computer History Museum, PDP-1 restoration project, [“Spacewar!”](https://www.computerhistory.org/pdp-1/spacewar/), main account | Museum synthesis for collective credit and demonstration use. Do not adopt unsupported sales-conversion figures or priority superlatives. Its statement about the machine's BBN origin is not used; S2's acknowledgment describes a DEC gift, so acquisition details need separate reconciliation. |
| S7 | Norbert Landsteiner, [Spacewar! browser emulator](https://www.masswerk.at/spacewar/), “Program Versions,” “Game Options” and 3.1 entry | Primary documentation of this implementation, not independent historical confirmation. Module/engine identities and execution record are in observations.json. Host facilities and splash screen are not original game features. |
| S8 | Computer History Museum, [browser edition](https://www.computerhistory.org/pdp-1/playspacewar/), provenance paragraph | Primary implementation disclosure for a different browser presentation. Its documented size/timing changes are not imputed to Landsteiner's implementation. |

These works retain their own terms. Links and restrained original paraphrase are used; the repository does not acquire their text, images, recordings or binaries for redistribution. No source permission or public-domain claim from a host is treated as a licence for the host's GUI or all linked material.

## Claim and interpretation ledger

| Draft section / claim | Basis | Verdict for this draft |
|---|---|---|
| Early account includes spectators and offers program tapes | S1, article body and final paragraph | Supported as what the newsletter reported. No count of players or distribution totals. |
| Thrust direction, inherited projectile velocity, gravity on ships rather than torpedoes | S2, p. 37, Introduction / The Game | Supported for the described state. Browser smoke checks are not a numerical physics verification. |
| Star capture/antipoint and three hyperspace jumps | S2, pp. 37–38 | Supported as early rules; explicitly not universalised to 3.1 or later variants. |
| Different ship shapes, exhaust and point-like torpedoes | S2, p. 38, The Spaceships | Supported description. Modern browser observations provide a separate visual check. |
| Browser player action responses, retained as supporting research rather than article narrative | Bounded observations in observations.json | Five execution cases and inspected captures; not gameplay coverage or a two-person play session. The revision makes no article claim based on a completed play session. |
| Silent switches and controller wear | S4, pp. 15–16 | Attributed recollection. Do not claim measured impact or an uncontested unique controller design. |
| Science-fiction influences and Wiitanen's absence | S3, section I, Lensman/Skylark; section II, First Steps | Attributed recollection. No invented motives, dialogue or geopolitical causation beyond that account. |
| Collective creation | S6 main account; S2 credits relevant to individual contributions | Supported; no single-author invention story. A full contributor biography set is not supplied by this draft. |
| Overlapping work and responses to perceived problems | S3, section III opening and named subsections | Attributed recollection, not an independently reconstructed production schedule. |
| Pace is a chosen preference | S4, p. 14 | Attributed, not proof of optimal settings or a universal player response. |
| Demonstration to prospective customers | S6 main account | Museum reports this use. No sales attribution or marketing budget claim. |
| Organised later play at Stanford on another machine | S5 opening scene | Supported as the reporter's account of the 1972 scene, not 1962 rules. |
| Browser emulation changes the means of encounter | S7/S8 disclosures, actual browser execution | Implementation-specific. No assertion of timing, CRT, controller or acoustic fidelity. |
| Decisions have continuing consequences; anticipation links movement and aiming | Analysis from the stated rules | Design interpretation, not a recovered quotation or documented intention. |
| Sparse imagery invites a larger imagined setting | Interpretation grounded in the game and attributed cultural account | A proposition for discussion, not evidence of what every player imagined. |
| Distribution required access to a suitable machine and a way to run the tape | S1 tape offer and S6 machine context | Bounded explanation of the distribution route; no unsupported demographic census or exclusion allegation. |
| Proposed two-player investigation | Author-designed activity | Not executed as a human trial or calibrated exercise. No difficulty/time/age claim. |

## Evidence needed before a publishable study

1. Independently match the module's embedded tape with an upstream archival image, retaining the identity and any loader/startup patches. The JS response hash pins the implementation read; it does not independently authenticate the tape.
2. Run a two-person play/read session on the named version. Observe learning, aiming, readability, exhaustion/recovery and the selected star/hyperspace behaviour. Record participant observations as observations, not representative audience data.
3. Compare a complete encounter, ending and restart. These short automated cases do not cover a match or establish every rule. Inspect the rule/code relationship before adding resource counts or probabilities.
4. Check source transcriptions against originals where available, including S1 pagination and any exact event chronology needed. Resolve acquisition details before using them.
5. Investigate audio/acoustic conditions before writing a historical sound account. The inspected browser engine contains no audio API references; that does not establish historical silence or the room's sound.
6. Identify period demonstrations and distribution material in more depth before quantifying reach, commercial effects or production resources. Do not invent a retail package for this game.
7. Choose permitted imagery and record source/credit/reuse terms under existing policy. Research screenshots are not article-ready publication assets. A CRT photograph, browser capture and illustrative diagram must remain distinguishable.
8. Human editorial review of the historical claims and design interpretation; then agree site placement and verify the rendered page. None of these steps changes the standing delivery queue automatically.

## Voice revision

The revised article starts with an illustrative player situation, not a reconstructed historical event or a report of a human trial. Source markers refer to the numbered reading list; S1–S8 above retain the research register numbering, which differs from that reading list. Methods, response identities and uncompleted checks remain here and in observations.json. The article retains attribution for recollections and edition differences where those affect its meaning. Warmth and interpretation do not establish additional historical facts.
