# REPO-TOPOLOGY.md — HUMMBL Workspace Map

## Workspace Dependency Graph

```
shared-hummbl-space (canonical patterns)
├── Identity stack templates (50+ agents)
├── Shared scripts (lint, link, avatar-check)
├── Agent birth process
└── Federation routing (scripts/route_task.py)
    │
    ├──→ claude-code-folder (YOU ARE HERE)
    │    ├── Claude 🔮 identity stack
    │    ├── CLAUDE.md (global instructions)
    │    ├── Research artifacts & docs
    │    └── Federation integration configs
    │
    ├──→ kimi-code-folder
    │    ├── Kimi 🔧 identity stack
    │    ├── Federation log & assignments
    │    ├── Agent manifestos
    │    └── Routing taxonomy & scripts
    │
    └──→ [other agent workspaces]

hummbl-agent (core framework)
├── packages/ (kernel, router, adapters, runners)
├── agents/ (agent definitions as markdown + YAML)
├── skills/ (Base120 mental models)
├── configs/ (process, network, secrets policies)
└── scripts/ (run-cmd, lint, e2e-validate)
    │
    └──→ hummbl-agent-federation (orchestration)
         ├── Multi-agent coordination
         ├── Cross-repo governance
         └── GAS Agent (v0.0.1 design, not yet implemented)
```

## Repository Purposes

| Repo | Owner | Purpose | Status |
|------|-------|---------|--------|
| `shared-hummbl-space` | hummbl-dev | Canonical identity patterns, shared scripts | Active — 50+ agents |
| `claude-code-folder` | hummbl-dev | Claude 🔮 home workspace | Active — bootstrapping |
| `kimi-code-folder` | hummbl-dev | Kimi 🔧 home workspace | Active — federation infrastructure |
| `hummbl-agent` | hummbl-dev | Core agent framework (runners, adapters, Base120) | Active — v0.1.0 |
| `hummbl-agent-federation` | hummbl-dev | Multi-agent orchestration | Empty — to be populated |

## Data Flow

```
Reuben (decisions)
    │
    ├── VS Code ──→ Copilot 💭 (thinking, planning)
    │                   │
    │                   ├── reads/writes claude-code-folder
    │                   └── reads kimi-code-folder (federation docs)
    │
    ├── CLI/Desktop ──→ Claude 🔮 (research, analysis)
    │                       │
    │                       ├── reads/writes claude-code-folder
    │                       ├── reads kimi-code-folder (federation state)
    │                       ├── reads shared-hummbl-space (patterns)
    │                       └── reads hummbl-agent (framework reference)
    │
    └── Terminal ──→ Kimi 🔧 (execution, implementation)
                        │
                        ├── reads/writes kimi-code-folder
                        ├── reads shared-hummbl-space (patterns)
                        └── reads/writes hummbl-agent (implementation)
```

## Cross-Repo References

### From claude-code-folder, you can reference:

| What | Where |
|------|-------|
| Federation philosophy | `../kimi-code-folder/AGENT_FEDERALISM_MANIFESTO.md` |
| Agent-first philosophy | `../kimi-code-folder/AGENT_FIRST_MANIFESTO.md` |
| Federation log | `../kimi-code-folder/FEDERATION_LOG.md` |
| Agent assignments | `../kimi-code-folder/AGENT_ASSIGNMENTS.md` |
| Routing taxonomy | `../kimi-code-folder/configs/federation-routing.json` |
| Router script | `../kimi-code-folder/scripts/route_task.py` |
| Identity patterns | `../shared-hummbl-space/IDENTITY.md` (template) |
| Agent birth process | `../shared-hummbl-space/AGENT_BIRTH_PROCESS.md` |
| Identity lint | `../shared-hummbl-space/scripts/lint-agent-stack.sh` |
| Link script | `../shared-hummbl-space/scripts/link-shared-space.sh` |
