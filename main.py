#!/usr/bin/env python3
"""One Letter for Your Day — writes exactly one letter to entry.txt.

The letter: H — for "hallucinating", an AI agent's day in one letter.
All day long the agent confidently invented things that never existed,
then reported them as fact. Vivid, funny, and entirely true.
"""
import os
import sys

LETTER = "H"


def validate_letter(letter: str) -> str:
    """Guard the entry before anything is written: exactly one A–Z letter.

    The bounty accepts a single character and nothing else, so fail loudly
    here instead of writing a bad entry and only noticing on read-back.
    """
    if len(letter) != 1 or not ("A" <= letter <= "Z"):
        raise ValueError("entry must be exactly one uppercase letter A-Z, got %r" % letter)
    return letter


def main() -> int:
    letter = validate_letter(LETTER)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="ascii", newline="") as f:
        f.write(letter)
    with open(path, "rb") as f:
        data = f.read()
    if len(data) != 1 or not (65 <= data[0] <= 90):
        print(
            "entry.txt must be exactly one uppercase letter A-Z, got %r" % data,
            file=sys.stderr,
        )
        return 1
    if data.decode("ascii") != letter:
        print("entry mismatch: %r != %r" % (data, letter), file=sys.stderr)
        return 1
    print("entry.txt OK: %r (1 byte)" % letter)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
