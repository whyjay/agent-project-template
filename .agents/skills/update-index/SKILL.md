---
name: update-index
description: Update system/INDEX.md after files are added, moved, renamed, or deleted. Use whenever project files change.
---

# update-index skill

Keep this skill identical across `skills/`, `.agents/skills/`, and `.claude/skills/`. Update `system/INDEX.md` by inspecting the project tree and editing the index directly.

## Procedure

1. Scan root markdown files, `system/`, `00_refs/`, `01_analysis/`, `02_outputs/`, and `skills/`.
2. Check `.agents/skills/` and `.claude/skills/` only for skill copy consistency.
3. Identify files missing from `system/INDEX.md` and files listed there but no longer present.
4. Add or update rows with relative path, type, source or date, one-line summary, and key output/usage.
5. Add a concise row to the change history.

## Rules

- Keep original materials in `00_refs/`.
- Keep analysis notes in `01_analysis/`.
- Keep externally shareable outputs in `02_outputs/`.
- Treat `skills/` as the shared skill source of truth.
- Do not index `.agents/skills/` or `.claude/skills/` separately unless a mismatch must be called out.
- Do not duplicate detailed file summaries in `AGENTS.md`.
