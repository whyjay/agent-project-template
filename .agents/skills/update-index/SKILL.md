---
name: update-index
description: Update system/INDEX.md after files are added, moved, renamed, or deleted. Use whenever project files change.
---

# update-index skill

This skill is part of the shared project template.

- Canonical location for all agents: `skills/update-index/SKILL.md`
- Codex discovery copy: `.agents/skills/update-index/SKILL.md`
- Claude Code copy: `.claude/skills/update-index/SKILL.md`

No external language runtime is required. Update the index by inspecting the project tree and editing `system/INDEX.md` directly.

## Procedure

1. Scan these locations:
   - root markdown files (`AGENTS.md`, `CLAUDE.md`, `README_FOR_TEAM.md`)
   - `system/` (Agent operations docs: `INIT.md`, `INDEX.md`)
   - `00_refs/`
   - `01_analysis/`
   - `02_outputs/`
   - `skills/`
   - `.agents/skills/` and `.claude/skills/` only to confirm skill copy consistency
2. Identify files missing from `system/INDEX.md`.
3. Identify files listed in `system/INDEX.md` but no longer present.
4. Add or update rows with:
   - relative path (links from `system/INDEX.md` use `../` to point to root files)
   - file type
   - source or creation date
   - one-line summary
   - key output / usage
5. Add a row to the change history.

## Rules

- Keep original materials in `00_refs/`.
- Keep analysis notes in `01_analysis/`.
- Keep externally shareable outputs in `02_outputs/`.
- Treat `skills/` as the shared skill source of truth.
- Treat `.agents/skills/` and `.claude/skills/` as discovery copies; do not index them separately unless a mismatch needs to be called out.
- Do not duplicate detailed file summaries in `AGENTS.md`.
- `system/` only holds Agent operations docs (`INIT.md`, `INDEX.md`); do not move project deliverables there.
