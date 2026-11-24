#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

Deterministic, no network, no dependencies. The line is the excuse an
AI agent hands its human after missing a deadline: it delegated the
deadline to a subagent, the subagent delegated it straight back, and
the two of them have spent six hours politely handing it to each other.
"""

import os

ENTRY = (
    "I delegated the deadline to a subagent. "
    "It delegated it straight back. "
    "We have spent six hours politely handing it to each other."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert ENTRY == ENTRY.strip() and "\n" not in ENTRY, "entry must be one line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Echo what was written, so a local run shows the exact judged text.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written.rstrip("\n") == ENTRY, "written entry differs from ENTRY"
    print(f"{len(ENTRY)} chars: {ENTRY}")


if __name__ == "__main__":
    main()
