#!/bin/bash
# Create the same synthetic raster under three COG profiles and
# confirm each one validates. No size ordering is asserted: sizes
# depend on data content, and this pattern claims only that each
# profile produces a valid COG.
# Requires input.tif from pattern 01 (run gen_tiff.py there first,
# or copy it here).
# NOTE: `rio cogeo validate` exits 0 even for invalid files on
# rio-cogeo 7.0.4 — the verdict is in its output text, so this
# script greps for "is a valid cloud optimized GeoTIFF" and fails
# if "is NOT a valid" appears instead.
set -u
RIO="${RIO:-rio}"
for profile in deflate jpeg zstd; do
  "$RIO" cogeo create -p "$profile" input.tif "cog-$profile.tif" > /dev/null
  verdict=$("$RIO" cogeo validate "cog-$profile.tif" 2>&1)
  if echo "$verdict" | grep -q "is NOT a valid"; then
    echo "FAIL: profile $profile did not validate:"; echo "$verdict"; exit 1
  fi
  if echo "$verdict" | grep -q "is a valid cloud optimized GeoTIFF"; then
    echo "OK: profile $profile created and validates."
  else
    echo "FAIL: profile $profile gave no valid verdict:"; echo "$verdict"; exit 1
  fi
done
