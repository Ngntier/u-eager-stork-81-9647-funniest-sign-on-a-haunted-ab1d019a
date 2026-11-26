"""Funniest sign on a haunted server room door.

Writes one funny sign line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Gate: UTF-8 text, 1-120 characters,
not only whitespace.
"""

import os

ENTRY = (
    "WARNING: the ghost in this server room has root access "
    "and will page YOU at 3am."
)


def main() -> None:
    # Gate self-check: UTF-8, single line, 1-120 chars, non-blank.
    assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} outside 1-120"
    assert "\n" not in ENTRY, "entry is more than one line"
    assert ENTRY == ENTRY.strip(), "entry has leading/trailing whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
