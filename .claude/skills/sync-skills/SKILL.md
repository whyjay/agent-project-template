---
name: sync-skills
description: Keep shared project skills synchronized across skills/, .agents/skills/, and .claude/skills/. Use whenever adding, editing, renaming, or deleting a skill.
---

# sync-skills skill

Keep every skill identical across `skills/`, `.agents/skills/`, and `.claude/skills/`.

## Procedure

1. List skill folders in all three locations.
2. For every skill name, ensure all three locations exist or all three are intentionally removed.
3. When adding or editing a skill, apply the same `SKILL.md` content to all three locations in the same change.
4. When deleting a skill, remove the matching folder from all three locations.
5. Update `AGENTS.md`, `CLAUDE.md`, `system/INIT.md`, and `system/INDEX.md` if default skill names or operating rules changed.
6. Verify matching skill names and matching `SKILL.md` hashes.

## Rules

- Keep skill bodies concise and procedural.
- Do not treat `.agents/skills/` or `.claude/skills/` as disposable generated output.
- Do not store project-specific file summaries inside skill files.
