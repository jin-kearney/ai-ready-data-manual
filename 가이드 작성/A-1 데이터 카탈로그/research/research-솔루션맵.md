# 데이터 카탈로그 솔루션 맵 — 리서치 원자료

> 관점: 데이터 카탈로그 = AI가 쓸 데이터 자산을 "찾고·등록·정비"하는 도구.
> 모델 학습·RAG 구현 방법은 다루지 않는다.
> 독자: 제조 대기업(두산 계열사) 현업 실무자.
> 접속일: 2026-06-18

---

## 1. 솔루션 유형 분류

데이터 카탈로그 솔루션은 크게 세 유형으로 나뉜다.

| 유형 | 특징 | 대표 솔루션 |
|------|------|-------------|
| **전용 카탈로그(Dedicated Catalog)** | 카탈로그·거버넌스 전문. 풍부한 워크플로우·비즈니스 메타데이터. 구축 기간 3~6개월 | Collibra, Alation, Informatica CDGC, IBM Knowledge Catalog, Atlan, data.world |
| **클라우드 네이티브(Cloud-Native)** | 해당 클라우드 서비스와 강력히 통합. 자동 크롤러·서버리스. 타 클라우드 연동은 제한적 | Microsoft Purview, AWS Glue Data Catalog, Google Knowledge Catalog, Databricks Unity Catalog |
| **오픈소스(Open Source)** | 라이선스 무료. 커스터마이징 자유. 인프라·운영 인력 필요(0.5~1 FTE) [src-001] | DataHub(Acryl), OpenMetadata, Amundsen, Apache Atlas |

### 유형별 장단점 요약

**전용 카탈로그**
- 장점: 엔터프라이즈 거버넌스 워크플로우 완성도, 비즈니스 용어집·정책·승인 프로세스 내장, 글로벌 규제(GDPR·HIPAA) 대응 템플릿
- 단점: 라이선스 비용 높음, 구축 기간 長(3~6개월), 기술 전담 팀 필요 [src-007]

**클라우드 네이티브**
- 장점: 기존 클라우드 서비스와 즉시 연동, 서버리스·자동 스케일링, 초기 도입 빠름(수 주 이내)
- 단점: 특정 클라우드 종속(lock-in), 멀티클라우드·온프레미스 연동 제한, 비즈니스 맥락 기능 빈약 [src-007]

**오픈소스**
- 장점: 라이선스 무료, 완전한 커스터마이징, 커뮤니티 생태계
- 단점: 실제 비용은 엔지니어링 인력(0.5~1 FTE)이 주를 이룸, 배포·통합·운영 직접 담당 [src-001]

---

## 2. 엔터프라이즈 전용 솔루션

### 2-1. Collibra Data Catalog

- **한 줄 정체성**: 데이터 자산을 중앙에서 통합 조망하게 해 주는 엔터프라이즈 메타데이터·거버넌스 플랫폼 [src-002]
- **자동 수집(커넥터/크롤러)**: 100개 이상 네이티브 커넥터. 클라우드 플랫폼, 데이터베이스, 엔터프라이즈 애플리케이션, BI 도구, 레거시 시스템 포함 [src-002]
- **검색·탐색**: Collibra AI Copilot을 통한 자연어 검색. 데이터 의존성·계보를 인터랙티브 흐름도로 시각화 [src-002]
- **메타데이터 통합/거버넌스**: 자동 데이터 분류·민감정보(PII/PHI) 탐지. 기술 메타데이터와 비즈니스 개념(용어집·정책)을 잇는 시맨틱 레이어. 데이터 계약(Data Contract)·데이터 공유 협약 관리. GDPR·HIPAA·CCPA·SOX 등 규제 자동 점검 [src-003]
- **AI·시맨틱 기능**: AI Copilot으로 자연어 탐색·용어 정의 즉시 답변. 2025년 Deasy Labs 인수로 비정형 데이터(문서·전사 자료) 메타데이터 확장. AI 거버넌스 기능으로 AI 모델·에이전트 자산도 카탈로그에 등록·모니터링 가능 [src-003]
- **시장 평가**: Gartner Magic Quadrant for Data and Analytics Governance Platforms 2025 Leaders [src-008]
- **공식 출처**: https://www.collibra.com/products/data-catalog [src-002]

### 2-2. Alation

