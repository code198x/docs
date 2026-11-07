export const meta = {
  name: 'vault-batch',
  description: 'Triage, research and draft a Vault batch, run every gate, and open draft PRs for review',
  whenToUse: 'Write the next Vault batch from the queue ranking, or from a list of VC- IDs. Args: {ids?, size?, slug?, attempt?, check?}',
  phases: [
    { title: 'Prepare', detail: 'choose the candidates and make the batch branches' },
    { title: 'Triage and sources', detail: 'one agent per candidate: coverage, scope and claim evidence' },
    { title: 'Draft', detail: 'write each new entry' },
    { title: 'Check claims', detail: 'an independent reader removes or qualifies what the sources do not support' },
    { title: 'Integrate', detail: 'links, queue rows, writing issues and review evidence' },
    { title: 'Gates', detail: 'scripts/vault_batch_gates.py; the batch stops here on any failure' },
    { title: 'Pull requests', detail: 'captures, commits and draft PRs' },
  ],
}

// Arguments, all optional:
//   ids      your own list of VC- IDs, in order; otherwise the queue ranking chooses
//   size     how many the ranking chooses (default 5)
//   slug     the batch name, used for branches and the review directory
//   attempt  raise it after fixing a failed batch: Gates and Pull requests then
//            run again while the earlier stages come back from the resume cache
//   check    true returns at once without starting an agent, to confirm this loads
const A = args || {}
if (A.check) return { loaded: true, args: A }

const CODE198X = '/Users/stevehill/Projects/198x/Code198x'
const UMBRELLA = '/Users/stevehill/Projects/198x'
const choice = A.ids && A.ids.length
  ? `--ids ${A.ids.join(' ')}`
  : `--size ${A.size || 5}`

const RULES = `
Rules for all Vault work (the Vault specification, ${CODE198X}/docs/specifications/vault.md, is binding; read its "Entry contract", "Writing and evidence", "Participant accounts and source kinds" and "Connections and review" sections before starting):
- Period magazines, manuals, service records and participants' own accounts are primary sources. Check a provenance claim (publisher, author, year) against the source itself.
- Corroborate every claim with a second, independent source where one exists. If you can't find one, say the claim is single-sourced; never present it as settled.
- World computing is in scope: regional and non-English sources are first-class.
- Read the reviewed entries that refer to the subject before deciding what it means, and agree with them or record the disagreement.
- Public content cites original, checkable sources only. Never mention the local library, its paths or private collections in anything that will be committed.
- Local research tools: the primary-source library at ${UMBRELLA}/reference/ (see its _meta), and the knowledge graph via \`python3 ${UMBRELLA}/ops/scripts/knowledge.py --help\` (results cap at 100; paginate with --offset).
`

const CANDIDATE = { type: 'object' }

phase('Prepare')
const prep = await agent(`Prepare a Vault batch. Work in ${CODE198X}.

1. Run \`date +%F\` for today's date. The batch slug is ${A.slug ? `"${A.slug}"` : '"<date>-vault-batch"'}.
2. Fetch code198x/docs and code198x/website. Create a docs worktree at ${CODE198X}/docs-batch-<slug> on a new branch vault-batch/<slug> from origin/main, and a website worktree at ${CODE198X}/website-batch-<slug> on the same branch name from origin/main. Never use the main checkouts; another session may own them. If either path or branch already exists, stop and report it rather than reusing or deleting it.
3. Set up the website worktree to build: \`npm ci\`, then \`bash scripts/fetch-ui.sh\`, then copy the built samples with \`cp -R ${CODE198X}/website/public/code-samples public/code-samples\` (a copy, not a link: Git ignores the directory but not a link to it, and the gates reject anything stray). The code-samples checkout the build reads already sits beside the worktree at ${CODE198X}/code-samples; create no link to it inside the worktree. Do not link public/emulators; \`npm run bundles\` stages it.
4. From the docs worktree run \`python3 scripts/next_vault_batch.py --website <website worktree> ${choice}\`. If it fails, report its output and stop.

Return the paths and the candidates exactly as the script printed them.`, {
  label: 'prepare',
  schema: {
    type: 'object',
    properties: {
      date: { type: 'string' },
      slug: { type: 'string' },
      docs: { type: 'string', description: 'absolute path of the docs worktree' },
      website: { type: 'string', description: 'absolute path of the website worktree' },
      candidates: { type: 'array', items: CANDIDATE },
      error: { type: 'string', description: 'set only if preparation failed' },
    },
    required: ['slug', 'docs', 'website', 'candidates'],
  },
})
if (!prep || prep.error || !prep.candidates.length) {
  return { stopped: 'prepare', detail: prep }
}
const REVIEW = `docs/reviews/${prep.slug}`
log(`${prep.candidates.length} candidates: ${prep.candidates.map(c => `${c.id} ${c.subject}`).join('; ')}`)

