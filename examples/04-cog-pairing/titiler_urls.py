"""Build TiTiler URL shapes for a COG, without contacting any server.

TILESERVER_BASE is a placeholder: this pattern asserts no TiTiler host
or port. Point it at a TiTiler you control to use the URLs for real.
The local check (rio cogeo info) proves the COG carries the tiling
and overviews a tile server needs; it does not prove any server
serves it.

Usage:
    TILESERVER_BASE=http://localhost:8000 python3 titiler_urls.py ../01-first-cog/output.tif
"""

import os
import subprocess
import sys

BASE = os.environ.get("TILESERVER_BASE", "http://TILESERVER-PLACEHOLDER:8000")
RIO = os.environ.get("RIO", "rio")


def main():
    cog = sys.argv[1] if len(sys.argv) > 1 else "../01-first-cog/output.tif"
    info = subprocess.run(
        [RIO, "cogeo", "info", cog], capture_output=True, text=True
    )
    print("rio cogeo info (tiling/overviews the server needs):")
    print(info.stdout.strip() or "(no info output)")
    if info.returncode != 0:
        raise SystemExit(f"FAIL: rio cogeo info failed for {cog}.")
    print()
    print("TiTiler URL shapes (placeholder base, no server contacted):")
    for path in (
        "/cog/info",
        "/cog/bounds",
        "/cog/statistics",
        "/cog/tiles/{z}/{x}/{y}.png",
    ):
        print(f"  {BASE}{path}?url=file://{cog}")


if __name__ == "__main__":
    main()
