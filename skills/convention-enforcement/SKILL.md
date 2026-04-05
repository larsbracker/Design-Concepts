---
name: convention-enforcement
description: >
  Audit your skills for silent failure risk. Finds event-based triggers
  without hook enforcement, runs health checks on all registered hooks,
  and reports which skills are ENFORCED vs UNPROTECTED.
  Trigger: "/convention-enforcement", "audit my hooks", "which skills are unprotected",
  "hook health check", "silent failure audit"
effort: low
---

# /convention-enforcement — Silent Failure Audit

Scans your skill set for the Convention-Enforcement gap:
skills that define event-based triggers but have no hook backing them.

**Principle:** Convention without enforcement is a silent failure waiting to happen.

---

## Phase 1: Inventory

1. Read `.claude/settings.json` — extract all registered hooks
2. Scan `.claude/skills/*/SKILL.md` — extract all trigger patterns
3. Classify each skill trigger as:
   - **COMMAND-BASED** (user types `/skill-name`) — LOW risk
   - **EVENT-BASED** (should fire on merge/commit/session-start/etc.) — check enforcement

## Phase 2: Match

For each EVENT-BASED trigger, check if a hook exists that enforces it:
- UserPromptSubmit hooks — match against trigger words
- PostToolUse hooks — match against tool events
- Scheduled/Cron — match against time-based triggers

## Phase 3: Report

```
CONVENTION ENFORCEMENT AUDIT
===============================================
Skills scanned:    [N]
Event-based:       [N]
Hook-enforced:     [N]
Unprotected:       [N]

ENFORCED:
  [+] /auto-cascade     -> merge_cascade_trigger.py (UserPromptSubmit)
  [+] /atom-sync-review -> post_commit_trigger.py (PostToolUse)

UNPROTECTED:
  [!] /research-surface -> "session start" trigger, no hook
  [!] /harvest          -> "weekly" trigger, no cron

HOOK HEALTH:
  [run hook_health_check.py output here]
===============================================
```

## Phase 4: Recommendations

For each UNPROTECTED skill, suggest the appropriate hook type:
- User message triggers -> UserPromptSubmit hook
- Tool event triggers -> PostToolUse hook
- Time-based triggers -> Scheduled task / cron
- Skill-chain triggers -> Add MANDATORY gate in upstream SKILL.md

**Never auto-fix.** Report only. Human decides which gaps to close.
