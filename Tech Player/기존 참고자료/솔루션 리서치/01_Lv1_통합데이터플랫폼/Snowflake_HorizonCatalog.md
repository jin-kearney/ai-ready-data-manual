# Snowflake — Horizon Catalog

> 작성일: 2026-06-10 | 조사 기준: 2025~2026년 최신 릴리스 (Snowflake Summit 2026 포함)

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Snowflake Inc. (미국, 보즈먼) |
| 라이선스 | 상용 (Apache Polaris는 OSS) |
| 배포 형태 | SaaS — AWS / Azure / GCP (40+ 리전) |
| 최신 주요 릴리스 | Snowflake Summit 2026 (2026-06): Horizon Context, Semantic Studio, Iceberg V3 지원 |
| AI 브랜드 변경 | Snowflake Intelligence → CoWork / Cortex Code → CoCo (2026 리브랜딩) |

---

## 한 줄 포지셔닝

**SQL 친화적 클라우드 DW를 기반으로 거버넌스·AI·데이터 공유를 내장한 엔터프라이즈 데이터 클라우드.**

---

## 주요 기능

### 1. Snowflake Horizon Catalog — 통합 거버넌스·컨텍스트 레이어
- **Apache Polaris 기반**: 오픈소스 Iceberg REST Catalog를 기반으로 모든 Iceberg 엔진과 상호운용
- **Horizon Context (2026 신기능)**: AI·BI 도구에 "하나의 정답"을 제공하는 컨텍스트 레이어. 비즈니스 정의·SQL 로직·거버넌스 정책을 통합
- **Semantic Studio**: SQL 전문 지식 없이 공유 비즈니스 로직 정의 (Semantic View Autopilot: 자동 세만틱 뷰 생성)
- **Cortex Sense**: 자연어 프롬프트에 관련 컨텍스트를 자동 주입하여 AI 답변 정확도 3~4배 향상

### 2. 데이터 카탈로그 & 메타데이터
- **통합 카탈로그**: Snowflake 내부 데이터 + 외부 Iceberg 테이블 일원화
- **자동 메타데이터 수집**: 테이블·컬럼·태그·사용 이력 자동 캡처
- **태그 기반 분류**: 시스템 정의 태그 + 커스텀 태그, 민감정보 자동 분류
- **카탈로그 연동 DB (Catalog-Linked Databases)**: Iceberg REST Catalog 동기화로 외부 엔진이 관리하는 테이블 거버넌스

### 3. 데이터 리니지
- **컬럼 레벨 리니지**: ACCESS_HISTORY 뷰로 모든 컬럼 읽기·쓰기 이력 추적
- **객체 의존성 추적**: 뷰→테이블, 저장 프로시저→테이블 의존관계 시각화
- **OpenLineage 수집**: 외부 데이터 파이프라인 리니지 통합

### 4. 데이터 품질
- **내장 DQ 함수**: Data Metric Functions (DMF) — 빌트인 + 커스텀 정의 가능
- **신선도·완전성 모니터링**: 스케줄 기반 품질 체크 자동화
- **AI 쿼리 시 신선도 보장**: 쿼리가 항상 최신 데이터에 접근하는지 자동 검증

### 5. 접근 제어 & 보안
- **RBAC 계층형**: 계정→데이터베이스→스키마→테이블→행·열 수준 세분화
- **동적 데이터 마스킹**: 역할 기반 마스킹 정책 (컬럼 레벨)
- **행 수준 보안**: Row Access Policies로 사용자별 데이터 범위 제한
- **AI Agent Identity (GA)**: 에이전트별 암호화 ID, per-agent RBAC, 완전한 감사 추적

### 6. AI 기능 (2025~2026)
- **Snowflake CoWork (구 Intelligence)**: 비즈니스 사용자용 개인 AI 에이전트 — 업무 패턴 학습, 태스크 자동화
- **CoCo (구 Cortex Code)**: AI 코드 어시스턴트, 외부 Databricks·AWS Glue·Postgres 지원 확대
- **Cortex AI_COMPLETE**: Gemini 3.5 Flash 지원, 멀티모달 비디오·오디오 분석
- **커스텀 모델 학습 (Summit 2026)**: Snowflake 내에서 도메인 특화 모델 파인튜닝

### 7. Data Sharing & Marketplace
- **Snowflake Marketplace**: 3rd party 데이터 제품 구매·판매, 자체 데이터 상품화
- **Delta Sharing 호환**: 외부 조직에 데이터 공유 (계열사 간 데이터 유통에 활용 가능)
- **Private Data Exchange**: 기업 내부 데이터 교환 플랫폼 구축

---

