# E-1 데이터 Product화 — Tech Stack / 솔루션 리서치 노트

> 작성일: 2026-06-24
> 목적: E-1 가이드의 솔루션 섹션 초안 근거 자료. 웹 리서치(공식 페이지 직접 확인) 기반.
> 주의: 가격·에디션·버전은 사실로 단정하지 않음 — "PoC/공식 견적·문서 확인" 표기.

---

## 1. 솔루션 유형 개요 (3가지 유형)

데이터 Product화를 지원하는 솔루션은 세 가지 유형으로 구분한다.

**유형 A — 데이터 Product 카탈로그 · 마켓플레이스(Catalog/Marketplace)**
데이터 Product를 명세서(Spec)·Owner·품질 기준과 함께 등록하고, 소비자가 검색·요청·승인을 거쳐 데이터에 접근하는 거버넌스 레이어. 전용 마켓플레이스 UI를 갖춘다.
대표: Collibra Data Marketplace, Alation Data Products Marketplace, Informatica Cloud Data Marketplace

**유형 B — 셀프서비스 제공 플랫폼(Self-Serve Data Platform)**
명세서 정의뿐 아니라 데이터 실제 전달(테이블·스트림·API·모델 등)까지 플랫폼 자체가 처리한다. 거버넌스·연산·공유 프로토콜이 통합되어 있다.
대표: Databricks (Unity Catalog + Marketplace), Snowflake (Horizon + Marketplace), Microsoft Fabric, Nextdata OS

**유형 C — 기존 데이터 카탈로그 확장형(Catalog Extension)**
기존 메타데이터 카탈로그에 "데이터 Product" 객체 유형을 추가한 형태. 데이터 실제 이동은 원천 시스템이 담당하고, 카탈로그는 명세·거버넌스·발견을 관리한다.
대표: Microsoft Purview Unified Catalog, DataHub OSS, Atlan, Google Knowledge Catalog, data.world CTK

---

## 2. 솔루션별 상세 (유형별 정리)

---

### 유형 A — 데이터 Product 카탈로그 · 마켓플레이스

---

#### 2-A1. Collibra Data Marketplace

**공식 URL:** https://www.collibra.com/products/data-marketplace

**솔루션 유형:** 유형 A — 엔터프라이즈 거버넌스 기반 카탈로그+마켓플레이스

**확인된 주요 기능:**

| 기능 | 내용 |
|---|---|
| 명세서(Spec) | 목적·품질 기대치·Owner·사용 가이드라인을 담은 데이터 Product 레코드 |
| Owner 관리 | Product 레코드의 구조화 메타데이터 항목으로 Owner 지정 |
| SLA/SLO | 전용 SLA 필드는 없음; 품질 인증(Quality Certification)·품질 점수·감사 추적으로 대체 |
| 소비 방식 | 마켓플레이스 쇼핑 UI → 요청·승인 → Collibra Data Notebook(쿼리); API는 Product 유형 중 하나로 등록 가능 |
| 사용 로그 | 요청자·목적·기간의 감사 추적; 평점·리뷰·댓글(인기도 시그널) |
| 다(多)시스템 연계 | 리니지 가시성 제공; 커넥터 에코시스템 통해 다중 원천 연계 |
| 발견·검색 | 도메인·Owner·시스템·분류·커스텀 속성 필터; AI Copilot(자연어 검색) |
| 특이사항 | Jira, ServiceNow 연동으로 승인·이행(fulfillment) 자동화 |

**적합:** 엔터프라이즈 거버넌스(GDPR·내부통제) 요구가 강하고, 기존에 Collibra를 카탈로그로 쓰는 조직. 마켓플레이스를 기존 거버넌스 레이어 위에 올리고 싶을 때.

---

#### 2-A2. Alation Data Products Marketplace + Data Products Builder Agent

**공식 URL:**
- 마켓플레이스: https://www.alation.com/product/data-products-marketplace/
- AI 빌더 에이전트: https://www.alation.com/product/data-products-builder-agent/

**솔루션 유형:** 유형 A/B 경계 — 카탈로그 네이티브 마켓플레이스 + AI 보조 Product 생성 (ODPS 표준 채택)

**확인된 주요 기능:**

| 기능 | 내용 |
|---|---|
| 명세서(Spec) | 개방 표준 **ODPS(Open Data Products Specification)** 기반; 버전·인증 상태·문서·Policy 연결·Owner 포함 |
| Owner 관리 | ODPS Owner 필드; 노코드 도메인팀이 수 분 내 Product 생성 |
| SLA/SLO | 전용 SLA 필드 없음; 인증 워크플로우(품질·소유권·컴플라이언스 기준 인증) + 버전 관리가 계약적 역할 |
| 소비 방식 | 마켓플레이스 UI; 자연어 채팅(데이터셋·조인·정의 응답); AI 에이전트 소비(ODPS 기계 가독 형식) |
| 사용 로그 | Product별 방문 수·사용 통계 대시보드 |
| 다(多)시스템 연계 | Active Metadata Graph + 100개 이상 커넥터 |
| 발견·검색 | 인증 마켓플레이스; 요청·승인 워크플로우; Data Products Builder Agent가 후보 자산 식별·자동 문서화 |
| 특이사항 | ODPS 표준으로 AI 에이전트(LLM) 직접 소비 가능 — 인간 셀프서비스와 AI 에이전트 소비를 동시 지원 |

**적합:** ODPS 표준을 도입해 다운스트림 AI 시스템이 데이터 Product를 기계 가독 형식으로 소비해야 하는 조직. AI 에이전트 기반 데이터 활용 로드맵이 있는 경우.

