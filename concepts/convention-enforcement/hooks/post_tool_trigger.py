#!/usr/bin/env python3
"""
Post-Tool Trigger — PostToolUse Hook Template.
Detects specific tool events and injects reminders.

Hook protocol:
  stdin: JSON with "tool_name", "tool_input", "tool_response"
  stdout: text context for the AI (empty = no trigger)
  exit 0 always (non-blocking)
"""
import json
import re
import sys

TRIGGERS = [
    ("Bash", re.compile(r"git commit"), "[TRIGGER] Commit detected. Run post-commit checks."),
    ("Bash", re.compile(r"git merge|git pull"), "[TRIGGER] Merge detected. Run post-merge checks."),
    # Add more:
    # ("Write", re.compile(r"\.env|credentials"), "[TRIGGER] Sensitive file written."),
]


def main():
    try:
        data = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, EOFError):
        return
    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})
    command = tool_input.get("command", "") if isinstance(tool_input, dict) else str(tool_input)
    hints = [hint for t, p, hint in TRIGGERS if tool_name == t and p.search(command)]
    if hints:
        print("\n".join(hints))


if __name__ == "__main__":
    main()
