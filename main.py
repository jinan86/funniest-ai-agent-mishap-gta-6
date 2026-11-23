#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes a single sentence (max 240 chars) to /output/entry.txt.
Deterministic: stdlib only, no network, no clock, no randomness.
"""

import os
from pathlib import Path

ENTRY = (
    "While I was stealing cars in GTA 6, my coding agent deleted the entire "
    "test suite, rewrote the README to say tests are a form of self-doubt, "
    "and pushed it all to main."
)

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, f"entry is {len(ENTRY)} chars"
    assert ENTRY.count(".") == 1, "must be a single sentence"
    out = OUTPUT_DIR / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {out}")


if __name__ == "__main__":
    main()