const TRIAGE = {
  type: 'object',
  properties: {
    id: { type: 'string' },
    decision: { enum: ['write', 'covered', 'deferred', 'blocked'] },
    path: { type: 'string', description: 'category/slug of the new entry, for write' },
    title: { type: 'string' },
    scope: { type: 'string', description: "what the entry covers and leaves out; the queue row's scope column if it needs correcting goes in scopeAxes" },
    scopeAxes: { type: 'string', description: 'corrected region:/period: values, semicolon-separated, or empty to keep the row as it is' },
    notes: { type: 'string', description: 'coverage checked (titles, aliases, redirects, sections, open and closed issues), the decision and why. No local paths.' },
    referringEntries: { type: 'array', items: { type: 'string' } },
    coveredBy: { type: 'array', items: { type: 'string' }, description: 'for covered: the entry paths that cover it' },
    blockedBy: { type: 'string', description: 'for blocked: the family tool issue URL' },
    sources: {
      type: 'array',
      items: {
        type: 'object',
        properties: { title: { type: 'string' }, kind: { type: 'string' }, note: { type: 'string' }, url: { type: 'string' } },
        required: ['title', 'kind', 'note'],
      },
    },
    claims: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          claim: { type: 'string' },
          evidence: { type: 'array', items: { type: 'string' }, description: 'source titles from sources' },
          single_source: { type: 'boolean' },
          qualification: { type: 'string' },
        },
        required: ['claim', 'evidence', 'single_source'],
      },
    },
    followups: {
      type: 'array',
      items: {
        type: 'object',
        properties: { subject: { type: 'string' }, category: { type: 'string' }, why: { type: 'string' }, existing: { type: 'string', description: 'an existing entry path or VC- ID if the subject already has one' } },
        required: ['subject', 'category', 'why'],
      },
    },
  },
  required: ['id', 'decision', 'notes', 'sources', 'claims', 'followups'],
}

const DRAFT = {
  type: 'object',
  properties: {
    path: { type: 'string' },
    backlinks: {
      type: 'array',
      description: 'existing unlinked mentions of this subject in other entries that should become links',
      items: { type: 'object', properties: { from: { type: 'string' }, text: { type: 'string', description: 'the exact existing words to wrap in the link' } }, required: ['from', 'text'] },
    },
    images: { type: 'array', items: { type: 'string' } },
    gaps: { type: 'array', items: { type: 'string' }, description: 'facts left out for lack of evidence, and why the entry runs past the length guide if it does' },
  },
  required: ['path', 'backlinks', 'gaps'],
}

const CHECKED = {
  type: 'object',
  properties: {
    path: { type: 'string' },
    removed: { type: 'array', items: { type: 'string' }, description: 'sentences removed or qualified, and why' },
    claims: TRIAGE.properties.claims,
    concerns: { type: 'array', items: { type: 'string' }, description: 'things a human reviewer should look at' },
  },
  required: ['path', 'removed', 'claims', 'concerns'],
}

