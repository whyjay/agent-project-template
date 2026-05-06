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

Agent는 새 세션을 시작할 때 먼저 이 섹션을 확인한다.

단, 이 저장소 자체를 유지보수하는 작업은 예외다. 사용자가 템플릿 수정, GitHub 배포, bootstrap 개선, skill 구조 개선을 요청한 경우에는 `Initialized: NO` 상태를 유지한 채 템플릿 유지보수 작업을 수행한다.

외부 빈 프로젝트에서 “이 템플릿으로 초기화해줘: https://github.com/whyjay/agent-project-template” 요청을 받은 Agent는 이 repo를 clone하거나 조회한 뒤 `AGENT_BOOTSTRAP.md`를 먼저 읽고 따른다.

`Initialized: NO` 상태인 경우 이 프로젝트는 아직 초기화되지 않은 것으로 간주한다.

초기화되지 않은 경우:

1. 프로젝트별 분석·제안·문서 작성을 바로 시작하지 않는다.
2. `system/INIT.md`를 먼저 읽고 초기화 프로토콜을 따른다.
3. 가능하면 공용 skill인 `skills/project-init/SKILL.md`를 참조한다.
4. 사용자에게 최소 두 가지를 요청한다.
   - 프로젝트의 목적
   - 관련 자료 위치: 회사 OneDrive/SharePoint 폴더 연결 여부 또는 `00_refs/` 수동 업로드 여부
5. 초기화가 끝나면 이 파일의 프로젝트 상태를 갱신한다.

초기화가 이미 끝난 경우에는 `system/INIT.md`를 다시 실행하지 않는다. 단, 사용자가 "초기화 다시 해줘", "프로젝트 목적을 바꿔줘", "자료 폴더를 새로 연결했어"라고 요청하면 `system/INIT.md`를 참조해 재초기화한다.

## 프로젝트 폴더 구조

프로젝트 폴더 구조와 파일 카탈로그는 `system/INDEX.md`에서 확인한다. 새 파일을 추가·이동·삭제하면 `system/INDEX.md`도 함께 갱신한다.

## Skill 사용 원칙

- 공용 skill의 원본은 `skills/` 아래에 둔다.
- `.agents/skills/`는 Codex가 자동 인식하기 쉽도록 둔 복사본이다.
- `.claude/skills/`는 Claude Code가 자동 인식하기 쉽도록 둔 복사본이다.
- Codex 또는 일반 Agent는 자동 skill 인식이 되지 않는 환경에서도 `skills/<skill-name>/SKILL.md`를 참조해 동일한 절차를 따른다.
- skill을 추가·수정·삭제할 때는 `skills/`, `.agents/skills/`, `.claude/skills/`의 같은 skill 폴더를 동일한 변경 안에서 함께 갱신한다.
- skill 동기화 절차가 필요하면 `skills/sync-skills/SKILL.md`를 따른다.
- skill은 반복 가능한 절차만 담고, 프로젝트별 파일 요약은 `system/INDEX.md`와 `01_analysis/`에 둔다.

기본 skill:

| Skill | 공용 원본 | Codex 복사본 | Claude Code 복사본 | 목적 |
|---|---|---|---|---|
| project-init | `skills/project-init/SKILL.md` | `.agents/skills/project-init/SKILL.md` | `.claude/skills/project-init/SKILL.md` | 프로젝트 초기화 |
| update-index | `skills/update-index/SKILL.md` | `.agents/skills/update-index/SKILL.md` | `.claude/skills/update-index/SKILL.md` | 파일 추가·이동 후 `system/INDEX.md` 갱신 |
| ingest-refs | `skills/ingest-refs/SKILL.md` | `.agents/skills/ingest-refs/SKILL.md` | `.claude/skills/ingest-refs/SKILL.md` | `00_refs/` 자료 요약 및 분석 준비 |
| sync-skills | `skills/sync-skills/SKILL.md` | `.agents/skills/sync-skills/SKILL.md` | `.claude/skills/sync-skills/SKILL.md` | 세 skill 위치 동시 갱신 |

## 파일 관리 원칙

- 파일 목록은 `system/INDEX.md`에서 관리한다.
- 새 파일을 추가·이동·삭제할 때마다 `system/INDEX.md`도 함께 업데이트한다.
- `AGENTS.md`에는 파일별 정보를 중복 기록하지 않는다.
- `00_refs/`의 원본 자료는 되도록 수정하지 않는다.
- 원본 자료를 읽고 만든 요약·분석·해석은 `01_analysis/`에 둔다.
- 외부 공유용 보고서, 발표자료, 코드, 다이어그램은 `02_outputs/`에 둔다.
- 외부에 공유할 `.docx`, `.pdf`, `.pptx` 문서는 외부 문서를 따로 읽지 않아도 이해 가능한 stand-alone 문서로 작성한다.

## 작업 시 따를 것

- 기본 소통 언어는 한국어로 한다.
- 중요한 결정이 필요한 경우에는 가능한 선택지를 짧게 제시한 뒤 사용자 결정을 받아 진행한다.
- 새 분석이나 제안을 시작하기 전에 `system/INDEX.md`에서 관련 자료를 먼저 확인한다.
- 작업 결과로 새 파일이 생기면 반드시 `system/INDEX.md`에 등록한다.
- 참고자료가 부족하면 추측으로 단정하지 말고, 필요한 자료 목록을 사용자에게 요청한다.
