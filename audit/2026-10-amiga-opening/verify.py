"""Validate source consistency without treating it as an execution pass."""

import argparse
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent


def read(name: str) -> Any:
    return json.loads((ROOT / name).read_text())


def git_bytes(repo: Path, revision: str, path: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), "show", revision + ":" + path])


def check_hash(data: bytes, expected: str) -> None:
    assert hashlib.sha256(data).hexdigest() == expected, "Source hash mismatch"


def check_typing(source: bytes, actions: list[dict[str, Any]]) -> None:
    typed = "".join(action["text"] for action in actions if action["action"] == "type_string")
    assert typed and typed == source.decode(), "Typed payload differs from source"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--website", required=True, type=Path)
    parser.add_argument("--samples", required=True, type=Path)
    args = parser.parse_args()
    record = read("source.json")
    assert record["counts"] == {"amos": {"mdx": 19, "units": 17}, "blitz": {"mdx": 17, "units": 15}}
    assert len(record["website"]) == 46 and len(record["samples"]) == 19
    for group, repo, revision in [("website", args.website, record["websiteRevision"]), ("samples", args.samples, record["samplesRevision"])]:
        for path, digest in record[group].items():
            check_hash(git_bytes(repo, revision, path), digest)
    selected = record["opening"]
    assert len(selected) == 6 and {(row["language"], row["unit"]) for row in selected} == {(lang, unit) for lang in ["amos", "blitz"] for unit in [1, 2, 3]}
    for row in selected:
        source = git_bytes(args.samples, record["samplesRevision"], row["sample"])
        actions = json.loads(git_bytes(args.samples, record["samplesRevision"], row["driver"]))
        check_typing(source, actions)
        lesson = git_bytes(args.website, record["websiteRevision"], row["lesson"]).decode()
        assert re.findall(r'<CodeFromFile\s+src="([^"]+)"', lesson) == [row["sample"]]
        manifest = json.loads(git_bytes(args.samples, record["samplesRevision"], row["manifest"]))
        assert manifest["captures"][0]["program"] == Path(row["sample"]).name
        assert manifest["machine"] == row["machineAlias"]
        assert row["freshExecution"] == "not performed"
    broken = copy.deepcopy(actions)
    next(action for action in broken if action["action"] == "type_string")["text"] += "wrong"
    for callback in [lambda: check_typing(source, broken), lambda: check_hash(source, "0" * 64)]:
        try:
            callback()
        except AssertionError:
            pass
        else:
            raise AssertionError("Negative control unexpectedly passed")
    upstream = read("upstream.json")["sources"]
    assert len(upstream) == 2 and all(re.fullmatch(r"[a-f0-9]{40}", item["revision"]) for item in upstream)
    findings = read("findings.json")
    assert len(findings) == 3 and len({item["url"] for item in findings}) == 3
    for item in findings:
        assert "/issues/" in item["url"] and "#116" in item["body"]
    report = (ROOT / "REPORT.md").read_text()
    assert record["websiteRevision"] in report and record["samplesRevision"] in report and record["docsBaseline"] in report
    for target in re.findall(r"\]\(([^)]+)\)", report):
        if "://" not in target and not target.startswith("#"):
            assert (ROOT / target.split("#")[0]).exists(), target
    manifest = (ROOT / "SHA256SUMS").read_text().splitlines()
    assert manifest
    for entry in manifest:
        digest, path = entry.split("  ", 1)
        check_hash((ROOT / path).read_bytes(), digest)
    print(json.dumps({"status": "passed source/evidence checks", "selectedPages": 10, "openingUnits": 6, "exactTypedSources": 6, "retainedSourceHashes": 65, "filedFindings": 3, "negativeControlsRejected": 2, "runtime": "not performed", "manifestEntries": len(manifest)}))


if __name__ == "__main__":
    main()
