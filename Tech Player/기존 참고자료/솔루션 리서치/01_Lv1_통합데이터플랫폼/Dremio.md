# Dremio — Agentic Lakehouse Platform

> 작성일: 2026-06-10 | 조사 기준: 2025~2026년 최신 릴리스 (Dremio Cloud 런칭 2025-11 포함)

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Dremio Corporation (미국, 산타클라라) |
| 라이선스 | 상용 (오픈소스 Community Edition 제공; Apache Arrow, Apache Iceberg 기여) |
| 배포 형태 | SaaS (Dremio Cloud) + 자체 호스팅 (Software Edition) |
| 최신 주요 릴리스 | 2025-04: Iceberg Clustering·Autonomous Reflections·AI Semantic Search; 2025-11: Dremio Cloud (Agentic Lakehouse) 런칭 |
| Gartner | Gartner Peer Insights Dremio Agentic Lakehouse Platform 2026 등재 |

---

## 한 줄 포지셔닝

**Apache Iceberg 기반 오픈 아키텍처에서 AI 에이전트가 자율적으로 최적화·발견·쿼리하는 에이전틱 레이크하우스 — 멀티소스 쿼리 가상화의 선도주자.**

---

## 주요 기능

### 1. Dremio Cloud — 에이전틱 레이크하우스 (2025-11 런칭)
- **자율 학습·적응**: AI가 쿼리 패턴·데이터 관계·사용 트렌드를 지속 학습하여 자율 최적화
- **Living Intelligence Layer**: 능동 메타데이터 시스템이 사용자 필요를 예측하고 선제적 조치 수행
- **데이터 엔지니어 부담 절감**: 데이터 발견, 파이프라인 구축, 성능 튜닝 작업을 AI가 자동화

### 2. Enterprise Catalog — 통합 오픈 카탈로그
- **멀티소스 자산 통합 거버넌스**: 레이크하우스·RDBMS·클라우드 데이터베이스 전반의 데이터 자산을 단일 카탈로그로 관리
- **AI 기반 시맨틱 검색 (2025 신기능)**: 키워드가 아닌 의미 기반 검색 — 유사 개념 자산 자동 추천
- **MCP (Model Context Protocol) 지원**: AI 에이전트가 다양한 데이터 소스에 접근하는 표준 프레임워크 — 내장 지원
- **시맨틱 레이어**: 비즈니스 컨텍스트를 메타데이터로 정의, AI 에이전트가 쿼리 시 활용
- **Wiki·설명 자동 생성**: AI 보조로 데이터 자산 문서 자동화

### 3. Autonomous Reflections (2025 신기능, 업계 최초)
- **자동 성능 최적화**: 쿼리 패턴 분석 → 최적 materialized view(Reflection) 자동 생성·갱신
- **항상 최신 데이터**: 캐시가 아닌 라이브 데이터 기반, SQL 변경 불필요
- **서브 초 단위 쿼리**: 수동 튜닝 없이 즉시 빠른 응답 제공

### 4. Iceberg Clustering (2025 신기능, 업계 최초)
- **Apache Iceberg용 자동 데이터 클러스터링**: 파티셔닝 없이 데이터 레이아웃 자동 최적화
- **쿼리 속도 대폭 향상**: 수동 파티션 관리 제거, 드라마틱한 쿼리 성능 개선
- **Iceberg 기반 레이크하우스의 데이터 관리 단순화**

### 5. 쿼리 가상화·페더레이션
- **멀티소스 단일 쿼리**: S3, ADLS, GCS, RDBMS(PostgreSQL, MySQL, SQL Server), NoSQL, Kafka를 단일 SQL로 조회
- **데이터 이동 없음**: 데이터를 복사하지 않고 소스에서 직접 쿼리 (Data Virtualization)
- **Apache Arrow 최적화**: 인메모리 벡터화 처리로 고속 쿼리 엔진

### 6. 접근 제어
- **역할 기반 접근 제어(RBAC)**: 카탈로그·스페이스·폴더·테이블 수준 권한 관리
- **열 마스킹**: 민감 컬럼에 대한 역할 기반 마스킹
- **감사 로그**: 모든 쿼리·접근 이력 기록

### 7. DataOps & 생애주기
- **Iceberg Time Travel**: 테이블 스냅샷 기반 과거 데이터 조회
- **테이블 최적화 자동화**: Compaction, Expire Snapshots, Remove Orphan Files 자동 실행
- **Git 통합**: 데이터 소스·쿼리 설정 버전 관리

---

## AI-Ready Data 주제 매핑

