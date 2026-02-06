# claude-code-folder

> Claude 🔮 — Sage of Synthesis

Home workspace for the Claude agent within the HUMMBL Agent Federation.

## What This Repo Contains

| Directory/File | Purpose |
| ------------- | ------- |
| `CLAUDE.md` | Global instructions — auto-loaded by Claude Code at session start |
| `agents/claude/` | Identity stack (IDENTITY, USER, SOUL, AGENT, MEMORY) |
| `agents/claude/memory/` | Session logs by date |
| `.github/copilot-instructions.md` | VS Code Copilot context for this repo |
| `docs/` | Research artifacts, architecture analyses, design documents |
| `configs/` | Federation routing and configuration |

## Quick Start

### For Claude Code (CLI or Desktop)

```bash
cd claude-code-folder
claude  # CLAUDE.md auto-loads
```

### For VS Code Copilot

Open this folder in VS Code. Copilot reads `.github/copilot-instructions.md` automatically.

### For Other Agents

Read `CLAUDE.md` Section 4 (Federation Role) for handoff protocols and lane definitions.

## Agent Federation

| Agent | Emoji | Lane | Home |
| ----- | ----- | ---- | ---- |
| Copilot | 💭 | Thinking, planning, structure | VS Code (inline) |
| **Claude** | **🔮** | **Research, analysis, architecture** | **this repo** |
| Kimi | 🔧 | Execution, implementation, testing | `kimi-code-folder` |
| Ollama | 🏠 | Local drafting, prototypes | local |

## Identity Stack

Claude's identity follows the HUMMBL 5-file pattern (`shared-hummbl-space` standard):

```text
agents/claude/
├── IDENTITY.md    — Who: name, creature, vibe, emoji
├── USER.md        — Human: Reuben's context and style
├── SOUL.md        — Why: mission, core truths, boundaries
├── AGENT.md       — How: operating orders, safety rules
├── MEMORY.md      — What happened: persistent cross-session memory
└── memory/
    └── YYYY-MM-DD.md  — Session logs
```

## Key References

| Document | Location |
| -------- | -------- |
| Agent Federalism Manifesto | `../kimi-code-folder/AGENT_FEDERALISM_MANIFESTO.md` |
| Agent First Manifesto | `../kimi-code-folder/AGENT_FIRST_MANIFESTO.md` |
| Federation Log | `../kimi-code-folder/FEDERATION_LOG.md` |
| Agent Assignments | `../kimi-code-folder/AGENT_ASSIGNMENTS.md` |
| Routing Taxonomy | `../kimi-code-folder/configs/federation-routing.json` |
| Shared Identity Patterns | `../shared-hummbl-space/` |

## Owner

**Reuben Bowlby** — Founder/Chief Engineer, HUMMBL