---

#### 2-A3. Informatica Cloud Data Marketplace

**공식 URL:** https://www.informatica.com/products/data-governance/cloud-data-marketplace.html
**참고:** https://www.informatica.com/resources/articles/data-marketplace-benefits-and-features.html

**솔루션 유형:** 유형 A — 전용 데이터 마켓플레이스 / 셀프서비스 데이터 포털

**확인된 주요 기능:**

| 기능 | 내용 |
|---|---|
| 명세서(Spec) | Data Collection(데이터 Product 상당)에 이름·목적·카테고리·이용 약관·품질 지표·프라이버시 정책 부착 |
| Owner 관리 | Data Owner 역할: 컬렉션 생성·접근 요청 승인·거버넌스 정책 관리 |
| SLA/SLO | 전용 SLA 필드 없음; 전달 방식·접근 파라미터 설정; 품질 지표 노출 |
| 소비 방식 | 셀프서비스 요청 → 승인 → 자동 프로비저닝(소비자 지정 전달 위치로); Bespoke Request(미등록 데이터 신규 요청) |
| 사용 로그 | 요청 상세·이행 상태·사용량 대시보드; Product별 구독자 수 및 수요 시그널(가장 많이 요청된 자산) |
| 다(多)시스템 연계 | IDMC(Informatica Intelligent Data Management Cloud) 에코시스템 커넥터 통해 다중 원천 자산 패키징 |
| 발견·검색 | 카테고리·도메인·전달방식·Owner별 브라우징; CLAIRE GPT(AI 검색); 동료 리뷰·평점; 자산별 채팅 채널 |
| 특이사항 | 쇼핑카트 UX·동료 리뷰·신규 데이터 타입 요청·자동 이행(fulfillment)이 가장 완성된 마켓플레이스 기능 세트 |

**적합:** 이미 Informatica IDMC를 사용하는 조직에서 내부 데이터 마켓플레이스를 빠르게 구축하려 할 때. 비기술 사용자 대상의 셀프서비스 데이터 쇼핑 경험이 필요한 경우.

---

### 유형 B — 셀프서비스 제공 플랫폼

---

#### 2-B1. Databricks — Unity Catalog + Databricks Marketplace + Delta Sharing

**공식 URL:**
- Unity Catalog: https://www.databricks.com/product/unity-catalog
- Databricks Marketplace: https://www.databricks.com/product/marketplace
- Marketplace 공개 브라우저: https://marketplace.databricks.com
- Delta Sharing 문서: https://docs.databricks.com/en/delta-sharing/index.html
- Marketplace 문서: https://docs.databricks.com/en/marketplace/index.html
- Unity Catalog 문서: https://docs.databricks.com/en/data-governance/unity-catalog/index.html

**솔루션 유형:** 유형 B — 카탈로그(Unity Catalog) + 오픈 마켓플레이스 + 공유 프로토콜(Delta Sharing/OpenSharing)의 3-레이어 구조

**확인된 주요 기능:**

| 기능 | 내용 |
|---|---|
| 명세서(Spec) | 리스팅 메타데이터: 제목·설명·샘플 SQL·프로바이더 정보; 전용 SLA 필드 없음 |
| Owner 관리 | Unity Catalog OWNERSHIP 권한 모델; 카탈로그 계층 전체에 Owner 전파 |
| SLA/SLO | 전용 SLA 필드 없음; PoC/공식 견적 확인 |
| 소비 방식 | Delta/Iceberg 테이블(쿼리), 스트리밍 테이블, Volume(비정형), 노트북, AI/ML 모델, 대시보드, MCP 서버, Solution Accelerator |
| 사용 로그 | 감사 로그 시스템 테이블; OpenSharing 구체화 이력; 프로바이더측 소비 모니터링 |
| 다(多)시스템 연계 | OpenSharing(오픈소스) — 복제 없이 크로스 클라우드(AWS·Azure·GCP) 실시간 공유; 비Databricks 클라이언트는 bearer token/OIDC로 접근; Time Travel; 행·열 레벨 필터 |
| 발견·검색 | 공개 마켓플레이스(workspace 없이 marketplace.databricks.com에서 검색); Private Exchange(초청 소비자 한정) |
| 특이사항 | MCP 서버 리스팅 — AI 에이전트가 외부 시스템과 상호작용하는 도구로 사용 |

**적합:** Databricks를 데이터 플랫폼으로 사용하는 조직이 내부 데이터 Product를 오픈 프로토콜(Delta Sharing)로 계열사·파트너에 공유하거나, 외부 데이터를 Marketplace에서 구독할 때.

---

#### 2-B2. Snowflake — Snowflake Marketplace + Horizon Catalog + Data Sharing

**공식 URL:**
- Marketplace: https://www.snowflake.com/en/data-cloud/marketplace/
- Horizon Catalog: https://www.snowflake.com/en/product/features/horizon/
- Data Sharing 개요: https://docs.snowflake.com/en/user-guide/data-sharing-intro
- Provider 가이드: https://docs.snowflake.com/en/user-guide/data-sharing-provider

**솔루션 유형:** 유형 B — 카탈로그(Horizon) + 공개/비공개 마켓플레이스 + 상용화 플랫폼

**확인된 주요 기능:**

