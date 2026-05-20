# AGENTS.md

This file is intended to live inside the configured `AGENT_PACKAGE_DIR`.

Root `CLAUDE.md` remains the primary development workflow and governance guide. The repository-specific folder names, package names, import names, and validation commands are defined once in the `Repository parameters` section of root `CLAUDE.md`.

Do not hardcode or assume the repository name, agent package directory name, or Python import package name in this file.

---

## Required read order

Before changing files in this directory, read:

1. `../CLAUDE.md`
2. `../AGENTS.md`
3. This file
4. Local `README.md`, if present
5. Local `Makefile`, if present
6. Local package metadata such as `pyproject.toml`, if present

If this file is moved deeper than one level below the repository root, update the relative references above.

---

## Local rules

- Keep sample agents didactic and easy to copy.
- Prefer existing patterns in the local Python package.
- Use the configured `PYTHON_PACKAGE_DIR` and `PYTHON_IMPORT_NAME` from root `CLAUDE.md`.
- Register new agents in the local registry if the package has one.
- Do not modify unrelated agents.
- Do not add production dependencies unless necessary.
- Keep runtime integration aligned with the public `fred-sdk` and `fred-runtime` APIs.
- Inspect the actual filesystem before changing imports, paths, configuration, or registry entries.

---

## Validation

Run the configured quality and test commands from this directory:

```bash
<QUALITY_COMMAND>
<TEST_COMMAND>
```

If the local Makefile or package metadata defines different commands, follow the local commands and update root `CLAUDE.md` if the repository parameters are outdated.

Do not claim validation succeeded unless the commands were actually run successfully.
