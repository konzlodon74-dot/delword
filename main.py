#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes the single word this entry would erase from the dictionary
forever to /output/entry.txt: "irregardless" -- the double-negative
non-word that somehow made it into the dictionary. Deleting it is
the punchline: the dictionary finally correcting its own mistake.
"""

import os

WORD = "irregardless"


def validate(word: str) -> None:
    """Gate: entry must be 1-77 chars, non-blank, a single word."""
    if not word or not word.strip():
        raise ValueError("entry must not be blank")
    if len(word) > 77:
        raise ValueError("entry must be at most 77 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main() -> None:
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
