# Claude Project Instructions

공통 프로젝트 지침은 `AGENTS.md`를 따른다.

@AGENTS.md

프로젝트가 아직 초기화되지 않았다면 `system/INIT.md`를 읽고 초기화 프로토콜을 따른다.

@system/INIT.md

Claude Code에서 사용하는 skill은 `.claude/skills/`에 있다.  
공용 skill 원본은 `skills/`에 있고 Codex용 복사본은 `.agents/skills/`에 있다.
skill을 수정한 뒤에는 `python3 scripts/sync_skills.py`를 실행해 `skills/`, `.agents/skills/`, `.claude/skills/`를 같은 내용으로 유지한다.
