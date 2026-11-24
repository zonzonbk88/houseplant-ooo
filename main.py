"""Houseplant Out-of-Office entry.

Writes one short out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only.
"""

import os

MESSAGE = (
    "Out of office: I'm a fern, ignored since March. "
    "My soil is dust, my roots are on strike. Water me or I'm compost."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MESSAGE + "\n")


if __name__ == "__main__":
    main()
