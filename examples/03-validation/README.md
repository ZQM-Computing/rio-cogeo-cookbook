# 03 — Validation

Validate a good COG (must pass) and a deliberately non-COG control
file (must fail). The control is the same synthetic gradient written
stripped (untiled) with no overviews, so `rio cogeo validate` must
reject it. This is the CLI-side validation flow; it complements
rasterio-cookbook 04, which checks COG layout from Python — the two
patterns do not duplicate each other.

## Prerequisites

- rio-cogeo 7.0.4 + rasterio 1.5.2 (Node-1 wave11-venv,
  `C:/geo-tools/wave11-venv`)
- `output.tif` from pattern 01
- Bash for `run.sh` (Git Bash on Windows)

## Run

```bash
RIO=C:/geo-tools/wave11-venv/Scripts/rio.exe \
PY=C:/geo-tools/wave11-venv/Scripts/python.exe bash run.sh
```

## Expected output

- `OK: COG validates.` for pattern 01's output.
- `OK: untiled control rejected as expected.` for `untiled.tif`,
  with `rio cogeo validate`'s own findings printed after that line
  (on 7.0.4: a warning that the file exceeds 512px without internal
  overviews, and an error that it exceeds 512px but is not tiled).
- Verdict detail that changes how this script is written:
  `rio cogeo validate` exits 0 even for invalid files on 7.0.4 —
  the verdict is its output text (`is a valid cloud optimized
  GeoTIFF` vs `is NOT a valid ...`). `run.sh` asserts on the
  verdict string, never on the exit code. Any future pattern that
  gates on `validate` must do the same.

## Failure behavior

- COG failing validation: the script exits 1 with `FAIL` — the
  pattern 01 output is not a valid COG; regenerate it before
  trusting any downstream step.
- Untiled control passing validation: the script exits 1 with
  `FAIL` — the negative control is broken, and a passing validate
  can no longer be trusted as evidence.

## Versions and evidence

- rio-cogeo 7.0.4 (Node-1 wave11-venv, wave-11 Part A, 2026-10-25).
- Draft-time execution (VM, same rio-cogeo 7.0.4 — not a fleet run):
  pass/fail pair behaves as above; exact validate findings are
  recorded at gate-3 validation.

## Validation boundary

Design-only, gate 1 target. Fleet validation runs this script on
Node-1's wave11-venv against pattern 01's fleet-built COG and
records the exact validate output for both files.
