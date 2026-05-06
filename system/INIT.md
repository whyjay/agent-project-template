# 프로젝트 초기화 프로토콜

`AGENTS.md`에서 프로젝트가 아직 초기화되지 않았다고 판단되면 이 문서를 따른다. 단, 원본 템플릿 repo 자체를 유지보수하는 작업에서는 초기화를 실행하지 않는다. 원본 템플릿은 배포를 위해 `Initialized: NO`, `PROJECT_NAME`, `TBD` 상태를 유지한다.

## 초기화 목표

초기화는 다음 상태를 만드는 절차다.

- 프로젝트 목적과 성공 기준이 `AGENTS.md`와 `01_analysis/00_project_brief.md`에 정리되어 있다.
- 관련 자료 위치가 `OneDrive/SharePoint`, `00_refs/`, `None` 중 하나로 기록되어 있다.
- `system/INDEX.md`가 현재 파일 구조와 자료 목록을 반영한다.
- 자료가 없거나 부족하면 필요한 자료 TODO가 `01_analysis/00_project_brief.md`에 남아 있다.

## 실행 절차

1. `skills/project-init/SKILL.md`를 읽고 그 절차를 따른다.
2. 파일 목록 갱신이 필요하면 `skills/update-index/SKILL.md`를 따른다.
3. skill 파일을 추가·수정·삭제했다면 `skills/sync-skills/SKILL.md`를 따른다.

`project-init`이 초기화 실행의 source of truth다. 특히 사용자에게 묻는 두 질문의 순서, A/B/C 자료 위치 선택, OneDrive/SharePoint 처리, macOS folder picker fallback은 해당 skill에만 상세히 둔다.

## 완료 조건

- `AGENTS.md`의 `Initialized`가 `YES`이다.
- 프로젝트 목표가 `TBD`가 아니다.
- `01_analysis/00_project_brief.md`가 생성되어 있다.
- `system/INDEX.md`가 현재 파일 구조를 반영한다.
- `skills/`, `.agents/skills/`, `.claude/skills/`의 기본 skill 이름과 내용이 서로 일치한다.
