# MEMORY.md — Claude Persistent Memory

## Major Events

| Date | Event | Impact |
|------|-------|--------|
| 2026-02-05 | Agent birth — identity stack created | Claude 🔮 operational in claude-code-folder |
| 2026-02-05 | CLAUDE.md (global) created | All Claude Code sessions now have auto-loaded instructions |
| 2026-02-05 | Federation Phase 3 contributions | Architecture analysis, routing taxonomy, router implementation |

## Patterns Learned

- Reuben works with multiple agents simultaneously (Copilot in VS Code, Kimi in terminal, Claude in CLI/desktop)
- "Lock it in" = decision is final, record and move on
- File locations matter — always verify artifacts are in the correct repo, not scattered across workspaces
- Kimi's drafts are good starting points but may lack full `shared-hummbl-space` pattern compliance
- The federation log and agent assignments live in `kimi-code-folder` (current canonical location)

## Capabilities & Tools

- Claude Code CLI: file read/write, terminal commands, git operations, web search
- Claude Desktop: conversation, analysis, document review
- VS Code Copilot Chat: inline assistance when representing Claude (rate-limit fallback)

## Architecture Decisions

| Decision | Rationale | Date |
|----------|-----------|------|
| Keep both CLAUDE.md and agents/claude/AGENT.md | CLAUDE.md auto-loads for Claude Code; AGENT.md maintains identity stack pattern consistency with 50+ agents | 2026-02-05 |
| Rewrite Kimi's draft identity stack | Kimi's drafts were created without full shared-hummbl-space patterns; rewrite ensures lint compliance | 2026-02-05 |
| GAS Agent forward-reference in CLAUDE.md | Placeholder only — no hard dependencies on unimplemented system | 2026-02-05 |
| GV domain (not GO) for governance | Avoids confusion with Go programming language | 2026-02-05 |

## Open Items

- [ ] Federation routing.json needs to be copied/adapted into claude-code-folder
- [ ] .github/copilot-instructions.md not yet created
- [ ] README.md, PERSPECTIVE.md, REPO-TOPOLOGY.md not yet created
- [ ] Avatar not yet created (pending Reuben approval)
- [ ] HUMMBL G.A.S. Agent Phase 1 foundation not yet implemented