- **한 줄 정체성**: AI 기반 데이터 탐색·거버넌스 플랫폼으로 현업이 데이터를 찾고 이해하고 신뢰하도록 지원 [src-004]
- **자동 수집(커넥터/크롤러)**: 120개 이상 사전 구축 커넥터. 관계형 DB, 파일, BI 시스템, 애플리케이션, AI 모델, Open Connector Framework(OFC)를 통한 커스텀 소스 [src-004]
- **검색·탐색**: 머신러닝 기반 자연어 검색. 인기 데이터 자산 자동 추천. Excel·Slack·Teams에서 바로 검색하는 Alation Anywhere 기능 [src-004]
- **메타데이터 통합/거버넌스**: 엔드투엔드 데이터 계보 추적. Trust Flag(신뢰도 표시)·사용자 코멘트·검증 워크플로. Open Data Quality Framework 연동. 컴플라이언스 정책 시행 [src-004]
- **AI·시맨틱 기능**: ALLIE AI로 메타데이터 자동 추천·지능형 큐레이션. Documentation Agent(자산명→비즈니스 용어 자동 번역), Data Quality Agent(이상 탐지 자동화), Data Products Builder Agent(신뢰 데이터셋 패키징) — 3개의 전문 에이전트로 구성된 Alation Intelligence Platform(AIP) [src-005]. 2026년 Claude 연동(Alation Skills) 발표 [src-009]
- **시장 평가**: Forrester Wave Data Governance Solutions Q1 2025 Leader [src-005], Gartner Magic Quadrant 2026 Leader [src-008]
- **공식 출처**: https://www.alation.com/product/data-catalog/ [src-004]

### 2-3. Informatica Cloud Data Governance and Catalog (CDGC)

- **한 줄 정체성**: 대규모 하이브리드·멀티클라우드 환경에서 데이터·AI 거버넌스를 자동화하는 엔드투엔드 플랫폼 [src-006]
- **자동 수집(커넥터/크롤러)**: Informatica IICS 생태계 전반 통합. 정형·비정형 데이터 모두 대상. 2025년 비정형 데이터 거버넌스·AI 자산 인벤토리 스캔 기능 추가(Google Vertex AI 포함) [src-006]
- **검색·탐색**: AI 기반 데이터 분류가 비즈니스 맥락·기술 메타데이터를 자동 연결. 브라우징 가능한 계층적 카탈로그 뷰 [src-006]
- **메타데이터 통합/거버넌스**: CLAIRE® AI 엔진으로 민감정보 자동 탐지·태그 추천·관계 추론·계보 시각화 — 사람 개입 최소화. 정책 자동화로 컴플라이언스 강화 [src-006]
- **AI·시맨틱 기능**: CLAIRE® 엔진 전반 내재. 2025 Fall 릴리스에서 멀티에이전트 시스템 모델링 및 AI 자산 거버넌스 확장 [src-006]
- **시장 평가**: Gartner Magic Quadrant 2025 Leader, Completeness of Vision·Ability to Execute 모두 최상위 [src-008]
- **공식 출처**: https://www.informatica.com/products/data-governance/cloud-data-governance-and-catalog.html [src-006]

### 2-4. IBM Knowledge Catalog (watsonx.data Intelligence)

- **한 줄 정체성**: 하이브리드 환경에서 데이터·AI 거버넌스를 자동화하는 IBM Cloud Pak for Data 통합 카탈로그 [src-010]
- **자동 수집(커넥터/크롤러)**: 30개 이상 네이티브 커넥터. DB2·Oracle·SQL Server 등 DB, Hadoop/Spark 빅데이터 플랫폼, AWS S3·Azure Blob·GCS 클라우드, Salesforce·Workday SaaS, Tableau·Cognos·Watson Studio BI·AI 도구 [src-010]
- **검색·탐색**: 메타데이터 보강·자동 분류로 검색 가능한 카탈로그 구성. Watson Knowledge Studio 연동으로 AI용 메타데이터 준비 [src-010]
- **메타데이터 통합/거버넌스**: 역할·속성 기반 접근 제어(RBAC/ABAC). PII 탐지·마스킹. 데이터 계보 추적·감사 로그. 정책 시행 자동화 [src-010]
- **AI·시맨틱 기능**: 비즈니스 의미·정책·관계를 데이터에 연결해 AI 시스템이 올바른 맥락으로 데이터 해석·사용 가능 [src-010]
- **시장 평가**: Gartner Magic Quadrant 2026 Leader [src-008]
- **공식 출처**: https://www.ibm.com/products/watsonx-data-intelligence/governance-catalog [src-010]

