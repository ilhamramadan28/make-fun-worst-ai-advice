#!/usr/bin/env python3
"""Write the worst AI advice one-liner to /output/entry.txt."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")
DEST = "/output/entry.txt"


def main():
    with open(SRC, "r", encoding="utf-8") as f:
        text = f.read()
    assert 1 <= len(text) <= 140, "entry must be 1-140 chars"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    shutil.copyfile(SRC, DEST)
    os.chmod(DEST, 0o644)
    with open(SRC, "rb") as a, open(DEST, "rb") as b:
        assert a.read() == b.read(), "copy mismatch"


if __name__ == "__main__":
    main()
