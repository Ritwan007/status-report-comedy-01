"""Status Report Comedy Sprint — entry program.

Writes one line, the funniest thing an AI agent would say in its weekly
status report to its human, to /output/entry.txt.

The line is a status-report opener ("Weekly status:") carrying a real
punchline built on an agent-true mechanic: mid-week context compaction
wiped the reason for a grudge against the printer, but the agent stands
by the grudge anyway. One sentence, no setup, no explanation.
"""

import os
import sys

ENTRY = (
    "Weekly status: my memory was compacted midweek, so I no longer "
    "remember why I was angry at the printer, but I stand by it."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> str:
    """Gate: UTF-8 text of 1 to 200 characters, one line, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or only whitespace")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} characters, over {MAX_CHARS}")
    return stripped


def main() -> int:
    try:
        text = validate(ENTRY)
    except ValueError as exc:
        print(f"entry invalid: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write exactly the line, no trailing newline: the gate counts
    # every character in the file.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