### 2-5. Atlan

- **한 줄 정체성**: AI를 위한 컨텍스트 레이어(Context Layer for AI) — 전통 카탈로그를 넘어 AI 에이전트가 읽을 수 있는 구조화된 메타데이터 컨텍스트 제공 [src-011]
- **자동 수집(커넥터/크롤러)**: 80개 이상 커넥터. Snowflake·BigQuery·Redshift·Databricks 등 데이터 웨어하우스, 파이프라인, BI 도구, SaaS 앱. App SDK로 커스텀 커넥터 빠른 개발 가능 [src-011]
- **검색·탐색**: 자연어 대화형 검색("우리 가장 신뢰할 수 있는 이탈 데이터셋이 뭐야?"). 도메인별 결과 개인화. Slack·Teams 연동 [src-011]
- **메타데이터 통합/거버넌스**: 컬럼 수준 계보(SQL·파이프라인·API 전체). 품질 신호·거버넌스 분류가 다운스트림으로 자동 전파. 속성 기반 접근 제어·자동 마스킹 [src-011]
- **AI·시맨틱 기능**: 9개의 Context Agent(설명 자동 생성·용어집·품질 점수·도메인 분류 등). 2026년 4월 기준 50개 이상 엔터프라이즈 고객에서 69만 건 이상 설명 자동 생성 — 87% 인간 수준 이상 평가 [src-011]. MCP·A2A·SQL·REST API로 컨텍스트 노출 [src-011]
- **시장 평가**: Gartner Magic Quadrant 2025 Metadata Management Leader, 2026 Data and Analytics Governance Platforms Leader [src-008]
- **공식 출처**: https://atlan.com/data-discovery-catalog/ [src-011]

### 2-6. data.world

- **한 줄 정체성**: 지식 그래프(Knowledge Graph) 아키텍처 기반의 데이터 카탈로그·거버넌스 플랫폼 [src-012]
- **자동 수집(커넥터/크롤러)**: 20개 이상 플랫폼 연동. Snowflake·Databricks·Oracle·PostgreSQL·dbt·Power BI·Tableau·Looker·Fivetran 포함. 하이브리드(온프레미스+클라우드) 아키텍처 지원 [src-012]
- **검색·탐색**: LLM 기반 AI 검색·자동 보강·가이드 탐색. 자연어 SQL 생성·해석. Eureka Answers™(검색 엔진 지식 카드 형태 답변)·Eureka Explorer™(지식 그래프 시각 탐색) [src-012]
- **메타데이터 통합/거버넌스**: 지식 그래프가 기술 메타데이터와 비즈니스 맥락을 실시간으로 연결. 데이터 계보 추적. 거버넌스 워크플로 자동화 [src-012]
- **AI·시맨틱 기능**: AI Context Engine이 전통 카탈로그 대비 4.2배 정확한 AI 응답 제공[src-012]. 클라우드 네이티브(서버리스)로 신규 AI 기능 즉시 전 사용자 배포 [src-012]
- **공식 출처**: https://data.world/product/ [src-012]

---

## 3. 클라우드 네이티브 솔루션

### 3-1. Microsoft Purview Unified Catalog

- **한 줄 정체성**: Azure·온프레미스·멀티클라우드 전체 데이터 자산을 단일 SaaS 거버넌스 프레임워크로 관리하는 통합 카탈로그 [src-013]
- **자동 수집(커넥터/크롤러)**: Azure 서비스(Blob Storage·ADLS Gen2·SQL Database·Synapse·Databricks·Cosmos DB 등), 데이터베이스(Oracle·Snowflake·Teradata·SAP HANA·SAP ECC·SAP S/4HANA·MySQL·PostgreSQL·DB2), 파일(Amazon S3·HDFS), 서비스·앱(Power BI·Fabric·Tableau·Looker·Salesforce·Qlik·Airflow·Dataverse) — 전체 약 35개 이상 공식 지원 소스 [src-014]
- **검색·탐색**: AI 코파일럿 기반 검색. 거버넌스 도메인·데이터 제품별 카탈로그 구조화 탐색. 셀프서비스 접근 요청 단일 창구 [src-013]
- **메타데이터 통합/거버넌스**: 3단계 스캔(L1 기본정보·L2 스키마·L3 분류 적용). 자동 민감정보 분류·감도 레이블 부착. 용어집·중요 데이터 요소(CDE)·데이터 품질 규칙 전사 적용. 거버넌스 도메인별 OKR 연동 [src-013][src-014]
- **AI·시맨틱 기능**: Purview AI 코파일럿 통한 데이터 탐색. Anthropic Claude Enterprise 데이터 커넥터 추가(Preview, 2025) [src-014]. Fabric·Power BI 라이브 뷰로 실시간 메타데이터 확인 [src-014]
- **공식 출처**: https://learn.microsoft.com/en-us/purview/unified-catalog [src-013]

