"""Check immutable sources, retained native observations, objective/task counts and links."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent.parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_bytes(repo: Path, revision: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{revision}:{path}"], cwd=repo)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--website", type=Path, required=True)
    parser.add_argument("--samples", type=Path, required=True)
    parser.add_argument("--emulator", type=Path, required=True)
    args = parser.parse_args()
    inventory = json.loads((HERE / "source-inventory.json").read_text())
    units = inventory["units"]
    require([u["unit"] for u in units] == list(range(1, 12)), "Missing authored units")
    require(len({u["path"] for u in units}) == 11, "Duplicate authored units")
    samples = {}
    for unit in units:
        source = git_bytes(args.website, inventory["website_revision"], unit["path"])
        require(sha(source) == unit["sha256"], "Lesson identity changed")
        includes = re.findall(r'<CodeFromFile src="([^"]+)"', source.decode())
        require(unit["sample_sources"], "Missing source owner")
        if unit["unit"] <= 5:
            require(
                includes == [s["path"] for s in unit["sample_sources"]],
                "Sample includes differ from inventory",
            )
        else:
            require(
                len(unit["sample_sources"]) == 6
                and f"step={{{unit['unit'] - 5}}}" in source.decode(),
                "Missing aiming files/step",
            )
        for sample in unit["sample_sources"]:
            data = git_bytes(
                args.samples, inventory["samples_revision"], sample["path"]
            )
            require(sha(data) == sample["sha256"], "Sample identity changed")
            require(
                (args.samples / sample["path"]).read_bytes() == data,
                "Executed checkout differs from recorded sample",
            )
            samples[sample["path"]] = sample["sha256"]
    for path, expected in inventory["integration_sources"].items():
        require(
            sha(git_bytes(args.website, inventory["website_revision"], path))
            == expected,
            "Integration identity changed",
        )
    native = json.loads((HERE / "native-shares.json").read_text())
    require(
        native["status"] == "passed" and len(native["cases"]) == 7,
        "Missing passed native cases",
    )
    require(
        native["emulator_sha256"] == sha(args.emulator.read_bytes()),
        "Emulator identity changed",
    )
    require(
        native["verifier_sha256"] == sha((HERE / "verify-shares.py").read_bytes()),
        "Native verifier identity changed",
    )
    source_path = (
        "sinclair-zx-spectrum/basic/dice-roller/teaching/shares/dice-roller.bas"
    )
    require(native["source_sha256"] == samples[source_path], "Executed source differs")
    for path, expected in native["driver_hashes"].items():
        require(
            sha(git_bytes(args.samples, inventory["samples_revision"], path))
            == expected,
            "Driver identity changed",
        )
    spec = spec_from_file_location("probability_checks", HERE / "verify-shares.py")
    require(spec is not None and spec.loader is not None, "Missing case checker")
    checker = module_from_spec(spec)
    spec.loader.exec_module(checker)
    for case in native["cases"]:
        checker.check_case(case)
    require(
        sum(c["kind"].startswith("ordinary") for c in native["cases"]) == 3,
        "Missing ordinary RUN observations",
    )
    require(
        len(native["diagnostic_commands"]) == 4
        and native["negative_control"]["rejected"]
        and native["altered_display_rejected"],
        "Missing diagnostic/known-red records",
    )
    try:
        checker.check_case({"counts": [], "total": 0})
    except AssertionError:
        empty_rejected = True
    else:
        raise AssertionError("Empty observation accepted")
    stored = json.loads((HERE / "stored-lines.json").read_text())
    source = git_bytes(
        args.samples, inventory["samples_revision"], source_path
    ).decode()
    require(
        {int(n) for n in stored}
        == {int(line.split()[0]) for line in source.splitlines()},
        "Missing stored program lines",
    )
    require(all(len(data) > 0 for data in stored.values()), "Empty stored line")
    objective_rows = re.findall(
        r"^\| (\d{2}) ", (HERE / "OBJECTIVES.md").read_text(), re.MULTILINE
    )
    require(
        objective_rows == [f"{i:02}" for i in range(1, 12)], "Missing objective rows"
    )
    for filename in ["LEARNER-TASKS.md", "ASSESSOR.md"]:
        tasks = re.findall(r"^(\d)\. ", (HERE / filename).read_text(), re.MULTILINE)
        require(tasks == list("123456"), "Missing learner/assessor tasks")
    links = 0
    for path in [
        *HERE.glob("*.md"),
        DOCS / "README.md",
        DOCS / "audit/2026-10-foundations-coverage.md",
        DOCS / "specifications/maths-for-games.md",
    ]:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if "://" not in target and not target.startswith("#"):
                require(
                    (path.parent / target.split("#")[0]).exists(),
                    f"Missing local link: {path}: {target}",
                )
                links += 1
    require(links > 30, "No meaningful local-link coverage")
    result = {
        "status": "passed",
        "authored_units": 11,
        "probability_units": 5,
        "aiming_units": 6,
        "unique_sample_files": len(samples),
        "native_cases": 7,
        "ordinary_runs": 3,
        "diagnostic_fixtures": 4,
        "known_red_controls_rejected": 2,
        "empty_observation_rejected": empty_rejected,
        "objective_rows": 11,
        "learner_tasks": 6,
        "assessor_entries": 6,
        "local_links_checked": links,
        "fresh_browser_runs": 0,
        "learner_observations": 0,
    }
    (HERE / "validation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
