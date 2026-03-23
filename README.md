# dual-critique

Asymmetric dual-critique protocol for Claude Code.

Two independent review phases — **C1** finds gaps, **C2** finds regressions — separated by a strict information firewall. C2 never sees what C1 found. Where both phases independently flag the same issue, confidence is high. Where they diverge, you've found a blind spot.

Produces a hardened **V2** artifact with all patches applied.

## Why asymmetric?

Single-pass code review creates anchoring bias. Once a reviewer spots one issue, subsequent findings cluster around it. Dual-critique breaks this pattern:

| Phase | Perspective | Asks |
|-------|------------|------|
| **C1** | Constructive reviewer | "What's missing? What's underspecified?" |
| **C2** | Hostile implementer | "What breaks if I build exactly this?" |

The **firewall** between phases is the key mechanism. C2 operates with zero knowledge of C1's findings. Independent convergence on the same issue is the strongest signal you can get from a review process.

## Installation

```bash
/plugin marketplace add larsbracker/dual-critique
/plugin install dual-critique
```

## Usage

```
/dual-critique
```

Works on any artifact: implementation plans, architecture docs, specs, RFCs.

Pass the artifact inline, as a file reference, or let the skill read it from context.

## Governance Axes

Every finding is tagged with the governance axis it violates:

| Axis | Question |
|------|----------|
| System Resilience | Does it handle errors, timeouts, and degraded states? |
| Spec Fidelity | Does the implementation match the specification? |
| Change Safety | Are existing contracts and interfaces preserved? |
| Human Agency | Do humans retain decision authority at critical points? |
| Justified Overhead | Is added complexity proportional to benefit? |
| Audit Trail | Are decisions traceable and persisted? |
| Evidence Quality | Are claims backed by multiple sources? |

These axes are derived from the [SR7D governance framework](https://steerable.ai) — a set of seven core principles and three ethical constraints for AI-assisted decision systems.

## How it works

```
Artifact ──→ C1 (Gap Analysis) ──→ C1 Matrix
                                        │
                                    FIREWALL
                                        │
Artifact ──→ C2 (Regression Analysis) ──→ C2 Matrix
                                        │
                              ┌─────────┴─────────┐
                              │    Synthesis       │
                              │ Convergence Rate   │
                              │ Stability Check    │
                              └─────────┬─────────┘
                                        │
                              Stable? ──→ V2 (hardened artifact)
                              Unstable? → Escalate to human
```

## Safety

The protocol includes safety patches discovered by running dual-critique on itself:

- **Loop prevention**: Max 1 iteration. V2 never triggers another cycle.
- **False-positive protection**: Triggers on substantive review requests, not casual mentions.
- **Rollback escalation**: If unstable after V2, escalates to human decision.
- **Crash safety**: If the skill fails, the artifact remains valid.

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| Output directory | `docs/critiques/` | Where critique files are saved |
| Language | English | Output language (`en` or `de`) |

## Credits

Built by [Lars Bracker](https://github.com/larsbracker). The governance axes are derived from the SR7D framework developed for [Steerable](https://steerable.ai), a decision governance system for financial advisory.

## License

MIT