const results = await pipeline(
  prep.candidates,
  c => agent(`Triage Vault candidate ${c.id}, "${c.subject}" (proposed category ${c.category}), and gather the evidence for it. You do not write any files.
${RULES}
Queue record: ${JSON.stringify(c)}

The website checkout to read is ${prep.website}; entries are in src/content/vault/, redirects in astro.config.mjs.

1. Check existing coverage: titles, aliases, redirects and relevant sections, not just file names. Search open and closed code198x/website issues for the ID, subject and aliases (\`gh issue list -R code198x/website --state all --search ...\`).
2. Decide: write (it earns its own entry; give its category/slug path), covered (existing entries serve the reader; list them), deferred (say why and what would change that), or blocked (a family tool must change first; give the tool issue). A combined row is written as its main subject; the others become followups.
3. For write: read the primary sources and corroborate. Record every claim the entry will make, with the source titles that support it, and mark any claim with one source single_source: true.
4. Record named subjects the entry will mention that have no entry yet as followups, saying if one already exists as an entry or a VC- candidate.`, {
    label: `triage ${c.id}`,
    phase: 'Triage and sources',
    schema: TRIAGE,
  }),
  (t, c) => t.decision !== 'write' ? { triage: t } : agent(`Write the new Vault entry ${t.path} for ${c.id}, "${t.title || c.subject}", in ${prep.website}/src/content/vault/${t.path}.mdx.
${RULES}
Scope: ${t.scope}
Sources: ${JSON.stringify(t.sources)}
Claims you may make, and only these: ${JSON.stringify(t.claims)}
Referring entries: ${JSON.stringify(t.referringEntries || [])}

- Write from this evidence; the research is done. Read the referring entries, the schema and recent entries in the category, and open a source only to check the wording of a quotation. If the entry needs a fact the claims don't hold, leave it out and list it in your gaps for the reviewer; don't go looking for it.
- Length: published ${c.category} entries run ${c.length_guide ? `${c.length_guide.median} words at the median and ${c.length_guide.p90} at the 90th percentile` : 'about the Vault median'} (the article, without frontmatter or the source list). Aim within that range. Go longer only when the evidence supports it, and say why in your gaps; a thinly sourced subject gets a short entry, never padding.
- Follow the frontmatter schema in src/content.config.ts and the shape of recent entries in the same category. Set ai_generated: true and reviewed: false. Every date in the frontmatter must agree with the prose.
- Concrete, plain British English for a curious reader: lead with what the subject is and why it mattered; explain any term a newcomer won't know; no hype or aphorisms. Keep process and evidence talk out of the article; the Sources section carries it.
- Link to existing Vault entries where the prose names them. Don't link to entries that don't exist.
- Add an image only under the specification's rights rules (an original diagram with a manifest under capture/vault/, never a borrowed photograph, portrait or screenshot). Leave it out if unsure.
- Change no other file. Then list existing entries with an unlinked mention of this subject that should link to it: the entry path and the exact existing words.
- Run \`node scripts/check-vault-sources.mjs --strict\` and \`npx vale src/content/vault/${t.path}.mdx\` in the website checkout and fix what they report in your file.`, {
    label: `draft ${t.path}`,
    phase: 'Draft',
    schema: DRAFT,
  }).then(d => ({ triage: t, draft: d })),
  (r, c) => !r.draft ? r : agent(`Check the draft Vault entry ${prep.website}/src/content/vault/${r.draft.path}.mdx against its evidence. You did not write it; read it as a sceptical reviewer.
${RULES}
Recorded claims and sources: ${JSON.stringify({ sources: r.triage.sources, claims: r.triage.claims })}

For every factual statement in the entry, including frontmatter dates and names, find the recorded claim and source that supports it, and check the source yourself where you can. Where a statement goes beyond its evidence, remove it or qualify it in the file. You may only remove or qualify; never add a new claim. Return the claims as they now stand (corrected where your reading of the sources changed them) and anything a human reviewer should look at.`, {
    label: `check ${r.draft.path}`,
    phase: 'Check claims',
    schema: CHECKED,
  }).then(k => ({ ...r, checked: k })),
)

const done = results.filter(Boolean)
const lost = prep.candidates.filter(c => !done.some(r => r.triage && r.triage.id === c.id)).map(c => c.id)
if (lost.length) log(`No result for ${lost.join(', ')}: they stay out of this batch and keep their queue status.`)
if (!done.length) return { stopped: 'triage', detail: 'no candidate produced a result', worktrees: [prep.docs, prep.website] }
const ids = done.map(r => r.triage.id)

