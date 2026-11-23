#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (max 240 chars) to /output/entry.txt.
Deterministic: Python 3.13 stdlib only, no network, no clock,
no randomness. Set OUTPUT_DIR to redirect the output locally.
"""

import os
from pathlib import Path

SETUP = "While I was stealing cars in GTA 6,"
DISASTER = "my coding agent deleted the entire test suite,"
REWRITE = "rewrote the README to say tests are a form of self-doubt,"
PUNCHLINE = "and pushed it all to main."

ENTRY = " ".join([SETUP, DISASTER, REWRITE, PUNCHLINE])

MIN_LEN = 1
MAX_LEN = 240


def output_dir() -> Path:
    """Resolve the output directory, defaulting to /output."""
    return Path(os.environ.get("OUTPUT_DIR", "/output"))


def validate(text: str) -> None:
    """Check the entry is one sentence of 1-240 characters."""
    assert MIN_LEN <= len(text) <= MAX_LEN, f"entry is {len(text)} chars"
    assert text.count(".") == 1, "must be a single sentence"
    assert text.endswith("."), "entry must end with a period"
    assert "  " not in text, "entry must not contain double spaces"
    assert text == text.strip(), "entry must not have edge whitespace"


def write_entry(text: str, directory: Path) -> Path:
    """Write the entry plus a trailing newline; return the file path."""
    target = directory / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text + "\n", encoding="utf-8")
    return target


def main() -> None:
    validate(ENTRY)
    path = write_entry(ENTRY, output_dir())
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
