#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
MANIFEST_PATH="$ROOT_DIR/out/release/release_manifest.json"

if [[ ! -f "$MANIFEST_PATH" ]]; then
  echo "[ERROR] manifest not found: $MANIFEST_PATH"
  exit 1
fi

if [[ -n "${OTS_BIN:-}" && -x "${OTS_BIN:-}" ]]; then
  FOUND_OTS="$OTS_BIN"
elif command -v ots >/dev/null 2>&1; then
  FOUND_OTS="$(command -v ots)"
elif command -v pyenv >/dev/null 2>&1 && pyenv which ots >/dev/null 2>&1; then
  FOUND_OTS="$(pyenv which ots)"
else
  echo "[ERROR] ots command not found in PATH"
  echo "Try one of these:"
  echo "  python3 -m pip install opentimestamps-client"
  echo "  pyenv rehash"
  echo "  which ots"
  exit 1
fi

echo "[OK] Using ots: $FOUND_OTS"

rm -f "${MANIFEST_PATH}.ots"
"$FOUND_OTS" stamp "$MANIFEST_PATH"

if [[ ! -f "${MANIFEST_PATH}.ots" ]]; then
  echo "[ERROR] failed to create ${MANIFEST_PATH}.ots"
  exit 1
fi

echo "[OK] OpenTimestamps stamp created: ${MANIFEST_PATH}.ots"
