# Agent Bootstrap

이 문서는 사용자가 빈 Claude/Codex 프로젝트에서 아래처럼 요청했을 때 따르는 초기화 절차다.

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
- 사용자의 운영체제나 별도 개발 도구 설치 여부에 의존하지 않는다. 사용자는 Claude/Codex와 파일 업로드 기능만 있으면 된다.

## 절차

1. 사용자가 준 GitHub repo URL을 확인한다.
2. Agent가 사용할 수 있는 내장 조회 기능으로 템플릿 repo의 파일 목록과 내용을 확인한다.
3. 현재 프로젝트 폴더에 필요한 템플릿 파일과 폴더를 직접 생성하거나 갱신한다.
   - 복사 대상: `AGENTS.md`, `CLAUDE.md`, `README.md`, `README_FOR_TEAM.md`, `AGENT_BOOTSTRAP.md`, `system/`, `skills/`, `.agents/skills/`, `.claude/skills/`, `00_refs/.gitkeep`, `01_analysis/.gitkeep`, `02_outputs/.gitkeep`, `02_outputs/diagrams/.gitkeep`, `02_outputs/reports/.gitkeep`
   - 제외 대상: `.git/`, `.claude/settings.local.json`, `CLAUDE.local.md`, `.env`
4. Agent가 repo URL을 직접 조회할 수 없는 환경이면 사용자에게 GitHub의 Download ZIP으로 받은 템플릿 파일을 프로젝트에 업로드해달라고 요청한다.
   - 압축이 해제된 파일 목록이 보이면 그 파일을 기준으로 같은 제외 규칙을 적용한다.
   - 사용자가 압축 파일만 올린 경우 Agent가 읽을 수 있는 범위에서 압축 내용을 확인하고, 읽을 수 없으면 압축 해제 후 다시 업로드하도록 요청한다.
5. 사용자에게 두 가지를 순서대로 묻는다.
   - 두 질문은 목적 먼저, 자료 위치 다음 순서로 분리해서 묻고 한 번에 묻지 않는다.
   - 프로젝트 목적은 자유서술로 요청하고 답변을 받은 뒤 다음 질문으로 넘어간다.
   - 관련 자료 위치는 가능한 경우 Claude/Codex의 native option/choice UI로 묻는다.
   - 선택형 UI가 없는 환경에서만 짧은 A/B/C 텍스트 질문으로 대체한다.

6. `skills/project-init/SKILL.md`를 읽고 그 절차에 따라 현재 프로젝트를 초기화한다.

자료 위치 값은 다음 중 하나로 기록한다.

| 값 | 의미 |
|---|---|
| `A` | 회사 OneDrive/SharePoint 폴더 연결 |
| `B` | `00_refs/`에 직접 업로드 |
| `C` | 아직 자료 없음 |

A를 선택한 경우 환경별로 다음 순서를 따른다.

- Claude 앱/웹에서는 공식 공개 기능으로 Agent가 Claude 앱 + 버튼을 직접 트리거한다고 가정하지 않는다. 사용자가 채팅창 왼쪽 아래 `+` 버튼 또는 프로젝트 Files 섹션에서 자료를 추가하도록 안내한다.
- Claude Code에서는 로컬 폴더 참조를 위해 `/add-dir <path>`, 실행 시 `--add-dir <path>`, 또는 설정의 `additionalDirectories`를 안내한다.
- macOS 로컬 GUI와 shell 실행이 실제로 가능하면 다음 명령으로 `osascript` 선택적 시도를 할 수 있다.

```sh
osascript -e 'POSIX path of (choose folder with prompt "OneDrive/SharePoint reference folder를 선택하세요")'
```

사용자가 취소하거나 GUI, 권한, 실행 환경 문제로 실패하면 OneDrive/SharePoint 폴더 경로를 직접 입력받는다. 받은 경로가 로컬에서 접근 가능하면 존재 여부를 확인하고 `system/INDEX.md`와 초기화 brief에 reference source로 기록한다.

7. skill 파일이 추가·수정·삭제된 경우 `skills/sync-skills/SKILL.md`를 읽고 세 skill 위치가 같은지 확인한다.
8. `system/INDEX.md`가 갱신되었는지 확인하고, 다음 추천 작업을 짧게 안내한다.

## 완료 조건

- `AGENTS.md`의 `Initialized`가 `YES`다.
- `PROJECT_NAME` placeholder가 실제 프로젝트명으로 바뀌었다.
- `01_analysis/00_project_brief.md`가 생성되었다.
- `system/INDEX.md`가 현재 파일 구조를 반영한다.
- `skills/`, `.agents/skills/`, `.claude/skills/`의 기본 skill이 같은 내용으로 유지되어 있다.
- 사용자 OS나 별도 명령줄 도구 설치 여부와 무관하게 진행 가능한 상태다.
