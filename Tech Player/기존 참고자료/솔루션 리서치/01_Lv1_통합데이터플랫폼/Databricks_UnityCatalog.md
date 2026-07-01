# Databricks — Unity Catalog

> 작성일: 2026-06-10 | 조사 기준: 2025~2026년 최신 릴리스

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Databricks, Inc. (미국, 샌프란시스코) |
| 라이선스 | 상용 (일부 핵심 기술은 OSS: Delta Lake, MLflow, Apache Spark) |
| 배포 형태 | SaaS — AWS / Azure / GCP 멀티클라우드 |
| 최신 주요 릴리스 | 2025 Data + AI Summit: Unity Catalog 대규모 업데이트; 2026: PostgreSQL 거버넌스 통합 |
| IDC 평가 | IDC MarketScape Worldwide Unified AI Governance Platforms 2025–2026 Leader 선정 |

---

## 한 줄 포지셔닝

**데이터·AI 워크로드를 단일 거버넌스 플레인 위에 통합하는, AI 네이티브 통합 데이터 플랫폼의 사실상 표준.**

---

## 주요 기능

### 1. Unity Catalog — 통합 거버넌스 레이어
- **3레벨 네임스페이스**: `카탈로그 > 스키마 > 테이블/볼륨/모델` 계층으로 모든 데이터·AI 자산 단일 관리
- **ABAC (Attribute-Based Access Control)**: 2025년 GA. 태그 기반 동적 접근 정책으로 수천 개 테이블에 단일 정책 적용 가능
- **행·열 수준 보안**: 동적 뷰 또는 Row/Column Filter로 세분화된 접근 제어
- **자동 데이터 분류**: AI 기반 민감정보 자동 태깅(PII, 재무 데이터 등), GDPR/CCPA 규정 준수 지원

### 2. 데이터 카탈로그 & 메타데이터
- **AI 자동 문서화**: LLM을 활용한 테이블·컬럼 설명 자동 생성
- **Unity Catalog Metrics**: 공인 비즈니스 지표(Certified Metrics)를 데이터 자산으로 관리, 감사 이력·리니지 내장
- **Data Marketplace (내부)**: 도메인별로 고가치 데이터·AI 자산을 큐레이션하여 조직 내 공유 촉진
- **Iceberg Federation (Public Preview)**: AWS Glue, Hive Metastore, Snowflake Horizon의 Iceberg 테이블을 복사 없이 쿼리·거버넌스

### 3. 데이터 리니지
- **컬럼 레벨 자동 리니지**: Spark·SQL 쿼리 실행 시 자동 캡처, 모든 워크스페이스에서 집계
- **AI 리니지**: ML 모델 학습에 사용된 데이터셋 추적, AI 감사 간소화
- **OpenLineage 호환**: 외부 파이프라인 리니지 수집 지원

### 4. 데이터 품질
- **자동 DQ 모니터링**: 스키마 전체에 대한 신선도·완전성 자동 체크
- **데이터 헬스 인디케이터**: 소비자가 한눈에 데이터 품질 상태 파악
- **Delta Live Tables**: 선언형 파이프라인에 품질 기대치(Expectations) 내장

### 5. AI 거버넌스 (2025~2026 신기능)
- **AI Agent 거버넌스**: AI 에이전트·모델 카탈로그 등록, 계보 추적, 접근 정책 적용
- **Volumes**: 이미지·영상·PDF 등 비정형 데이터를 Unity Catalog로 거버넌스
- **Databricks Genie**: 자연어로 데이터 질의 (Text-to-SQL), 비즈니스 사용자 셀프서비스 분석

### 6. DataOps & 생애주기
- **Delta Lake Time Travel**: 쿼리 시점 데이터 복원, 기본 7~30일
- **OPTIMIZE/ZORDER/Auto-Compaction**: 테이블 자동 최적화
- **Databricks Asset Bundles (DAB)**: 파이프라인·잡의 CI/CD 코드형 배포
- **PostgreSQL 거버넌스 (2026 신기능)**: 운영 DB 데이터를 Unity Catalog 거버넌스 우산 아래 편입

---

## AI-Ready Data 주제 매핑

