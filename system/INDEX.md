# 프로젝트 파일 인덱스

이 프로젝트의 입력 자료·분석 노트·산출물 카탈로그다. 새 파일을 추가·이동·삭제하면 함께 갱신한다.

## 폴더 규칙

| 폴더 | 용도 | 파일 명명 규칙 |
|---|---|---|
| `system/` | Agent 운영용 관리 문서 | `INIT.md`, `INDEX.md`, `LOG.md` |
| `00_refs/` | 외부에서 받은 원본 자료 | 가능하면 원본 파일명 유지 |
| `01_analysis/` | Agent가 작성·유지하는 위키 (entity·concept·summary·comparison·synthesis 페이지) | 컨벤션은 `01_analysis/README.md` |
| `02_outputs/` | 보고서, 발표자료, 코드, 다이어그램 등 산출물 | 자유. 필요 시 하위 폴더 사용 |
| `skills/` | 공용 skill 원본 | `<skill-name>/SKILL.md` |
| `.agents/skills/` | Codex 자동 인식용 skill 복사본 | `skills/`와 동일하게 유지 |
| `.claude/skills/` | Claude Code용 skill 복사본 | `skills/`와 동일하게 유지 |

## 루트 진입 문서

| # | 파일 | 종류 | 한 줄 요약 |
|---|---|---|---|
| 1 | [README.md](../README.md) | MD | 템플릿 빠른 시작과 원본 운영 메모 |
| 2 | [AGENT_BOOTSTRAP.md](../AGENT_BOOTSTRAP.md) | MD | 외부 프로젝트에 템플릿 파일을 가져오는 bootstrap 절차 |
| 3 | [AGENTS.md](../AGENTS.md) | MD | Agent 세션 guard와 핵심 운영 규칙 |
| 4 | [CLAUDE.md](../CLAUDE.md) | MD | Claude Code용 진입 지침 |
| 5 | [README_FOR_TEAM.md](../README_FOR_TEAM.md) | MD | 비개발자 팀원용 사용 안내 |
| 6 | [.gitignore](../.gitignore) | GITIGNORE | 로컬 설정과 원본 참고자료 commit 방지 규칙 |

## system/ — Agent 운영 문서

| # | 파일 | 종류 | 한 줄 요약 |
|---|---|---|---|
| 1 | [system/INIT.md](INIT.md) | MD | 초기화 산출물 계약과 skill 위임 지침 |
| 2 | [system/INDEX.md](INDEX.md) | MD | 프로젝트 파일 카탈로그 |
| 3 | [system/LOG.md](LOG.md) | MD | ingest·query·lint 등 위키 운영 이벤트 시간순 로그 |

## 공용 Agent Skills

| # | Skill | 파일 | 한 줄 요약 |
|---|---|---|---|
| 1 | ingest-refs | [skills/ingest-refs/SKILL.md](../skills/ingest-refs/SKILL.md) | `00_refs/` 자료 요약 및 분석 준비 |
| 2 | project-init | [skills/project-init/SKILL.md](../skills/project-init/SKILL.md) | 프로젝트 목적과 자료 위치를 받아 초기화 |
| 3 | sync-skills | [skills/sync-skills/SKILL.md](../skills/sync-skills/SKILL.md) | 세 skill 위치 동시 갱신 |
| 4 | update-index | [skills/update-index/SKILL.md](../skills/update-index/SKILL.md) | 파일 변경 후 INDEX 갱신 |

> `.agents/skills/`와 `.claude/skills/`는 자동 인식용 복사본이므로 별도 카탈로그에는 중복 등록하지 않는다.

## 00_refs/ — 외부 입력

| # | 파일 | 종류 | 출처 | 날짜 | 한 줄 요약 |
|---|---|---|---|---|---|
|-|-|-|-|-|-|

## 01_analysis/ — 위키 (entity·concept·summary·comparison·synthesis)

| # | 파일 | 작성일 | 한 줄 요약 | 핵심 산출 |
|---|---|---|---|---|
| 1 | [01_analysis/README.md](../01_analysis/README.md) | 2026-05-09 | 위키 페이지 유형, front-matter, cross-link, 출처 컨벤션 | — |

## 02_outputs/ — 산출물

| # | 파일 | 종류 | 작성일 | 한 줄 요약 | 핵심 산출 / 사용처 |
|---|---|---|---|---|---|
|-|-|-|-|-|-|

## 메타데이터 컨벤션

- 루트 파일 링크는 `../` 접두사를 사용한다.
- `00_refs/`는 출처와 날짜를, `01_analysis/`와 `02_outputs/`는 작성일과 핵심 산출을 적는다.
- 한 줄 요약은 80자 이내로 유지한다.

## 변경 이력

| 날짜 | 변경 |
|---|---|
| 2026-05-09 | Karpathy "LLM Wiki" 패턴 반영 — `system/LOG.md`, `01_analysis/README.md` 추가, `ingest-refs` 확장 |
| 2026-05-06 | 중복 문서를 skill 중심 구조로 압축 |
| 2026-05-06 | Claude 앱/Claude Code 자료 연결 안내 보강 |
| 2026-05-06 | 초기화 질문을 선택형 UI 우선 흐름으로 개선 |
| 2026-05-06 | bootstrap 절차에서 시스템 의존성 제거 문서 개편 |
| 2026-05-06 | 템플릿 운영을 skill 기반 절차로 정리 |
