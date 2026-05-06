# 팀원용 프로젝트 템플릿 사용법

이 템플릿은 Codex, Claude Code, ChatGPT 같은 Agent와 함께 프로젝트 자료를 정리하고 산출물을 만들기 위한 최소 구조입니다.

---

## 처음 시작하는 방법

1. Claude 또는 Codex에서 빈 프로젝트를 만듭니다.
2. 아래 문장을 붙여넣습니다.

```text
이 템플릿으로 초기화해줘: https://github.com/whyjay/agent-project-template
```

3. Agent가 프로젝트 목적과 관련 자료 위치를 물으면 답합니다.
4. 관련 자료를 `00_refs/` 폴더에 넣습니다.
   - PDF
   - 회의 자료
   - 기존 보고서
   - 고객 자료
   - 참고 문서
5. 회사 OneDrive/SharePoint 자료를 쓰는 경우에는 해당 폴더를 로컬에 동기화한 뒤 `00_refs/` 아래에 넣거나 연결합니다.
   - Claude 앱/웹에서는 채팅창 왼쪽 아래 `+` 버튼으로 파일을 업로드하거나 프로젝트 Files 섹션에 추가합니다.
   - Claude Code에서는 폴더 경로를 알려주거나 `/add-dir <path>`로 참고 폴더를 추가할 수 있습니다.

---

## 폴더를 어떻게 쓰나요?

| 폴더 | 무엇을 넣나요? |
|---|---|
| `00_refs/` | 외부에서 받은 원본 자료 |
| `01_analysis/` | Agent와 함께 만든 분석 메모 |
| `02_outputs/` | 최종 보고서, 발표자료, 코드, 다이어그램 |
| `system/` | Agent 운영용 관리 문서 (초기화 프로토콜, 파일 인덱스) — 수정 불필요 |
| `skills/` | Codex/Claude/ChatGPT가 공통으로 참고할 작업 절차 |
| `.agents/skills/` | Codex가 자동 인식하는 skill 복사본 |
| `.claude/skills/` | Claude Code가 자동으로 인식하기 위한 skill 복사본 |

일반 팀원은 `skills/`, `.agents/skills/`, `.claude/skills/`를 직접 수정할 필요가 없습니다.  
그냥 Agent에게 “초기화해줘”, “INDEX 업데이트해줘”, “자료 요약해줘”라고 요청하면 됩니다.

---

## 꼭 기억할 규칙

- 원본 자료는 `00_refs/`에 그대로 둡니다.
- 분석 과정에서 만든 문서는 `01_analysis/`에 둡니다.
- 외부에 보낼 산출물은 `02_outputs/`에 둡니다.
- 파일을 추가하면 Agent에게 `system/INDEX.md 업데이트해줘`라고 요청합니다.

---

## 자주 쓰는 요청 문장

```text
이 프로젝트를 초기화해줘.
```

```text
00_refs에 새 자료를 넣었으니 system/INDEX.md를 업데이트해줘.
```

```text
00_refs 자료를 읽고 핵심 내용을 01_analysis에 요약해줘.
```

```text
지금까지 분석 내용을 바탕으로 외부 공유용 보고서를 02_outputs에 만들어줘.
```

---

## Codex와 Claude Code를 같이 쓸 때

- Codex 또는 일반 Agent는 루트의 `AGENTS.md`, `system/INIT.md`, `skills/`, `.agents/skills/`를 기준으로 작업합니다.
- Claude Code는 `CLAUDE.md`와 `.claude/skills/`를 함께 사용할 수 있습니다.
- skill을 수정할 때는 Agent에게 `skills/`, `.agents/skills/`, `.claude/skills/`의 같은 skill을 함께 갱신해달라고 요청하면 됩니다.
