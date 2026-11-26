#!/usr/bin/env python3
"""Copy the bundled entry.png to the requested output location.

The destination comes from the ENTRY_OUTPUT environment variable when it
is set; otherwise the image lands at /output/entry.png. If writing there
fails with an OSError, the program falls back to ./output/entry.png
relative to the current working directory.
"""

import os
import shutil
from pathlib import Path


def resolve_destination() -> Path:
    chosen = os.environ.get("ENTRY_OUTPUT")
    if chosen:
        return Path(chosen)
    return Path("/output/entry.png")


def deliver(source_png: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source_png, destination)


def main() -> None:
    source_png = Path(__file__).resolve().parent / "entry.png"
    try:
        deliver(source_png, resolve_destination())
    except OSError:
        fallback = Path.cwd() / "output" / "entry.png"
        deliver(source_png, fallback)


if __name__ == "__main__":
    main()
