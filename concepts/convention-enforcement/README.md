# Convention Enforcement

**Principle:** Convention without enforcement is a silent failure waiting to happen.

## The Failure

We had 50+ custom skills in a Claude Code project. One of them — `auto-cascade` — was supposed to trigger automatically whenever someone confirmed a merge ("merged", "PR through", etc.). The trigger patterns were documented in the skill file. The protocol was clear.

It never fired.

Nobody noticed for weeks. The skill relied entirely on the AI remembering to invoke it based on trigger words in a description. The description was truncated because the context budget couldn't fit 50+ skill descriptions. The AI couldn't match the trigger. The feedback loop that was supposed to capture build knowledge after every merge — silently stopped working.

When we audited the full skill set, we found **14 out of 50 skills** had the same vulnerability: event-based triggers defined in documentation, with zero enforcement mechanism backing them.

## The Principle

There are two types of triggers in AI agent systems:

| Type | Example | Risk |
|------|---------|------|
| **Command-based** | User types `/review` | Low — explicit invocation is reliable |
| **Event-based** | "Should fire after every merge" | **High — depends on AI memory, context budget, and description matching** |

Event-based triggers that rely on the AI "remembering" will fail when:
- Context budget truncates skill descriptions (>30 skills)
- Session context is lost (new conversation)
- The trigger phrase doesn't exactly match the documentation
- The AI prioritizes the user's explicit request over background triggers

**If a trigger matters, it needs a mechanism — not a convention.**

## The 3-Layer Pattern

We solved this with three independent enforcement layers. Each layer catches failures the others miss:

```
Layer 1: HOOKS (mechanical — fires on every message/tool call)
   | fails silently after platform update?
Layer 2: MEMORY (cognitive — loaded at session start)
   | not loaded in this environment?
Layer 3: DOCUMENTATION (persistent — in project instructions)<img width="2816" height="1536" alt="Gemini_Generated_Image_oik5amoik5amoik5" src="https://github.com/user-attachments/assets/16e280c5-4acb-495b-98ae-48915004ab6a" />

   | truncated by context budget?
Layer 1: HOOKS catch it anyway
```

### Layer 1: Hooks (Mechanical Enforcement)

Small Python scripts that run on every user message or tool call. They pattern-match against trigger words and inject a context hint that the AI cannot ignore.

```python
# UserPromptSubmit hook — fires on every user message
MERGE_PATTERNS = [
    r"merged", r"PR through", r"is merged",
    r"PR\s*#?\d+\s*merged",
]

def main():
    data = json.loads(sys.stdin.read())
    message = data.get("message", "")
    if MERGE_RE.search(message):
        print("[TRIGGER] Merge confirmed. Run /auto-cascade now.")
```

See `hooks/` for ready-to-use templates:
- [`user_prompt_trigger.py`](hooks/user_prompt_trigger.py) — Detects phrases in user messages
- [`post_tool_trigger.py`](hooks/post_tool_trigger.py) — Detects events after tool execution (e.g., git commit)
- [`hook_health_check.py`](hooks/hook_health_check.py) — Verifies all hooks are healthy (the meta-layer)

### Layer 2: Memory (Cognitive Enforcement)

A persistent memory entry that gets loaded into every new session:

```markdown
# Memory: Auto-Cascade is mandatory after merges
After every merge confirmation, run /auto-cascade Phase 1-4.
This is not optional. The hook will remind you, but if it fails, this memory is the fallback.
```

In Claude Code, this goes in `~/.claude/projects/<project>/memory/`.

### Layer 3: Documentation (Persistent Enforcement)

A rule in the project instructions (CLAUDE.md) that the AI reads at session start:

```markdown
## Behavior Rules
- **Merge confirmation -> /auto-cascade MANDATORY**: On "merged", "PR through", etc.
  always run auto-cascade Phase 1-4. Hook merge_cascade_trigger.py reminds additionally.
```

## The Meta-Layer: Who Watches the Watchers?

Hooks can break silently. We discovered this when Claude Code v2.1.92 fixed a regression where PreToolUse hooks with JSON stdout and exit code 2 weren't correctly blocking tool calls — a bug that existed for weeks without anyone noticing.

If your enforcement layer can fail without alerting you, you don't have enforcement — you have a more comfortable illusion of safety.

The **Hook Health Monitor** solves this:

```bash
python hooks/hook_health_check.py
```

```
HOOK HEALTH CHECK — 21 hooks, 0 failures
============================================================
[+] PreToolUse     bash_guard.py
[+] PostToolUse    post_commit_skill_trigger.py
[~] TeammateIdle   teammate_idle.py
    runtime: EXIT 2 (expected for blocking hooks with test input)
============================================================
ALL 21 HOOKS HEALTHY
```

It reads your settings, finds every registered hook, and verifies:
1. **File exists** — not deleted or moved
2. **Syntax valid** — py_compile passes
3. **Runtime OK** — test input produces non-error output

Run it at session start, on a schedule, or after platform updates.

## The Reflexive Proof

The most compelling evidence for this principle: **we discovered it by applying our own product's methodology to our own build system.**

Our product's thesis: "Implicit decisions must be externalized into auditable artifacts."

The auto-cascade failure was exactly that — an implicit convention (the AI should remember to trigger a skill) that wasn't externalized into an enforceable mechanism. Our governance framework caught a governance gap in our own tooling.

This isn't dogfooding (using your own product). It's **reflexive governance** — the methodology proving itself through self-application.

## Quick Start

### For Claude Code Users

Install the plugin:
```bash
/plugin marketplace add larsbracker/Design-Concepts
/plugin install Design-Concepts
```

Run the audit:
```
/convention-enforcement
```

This scans your skills for event-based triggers without hook enforcement and reports which ones are vulnerable.

### For Any AI Agent System

1. **Audit your triggers**: List every automation that should fire "automatically" or "when X happens"
2. **Check enforcement**: For each trigger, ask: "What mechanism ensures this fires? Is it just documentation?"
3. **Add hooks**: Copy templates from `hooks/` and adapt the patterns
4. **Add the health monitor**: Run `hook_health_check.py` periodically
5. **Document the rule**: Add it to your agent's persistent instructions

## Further Reading

- [dual-critique](../dual-critique/) — Asymmetric review protocol (another Design Concept)
- [SR7D Framework](https://steerable.org) — The governance framework these concepts are extracted from

## License

MIT