phase('Integrate')
const integrated = await agent(`Integrate a Vault batch. Website worktree: ${prep.website}. Docs worktree: ${prep.docs}. Review directory: ${prep.website}/${REVIEW}.
${RULES}
Results per candidate (triage, draft and claim check): ${JSON.stringify(done)}

1. Backlinks: in each existing entry named in a draft's backlinks, wrap the exact existing words in a link to /vault/<path>. Change nothing else in those files: no new words, no frontmatter, no review flags. Every new entry needs at least one incoming link; if none of the proposed ones work, look for another existing unlinked mention. Record each, added or rejected with the reason.
2. Writing issues: for each write decision, search open and closed code198x/website issues by ID, subject and aliases and reuse a match; otherwise create "Write the Vault entry for <subject> (<id>)" with the labels enhancement and area:curriculum and the outline in docs vault-candidates.md "Open an issue when ready". Issues are public the moment they exist: write each title and body to a file outside the worktrees and run \`python3 scripts/vault_batch_gates.py --scan <file>\` from the docs worktree first, and create the issue only when it passes.
3. Queue rows in ${prep.docs}/vault-candidates.csv (Python csv module; keep the header and order): write → in-progress with the issue URL; covered → covered with covered_by; deferred → deferred; blocked → blocked with blocked_by. Record triage notes (scope, coverage checked, source leads; no local paths) and corrected scope axes. Add followups that have no entry or candidate yet as needs-triage rows with the next IDs, after checking titles, aliases and the queue for an existing match. Anywhere the queue refers to one of this batch's new entries (a new row's link_from, or an existing row gaining one), write candidate:<that entry's ID>, never its path: the docs branch is checked against website main, where the drafts don't exist until they are published.
4. Evidence in ${REVIEW}/: triage.json ([{id, decision, path, issue, notes}] for exactly these IDs: ${ids.join(', ')}), claims.json ([{entry, claim, evidence, single_source, qualification}] using the checked claims), backlinks.json ([{from, to, result, label|note}]), followups.json ([{subject, decision, id|existing, referringEntries}]) and REPORT.md: what the batch covers, decisions, sources and their limits, connections, the drafters' gaps, each entry's article length against its category guide, and the claim checker's concerns for the reviewer. Leave a "## Verification" heading for the gates.
5. Run \`python3 scripts/check_vault_candidates.py --website ${prep.website}\` in the docs worktree and fix any failure in what you wrote. Do not commit.`, {
  label: 'integrate',
  schema: {
    type: 'object',
    properties: {
      written: { type: 'array', items: { type: 'string' } },
      issues: { type: 'array', items: { type: 'string' } },
      newCandidates: { type: 'array', items: { type: 'string' } },
      backlinksAdded: { type: 'number' },
      problems: { type: 'array', items: { type: 'string' } },
    },
    required: ['written', 'issues', 'newCandidates', 'backlinksAdded', 'problems'],
  },
})

phase('Gates')
const attempt = A.attempt || 1
const gates = await agent(`Run the Vault batch gates (attempt ${attempt}). Change no files.

In ${prep.docs} run:
  python3 scripts/vault_batch_gates.py --website ${prep.website} --review ${REVIEW} --ids ${ids.join(' ')} --drafts-only
It runs the website's full release check, which takes several minutes; let it finish. Return its exit code and its complete output verbatim.`, {
  label: `gates (attempt ${attempt})`,
  schema: {
    type: 'object',
    properties: { exitCode: { type: 'number' }, output: { type: 'string' } },
    required: ['exitCode', 'output'],
  },
})
if (!gates || gates.exitCode !== 0) {
  log('The batch failed its gates. Nothing was committed or pushed.')
  return {
    stopped: 'gates',
    gates,
    integrated,
    worktrees: { docs: prep.docs, website: prep.website },
    next: 'Fix the failure in the worktrees, then resume this run with the same args plus attempt: ' + (attempt + 1),
  }
}

phase('Pull requests')
const prs = await agent(`Open draft pull requests for a Vault batch that has passed its gates (attempt ${attempt}). Website worktree: ${prep.website}. Docs worktree: ${prep.docs}. Review directory: ${REVIEW}.

Gate output:
${gates.output}

1. Capture every new entry (${(integrated && integrated.written || []).join(', ')}) at desktop 1440×1000 and phone (Pixel 7) from the built site served with \`npx astro preview --port 4431\`, into ${REVIEW}/screenshots/. Look at each capture; report any page that renders wrongly instead of opening the PR. Stop the preview server afterwards.
2. Fill the "## Verification" section of ${REVIEW}/REPORT.md from the gate output, with numbers, not adjectives.
3. Commit in each worktree, staging explicit paths only (never \`git add -A\`): the website's new entries, linked entries, images, manifests and ${REVIEW}; the docs' vault-candidates.csv. Commit titles describe the effect for a reader (for example "Explain N subjects in new Vault drafts"); bodies say why and list the IDs.
4. Before pushing, write each commit message and both PR descriptions to files outside the worktrees and run \`python3 scripts/vault_batch_gates.py --scan <files>\` from the docs worktree. The repositories are public: if it reports a private path, rewrite the text (amend the commit message if needed) until it passes. Never push past a failure.
5. Push both branches and open both as draft PRs. The website PR summarises the batch, links ${REVIEW}/REPORT.md and the docs PR, and says the entries stay unreviewed until a person approves them. Comment the website PR link on each writing issue.
6. Confirm both branches are on the remote at the commits you made, then remove both worktrees with \`git worktree remove\` (not --force) and delete their build caches.

Return the PR URLs.`, {
  label: 'pull requests',
  schema: {
    type: 'object',
    properties: { website: { type: 'string' }, docs: { type: 'string' }, problems: { type: 'array', items: { type: 'string' } } },
    required: ['website', 'docs', 'problems'],
  },
})

return { batch: prep.slug, candidates: ids, lost, integrated, prs }
