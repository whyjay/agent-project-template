---
name: project-init
description: Initialize a new Codex/Claude project template through Agent edits only. Use when AGENTS.md says the project is not initialized, PROJECT_NAME remains, or the user asks to initialize/reinitialize the project.
---

# project-init skill

This skill is part of the shared project template.

- Canonical location for all agents: `skills/project-init/SKILL.md`
- Codex discovery copy: `.agents/skills/project-init/SKILL.md`
- Claude Code copy: `.claude/skills/project-init/SKILL.md`

No external language runtime is required. Perform initialization by editing the project files directly.

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
   - If this is the original template repo and the user is maintaining the template itself, do not initialize it.
   - If already initialized, do not reinitialize unless the user asked for it.
3. Use the current folder name as the project name unless the user provided a better name.
4. If not initialized, collect the two required inputs.
5. Ensure these folders exist: `00_refs/`, `01_analysis/`, `02_outputs/`, `skills/`, `.agents/skills/`, `.claude/skills/`, `system/`.
6. Update `AGENTS.md`.
   - Replace `PROJECT_NAME`.
   - Set `Initialized: YES`.
   - Set `Project name`.
   - Set `Last initialized` to today's date.
   - Fill project goal between `PROJECT_GOAL_START` and `PROJECT_GOAL_END`.
   - Record primary reference source.
   - Keep `Owner` blank unless the user provided one.
7. Create `01_analysis/00_project_brief.md` if missing.
   - Include project purpose, final output, intended reader/user, success criteria, reference location, current reference list, missing materials, and next work candidates.
   - If the file already exists, update only the fields affected by the initialization request and preserve user notes.
8. Run the `update-index` skill procedure to update `system/INDEX.md`.
9. Summarize what changed and what the next recommended action is.

## Do not

- Do not store per-file summaries inside `AGENTS.md`.
- Do not modify original files inside `00_refs/`.
- Do not proceed with detailed analysis before initialization is complete unless the user explicitly overrides.
