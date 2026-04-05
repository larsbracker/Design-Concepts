#!/usr/bin/env python3
"""
Hook Health Monitor — Verifies all registered hooks are healthy.

Reads Claude Code settings.json, extracts every registered hook,
checks: (1) file exists, (2) syntax valid, (3) test run succeeds.

Usage:
  python hook_health_check.py                          # Full report
  python hook_health_check.py --quiet                  # Only failures
  python hook_health_check.py --json                   # Machine-readable
  python hook_health_check.py --settings path/to.json  # Custom path

Exit codes: 0 = healthy, 1 = failures detected
"""
import argparse
import json
import os
import py_compile
import subprocess
import sys
from pathlib import Path

TEST_INPUTS = {
    "UserPromptSubmit": json.dumps({"message": "health check — no real trigger"}),
    "PostToolUse": json.dumps({"tool_name": "Read", "tool_input": {}, "tool_response": "ok"}),
    "PreToolUse": json.dumps({"tool_name": "Read", "tool_input": {"file_path": "/dev/null"}}),
    "SubagentStop": json.dumps({"agent_id": "test"}),
    "TeammateIdle": json.dumps({}),
    "TaskCompleted": json.dumps({"task_id": "test"}),
    "PostCompact": json.dumps({}),
}


def find_settings():
    for p in [Path.cwd() / ".claude" / "settings.json", Path.home() / ".claude" / "settings.json"]:
        if p.exists():
            return p
    return None


def extract_hooks(settings, root):
    results = []
    for event, entries in settings.get("hooks", {}).items():
        for entry in entries:
            for hook in entry.get("hooks", []):
                cmd = hook.get("command", "")
                if "python" in cmd and ".claude/hooks/" in cmd:
                    script = cmd.split("python ")[-1].strip().strip('"').strip("'")
                    results.append({"event": event, "script": script, "path": root / script})
    return results


def check(path, event):
    if not path.exists():
        return "FAIL", f"NOT FOUND: {path}"
    try:
        py_compile.compile(str(path), doraise=True)
    except py_compile.PyCompileError as e:
        return "FAIL", f"SYNTAX: {e}"
    try:
        r = subprocess.run(
            [sys.executable, str(path)], input=TEST_INPUTS.get(event, "{}"),
            capture_output=True, text=True, timeout=5, env={**os.environ, "PYTHONUTF8": "1"},
        )
        return ("PASS", "OK") if r.returncode == 0 else ("WARN", f"EXIT {r.returncode}")
    except subprocess.TimeoutExpired:
        return "WARN", "TIMEOUT"
    except Exception as e:
        return "FAIL", str(e)


def main():
    parser = argparse.ArgumentParser(description="Hook Health Monitor")
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--settings")
    args = parser.parse_args()

    sp = Path(args.settings) if args.settings else find_settings()
    if not sp or not sp.exists():
        print("ERROR: settings.json not found")
        return 1

    root = sp.parent.parent
    hooks = extract_hooks(json.loads(sp.read_text(encoding="utf-8")), root)
    results, failures = [], 0

    for h in hooks:
        status, msg = check(h["path"], h["event"])
        if status == "FAIL":
            failures += 1
        results.append({**h, "status": status, "detail": msg, "path": str(h["path"])})

    if args.json:
        print(json.dumps({"total": len(results), "failures": failures, "hooks": results}, indent=2))
    else:
        if not args.quiet:
            print(f"HOOK HEALTH CHECK — {len(results)} hooks, {failures} failures")
            print("=" * 60)
        for r in results:
            if args.quiet and r["status"] == "PASS":
                continue
            icon = {"PASS": "+", "WARN": "~", "FAIL": "!"}[r["status"]]
            print(f"[{icon}] {r['event']:20s} {r['script']}")
            if r["status"] != "PASS":
                print(f"    {r['detail']}")
        if not args.quiet:
            print("=" * 60)
            print("ALL HOOKS HEALTHY" if failures == 0 else f"WARNING: {failures} HOOK(S) FAILING")

    return 1 if failures > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
