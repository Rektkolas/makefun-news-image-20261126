"""Entry program: copies the bundled entry.png to the output path."""
from pathlib import Path
import os
import shutil

ASSET = Path(__file__).resolve().parent / "entry.png"


def target() -> Path:
    raw = os.environ.get("ENTRY_OUTPUT")
    return Path(raw) if raw else Path("/output/entry.png")


def main() -> None:
    dest = target()
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ASSET, dest)
    except OSError:
        fallback = Path.cwd() / "output" / "entry.png"
        fallback.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ASSET, fallback)


if __name__ == "__main__":
    main()