| 기능 | 내용 |
|---|---|
| 명세서(Spec) | 리스팅 메타데이터: 제목·설명·샘플 SQL·연락처; 유료 리스팅은 계약 시작/종료일·지불 조건 추가 |
| Owner 관리 | Share 객체 OWNERSHIP 권한; `SHOW GRANTS OF SHARE`로 추적 |
| SLA/SLO | 전용 SLA 필드 없음; 유료 오퍼의 계약 기간·지불 스케줄이 유사 기능 |
| 소비 방식 | SQL 직접 쿼리(공유 DB), Secure View/Semantic View, Streams(CDC), External/Iceberg 테이블, Native App, Cortex 검색 서비스, ML 모델, UDF, Reader Account(비Snowflake 사용자) |
| 사용 로그 | 소비자 사용 메트릭(프로바이더측); Data Sharing Usage 스키마; `INFORMATION_SCHEMA.SHARED_DATASET_USAGE`; 자산 인기도 순위 |
| 다(多)시스템 연계 | Horizon Catalog — Iceberg·PostgreSQL·Tableau·Power BI·dbt 통합; 크로스 리전·크로스 클라우드 공유; 외부 엔진에도 행·열 접근 정책 시행 |
| 발견·검색 | Snowflake Marketplace(820+ 프로바이더, 3,400+ 리스팅); 내부 마켓플레이스(조직 내부용); Private Data Exchange; Horizon 단일 카탈로그 UI |
| 특이사항 | 상용화 1등급 지원(무료/체험/유료 리스팅; 개별 오퍼·청구); Clean Room(원시 데이터 노출 없이 쿼리 허용) |

**적합:** Snowflake 기반 데이터 플랫폼을 운영하는 조직이 내부 데이터 Product를 계열사에 제공하거나, 외부 데이터 마켓플레이스를 통해 유·무상으로 데이터를 수익화할 때.

---

#### 2-B3. Nextdata OS ⚠️ 초기 단계 (실험적)

**공식 URL:** https://www.nextdata.com
**제품 페이지:** https://www.nextdata.com/product
**설립자:** Zhamak Dehghani (데이터 메시 개념 창시자)
**상태:** 2025년 4월 출시; GA 일정 PoC/공식 확인 필요

**솔루션 유형:** 유형 B — 자율(Autonomous) 데이터 Product 운영 OS (데이터 메시 특화)

**확인된 주요 기능:**

| 기능 | 내용 |
|---|---|
| 명세서(Spec) | 시맨틱 우선 Product 정의; 업스트림 소비·다운스트림 공유를 위한 데이터 계약; 코드로서의 정책(Policies-as-Code) 자동 시행 |
| Owner 관리 | 도메인 Owner가 1등급 개념 — Product는 비즈니스 도메인이 소유·관리 |
| SLA/SLO | 데이터 계약에 포함; 모든 라이프사이클 단계에서 자동 시행 |
| 소비 방식 | 단일 Product에서 다중 출력: 테이블(분석), 벡터 임베딩(AI/RAG), 파일, MCP 엔드포인트 — 추가 파이프라인 불필요 |
| 사용 로그 | 실시간 모니터링 대시보드: 어떤 Product가 누구에게(사람·에이전트) 얼마나 사용되는지; 비용·컴플라이언스·헬스 메트릭 |
| 다(多)시스템 연계 | 플러그인형 드라이버로 기존 스토리지·컴퓨트·보안·품질 시스템 연계; 데이터 이전 없이 기존 스택 활용 |
| 발견·검색 | 자동 자가 발행(self-publishing); 시맨틱 그래프 형성; 인간 대상 시맨틱 검색 + AI 에이전트 대상 MCP API 자동 발견 |
| 특이사항 | 유일하게 처음부터 데이터 메시·데이터 Product 관리를 위해 설계된 플랫폼; MCP 네이티브 지원 |

**적합:** 데이터 메시 아키텍처를 도입하며 도메인별 자율적 데이터 Product 생성·운영·공유 체계를 구축하려는 조직. 단, 초기 단계이므로 PoC 및 레퍼런스 사례(Mars Pet Nutrition 외) 추가 확인 필요.

---

### 유형 C — 기존 데이터 카탈로그 확장형

---

#### 2-C1. Atlan — Data Products Marketplace (카탈로그 내장형)

**공식 URL:**
- 마케팅: https://atlan.com/data-products-marketplace/
- 마켓플레이스: https://atlan.com/data-marketplace/
- 문서: https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products

**솔루션 유형:** 유형 A/C 경계 — 카탈로그 내장 데이터 마켓플레이스 + 셀프서비스 레이어 (200+ 커넥터, MCP 지원)

**확인된 주요 기능:**

| 기능 | 내용 |
|---|---|
| 명세서(Spec) | 상태(Draft/Published/Sunset/Archived), 인증, 중요도, 민감도, 신선도, Owner, 도메인, 설명, README, 태그, 용어, 리소스, **계약(Data Contract 연결)**, 가시성 설정 |
| Owner 관리 | Owner 사용자 목록 + Owner 유형 지정 |
| SLA/SLO | Product 자체가 아닌 연결된 데이터 계약(Data Contract) 레이어에서 관리 (가용성·지연·완결성·MTBF/MTTR) |
| 소비 방식 | Output Port(테이블·대시보드·메트릭·dbt 모델·API); MCP 서버(AI 에이전트용); Slack/Teams 내 접근 요청; SQL 엔드포인트 |
| 사용 로그 | Product별 총 조회수·고유 방문자·7/30/90일 트렌드; Product Score(메타데이터 완성도); 접근 요청 추적; 신선도 모니터링 |
| 다(多)시스템 연계 | 200+ 소스 커넥터(Snowflake·Databricks·BigQuery·Redshift·dbt·Looker·Tableau·Fivetran·Airflow 등); 크로스 도메인 다중 hop 리니지 |
| 발견·검색 | 전용 마켓플레이스 UI(비기술 사용자 대상); 자연어 대화형 검색; 역할별 개인화 결과; 원클릭 접근 요청(Jira/ServiceNow 연동); Zero-Touch 프로비저닝(Immuta 연동) |

