"""Propose Vault candidates related to one existing Vault entry.

Step 5 of the content factory plan. Three sources, strongest first:

- the entry's own prose: names it emphasises that have no entry yet (the same
  rules as the website's vault-candidates.mjs, applied to one entry);
- the knowledge graph (reference/_tools/facts.sqlite through
  ops/scripts/knowledge.py): publishers, developers, games and people related
  to the entry's own identity, with the evidence for each;
- the queue: existing candidates the entry names whose link_from lacks it.

It never creates entries, and never merges identities. A name that matches
more than one graph identity, or nearly matches something that already
exists, comes back as a question. By default it only prints proposals;
--apply appends the new candidates and link_from additions to
vault-candidates.csv, for review as a pull request.

The graph lives in the umbrella's reference/ library, so this runs locally,
not in CI.
"""

import argparse
import csv
import io
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

from check_vault_candidates import FIELDS, load_backlog, paths

ROOT = Path(__file__).resolve().parent.parent
UMBRELLA = ROOT.parent.parent
GRAPH_LIMIT = 10

# Words emphasised constantly that are not subjects; kept in step with
# code198x/website scripts/vault-candidates.mjs.
STOP = {
    "crash", "sinclair-user", "your-sinclair", "zzap-64", "the-games-machine", "ace", "c-vg",
    "yes", "no", "not", "and", "but", "the", "a", "an", "producer", "author", "retail-price",
    "spectrum", "zx-spectrum", "commodore-64", "amiga", "not-rated", "unrateable",
    "graphics", "sound", "developer", "publisher", "designer", "director", "animation",
    "community", "innovation", "cost", "quality", "resolution", "style", "games", "born",
    "documentation", "preservation", "distribution", "music", "gameplay", "price",
    "legacy", "purpose", "origin", "setting", "platform", "platforms", "company",
    "status", "role", "era", "players", "sales", "cpu", "memory", "speed", "colour", "color",
    "c64", "snes", "nes", "pc", "arcade", "uk", "us", "japan", "europe", "britain",
}
# Graph entity types that can stand for an entry of each Vault category.
# In order of preference: the subject's identity is the most specific type
# that matches. Choosing which record to read is not a merge; two identities of
# the same type still come back as a question.
CATEGORY_TYPES = {
    "games": ["game"],
    "companies": ["company", "publisher", "advertiser"],
    "people": ["person"],
    "systems": ["machine", "machine_family", "platform"],
    "hardware": ["machine", "machine_family"],
    "groups": ["group"],
    "magazines": ["magazine"],
}
GRAPH_MIN_RECORDS = 2
TYPE_CATEGORY = {
    "game": "games", "company": "companies", "publisher": "companies", "advertiser": "companies",
    "person": "people", "machine": "systems", "machine_family": "systems", "platform": "systems",
    "group": "groups", "magazine": "magazines",
}
NEIGHBOUR_RELATIONS = {"published", "published_by", "developed", "credited_with", "released_by"}


def norm(name: str) -> str:
    name = name.lower().replace("’", "").replace("'", "").replace("&", "and")
    # "The Dark Wheel" and "Dark Wheel" are one name.
    return re.sub(r"^the-", "", re.sub(r"[^a-z0-9]+", "-", name).strip("-"))


def tidy(name: str) -> str:
    """Graph names are often in capitals; give them ordinary case, keeping numerals."""
    if name != name.upper():
        return name
    return " ".join(w if re.fullmatch(r"[IVX]+|\d.*", w) else w.capitalize() for w in name.split())


@dataclass
class Proposal:
    subject: str
    category: str
    source: str
    evidence: str


@dataclass
class Expansion:
    entry: str
    new: list[Proposal] = field(default_factory=list)
    link_from: list[tuple[str, str]] = field(default_factory=list)  # (candidate ID, subject)
    questions: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


