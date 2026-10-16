"""Validate retained aiming boundary evidence and immutable source identities."""

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent


def read(name: str) -> Any:
    return json.loads((ROOT / name).read_text())


def check_model(result: dict[str, Any]) -> None:
    assert result["status"] == "passed" and result["policy"] == "actual"
    assert len(result["geometry"]) == 10
    assert len({item["name"] for item in result["geometry"]}) == 10
    for item in result["geometry"]:
        assert abs(item["distance"] ** 2 - item["expectedSquared"]) < 1e-10
        assert item["hit"] == item["expectedHit"]
    assert len(result["rounding"]) == len(result["directions"]) == 9
    assert all(item["actual"] == item["expected"] for item in result["rounding"] + result["directions"])
    assert result["sweep"]["combinations"] == 10800
    assert result["sweep"]["maximumStoredComponent"] <= 32767
    shots = result["shots"]
    expected = {(angle, scale) for angle in [32.8, 138.4, 248.6, 90, 318.2, 180] for scale in [4, 16, 256]}
    assert len(shots) == 18 and {(shot["angle"], shot["scale"]) for shot in shots} == expected
    assert all(shot["referenceHit"] and 0 < shot["maximumStoredPosition"] <= 2147483647 for shot in shots)
    assert all(shot["fixedHit"] for shot in shots if shot["scale"] == 256)


def git_bytes(repo: Path, revision: str, path: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), "show", f"{revision}:{path}"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--website", required=True, type=Path)
    parser.add_argument("--samples", required=True, type=Path)
    args = parser.parse_args()
    identities = read("identities.json")
    assert len(identities["units"]) == 6
    for unit in identities["units"]:
        assert unit["unchangedSinceObjectiveMap"]
        assert hashlib.sha256(git_bytes(args.website, identities["websiteRevision"], unit["path"])).hexdigest() == unit["sha256"]
    for path, digest in identities["samples"].items():
        assert hashlib.sha256(git_bytes(args.samples, identities["samplesBaseline"], path)).hexdigest() == digest
    correction = identities["samplesCorrection"]
    corrected = git_bytes(args.samples, correction["revision"], correction["path"])
    assert hashlib.sha256(corrected).hexdigest() == correction["sha256"]
    assert b"Not published" not in corrected and b"awaiting review" not in corrected
    changed = subprocess.check_output(["git", "-C", str(args.samples), "diff", "--name-only", identities["samplesBaseline"], correction["revision"]], text=True).splitlines()
    assert changed == [correction["path"]]
    result = read("model.json")
    check_model(result)
    assert result["modelSha256"] == identities["samples"]["craft/maths-for-games/aiming/model.mjs"]
    controls = read("negative-controls.json")
    assert {control["policy"] for control in controls} == {"endpoints", "line"}
    assert len(controls) == 2 and all(control["exit"] != 0 for control in controls)
    for control in controls:
        assert "wrong finite segment distance" in control["stderr"]
        assert read(f"wrong-{control['policy']}.json")["status"] == "failed"
    initial = read("initial-signed-zero-check.json")
    assert initial["status"] == "failed" and "Fractional position lost" in initial["failure"]
    assert "pass 5" in (ROOT / "existing-model-tests.txt").read_text()
    try:
        check_model(dict(result, shots=result["shots"][:-1]))
    except AssertionError:
        pass
    else:
        raise AssertionError("Missing selected shot accepted")
    links = 0
    for name in ["REPORT.md", "EXPECTED.md", "LEARNER-TASKS.md", "ASSESSOR.md"]:
        for target in re.findall(r"\]\(([^)]+)\)", (ROOT / name).read_text()):
            if "://" not in target and not target.startswith("#"):
                assert (ROOT / target.split("#")[0]).exists(), target
                links += 1
    assert links > 10
    manifest = (ROOT / "SHA256SUMS").read_text().splitlines()
    assert manifest
    for entry in manifest:
        digest, name = entry.split("  ", 1)
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    print(json.dumps({"status": "passed", "units": 6, "geometryCases": 10, "velocityGridCases": 10800, "selectedShots": 18, "rejectedWrongPolicies": 2, "missingShotRejected": True, "localLinks": links, "manifestEntries": len(manifest)}))


if __name__ == "__main__":
    main()
