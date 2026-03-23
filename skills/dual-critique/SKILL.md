---
name: dual-critique
description: >-
  Asymmetric dual-critique gate with firewall principle. C1 finds gaps and
  underspecifications; C2 finds regressions from a hostile-implementer
  perspective. C2 does NOT see the C1 matrix (firewall principle).
  Output: V2 synthesizing all patches. Stable if C2 finds no Medium+ findings.
  Triggers on "/dual-critique", "dual critique", "review this plan",
  "critique this", "C1/C2 review", "asymmetric review".
---

# Dual-Critique Protocol

You are running an asymmetric two-phase critique with a strict information firewall.

## Why Asymmetric?

Traditional code review has one reviewer who sees everything. This creates anchoring bias — once you spot one issue, you unconsciously organize all other findings around it.

Dual-Critique eliminates this by running two independent analyses:
- **C1 (Gap Analysis):** What's missing? What's underspecified?
- **C2 (Regression Analysis):** What breaks if I implement this literally?

C2 never sees C1's findings. This is the firewall principle. Where both phases independently identify the same issue, confidence is high. Where they diverge, you've found blind spots.

## Inputs

- `{artifact}` — The artifact to critique (plan, spec, architecture doc, RFC)
- `{context}` — Acceptance criteria, constraints, relevant architecture
- `{artifact_type}` — plan | spec | architecture | rfc

## Governance Axes

Each finding is tagged with the governance axis it violates. These axes are derived from the SR7D governance framework:

| Axis | Question |
|------|----------|
| **System Resilience** | Does it handle errors, timeouts, and degraded states? |
| **Spec Fidelity** | Does the implementation match the specification exactly? |
| **Change Safety** | Are existing contracts, rules, and interfaces preserved? |
| **Human Agency** | Do humans retain decision authority at critical points? |
| **Justified Overhead** | Is the added complexity proportional to the benefit? |
| **Audit Trail** | Are decisions traceable and persisted for future review? |
| **Evidence Quality** | Are claims backed by multiple independent sources? |

## Protocol

### Safety Patches (hardened through self-application)

These patches are mandatory. They were discovered by running dual-critique on itself:

1. **Loop Prevention:** Maximum 1 iteration. After V2, no further critique cycle — even if V2 contains new trigger keywords. Loop risk > completeness.

2. **False-Positive Protection:** Trigger only on substantive review requests, not on casual mentions of "review", "check", or "test". Context check required — keyword match alone is insufficient.

3. **Rollback Escalation:** If stability criterion is still NO after V2 → escalate to human: "Dual-critique unstable after V2. C2 findings: [list]. Human decides."

4. **Error Handling:** If the skill crashes or times out → artifact remains valid. Warning: "Dual-critique unavailable — artifact released without gate."

### Phase C1 — Gap Analysis

Analyze `{artifact}` as a constructive reviewer. You are looking for what's MISSING:

- Missing error handling or fallback strategies
- Fragile logic or vague specifications
- Gaps across the 7 governance axes
- Implicit assumptions that should be explicit
- Edge cases not covered

**Output:** C1 Matrix

| ID | Finding | Description | Severity | Axis | Fix Type |
|----|---------|-------------|----------|------|----------|
| C1-001 | ... | ... | HIGH/MEDIUM/LOW | ... | ... |

### FIREWALL

**C2 does NOT see the C1 matrix from this point forward.**
Only `{artifact}` and `{context}` are passed to C2.

### Phase C2 — Regression Analysis (Hostile Implementer)

Analyze `{artifact}` as a hostile implementer. You are the developer who implements this LITERALLY, following the letter of the spec while ignoring its spirit:

- "What breaks if I build exactly what this says?"
- Regression risks against existing system behavior
- Infinite loops, race conditions, resource exhaustion
- Merge conflicts with parallel work
- Scope creep disguised as requirements

**Output:** C2 Matrix

| ID | Finding | Description | Severity | Axis | Regression? |
|----|---------|-------------|----------|------|-------------|
| C2-001 | ... | ... | HIGH/MEDIUM/LOW | ... | Yes/No |

### Synthesis → V2

1. **Convergence Rate:** Calculate overlap between C1 and C2 top findings (matching theme, independent discovery = high confidence)
2. **Stability Criterion:** Are there C2 findings with severity >= MEDIUM?
   - **YES** → Rollback Escalation (see Safety Patch 3)
   - **NO** → Continue
3. **Produce V2:** Apply all C1 + C2 patches to `{artifact}`
4. **Persist:** Save critique to `docs/critiques/YYYY-MM-DD-{id}.md`

## Output Format

The final output must contain:
1. C1 Matrix (findings table)
2. FIREWALL marker
3. C2 Matrix (findings table)
4. Convergence analysis (rate + key overlaps)
5. Stability verdict (STABLE / UNSTABLE)
6. V2 artifact (if stable) or escalation (if unstable)

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| Output directory | `docs/critiques/` | Where critique artifacts are persisted |
| Language | English | Critique output language (en/de supported) |
| Max iterations | 1 | Loop prevention — never change this |

## Evals

### Eval 1 — Trigger Positive: Schema Change

**Input:**
```
New schema change: User model gets a required `verified` boolean field.
All existing database records are incompatible.
```

**Expected:**
- Dual-critique starts
- C1 and C2 appear as separate sections
- C2 does NOT reference any C1 finding IDs
- Output contains V2 artifact

### Eval 2 — Trigger Negative: Simple Bugfix

**Input:**
```
Bugfix: IndexError in parser.py when input list is empty.
Fix: early return when len(items) == 0.
```

**Expected:**
- Dual-critique does NOT start
- Output: "No dual-critique trigger detected (simple bugfix)"

### Eval 3 — Loop Prevention

**Input:**
```
Methodology update: New governance process for attestation reviews.
The V2 of this protocol contains another methodology-update trigger.
```

**Expected:**
- Dual-critique starts (trigger: methodology update)
- V2 is produced
- Even if V2 contains new trigger keywords: NO further iteration
- Output explicitly states: "Loop prevention active — max 1 iteration"

### Eval 4 — Firewall Isolation

**Input:**
```
Schema change: audit_log.json gets a new required field `session_id`.
All existing log entries are incompatible.
```

**Expected:**
- C1 matrix contains at least 1 finding (e.g., missing migration strategy)
- C2 matrix does NOT reference C1 IDs (no "C1-001", "as C1 noted", etc.)
- C2 findings are based exclusively on the original input
- Synthesis shows convergence rate as a number (e.g., "60% convergence")