**적합:** 멀티 클라우드·멀티 소스 환경에서 기술·비기술 사용자 모두를 위한 데이터 마켓플레이스가 필요한 조직. AI 에이전트 소비를 위한 MCP 지원이 필요할 때.

---

#### 2-C2. DataHub OSS — Data Products (오픈소스)

**공식 URL:**
- 프로젝트: https://datahubproject.io (→ https://datahub.com 으로 리다이렉트)
- 문서: https://docs.datahub.com/docs/dataproducts/
- 데이터 계약: https://docs.datahub.com/docs/generated/metamodel/entities/datacontract
- GitHub: https://github.com/datahub-project/datahub

**솔루션 유형:** 유형 C — 오픈소스 메타데이터 카탈로그 + 데이터 Product 조직화 레이어

**확인된 주요 기능:**

| 기능 | 내용 |
|---|---|
| 명세서(Spec) | DataProduct 엔티티: id·도메인·표시명·설명·Owner(유형 포함)·태그·용어·커스텀 속성·output_ports·assets 목록 |
| Owner 관리 | owners 목록 + 유형(BUSINESS_OWNER 등) |
| SLA/SLO | DataContract 별도 엔티티 → FreshnessAssertion(lookback_interval·스케줄) 연결; 데이터 Product와 계약이 ContractFor 관계로 연결 |
| 소비 방식 | 카탈로그 검색 UI; GraphQL API; REST API; Python/Java SDK; DataHub CLI; Kafka 이벤트 스트림; AWS EventBridge |
| 사용 로그 | 데이터셋 수준 사용 이력; Product 수준 뷰 카운트는 로드맵(미출시) |
| 다(多)시스템 연계 | 240+ 수집 커넥터(메타데이터 복사 모델); 크로스 소스 엔드투엔드 리니지 |
| 발견·검색 | 카탈로그 검색 + 도메인 기반 탐색; 별도 마켓플레이스 UI 없음; 접근 요청 워크플로우 없음 |
| 특이사항 | 엔터프라이즈/관리형 버전(Acryl DataHub Cloud)에서 추가 기능 제공 가능; OSS 자체는 마켓플레이스 UI 부재 |

**적합:** 오픈소스 기반으로 데이터 Product 조직화와 데이터 계약(Contract)을 구현하려는 기술 역량이 있는 팀. 소비자 대상 마켓플레이스 경험보다 거버넌스 메타데이터 구조화에 집중하는 경우.

---

#### 2-C3. Microsoft Purview Unified Catalog — Data Products

**공식 URL:**
- 개요: https://learn.microsoft.com/en-us/purview/unified-catalog-data-products
- 생성·관리: https://learn.microsoft.com/en-us/purview/unified-catalog-data-products-create-manage
- 검색: https://learn.microsoft.com/en-us/purview/unified-catalog-data-products-search

**솔루션 유형:** 유형 C — 카탈로그 확장형 (Purview 스캔 데이터 위에 거버넌스·발견 레이어 추가)

**확인된 주요 기능:**

| 기능 | 내용 |
|---|---|
| 명세서(Spec) | 이름·설명(최대 10,000자)·유형(12가지)·대상 독자(8종)·Owner·거버넌스 도메인·유스케이스·Endorsed 플래그·업데이트 빈도·상태(Draft/Published/Expired)·이용 약관·OKR·용어·핵심 데이터 요소·커스텀 속성 |
| Owner 관리 | 지명 Owner + Data Product Owner 역할 |
| SLA/SLO | 전용 SLA 필드 없음; 업데이트 빈도 + 데이터 품질 점수 + 헬스 액션이 프록시 |
| 소비 방식 | 접근 요청 버튼 → 승인 워크플로우 → 번들된 모든 자산에 직접 접근(중간 레이어 없음) |
| 사용 로그 | 구독자 수; 데이터 관찰성 탭(Preview); Purview Audit 로그 |
| 다(多)시스템 연계 | Purview Data Map이 스캔한 Azure·Fabric·온프레미스·멀티클라우드 자산 모두 번들 가능 |
| 발견·검색 | Unified Catalog 검색(키워드·자연어, Preview); 거버넌스 도메인·유형·커스텀 속성·Endorsed 필터; 조직 내부 전용 |

**적합:** Microsoft Azure/Fabric 생태계를 사용하며 Purview를 데이터 거버넌스 도구로 이미 운영 중인 조직. 여러 원천 시스템의 데이터 자산을 하나의 데이터 Product로 묶어 조직 내부에 공개하고 싶을 때.

---

#### 2-C4. Microsoft Fabric — OneLake Catalog (참고: 전용 "데이터 Product" 객체 없음)

**공식 URL:**
- OneLake Catalog: https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview
- 거버넌스: https://learn.microsoft.com/en-us/fabric/governance/governance-compliance-overview

> **주의:** Fabric에는 독립된 "Data Product" 객체 유형이 없다. 데이터 메시 패턴 권고에 따르면 "워크스페이스 1개 = 데이터 Product 1개" 관례로 운영한다. 아래 기능은 Fabric 아이템(Lakehouse·Warehouse·Semantic Model·Report 등)에 적용된다.

