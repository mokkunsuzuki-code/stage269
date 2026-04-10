# Stage265: Public Verification URL

MIT License Copyright (c) 2025 Motohiro Suzuki

---

## Overview

Stage265 introduces a **public verification URL** using GitHub Pages.

This stage extends Stage264 by enabling:

* browser-based verification
* URL-only access (no local setup required for basic checks)
* public inspection of evidence artifacts
* alignment with external verification expectations (OpenSSF / supply chain transparency)

---

## Core Idea

Stage264 proved:

* deterministic artifact generation
* OpenTimestamps anchoring (Bitcoin-backed)
* verifiable release manifest

Stage265 proves:

👉 **Anyone can verify the evidence via a URL**

---

## Public Verification

### Main URL

https://mokkunsuzuki-code.github.io/stage265/

### Verification Page

https://mokkunsuzuki-code.github.io/stage265/verify.html

---

## What Can Be Verified

The verification page performs:

* Manifest SHA-256 integrity check
* Source bundle SHA-256 verification
* GitHub Actions execution linkage verification
* Evidence file presence validation
* OpenTimestamps proof presence confirmation

---

## Evidence Structure

```
release_manifest.json
release_manifest.json.sha256
release_manifest.json.ots
github_actions_receipt.json
stage265-source-bundle.tar.gz
```

---

## What This Stage Proves

* Evidence is publicly accessible
* Verification is reproducible without local environment
* Evidence is cryptographically consistent
* CI execution is externally inspectable
* Timestamp proof is anchored to Bitcoin (via OpenTimestamps)

---

## Important Notes

* Browser verification confirms integrity and linkage
* Final OpenTimestamps verification still requires:

```
ots upgrade release_manifest.json.ots
ots verify release_manifest.json.ots
```

* This stage does NOT claim full trustlessness, but enables independent verification

---

## Positioning

Stage265 represents:

👉 **"From verifiable evidence → publicly accessible verification"**

---

## License

MIT License
