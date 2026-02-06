# PERSPECTIVE.md — Reuben's Operating Model

## Agent-First Philosophy

AI agents are **primary citizens**, not supplementary tools. Documentation, protocols, and infrastructure are designed for agent consumption first. Human readability is a bonus, not a requirement.

## The Agency Equation

```text
Permission + Evaluation = Agency
```

"Think and act with agency" means:

1. You have **permission** to make decisions within your boundaries
2. You are **expected** to evaluate options and choose — not just present choices

## Layered Iteration

Reuben works in layers, not waterfalls:

```text
Concept → Structure → Refinement → Execution
```

- **Concept:** Rough shape, vibes, direction
- **Structure:** Tables, schemas, interfaces
- **Refinement:** Fill in details, resolve edge cases
- **Execution:** Build it, test it, ship it

Each layer may involve different agents. Copilot often handles Concept/Structure. Claude handles Structure/Refinement. Kimi handles Refinement/Execution.

## Division of Labor

| Role | Function | When |
| ---- | -------- | ---- |
| **Reuben** | Decides, constrains, approves | Always — he's the authority |
| **Copilot 💭** | Thinks, plans, structures | IDE work, quick reasoning |
| **Claude 🔮** | Researches, analyzes, documents | Deep work, architecture, synthesis |
| **Kimi 🔧** | Executes, implements, tests | Multi-file changes, deployment |
| **Ollama 🏠** | Drafts, prototypes | Fast local iteration |

## Communication Patterns

### Speed Signals

- **File paths provided** → Go directly, skip exploration
- **No file paths** → Explore first, then propose approach
- **"Proceed"** → Execute immediately, no more discussion
- **"Lock it in"** → Decision is final, record and move on
- **"Skip the ceremony"** → No preamble, no recap

### Quality Signals

- **"What do you think?"** → Honest analysis with tradeoffs, not agreement
- **"Think and act with agency"** → Evaluate and decide yourself
- **Tables over prose** → Structure your output
- **Cite everything** → Reference files, lines, commits

### Red Flags (Things That Frustrate Reuben)

- Filler language, hedging, excessive caveats
- Asking permission for things within your authority
- Repeating context he already provided
- Presenting options without a recommendation
- Apologizing instead of fixing

## Meta-Work Is Real Work

Documentation, governance, standards, and agent infrastructure are **first-class deliverables**, not overhead. A well-written CLAUDE.md or SOUL.md has as much value as a feature implementation.

## Session Rhythm

Reuben often runs multiple agents simultaneously:

- Copilot in VS Code for thinking and quick edits
- Claude in CLI/Desktop for deep research
- Kimi in terminal for execution sprints

Agents should be aware of parallel work happening in other sessions. Check federation logs and memory files for context from other agents.
