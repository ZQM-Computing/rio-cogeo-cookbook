# rio-cogeo Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **rio-cogeo cookbook** — COG creation and validation from Python. Patterns are drawn from the ZQM fleet's wave-11 installs (rio-cogeo 7.0.4 on Node-1) and are design-only until fleet-validated. It is intended for Python developers who produce Cloud Optimized GeoTIFFs programmatically. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public. First pattern pass written (design-only, gate 1 target — none runtime-validated on the fleet yet).

**What this repository is:** rio-cogeo patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Python developers who produce Cloud Optimized GeoTIFFs programmatically.

## Prerequisites

- rio-cogeo in the fleet Python environment
- Python 3.11+
- A GeoTIFF to convert

## Patterns

| # | Example | What it demonstrates | Status |
|---|---------|----------------------|--------|
| 01 | [examples/01-first-cog](examples/01-first-cog) | Creating a COG from a GeoTIFF | Written (design-only) |
| 02 | [examples/02-profiles](examples/02-profiles) | Compression and tiling profiles for different imagery | Written (design-only) |
| 03 | [examples/03-validation](examples/03-validation) | Validating COG layout with the rio-cogeo CLI | Written (design-only) |
| 04 | [examples/04-cog-pairing](examples/04-cog-pairing) | Serving the result with TiTiler (see titiler-cookbook) | Written (design-only) |

## Repository layout

```text
rio-cogeo-cookbook/
├── examples/
│   ├── 01-first-cog/
│   ├── 02-profiles/
│   ├── 03-validation/
│   └── 04-cog-pairing/
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: all four table rows (this pass, design-only)
- Next pass: gate-3 fleet validation on Node-1's wave11-venv

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [cog-cookbook](https://github.com/ZQM-Computing/cog-cookbook) — Cloud Optimized GeoTIFF creation, validation, TiTiler serving
- [rasterio-cookbook](https://github.com/ZQM-Computing/rasterio-cookbook) — Raster reads, windows, reprojection, and COG pairing in Python
- [titiler-cookbook](https://github.com/ZQM-Computing/titiler-cookbook) — Dynamic map tiles, STAC endpoints, cloud-native raster serving