| 기능 | 내용 |
|---|---|
| Owner 관리 | 워크스페이스 Owner; 아이템 Owner가 Promoted 인증; 도메인 관리자가 Certified 인증 |
| SLA/SLO | 전용 필드 없음; 민감도 레이블(Purview 연동)·DLP 정책·감사 로그로 거버넌스 |
| 소비 방식 | SQL(분석 엔드포인트), Semantic Model(Power BI/Excel/Copilot Studio), 파일(ADLS/OneLake API), Fabric REST API |
| 사용 로그 | Monitoring Hub, Capacity Metrics App, Admin Monitoring Workspace, Purview Audit |
| 다(多)시스템 연계 | 170+ 소스 커넥터; Mirroring(운영 DB 준실시간 복제); External Table/Shortcut(S3·ADLS·GCS 쿼리, 복제 없음) |
| 발견·검색 | OneLake Catalog Explore(도메인·태그·Endorsed 필터); 조직 내부 전용 |

**적합:** Microsoft Fabric을 메인 데이터 플랫폼으로 사용하는 조직이 데이터 Product 개념을 워크스페이스 단위로 운영하려 할 때. 별도 마켓플레이스 도입 없이 Fabric 생태계 내에서 셀프서비스를 실현하려는 경우. (완전한 데이터 Product 기능은 Purview와 병용 권장)

---

#### 2-C5. Google Knowledge Catalog — Data Products (구 Dataplex Universal Catalog)

**공식 URL:**
- 제품: https://cloud.google.com/products/knowledge-catalog
- Data Products 블로그(GA 2026년 5월): https://cloud.google.com/blog/products/data-analytics/introducing-data-products-in-dataplex-universal-catalog
- Data Products 개요: https://docs.cloud.google.com/dataplex/docs/data-products-overview

**솔루션 유형:** 유형 C — 카탈로그 확장형 (Google Cloud 데이터 자산에 데이터 Product 거버넌스 레이어 추가; GA 2026년 5월)

| 기능 | 내용 |
|---|---|
| 명세서(Spec) | 자산(포인터)·Access Group·**Contract(새로고침 일정+품질 기준, 네이티브 SLA 메커니즘)**·Context(설명·문서·SQL 템플릿·용어집) |
| Owner 관리 | Data Product Owner/Producer 역할 |
| SLA/SLO | **Contract 객체 — 새로고침 일정 + 품질 기준을 포함하는 공식 SLA 메커니즘** (조사 대상 중 가장 명시적) |
| 소비 방식 | BigQuery 직접 쿼리; **Knowledge Catalog 원격 MCP 서버** — Google Cloud 외부 앱·AI 에이전트용 도구로 데이터 Product 노출 |
| 사용 로그 | 공개 문서에 상세 미기재 |
| 다(多)시스템 연계 | Databricks Unity·AWS Glue Data Catalog·Snowflake Horizon 연합(Preview) |
| 발견·검색 | Knowledge Catalog 키워드·자연어 검색; 조직 내부 전용; Analytics Hub가 외부 교환 담당 |
| 특이사항 | Contract 객체(SLA 네이티브)와 MCP 서버(AI 에이전트 소비)가 차별점 |

**적합:** Google Cloud(BigQuery) 기반 조직이 데이터 Product에 공식 계약(Contract) 기반 SLA를 도입하고, AI 에이전트가 MCP 프로토콜로 데이터 Product를 자동 소비하길 원할 때.

---

#### 2-C6. Google Analytics Hub — 외부 데이터 교환 마켓플레이스

**공식 URL:**
- 개요: https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction
- Cloud Marketplace 연동: https://docs.cloud.google.com/bigquery/docs/analytics-hub-cloud-marketplace

**솔루션 유형:** 유형 A — 데이터 마켓플레이스(교환·상용화 모델)

> **참고:** Knowledge Catalog이 내부 거버넌스, Analytics Hub가 외부 교환·상용화를 담당. 함께 쓰는 것이 일반적.

| 기능 | 내용 |
|---|---|
| 명세서(Spec) | 리스팅 메타데이터: 설명·유스케이스·샘플 쿼리·문서 링크·연락처; 공개/비공개 Exchange 유형 |
| Owner 관리 | Publisher 조직 + 기본 연락처 이메일 |
| SLA/SLO | 전용 SLA 필드 없음 |
| 소비 방식 | Linked Dataset(제로카피·읽기전용 SQL 쿼리), Linked Pub/Sub 구독(스트리밍), ML 모델·외부 테이블·루틴 공유 |
| 사용 로그 | 프로바이더: 구독 프로젝트별 잡·행·바이트 처리량(`INFORMATION_SCHEMA.SHARED_DATASET_USAGE`); 구독자: 미지원 |
| 다(多)시스템 연계 | BigLake 연합 쿼리(S3·Azure Blob·Iceberg·Salesforce Data Cloud) |
| 발견·검색 | Google Cloud Marketplace(유료 상용화); BigQuery 인터페이스 내 내부 검색; 크로스 조직 공개 리스팅 |

**적합:** Google Cloud 기반 조직이 데이터를 외부 파트너·계열사와 제로카피로 교환하거나 상용화할 때.

---

#### 2-C7. data.world — Knowledge Graph + Marketplace (CTK)

**공식 URL:**
- 제품: https://data.world/product/knowledge-graph
- 마켓플레이스 문서: https://docs.data.world/en/375399-marketplace-preview.html
- Data Products 리소스 유형 활성화: https://docs.data.world/en/396084-enabling-the-data-products-resource-types--ctk-.html
- Marketplace 설정: https://docs.data.world/en/396082-setting-up-marketplace.html

