#!/usr/bin/env python3
"""
Regenerate system/INDEX.md from the current project folder.

This script intentionally uses conservative placeholder summaries.
Ask an Agent to improve the summaries after running it.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ROOT_DOCS = [
    "README.md",
    "AGENT_BOOTSTRAP.md",
    "AGENTS.md",
    "CLAUDE.md",
    "README_FOR_TEAM.md",
    ".gitignore",
]

SYSTEM_DOCS = [
    "system/INIT.md",
    "system/INDEX.md",
]

SCAN_DIRS = [
    "00_refs",
    "01_analysis",
    "02_outputs",
]


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def file_kind(path: Path) -> str:
    ext = path.suffix.lower().lstrip(".")
    if not ext:
        ext = "file"
    size = path.stat().st_size
    if size >= 1024 * 1024:
        return f"{ext.upper()} / {size / (1024 * 1024):.1f} MB"
    if size >= 1024:
        return f"{ext.upper()} / {size / 1024:.1f} KB"
    return ext.upper()


def list_files(folder: str) -> list[Path]:
    root = ROOT / folder
    if not root.exists():
        return []
    files = [
        p for p in root.rglob("*")
        if p.is_file() and p.name not in {".gitkeep", ".DS_Store"}
    ]
    return sorted(files, key=lambda p: rel(p))


def md_link(path: Path) -> str:
    """INDEX.md는 system/ 안에 있으므로 모든 링크 앞에 ../을 붙인다."""
    r = rel(path)
    return f"[{r}](../{r})"


def list_skills() -> list[Path]:
    skills_root = ROOT / "skills"
    if not skills_root.exists():
        return []
    return sorted(
        [p / "SKILL.md" for p in skills_root.iterdir() if (p / "SKILL.md").is_file()],
        key=lambda p: rel(p),
    )


def build_index() -> str:
    today = date.today().isoformat()

    root_summaries = {
        "README.md": "GitHub 첫 화면용 템플릿 사용 안내",
        "AGENT_BOOTSTRAP.md": "repo URL 기반 템플릿 설치 절차",
        "AGENTS.md": "Agent가 항상 따라야 하는 프로젝트 운영 규칙",
        "CLAUDE.md": "Claude Code용 진입 지침",
        "README_FOR_TEAM.md": "비개발자 팀원용 사용 안내",
        ".gitignore": "로컬 설정과 원본 참고자료 commit 방지 규칙",
    }
    root_kinds = {
        "README.md": "MD",
        "AGENT_BOOTSTRAP.md": "MD",
        "AGENTS.md": "MD",
        "CLAUDE.md": "MD",
        "README_FOR_TEAM.md": "MD",
        ".gitignore": "GITIGNORE",
    }
    root_rows = []
    for i, name in enumerate(ROOT_DOCS, start=1):
        p = ROOT / name
        if p.exists():
            # INDEX.md는 system/ 안에 있으므로 루트 파일 링크는 ../로 시작한다.
            root_rows.append(
                f"| {i} | [{name}](../{name}) | {root_kinds.get(name, file_kind(p))} | {root_summaries.get(name, '루트 문서')} |"
            )

    system_summaries = {
        "system/INIT.md": "새 프로젝트 초기화 프로토콜",
        "system/INDEX.md": "프로젝트 파일 카탈로그",
    }
    system_rows = []
    for i, name in enumerate(SYSTEM_DOCS, start=1):
        p = ROOT / name
        if p.exists():
            # system/ 안에서 본인 폴더의 파일은 상대 경로로 직접 가리킨다.
            link_target = name.split("/", 1)[1]
            system_rows.append(
                f"| {i} | [{name}]({link_target}) | MD | {system_summaries.get(name, 'system 문서')} |"
            )
    if not system_rows:
        system_rows.append("|-|-|-|-|")

    skill_summaries = {
        "project-init": "프로젝트 목적과 자료 위치를 받아 초기화",
        "update-index": "파일 변경 후 INDEX.md 갱신",
        "ingest-refs": "00_refs 자료 요약 및 분석 준비",
    }
    skill_rows = []
    for i, p in enumerate(list_skills(), start=1):
        skill_name = p.parent.name
        skill_rows.append(
            f"| {i} | {skill_name} | {md_link(p)} | {skill_summaries.get(skill_name, '공용 Agent skill')} |"
        )
    if not skill_rows:
        skill_rows.append("|-|-|-|-|")

    script_rows = []
    script_summaries = {
        "init_project.py": "대화형 프로젝트 초기화 스크립트",
        "sync_skills.py": "공용 skill 원본을 Agent별 자동 인식 폴더로 동기화",
        "update_index.py": "현재 폴더 구조를 기준으로 INDEX.md 재생성",
    }
    for i, p in enumerate(list_files("scripts"), start=1):
        script_rows.append(
            f"| {i} | {md_link(p)} | {file_kind(p)} | {script_summaries.get(p.name, '선택 실행용 자동화 스크립트')} |"
        )
    if not script_rows:
        script_rows.append("|-|-|-|-|")

    refs_rows = []
    for i, p in enumerate(list_files("00_refs"), start=1):
        refs_rows.append(f"| {i} | {md_link(p)} | {file_kind(p)} | TODO | TODO | TODO: 한 줄 요약 |")

    analysis_rows = []
    for i, p in enumerate(list_files("01_analysis"), start=1):
        analysis_rows.append(f"| {i} | {md_link(p)} | {today} | TODO: 한 줄 요약 | TODO: 핵심 산출 |")

    outputs_rows = []
    for i, p in enumerate(list_files("02_outputs"), start=1):
        outputs_rows.append(f"| {i} | {md_link(p)} | {file_kind(p)} | {today} | TODO: 한 줄 요약 | TODO: 사용처 |")

    if not refs_rows:
        refs_rows.append("|-|-|-|-|-|-|")
    if not analysis_rows:
        analysis_rows.append("|-|-|-|-|-|")
    if not outputs_rows:
        outputs_rows.append("|-|-|-|-|-|-|")

    return f"""# 프로젝트 파일 인덱스

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
{chr(10).join(root_rows)}

---

## system/ — Agent 운영 문서

| # | 파일 | 종류 | 한 줄 요약 |
|---|---|---|---|
{chr(10).join(system_rows)}

---

## 공용 Agent Skills

| # | Skill | 파일 | 한 줄 요약 |
|---|---|---|---|
{chr(10).join(skill_rows)}

> `.agents/skills/`와 `.claude/skills/`는 자동 인식용 복사본이므로 별도 카탈로그에는 중복 등록하지 않는다.

---

## 자동화 스크립트

| # | 파일 | 종류 | 한 줄 요약 |
|---|---|---|---|
{chr(10).join(script_rows)}

---

## 00_refs/ — 외부 입력

| # | 파일 | 종류 | 출처 | 날짜 | 한 줄 요약 |
|---|---|---|---|---|---|
{chr(10).join(refs_rows)}

---

## 01_analysis/ — 분석·설계 노트

| # | 파일 | 작성일 | 한 줄 요약 | 핵심 산출 |
|---|---|---|---|---|
{chr(10).join(analysis_rows)}

---

## 02_outputs/ — 산출물

| # | 파일 | 종류 | 작성일 | 한 줄 요약 | 핵심 산출 / 사용처 |
|---|---|---|---|---|---|
{chr(10).join(outputs_rows)}

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
| {today} | `scripts/update_index.py`로 INDEX 자동 갱신 |
"""


def main() -> None:
    path = ROOT / "system" / "INDEX.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_index(), encoding="utf-8")
    print(f"Updated {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
