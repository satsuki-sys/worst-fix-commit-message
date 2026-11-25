#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes a single commit message for a bug fix that made everything
worse to /output/entry.txt. Stdlib only, no network, no input files.
"""

import os

ENTRY = "fix: fixed the crash by making the app quit first"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 100, f"entry is {len(text)} chars, over the 100 cap"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
