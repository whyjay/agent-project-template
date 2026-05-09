# 01_analysis 위키 컨벤션

`01_analysis/`는 일회성 메모 모음이 아니라 **LLM이 작성·유지하는 위키**다. 여기에 누적된 페이지들이 cross-link으로 연결되며 자료(`00_refs/`)를 합성한 결과를 담는다. `02_outputs/`로 나갈 산출물의 원천 자료 역할을 한다.

## 페이지 유형

| type | 용도 | 예시 파일명 |
|---|---|---|
| `summary` | 단일 source 한 건의 요약 | `summary-2026-05-08-foo-report.md` |
| `entity` | 인물, 조직, 제품, 사건 등 고유명사 페이지 | `entity-홍길동.md` |
| `concept` | 개념, 테마, 프레임워크 페이지 | `concept-rag.md` |
| `comparison` | 두 개 이상 entity·concept 비교 | `comparison-rag-vs-wiki.md` |
| `synthesis` | 여러 페이지를 묶은 종합·논지 | `synthesis-2026q2-thesis.md` |

## Front-matter (YAML)

모든 페이지는 다음 형식을 머리에 둔다.

```yaml
---
type: entity         # entity | concept | summary | comparison | synthesis
source_ids:          # 이 페이지가 근거로 삼은 00_refs/ 파일들
  - 00_refs/2026-05-08-foo-report.md
tags: []
last_updated: 2026-05-09
status: draft        # draft | stable
---
```

- `source_ids` 가 비어 있으면 (`synthesis` 외에는) 사실상 출처 없는 단정 → 가급적 피한다.
- `last_updated` 는 페이지를 새 source로 갱신할 때마다 갱신한다.

## Cross-link 규칙

- 같은 폴더 내부는 **상대 경로** 링크: `[홍길동](./entity-홍길동.md)`.
- Obsidian `[[문법]]` 도 호환되지만, 외부 도구에서 깨지지 않도록 상대 경로를 우선한다.
- 양방향 링크: 새 페이지를 만들면 관련 기존 페이지에서도 그 페이지로 연결한다.

## 출처 (provenance) 규칙

- 사실, 수치, 인용은 본문 인라인으로 출처를 표기: `... (출처: 00_refs/2026-05-08-foo-report.md)`.
- 같은 source가 여러 번 나오면 약식으로 가능: `(출처: foo-report)`. 단, 첫 등장 시 풀 경로를 한 번 적는다.
- 출처 없는 단정은 피한다. 추론·해석은 명시적으로 *해석:* 또는 *추정:* 으로 표시한다.

## 명명 규칙

- 소문자 kebab-case: `concept-knowledge-graph.md`.
- 한국어 명사가 핵심이면 그대로 사용 가능: `entity-홍길동.md`, `concept-지식베이스.md`.
- 페이지 유형 prefix(`summary-`, `entity-`, `concept-`, `comparison-`, `synthesis-`)는 권장사항이며 강제는 아님. 카탈로그(`system/INDEX.md`)와 검색 편의를 위해 사용한다.

## 위키 운영 흐름

1. **Ingest**: `00_refs/`에 새 자료가 들어오면 `ingest-refs` skill을 따라 summary 페이지 + 관련 entity/concept 페이지를 갱신한다.
2. **Query**: 위키에 질의할 때는 먼저 `system/INDEX.md`로 후보 페이지를 좁히고, 본문을 읽어 종합한다. 가치 있는 종합 결과는 새 `synthesis-*.md` 페이지로 다시 위키에 남긴다.
3. **Lint**: 주기적으로 모순, 고아 페이지(inbound link 없음), 오래된 단정, 빠진 cross-reference를 점검한다.

모든 운영 이벤트는 `system/LOG.md` 에 항목을 추가한다.

## 안 하는 것

- `00_refs/` 원본을 수정하지 않는다.
- 페이지별 요약을 `AGENTS.md`에 중복 기록하지 않는다 (그건 `system/INDEX.md`의 일).
- 외부 공유용 `.docx`/`.pdf`/`.pptx` 같은 stand-alone 산출물은 `02_outputs/`로 보낸다.
