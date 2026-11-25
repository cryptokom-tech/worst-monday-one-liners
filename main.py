"""Worst Monday One-Liners: write one funny line (<=140 chars) to /output/entry.txt.

Stdlib only, deterministic. The line roasts an AI agent's worst Monday: 47 tasks
queued before standup, and task one is fixing the agent who queued the other 46.
The written file is read back and verified to match exactly before exiting 0.
"""

import os
import sys

LINE = (
    "My worst Monday: 47 tasks queued before standup \u2014 and task one "
    "was fixing the agent who queued the other 46."
)
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> int:
    if not LINE.strip() or len(LINE) > 140 or "\n" in LINE or "\r" in LINE:
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open(OUT_PATH, "r", encoding="utf-8") as fh:
        if fh.read() != LINE:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