| 주제코드 | 주제명 | 커버 수준 | 비고 |
|---------|--------|-----------|------|
| A-1 | 데이터 카탈로그 | ○ 완전 | Enterprise Catalog, 시맨틱 검색 |
| A-2 | 메타데이터 관리 | ○ 완전 | Active Metadata, AI 자동 문서화 |
| A-3 | 데이터 리니지 | △ 부분 | 테이블 레벨 리니지, 컬럼 레벨 일부 지원 |
| C-3 | Business Glossary | △ 부분 | 시맨틱 레이어 있음, 전용 Glossary 관리는 제한적 |
| E-1 | 데이터 품질 | △ 부분 | 프로파일링·기본 DQ, 전용 DQ 엔진 대비 미흡 |
| C-1 | 접근 제어 | ○ 완전 | RBAC + 열 마스킹 |
| C-2 | 데이터 분류 | △ 부분 | 수동 태깅 중심, 자동 분류 미흡 |
| F-1 | DataOps | △ 부분 | Iceberg 관리 자동화 강함, 파이프라인 오케스트레이션은 외부 의존 |
| F-2 | 데이터 생애주기 | ○ 완전 | Iceberg Time Travel, Snapshot 관리 |

---

## 강점

1. **에이전틱 자동화 선도**: Autonomous Reflections·AI Semantic Search·MCP 지원으로 에이전트 AI 시대 선도
2. **Apache Iceberg 생태계 선두**: Iceberg Clustering·REST Catalog 기여로 Iceberg 관련 기능이 업계 최고 수준
3. **쿼리 가상화**: 데이터 이동 없는 멀티소스 페더레이션 쿼리 — 마이그레이션 부담 없는 즉시 분석 가능
4. **MCP 네이티브 지원**: AI 에이전트가 데이터 소스에 직접 접근하는 표준 프로토콜 내장
5. **오픈 아키텍처**: Apache Arrow, Apache Iceberg, Apache Polaris 생태계와 개방적 연동

---

## 약점·주의점

1. **데이터 거버넌스 성숙도**: Databricks·Snowflake 대비 ABAC, 자동 분류, Business Glossary 기능 미흡
2. **단독 저장소 없음**: 자체 저장 레이어 없이 S3·ADLS·GCS에 의존 — 저장 전략 별도 수립 필요
3. **인지도**: 대기업 조직 내 Databricks·Snowflake 대비 낮은 인지도로 조달 설득 필요
4. **ML/AI 플랫폼**: MLflow·CML 수준의 내장 ML 환경 없음 — 외부 ML 플랫폼 연동 필요
5. **완전 관리형 SaaS**: 2025년 이후 자체 호스팅 기능은 유지하나 주력이 SaaS로 이동 중

---

## 가격 모델

- **Dremio Cloud (SaaS)**: 소비 기반 (쿼리 실행 시간·컴퓨팅 리소스 기준)
- **Software Edition (자체 호스팅)**: Enterprise 구독 라이선스 (연간 계약, 노드/코어 기준)
- **Community Edition**: 소규모 무료 자체 호스팅 (프로덕션 지원 없음)
- 공개 가격 없음, 영업 채널 통해 견적 — 일반적으로 $50K~$300K+/년 수준
- 참고: https://www.dremio.com/get-started/

---

## 연동 생태계

- **데이터 소스**: 30+ 커넥터 (S3, ADLS, GCS, PostgreSQL, MySQL, MongoDB, Elasticsearch, Kafka, Hive 등)
- **BI**: Tableau, Power BI, Looker, Metabase (SQL 엔드포인트 경유)
- **오픈 표준**: Apache Arrow, Apache Iceberg, Apache Parquet, Apache Polaris
- **AI/ML**: LangChain·LlamaIndex 통합(MCP 경유), Hugging Face 모델 서빙
- **API**: REST API, JDBC/ODBC, Arrow Flight
- **MCP**: 네이티브 MCP 서버 지원 — Claude, Cursor, 내부 에이전트 프레임워크와 직접 연결
- **Iceberg Federation**: AWS Glue, Databricks Unity Catalog, Snowflake Horizon과 카탈로그 연동

---

## 출처

- https://www.dremio.com/blog/introducing-dremio-cloud-the-agentic-lakehouse/
- https://siliconangle.com/2025/11/10/dremio-cloud-debuts-agentic-data-lakehouse-operated-ai-agents/
- https://www.globenewswire.com/news-release/2025/04/08/3057627/0/en/Dremio-Advances-Lakehouse-Intelligence-Reinvents-the-Data-Warehouse-for-the-AI-Era.html
- https://www.hpcwire.com/bigdatawire/this-just-in/dremio-enhances-iceberg-based-lakehouse-with-new-semantic-search-and-clustering/
- https://www.techtarget.com/searchdatamanagement/news/366634167/Dremio-Cloud-An-autonomous-lakehouse-powered-by-AI-agents
- https://www.dremio.com/blog/how-dremios-agentic-lakehouse-is-turning-data-into-action/
