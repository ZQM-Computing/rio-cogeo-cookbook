#!/bin/bash
# Validate a good COG (must pass) and the untiled control (must fail).
# Requires output.tif from pattern 01; generates untiled.tif here.
# NOTE: `rio cogeo validate` exits 0 even for invalid files on
# rio-cogeo 7.0.4 — the verdict is in its output text ("is a valid
# cloud optimized GeoTIFF" vs "is NOT a valid ..."), so this script
# asserts on the verdict string, never on the exit code.
# Fleet venv entry points (Node-1 wave11-venv); on Windows run from
# Git Bash with RIO/PY pointed at the venv executables, e.g.:
#   RIO=C:/geo-tools/wave11-venv/Scripts/rio.exe \
#   PY=C:/geo-tools/wave11-venv/Scripts/python.exe bash run.sh
set -u
RIO="${RIO:-rio}"
PY="${PY:-python3}"
"$PY" gen_untiled.py
good=$("$RIO" cogeo validate ../01-first-cog/output.tif 2>&1)
if echo "$good" | grep -q "is NOT a valid"; then
  echo "FAIL: COG should have validated:"; echo "$good"; exit 1
fi
echo "$good" | grep -q "is a valid cloud optimized GeoTIFF" \
  && echo "OK: COG validates." \
  || { echo "FAIL: COG gave no valid verdict:"; echo "$good"; exit 1; }
bad=$("$RIO" cogeo validate untiled.tif 2>&1)
if echo "$bad" | grep -q "is NOT a valid"; then
  echo "OK: untiled control rejected as expected."
  echo "--- control findings ---"; echo "$bad"
else
  echo "FAIL: untiled control unexpectedly validated:"; echo "$bad"; exit 1
fi
