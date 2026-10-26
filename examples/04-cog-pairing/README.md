# 04 — COG pairing (TiTiler)

Take a COG built by pattern 01 and show how it pairs with TiTiler:
the URL shapes for info, bounds, statistics, and tiles, plus the
local `rio cogeo info` check proving the file carries the tiling and
overviews a tile server needs. This pattern contacts no server and
asserts no TiTiler host or port — the base URL is a placeholder.

## Prerequisites

- rio-cogeo 7.0.4 (Node-1 wave11-venv, `C:/geo-tools/wave11-venv`)
- `output.tif` from pattern 01
- titiler-cookbook for the server side

## Run

```bash
C:/geo-tools/wave11-venv/Scripts/python.exe titiler_urls.py ../01-first-cog/output.tif
```

## Expected output

- The `rio cogeo info` block for the COG (tiled layout + overviews).
- Four URL shapes under the placeholder base: `/cog/info`,
  `/cog/bounds`, `/cog/statistics`, `/cog/tiles/{z}/{x}/{y}.png`,
  each with a `url=` parameter pointing at the COG.

## Failure behavior

- `rio cogeo info` failing: the COG is missing or not readable —
  rebuild it with pattern 01 before drawing any serving conclusion.
- A real TiTiler returning errors for these shapes: check that the
  TiTiler instance serves the COG path given in `url=`; endpoint
  spellings are confirmed against titiler-cookbook at gate-3
  validation.

## Versions and evidence

- rio-cogeo 7.0.4 (Node-1 wave11-venv, wave-11 Part A, 2026-10-25).
- Draft-time execution (VM, same rio-cogeo 7.0.4 — not a fleet run):
  info + URL shapes print as above; no server was contacted.

## Validation boundary

Design-only, gate 1 target. Fleet validation runs this script on
Node-1's wave11-venv, then checks the URL shapes against a TiTiler
the validator controls and records any spelling corrections.
