---
name: ingest-refs
description: Read a new source in 00_refs and integrate it into the 01_analysis wiki — write a summary page, update related entity/concept pages, maintain cross-links, and log the ingest.
---

# ingest-refs skill

Keep this skill identical across `skills/`, `.agents/skills/`, and `.claude/skills/`.

`01_analysis/`는 누적되는 위키다. 단순 요약이 아니라 source 한 건이 들어올 때마다 관련 페이지를 함께 갱신한다. 페이지 컨벤션은 `01_analysis/README.md` 참고.

Use after one or more reference files are added to `00_refs/`.

## Procedure

1. **Scan** `00_refs/` 와 비교해 `01_analysis/`에 아직 ingest 되지 않은 source를 찾는다 (필요 시 `system/LOG.md`의 ingest 이력 확인).
2. **Read & summarize**: 각 source에 대해 제목/파일명, 출처, 날짜, 핵심 주장 3~5개, 프로젝트와의 관련성을 추출한다.
3. **Summary page**: `01_analysis/summary-<slug>.md` 를 생성하거나 갱신한다. `01_analysis/README.md` 의 front-matter 규약을 따르고 `source_ids` 에 해당 ref 경로를 적는다.
4. **Wiki update**: source가 다루는 entity, concept를 식별한다.
   - 해당 페이지가 이미 있으면 새 사실을 통합한다. 기존 단정과 모순되면 *모순:* 또는 *업데이트:* 로 명시하고 두 출처를 모두 인용한다.
   - 없으면 `entity-*.md`, `concept-*.md` 등을 새로 만든다.
5. **Cross-links**: summary 페이지 ↔ entity/concept 페이지를 양방향으로 연결한다. 관련 기존 페이지에서도 새 페이지로의 링크를 추가한다.
6. **Index**: `update-index` skill 절차에 따라 `system/INDEX.md` 의 `00_refs/`, `01_analysis/` 섹션을 갱신한다.
7. **Log**: `system/LOG.md` 끝에 항목을 append.
   ```
   ## [YYYY-MM-DD] ingest | <source 제목>
   - source: 00_refs/<file>
   - touched: 01_analysis/summary-<slug>.md, 01_analysis/entity-<x>.md, ...
   - notes: 한 줄 메모 (선택)
   ```
8. **Missing materials**: 중요한 자료가 빠져 있으면 `01_analysis/00_project_brief.md` 의 TODO에 추가한다 (있을 때만).

## Rules

- `00_refs/` 의 원본 파일을 수정하지 않는다.
- `AGENTS.md` 에 source별 요약을 직접 적지 않는다. 위키와 INDEX, LOG에만 남긴다.
- 사실·수치·인용은 페이지 본문에서 출처를 인라인으로 표기한다 (`(출처: 00_refs/...)`).
- 한 source가 보통 5~15개 페이지를 건드릴 수 있다. 모두 같은 ingest 작업의 일부로 처리한다.
- 파일을 읽을 수 없으면 LOG와 summary 페이지에 그 한계를 명시하고, 추측으로 채우지 않는다.
- skill 본문에 프로젝트별 파일 요약을 넣지 않는다.