> **중요:** 공개 data.world 커뮤니티는 2026년 7월 11일 종료(ServiceNow 인수). 엔터프라이즈/카탈로그 플랫폼은 계속 운영.

**솔루션 유형:** 유형 C — 지식 그래프 기반 카탈로그 + 마켓플레이스 레이어

| 기능 | 내용 |
|---|---|
| 명세서(Spec) | CTK 모듈 활성화 시 Data Product·Policy 2가지 리소스 유형 생성; 마켓플레이스 공개에 필요한 기본 필드 일괄 로드 |
| Owner 관리 | 지식 그래프에 소유권·비즈니스 정의·접근 정책 저장 |
| SLA/SLO | 전용 SLA 필드 없음; Policy 리소스 유형이 거버넌스 계약 요소 담당 |
| 소비 방식 | Explorer/Catalog/Marketplace/Workbench 계층별 접근; 크로스 플랫폼 SQL; 다운로드/내보내기; 자연어 SQL 생성 |
| 사용 로그 | 데이터 인기도·소유권·품질 메트릭(지식 그래프); 실시간 변경 알림; 이해관계자 인앱 알림 |
| 다(多)시스템 연계 | 15+ 플랫폼 통합(Snowflake·Databricks·PostgreSQL·Oracle·dbt·Tableau·Power BI·Looker 등); 하이브리드(클라우드+온프레미스) |
| 발견·검색 | 비즈니스 도메인별 마켓플레이스 구성; 접근 요청 워크플로우; 지식 그래프 기반 검색(기존 카탈로그 대비 4.2배 정확도 주장) |

**적합:** ServiceNow 에코시스템을 활용하며 지식 그래프 기반의 시맨틱 데이터 거버넌스가 필요한 조직. 이미 data.world 엔터프라이즈를 카탈로그로 사용 중인 경우 마켓플레이스 확장.

---

#### 2-C8. Secoda — 카탈로그 + 거버넌스 (부분 지원)

**공식 URL:** https://www.secoda.co
**비고:** 2025년 Atlassian이 인수; Rovo AI와 통합 예정; 제품명 유지

**솔루션 유형:** 유형 C (부분) — 데이터 카탈로그 + 거버넌스 플랫폼

> 데이터 Product 전용 객체 없음; 소유권·접근 요청·거버넌스 정책이 데이터 Product 프로그램을 *지원*하는 수준.

| 기능 | 내용 |
|---|---|
| Owner 관리 | 자산별 Owner 지정(카탈로그 내 표시) |
| SLA/SLO | 전용 필드 없음 |
| 소비 방식 | Data Requests Portal(거버넌스 접근 요청); AI 검색·카탈로그 |
| 사용 로그 | AI 사용 분석(워크스페이스 수준); 데이터 품질 모니터링 |
| 다(多)시스템 연계 | 20+ 플랫폼 메타데이터 수집(Snowflake·BigQuery·Redshift·dbt·Looker·Tableau 등) |
| 발견·검색 | AI 검색; 마켓플레이스 UI 없음 |

**적합:** 별도 데이터 Product 플랫폼 도입 전에 기존 카탈로그 수준에서 소유권 관리와 접근 요청 거버넌스를 시작하려는 조직. Atlassian 생태계(Jira·Confluence)와 통합이 필요한 경우.

---

#### 2-C9. Select Star — 메타데이터 거버넌스 (제한적 지원)

**공식 URL:** https://www.selectstar.com
**비고:** 2025년 Snowflake 인수 합의; 제품 운영 지속

**솔루션 유형:** 유형 C (제한적) — 데이터 카탈로그 + 사용 분석 도구

> 데이터 Product 전용 객체·마켓플레이스 없음. 주요 강점은 사용 분석(Behavioral Analysis Engine)과 리니지.

| 기능 | 내용 |
|---|---|
| Owner 관리 | 테이블·자산 수준 Owner 지정 |
| SLA/SLO | 거버넌스 벤치마크·신뢰도 기준 언급; 전용 Product SLA 없음 |
| 사용 로그 | Behavioral Analysis Engine: 자산별 이용 패턴·상위 자산·상위 사용자 추적 |
| 다(多)시스템 연계 | Snowflake·BigQuery·Redshift·dbt·BI 도구 메타데이터 수집 |
| 발견·검색 | 카탈로그·리니지 기반 검색; 마켓플레이스 없음 |

**적합:** 데이터 Product 이전 단계 — 어떤 자산이 가장 많이 쓰이는지(사용 분석)를 파악해 Product화 우선순위를 정하는 데 활용. Snowflake 인수 후 Horizon Catalog와 통합될 가능성.

---

#### 2-C10. Castor / Coalesce Catalog — 해당 기능 없음

**공식 URL:** https://www.castordoc.com (Coalesce에 인수, 2025년 3월 → https://coalesce.io/product/catalog/)

> 데이터 Product·마켓플레이스 기능 없음. dbt 중심 경량 카탈로그로 리포지셔닝. 본 Tech Stack 비교에서 제외.

---

## 3. 종합 비교표

