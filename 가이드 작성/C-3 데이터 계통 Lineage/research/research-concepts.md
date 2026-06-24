# C-3 데이터 계통(Data Lineage) — 개념·방법 정밀 리서치

> 작성일: 2026-06-24
> 목적: C-3 가이드 작성자용 원자료. 사실·출처 중심, 추측 표시 명기.

---

## 1. 데이터 계통(Data Lineage) 정의·구성

### 핵심 정의
- **데이터 계통**: 데이터가 원본 소스에서 최종 목적지까지 이동하는 경로를 추적하고, 각 단계에서의 변환·결합·필터링·집계 과정을 기록하는 체계.
- "데이터가 어떻게 시스템을 통해 이동하는지, 어디서 왔고, 어떻게 변했으며, 어디서 쓰이는지" 전 과정의 가시성을 제공한다.
- 출처: [Dagster — Data Lineage in 2025](https://dagster.io/learn/data-lineage), [Databricks](https://www.databricks.com/blog/what-is-data-lineage)

### 데이터 계통 vs 데이터 출처(Provenance)
| 구분 | 데이터 계통(Data Lineage) | 데이터 출처(Data Provenance) |
|------|--------------------------|------------------------------|
| 초점 | 시스템 간 데이터 **흐름과 변환** | 원점·소유권·**변경 이력** |
| 답하는 질문 | 데이터가 어떻게 이동했는가 | 누가 언제 왜 만들었/바꿨는가 |
| 주요 용도 | 파이프라인 디버깅, 영향 분석 | 감사 추적, 규정 준수 |
| 관계 | 상호 보완적 — 계통은 "흐름의 가시성", 출처는 "신뢰성 검증" |

- 현대 거버넌스는 두 개념을 통합하여 운영.
- 출처: [OvalEdge — Data Lineage vs Data Provenance](https://www.ovaledge.com/blog/data-lineage-vs-data-provenance)

### DAG(Directed Acyclic Graph) 표준 프레이밍
- 데이터 계통은 **방향 비순환 그래프(DAG)** 로 표현하는 것이 표준.
  - **노드(Node)**: 데이터 자산(테이블·파일·뷰·모델·RAG 인덱스·보고서 등)과 작업(Job/Task)
  - **엣지(Edge)**: 노드 간 데이터 흐름·변환 관계(방향 있음)
- ETL 파이프라인·SQL 변환·ML 피처 엔지니어링 등 모든 데이터 처리 과정을 이 그래프 위에 올린다.
- 출처: [Alation — What is Data Lineage?](https://www.alation.com/blog/what-is-data-lineage/), [Dagster](https://dagster.io/learn/data-lineage)

### W3C PROV 표준
- **W3C PROV**: 엔티티(Entity)·활동(Activity)·에이전트(Agent) 세 개 핵심 개념으로 출처 정보를 표현하는 도메인 무관 국제 표준(W3C Recommendation).
- 과학·의료·산업 등 전 분야에 적용 가능. OpenLineage 등 현대 도구들이 이 개념을 확장해 사용.
- 출처: 검색 결과(W3C PROV), [TrueScreen](https://truescreen.io/articles/data-provenance-definition-source-authenticity/)

### OpenLineage 표준
- **OpenLineage**: LF AI & Data Foundation 호스팅, 실행 중인 파이프라인에서 계통 메타데이터를 수집하는 **오픈 API 표준**.
- 핵심 모델: **RunEvent·Job·Dataset** — 세 엔티티를 일관된 식별 전략으로 정의.
- **Facet 시스템**: 핵심 엔티티에 부착하는 원자적 메타데이터 조각. 사용자 정의 확장 가능.
- Apache Airflow·Apache Spark·dbt·Snowflake·BigQuery 등 주요 데이터 도구와 통합.
  - Spark: 테이블·컬럼 수준 계통 지원
  - Airflow: 선택된 SQL 기반 오퍼레이터 지원
  - dbt: 테이블·컬럼 수준 계통 지원
  - Flink: 테이블 수준만 지원(미확인: 최신 버전 지원 여부)
- 2020년 이후 파이프라인 계통의 산업 표준으로 자리 잡음. IBM watsonx이 2026년 초 지원 확대 발표.
- 출처: [OpenLineage GitHub](https://github.com/OpenLineage/OpenLineage), [OpenLineage.io](https://openlineage.io/docs/integrations/spark/spark_column_lineage/)

---

## 2. 수집 방식 — 세 가지 방법

### ① 정적 파싱(Static Parsing)
- SQL 쿼리·저장 프로시저·ETL 스크립트·뷰 정의·애플리케이션 코드를 **파싱하여 계통 추출**.
- 가장 철저한 방법이지만, 레거시 코드 밀도가 높을수록 구현 난도 상승.
- 컬럼 레벨 계통 생성의 주요 수단 — SQL 파서가 쿼리 문자열에서 컬럼 의존성 추출.
- 출처: [DataHub — SQL Lineage Parser](https://datahub.com/blog/extracting-column-level-lineage-from-sql/), [7 Best Automated Data Lineage Tools](https://www.puppygraph.com/learn/automated-data-lineage-tools)

### ② 런타임 이벤트 캡처(Runtime Event Capture)
- 파이프라인이 **실제 실행될 때** 이벤트를 내보내 메타데이터 수집.
- OpenLineage 표준이 이 방식의 핵심 — 오케스트레이터·엔진이 실행 중 계통 이벤트 방출.
- 실제 실행된 경로만 반영하므로, 실행되지 않은 분기는 누락될 수 있음.
- 쿼리 로그·시스템 카탈로그 마이닝도 런타임 계통 복원의 방법.
- 출처: [OpenLineage Standard — apxml](https://apxml.com/courses/data-governance-quality-observability-production/chapter-4-data-lineage-metadata-management/openlineage-standard)

### ③ 수기 선언(Manual Declaration)
- 자동 수집이 불가한 비정형 프로세스·수작업 데이터 이동을 사람이 직접 선언.
- 정확도가 낮고 유지관리 부담이 크지만, 자동화 불가 영역의 공백 보완 역할.

### 현대 시스템의 조합 전략
- **정적 파싱 + 런타임 이벤트 캡처**를 결합해 통합 계통 그래프 구성.
- 정적 파싱으로 설계 의도를, 런타임으로 실제 실행을 보완.
- 출처: [Galaxy — Column-Level Lineage](https://www.getgalaxy.io/learn/glossary/column-level-lineage-open-source-tools-explained)

---

## 3. 입도(Granularity) — 세 수준

### 테이블 수준(Table-Level)
- 두 데이터셋이 연결되었음을 보여주는 가장 기본 수준.
- "A 테이블 → B 테이블"만 표시, 어떤 컬럼이 관여하는지 불명.
- 영향도 분석에서 정밀도 부족: 특정 컬럼 의존성을 놓칠 수 있음.

### 컬럼 수준(Column-Level)
- 개별 필드를 소스 컬럼에서 모든 변환을 거쳐 최종 목적지까지 추적.
- "어떤 3개 데이터 자산(대시보드 2개, ML 파이프라인 1개)이 이 필드에 의존하는가" 파악 가능.
- **규제 준수 감사**와 **정확한 영향도 예측**의 필수 조건.
- 영향도 분석 패러다임 전환: "배포하고 뭐가 깨지나 보기" → "배포 전에 뭐가 깨질지 알기".
- DataHub, Atlan, OpenMetadata 등 주요 도구들이 지원.
- 출처: [DataHub — Column-Level Lineage](https://datahub.com/blog/column-level-lineage-comes-to-datahub/), [OpenLineage Column Lineage](https://openlineage.io/docs/integrations/spark/spark_column_lineage/)

### 청크·근거 수준(Chunk/Citation-Level, AI 답변용)
- RAG 시스템에서 AI 답변이 참조한 **문서 청크·원본 위치·근거 데이터**를 기록하는 수준.
- 각 청크에 메타데이터 부착: 원본 문서명·섹션 제목·페이지 번호·부모 청크 ID.
- 이 메타데이터가 "AI 답변 → 원본 문서" 역추적의 출발점.
- 출처: [RAG Production Guide 2026](https://lushbinary.com/blog/rag-retrieval-augmented-generation-production-guide/), [Morphik RAG Strategies](https://www.morphik.ai/blog/retrieval-augmented-generation-strategies)

> **왜 컬럼 수준이 영향도 분석에 필요한가**: 테이블 수준은 "A가 B를 쓴다"는 것만 알려주나, 컬럼 수준은 "A의 revenue_usd 컬럼이 B의 net_sales × exchange_rate로 유도된다"를 알려준다. 스키마 변경 시 이 정밀도가 없으면 어떤 리포트·모델이 실제로 영향받는지 알 수 없다.

---

## 4. AI 답변 근거(Citation/Provenance) 추적

### RAG에서의 근거 추적 구조
- **전처리 단계에서의 provenance 기록**: 문서를 청크로 분할할 때 각 청크에 원본 위치 정보(파일명·경로·섹션·페이지 번호·생성 시각) 부착 → 이것이 AI 답변 근거 추적의 출발점.
- **검색(Retrieve) 단계**: 상위 K개 청크 반환 시 어떤 청크가 사용됐는지 기록.
- **생성(Generate) 단계**: 프롬프트에 포함된 청크·컨텍스트, LLM 호출, 최종 답변을 묶어 로그화 → "이 답변은 이 청크들을 근거로 생성됐다"는 구조 형성.

### LLM 관측 도구의 역할 (데이터 근거 기록 관점)
- **LangSmith** (LangChain): 프롬프트·검색된 컨텍스트·LLM 출력을 추적 로그로 저장. 근거 데이터를 "어떤 문서 어떤 청크에서 왔는가"와 연결.
- **Langfuse**: 오픈소스 LLMOps 플랫폼. 프롬프트 버전·사람 주석·사후 품질 평가를 OpenTelemetry 기반으로 관리.
- **OpenTelemetry GenAI**: 인프라 레벨 신호(입출력·레이턴시·토큰 수)를 벤더 무관하게 수집. Langfuse와 통합 가능.
- **Arize Phoenix**: 오픈소스 AI 관측 플랫폼. OpenTelemetry 기반, LlamaIndex·LangChain·Haystack·DSPy 지원.
- 이 도구들이 남기는 것: 입력(쿼리), 시스템 프롬프트, 검색된 컨텍스트(청크), LLM 출력, 신뢰도/레이턴시 등. 이 로그가 "AI 답변 → 근거 청크 → 원본 문서" 역추적 체인의 기술적 구현.
- 출처: [n1n.ai — LLM Observability Comparison 2026](https://explore.n1n.ai/blog/llm-observability-langfuse-langsmith-opentelemetry-2026-05-17), [Langfuse OpenTelemetry](https://langfuse.com/integrations/native/opentelemetry)

### 현재 한계(미확인)
- 구조적 추론 근거(structured reasoning provenance)를 네이티브 스키마 레벨에서 제공하는 도구는 아직 충분히 성숙하지 않음 — 기계적 실행 계층은 잘 추적되나, "왜 이 청크를 사용했는가"에 대한 추론 근거는 아직 도구 수준에서 공백.
- 출처: [arxiv 2503.06745](https://arxiv.org/pdf/2503.06745)

### AI 추적성(AI Traceability) 구성요소 (Snowflake 정의)
| 구성요소 | 설명 |
|---------|------|
| 데이터 계통(Data Lineage) | 특정 피처·컬럼을 원본 소스까지 변환 포함 역추적 |
| 모델 계통 | 모델 버전·학습 데이터·하이퍼파라미터·평가 결과 기록 |
| 프롬프트/응답 로그 | 사용자 입력·시스템 프롬프트·검색 컨텍스트·최종 출력 저장 |
| 접근 이력 | 누가 언제 어떤 데이터에 접근했는지 |
| AI-BOM | 모델·데이터·라이브러리·API 등 시스템 구성 목록 |
- 출처: [Snowflake — AI Traceability](https://www.snowflake.com/en/artificial-intelligence/ai-governance/ai-traceability/)

---

## 5. 영향도 분석(Impact Analysis)

### 개념
- **영향도 분석**: 데이터 워크플로우·시스템·자산의 변경이 조직 전체에 어떻게 파급되는지를 **사전에** 전략적으로 평가하는 것.
- Atlan 정의: "the strategic assessment of how a proposed change to a data workflow, system, or asset may propagate across the organization"
- 출처: [Atlan — Data Lineage Impact Analysis](https://atlan.com/know/data-lineage-impact-analysis/)

### 상류(Upstream) vs 하류(Downstream) 추적
- **상류 추적**: 데이터의 출처를 역방향으로 추적. "이 데이터는 어디서 왔고 어떻게 변환됐는가" — 근본 원인 분석(Root Cause Analysis)에 활용.
- **하류 추적**: 변경이 영향을 미칠 경로를 전방향으로 추적. "이것이 바뀌면 무엇이 깨지는가" — 영향도 분석에 활용.
- 예시: dbt 모델은 소스 테이블의 하류(downstream)이면서, 그것을 쿼리하는 Looker 대시보드의 상류(upstream).

### 컬럼 수준 영향도 분석의 필요성
- 테이블 수준: "A 테이블이 B 테이블에 영향을 준다"만 알 수 있음.
- 컬럼 수준: "A.revenue 컬럼 변경이 B.net_profit 컬럼, ML 파이프라인 X의 피처 Y에 영향을 준다"를 정확히 파악.
- 컬럼 이름 변경·타입 변경 전에 실제로 영향받는 자산의 목록을 신뢰할 수 있는 수준으로 확인 가능.

### 계층 구조 (Atlan 기준)
1. **테이블 수준**: 데이터셋 이동 추적
2. **컬럼 수준**: 개별 필드의 정밀 변환 추적
3. **비즈니스 수준**: KPI·메트릭과의 연결

---

## 6. 감사·규제 대응(Audit/Lineage Report)

### EU AI Act 요구사항 (2024~2026 시행)
- EU AI Act 발효: 2024년 8월 1일 시행, 2026년 8월 2일 완전 적용.
- **고위험 AI 시스템** 해당 시 계통 추적이 법적 의무 수준.
  - **Article 11** — 기술 문서화: 훈련 데이터 출처·수집 방법, 전처리 단계별 기록, 라벨링 절차.
  - **Article 12** — 자동 로깅: 모든 추론 기록(입력·출력·신뢰도 점수), 최소 6개월 보관.
  - **Article 13** — 투명성: 신뢰도 점수 공개, 시스템 한계 공시.
- 위반 시 최대 €35,000,000 또는 글로벌 연간 매출 7%.
- 출처: [EU AI Act Medium](https://medium.com/@pulsr-io-enrico/gdpr-taught-us-data-governance-the-ai-act-demands-data-lineage-heres-the-difference-eb3c3466f324), [Atlan — Regulatory Lineage](https://atlan.com/regulatory-data-lineage-tracking/)

### GDPR vs AI Act 차이
- GDPR: "어디에 데이터가 있고 누가 접근하는가" 추적
- AI Act: "AI 시스템이 어떻게 결정을 내렸는가"를 증명해야 함 — 더 심층적 계통 요구

### 주요 규제별 계통 요구사항 요약
| 규제 | 주요 요구 |
|------|----------|
| EU AI Act | 데이터 수집·변환·혼합·수정의 광범위한 로깅 및 감사 기록 |
| BCBS 239 | 데이터 흐름 상세 파악, 데이터 품질 유지, 보고 정확성 및 재현성 입증 |
| GDPR/CCPA | 지리적 데이터 프라이버시 규제 준수 (PII 데이터 흐름 감시) |

### 감사 리포트 구성 요소
- 데이터 출처에서 목적지까지의 이동 기록(감사 로그)
- 보고서·데이터 자산의 재현성 보장 상세 맥락 로깅
- 특정 시점의 접근 제어 정책 기록
- 시간 경과에 따른 데이터 품질 평가 기록
- 컬럼·필드 수준의 세밀한 계통 추적 기록

### 감사 대응 절차
1. 중요 데이터 자산 카탈로그화
2. 메타데이터 수집 자동화
3. 핵심 규제 프로세스 매핑
4. 동적 계통 시각화 도구 도입
5. 시간 경과에 따른 계통 변경 추적

---

## 7. 성과 지표(KPI)

| 지표명 | 정의 | 측정 방법 | 목표 방향 | 비고 |
|--------|------|---------|---------|------|
| **CDE 커버리지** | 문서화된 계통을 보유한 중요 데이터 요소(CDE) 비율 | 검증된 CDE / 전체 식별 CDE × 100 | ↑ (100% 목표) | 계통 범위의 핵심 지표 |
| **계통 정확도** | 실제 물리적 데이터 흐름과 일치하는 매핑 경로 비율 | 검증된 경로 수 / 전체 매핑 경로 × 100 | ↑ (95% 이상 목표) | 미확인: 벤더별 측정 기준 상이 |
| **계통 노후화율** | 현재 프로덕션 파이프라인과 불일치하는 계통 기록 비율 | 미갱신 기록 / 전체 기록 × 100 | ↓ (낮을수록 좋음) | 계통 신뢰성 지표 |
| **감사 대응 시간** | 규제 문의 접수에서 증빙 제출까지 소요 시간 | 문의 접수 시점 → 계통 리포트 제출 시점 | ↓ (수 시간 이내 목표) | 감사 효율 지표 |
| **자동화 비율** | 자동으로 추출된 메타데이터 비율 | 자동 추출 / 전체 추출 × 100 | ↑ (90% 이상 목표) | 운영 효율 지표 |
| **경로 완성도** | 중단 없이 완성된 데이터 흐름 경로 비율 | 완성 경로 / 전체 매핑 경로 × 100 | ↑ (95% 이상 목표) | 계통 완전성 지표 |

- 출처: [murdio — Data Lineage Metrics 2026](https://murdio.com/insights/data-lineage-metrics/), [kpidepot — Data Lineage Accuracy](https://kpidepot.com/kpi/data-lineage-accuracy)

---

## 8. 제조업 맥락 — Pain Point와 효과 (예시 재료)

> 아래는 두산 계열사 맥락 기반 **가상 예시**다. 구체 수치·계열사명은 가이드 작성 시 가상임을 명기할 것.

### Pain Point (계통 미비 시)
- **신뢰 불가 문제**: AI 점검 리포트가 "어떤 센서 데이터·성적서·설계 문서를 근거로 이 결론을 냈는지" 역추적 불가 → 현장 엔지니어가 AI 결과를 수용하지 않음.
- **변경 충격 예측 불가**: 원천 테이블(예: 생산 이력 DB) 스키마 변경 시, 어떤 품질 분석 모델·리포트·RAG 인덱스가 영향받는지 알 수 없어 변경 후 장애 발생.
- **감사 대응 불능**: 내부 품질 감사에서 "이 불량 판정 AI의 학습 데이터 출처는 무엇인가"를 물을 때 즉각 답변 불가.
- **데이터 팀 간 단절**: QA팀·생산팀·IT팀이 동일 데이터의 출처와 변환 이력을 각기 다르게 이해.

### 효과 (계통 구축 후)
| Before | After |
|--------|-------|
| AI 점검 리포트 근거 불명 | 답변 생성에 참조된 센서 로그·공정 기준서·이전 판정 이력을 클릭 한 번에 확인 |
| 원천 변경 시 장애 발생 후 대응 | 변경 전 영향받는 자산 목록 확인 → 사전 조율 |
| 감사 시 수일 걸려 증빙 수집 | 계통 리포트 자동 생성, 당일 제출 가능 |
| 불량 원인 추적 수작업 | 불량 데이터 → 전처리 단계 → 원천 로그까지 역추적 자동화 |

- 참고 출처: [acodis — Traceability Crucial for AI Success](https://www.acodis.io/blog/from-data-to-insight-why-traceability-is-crucial-for-ai-success), [Encord — Data Visibility Traceability](https://encord.com/blog/data-visibility-traceability/)

---

## 9. 주요 도구·솔루션 스냅샷

| 도구 | 유형 | 특징 |
|------|------|------|
| DataHub | 오픈소스 | 컬럼 레벨 SQL 파싱 계통, 커뮤니티 활발 |
| OpenMetadata | 오픈소스 | 계통·품질·프로파일링·거버넌스 통합. ML 태그 추천·관계 추론 |
| Apache Atlas | 오픈소스 | Hadoop·Hive·Spark 중심 빅데이터 환경 |
| Atlan | SaaS | G2 9.1/10 계통 점수. 컬럼 레벨 dbt·Snowflake·BigQuery·BI 자동 추적. 4~6주 배포 |
| Collibra | Enterprise | 비즈니스 Glossary·정책 관리 강점. 2025.6 OpenLineage 통합 추가. 3~9개월 배포 |
| Alation | Enterprise | 비즈니스 친화적 시각화. 크로스 시스템 계통은 Manta 애드온 필요 |
| LangSmith | LLMOps | RAG 파이프라인 근거 추적·디버깅 전문 |
| Langfuse | LLMOps (오픈소스) | OpenTelemetry 기반, 프롬프트 버전·사람 주석 관리 |
- 출처: [5x.co — Top 10 Data Lineage Tools 2026](https://www.5x.co/blogs/data-lineage-tools), [Atlan — Alation vs Collibra vs OpenMetadata vs Atlan](https://atlan.com/alation-vs-collibra-vs-openmetadata-vs-atlan/)

---

## 10. 미확인·추가 조사 필요 항목

- OpenLineage의 Flink 최신 버전 컬럼 레벨 지원 여부(현재 "테이블 수준만" 기록됨, 2025~2026 업데이트 반영 여부 미확인)
- RAG Citation을 데이터 계통 그래프에 통합하는 구체 구현 사례(벤더 솔루션 레벨에서 성숙한 제품 아직 없음)
- 가격·라이선스 정보는 단정 금지(SaaS 도구들 가격 변동 잦음)

---

## 참고 출처 목록

1. [Dagster — Data Lineage in 2025](https://dagster.io/learn/data-lineage)
2. [OvalEdge — Data Lineage vs Data Provenance](https://www.ovaledge.com/blog/data-lineage-vs-data-provenance)
3. [OpenLineage GitHub](https://github.com/OpenLineage/OpenLineage)
4. [OpenLineage — Spark Column Lineage](https://openlineage.io/docs/integrations/spark/spark_column_lineage/)
5. [DataHub — Column-Level Lineage](https://datahub.com/blog/column-level-lineage-comes-to-datahub/)
6. [DataHub — SQL Lineage Parser](https://datahub.com/blog/extracting-column-level-lineage-from-sql/)
7. [Atlan — Impact Analysis](https://atlan.com/know/data-lineage-impact-analysis/)
8. [Atlan — Regulatory Lineage](https://atlan.com/regulatory-data-lineage-tracking/)
9. [EU AI Act — Medium (Enrico)](https://medium.com/@pulsr-io-enrico/gdpr-taught-us-data-governance-the-ai-act-demands-data-lineage-heres-the-difference-eb3c3466f324)
10. [EU AI Act — Digital Strategy EC](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
11. [Snowflake — AI Traceability](https://www.snowflake.com/en/artificial-intelligence/ai-governance/ai-traceability/)
12. [murdio — Data Lineage Metrics 2026](https://murdio.com/insights/data-lineage-metrics/)
13. [KPI Depot — Data Lineage Accuracy](https://kpidepot.com/kpi/data-lineage-accuracy)
14. [acodis — Traceability Crucial for AI](https://www.acodis.io/blog/from-data-to-insight-why-traceability-is-crucial-for-ai-success)
15. [Langfuse OpenTelemetry](https://langfuse.com/integrations/native/opentelemetry)
16. [n1n.ai — LLM Observability 2026](https://explore.n1n.ai/blog/llm-observability-langfuse-langsmith-opentelemetry-2026-05-17)
17. [Morphik — RAG Strategies 2025](https://www.morphik.ai/blog/retrieval-augmented-generation-strategies)
18. [Alation — What is Data Lineage?](https://www.alation.com/blog/what-is-data-lineage/)
19. [5x.co — Top 10 Data Lineage Tools 2026](https://www.5x.co/blogs/data-lineage-tools)
20. [Atlan — Tool Comparison](https://atlan.com/alation-vs-collibra-vs-openmetadata-vs-atlan/)
