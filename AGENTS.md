# AGENTS.md

This repository uses root `CLAUDE.md` as the primary development workflow and governance guide.

Codex and other AI coding assistants must read and follow root `CLAUDE.md` before making code or documentation changes.

Do not duplicate repository-specific names in this file. Use the `Repository parameters` section in root `CLAUDE.md` as the single source of truth for folder names, package names, import names, validation commands, and reference paths.

---

## Required read order

Before making any change, read and follow:

1. Root `CLAUDE.md`
2. This root `AGENTS.md`
3. Any nested `AGENTS.md`, `AGENTS.override.md`, or `CLAUDE.md` files in the target subdirectory
4. The relevant local `README.md`, `Makefile`, and package metadata

When `CLAUDE.md` refers to Claude or Claude Code, apply the same instruction to Codex unless technically impossible.

---

## Conflict resolution order

1. Explicit user instruction
2. Closest nested `AGENTS.override.md`, `AGENTS.md`, or `CLAUDE.md`
3. Root `CLAUDE.md`
4. Root `AGENTS.md`
5. Local README, Makefile, or package metadata guidance

If there is a conflict that cannot be resolved safely, stop and ask for clarification before changing files.

---

## Mandatory defaults

- Keep changes minimal and didactic.
- Do not modify unrelated samples.
- Do not introduce architecture that belongs in Fred core.
- Do not copy internal Fred code unless explicitly requested.
- Prefer current public `fred-sdk` and `fred-runtime` APIs.
- Keep default validation offline.
- Use the repository parameters in root `CLAUDE.md`; do not assume fixed folder or package names.
- Inspect the actual filesystem before changing imports, paths, registry entries, or configuration.
- Update documentation when commands, package names, import paths, agent IDs, MCP dependencies, ports, configuration, or runtime behavior change.

---

## Validation

For changes under the configured agent package directory, run the commands defined in root `CLAUDE.md` from that directory:

```bash
cd <AGENT_PACKAGE_DIR>
<QUALITY_COMMAND>
<TEST_COMMAND>
```

Do not claim validation succeeded unless the commands were actually run successfully.
