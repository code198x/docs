"""Run every gate a Vault batch must pass; exit non-zero if any fails.

A batch is a website branch with new drafts, a docs branch with the queue's
updated rows, and a review directory in the website (docs/reviews/<slug>/)
holding the evidence the vault-batch workflow records:

- triage.json: one record per candidate: {id, decision, path?, issue?, notes}.
  decision is write, covered, deferred or blocked.
- claims.json: [{entry, claim, evidence: [...], single_source?, qualification}].
- backlinks.json and followups.json: what was linked and what was queued.

The gates check the evidence agrees with the files, that existing entries only
gained links, that a planted broken link fails the link check, and then run the
website's full release check and inspect the built pages. Run from the docs
branch of the batch:

    python3.13 scripts/vault_batch_gates.py --website ../website-batch \\
        --review docs/reviews/2026-11-07-example --ids VC-0142 VC-2076

--skip-release leaves out the release check and the built-page gate; the result
is then INCOMPLETE (exit 3), never a pass. Website CI runs it that way on every
pull request that adds a review directory, and accepts only exit 3: the release
check is local, and 2 is what a usage error returns.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

from check_vault_candidates import ROOT, load_backlog

DECISIONS = {"write", "covered", "deferred", "blocked"}
STATUS_FOR = {"write": "in-progress", "covered": "covered", "deferred": "deferred", "blocked": "blocked"}
# What a batch may change in the website, besides the review directory itself.
ALLOWED = ("src/content/vault/", "public/images/vault/", "capture/vault/")
VAULT_LINK = re.compile(r"\[([^\]]*)\]\(/vault/[^)\s]*\)")
CONTROL = "[link control](/vault/vault-batch-deliberate-broken-link-control)"
Run = Callable[[list[str], Path], subprocess.CompletedProcess]
# Not 2: argparse exits 2 on a usage error, and CI must not mistake one for the other.
INCOMPLETE = 3


def run(command: list[str], cwd: Path, env: dict[str, str] | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=False, env=env)


def git(website: Path, *args: str) -> str:
    result = run(["git", *args], website)
    if result.returncode != 0:
        raise ValueError(f"git {' '.join(args)}: {result.stderr.strip()}")
    return result.stdout


def front(text: str) -> str:
    parts = text.split("---")
    return parts[1] if text.startswith("---") and len(parts) > 2 else ""


def flag(text: str, key: str) -> str | None:
    match = re.search(rf"^{key}:[ \t]*(\S+)[ \t]*$", front(text), re.M)
    return match.group(1) if match else None


def load_review(review: Path) -> tuple[list[dict], list[dict]]:
    triage = json.loads((review / "triage.json").read_text(encoding="utf-8"))
    claims = json.loads((review / "claims.json").read_text(encoding="utf-8"))
    for name in ("backlinks.json", "followups.json"):
        json.loads((review / name).read_text(encoding="utf-8"))
    if not isinstance(triage, list) or not isinstance(claims, list):
        raise ValueError("triage.json and claims.json must each hold a list")
    return triage, claims


def check_triage(triage: list[dict], ids: list[str]) -> list[str]:
    failures = []
    seen = [record.get("id") for record in triage]
    for item in ids:
        if seen.count(item) != 1:
            failures.append(f"{item}: needs exactly one triage record, found {seen.count(item)}")
    for record in triage:
        label = record.get("id", "?")
        if record.get("id") not in ids:
            failures.append(f"{label}: triage record for a candidate outside the batch")
        if record.get("decision") not in DECISIONS:
            failures.append(f"{label}: unknown decision {record.get('decision')!r}")
        if not record.get("notes"):
            failures.append(f"{label}: triage needs notes")
        if record.get("decision") == "write" and not re.fullmatch(r"[a-z0-9-]+/[a-z0-9-]+", record.get("path", "")):
            failures.append(f"{label}: a written entry needs its category/slug path")
    return failures


def written(triage: list[dict]) -> list[str]:
    return [record["path"] for record in triage if record.get("decision") == "write" and record.get("path")]


def check_entries(website: Path, base: str, paths: list[str]) -> list[str]:
    failures = []
    for path in paths:
        relative = f"src/content/vault/{path}.mdx"
        source = website / relative
        if not source.is_file():
            failures.append(f"{path}: entry file missing")
            continue
        text = source.read_text(encoding="utf-8")
        if flag(text, "ai_generated") != "true":
            failures.append(f"{path}: must be marked ai_generated: true")
        if flag(text, "reviewed") != "false":
            failures.append(f"{path}: must stay reviewed: false until a person approves it")
        if run(["git", "cat-file", "-e", f"{base}:{relative}"], website).returncode == 0:
            failures.append(f"{path}: already exists on the base branch; a batch writes new entries")
    return failures


def check_claims(claims: list[dict], paths: list[str]) -> list[str]:
    failures = []
    for path in paths:
        if not any(claim.get("entry") == path for claim in claims):
            failures.append(f"{path}: no claims recorded")
    for number, claim in enumerate(claims, 1):
        label = f"{claim.get('entry', '?')} claim {number}"
        if claim.get("entry") not in paths:
            failures.append(f"{label}: names an entry the batch didn't write")
        evidence = claim.get("evidence") or []
        if not claim.get("claim") or not evidence:
            failures.append(f"{label}: needs the claim and at least one source")
        elif len(evidence) == 1 and claim.get("single_source") is not True:
            failures.append(f"{label}: one source; find a second or mark it single_source")
    return failures


def check_incoming(website: Path, paths: list[str]) -> list[str]:
    """A draft nobody links to can't be found; each needs a link from another page."""
    failures = []
    pages = [p for p in (website / "src").rglob("*") if p.suffix in {".mdx", ".md", ".astro"} and p.is_file()]
    texts = {page: page.read_text(encoding="utf-8") for page in pages}
    for path in paths:
        own = website / f"src/content/vault/{path}.mdx"
        target = re.compile(rf"/vault/{re.escape(path)}(?:[#/)\"'\s]|$)")
        if not any(target.search(text) for page, text in texts.items() if page != own):
            failures.append(f"{path}: no incoming link from any other page")
    return failures


