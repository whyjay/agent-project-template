# Agent Bootstrap

빈 Claude/Codex 프로젝트에서 사용자가 아래처럼 요청했을 때 따르는 진입 절차다.

```text
이 템플릿으로 초기화해줘: https://github.com/whyjay/agent-project-template
```

## 목표

현재 작업 폴더에 이 템플릿의 기본 파일 구조를 안전하게 가져온 뒤, `skills/project-init/SKILL.md` 절차로 실제 프로젝트 초기화를 넘긴다.

## 안전 규칙

- 현재 폴더에 `AGENTS.md`, `CLAUDE.md`, `system/`, `skills/`, `.agents/skills/`, `.claude/skills/` 중 하나라도 이미 있으면 덮어쓰기 전에 중단하고 사용자 확인을 받는다.
- `README.md`만 있는 빈 GitHub repo라면 내용이 비어 있거나 템플릿 교체에 사용자가 동의한 경우에만 덮어쓴다.
- `.git/`, `.claude/settings.local.json`, `CLAUDE.local.md`, `.env` 파일은 템플릿에서 복사하지 않는다.
- 이 원본 템플릿 repo 안에서 작업 중이면 초기화를 실행하지 않고 템플릿 유지보수 작업으로 취급한다.
- 사용자 운영체제나 별도 개발 도구 설치 여부에 의존하지 않는다.

## 절차

1. 사용자가 준 GitHub repo URL을 확인한다.
2. Agent가 사용할 수 있는 내장 조회 기능으로 템플릿 repo의 파일 목록과 내용을 확인한다.
3. 현재 프로젝트 폴더에 필요한 템플릿 파일과 폴더를 직접 생성하거나 갱신한다.
   - 복사 대상: `AGENTS.md`, `CLAUDE.md`, `README.md`, `README_FOR_TEAM.md`, `AGENT_BOOTSTRAP.md`, `system/`, `skills/`, `.agents/skills/`, `.claude/skills/`, `00_refs/.gitkeep`, `01_analysis/.gitkeep`, `02_outputs/.gitkeep`, `02_outputs/diagrams/.gitkeep`, `02_outputs/reports/.gitkeep`
   - 제외 대상: `.git/`, `.claude/settings.local.json`, `CLAUDE.local.md`, `.env`
4. repo URL을 직접 조회할 수 없으면 사용자에게 GitHub의 Download ZIP으로 받은 템플릿 파일을 프로젝트에 업로드해달라고 요청한다.
   - 압축이 해제된 파일 목록이 보이면 그 파일을 기준으로 같은 제외 규칙을 적용한다.
   - 압축 파일만 보이고 내용을 확인할 수 없으면 압축 해제 후 다시 업로드하도록 요청한다.
5. `skills/project-init/SKILL.md`를 읽고 프로젝트 목적 질문, 자료 위치 선택, 파일 갱신, 완료 확인을 그 절차에 따라 수행한다.
6. skill 파일이 추가·수정·삭제된 경우 `skills/sync-skills/SKILL.md`로 세 skill 위치의 정합성을 확인한다.
7. `system/INDEX.md`가 현재 파일 구조를 반영하는지 확인하고 다음 추천 작업을 짧게 안내한다.