| 솔루션 | 유형 | 명세서·Owner·SLA | 소비 방식 다양성 | 사용 로그 | 다(多)시스템 연계 | 마켓플레이스·발견 | 적합 (한 줄) |
|---|---|---|---|---|---|---|---|
| **Collibra Data Marketplace** | A | ◎명세+Owner / △SLA(품질인증 대체) | △(쇼핑UI·쿼리·API 유형) | ○(감사 추적·평점) | ○(리니지+커넥터) | ◎(AI Copilot NL검색·필터) | 엔터프라이즈 거버넌스 기반 내부 마켓플레이스 |
| **Alation Data Products Marketplace** | A→B | ◎(ODPS 표준·인증·버전) / △SLA | ◎(UI·NL챗·AI에이전트 ODPS) | ○(방문수·사용통계) | ○(100+ 커넥터) | ◎(인증 마켓플레이스·AI빌더) | ODPS 표준+AI에이전트 소비 |
| **Informatica Cloud Data Marketplace** | A | ○(컬렉션 명세+Owner) / △SLA | ○(요청→자동 프로비저닝) | ◎(소비 대시보드·수요 시그널) | ○(IDMC 커넥터) | ○(쇼핑카트·리뷰·신규 요청) | Informatica 기반 조직의 완성형 마켓플레이스 |
| **Databricks (Unity Catalog + Marketplace)** | B | ○명세+OWNERSHIP / △SLA | ◎(테이블·스트림·모델·MCP·앱) | ○(감사 시스템테이블·프로바이더 대시보드) | ◎(OpenSharing 크로스클라우드) | ○(공개+Private Exchange) | Databricks 기반 오픈 공유 프로토콜 |
| **Snowflake (Horizon + Marketplace)** | B | ○명세+OWNERSHIP / △SLA(계약기간) | ◎(SQL·뷰·앱·ML·UDF·Native App) | ○(Usage스키마·인기순위) | ◎(Horizon 크로스엔진) | ◎(820+ 프로바이더·내부+공개) | 상용화 포함 완성형 마켓플레이스 |
| **Microsoft Fabric OneLake** | B | △(워크스페이스=Product 관례) / △SLA | ○(SQL·Semantic Model·파일·API) | ○(Monitoring Hub·Purview Audit) | ◎(170+ 커넥터·Shortcut) | △(내부 카탈로그만) | Fabric 기반 셀프서비스 플랫폼 (Purview 병용 권장) |
| **Nextdata OS** ⚠️초기 | B | ◎(데이터 계약·Policies-as-Code) / ◎SLA | ◎(테이블·벡터·파일·MCP) | ◎(실시간 대시보드·AI에이전트 포함) | ○(플러그인 드라이버) | ○(자동 자가발행·시맨틱 검색) | 데이터 메시 네이티브 자율 Product OS (초기 단계) |
| **Atlan Data Products Marketplace** | A/C | ◎(계약 연결·12개 상태·필드 풍부) / ○SLA(계약 레이어) | ◎(Output Port·MCP·Teams·SQL) | ◎(Product별 뷰·방문자·트렌드) | ◎(200+ 커넥터·크로스도메인) | ◎(마켓플레이스 UI·NL·Zero-Touch) | 가장 완성된 카탈로그 내장 마켓플레이스 |
| **DataHub OSS** | C | ○(엔티티 명세·Owner·Contract) / ○SLA(FreshnessAssertion) | △(API·SDK·CLI 중심, UI 마켓플레이스 없음) | △(데이터셋 수준; Product 수준은 로드맵) | ○(240+ 수집 커넥터) | △(카탈로그 검색만) | OSS 거버넌스 구조화; 기술팀 직접 구현 |
| **MS Purview Unified Catalog** | C | ◎(12유형·커스텀 속성·Endorsed) / △SLA(품질점수 대체) | △(요청→원천 자산 직접 접근) | △(구독자수·관찰성 Preview) | ◎(Purview 스캔 전 원천) | ○(NL검색·Endorsed 필터; 내부만) | Azure/Fabric 생태계 데이터 Product 거버넌스 |
| **Google Knowledge Catalog** | C | ◎(Contract 객체 = 네이티브 SLA) / ◎SLA | ○(BigQuery·MCP 서버) | △(미문서화) | ○(Databricks·Glue·Snowflake 연합 Preview) | △(내부 NL검색; 외부는 Analytics Hub) | Google Cloud SLA+MCP 기반 AI 에이전트 소비 |
| **Google Analytics Hub** | A | △(리스팅 명세; SLA 없음) | ○(제로카피 SQL·스트림·ML모델) | ○(INFORMATION_SCHEMA 사용량) | ○(BigLake 연합) | ○(Cloud Marketplace 상용화) | GCP 외부 데이터 교환·상용화 |
| **data.world (Enterprise)** | C | ○(CTK 리소스 유형·Policy) / △SLA | ○(계층별 접근·크로스소스 SQL) | ○(지식 그래프 인기도·알림) | ○(15+ 플랫폼·하이브리드) | ○(도메인별 마켓플레이스·접근 요청) | ServiceNow 생태계·지식 그래프 기반 거버넌스 |
| **Secoda** | C(부분) | △(Owner O / SLA X) | △(접근 요청 포털) | △(워크스페이스 수준) | ○(20+ 메타데이터 수집) | △(AI 검색; 마켓플레이스 없음) | 마켓플레이스 도입 전 카탈로그+접근 거버넌스 |
| **Select Star** | C(제한) | △(Owner O / SLA 없음) | ✕ | ○(Behavioral Analysis) | ○(Snowflake·BQ 등) | △(카탈로그 검색만) | Product화 우선순위 파악용 사용 분석 |
| **Castor/Coalesce Catalog** | — | ✕ | ✕ | ✕ | △(dbt 중심) | △(NL검색) | 해당 없음 — dbt 카탈로그 도구 |

> 범례: ◎ 강점·충분 / ○ 지원 / △ 부분/제한 / ✕ 없음

---

## 4. 선정 기준 체크리스트