class Known:
    """Everything that already has a name: entries, redirects and candidates."""

    def __init__(self, website: Path, rows: list[dict[str, str]]):
        self.entries: dict[str, str] = {}
        for entry in (website / "src/content/vault").glob("*/*.mdx"):
            path = f"{entry.parent.name}/{entry.stem}"
            self.entries[norm(entry.stem)] = path
            title = re.search(r'^title:\s*"?(.+?)"?\s*$', front(entry.read_text(encoding="utf-8")), re.M)
            if title:
                self.entries[norm(title.group(1))] = path
        config = (website / "astro.config.mjs").read_text(encoding="utf-8")
        for old in re.findall(r"['\"]/vault/[a-z0-9-]+/([a-z0-9-]+)/?['\"]\s*:", config):
            self.entries.setdefault(norm(old), f"(redirect) {old}")
        self.candidates: dict[str, dict[str, str]] = {}
        for row in rows:
            for part in subject_parts(row["subject"]):
                self.candidates.setdefault(norm(part), row)

    def match(self, name: str) -> tuple[str, object] | None:
        key = norm(name)
        if key in self.entries:
            return "entry", self.entries[key]
        if key in self.candidates:
            return "candidate", self.candidates[key]
        # "Jet-Pac" is the Jetpac entry and "Galaxians" the Galaxian one:
        # compare without word breaks or a final s too.
        def loose(name: str) -> str:
            squeezed = name.replace("-", "")
            return squeezed[:-1] if len(squeezed) > 4 and squeezed.endswith("s") else squeezed

        compact = loose(key)
        for known, target in self.entries.items():
            if loose(known) == compact:
                return "entry", target
        for known, row in self.candidates.items():
            if loose(known) == compact:
                return "candidate", row
        return None

    def near(self, name: str) -> str | None:
        """A known name sharing every word with this one, or the reverse."""
        words = set(norm(name).split("-"))
        if len(norm(name)) < 4:
            return None
        for key, target in [*self.entries.items(), *((k, r["id"]) for k, r in self.candidates.items())]:
            other = set(key.split("-"))
            if len(key) >= 5 and other != words and (words < other or other < words):
                return f"{key} ({target})"
        return None


def front(text: str) -> str:
    parts = text.split("---")
    return parts[1] if len(parts) > 2 else ""


def subject_parts(subject: str) -> list[str]:
    parts = [p.strip(" *'\"") for p in re.split(r",\s*| and | / |; ", subject)]
    return [p for p in parts if p] + [subject]


def prose_names(text: str) -> dict[str, int]:
    """Emphasised, capitalised names in unlinked prose, as vault-candidates.mjs finds them."""
    body = re.sub(r"\A---\n.*?\n---", "", text, flags=re.S)
    unlinked = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", body)
    marks = (
        re.findall(r"\*\*\*([^*\n]{3,50})\*\*\*", unlinked)
        + re.findall(r"\*\*([^*\n]{3,50})\*\*", unlinked)
        + re.findall(r"(?<!\*)\*([A-Z][^*\n]{2,49})\*(?!\*)", unlinked)
    )
    names: dict[str, int] = {}
    for raw in marks:
        raw = raw.strip()
        if raw.endswith(":"):
            continue  # a facts-list label (**Developer:**), not a subject
        label = raw.rstrip(".,;!?")
        if not re.match(r"[A-Z]", label) or re.match(r"\d", label) or len(label.split()) > 6:
            continue
        key = norm(label)
        if len(key) < 3 or key in STOP:
            continue
        names[label] = names.get(label, 0) + 1
    return names


def graph(knowledge: Path, *args: str, offset: int = 0) -> dict:
    # knowledge.py pages at most 100 items a call.
    out = subprocess.run(
        [sys.executable, str(knowledge), "--limit", "100", "--offset", str(offset), *args],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)


def graph_edges(knowledge: Path, entity_id: int, cap: int = 1000) -> list[dict]:
    edges: list[dict] = []
    while len(edges) < cap:
        page = graph(knowledge, "explore", "entity", str(entity_id), offset=len(edges))["edges"]
        edges.extend(page["items"])
        if not page["has_more"] or not page["items"]:
            break
    return edges


