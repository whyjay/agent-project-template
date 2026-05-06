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

Ask for exactly these two inputs first, in this order:

1. Project purpose as free text
   - Why this project exists
   - Desired final output
   - Intended reader/user
   - Success criteria
2. Reference material location as a native option/choice question when available
   - A: OneDrive/SharePoint folder connected
   - B: Files manually uploaded to `00_refs/`
   - C: No materials yet

For Codex, use a native choice tool such as `request_user_input` when it is available. For Claude/Codex environments with another built-in choice UI, use that. Only fall back to a short A/B/C text question when no native choice UI is available.

If the user selects A, optionally try to open a folder picker only when running on macOS with local GUI access and shell execution:

```sh
osascript -e 'POSIX path of (choose folder with prompt "OneDrive/SharePoint reference folder를 선택하세요")'
```

If the user cancels, or if GUI access, permissions, or the runtime environment prevent the picker from opening, ask the user to paste the OneDrive/SharePoint folder path instead. When a path is available, verify that it exists locally if the environment allows it, then record it as the reference source in `system/INDEX.md` and the project brief. The folder picker is optional convenience only; path input must remain the universal fallback.

## Procedure

1. Read `AGENTS.md`, `system/INIT.md`, and `system/INDEX.md`.
2. Determine whether the project is already initialized.
   - If this is the original template repo and the user is maintaining the template itself, do not initialize it.
   - If already initialized, do not reinitialize unless the user asked for it.
3. Use the current folder name as the project name unless the user provided a better name.
4. If not initialized, collect the two required inputs using the free-text and choice flow above.
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
