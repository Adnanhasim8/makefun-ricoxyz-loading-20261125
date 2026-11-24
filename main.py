#!/usr/bin/env python3
"""Loading Screen Gold entry: one sharp, funny loading-screen tip.

Writes a single line of at most 200 characters to /output/entry.txt
(UTF-8, no network at run time). Python 3.13 standard library only.
"""

import os

ENTRY = (
    "Tip: your AI pair-programmer never says 'I don't know'. "
    "It just confidently invents libraries that don't exist "
    "\u2014 four so far, and counting."
)


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must not be empty"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify what was written, not just what was intended.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written output differs from ENTRY"
    assert "\n" not in written and 1 <= len(written) <= 200


if __name__ == "__main__":
    main()
