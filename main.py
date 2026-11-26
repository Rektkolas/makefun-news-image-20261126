"""Make.fun entry: Sum up 26 November's world news in one image. Copies entry.png to the output path."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.png")
    try:
        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        shutil.copyfile(SOURCE, path)
    except OSError:
        local_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(local_dir, exist_ok=True)
        shutil.copyfile(SOURCE, os.path.join(local_dir, "entry.png"))


if __name__ == "__main__":
    main()
