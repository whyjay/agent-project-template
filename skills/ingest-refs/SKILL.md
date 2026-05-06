---
name: ingest-refs
description: Read and summarize reference materials in 00_refs so the project can use them for analysis and output generation.
---

# ingest-refs skill

This skill is part of the shared project template.

- Canonical location for all agents: `skills/ingest-refs/SKILL.md`
- Codex discovery copy: `.agents/skills/ingest-refs/SKILL.md`
- Claude Code copy: `.claude/skills/ingest-refs/SKILL.md`

Use this skill after reference files are added to `00_refs/`.

## Procedure

1. Scan `00_refs/`.
2. For each readable file, capture:
   - title or filename
   - source if known
   - date if known
   - one-line summary
   - why it matters to this project
3. Create or update `01_analysis/00_refs_digest.md`.
4. Update `system/INDEX.md`.
5. If important materials are missing, create a TODO list in `01_analysis/00_project_brief.md`.

## Rules

- Do not modify source files in `00_refs/`.
- Do not over-summarize large files directly in `AGENTS.md`.
- If a file cannot be read, record that limitation clearly.
