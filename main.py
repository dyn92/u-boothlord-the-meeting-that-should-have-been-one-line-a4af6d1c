#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line - entry program.

Writes one sentence to /output/entry.txt (override the path with the
ENTRY_OUTPUT environment variable for local testing).

The sentence was written by hand in the build session, chosen for the
judge's brief: it is the single sentence that could have replaced an
entire pointless meeting. It kills the meeting outright - the decision
was already "yes", so there is nothing left to meet about - it is
relatable to anyone who has sat through a meeting that should have
been an email, and it lands as a joke with a turn: the email itself
shrinks to a single word.

Pure Python standard library, deterministic: the same bytes come out
on every run. The program self-checks its output before exiting: the
text must be 1-200 characters, a single line, with no leading or
trailing whitespace; it then reads the file back and verifies the
bytes on disk are exactly what was written.
"""

import os
import sys

LINE = (
    "This meeting could have been an email, and the email "
    "could have been a single word: yes."
)

MIN_CHARS = 1
MAX_CHARS = 200
DEFAULT_OUTPUT = "/output/entry.txt"


def self_check(line: str) -> None:
    """Validate the line against the competition gate before writing."""
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(
            "line is %d characters, gate requires %d-%d"
            % (len(line), MIN_CHARS, MAX_CHARS)
        )
    if line.strip() != line:
        raise ValueError("line has leading or trailing whitespace")
    if not line.strip():
        raise ValueError("line is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if "  " in line:
        raise ValueError("line has doubled spaces")


def main() -> int:
    try:
        self_check(LINE)
    except ValueError as exc:
        print("self-check failed: %s" % exc, file=sys.stderr)
        return 1
    output = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    parent = os.path.dirname(output)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    with open(output, "r", encoding="utf-8") as handle:
        on_disk = handle.read()
    if on_disk != LINE:
        print("verify failed: bytes on disk differ", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(LINE), output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
