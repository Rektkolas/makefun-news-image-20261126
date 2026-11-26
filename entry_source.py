import os
import shutil
from pathlib import Path

HERE = Path(__file__).parent
BUNDLED = HERE / "entry.png"


def destination():
    env = os.getenv("ENTRY_OUTPUT")
    if env:
        return Path(env)
    return Path("/output") / "entry.png"


def run():
    out = destination()
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(BUNDLED, "rb") as src, open(out, "wb") as dst:
            shutil.copyfileobj(src, dst)
    except OSError:
        alt = Path("output") / "entry.png"
        alt.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(BUNDLED, alt)


if __name__ == "__main__":
    run()
