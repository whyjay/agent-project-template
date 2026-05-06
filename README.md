# Agent Project Template

조직 내부에서 Claude Code, Codex, ChatGPT 같은 Agent와 함께 자료를 정리하고 산출물을 만들기 위한 프로젝트 템플릿입니다.

## 가장 쉬운 시작

1. Claude 또는 Codex에서 빈 프로젝트를 만듭니다.
2. 아래 문장을 그대로 붙여넣습니다.

```text
이 템플릿으로 초기화해줘: https://github.com/whyjay/agent-project-template
```

3. Agent가 묻는 두 가지에만 답합니다.
   - 프로젝트 목적
   - 관련 자료 위치: OneDrive/SharePoint 연결, `00_refs/` 업로드, 아직 없음

## Agent Bootstrap

Agent가 위 문장을 받으면 템플릿 파일을 조회해 현재 프로젝트에 직접 반영한 뒤 `AGENT_BOOTSTRAP.md`를 읽고 따라야 합니다.
사용자에게 별도 개발 도구 설치를 요구하지 않습니다. Agent가 repo를 직접 조회할 수 없는 환경에서는 사용자가 GitHub의 Download ZIP으로 받은 템플릿 파일을 업로드하면 됩니다.

이 저장소 자체는 원본 템플릿이므로 `AGENTS.md`의 `Initialized: NO`, `PROJECT_NAME`, `TBD` 상태를 유지합니다. 실제 프로젝트로 초기화하지 않습니다.

## GitHub 운영자 메모

- 조직 내부 GitHub repo로 관리합니다.
- Settings에서 `Template repository`를 켭니다.
- 대용량 파일 관리 도구는 사용하지 않습니다.
- 공용 skill 원본은 `skills/`에 두고, 같은 skill을 `.agents/skills/`와 `.claude/skills/`에도 동일하게 유지합니다.
