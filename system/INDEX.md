# 프로젝트 파일 인덱스

이 프로젝트의 모든 입력 자료·분석 노트·산출물 카탈로그.  
새 파일을 추가하거나 옮기면 여기에 함께 등록한다.

---

## 폴더 규칙

| 폴더 | 용도 | 파일 명명 규칙 |
|---|---|---|
| `system/` | Agent 운영용 관리 문서 (초기화 프로토콜, 파일 인덱스) | `INIT.md`, `INDEX.md` |
| `00_refs/` | 외부에서 받은 자료 원본. PDF, 회의 자료, 표준 문서, 고객 자료 등 | 가능하면 원본 파일명 유지 |
| `01_analysis/` | Agent와 함께 만든 분석·설계 노트 | `NN_topic.md` |
| `02_outputs/` | 코드, 다이어그램, 발표자료, 보고서 등 산출물 | 자유. 필요 시 하위 폴더 사용 |
| `skills/` | Codex/Claude/ChatGPT 공용 skill 원본 | `<skill-name>/SKILL.md` |
| `.agents/skills/` | Codex 자동 인식용 skill 복사본 | `skills/`와 동일하게 유지 |
| `.claude/skills/` | Claude Code용 skill 복사본 | `skills/`와 동일하게 유지 |

---

## 루트 진입 문서

| # | 파일 | 종류 | 한 줄 요약 |
|---|---|---|---|
| 1 | [README.md](../README.md) | MD | GitHub 첫 화면용 템플릿 사용 안내 |
| 2 | [AGENT_BOOTSTRAP.md](../AGENT_BOOTSTRAP.md) | MD | 무설치 repo URL 기반 템플릿 초기화 절차 |
| 3 | [AGENTS.md](../AGENTS.md) | MD | Agent가 항상 따라야 하는 프로젝트 운영 규칙 |
| 4 | [CLAUDE.md](../CLAUDE.md) | MD | Claude Code용 진입 지침 |
| 5 | [README_FOR_TEAM.md](../README_FOR_TEAM.md) | MD | 비개발자 팀원용 사용 안내 |
| 6 | [.gitignore](../.gitignore) | GITIGNORE | 로컬 설정과 원본 참고자료 commit 방지 규칙 |

---

## system/ — Agent 운영 문서

| # | 파일 | 종류 | 한 줄 요약 |
|---|---|---|---|
| 1 | [system/INIT.md](INIT.md) | MD | 새 프로젝트 초기화 프로토콜 |
| 2 | [system/INDEX.md](INDEX.md) | MD | 프로젝트 파일 카탈로그 |

---

## 공용 Agent Skills

| # | Skill | 파일 | 한 줄 요약 |
|---|---|---|---|
| 1 | ingest-refs | [skills/ingest-refs/SKILL.md](../skills/ingest-refs/SKILL.md) | 00_refs 자료 요약 및 분석 준비 |
| 2 | project-init | [skills/project-init/SKILL.md](../skills/project-init/SKILL.md) | 프로젝트 목적과 자료 위치를 받아 초기화 |
| 3 | sync-skills | [skills/sync-skills/SKILL.md](../skills/sync-skills/SKILL.md) | 세 skill 위치 동시 갱신 |
| 4 | update-index | [skills/update-index/SKILL.md](../skills/update-index/SKILL.md) | 파일 변경 후 INDEX.md 갱신 |

> `.agents/skills/`와 `.claude/skills/`는 자동 인식용 복사본이므로 별도 카탈로그에는 중복 등록하지 않는다.

---

## 00_refs/ — 외부 입력

| # | 파일 | 종류 | 출처 | 날짜 | 한 줄 요약 |
|---|---|---|---|---|---|
|-|-|-|-|-|-|

---

## 01_analysis/ — 분석·설계 노트

| # | 파일 | 작성일 | 한 줄 요약 | 핵심 산출 |
|---|---|---|---|---|
|-|-|-|-|-|

---

## 02_outputs/ — 산출물

| # | 파일 | 종류 | 작성일 | 한 줄 요약 | 핵심 산출 / 사용처 |
|---|---|---|---|---|---|
|-|-|-|-|-|-|

---

## 메타데이터 컨벤션

새 파일을 INDEX에 추가할 때 채울 필드:

- **파일**: 상대 경로 + Markdown 링크 (이 파일이 `system/` 안에 있으므로 루트 파일은 `../` 접두사 사용)
- **종류**: PDF / MD / IPYNB / PPTX / DOCX / 기타 + 크기
- **출처 또는 작성일**: refs는 `출처 / 날짜`, analysis·outputs는 `작성일`
- **한 줄 요약**: 80자 이내
- **핵심 산출**: 이 문서나 파일에서 끄집어낼 수 있는 결론·자산

---

## 변경 이력

| 날짜 | 변경 |
|---|---|
| 2026-05-06 | Claude 앱/Claude Code 자료 연결 안내 보강 |
| 2026-05-06 | 초기화 질문을 선택형 UI 우선 흐름으로 개선 |
| 2026-05-06 | bootstrap 절차에서 시스템 의존성 제거 문서 개편 |
| 2026-05-06 | 템플릿 운영을 skill 기반 절차로 정리 |
