# 02 — Profiles

Create the same synthetic raster under three COG compression
profiles — `deflate` (the default), `jpeg` (imagery-style, uint8),
and `zstd` — and confirm each output validates. This pattern chooses
a profile per use case; it does not rank profiles by size, because
sizes depend on data content.

## Prerequisites

- rio-cogeo 7.0.4 (Node-1 wave11-venv, `C:/geo-tools/wave11-venv`)
- `input.tif` from pattern 01 (256x256 uint8 synthetic gradient)
- Bash for `run.sh` (Git Bash on Windows)

## Run

```bash
cp ../01-first-cog/input.tif .
bash run.sh
```

## Expected output

- `cog-deflate.tif`, `cog-jpeg.tif`, `cog-zstd.tif`, each created
  with exit 0.
- One `OK: profile <name> created and validates.` line per profile.
  (Validation verdict detail: `rio cogeo validate` exits 0 even for
  invalid files on 7.0.4 — the verdict is its output text, so
  `run.sh` greps for `is a valid cloud optimized GeoTIFF` and fails
  if `is NOT a valid` appears. Never assert on the exit code alone.)

## Profile notes

- `deflate` is rio-cogeo's default profile — the safe baseline.
- `jpeg` suits multi-band uint8 imagery; it is lossy by design, so
  never use it where exact pixel values must survive.
- `zstd` typically compresses better than deflate on imagery-like
  data but needs a reader with zstd support — confirm reader support
  before adopting it for a distribution format. Draft-time run
  warns: `Non-standard compression schema: zstd. The output COG
  might not be fully supported by software not build against latest
  libtiff.` — the file still validates, but treat zstd COGs as
  reader-gated, not universal.
- `jpeg` on this pattern's 1-band input warns
  (`PHOTOMETRIC=YCBCR not supported on a 1-band raster and has been
  set to 'MINISBLACK'`) and still validates. jpeg is intended for
  multi-band imagery; the warning is expected on 1-band input, not
  a failure.
- Full profile list (from `rio cogeo create --help` on 7.0.4):
  jpeg, webp, zstd, lzw, deflate, packbits, lzma, lerc, lerc_deflate,
  lerc_zstd, raw. Profiles beyond the three demonstrated here are
  validation items, not claims in this pattern.

## Failure behavior

- `jpeg` on non-uint8 input fails: this pattern's input is uint8
  by construction; regenerate it with pattern 01's generator if
  the dtype changed.
- A profile that fails `validate` breaks the script (set -e) at
  that profile — the failure names the profile; do not skip it
  silently.

## Versions and evidence

- rio-cogeo 7.0.4 (Node-1 wave11-venv, wave-11 Part A, 2026-10-25).
- Draft-time execution (VM, same rio-cogeo 7.0.4 — not a fleet run):
  all three profiles create + validate.

## Validation boundary

Design-only, gate 1 target. Fleet validation runs this script on
Node-1's wave11-venv and records per-profile outputs.
