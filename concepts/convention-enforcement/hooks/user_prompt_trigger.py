#!/usr/bin/env python3
"""
User Prompt Trigger — UserPromptSubmit Hook Template.
Detects specific phrases in user messages and injects context hints.

Hook protocol:
  stdin: JSON with "message" field
  stdout: text context for the AI (empty = no trigger)
  exit 0 always (non-blocking)
"""
import json
import re
import sys

TRIGGERS = [
    (
        re.compile(r"merged|PR\s*through|is\s*merged|PR\s*#?\d+\s*merged", re.IGNORECASE),
        "[TRIGGER] Merge confirmed. Run your post-merge protocol now.",
    ),
    (
        re.compile(r"new\s*impulse|external\s*input|recalibrate", re.IGNORECASE),
        "[TRIGGER] External input detected. Run your intake protocol.",
    ),
    # Add more:
    # (re.compile(r"pattern", re.IGNORECASE), "[TRIGGER] Your hint."),
]


def main():
    try:
        data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, EOFError):
        return
    message = data.get("message", "")
    if not message:
        return
    hints = [hint for pattern, hint in TRIGGERS if pattern.search(message)]
    if hints:
        print("\n".join(hints))


if __name__ == "__main__":
    main()
