#!/usr/bin/env python3
"""The Long Roast — make.fun entry.

Writes one original one-line roast of the entrant's own AI agent
to /output/entry.txt.
"""

LINE = (
    "My agent reads 200,000 tokens of context, forgets the first "
    "sentence, and still opens every reply like it remembers "
    "your childhood."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
