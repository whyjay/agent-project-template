# Agent Project Template

조직 내부에서 Claude Code, Codex, ChatGPT 같은 Agent와 함께 자료를 정리하고 산출물을 만들기 위한 프로젝트 템플릿입니다.

## 가장 쉬운 시작

1. Claude 또는 Codex에서 빈 프로젝트를 만듭니다.
2. 아래 문장을 그대로 붙여넣습니다.

```text
이 템플릿으로 초기화해줘: https://github.com/whyjay/agent-project-template
```

3. Agent가 프로젝트 목적과 자료 위치를 물으면 답합니다.

Agent는 `AGENT_BOOTSTRAP.md`로 템플릿 파일을 가져오고, `skills/project-init/SKILL.md`로 초기화를 마칩니다. 별도 개발 도구 설치는 필요하지 않습니다.

## 원본 템플릿 운영

이 저장소 자체는 원본 템플릿이므로 `AGENTS.md`의 `Initialized: NO`, `PROJECT_NAME`, `TBD` 상태를 유지합니다.

- GitHub Settings에서 `Template repository`를 켭니다.
- 대용량 파일 관리 도구는 사용하지 않습니다.
- 공용 skill 원본은 `skills/`에 두고, `.agents/skills/`와 `.claude/skills/` 복사본을 동일하게 유지합니다.