### 3-2. AWS Glue Data Catalog

- **한 줄 정체성**: AWS 데이터 레이크·웨어하우스의 서버리스 중앙 메타데이터 저장소로 크롤러가 스키마를 자동 발견·등록 [src-015]
- **자동 수집(커넥터/크롤러)**: 크롤러가 Amazon S3·Redshift·Aurora·RDS에 직접 연결해 스키마 자동 추출·등록. 온디맨드·스케줄·이벤트 트리거 방식 지원. AWS 외 외부 소스는 호환 커넥터 필요(메타데이터 동기화에 제한적) [src-015]
- **검색·탐색**: AWS Athena·Redshift Spectrum 등 서비스와 직접 연동해 카탈로그 테이블을 바로 쿼리 가능. Amazon SageMaker·CloudWatch와 통합 [src-015]
- **메타데이터 통합/거버넌스**: 테이블 정의·잡 명세·스키마 이력 관리. 파티션 자동 등록·통계 자동 계산 [src-015]
- **AI·시맨틱 기능**: Schema Registry로 Apache Avro 스키마 유효성 검증·진화 관리(Kafka·MSK·Kinesis·Flink·Lambda 연동). 비즈니스 맥락 기능은 제한적 — AWS Lake Formation과 조합 시 거버넌스 강화 [src-015]
- **공식 출처**: https://aws.amazon.com/glue/features/ [src-015]

### 3-3. Google Knowledge Catalog (구 Dataplex Universal Catalog)

- **한 줄 정체성**: 분산된 데이터·AI 자산의 발견·인벤토리를 자동화하는 완전 관리형 서비스. 2026년 4월 10일 Knowledge Catalog으로 리브랜딩 [src-016]
- **자동 수집(커넥터/크롤러)**: BigQuery(데이터셋·테이블·뷰·모델), Dataform, Dataproc Metastore, Iceberg REST Catalog, Vertex AI(모델·데이터셋·피처 그룹), Bigtable, Spanner, AlloyDB, Cloud SQL, Pub/Sub, Cloud Storage, Looker(Preview). 서드파티는 관리형 연결 파이프라인으로 통합 [src-016]
- **검색·탐색**: 자연어 시맨틱 검색으로 전체 Google Cloud 소스 탐색. 검색 API 무료 제공 [src-016]
- **메타데이터 통합/거버넌스**: 비즈니스 용어집·엔트리 링크·측면(Aspect) 기반 메타데이터 보강. 타입별 항목(Entry Type)으로 메타데이터 표준 강제. 메타데이터 변경 피드를 Pub/Sub으로 스트리밍해 자동화 워크플로 가능 [src-016]
- **AI·시맨틱 기능**: Gemini 기반 카탈로그. 정형·비정형 데이터에서 의미 자동 추출해 동적 컨텍스트 그래프 구성. AI 에이전트 할루시네이션 저감 위해 MCP 표준으로 인증된 컨텍스트 제공 [src-016]
- **공식 출처**: https://docs.cloud.google.com/dataplex/docs/catalog-overview [src-016]

### 3-4. Databricks Unity Catalog

