#!/bin/bash
# Create a COG from the synthetic GeoTIFF and show its layout.
# Fleet venv entry points (Node-1 wave11-venv); on Windows run from
# Git Bash or adapt the paths to the Scripts dir executables.
set -e
RIO="${RIO:-rio}"
"$RIO" cogeo create input.tif output.tif
echo "--- rio cogeo info output.tif ---"
"$RIO" cogeo info output.tif
echo "OK: output.tif created."
