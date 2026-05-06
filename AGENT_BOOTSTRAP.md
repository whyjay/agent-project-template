# Agent Bootstrap

이 문서는 사용자가 빈 Claude/Codex 프로젝트에서 아래처럼 요청했을 때 따르는 설치 절차다.

```text
이 템플릿으로 초기화해줘: https://github.com/whyjay/agent-project-template
```

## 목표

현재 작업 폴더를 이 템플릿 구조로 채우고, 프로젝트 목적과 참고자료 위치만 받아 실제 프로젝트로 초기화한다.

## 안전 규칙

- 현재 폴더에 `AGENTS.md`, `CLAUDE.md`, `system/`, `skills/`, `.agents/skills/`, `.claude/skills/` 중 하나라도 이미 있으면 덮어쓰기 전에 중단하고 사용자 확인을 받는다.
- `README.md`만 있는 빈 GitHub repo라면, 내용이 비어 있거나 템플릿 교체에 사용자가 동의한 경우에만 덮어쓴다.
- `.git/`, `.claude/settings.local.json`, `CLAUDE.local.md`, `.env` 파일은 템플릿에서 복사하지 않는다.
- 이 원본 템플릿 repo 안에서 작업 중이면 초기화를 실행하지 않는다. 템플릿 유지보수 작업으로 취급한다.

## 절차

1. 사용자가 준 GitHub repo URL을 확인한다.
2. 임시 폴더에 템플릿을 clone한다.

```sh
tmp_dir="$(mktemp -d)"
git clone --depth 1 "<repo-url>" "$tmp_dir/template"
```

3. 현재 프로젝트 폴더로 템플릿 파일을 복사한다.

```sh
rsync -a \
  --exclude ".git/" \
  --exclude ".claude/settings.local.json" \
  --exclude "CLAUDE.local.md" \
  --exclude ".env" \
  "$tmp_dir/template/" ./
```

4. 사용자에게 두 가지만 묻는다.
   - 프로젝트 목적
   - 관련 자료 위치: OneDrive/SharePoint 연결, `00_refs/` 업로드, 아직 없음

5. `skills/project-init/SKILL.md`를 읽고 그 절차에 따라 현재 프로젝트를 초기화한다.

자료 위치 값은 다음 중 하나로 기록한다.

| 값 | 의미 |
|---|---|
| `A` | 회사 OneDrive/SharePoint 폴더 연결 |
| `B` | `00_refs/`에 직접 업로드 |
| `C` | 아직 자료 없음 |

6. skill 파일이 추가·수정·삭제된 경우 `skills/sync-skills/SKILL.md`를 읽고 세 skill 위치가 같은지 확인한다.
7. `system/INDEX.md`가 갱신되었는지 확인하고, 다음 추천 작업을 짧게 안내한다.

## 완료 조건

- `AGENTS.md`의 `Initialized`가 `YES`다.
- `PROJECT_NAME` placeholder가 실제 프로젝트명으로 바뀌었다.
- `01_analysis/00_project_brief.md`가 생성되었다.
- `system/INDEX.md`가 현재 파일 구조를 반영한다.
- `skills/`, `.agents/skills/`, `.claude/skills/`의 기본 skill이 같은 내용으로 유지되어 있다.
