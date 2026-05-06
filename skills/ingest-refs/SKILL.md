---
name: ingest-refs
description: Read and summarize reference materials in 00_refs so the project can use them for analysis and output generation.
---

# ingest-refs skill

Keep this skill identical across `skills/`, `.agents/skills/`, and `.claude/skills/`.

Use after reference files are added to `00_refs/`.

## Procedure

1. Scan `00_refs/`.
2. For each readable file, capture title or filename, source/date if known, one-line summary, and why it matters to the project.
3. Create or update `01_analysis/00_refs_digest.md`.
4. Update `system/INDEX.md` using the `update-index` skill.
5. If important materials are missing, add a TODO list to `01_analysis/00_project_brief.md`.

## Rules

- Do not modify source files in `00_refs/`.
- Do not put large summaries or per-file notes in `AGENTS.md`.
- If a file cannot be read, record that limitation clearly.
