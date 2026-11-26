"""Write the entry for u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a.

One funny line, taped to the door of a haunted server room: a warning
sign about the ghost that has been on call since 2003. Deterministic:
the same bytes on every run.
"""

import os

ENTRY = (
    "WARNING: The ghost in Rack 4 has been on call since 2003. "
    "It answers pages. It never closes tickets."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