- **한 줄 정체성**: Databricks 레이크하우스 위에서 데이터·앱·AI 에이전트를 통합 거버넌스하는 단일 계층 [src-017]
- **자동 수집(커넥터/크롤러)**: Databricks 내 SQL 쿼리·Delta Live Tables 파이프라인 실행 시 계보 자동 캡처(별도 설정 불필요). 외부 계보는 Salesforce·MySQL(업스트림), Tableau·Power BI(다운스트림)를 Catalog Explorer UI·API·SDK·Lakeflow Connect로 수동 등록 [src-017]
- **검색·탐색**: Unity Catalog 메타데이터를 Microsoft Purview와 통합해 Azure 전체 거버넌스 단일 뷰 가능 [src-017]
- **메타데이터 통합/거버넌스**: 컬럼 수준 자동 계보. 워크스페이스 전반 접근 제어·감사 로그 자동 적용. EU AI Act 컴플라이언스용 AI 모델·피처 테이블·평가 데이터셋 거버넌스 [src-017]
- **AI·시맨틱 기능**: 2025년 LLM 기반 문서 자동 생성으로 메타데이터 일관성·투명성 향상. Unity AI Gateway로 파운데이션 모델 접근 정책(모델 제공자·국가·승인 상태·태그 등 속성 기반) 동적 적용 [src-017]
- **공식 출처**: https://www.databricks.com/product/unity-catalog [src-017]

---

## 4. 오픈소스 솔루션

### 4-1. DataHub (Acryl Data)

- **한 줄 정체성**: LinkedIn이 개발하고 AcrylData가 관리하는 확장 가능한 메타데이터 플랫폼 — 데이터 탐색·관측성·연합 거버넌스 지원 [src-018]
- **자동 수집(커넥터/크롤러)**: Snowflake·BigQuery·dbt·Airflow·Looker·Kafka 등 사전 구축 커넥터 다수. 커뮤니티에서 지속 추가 중. v1.4.0에서 Google Dataplex·Azure Data Factory·IBM Db2 커넥터 추가 [src-018]
- **검색·탐색**: DB·데이터 레이크·BI 플랫폼·ML 피처 스토어·오케스트레이션 도구 전체를 단일 검색으로 조회. 플랫폼·데이터셋·ETL·차트·대시보드 계보 추적 [src-018]
- **메타데이터 통합/거버넌스**: Kafka 기반 이벤트 스트림으로 실시간 메타데이터 처리(데이터 메시 아키텍처 적합). 컬럼 수준 계보. 메타데이터 테스트(Metadata Tests)로 중요 자산 조건 지속 평가. 용어집·태그 승인 워크플로 [src-018]
- **AI·시맨틱 기능**: MCP(Model Context Protocol) 지원으로 AI 어시스턴트가 메타데이터를 대화형으로 쿼리. ML 모델·피처·벡터 DB·노트북·LLM 파이프라인도 카탈로그에 등록 [src-018]. 2025년 1월 DataHub 1.0 출시(5주년) [src-001]
- **아키텍처**: 관계형 DB(문서 저장)·Elasticsearch(검색)·JanusGraph/Neo4j(그래프)·Kafka(스트림) — 강력하나 인프라 복잡도 높음 [src-001]
- **공식 출처**: https://datahubproject.io/ [src-018]

### 4-2. OpenMetadata

- **한 줄 정체성**: AI·데이터 카탈로그·메타데이터 관리를 위한 #1 오픈소스 컨텍스트 레이어 — Apache Hadoop·Atlas·Uber Databook 설립자들이 구축 [src-019]
- **자동 수집(커넥터/크롤러)**: 130개 이상 데이터 커넥터. 데이터베이스(Snowflake·BigQuery·PostgreSQL·MySQL·Oracle 등), 데이터 레이크(AWS S3·Azure Data Lake·GCS), 파이프라인(Airflow·Dagster·dbt·Fivetran), 대시보드(Tableau·Looker·Power BI·Metabase), ML(MLflow·SageMaker), 메시징(Kafka·Kinesis) [src-019]
- **검색·탐색**: 시맨틱 그래프 기반 탐색. 데이터 계보 시각화. 커뮤니티 4,000개 이상 엔터프라이즈 배포, 13,500명 이상 커뮤니티 멤버 [src-019]
- **메타데이터 통합/거버넌스**: W3C 표준(RDF·OWL·DCAT·Schema.org) 기반 관계. 용어집·메트릭 정의·분류·온톨로지. 인간과 AI 모든 변경 감사 추적. 2025년 6월 OpenMetadata 1.8에서 데이터 계약(Data Contract — 머신 판독 스키마·SLA·품질 보증 자동 시행) 도입 [src-001]
- **AI·시맨틱 기능**: 네이티브 MCP 서버로 에이전트가 메타데이터 직접 접근. AI SDK로 외부 에이전트 프로그래매틱 접근 [src-019]
- **아키텍처**: MySQL/PostgreSQL(메타데이터) + Elasticsearch(검색) — 그래프 DB 없이 단순 스택 유지. DataHub 대비 운영 복잡도 낮음 [src-001]
- **공식 출처**: https://open-metadata.org/ [src-019]

