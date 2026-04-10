#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import pathlib
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "out" / "release"


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest = OUT_DIR / "release_manifest.json"
    manifest_ots = OUT_DIR / "release_manifest.json.ots"
    manifest_sha = OUT_DIR / "release_manifest.json.sha256"
    receipt = OUT_DIR / "github_actions_receipt.json"

    server_url = os.getenv("GITHUB_SERVER_URL", "https://github.com")
    repository = os.getenv("GITHUB_REPOSITORY", "")
    run_id = os.getenv("GITHUB_RUN_ID", "")

    run_url = ""
    if repository and run_id:
        run_url = f"{server_url}/{repository}/actions/runs/{run_id}"

    payload = {
        "version": 1,
        "stage": "stage264",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "github_actions": {
            "workflow": os.getenv("GITHUB_WORKFLOW", ""),
            "repository": repository,
            "run_id": run_id,
            "run_attempt": os.getenv("GITHUB_RUN_ATTEMPT", ""),
            "run_url": run_url,
            "sha": os.getenv("GITHUB_SHA", ""),
            "ref": os.getenv("GITHUB_REF", ""),
            "actor": os.getenv("GITHUB_ACTOR", ""),
        },
        "files": {
            "release_manifest.json": {
                "path": "out/release/release_manifest.json",
                "sha256": sha256_file(manifest) if manifest.exists() else "",
            },
            "release_manifest.json.sha256": {
                "path": "out/release/release_manifest.json.sha256",
                "sha256": sha256_file(manifest_sha) if manifest_sha.exists() else "",
            },
            "release_manifest.json.ots": {
                "path": "out/release/release_manifest.json.ots",
                "sha256": sha256_file(manifest_ots) if manifest_ots.exists() else "",
            },
        },
        "meaning": [
            "This receipt proves the manifest stamping pipeline ran in GitHub Actions.",
            "The manifest hash, sha256 sidecar, and ots proof are bound to this workflow execution."
        ],
    }

    receipt.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(f"[OK] wrote receipt: {receipt}")


if __name__ == "__main__":
    main()
