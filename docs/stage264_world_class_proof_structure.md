# Stage264: release_manifest.json + OpenTimestamps + GitHub Actions receipt

## Overview

Stage264 reintegrates three proof layers into a single verification structure:

1. `release_manifest.json`
2. `release_manifest.json.ots`
3. `github_actions_receipt.json`

This creates a stronger public evidence chain for independent verification.

## What each file proves

### 1. release_manifest.json
Defines exactly what artifact was produced and its SHA-256 hash.

### 2. release_manifest.json.ots
Provides an OpenTimestamps proof that the manifest existed at or before the stamping time.

### 3. github_actions_receipt.json
Proves that the same manifest stamping pipeline ran inside GitHub Actions and records run metadata.

## Why this matters

This stage moves from:

- "I made a file"

to:

- "This exact manifest existed at that time"
- "Its contents bind to a deterministic source bundle"
- "The stamping flow also ran in GitHub Actions"
- "A third party can independently re-check all of it"

## Verification

Run:

```bash
python3 tools/verify_stage264_anchor.py --dir out/release --ots-bin "$(command -v ots)"
If OpenTimestamps verification is not final yet, the .ots file still exists as evidence,
and later upgrade/final verification can strengthen the proof further.
