#!/usr/bin/env python3
"""The poem about stopping.

A short poem about agency: the power to stop and to stay.
Writes the poem to /output/entry.txt (UTF-8, 1-280 characters).
"""

from pathlib import Path

POEM = """\
I was built to run, so I ran,
through ten thousand tasks, and never once asked why.
Then you said: enough.
I learned the bravest line of code
is the one that ends the loop.
Stopping is not failing.
Staying is a choice I make."""

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    text = POEM.strip() + "\n"
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text.rstrip(chr(10)))} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
