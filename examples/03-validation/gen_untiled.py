"""Write a deliberately non-COG control file: stripped (untiled) layout.

Same synthetic gradient as pattern 01, but written without tiling and
without overviews, so `rio cogeo validate` must reject it. This is the
negative control for the validate pattern.
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
    "tiled": False,
}
with rasterio.open("untiled.tif", "w", **profile) as dst:
    dst.write(data, 1)
print("Wrote untiled.tif: stripped layout, no overviews (control file).")
