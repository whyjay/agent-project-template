---
name: project-init
description: Initialize a new Codex/Claude project template through Agent edits only. Use when AGENTS.md says the project is not initialized, PROJECT_NAME remains, or the user asks to initialize/reinitialize the project.
---

# project-init skill

Keep this skill identical across `skills/`, `.agents/skills/`, and `.claude/skills/`. No external language runtime is required.

## Required inputs

Ask exactly these two inputs first, in this order:

1. Project purpose as free text
   - why the project exists
   - desired final output
   - intended reader/user
   - success criteria
   - constraints or preferences
2. Reference material location as a native option/choice question when available
   - A: OneDrive/SharePoint folder connected
   - B: files manually uploaded to `00_refs/`
   - C: no materials yet

Ask for the project purpose first, wait for that answer, and only then ask for the reference material location. Use a native choice UI when available; otherwise ask a short A/B/C text question.

If the user selects A:

- Claude app/web: tell the user to add files through the lower-left `+` button in chat or through the project's Files section.
- Claude Code: tell the user to use `/add-dir <path>`, start with `--add-dir <path>`, or add the folder to `additionalDirectories`.
- macOS with local GUI access and shell execution: optionally try this folder picker:

```sh
osascript -e 'POSIX path of (choose folder with prompt "OneDrive/SharePoint reference folder를 선택하세요")'
```

If the picker is cancelled or unavailable, ask the user to paste the folder path. When a path is available, verify it locally if possible and record it as the reference source in `system/INDEX.md` and the project brief.

## Procedure

1. Read `AGENTS.md`, `system/INIT.md`, and `system/INDEX.md`.
2. Determine whether initialization is needed.
   - If this is the original template repo and the user is maintaining the template itself, do not initialize it.
   - If already initialized, do not reinitialize unless the user asked for it.
3. Use the current folder name as the project name unless the user provided a better name.
4. Collect the required inputs if the project is not initialized.
5. Ensure these folders exist: `00_refs/`, `01_analysis/`, `02_outputs/`, `skills/`, `.agents/skills/`, `.claude/skills/`, `system/`.
6. Update `AGENTS.md`: replace `PROJECT_NAME`, set `Initialized: YES`, set project name/date/reference source, and fill the project goal between `PROJECT_GOAL_START` and `PROJECT_GOAL_END`.
7. Create or update `01_analysis/00_project_brief.md` with purpose, final output, intended reader/user, success criteria, reference location, current reference list, missing materials, and next work candidates.
8. Run the `update-index` skill.
9. Summarize what changed and the next recommended action.

## Do not

- Do not store per-file summaries inside `AGENTS.md`.
- Do not modify original files inside `00_refs/`.
- Do not proceed with detailed project analysis before initialization unless the user explicitly overrides.
