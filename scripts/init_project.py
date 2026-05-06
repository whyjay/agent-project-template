#!/usr/bin/env python3
"""
Initialize a Codex/Claude project template.

Usage:
    python3 scripts/init_project.py
    python3 scripts/init_project.py --project-name "My Project" --purpose "..." --ref-choice C --yes
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
REF_SOURCE_BY_CHOICE = {
    "A": "OneDrive/SharePoint connected",
    "B": "00_refs manual upload",
    "C": "None yet",
}


def prompt_multiline(title: str) -> str:
    print(title)
    print("입력을 마치려면 빈 줄에서 Enter를 누르세요.")
    lines: list[str] = []
    while True:
        line = input("> ")
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def replace_between_markers(text: str, start: str, end: str, replacement: str) -> str:
    start_idx = text.find(start)
    end_idx = text.find(end)
    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        return text

    start_pos = start_idx + len(start)
    return text[:start_pos] + "\n" + replacement.strip() + "\n" + text[end_idx:]


def replace_metadata_line(text: str, key: str, value: str) -> str:
    prefix = f"- {key}:"
    replacement = f"{prefix} {value}".rstrip()
    lines = []
    replaced = False

    for line in text.splitlines():
        if line.startswith(prefix):
            lines.append(replacement)
            replaced = True
        else:
            lines.append(line)

    if not replaced:
        lines.append(replacement)

    return "\n".join(lines) + "\n"


def update_agents(project_name: str, purpose: str, ref_source: str, owner: str = "") -> None:
    path = ROOT / "AGENTS.md"
    text = path.read_text(encoding="utf-8")

    text = text.replace("PROJECT_NAME", project_name)
    text = replace_metadata_line(text, "Initialized", "YES")
    text = replace_metadata_line(text, "Project name", project_name)
    if owner:
        text = replace_metadata_line(text, "Owner", owner)
    text = replace_metadata_line(text, "Last initialized", date.today().isoformat())
    text = replace_metadata_line(text, "Primary reference source", ref_source)

    purpose_md = purpose.strip() if purpose.strip() else "TBD"
    text = replace_between_markers(
        text,
        "<!-- PROJECT_GOAL_START -->",
        "<!-- PROJECT_GOAL_END -->",
        purpose_md,
    )

    path.write_text(text, encoding="utf-8")


def create_project_brief(project_name: str, purpose: str, ref_source: str) -> None:
    path = ROOT / "01_analysis" / "00_project_brief.md"
    if path.exists():
        print(f"이미 존재해서 덮어쓰지 않았습니다: {path.relative_to(ROOT)}")
        return

    content = f"""# Project Brief — {project_name}

## 1. 프로젝트 목적

{purpose if purpose else "TBD"}

## 2. 최종 산출물

TBD

## 3. 주요 사용자 / 독자

TBD

## 4. 성공 기준

TBD

## 5. 참고자료 위치

{ref_source}

## 6. 현재 참고자료 목록

Agent 또는 `scripts/update_index.py`로 `system/INDEX.md`를 갱신한 뒤 확인한다.

## 7. 아직 필요한 자료

- [ ] 배경 설명 자료
- [ ] 기존 회의록 또는 논의 메모
- [ ] 고객/이해관계자 요구사항
- [ ] 관련 기술 문서
- [ ] 기존 산출물 또는 예시 문서

## 8. 다음 작업 후보

- [ ] `00_refs/` 자료 요약
- [ ] 핵심 질문 정리
- [ ] 산출물 목차 초안 작성
"""
    path.write_text(content, encoding="utf-8")


def run_update_index() -> None:
    script = ROOT / "scripts" / "update_index.py"
    if not script.exists():
        return
    result = subprocess.run([sys.executable, str(script)], cwd=ROOT, text=True)
    if result.returncode != 0:
        print("INDEX.md 자동 갱신 중 오류가 있었습니다. 수동 확인이 필요합니다.")


def read_purpose(args: argparse.Namespace) -> str:
    if args.purpose and args.purpose_file:
        raise SystemExit("--purpose와 --purpose-file은 동시에 사용할 수 없습니다.")
    if args.purpose_file:
        return Path(args.purpose_file).read_text(encoding="utf-8").strip()
    return (args.purpose or "").strip()


def ref_source_from_args(args: argparse.Namespace) -> str:
    if args.ref_source:
        return args.ref_source.strip()

    choice = (args.ref_choice or "C").strip().upper()
    if choice not in REF_SOURCE_BY_CHOICE:
        raise SystemExit("--ref-choice는 A, B, C 중 하나여야 합니다.")
    return REF_SOURCE_BY_CHOICE[choice]


def collect_inputs(args: argparse.Namespace) -> tuple[str, str, str, str]:
    non_interactive = args.yes or args.non_interactive

    default_project_name = ROOT.name
    supplied_purpose = read_purpose(args)

    if non_interactive:
        if not supplied_purpose:
            raise SystemExit("비대화형 초기화에는 --purpose 또는 --purpose-file이 필요합니다.")
        return (
            args.project_name or default_project_name,
            supplied_purpose,
            ref_source_from_args(args),
            args.owner or "",
        )

    print("프로젝트 초기화를 시작합니다.\n")

    if args.project_name:
        project_name = args.project_name
    else:
        project_name = input(f"프로젝트명 [{default_project_name}]: ").strip() or default_project_name

    purpose = supplied_purpose or prompt_multiline(
        "\n프로젝트 목적을 입력해주세요. 왜 시작했는지, 최종 산출물, 사용자, 성공 기준을 포함하면 좋습니다."
    )

    if args.ref_choice or args.ref_source:
        ref_source = ref_source_from_args(args)
    else:
        print("\n관련 자료 위치를 선택해주세요.")
        print("A. 회사 OneDrive/SharePoint 폴더를 프로젝트에 연결함")
        print("B. 관련 자료를 00_refs/에 직접 업로드함")
        print("C. 아직 자료 없음")
        choice = input("선택 [A/B/C]: ").strip().upper() or "C"
        args.ref_choice = choice
        ref_source = ref_source_from_args(args)

    return project_name, purpose, ref_source, args.owner or ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Initialize this Agent project template.")
    parser.add_argument("--project-name", help="Project name. Defaults to the current folder name.")
    parser.add_argument("--owner", help="Optional project owner.")
    parser.add_argument("--purpose", help="Project purpose text.")
    parser.add_argument("--purpose-file", help="UTF-8 text file containing the project purpose.")
    parser.add_argument("--ref-choice", choices=["A", "B", "C", "a", "b", "c"], help="Reference source choice.")
    parser.add_argument("--ref-source", help="Explicit reference source label.")
    parser.add_argument("--yes", action="store_true", help="Run without interactive prompts.")
    parser.add_argument("--non-interactive", action="store_true", help="Alias for --yes.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    project_name, purpose, ref_source, owner = collect_inputs(args)

    for folder in ["00_refs", "01_analysis", "02_outputs", "skills", ".agents/skills", ".claude/skills", "system"]:
        (ROOT / folder).mkdir(parents=True, exist_ok=True)

    update_agents(project_name, purpose, ref_source, owner)
    create_project_brief(project_name, purpose, ref_source)
    run_update_index()

    print("\n초기화가 완료되었습니다.")
    print("- AGENTS.md 갱신")
    print("- 01_analysis/00_project_brief.md 생성 또는 확인")
    print("- system/INDEX.md 갱신 시도 완료")
    print("- 공용 skill 위치: skills/")
    print("- Codex용 skill 위치: .agents/skills/")
    print("- Claude Code용 skill 위치: .claude/skills/")


if __name__ == "__main__":
    main()
