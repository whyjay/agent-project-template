# Claude Project Instructions

공통 프로젝트 지침은 `AGENTS.md`를 따른다.

@AGENTS.md

프로젝트가 아직 초기화되지 않았다면 `system/INIT.md`를 읽고 초기화 프로토콜을 따른다.

@system/INIT.md

Claude Code에서 사용하는 skill은 `.claude/skills/`에 있다.  
공용 skill 원본은 `skills/`에 있고 Codex용 복사본은 `.agents/skills/`에 있다.
skill을 추가·수정·삭제할 때는 `skills/`, `.agents/skills/`, `.claude/skills/`의 같은 skill 폴더를 동일한 변경 안에서 함께 갱신한다. 자세한 절차는 `skills/sync-skills/SKILL.md`를 따른다.