def graph_neighbours(knowledge: Path, entry: str, title: str, result: Expansion) -> list[Proposal]:
    category = entry.split("/")[0]
    types = CATEGORY_TYPES.get(category)
    if not types:
        result.notes.append(f"graph: no entity types for the {category} category")
        return []
    items = graph(knowledge, "resolve", title)["items"]
    matching = [i["entity"] for i in items if i["match"] in {"exact", "normalised_exact"} and i["entity"]["type"] in types]
    if not matching:
        result.notes.append(f"graph: no {'/'.join(types)} identity named {title!r}")
        return []
    best = min(types.index(e["type"]) for e in matching)
    exact = [e for e in matching if types.index(e["type"]) == best]
    ids = {e["id"] for e in exact}
    if len(ids) > 1:
        listed = ", ".join(f"#{e['id']} {e['type']} {e['name']!r}" for e in exact)
        result.questions.append(f"{title!r} matches {len(ids)} graph identities ({listed}); not merged, so no graph neighbours")
        return []
    subject_id = exact[0]["id"]
    counts: dict[tuple[str, str], list[str]] = {}
    for edge in graph_edges(knowledge, subject_id):
        if edge["relation"] not in NEIGHBOUR_RELATIONS:
            continue
        other = edge["destination"] if edge["source"].get("id") == subject_id else edge["source"]
        if other.get("kind") == "release":
            other = other.get("game") or {}
        name, kind = other.get("name"), other.get("type")
        if not name or kind not in TYPE_CATEGORY or other.get("suspect"):
            continue
        if re.fullmatch(r"[^,]+, [^,]+", name):
            continue  # a catalogue's "Surname, Forename": a person filed as a publisher
        evidence = edge.get("evidence") or {}
        where = evidence.get("source") or "graph"
        page = evidence.get("recorded_page")
        counts.setdefault((tidy(name), TYPE_CATEGORY[kind]), []).append(f"{where}{f' p{page}' if page else ''}")
    ranked = sorted(counts.items(), key=lambda kv: (-len(kv[1]), kv[0][0]))
    return [
        Proposal(name, category, "graph", f"{len(found)} records, e.g. {found[0]}")
        for (name, category), found in ranked
        if len(found) >= GRAPH_MIN_RECORDS
    ]


def expand(entry: str, website: Path, rows: list[dict[str, str]], knowledge: Path | None) -> Expansion:
    file = website / "src/content/vault" / f"{entry}.mdx"
    if not file.is_file():
        raise ValueError(f"no Vault entry {entry}")
    text = file.read_text(encoding="utf-8")
    title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', front(text), re.M)
    title = title_match.group(1) if title_match else entry.split("/")[1]
    known = Known(website, rows)
    result = Expansion(entry)
    seen: set[str] = set()

    own = set(norm(title).split("-")) | set(norm(entry.split("/")[1]).split("-"))

    def consider(name: str, category: str | None, source: str, evidence: str) -> None:
        key = norm(name)
        if key in seen or key == norm(title) or key == norm(entry.split("/")[1]):
            return
        seen.add(key)
        parts = [part.strip() for part in name.split(" and ")]
        if len(parts) > 1 and not known.match(name) and all(known.match(part) for part in parts):
            # "MSX and IBM PC" names two known subjects; "Alan and Soo Maton" doesn't.
            for part in parts:
                consider(part, category, source, evidence)
            return
        if own < set(key.split("-")):
            result.notes.append(f"{name!r} extends the entry's own name (a source or edition about it); not proposed")
            return
        found = known.match(name)
        if found and found[0] == "candidate":
            row = found[1]
            if entry not in paths(row["link_from"]) and (row["id"], row["subject"]) not in result.link_from:
                result.link_from.append((row["id"], row["subject"]))
            return
        if found:
            return  # an entry already covers it; linking it is the link pass's job
        near = known.near(name)
        if near:
            result.questions.append(f"{name!r} ({source}) nearly matches {near}; not proposed")
        elif category is None:
            result.questions.append(f"{name!r} is named in the prose, but its category isn't known; not proposed")
        else:
            result.new.append(Proposal(name, category, source, evidence))

    for name, count in prose_names(text).items():
        consider(name, guess_category(knowledge, name), "prose", f"emphasised {count}× in {entry}")
    if knowledge is not None:
        added = 0
        for proposal in graph_neighbours(knowledge, entry, title, result):
            before = len(result.new)
            consider(proposal.subject, proposal.category, "graph", proposal.evidence)
            added += len(result.new) - before
            if added >= GRAPH_LIMIT:
                result.notes.append(f"graph: stopped at {GRAPH_LIMIT} new proposals, strongest evidence first")
                break
    else:
        result.notes.append("graph: not consulted (pass --knowledge or keep the umbrella's reference/ beside this repository)")
    body = re.sub(r"\[[^\]]+\]\([^)]+\)", " ", text)
    for row in rows:
        if row["status"] not in {"needs-triage", "ready", "in-progress"} or entry in paths(row["link_from"]):
            continue
        for part in subject_parts(row["subject"]):
            distinctive = len(part) >= 6 and (" " in part or re.search(r"[A-Z].*[A-Z0-9]", part))
            if distinctive and re.search(rf"(?<![\w-]){re.escape(part)}(?![\w-])", body):
                if (row["id"], row["subject"]) not in result.link_from:
                    result.link_from.append((row["id"], row["subject"]))
                break
    return result


