# PROJECT_NAME

## 프로젝트 상태

- Initialized: NO
- Project name: PROJECT_NAME
- Owner:
- Last initialized:
- Primary reference source: NOT_SET

## 프로젝트 목표

<!-- PROJECT_GOAL_START -->
TBD
<!-- PROJECT_GOAL_END -->

## 초기화 여부 체크

Agent는 새 세션을 시작할 때 이 섹션을 먼저 확인한다.

단, 이 저장소 자체를 유지보수하는 작업은 예외다. 사용자가 템플릿 수정, GitHub 배포, bootstrap 개선, skill 구조 개선을 요청한 경우에는 `Initialized: NO` 상태를 유지한 채 템플릿 유지보수 작업을 수행한다.

외부 빈 프로젝트에서 아래 요청을 받은 Agent는 repo를 조회하거나, 조회가 불가하면 사용자가 제공한 ZIP/파일을 기준으로 `AGENT_BOOTSTRAP.md`를 먼저 읽고 따른다.

```text
이 템플릿으로 초기화해줘: https://github.com/whyjay/agent-project-template
```

`Initialized: NO` 상태인 경우 이 프로젝트는 아직 초기화되지 않은 것으로 간주한다. 프로젝트별 분석·제안·문서 작성을 시작하기 전에 `system/INIT.md`와 `skills/project-init/SKILL.md`를 읽고 초기화한다.

초기화가 이미 끝난 경우에는 `system/INIT.md`를 다시 실행하지 않는다. 단, 사용자가 "초기화 다시 해줘", "프로젝트 목적을 바꿔줘", "자료 폴더를 새로 연결했어"라고 요청하면 `system/INIT.md`를 참조해 재초기화한다.

## 파일 관리 원칙

- 프로젝트 폴더 구조와 파일 카탈로그는 `system/INDEX.md`에서 관리한다.
- 새 파일을 추가·이동·삭제하면 `skills/update-index/SKILL.md`에 따라 `system/INDEX.md`도 함께 갱신한다.
- `AGENTS.md`에는 프로젝트 상태, 목표, 운영 규칙만 담고 파일별 요약은 중복 기록하지 않는다.
- `00_refs/`의 원본 자료는 되도록 수정하지 않는다.
- 원본 자료를 읽고 만든 요약·분석·해석은 `01_analysis/`에 둔다. 페이지 유형, front-matter, cross-link, 출처 표기 규칙은 `01_analysis/README.md`를 따른다.
- 외부 공유용 보고서, 발표자료, 코드, 다이어그램은 `02_outputs/`에 둔다.
- 외부에 공유할 `.docx`, `.pdf`, `.pptx` 문서는 외부 문서를 따로 읽지 않아도 이해 가능한 stand-alone 문서로 작성한다.
- ingest, query, lint 같은 위키 운영 이벤트는 `system/LOG.md` 끝에 한 항목으로 append 한다.

## Skill 사용 원칙

- 공용 skill 원본은 `skills/` 아래에 둔다.
- `.agents/skills/`와 `.claude/skills/`는 자동 인식용 복사본이며 원본과 동일하게 유지한다.
- skill을 추가·수정·삭제할 때는 `skills/sync-skills/SKILL.md`를 따른다.
- skill은 반복 가능한 절차만 담고, 프로젝트별 파일 요약은 `system/INDEX.md`와 `01_analysis/`에 둔다.

## 지식 베이스 운영 원칙

이 프로젝트는 세 계층으로 운영한다.

- `00_refs/` — 외부에서 받은 **불변 원본**. 수정하지 않는다.
- `01_analysis/` — Agent가 작성·유지하는 **누적 위키**. 단순 메모 모음이 아니라 entity·concept·summary·comparison·synthesis 페이지가 cross-link으로 연결된다. 컨벤션은 `01_analysis/README.md`.
- `02_outputs/` — 외부에 공유 가능한 stand-alone 산출물. `01_analysis/`를 원천으로 작성한다.

## 작업 시 따를 것

- 기본 소통 언어는 한국어로 한다.
- 중요한 결정이 필요한 경우에는 가능한 선택지를 짧게 제시한 뒤 사용자 결정을 받아 진행한다.
- 새 분석이나 제안을 시작하기 전에 `system/INDEX.md`에서 관련 자료를 먼저 확인한다.
- 참고자료가 부족하면 추측으로 단정하지 말고, 필요한 자료 목록을 사용자에게 요청한다.
