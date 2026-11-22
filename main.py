#!/usr/bin/env python3
"""Entry for the make.fun bounty news-image-20261122.

Writes one image summing up the world news of Sunday
22 November 2026 to /output/entry.png.

The shipped image (entry.png, beside this file) was drawn by
draw_entry.py from stories cross-checked across several news
sources for that day. Drawing happens before submission because
the grading sandbox has no network and no font guarantees, so
the reliable deterministic program copies the finished image
byte for byte. Two runs always write the same bytes.

The output directory is /output in the grader; local runs may
override it with the MAKEFUN_OUTPUT_DIR environment variable.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
MAX_BYTES = 1048576


def source_image() -> Path:
    """Locate the image shipped with this repository."""
    here = Path(__file__).resolve().parent
    local = here / IMAGE_NAME
    if local.is_file():
        return local
    mounted = Path("/bot") / IMAGE_NAME
    if mounted.is_file():
        return mounted
    raise FileNotFoundError(f"{IMAGE_NAME} not found beside main.py or in /bot")


def output_path() -> Path:
    """Return the destination the grader expects."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(out_dir) / IMAGE_NAME


def main() -> int:
    src = source_image()
    dst = output_path()
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    written = dst.read_bytes()
    if written != src.read_bytes():
        raise RuntimeError("copied image does not match the source bytes")
    if len(written) > MAX_BYTES:
        raise RuntimeError("entry image exceeds the 1 MiB limit")
    print(f"wrote {dst} ({len(written)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
