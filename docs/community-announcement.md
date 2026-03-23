# Community Announcement — dual-critique

> Varianten fuer verschiedene Plattformen. Lars waehlt + passt an.

---

## Variante 1: Claude Code Discord / GitHub Discussions (ausfuehrlich)

**Title:** Releasing dual-critique — an asymmetric review protocol for Claude Code

I've been building a decision governance system (SR7D framework) and kept running into the same problem: single-pass code review anchors on the first finding. Once you spot one issue, everything else clusters around it.

So I built a different approach: **dual-critique** runs two independent review phases with a strict information firewall between them.

- **C1 (Gap Analysis):** "What's missing? What's underspecified?"
- **C2 (Regression Analysis):** "What breaks if I implement this literally?"

C2 never sees what C1 found. Where both phases independently flag the same issue, confidence is high. Where they diverge, you've found a blind spot no single reviewer would catch.

The protocol self-hardens: I ran dual-critique on itself and discovered 4 safety patches (loop prevention, false-positive protection, rollback escalation, crash safety) that are now baked in.

**Install:**
```
/plugin marketplace add larsbracker/dual-critique
/plugin install dual-critique
```

Then use `/dual-critique` on any plan, spec, or architecture doc.

Each finding gets tagged with one of 7 governance axes (System Resilience, Spec Fidelity, Change Safety, Human Agency, Justified Overhead, Audit Trail, Evidence Quality) — so you don't just know *what's* wrong, you know *which dimension* of quality is affected.

Repo: https://github.com/larsbracker/dual-critique

Feedback welcome. This is extracted from a larger governance framework I'm building for financial advisory software, but the review protocol is domain-agnostic.

---

## Variante 2: Twitter/X (kurz, hook-orientiert)

Single-pass code review has anchoring bias. Once you find one issue, everything clusters around it.

I built dual-critique for Claude Code — two independent review phases with a firewall between them. C1 finds gaps, C2 finds regressions. Neither sees the other's findings.

Where both converge independently: high confidence.
Where they diverge: blind spots you'd never catch otherwise.

`/plugin marketplace add larsbracker/dual-critique`

Open source, MIT licensed.
github.com/larsbracker/dual-critique

---

## Variante 3: LinkedIn (professional, positioning)

**When I review my own architecture decisions, I anchor on the first issue I find.** Every subsequent finding clusters around it. This is well-documented cognitive bias — and it applies equally to AI-assisted code review.

I built an open-source Claude Code plugin that eliminates this: **dual-critique** runs two independent review phases separated by a strict information firewall.

Phase 1 (C1) asks: "What's missing?"
Phase 2 (C2) asks: "What breaks if I build exactly this?"

C2 has zero knowledge of C1's findings. Independent convergence on the same issue is the strongest signal a review process can produce.

The protocol includes 7 governance axes derived from the SR7D framework I developed for Steerable, a decision governance system for financial advisory. But the review mechanism is domain-agnostic — it works on any plan, spec, or architecture document.

Self-hardened: I ran the protocol on itself and discovered 4 safety patches that are now built in (loop prevention, false-positive protection, rollback escalation, crash safety).

Install in Claude Code:
/plugin marketplace add larsbracker/dual-critique

Open source (MIT): https://github.com/larsbracker/dual-critique

I'm curious how others approach the anchoring problem in AI-assisted review. What patterns have you found?

---

## Variante 4: Hacker News (Show HN, technisch)

**Show HN: dual-critique — Asymmetric code review with information firewall for Claude Code**

Problem: Single-pass review creates anchoring bias. First finding dominates subsequent analysis.

Solution: Two independent review phases (C1: gap analysis, C2: regression analysis from hostile-implementer perspective) separated by a strict information firewall. C2 never sees C1's output.

Key mechanism: Where C1 and C2 independently converge on the same issue, confidence is high. Where they diverge, you've found blind spots invisible to any single-pass approach.

Self-hardening: Running the protocol on itself discovered 4 safety patches (loop prevention, false-positive protection, rollback escalation, crash safety).

7 governance axes tag each finding by quality dimension: System Resilience, Spec Fidelity, Change Safety, Human Agency, Justified Overhead, Audit Trail, Evidence Quality.

Claude Code plugin, MIT licensed. Install: `/plugin marketplace add larsbracker/dual-critique`

https://github.com/larsbracker/dual-critique

Extracted from a larger governance framework (SR7D) I'm building for financial advisory decision systems, but the review protocol is domain-agnostic.
