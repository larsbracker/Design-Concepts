# Design Concepts

Battle-tested governance patterns for AI agent systems.

Each concept is a self-contained principle — independently usable, extracted from production systems, validated through real failures. Pick what fits your workflow.

## Concepts

| Concept | Problem | Format |
|---------|---------|--------|
| [dual-critique](concepts/dual-critique/) | Single-pass review has anchoring bias | Claude Code Skill |
| [convention-enforcement](concepts/convention-enforcement/) | Conventions without enforcement fail silently | Skill + Hooks + Health Monitor |

## Install as Claude Code Plugin

All skills are installable as a single plugin:

```bash
/plugin marketplace add larsbracker/Design-Concepts
/plugin install Design-Concepts
```

This gives you access to all skills: `/dual-critique`, `/convention-enforcement`, etc.

## Use Without Claude Code

Every concept includes:
- A **README** explaining the principle, the failure that motivated it, and how to apply it
- **Copy-paste hooks** (Python scripts) that work in any automation pipeline
- **Framework-agnostic guidance** — the patterns apply beyond Claude Code

Browse the `concepts/` directory and grab what you need.

## Contributing

Want to add a concept? See the [template](concepts/_template/README.md) for the structure. Each concept should include:
- A real failure case (not a theoretical risk)
- A clear principle (one sentence)
- A working implementation (code, not just advice)

## Origin

These concepts are extracted from [Steerable](https://steerable.org), a decision governance system for financial advisory built on the SR7D framework. The governance patterns are domain-agnostic — they apply wherever AI agents make or support decisions.

## License

MIT
