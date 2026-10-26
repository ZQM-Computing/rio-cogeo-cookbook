# 01 — First COG

Create a Cloud Optimized GeoTIFF from a synthetic GeoTIFF with
`rio cogeo create`, then inspect the result with `rio cogeo info`.
The input is a 2048x2048 uint8 diagonal gradient — not real imagery —
so no data licensing or place questions arise.

## Prerequisites

- rio-cogeo 7.0.4 + rasterio 1.5.2 (Node-1 wave11-venv,
  `C:/geo-tools/wave11-venv`)
- Python 3.12.10; invoke the venv Python by its full path, never
  Node-1's bare `python`
- Bash for `run.sh` (Git Bash on Windows), or run the two `rio`
  commands directly

## Run

```bash
C:/geo-tools/wave11-venv/Scripts/python.exe gen_tiff.py
bash run.sh
```

## Expected output

- `input.tif` (2048x2048 uint8) and `output.tif` (COG).
- `rio cogeo create` exits 0.
- `rio cogeo info output.tif` reports `COG: True`, `Tiled: True`,
  `LAYOUT: COG`, block size 512x512, overview factors [2, 4], and
  MinZoom 11 / MaxZoom 14 (draft-time observed values for the 2048
  input; fleet validation re-records them).

## Failure behavior

- `rio` not found: the venv Scripts dir is not on PATH — invoke
  `C:/geo-tools/wave11-venv/Scripts/rio.exe` by full path.
- Non-COG input (e.g. a corrupt TIFF): `rio cogeo create` fails
  before writing output; regenerate `input.tif` with `gen_tiff.py`.

## Versions and evidence

- rio-cogeo 7.0.4, rasterio 1.5.2 (Node-1 wave11-venv, wave-11 Part A,
  2026-10-25; import-verified there).
- Draft-time execution (VM, same rio-cogeo 7.0.4 / rasterio 1.5.2 —
  not a fleet run): create + info succeed; the CLI spellings above
  are the installed CLI's own (`rio cogeo create/info/validate`).

## Validation boundary

Design-only, gate 1 target. Fleet validation runs this pair on
Node-1's wave11-venv and records the exact `info` output.