_category_cache: dict[str, str | None] = {}


def guess_category(knowledge: Path | None, name: str) -> str | None:
    """The category of a prose name, when the graph has exactly one identity for it."""
    if knowledge is None:
        return None
    if name not in _category_cache:
        items = graph(knowledge, "resolve", name)["items"]
        # Advertisers are names in magazine adverts, too loose to type a subject.
        types = {
            i["entity"]["type"] for i in items
            if i["match"] in {"exact", "normalised_exact"} and i["entity"]["type"] != "advertiser"
        }
        categories = {TYPE_CATEGORY[t] for t in types if t in TYPE_CATEGORY}
        _category_cache[name] = categories.pop() if len(categories) == 1 else None
    return _category_cache[name]


def apply(source: Path, result: Expansion) -> int:
    """Append new candidates and link_from additions, then revalidate the whole backlog."""
    raw = source.read_text(encoding="utf-8")
    rows = list(csv.DictReader(io.StringIO(raw, newline="")))
    by_id = {row["id"]: row for row in rows}
    for candidate_id, _ in result.link_from:
        row = by_id[candidate_id]
        row["link_from"] = ";".join([*paths(row["link_from"]), result.entry])
    number = max(int(row["id"][3:]) for row in rows)
    for proposal in result.new:
        number += 1
        rows.append(dict.fromkeys(FIELDS, "") | {
            "id": f"VC-{number:04}",
            "subject": proposal.subject,
            "category": proposal.category,
            "status": "needs-triage",
            "why": f"Related to {result.entry} ({proposal.source}: {proposal.evidence})",
            "link_from": result.entry,
        })
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    source.write_text(buffer.getvalue(), encoding="utf-8")
    try:
        load_backlog(source)
    except ValueError:
        source.write_text(raw, encoding="utf-8")
        raise
    return len(result.new)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("entry", help="Vault entry path, such as companies/ultimate")
    parser.add_argument("--website", type=Path, required=True)
    parser.add_argument("--file", type=Path, default=ROOT / "vault-candidates.csv")
    parser.add_argument("--knowledge", type=Path, default=UMBRELLA / "ops/scripts/knowledge.py")
    parser.add_argument("--no-graph", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    knowledge = None if args.no_graph or not args.knowledge.is_file() else args.knowledge
    try:
        rows = load_backlog(args.file, args.website)
        result = expand(args.entry, args.website, rows, knowledge)
    except (OSError, ValueError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"Expanding {result.entry}\n")
    print(f"{len(result.new)} new candidate(s):")
    for p in result.new:
        print(f"  + {p.subject}  [{p.category}]  {p.source}: {p.evidence}")
    print(f"\n{len(result.link_from)} existing candidate(s) gain link_from {result.entry}:")
    for candidate_id, subject in result.link_from:
        print(f"  ~ {candidate_id}  {subject}")
    print(f"\n{len(result.questions)} question(s), not proposed:")
    for q in result.questions:
        print(f"  ? {q}")
    for note in result.notes:
        print(f"  ({note})")
    if args.apply:
        try:
            added = apply(args.file, result)
        except ValueError as error:
            print(f"FAIL: the backlog would be invalid, so nothing was written: {error}", file=sys.stderr)
            return 1
        print(f"\nApplied: {added} candidate(s) added, {len(result.link_from)} link_from updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
