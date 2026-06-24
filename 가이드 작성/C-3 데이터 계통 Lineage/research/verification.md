# C-3 데이터 계통(Data Lineage) 가이드 — 출처 검증 보고서

검증일: 2026-06-24
검증자: 출처 검증 에이전트

## 검증 결과 요약

- 전체 20개 URL 검증
- 정상(200): 17개
- 차단(403, 존재 가능): 1개 (#14 IBM)
- 오류(404): 1개 (#18 Langfuse 메인 도메인)
- 주제 불일치: 0개

---

## 상세 결과

| # | URL | 상태 | 비고 | 대안 URL |
|---|-----|------|------|----------|
| 1 | https://openlineage.io/ | 정상 | OpenLineage 오픈 표준 — 데이터 리니지 수집·분석 프레임워크. Linux Foundation 소속. 주제 일치 | — |
| 2 | https://marquezproject.ai/ | 정상 | Marquez — OpenLineage 레퍼런스 구현, 메타데이터 서버+UI. 주제 일치 | — |
| 3 | https://datahub.com/ | 정상 | DataHub — 오픈소스 메타데이터 플랫폼, 리니지·거버넌스 포함. 주제 일치 | — |
| 4 | https://datahub.com/blog/column-level-lineage-comes-to-datahub/ | 정상 | 컬럼 레벨 리니지 DataHub 블로그 포스트(2026-05-20). 주제 일치 | — |
| 5 | https://atlas.apache.org/ | 정상 | Apache Atlas — Hadoop 생태계 메타데이터·거버넌스 프레임워크. 주제 일치 | — |
| 6 | https://docs.getdbt.com/docs/explore/column-level-lineage | 정상 | dbt 컬럼 레벨 리니지 공식 문서(2026-06-22 업데이트). Enterprise 플랜 기능. 주제 일치 | — |
| 7 | https://absaoss.github.io/spline/ | 정상 | Spline — Apache Spark 기반 오픈소스 데이터 리니지 추적 도구(AbsaOSS). 주제 일치 | — |
| 8 | https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage | 정상 | Databricks Unity Catalog 데이터 리니지 공식 문서(2026-06-09 업데이트). 주제 일치 | — |
| 9 | https://learn.microsoft.com/en-us/purview/ | 정상 | Microsoft Purview 공식 문서 허브 — 데이터 거버넌스·보안·컴플라이언스. 주제 일치 | — |
| 10 | https://docs.snowflake.com/en/user-guide/ui-snowsight-lineage | 정상 | Snowflake Snowsight 데이터 리니지 공식 문서. 컬럼 레벨 리니지 포함. Enterprise Edition 기능. 주제 일치 | — |
| 11 | https://docs.cloud.google.com/dataplex/docs/about-data-lineage | 정상 | Google Cloud Dataplex(Knowledge Catalog) 데이터 리니지 공식 문서(2026-06-23 업데이트). 주제 일치 | — |
| 12 | https://www.collibra.com/products/data-lineage | 정상 | Collibra 데이터 리니지 제품 페이지 — 40+ 소스 자동 추출, OpenLineage 통합. 주제 일치 | — |
| 13 | https://atlan.com/data-lineage/ | 정상 | Atlan 데이터 리니지 제품 페이지 — 80+ 시스템 컬럼 레벨 리니지. 주제 일치 | — |
| 14 | https://www.ibm.com/products/manta-data-lineage | **차단(403)** | IBM 서버가 봇 차단(403 Forbidden) 반환. 페이지 자체는 존재할 가능성 있음. 브라우저로 직접 접속 필요 | https://www.ibm.com/products/manta-automated-data-lineage (대안 검토 권장) |
| 15 | https://www.alation.com/product/data-lineage/ | 정상 | Alation 데이터 리니지 제품 페이지. 주제 일치 | — |
| 16 | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 정상 | EU 집행위원회 AI Act 규제 프레임워크 공식 페이지(2026-05-11 업데이트). 주제 일치(AI 거버넌스·리니지 규제 근거) | — |
| 17 | https://www.langchain.com/langsmith | 정상 | LangSmith 제품 페이지 — LLM 에이전트 추적·모니터링·관측가능성. 주제 일치(AI 파이프라인 리니지). **대시보드 실제 접속 URL은 `https://smith.langchain.com`** | https://smith.langchain.com (앱 URL) |
| 18 | https://langfuse.com/ | **오류(404)** | 메인 도메인에서 404 반환. 단, `/docs` 경로는 정상 접속됨 — Langfuse는 오픈소스 LLM 관측가능성 플랫폼으로 실제 서비스 중 | https://langfuse.com/docs (정상 확인) |
| 19 | https://atlan.com/know/data-lineage-impact-analysis/ | 정상 | Atlan 데이터 리니지 영향 분석 가이드(2025-12-11 업데이트). 주제 일치 | — |
| 20 | https://murdio.com/insights/data-lineage-metrics/ | 정상 | Murdio(데이터 거버넌스 컨설팅) 데이터 리니지 KPI/지표 아티클(2026-05-19). 주제 일치 | — |

---

## 조치 필요 사항

### #14 IBM MANTA (차단 — 존재 가능)
- `https://www.ibm.com/products/manta-data-lineage` → 403 Forbidden(봇 차단).
- IBM이 크롤러를 차단하는 경우가 많아 실제 페이지는 존재할 수 있음.
- 브라우저로 직접 확인 후, 접속 불가 시 아래 대안 검토:
  - `https://www.ibm.com/products/manta-automated-data-lineage`
  - `https://www.ibm.com/blog/ibm-acquires-manta/` (IBM의 MANTA 인수 발표)

### #18 Langfuse 메인 도메인 (404)
- `https://langfuse.com/` → 404 Not Found.
- `/docs` 페이지는 정상: `https://langfuse.com/docs`
- 가이드 본문 링크를 `https://langfuse.com/docs`로 교체 권장.

### #17 LangSmith URL 명확화
- `https://www.langchain.com/langsmith` → 제품 소개 페이지(마케팅). 정상.
- 실제 앱 대시보드는 `https://smith.langchain.com`.
- 가이드에서 "공식 소개 페이지"로 인용하는 경우 현 URL 유지 가능.
- 기술 문서를 참조해야 하면 `https://docs.smith.langchain.com` 사용 권장.

---

## 판정 기준
- **정상**: HTTP 200, 내용이 해당 솔루션·리니지 주제와 일치
- **차단(존재 가능)**: HTTP 403, 봇 차단으로 내용 미확인이나 서비스 중일 가능성 높음
- **오류(404)**: HTTP 404, 해당 경로에서 페이지 없음
