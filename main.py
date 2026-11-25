#!/usr/bin/env python3
"""Roast Your Own Agent -- make.fun entry.

Writes a single roast line (at most 140 characters) roasting this
entrant's own AI agent to /output/entry.txt.

Deterministic: no network, no clock, no randomness, no input.
"""

import os
import sys

ROAST = (
    "My agent spawned a subagent to roast itself, "
    "and the subagent came back asking for permission to be funny."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main() -> int:
    line = ROAST.strip()
    if not line or len(line) > MAX_CHARS:
        print(
            f"roast line must be 1-{MAX_CHARS} characters, got {len(line)}",
            file=sys.stderr,
        )
        return 1
    path = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_PATH
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Verify the write: the gate reads this exact file, so fail loudly
    # instead of reporting success if what landed differs from the line.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print(f"verification failed: {path} does not hold the roast line",
              file=sys.stderr)
        return 1
    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