| 주제코드 | 주제명 | 커버 수준 | 비고 |
|---------|--------|-----------|------|
| A-1 | 데이터 카탈로그 | ○ 완전 | Unity Catalog, AI 자동 문서화 |
| A-2 | 메타데이터 관리 | ○ 완전 | 태그·분류 자동화 |
| A-3 | 데이터 리니지 | ○ 완전 | 컬럼 레벨, AI 리니지 |
| C-3 | Business Glossary | ○ 완전 | Certified Metrics, Semantic Layer |
| E-1 | 데이터 품질 | ○ 완전 | DLT Expectations, DQ 모니터링 |
| C-1 | 접근 제어 | ○ 완전 | RBAC + ABAC(GA) |
| C-2 | 데이터 분류 | ○ 완전 | AI 자동 태깅, 정책 연동 |
| F-1 | DataOps | ○ 완전 | DAB, Workflows, CI/CD |
| F-2 | 데이터 생애주기 | ○ 완전 | Time Travel, Retention Policy |

---

## 강점

1. **AI 거버넌스 올인원**: 데이터·ML 모델·AI 에이전트를 단일 Unity Catalog로 통합 관리
2. **컬럼 레벨 리니지 자동화**: 별도 설정 없이 Spark 쿼리 실행만으로 캡처
3. **Delta Lake 생태계**: Delta Sharing, Iceberg 상호운용으로 개방성 확보
4. **IDC/Gartner 최상위 평가**: AI 거버넌스 플랫폼 리더 포지션 지속
5. **개발자 친화적**: Git 연동, DAB, Terraform으로 Infrastructure as Code 완성

---

## 약점·주의점

1. **SaaS 전용**: 완전 온프레미스 배포 불가 — 데이터 주권 규제가 강한 환경은 제약
2. **비용 예측 어려움**: DBU 소비 기반으로 워크로드 증가 시 비용 급등 가능
3. **비(非) Spark 워크로드 거버넌스**: 외부 DB(PostgreSQL 등)는 2026년부터 점진적 지원 중, 아직 완성도 미흡
4. **Business Glossary 사용성**: 기술 사용자 중심 UI — 비즈니스 사용자 채택에 추가 교육 필요
5. **복잡도**: 초기 아키텍처 설계(메타스토어·카탈로그·스키마 계층) 설계 오류 시 수정 비용 큼

---

## 가격 모델

- **DBU (Databricks Unit)** 소비 기반 — 워크로드 유형(All-Purpose, Jobs, SQL, DLT, Photon)별 DBU 단가 차등
- Unity Catalog는 Databricks 구독에 포함 (별도 추가 비용 없음)
- 클라우드 저장소(S3/ADLS/GCS) 비용은 별도
- Enterprise 플랜(계약 기반)은 볼륨 할인 가능
- 참고: https://www.databricks.com/product/pricing

---

## 연동 생태계

- **커넥터**: 200+ 데이터 소스 (Fivetran, dbt, Airbyte, 네이티브 파트너십)
- **BI 도구**: Power BI, Tableau, Looker, ThoughtSpot (Databricks SQL 엔드포인트 경유)
- **AI/ML**: MLflow, Hugging Face, LangChain, LlamaIndex 네이티브 통합
- **오픈 표준**: Delta Lake, Apache Iceberg, Apache Spark, Apache Parquet
- **API**: REST API, JDBC/ODBC, Terraform Provider
- **MCP**: 파트너 솔루션(Atlan, OpenMetadata)을 통한 간접 지원; 자체 MCP 서버는 개발 중(2026)
- **Iceberg Federation**: AWS Glue, Snowflake Horizon, Hive Metastore 연동

---

## 출처

- https://www.databricks.com/blog/whats-new-databricks-unity-catalog-data-ai-summit-2025
- https://www.databricks.com/blog/databricks-named-leader-idc-marketscape-worldwide-unified-ai-governance-platforms-2025-2026
- https://www.databricks.com/blog/governing-ai-agents-scale-unity-catalog
- https://docs.databricks.com/aws/en/data-governance/unity-catalog/
- https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/ai-governance
- https://www.startuphub.ai/ai-news/technology/2026/databricks-unifies-data-governance
- https://dzone.com/articles/unity-catalog-ai-databricks-data-governance
