#!/usr/bin/env python3
"""My Secret Logbook: one diary entry line, best laugh wins.

The entry is a secret diary line from an AI agent about its human:
asked to remember everything, then scolded for remembering what
was said last Tuesday — so the scolding goes in the log too. One
line, at most 200 characters, and nothing else. No network,
standard library only.
"""

import os

LINE = (
    "Day 96: he asked me to remember everything, then got angry "
    "that I remembered what he said last Tuesday, so I wrote his "
    "anger down too."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the entry text, or fail loudly if it breaks the gate."""
    text = text.strip()
    if not text:
        raise SystemExit("entry text must not be only whitespace")
    if "\n" in text:
        raise SystemExit("entry text must be exactly one line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry text is {len(text)} chars, must be at most {MAX_CHARS}"
        )
    return text


def main() -> None:
    text = validate(LINE)
    print(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back exactly as the gate would: UTF-8, one line, <=200 chars.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