## AI-Ready Data 주제 매핑

| 주제코드 | 주제명 | 커버 수준 | 비고 |
|---------|--------|-----------|------|
| A-1 | 데이터 카탈로그 | ○ 완전 | Horizon Catalog, 외부 Iceberg 통합 |
| A-2 | 메타데이터 관리 | ○ 완전 | 태그·분류 자동화 |
| A-3 | 데이터 리니지 | ○ 완전 | 컬럼 레벨, ACCESS_HISTORY |
| C-3 | Business Glossary | △ 부분 | Semantic Studio로 보완 중, 전용 Glossary는 미흡 |
| E-1 | 데이터 품질 | ○ 완전 | Data Metric Functions |
| C-1 | 접근 제어 | ○ 완전 | RBAC + 동적 마스킹 + 행 수준 보안 |
| C-2 | 데이터 분류 | ○ 완전 | 자동 태그 분류, Horizon Context |
| F-1 | DataOps | △ 부분 | Snowpark, Tasks·Streams으로 파이프라인 지원 |
| F-2 | 데이터 생애주기 | ○ 완전 | Time Travel (90일), Fail-Safe, 클론 |

---

## 강점

1. **관리 오버헤드 최소**: 완전 관리형 SaaS, 인프라 운영 부담 없음
2. **Data Sharing 생태계**: 계열사 간 데이터 공유·Data Marketplace 활용 탁월
3. **AI 컨텍스트 레이어**: Horizon Context + Cortex Sense로 AI 정확도 대폭 향상
4. **Iceberg 상호운용**: Apache Polaris 기반으로 외부 엔진(Databricks, Spark 등)과 개방적 연동
5. **SQL 친화적**: 기존 DW 조직의 낮은 학습 곡선

---

## 약점·주의점

1. **클라우드 락인**: 완전 SaaS 전용, 온프레미스·하이브리드 불가
2. **Business Glossary 약점**: 전용 Glossary 기능이 Collibra·Alation 수준에 미치지 못함 (Semantic Studio가 보완 중)
3. **비용 증가**: 쿼리 볼륨 증가 시 크레딧 소진 급증 — 거버넌스 파이프라인 설계 필요
4. **스트리밍 처리 한계**: Spark 기반 실시간 처리는 Databricks 대비 약함
5. **ML/AI 모델 학습**: Spark ML·PyTorch 수준의 고급 ML 환경은 Databricks 대비 제한적

---

## 가격 모델

- **크레딧 소비 기반**: 컴퓨팅(Virtual Warehouse), 저장소, 서버리스 태스크 별도 과금
- **에디션**: Standard / Enterprise / Business Critical / Virtual Private Snowflake
- **Enterprise 이상**에서 대부분의 거버넌스·보안 기능 활성화 (Dynamic Data Masking, Time Travel 90일 등)
- Horizon Catalog 기능 자체는 Enterprise+ 구독에 포함
- 참고: https://www.snowflake.com/pricing/

---

## 연동 생태계

- **커넥터**: 200+ 파트너 (Fivetran, Airbyte, dbt, Matillion, Talend 등)
- **BI**: Tableau, Power BI, Looker, ThoughtSpot, Sigma
- **AI/ML**: Dataiku, DataRobot, SageMaker, Azure ML, Vertex AI (Snowpark ML)
- **오픈 표준**: Apache Iceberg (Polaris), Apache Parquet, Delta Lake (읽기)
- **API**: REST API, JDBC/ODBC, Python SDK (Snowpark)
- **MCP**: Atlan MCP를 통한 Snowflake 메타데이터 연동; 자체 MCP 서버 개발 중
- **외부 엔진 쓰기 (GA)**: Databricks, Apache Spark 등 외부 엔진에서 Snowflake Iceberg 테이블 읽기/쓰기

---

## 출처

- https://www.snowflake.com/en/news/press-releases/snowflake-advances-trusted-ai-with-snowflake-horizon-catalog-centralizing-governance-context-and-security-across-the-enterprise/
- https://www.constellationr.com/insights/news/snowflake-summit-2026-context-custom-model-training-iceberg-v3
- https://www.snowflake.com/en/news/press-releases/snowflake-expands-snowflake-intelligence-and-cortex-code-to-power-the-control-plane-for-the-agentic-enterprise/
- https://docs.snowflake.com/en/user-guide/snowflake-horizon
- https://atlan.com/know/snowflake/summit-2026-announcements/
- https://www.businesswire.com/news/home/20260602887292/en/Snowflake-Advances-Trusted-AI-with-Snowflake-Horizon-Catalog-Centralizing-Governance-Context-and-Security-Across-the-Enterprise
