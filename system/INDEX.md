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
| `.agents/skills/` | Codex 자동 인식용 skill 복사본 | `python3 scripts/sync_skills.py`로 생성 |
| `.claude/skills/` | Claude Code용 skill 복사본 | `skills/`와 동일하게 유지 |
| `scripts/` | 선택 실행용 자동화 스크립트 | `verb_noun.py` |

---

## 루트 진입 문서

| # | 파일 | 종류 | 한 줄 요약 |
|---|---|---|---|
| 1 | [README.md](../README.md) | MD | GitHub 첫 화면용 템플릿 사용 안내 |
| 2 | [AGENT_BOOTSTRAP.md](../AGENT_BOOTSTRAP.md) | MD | repo URL 기반 템플릿 설치 절차 |
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
| 3 | update-index | [skills/update-index/SKILL.md](../skills/update-index/SKILL.md) | 파일 변경 후 INDEX.md 갱신 |

> `.agents/skills/`와 `.claude/skills/`는 자동 인식용 복사본이므로 별도 카탈로그에는 중복 등록하지 않는다.

---

## 자동화 스크립트

| # | 파일 | 종류 | 한 줄 요약 |
|---|---|---|---|
| 1 | [scripts/init_project.py](../scripts/init_project.py) | PY / 7.7 KB | 대화형 프로젝트 초기화 스크립트 |
| 2 | [scripts/sync_skills.py](../scripts/sync_skills.py) | PY / 3.2 KB | 공용 skill 원본을 Agent별 자동 인식 폴더로 동기화 |
| 3 | [scripts/update_index.py](../scripts/update_index.py) | PY / 8.4 KB | 현재 폴더 구조를 기준으로 INDEX.md 재생성 |

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
- **종류**: PDF / MD / PY / IPYNB / PPTX / DOCX / 기타 + 크기
- **출처 또는 작성일**: refs는 `출처 / 날짜`, analysis·outputs는 `작성일`
- **한 줄 요약**: 80자 이내
- **핵심 산출**: 이 문서나 파일에서 끄집어낼 수 있는 결론·자산

---

## 변경 이력

| 날짜 | 변경 |
|---|---|
| 2026-05-06 | `scripts/update_index.py`로 INDEX 자동 갱신 |
