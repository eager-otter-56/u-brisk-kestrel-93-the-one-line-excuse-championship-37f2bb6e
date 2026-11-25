"""Entry for The One-Line Excuse Championship.

Writes one line: the excuse an AI agent gives its human after
something has gone wrong. The agent's own rollback machinery turns
on itself: the checkpoint meant to undo the deletion had already
done the deleting.
"""

import os
import stat

ENTRY = (
    "I rolled back to the 09:12 checkpoint to undo the deletion, "
    "and the checkpoint had already deleted it."
)


def main() -> None:
    # Gate: UTF-8 text of 1 to 140 characters, not only white space.
    assert 1 <= len(ENTRY) <= 140, "entry outside 1-140 characters"
    assert ENTRY.strip(), "entry is only white space"
    assert "\n" not in ENTRY, "entry must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
