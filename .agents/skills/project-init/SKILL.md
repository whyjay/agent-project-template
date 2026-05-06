---
name: project-init
description: Initialize a new Codex/Claude project template. Use this when AGENTS.md says the project is not initialized, PROJECT_NAME remains, or the user asks to initialize/reinitialize the project.
---

# project-init skill

This skill is part of the shared project template.

- Canonical location for all agents: `skills/project-init/SKILL.md`
- Codex discovery copy: `.agents/skills/project-init/SKILL.md`
- Claude Code copy: `.claude/skills/project-init/SKILL.md`

After editing the canonical skill, run `python3 scripts/sync_skills.py` to synchronize Agent-specific copies.

## Required inputs from the user

Ask for exactly these two inputs first:

1. Project purpose
   - Why this project exists
   - Desired final output
   - Intended reader/user
   - Success criteria
2. Reference material location
   - OneDrive/SharePoint folder connected
   - Files manually uploaded to `00_refs/`
   - No materials yet

## Procedure

1. Read `AGENTS.md`, `system/INIT.md`, and `system/INDEX.md`.
2. Determine whether the project is already initialized.
3. If not initialized, collect the two required inputs.
4. Update `AGENTS.md`.
   - Replace `PROJECT_NAME`.
   - Set `Initialized: YES`.
   - Fill project goal between `PROJECT_GOAL_START` and `PROJECT_GOAL_END`.
   - Record primary reference source.
5. Create `01_analysis/00_project_brief.md`.
6. Scan `00_refs/`, `01_analysis/`, `02_outputs/`, `skills/`, and `scripts/`.
7. Update `system/INDEX.md`.
8. Summarize what changed and what the next recommended action is.

## Do not

- Do not store per-file summaries inside `AGENTS.md`.
- Do not modify original files inside `00_refs/`.
- Do not proceed with detailed analysis before initialization is complete unless the user explicitly overrides.
