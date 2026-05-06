# 프로젝트 초기화 프로토콜

이 문서는 새 Codex/Claude 프로젝트를 처음 사용할 때 따라야 하는 초기화 절차를 정의한다.  
`AGENTS.md`에서 프로젝트가 아직 초기화되지 않았다고 판단되면 이 문서를 따른다.

단, 원본 템플릿 repo 자체를 유지보수하는 작업에서는 초기화를 실행하지 않는다. 원본 템플릿은 배포를 위해 `Initialized: NO`, `PROJECT_NAME`, `TBD` 상태를 유지한다.

---

## 초기화의 목표

초기화의 목적은 다음 네 가지다.

1. 프로젝트 목적을 Agent가 이해할 수 있는 형태로 정리한다.
2. 관련 자료가 어디에 있는지 확인한다.
3. `AGENTS.md`, `system/INDEX.md`, `01_analysis/00_project_brief.md`를 초기 상태로 갱신한다.
4. 이후 작업에서 파일·자료·산출물이 흩어지지 않도록 최소 운영 규칙을 확정한다.

---

## 사용자에게 반드시 요청할 정보

초기화 시 Agent는 사용자에게 아래 두 가지를 반드시 요청한다.

### 1. 프로젝트 목적

사용자에게 다음 내용을 자유롭게 설명해달라고 요청한다.

- 이 프로젝트를 왜 시작했는가?
- 최종적으로 만들고 싶은 산출물은 무엇인가?
- 이 산출물을 누가 읽거나 사용할 예정인가?
- 성공적으로 끝났다고 판단할 기준은 무엇인가?
- 특별히 지켜야 할 제약, 선호, 문체, 포맷이 있는가?

사용자에게 보여줄 기본 질문 예시는 다음과 같다.

```text
프로젝트를 초기화하기 위해 두 가지만 확인하겠습니다.

1. 이 프로젝트의 목적을 3~10문장 정도로 설명해주세요.
   - 왜 시작했는지
   - 최종 산출물이 무엇인지
   - 누가 사용할 것인지
   - 성공 기준이 무엇인지

2. 관련 자료는 어디에 있나요?
   A. 회사 OneDrive/SharePoint 폴더를 프로젝트에 연결했습니다.
   B. 관련 자료를 `00_refs/`에 직접 업로드했습니다.
   C. 아직 자료가 없습니다.
```

### 2. 관련 자료 위치

자료 위치는 다음 세 가지 중 하나로 기록한다.

| 선택지 | 의미 | Agent의 다음 행동 |
|---|---|---|
| A | OneDrive/SharePoint 폴더를 프로젝트에 연결 | 연결된 폴더 경로를 확인하고 `system/INDEX.md`에 기록 |
| B | 파일을 `00_refs/`에 직접 업로드 | `00_refs/`를 스캔해 `system/INDEX.md` 갱신 |
| C | 아직 자료 없음 | 필요한 자료 목록을 `01_analysis/00_project_brief.md`에 TODO로 기록 |

---

## Agent가 수행할 초기화 절차

### Step 1. 프로젝트명 추정

가능하면 현재 폴더명을 프로젝트명으로 사용한다.  
사용자가 별도 프로젝트명을 제공하면 사용자의 이름을 우선한다.

### Step 2. `AGENTS.md` 갱신

다음 항목을 업데이트한다.

- `PROJECT_NAME` placeholder를 실제 프로젝트명으로 교체
- `Initialized: YES`
- `Project name: ...`
- `Owner: ...` 또는 비워둠
- `Last initialized: YYYY-MM-DD`
- `Primary reference source: OneDrive / 00_refs / None`
- `## 프로젝트 목표`의 `PROJECT_GOAL_START`와 `PROJECT_GOAL_END` 사이를 사용자 설명 기반으로 작성

주의:

- 파일별 요약을 `AGENTS.md`에 누적하지 않는다.
- 파일 목록과 메타데이터는 항상 `system/INDEX.md`에서 관리한다.
- `AGENTS.md`는 프로젝트 운영 규칙과 목표만 담는다.

### Step 3. `system/INDEX.md` 갱신

현재 존재하는 파일을 스캔해 `system/INDEX.md`에 등록한다.

특히 다음을 확인한다.

