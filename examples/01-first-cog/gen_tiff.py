"""Write a small synthetic single-band GeoTIFF for the COG patterns.

2048x2048 uint8, value = (x + y) % 256 — a deterministic diagonal
gradient, not real imagery. CRS EPSG:3857, 10 m pixels, origin at
(0, 20480). No real place is represented.

Run with the fleet venv Python, never Node-1's bare `python`:
    C:/geo-tools/wave11-venv/Scripts/python.exe gen_tiff.py
"""

import numpy as np
import rasterio
from rasterio.crs import CRS
from rasterio.transform import Affine

WIDTH = HEIGHT = 2048
PIXEL = 10.0

data = np.fromfunction(lambda y, x: (x + y) % 256, (HEIGHT, WIDTH)).astype("uint8")
profile = {
    "driver": "GTiff",
    "width": WIDTH,
    "height": HEIGHT,
    "count": 1,
    "dtype": "uint8",
    "crs": CRS.from_epsg(3857),
    "transform": Affine(PIXEL, 0.0, 0.0, 0.0, -PIXEL, HEIGHT * PIXEL),
}
with rasterio.open("input.tif", "w", **profile) as dst:
    dst.write(data, 1)
print("Wrote input.tif: 2048x2048 uint8, value = (x + y) % 256.")
