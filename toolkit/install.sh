#!/bin/sh
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3.9+ is required. Install it from python.org, then retry." >&2
  exit 1
fi
exec python3 "$root/scripts/install.py"