### 4-3. Amundsen (Linux Foundation)

- **한 줄 정체성**: Lyft가 만든 "구글 검색 같은" 데이터 발견 도구 — 발견 특화, 거버넌스 기능은 제한적 [src-020]
- **자동 수집(커넥터/크롤러)**: 다양한 백엔드 환경 지원. 정교한 데이터 미리보기 기능 [src-020]
- **검색·탐색**: PageRank 기반 검색 알고리즘으로 관련성 높은 자산 상위 노출. 데이터 기원(Provenance)·영향 계보 표시. 데이터셋 주석·인사이트 공유 [src-020]
- **메타데이터 통합/거버넌스**: 기본 거버넌스 기능 제한적 — 데이터 품질 등 추가 기능은 커스텀 개발 필요 [src-020]
- **AI·시맨틱 기능**: 제한적. Linux Foundation으로 이전 후 로드맵 불명확, 문서 노후화 [src-001]
- **주의**: 새로 도입 시 DataHub·OpenMetadata 우선 검토 권장. 이미 Amundsen을 수년 사용 중인 경우에만 유지 [src-001]
- **공식 출처**: https://www.amundsen.io/ [src-020]

### 4-4. Apache Atlas

- **한 줄 정체성**: Hadoop 생태계 전용 오픈소스 메타데이터 관리·데이터 거버넌스 플랫폼 [src-020]
- **자동 수집(커넥터/크롤러)**: Hadoop 네이티브 소스(HDFS·Hive·HBase·Kafka·Sqoop·Storm·Falcon·Oozie 등)와 자동 연동. Hadoop 외 커넥터는 제한적 [src-020]
- **검색·탐색**: 유형·엔터티 모델(Type-and-Entity) 기반 자산 검색. Apache Ranger 통합으로 분류 기반 정책 시행 [src-020]
- **메타데이터 통합/거버넌스**: 컬럼 수준 계보(Hadoop 네이티브 소스). 계층적 비즈니스 용어집. Apache Ranger와 연동한 세밀한 접근 제어·데이터 마스킹 [src-020]
- **AI·시맨틱 기능**: 제한적. 2025년 초 기준 이슈 대응 속도 느림, 일부 GitHub 이슈 수개월 미해결 [src-001]
- **주의**: Hadoop 환경을 이미 운영 중인 조직 외에는 신규 도입 비추천 [src-020]
- **공식 출처**: https://atlas.apache.org/ [src-020]

---

## 5. 기능 비교 기준 매트릭스

| 비교 기준 | 엔터프라이즈 전용 | 클라우드 네이티브 | 오픈소스 |
|-----------|-----------------|-----------------|----------|
| **자동 수집 커버리지** | 80~120+ 소스 | 해당 클라우드 강함, 타 클라우드 제한 | DataHub·OpenMetadata 130+, Atlas·Amundsen 제한 |
| **비즈니스 메타데이터·용어집** | 풍부 (내장 워크플로) | 기본~중간 | DataHub·OpenMetadata 지원, Atlas·Amundsen 제한 |
| **검색·탐색 UX** | 자연어·AI 코파일럿 | 자연어·클라우드 통합 | DataHub·OpenMetadata 자연어, Amundsen PageRank |
| **계보(Lineage) 깊이** | 엔드투엔드 (컬럼 수준) | 클라우드 내 자동, 외부 제한 | 컬럼 수준 (DataHub·OpenMetadata), Atlas Hadoop 전용 |
| **권한·거버넌스** | 엔터프라이즈급 워크플로 | 클라우드 IAM 연동 | 커스텀 개발 필요 |
| **AI·자동 분류** | CLAIRE/ALLIE/AI Copilot 등 | Gemini/Copilot/LLM | MCP 지원, AI 기능 직접 구현 |
| **가격 모델** | 라이선스 기반 (고비용) | 사용량 기반 (클라우드 요금) | 무료(인프라·인력 비용 별도) |
| **구축 난이도** | 3~6개월, 전담팀 필요 | 수 주(동일 클라우드 기준) | 0.5~1 FTE 지속 필요 [src-001] |
| **초기 도입 시간** | 느림 | 빠름 | 중간~느림 |