- `00_refs/`의 원본 자료
- `01_analysis/`의 분석 노트
- `02_outputs/`의 산출물
- `skills/`의 공용 skill
- `.agents/skills/`의 Codex용 skill 복사본
- `.claude/skills/`의 Claude Code용 skill 복사본
- 루트 진입 문서: `README.md`, `AGENT_BOOTSTRAP.md`, `AGENTS.md`, `CLAUDE.md`, `README_FOR_TEAM.md`
- `system/`의 운영 문서: `system/INIT.md`, `system/INDEX.md`

파일별로 가능한 한 아래 정보를 채운다.

- 상대 경로
- 종류
- 출처 또는 작성일
- 한 줄 요약
- 핵심 산출 또는 사용처

### Step 4. `01_analysis/00_project_brief.md` 생성

초기화 결과를 별도 문서로 남긴다.

권장 구조:

```md
# Project Brief

## 1. 프로젝트 목적

## 2. 최종 산출물

## 3. 주요 사용자 / 독자

## 4. 성공 기준

## 5. 참고자료 위치

## 6. 현재 참고자료 목록

## 7. 아직 필요한 자료

## 8. 다음 작업 후보
```

### Step 5. 자료 부족 시 요청 목록 생성

자료가 없거나 부족하면 추측으로 진행하지 말고 다음과 같이 정리한다.

```md
## 아직 필요한 자료

- [ ] 배경 설명 자료
- [ ] 기존 회의록 또는 논의 메모
- [ ] 고객/이해관계자 요구사항
- [ ] 관련 기술 문서
- [ ] 기존 산출물 또는 예시 문서
```

### Step 6. 초기화 완료 확인

초기화 완료 조건은 다음과 같다.

- `AGENTS.md`의 `Initialized`가 `YES`이다.
- 프로젝트 목표가 `TBD`가 아니다.
- `system/INDEX.md`가 현재 파일 구조를 반영한다.
- `01_analysis/00_project_brief.md`가 생성되어 있다.
- 자료가 없더라도 필요한 자료 TODO가 기록되어 있다.

---

## 최소 Skill 구성

이 템플릿은 다음 네 가지 skill을 기본으로 둔다.

| Skill | 공용 원본 | Codex용 복사본 | Claude Code용 복사본 | 목적 |
|---|---|---|---|---|
| project-init | `skills/project-init/SKILL.md` | `.agents/skills/project-init/SKILL.md` | `.claude/skills/project-init/SKILL.md` | 프로젝트 초기화 |
| update-index | `skills/update-index/SKILL.md` | `.agents/skills/update-index/SKILL.md` | `.claude/skills/update-index/SKILL.md` | 파일 추가·이동 후 `system/INDEX.md` 갱신 |
| ingest-refs | `skills/ingest-refs/SKILL.md` | `.agents/skills/ingest-refs/SKILL.md` | `.claude/skills/ingest-refs/SKILL.md` | `00_refs/` 자료 요약 및 분석 준비 |
| sync-skills | `skills/sync-skills/SKILL.md` | `.agents/skills/sync-skills/SKILL.md` | `.claude/skills/sync-skills/SKILL.md` | 세 skill 위치 동시 갱신 |

운영 원칙:

- `skills/`를 Codex, Claude, ChatGPT 등 모든 Agent가 참조할 공용 skill 원본으로 본다.
- `.agents/skills/`는 Codex가 자동 인식하기 위한 복사본이다.
- `.claude/skills/`는 Claude Code가 자동 인식하기 위한 복사본이다.
- skill을 추가·수정·삭제할 때는 `skills/`, `.agents/skills/`, `.claude/skills/`의 같은 skill 폴더를 동일한 변경 안에서 함께 갱신한다.
- skill 정합성을 확인해야 하면 `skills/sync-skills/SKILL.md`를 따른다.

---

## 비개발자용 운영 원칙

비개발자 사용자는 내부 파일 구조를 자세히 알 필요가 없다.  
다음 세 가지 행동만 기억하면 된다.

1. Claude/Codex에서 빈 프로젝트를 만든다.
2. “이 템플릿으로 초기화해줘: https://github.com/whyjay/agent-project-template”라고 요청한다.
3. 관련 자료를 `00_refs/`에 넣거나 OneDrive 폴더를 연결한다.

Agent는 이 요청을 받으면 이 문서를 참조해 초기화한다.
