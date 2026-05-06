---
name: sync-skills
description: Keep shared project skills synchronized across skills/, .agents/skills/, and .claude/skills/. Use whenever adding, editing, renaming, or deleting a skill.
---

# sync-skills skill

This skill keeps the three skill locations consistent without relying on any helper program.

- Canonical location for all agents: `skills/<skill-name>/SKILL.md`
- Codex discovery copy: `.agents/skills/<skill-name>/SKILL.md`
- Claude Code copy: `.claude/skills/<skill-name>/SKILL.md`

## Procedure

1. List skill folders in `skills/`, `.agents/skills/`, and `.claude/skills/`.
2. For every skill name, ensure all three locations exist or all three are intentionally removed.
3. When adding a skill, create the same `SKILL.md` content in all three locations in the same change.
4. When editing a skill, apply the same content change to all three `SKILL.md` files.
5. When deleting a skill, remove the matching folder from all three locations.
6. Update `AGENTS.md`, `CLAUDE.md`, `system/INIT.md`, and `system/INDEX.md` if the default skill list or operating rules changed.
7. Verify the three locations have the same skill names and matching `SKILL.md` content.

## Rules

- Keep skill bodies concise and procedural.
- Do not treat `.agents/skills/` or `.claude/skills/` as disposable generated output.
- Do not leave a skill updated in only one or two locations.
- Do not store project-specific file summaries inside skill files.