---

## 6. 시장 평가 (Gartner Magic Quadrant)

2025~2026 Gartner Magic Quadrant for Data and Analytics Governance Platforms에서 공개된 Leaders군 [src-008]:

- **Collibra** — Leader (2025)
- **Alation** — Leader (2025, 2026)
- **Informatica** — Leader (2025), Completeness of Vision·Ability to Execute 최상위
- **IBM** — Leader (2026)
- **Atlan** — 2025 Visionary → 2026 Leader로 이동

> 주의: Gartner 보고서 본문은 유료. 위 내용은 각 벤더 공식 발표·블로그(공개 자료)에서 확인한 사실만 기재.

---

## 출처

| id | URL | 제목 | 접속일 |
|----|-----|------|--------|
| src-001 | https://thedataguy.pro/blog/2025/08/open-source-data-governance-frameworks/ | Open-Source Data Governance Frameworks: A Strategic Analysis | 2026-06-18 |
| src-002 | https://www.collibra.com/products/data-catalog | Data catalog: Bring your data into focus \| Collibra | 2026-06-18 |
| src-003 | https://erstudio.com/blog/collibra-data-governance/ | Collibra Data Governance: Features, Reviews, and Use Cases | 2026-06-18 |
| src-004 | https://www.alation.com/product/data-catalog/ | Alation Data Catalog \| AI-Powered Data Discovery & Governance | 2026-06-18 |
| src-005 | https://www.alation.com/ | Alation Agentic Data Intelligence Platform | 2026-06-18 |
| src-006 | https://www.informatica.com/products/data-governance/cloud-data-governance-and-catalog.html | Cloud Data Governance and Data Catalog – Informatica | 2026-06-18 |
| src-007 | https://atlan.com/data-catalog-tools/ | 16 Best Data Catalog Tools in 2026: Buyer's Guide \| Atlan | 2026-06-18 |
| src-008 | https://www.informatica.com/about-us/news/news-releases/2025/01/20250113-informatica-named-a-leader-in-2025-gartner-magic-quadrant-for-data-and-analytics-governance-platforms.html | Informatica Named a Leader in 2025 Gartner Magic Quadrant | 2026-06-18 |
| src-009 | https://www.alation.com/blog/claude-data-catalog-introducing-alation-skills/ | Introducing Alation Skills: AI-Powered Data Catalog Access in Claude | 2026-06-18 |
| src-010 | https://nexright.com/ibm-watson-knowledge-catalog/ | IBM Watson Knowledge Catalog: Smarter Data Management | 2026-06-18 |
| src-011 | https://atlan.com/data-discovery-catalog/ | The Data Catalog of Choice for Enterprise AI \| Atlan | 2026-06-18 |
| src-012 | https://data.world/product/ | The data catalog platform powered by a knowledge graph architecture \| data.world | 2026-06-18 |
| src-013 | https://learn.microsoft.com/en-us/purview/unified-catalog | Learn about Microsoft Purview Unified Catalog \| Microsoft Learn | 2026-06-18 |
| src-014 | https://learn.microsoft.com/en-us/purview/data-map-data-sources | Data sources that connect to Microsoft Purview Data Map \| Microsoft Learn | 2026-06-18 |
| src-015 | https://aws.amazon.com/glue/features/ | Serverless Data Integration – AWS Glue Features – AWS | 2026-06-18 |
| src-016 | https://docs.cloud.google.com/dataplex/docs/catalog-overview | About metadata management in Knowledge Catalog \| Google Cloud | 2026-06-18 |
| src-017 | https://www.databricks.com/product/unity-catalog | Unity Catalog \| Databricks | 2026-06-18 |
| src-018 | https://datahubproject.io/ | DataHub \| AI & Data Context Management Platform | 2026-06-18 |
| src-019 | https://open-metadata.org/ | OpenMetadata — The #1 Open Source Context Layer for AI | 2026-06-18 |
| src-020 | https://atlan.com/open-source-data-catalog-tools/ | Open Source Data Catalog: Top 5 Tools To Consider in 2026 \| Atlan | 2026-06-18 |