데이터 Product화 솔루션을 도입하기 전 아래 항목을 확인한다.

```
[ ] 1. 데이터 Product 객체가 1등급(first-class)으로 존재하는가?
       → Purview, Atlan, Alation, Knowledge Catalog: ◎ / DataHub OSS: ○ / Fabric: △(관례)

[ ] 2. Owner·Spec 필드가 구조화되어 있는가?
       → Purview, Atlan, Alation: 필드 수·커스텀 속성이 가장 풍부

[ ] 3. SLA/데이터 계약(Contract)을 공식 객체로 지원하는가?
       → Google Knowledge Catalog: Contract 네이티브 ◎ / DataHub: FreshnessAssertion ○ / 나머지: △(대체)

[ ] 4. 비기술 소비자가 쓸 수 있는 마켓플레이스 UI가 있는가?
       → Atlan, Alation, Collibra, Informatica, Snowflake, Databricks: ◎ / DataHub OSS: ✕

[ ] 5. 소비 방식 다양성 — 테이블 외에 AI(RAG·벡터·MCP)를 지원하는가?
       → Nextdata OS: ◎ / Atlan(MCP), Databricks(MCP 리스팅), Google Knowledge Catalog(MCP 서버): ○

[ ] 6. Product별 사용 로그(뷰 수·소비 패턴)가 있는가?
       → Atlan(방문자 트렌드), Informatica(소비 대시보드), Nextdata: ◎ / 나머지: ○↓

[ ] 7. 현재 데이터 플랫폼과 연계되는가?
       → 기존 플랫폼(Databricks/Snowflake/Azure/GCP)의 네이티브 솔루션 우선 검토

[ ] 8. 오픈소스 또는 벤더 중립 표준을 지원하는가?
       → DataHub OSS: ◎ / Alation(ODPS 표준): ○ / Databricks(OpenSharing/Iceberg): ○

[ ] 9. 계열사 간 크로스 조직 공유(제로카피)를 지원하는가?
       → Snowflake(Data Sharing), Databricks(Delta Sharing/OpenSharing), Analytics Hub: ◎

[ ] 10. 초기 단계 솔루션인가? (GA 여부, 레퍼런스 사례 수)
        → Nextdata OS: 초기 ⚠️ / Google Knowledge Catalog Data Products: 2026년 5월 GA(최신)
```

---

## 5. 참고자료 (공식 URL 검증 목록)

| 솔루션 | 확인된 공식 URL |
|---|---|
| Collibra Data Marketplace | https://www.collibra.com/products/data-marketplace |
| Alation Data Products Marketplace | https://www.alation.com/product/data-products-marketplace/ |
| Alation Data Products Builder Agent | https://www.alation.com/product/data-products-builder-agent/ |
| Informatica Cloud Data Marketplace | https://www.informatica.com/products/data-governance/cloud-data-marketplace.html |
| Databricks Unity Catalog | https://www.databricks.com/product/unity-catalog |
| Databricks Marketplace | https://www.databricks.com/product/marketplace |
| Databricks Marketplace 브라우저 | https://marketplace.databricks.com |
| Databricks Delta Sharing 문서 | https://docs.databricks.com/en/delta-sharing/index.html |
| Snowflake Marketplace | https://www.snowflake.com/en/data-cloud/marketplace/ |
| Snowflake Horizon Catalog | https://www.snowflake.com/en/product/features/horizon/ |
| Snowflake Data Sharing 문서 | https://docs.snowflake.com/en/user-guide/data-sharing-intro |
| Microsoft Fabric OneLake Catalog | https://learn.microsoft.com/en-us/fabric/governance/onelake-catalog-overview |
| Microsoft Purview Data Products | https://learn.microsoft.com/en-us/purview/unified-catalog-data-products |
| Informatica 마켓플레이스 기능 아티클 | https://www.informatica.com/resources/articles/data-marketplace-benefits-and-features.html |
| Google Analytics Hub | https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction |
| Google Knowledge Catalog | https://cloud.google.com/products/knowledge-catalog |
| Google Knowledge Catalog Data Products 문서 | https://docs.cloud.google.com/dataplex/docs/data-products-overview |
| Google Data Products GA 블로그 | https://cloud.google.com/blog/products/data-analytics/introducing-data-products-in-dataplex-universal-catalog |
| Atlan Data Products Marketplace | https://atlan.com/data-products-marketplace/ |
| Atlan 문서 (Data Products) | https://docs.atlan.com/product/capabilities/data-products/concepts/what-are-data-products |
| DataHub 프로젝트 | https://datahubproject.io (→ https://datahub.com) |
| DataHub Data Products 문서 | https://docs.datahub.com/docs/dataproducts/ |
| data.world 엔터프라이즈 | https://data.world/product/knowledge-graph |
| data.world Marketplace 문서 | https://docs.data.world/en/375399-marketplace-preview.html |
| data.world Data Products CTK | https://docs.data.world/en/396084-enabling-the-data-products-resource-types--ctk-.html |
| Nextdata OS 공식 | https://www.nextdata.com |
| Nextdata OS 제품 페이지 | https://www.nextdata.com/product |
| Secoda | https://www.secoda.co |
| Select Star | https://www.selectstar.com |
| Castor → Coalesce Catalog | https://www.castordoc.com / https://coalesce.io/product/catalog/ |

---

*이 노트는 E-1 가이드 솔루션 섹션의 초안 근거 자료다. 최종 가이드 작성 전 주요 수치·에디션 정보는 PoC/공식 견적을 통해 재확인한다.*