def unlinked(text: str) -> str:
    return VAULT_LINK.sub(r"\1", text)


def check_scope_and_preservation(website: Path, base: str, review: str, paths: list[str]) -> list[str]:
    """Outside its own files, a batch may only change existing entries by wrapping text in Vault links."""
    failures = []
    new = {f"src/content/vault/{path}.mdx" for path in paths}
    changed = git(website, "diff", "--name-status", "--no-renames", base, "--").splitlines()
    changed += [f"A\t{name}" for name in git(website, "ls-files", "--others", "--exclude-standard").splitlines()]
    for line in changed:
        status, name = line.split("\t", 1)
        if name.startswith(review.rstrip("/") + "/") or name in new:
            continue
        if not name.startswith(ALLOWED):
            failures.append(f"{name}: outside what a Vault batch may change")
            continue
        if status == "A" and name.startswith("src/content/vault/"):
            failures.append(f"{name}: a new entry with no triage record")
            continue
        if status != "M" or not name.startswith("src/content/vault/"):
            if status != "A":
                failures.append(f"{name}: a batch may not delete or rename existing files")
            continue
        before = git(website, "show", f"{base}:{name}")
        after = (website / name).read_text(encoding="utf-8")
        if unlinked(before) != unlinked(after):
            failures.append(f"{name}: changed beyond adding Vault links")
    return failures


def link_control(website: Path, entry: str, runner: Run = run) -> list[str]:
    """Plant a broken link in a draft: the link check must fail, then pass once it's removed."""
    source = website / f"src/content/vault/{entry}.mdx"
    original = source.read_bytes()
    command = ["node", "scripts/check-vault-links.mjs"]
    try:
        source.write_bytes(original + f"\n{CONTROL}\n".encode())
        planted = runner(command, website)
    finally:
        source.write_bytes(original)
    restored = runner(command, website)
    failures = []
    if planted.returncode == 0:
        failures.append("link control: the link check passed with a planted broken link")
    if restored.returncode != 0:
        failures.append(f"link control: the link check fails on the batch itself:\n{restored.stdout}{restored.stderr}")
    return failures


