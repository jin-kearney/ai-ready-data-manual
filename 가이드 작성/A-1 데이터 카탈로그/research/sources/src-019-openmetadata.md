# src-019 — OpenMetadata

- **URL**: https://open-metadata.org/
- **제목**: OpenMetadata — The #1 Open Source Context Layer for AI
- **접속일**: 2026-06-18

---

## 주요 내용 (WebFetch 수집)

### 정체성
"AI·데이터 카탈로그·메타데이터 관리를 위한 #1 오픈소스 컨텍스트 레이어"
- 창립: Apache Hadoop·Atlas·Uber Databook 팀 출신
- 규모: 4,000개 이상 엔터프라이즈 배포, 13,500명 이상 커뮤니티, 450명 이상 코드 기여자

### 커넥터 (130개 이상)

| 카테고리 | 예시 |
|---------|------|
| 데이터베이스 | Snowflake, BigQuery, PostgreSQL, MySQL, Oracle |
| 데이터 레이크 | AWS S3, Azure Data Lake, Google Cloud Storage |
| 파이프라인 | Airflow, Dagster, dbt, Fivetran |
| 대시보드 | Tableau, Looker, Power BI, Metabase |
| ML | MLflow, SageMaker |
| 메시징 | Kafka, Kinesis, Google Pub/Sub |
| 검색/API | Elasticsearch, OpenSearch |

### 메타데이터 표준
- W3C 표준: RDF, OWL, DCAT, Schema.org 기반 관계 정의
- 용어집·메트릭 정의·분류·온톨로지 지원
- 감사 추적: 인간·AI 모든 변경 기록

### 주요 기능 (2025년 기준)
- OpenMetadata 1.8 (2025년 6월): 데이터 계약(Data Contract) 도입 — 머신 판독 스키마·SLA·품질 보증 자동 시행
- 네이티브 MCP 서버: AI 에이전트가 메타데이터 직접 접근
- AI SDK: 외부 에이전트 프로그래매틱 접근

### 아키텍처 (DataHub 대비 단순)
- MySQL/PostgreSQL (메타데이터 저장)
- Elasticsearch (검색)
- 그래프 DB 없음 → 운영 복잡도 낮음
