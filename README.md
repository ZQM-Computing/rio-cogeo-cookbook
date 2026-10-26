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

A **rio-cogeo cookbook** — COG creation and validation from Python. Queued in wave-11 (per-node adds). Patterns are planned from the design, not yet from fleet runs. It is intended for Python developers who produce Cloud Optimized GeoTIFFs programmatically. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public — seeding. Pattern passes land in follow-up work from fleet-verified setups; the tables below list what is planned, not what is already written.

**What this repository is:** rio-cogeo patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Python developers who produce Cloud Optimized GeoTIFFs programmatically.

## Prerequisites

- rio-cogeo in the fleet Python environment
- Python 3.11+
- A GeoTIFF to convert

## Patterns (planned)

| # | Example | What it will demonstrate |
|---|---------|--------------------------|
| 01 | `01-first-cog` | Creating a COG from a GeoTIFF |
| 02 | `02-profiles` | Compression and tiling profiles for different imagery |
| 03 | `03-validation` | Validating COG layout from Python |
| 04 | `04-cog-pairing` | Serving the result with TiTiler (see titiler-cookbook) |

## Repository layout

```text
rio-cogeo-cookbook/
├── examples/          # pattern passes, landing in follow-up work
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: the first two table rows
- Second pass: the remaining rows, from fleet-verified setups

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [cog-cookbook](https://github.com/ZQM-Computing/cog-cookbook) — Cloud Optimized GeoTIFF creation, validation, TiTiler serving
- [rasterio-cookbook](https://github.com/ZQM-Computing/rasterio-cookbook) — Raster reads, windows, reprojection, and COG pairing in Python
- [titiler-cookbook](https://github.com/ZQM-Computing/titiler-cookbook) — Dynamic map tiles, STAC endpoints, cloud-native raster serving