def check_queue(docs: Path, website: Path, triage: list[dict]) -> list[str]:
    try:
        rows = {row["id"]: row for row in load_backlog(docs / "vault-candidates.csv", website)}
    except ValueError as error:
        return [f"queue: {error}"]
    failures = []
    for record in triage:
        row = rows.get(record.get("id"))
        if row is None:
            continue
        want = STATUS_FOR.get(record.get("decision"))
        if row["status"] != want:
            failures.append(f"{row['id']}: queue says {row['status']}, triage says {record.get('decision')} ({want})")
        if record.get("decision") == "write" and record.get("issue") != row["issue"]:
            failures.append(f"{row['id']}: triage and queue name different writing issues")
    return failures


def check_built(website: Path, paths: list[str]) -> list[str]:
    failures = []
    dist = website / "dist"
    sitemap = "".join(p.read_text(encoding="utf-8") for p in dist.glob("sitemap*.xml"))
    if not sitemap:
        failures.append("built site has no sitemap to check")
    for path in paths:
        page = dist / "vault" / path / "index.html"
        if not page.is_file():
            failures.append(f"{path}: not in the built site")
            continue
        if not re.search(r'<meta name="robots" content="noindex', page.read_text(encoding="utf-8")):
            failures.append(f"{path}: built page lacks noindex")
        if re.search(rf"/vault/{re.escape(path)}/?<", sitemap):
            failures.append(f"{path}: unreviewed entry is in the sitemap")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--website", type=Path, required=True, help="the batch's website checkout")
    parser.add_argument("--review", required=True, help="review directory, relative to the website")
    parser.add_argument("--ids", nargs="+", required=True, metavar="VC-NNNN")
    parser.add_argument("--base", default="origin/main", help="website ref the batch starts from")
    parser.add_argument("--skip-release", action="store_true", help="leave out the slow release check")
    args = parser.parse_args()
    website = args.website.resolve()
    gates: list[tuple[str, Callable[[], list[str]]]] = []
    try:
        base = git(website, "merge-base", "HEAD", args.base).strip()
        triage, claims = load_review(website / args.review)
    except (OSError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    paths = written(triage)
    gates = [
        ("triage covers the batch", lambda: check_triage(triage, args.ids)),
        ("drafts are new, AI-marked and unreviewed", lambda: check_entries(website, base, paths)),
        ("every claim has its sources", lambda: check_claims(claims, paths)),
        ("every draft has an incoming link", lambda: check_incoming(website, paths)),
        ("existing entries only gained links", lambda: check_scope_and_preservation(website, base, args.review, paths)),
        ("queue agrees with triage", lambda: check_queue(ROOT, website, triage)),
        (
            "queue tests",
            lambda: [] if (r := run([sys.executable, "-m", "unittest", "discover", "-s", "scripts", "-p", "test_*.py"], ROOT)).returncode == 0
            else [r.stderr[-2000:]],
        ),
    ]
    if paths:
        gates.append(("a planted broken link fails", lambda: link_control(website, paths[0])))
    if not args.skip_release:
        env = os.environ | {"PLAYWRIGHT_PORT": os.environ.get("PLAYWRIGHT_PORT", "4431")}
        gates.append(
            (
                "website release check",
                lambda: [] if (r := run(["npm", "run", "check:release"], website, env)).returncode == 0
                else [f"npm run check:release exited {r.returncode}:\n{(r.stdout + r.stderr)[-4000:]}"],
            )
        )
        gates.append(("built drafts are noindex and out of the sitemap", lambda: check_built(website, paths)))
    failed = False
    for name, gate in gates:
        try:
            failures = gate()
        except (OSError, ValueError, json.JSONDecodeError) as error:
            failures = [str(error)]
        print(f"{'FAIL' if failures else 'pass'}  {name}")
        for failure in failures:
            print(f"      {failure}")
        failed = failed or bool(failures)
    if failed:
        print("FAIL: the batch is not ready for review")
        return 1
    if args.skip_release:
        print("INCOMPLETE: the release check and built pages were skipped")
        return INCOMPLETE
    print(f"PASS: {len(paths)} drafts and {len(triage)} triage decisions ready for review")
    return 0


if __name__ == "__main__":
    sys.exit(main())
