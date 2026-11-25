#!/usr/bin/env python3
"""One Star for Monday entry.

Writes a single original one-star review of Monday, written as if Monday
were a restaurant, to /output/entry.txt. Stdlib only; no network, no reads
outside the repo.
"""

import os

LINE = (
    "One star. Seated by the bathroom, cold coffee, and the waiter billed "
    "us for bread we never ordered. Never returning to Monday."
)
# A real diner's complaint: bad table (by the bathroom), a dish gone wrong
# (cold coffee), a bill gone wrong (charged for bread never ordered) — and
# the punch lands on Monday itself, named twice, first as the rating and
# last as the place never to return to. One line, plain text, well under
# 25 words and 180 chars; no trailing newline in the file.


def main() -> None:
    text = LINE.strip()
    words = text.split()
    assert 1 <= len(text) <= 180, f"line is {len(text)} chars, must be 1-180"
    assert 1 <= len(words) <= 25, f"line is {len(words)} words, must be <=25"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
