# E-1 데이터 Product화 — 개념 리서치 노트

> **용도:** 가이드 작성자를 위한 원자료. 최종 가이드 문서가 아님.  
> **작성일:** 2026-06-24  
> **렌즈:** "AI·여러 팀이 재사용할 데이터를 준비·정비하는 법" — AI 모델·RAG·에이전트 구축법 아님.

---

## 목차
- [A. 개념·기원 — Data as a Product 원칙](#a-개념기원)
- [B. 데이터 Product 구성요소·명세](#b-데이터-product-구성요소명세)
- [C. Product Owner 역할](#c-product-owner-역할)
- [D. Self-Serve 플랫폼 · 멀티 시스템 제공](#d-self-serve-플랫폼--멀티-시스템-제공)
- [E. 데이터 계약(Data Contract)과의 관계](#e-데이터-계약data-contract과의-관계)
- [5 Key Question 답변 재료](#5-key-question-답변-재료)
- [제조·두산 맥락 예시 소재](#제조두산-맥락-예시-소재)
- [참고 URL 목록](#참고-url-목록)

---

## A. 개념·기원

### Data Mesh 4원칙 중 두 번째: "Data as a Product"

Zhamak Dehghani(ThoughtWorks)가 2019년 최초 제안하고, 2022년 O'Reilly 책 *Data Mesh: Delivering Data-Driven Value at Scale*으로 정립한 개념.

> **Data Mesh 4원칙:**  
> 1. 도메인 중심 분산 소유권(Domain-oriented decentralized ownership)  
> 2. **데이터를 Product로(Data as a Product)** ← E-1의 핵심  
> 3. 셀프서비스 데이터 인프라(Self-serve data infrastructure)  
> 4. 연합적 거버넌스(Federated computational governance)

출처: [martinfowler.com/articles/data-mesh-principles.html](https://martinfowler.com/articles/data-mesh-principles.html)

### "Data as a Product"란 무엇인가

- **핵심 전환:** 분석 데이터를 "제공하면 그만인 파일/보고서"가 아니라, 소비 고객(다른 도메인·팀·AI)이 만족할 때까지 지속 책임지는 **상품(Product)**으로 취급.
- Dehghani 직접 인용: *"Analytical data provided by domains must be treated as a product, and the consumers of that data should be treated as customers — happy and delighted customers."*
- **도메인팀이 품질 책임을 진다:** 전통 방식은 중앙 데이터팀이 수동으로 파이프라인을 짜주는 구조였지만, Data as a Product는 **데이터 품질 책임을 원천(소스)에 최대한 가까이** 이관한다.

출처: [martinfowler.com/articles/data-mesh-principles.html](https://martinfowler.com/articles/data-mesh-principles.html), [Thoughtworks 설명](https://www.thoughtworks.com/en-us/insights/e-books/modern-data-engineering-playbook/data-as-a-product)

### 데이터 Product vs. 일회성 데이터셋/보고서

| 구분 | 일회성 데이터셋/보고서 | 데이터 Product |
|------|----------------------|----------------|
| 생명주기 | 납품 후 종료 | Owner가 지속 운영·유지 |
| 품질 보장 | 없음 | SLO/SLA 명시 |
| 소비 방식 | 단일 용도 | 다수 팀·AI가 반복 재사용 |
| 발견 가능성 | 없음(요청해야) | 카탈로그 등록·검색 가능 |
| 변경 관리 | 없음 | 버전 관리·소비자 공지 |

출처: [dbt Labs — Data products vs. data as a product](https://www.getdbt.com/blog/data-product-data-as-product), [Thoughtworks](https://www.thoughtworks.com/en-us/insights/e-books/modern-data-engineering-playbook/data-as-a-product)

### 데이터 Product의 세 가지 유형 분류

datamesh-architecture.com에 따르면:
1. **Source-aligned(소스 정렬형):** 운영 시스템의 도메인 이벤트·엔티티를 그대로 노출. 예: 설비 가동 이벤트 Product.
2. **Aggregate(집계형):** 여러 도메인 데이터를 통합·집계. 예: 전사 수율(Yield) 360° 뷰.
3. **Consumer-aligned(소비자 정렬형):** 특정 부서/목적에 최적화된 모델. 예: 생산관리팀 전용 KPI 대시보드 소스 Product.

출처: [datamesh-architecture.com](https://www.datamesh-architecture.com/)

---

## B. 데이터 Product 구성요소·명세

### 핵심 정의 (datamesh-manager.com)

> "A data product is a logical unit that contains all components to process and store domain data for analytical or data-intensive use cases and **makes them available to other teams via output ports**."

출처: [datamesh-manager.com/learn/what-is-a-data-product](https://www.datamesh-manager.com/learn/what-is-a-data-product)

### Data Product Canvas — 8개 구성 블록

datamesh-architecture.com의 Data Product Canvas 기준:

1. **Domain(도메인):** 책임 팀·담당자·유지보수 주체
2. **Data Product Name(명칭):** 조직 내 유일한 식별자, 명명 규칙 적용
3. **Consumer & Use Case(소비자·사용 목적):** 어느 팀이 무슨 분석/목적으로 쓰는가
4. **Data Contract(데이터 계약):** Output Port 형식·소비 프로토콜·데이터 모델(속성·타입·제약·의미)·이용 조건
5. **Sources(소스/Input Ports):** 운영 시스템 또는 다른 데이터 Product로부터 데이터를 받는 방식
6. **Data Product Architecture(내부 아키텍처):** Input→Output 사이의 수집·저장·변환·강화·분석 처리
7. **Ubiquitous Language(공통 언어):** 이해관계자 전반이 공유하는 도메인 용어 정의
8. **Classification(분류):** Source-aligned / Aggregate / Consumer-aligned 중 하나

출처: [datamesh-architecture.com/data-product-canvas](https://www.datamesh-architecture.com/data-product-canvas)

### 기술 구성요소 상세 (datamesh-manager.com)

| 구성요소 | 설명 |
|---------|------|
| **Output Ports** | SQL 뷰·파일·스트리밍 토픽 등 읽기 전용 인터페이스. 동일 데이터를 다른 형식·접근권한으로 여러 포트 제공 가능 |
| **Input Ports** | 운영 시스템(도메인 이벤트) 또는 다른 Product로부터의 데이터 소스 |
| **Discovery Port** | 카탈로그에 메타데이터 발행(의미·담당자 연락처·성숙도·품질 지표·서비스 목표) |
| **Transformation Code** | 데이터 정제·집계용 SQL/Spark 파이프라인 (Airflow 등으로 오케스트레이션) |
| **Data Storage** | 컬럼 지향 기술 등으로 격리된 전용 저장소 |
| **Tests** | 변환 로직 단위테스트·배포 시 기대값 검증·지속 품질 모니터링 |
| **Documentation** | 데이터 의미·비즈니스 맥락·예시 쿼리가 담긴 문서 |
| **CI/CD Pipeline** | 자동 배포·테스트·정책 준수 검사 |
| **Observability** | 모니터링·로깅·관리 포트 |
| **Policies as Code** | 명명 규칙·분류·접근 제어 도메인별 구현 |

출처: [datamesh-manager.com/learn/what-is-a-data-product](https://www.datamesh-manager.com/learn/what-is-a-data-product)

### martinfowler.com 3요소 모델

martinfowler.com은 데이터 Product를 **"아키텍처적 양자(Architectural Quantum)"**로 정의하며 3요소로 구성:

1. **Code:** 데이터 파이프라인·API·접근 제어 코드
2. **Data & Metadata:** 분석용 이력 데이터(이벤트·파일·관계형·그래프) + 메타데이터(스키마·품질 지표)
3. **Infrastructure:** 코드 빌드·배포·실행·모니터링·저장·접근 인프라

출처: [martinfowler.com/articles/data-mesh-principles.html](https://martinfowler.com/articles/data-mesh-principles.html)

### USABLE 품질 특성 (Thoughtworks 5대 속성)

데이터 Product가 갖춰야 할 품질:
1. **Discoverable(발견 가능):** 카탈로그에 메타데이터 등록
2. **Addressable(주소 지정 가능):** 안정적 URI/포트로 접근
3. **Self-describing(자기 설명적):** 투명한 스키마·계보(Lineage)
4. **Trustworthy(신뢰 가능):** SLO(서비스 수준 목표) 가시화
5. **Secure(보안):** 연합적 접근 제어

출처: [Thoughtworks data-as-a-product](https://www.thoughtworks.com/en-us/insights/e-books/modern-data-engineering-playbook/data-as-a-product)

### Open Data Product Specification (ODPS)

Linux Foundation이 관리하는 오픈 표준(YAML 기반). 데이터 Product를 기계 가독 방식으로 명세.

**ODPS 2.0 주요 섹션:**
- **Product:** name, productID, visibility, status, type, valueProposition, version, tags, useCases
- **Pricing Plans:** priceCurrency, billingDuration, unit, offering (내부 사용 시 open/free)
- **DataOps:** platform, storageTechnology, storageType, schemaLocationURL, dataLineageTool
- **Data Access:** outputPorttype(API·SQL·SFTP·gRPC), authenticationMethod, format
- **Data SLA:** updateFrequency, uptime, responseTime, support channels, logsURL, dashboardURL
- **License:** scope, privacy(개인정보), termination, governance
- **Data Holder:** legalName, businessID, email

출처: [opendataproducts.org/v2.0/](https://opendataproducts.org/v2.0/)

ODPS는 OpenSLO(SLO 정의), Soda Core(품질 규칙), Schema.org(메타데이터)와 통합됨.

### Open Data Mesh — Data Product Descriptor Specification (DPDS)

오픈 데이터 메시 이니셔티브(agile-lab-dev)의 사양. 5가지 포트 유형 정의:

1. **Input Ports:** 소스 데이터 수집(Push/Pull)
2. **Output Ports:** 신뢰·이해 가능한 형식으로 데이터 공유
3. **Discovery Ports:** 정적 아키텍처 정보(목적·구조·위치) 제공
4. **Observability Ports:** 동적 행동 정보(로그·트레이스·메트릭·감사 추적)
5. **Control Ports:** 로컬 정책 설정·거버넌스 운영

출처: [dpds.opendatamesh.org/concepts/data-product-descriptor/](https://dpds.opendatamesh.org/concepts/data-product-descriptor/)

### 데이터 Product 5가지 유형 (Alation 분류)

1. **Analytic Data Products:** 대시보드·탐색용 큐레이션 데이터셋 — 반복 쿼리 대상에 적합
2. **Operational Data Pipelines:** 다수 소스→거버넌스된 출력 자동화 워크플로우 — 실시간 SLA 필요 시
3. **Machine Learning Models:** 예측·점수·추천 제공하는 패키지 모델 — AI 소비 대상
4. **Data APIs:** 앱·AI 에이전트가 직접 통합하는 표준 엔드포인트
5. **Embedded Insights:** 업무 워크플로우에 직접 내장된 시각화·인사이트

출처: [alation.com/blog/data-product-types/](https://www.alation.com/blog/data-product-types/)

---

## C. Product Owner 역할

### Owner 핵심 책임

ovaledge.com, atlan.com, datamesh 문헌 종합:

| 책임 영역 | 세부 내용 |
|---------|---------|
| **품질 유지** | 데이터 신선도·정확도·완전성 모니터링; SLA 준수 여부 추적 |
| **소비자 대응** | 사용 문의·피드백 수집·지원 요청 처리 |
| **변경 공지** | 스키마·SLA 변경 시 소비팀에 사전 공지; 버전업 이력 유지 |
| **개선 백로그** | 채택률·피드백 기반 개선 우선순위 관리 |
| **버전·폐기 결정** | 버전 정책(하위호환성 규칙) 수립; 폐기 예고 기간 설정 후 마이그레이션 지원 |
| **접근 거버넌스** | 이용 조건 정의·접근 승인·감사 |
| **비용 추적** | 사용량·비용 투명 공개(소비자 과금 모델 지원) |

출처: [ovaledge.com/blog/data-product-strategy-guide](https://www.ovaledge.com/blog/data-product-strategy-guide), [atlan.com/know/data-product-lifecycle/](https://atlan.com/know/data-product-lifecycle/)

### 버전 관리 및 폐기(Deprecation) 정책

우수 사례(ovaledge.com 기준):
- **하위 호환성 규칙 명시:** 필드 deprecated → optional → removed 순으로 단계적 처리
- **소비자에게 최소 1 릴리스 사이클** 이상의 전환 기간 제공
- **폐기 공지 → 마이그레이션 지원 → 자산 아카이브 → 접근 권한 회수 → 리니지 정리** 순으로 실행

폐기 트리거:
- 낮은 사용량 추세
- 다른 Product와 중복
- 소스 시스템 변경으로 신뢰성 저하
- 규정 준수 위험 증가

출처: [ovaledge.com/blog/data-product-strategy-guide](https://www.ovaledge.com/blog/data-product-strategy-guide)

### 데이터 Product 라이프사이클 6단계

atlan.com 기준:

```
요구사항 수집 → 설계 → 개발 → 운영 → 개선 → 폐기
(Discovery) (Design) (Dev) (Ops) (Iteration) (Deprecation)
```

출처: [atlan.com/know/data-product-lifecycle/](https://atlan.com/know/data-product-lifecycle/)

ovaledge.com은 동일 흐름을 6단계로:  
발견(Discovery) → 설계(Design) → 출시(Delivery) → 채택(Adoption) → 개선(Improvement) → 은퇴(Retirement)

출처: [ovaledge.com/blog/data-product-strategy-guide](https://www.ovaledge.com/blog/data-product-strategy-guide)

### 성과 지표 (KPI)

- **채택률:** 의도한 소비팀이 실제로 사용하는가
- **인사이트 도달 시간(Time-to-insight):** 소비자가 필요한 답을 얻는 데 걸리는 시간
- **의사결정 영향:** 비즈니스 프로세스 정확도·속도 개선 여부
- **효율 개선:** 수동 작업·다운스트림 오류 감소
- **SLA 준수율:** 약속한 uptime·freshness 달성 비율
- **사용자 만족도:** 피드백·스테이크홀더 참여 수준

출처: [ovaledge.com/blog/data-product-strategy-guide](https://www.ovaledge.com/blog/data-product-strategy-guide), [atlan.com/know/data-product-lifecycle/](https://atlan.com/know/data-product-lifecycle/)

---

## D. Self-Serve 플랫폼 · 멀티 시스템 제공

### 자기서비스 데이터 플랫폼 3계층

martinfowler.com 기준 논리 아키텍처:

```
1. 데이터 인프라 유틸리티 플레인 (Data Infrastructure Utility Plane)
   — 스토리지·컴퓨팅·네트워크 등 기반 인프라 추상화
2. 데이터 Product 경험 플레인 (Data Product Experience Plane)
   — Product 생성·모니터링·발견·접근 지원
3. 메시 경험 플레인 (Mesh Experience Plane)
   — 도메인 간 교차 조회·정책 자동화·거버넌스 운영
```

출처: [martinfowler.com/articles/data-mesh-principles.html](https://martinfowler.com/articles/data-mesh-principles.html)

### 이질적 소스 시스템에서 균일한 Product 제공

핵심 원리: **추상화 레이어(Abstraction Layer)**가 각기 다른 소스 시스템(ERP·MES·SCADA·PLM 등) 위에 올라가서, 소비자는 **동일한 Output Port** 형식(SQL·API·File)으로 데이터를 받는다.

구체적 메커니즘 (Enterprise Data Marketplace 특허·arxiv 논문 종합):
- **데이터 추상화 레이어:** 이기종 보고서·데이터 추출물을 REST API 형태의 가상 뷰(Virtual View)로 노출
- **표준화된 추상화 인터페이스:** 검색·모니터링·제어·변환·등록·배포에 대한 표준 추상화 제공 → 도메인팀이 전문가 없이도 Product를 빠르게 만들고 소비 가능
- **모델 계약(Model Contract):** 소비자에 대한 약속을 정의하고, 데이터 변환 레이어와 데이터 접근 API 생성을 지원

출처: [arxiv.org/pdf/2402.04681](https://arxiv.org/pdf/2402.04681) (Architectural Design Decisions for Self-Serve Data Platforms in Data Meshes), [martinfowler.com/articles/data-mesh-principles.html](https://martinfowler.com/articles/data-mesh-principles.html)

### 플랫폼이 제공해야 할 역량

datamesh-architecture.com 기준:

**분석 역량:** 데이터 수집·저장·쿼리·시각화를 셀프서비스로(도메인팀별 격리 인프라)

**데이터 Product 역량(고급):**
- Product 생성·모니터링·발견·접근 지원
- 크로스 도메인 접근 지원
- 정책 자동화
- 대규모 크로스 도메인 조인 쿼리 엔진

출처: [datamesh-architecture.com](https://www.datamesh-architecture.com/)

### 데이터 Product 마켓플레이스(Marketplace)

- 엔터프라이즈 데이터 마켓플레이스(EDM): 데이터 자산의 가상·물리적 허브 역할을 하는 셀프서비스 웹 앱
- 소비자가 "쇼핑"하듯 필요한 Product를 검색·구독·소비
- 중복 제거·비용 절감·재사용 촉진

출처: [USPTO 특허 문서 기반 — 공식 제품명은 PoC 확인 권장](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12307506)

---

## E. 데이터 계약(Data Contract)과의 관계

### 핵심 관계: "데이터 Product가 품질 보증서, 데이터 계약은 그 품질 약속의 문서"

Jean-Georges Perrin(Data Mesh Learning) 정의:
- **데이터 Product:** 재사용 가능한 능동적·표준화된 데이터 자산. 여러 데이터 아티팩트(데이터셋·모델·파이프라인) + Output Port + **각 Output Port당 1개의 데이터 계약**을 포함.
- **데이터 계약:** 데이터 생산자와 소비자 사이의 공식 합의. 스키마·품질·의미·가용성 기대치를 정의.

> "Data contracts guarantee that your data product is behaving in the expected way."

**"Output Port 당 1개의 데이터 계약"** 원칙:
- 각 Output Port는 자신만의 데이터 계약을 가짐
- 계약이 소비자가 의존할 수 있는 신뢰성 보장을 설정

출처: [medium.com/data-mesh-learning — Data Product vs. Data Contract](https://medium.com/data-mesh-learning/data-product-vs-data-contract-whats-the-difference-d39e82cf8ed3)

### 데이터 계약 vs. 데이터 Product 명세의 차이

Andrea Gioia(Agile Lab):
- **데이터 계약 명세:** 데이터 자산의 *구조*와 연관 메타데이터 정의에 집중
- **데이터 Product 명세:** 데이터 Product가 데이터 자산을 어떻게 *관리·노출·서비스하는지* 정의

즉, 계약은 Product의 Output Port 인터페이스 약속이고, Product 명세는 그 약속을 이행하는 전체 체계를 정의한다.

출처: [medium.com/@andrea_gioia — Data Contract vs. Data Product Specifications](https://medium.com/@andrea_gioia/data-contract-vs-data-product-specifications-8ffa3cc16725)

### DPDS에서의 관계

Open Data Mesh DPDS:
- 각 포트 요소에 **사용 중인 데이터 계약 정의에 대한 참조(reference)** 를 커스텀 프로퍼티로 포함 가능
- 즉 Product Descriptor가 Data Contract를 **참조·포함**하는 구조

출처: [dpds.opendatamesh.org/concepts/data-product-descriptor/](https://dpds.opendatamesh.org/concepts/data-product-descriptor/)

---

## 5 Key Question 답변 재료

### KQ1 — 어떤 데이터를 Product화할 것인가?

**우선순위 판단 기준 (ovaledge.com + 일반 문헌 종합):**

| 기준 | 설명 |
|-----|------|
| **반복 요청 빈도** | 여러 팀이 같은 데이터를 반복 요청하는가 → 높을수록 우선 |
| **소비 팀 수** | 몇 개 팀·AI 태스크가 동일 데이터를 사용하는가 → 많을수록 우선 |
| **중복 제거 효과** | 각 팀이 독자 집계→오류 발생 → Product화로 단일 정본 제공 효과 |
| **비즈니스 영향도** | 핵심 의사결정에 직결되는가 |
| **기술적 준비도** | 현재 데이터 품질·가용성이 Product화하기에 충분한가 |
| **AI 태스크 사용** | AI 모델·에이전트가 반복 소비할 데이터인가 |

**우선순위 매트릭스:**
- 높은 비즈니스 영향 + 높은 기술 준비도 = 즉시 Product화 (Quick Win)
- 높은 영향 + 낮은 준비도 = 전략적 투자
- 낮은 영향 + 높은 준비도 = 나중으로 미룸
- 낮은 영향 + 낮은 준비도 = 아카이브 또는 무시

출처: [ovaledge.com/blog/data-product-strategy-guide](https://www.ovaledge.com/blog/data-product-strategy-guide)

### KQ2 — 데이터 Product의 구성요소는 무엇인가?

**Product 명세서(Data Product Canvas/Spec) 핵심 항목:**

| 항목 | 내용 |
|-----|------|
| 대상 소비자 | 어느 팀·역할이 소비하는가 |
| 제공 데이터 | 어떤 데이터를 담는가 (스키마·데이터 모델) |
| 목적·사용 목적 | 어떤 분석/의사결정에 쓰이는가 |
| 품질 기준 | 정확도·완전성·일관성·적시성 기준(%) |
| 갱신 주기 | 실시간·시간별·일별·주별 등 |
| SLA | 가용성·응답시간·지연시간 약속 |
| Owner | 책임자(팀·개인)·연락처 |
| 이용 조건 | 접근 방법·라이선스·개인정보 처리 |
| 예시 쿼리 | 소비자가 바로 써볼 수 있는 예시 |
| 제공 방식 | Output Port 유형(SQL·파일·API·스트림·대시보드) |

출처: [datamesh-architecture.com/data-product-canvas](https://www.datamesh-architecture.com/data-product-canvas), [opendataproducts.org/v2.0/](https://opendataproducts.org/v2.0/)

### KQ3 — 이질적 솔루션 환경에서 표준 Product를 어떻게 제공하는가?

**핵심 답변:** Self-Serve 데이터 플랫폼이 제공하는 **추상화 레이어**가 각 소스 시스템(ERP·MES·SCADA 등)의 차이를 감추고, 소비자에게는 동일한 Output Port(SQL 뷰·REST API·파일) 형식으로 노출.

메커니즘:
1. 도메인팀이 자기 소스 시스템에서 데이터를 가져와 Product로 변환·관리
2. 소비자는 어떤 소스 시스템에서 왔는지 알 필요 없이 Output Port로 소비
3. 플랫폼은 표준 인터페이스(검색·모니터링·접근·배포)를 제공해 Product 개발·소비를 단순화

출처: [martinfowler.com/articles/data-mesh-principles.html](https://martinfowler.com/articles/data-mesh-principles.html), [arxiv.org/pdf/2402.04681](https://arxiv.org/pdf/2402.04681)

### KQ4 — 소비자는 데이터 Product를 어떻게 소비하는가?

**Output Port 유형 (소비 방식):**

| 유형 | 설명 | 제조 적용 예 |
|-----|------|-------------|
| **SQL / DB 테이블** | SQL 뷰로 직접 쿼리 | 월별 수율 테이블 → 분석팀 쿼리 |
| **파일(File)** | CSV·Parquet·JSON 등 배치 파일 | 품질성적서 일괄 다운로드 |
| **API** | REST/gRPC 엔드포인트 | 실시간 설비 가동률 조회 API |
| **스트리밍** | Kafka 토픽·이벤트 스트림 | 설비 이상 이벤트 실시간 수신 |
| **대시보드** | 임베디드 시각화 | 생산관리 대시보드 직접 통합 |
| **RAG 소스** | AI/LLM의 지식 기반 소스 | 품질 기준서 Product → AI 에이전트 조회 |
| **Analytics Package** | 분석 노트북·ML Feature Store | AI 학습용 Feature Product |

출처: [datamesh-architecture.com/data-product-canvas](https://www.datamesh-architecture.com/data-product-canvas), [alation.com/blog/data-product-types/](https://www.alation.com/blog/data-product-types/), [opendataproducts.org/v2.0/](https://opendataproducts.org/v2.0/)

### KQ5 — Product Owner는 무엇을 책임지나?

(섹션 C에서 상세 기술. 요약:)
- **품질 유지:** 갱신·정확도·완전성·SLA 준수 모니터링
- **변경 공지:** 스키마·SLA 변경 시 사전 소비자 공지, 버전 이력 유지
- **사용자 문의 대응:** 질문·피드백·지원 요청 처리
- **개선 백로그:** 채택률·피드백 기반 개선 우선순위 관리
- **버전·폐기 결정:** 하위호환성 정책 수립, 폐기 예고 및 마이그레이션 지원

출처: [ovaledge.com/blog/data-product-strategy-guide](https://www.ovaledge.com/blog/data-product-strategy-guide), [atlan.com/know/data-product-lifecycle/](https://atlan.com/know/data-product-lifecycle/)

---

## 제조·두산 맥락 예시 소재

아래 예시는 가이드 작성 시 구체화할 소재 (실제 두산 수치는 확인 필요):

### 예시 데이터 Product 후보

| Product명 | 소비 팀 | 갱신 주기 | Output Port 예시 |
|-----------|--------|----------|----------------|
| **월별 수율(Yield) Product** | 생산관리·품질·AI 학습팀·경영기획 | 월별(배치) | SQL 뷰 + 파일 |
| **설비 가동률(OEE) Product** | 설비관리·생산계획·예지보전 AI | 시간별(실시간 近) | SQL + API |
| **품질 성적서 Product** | 품질·고객서비스·규제 대응·RAG AI | 건별(이벤트) | 파일 + RAG 소스 |
| **불량 유형 집계 Product** | 품질·설계·AI 분류 모델 | 일별 | SQL + Analytics Package |
| **납기 실적 Product** | SCM·영업·경영기획 | 주별 | SQL + 대시보드 임베드 |

### 제조 맥락에서 "일회성 데이터" vs "Product화" 구분

**일회성(현재 관행):** 영업팀이 "이번 달 A제품 수율"을 요청 → 데이터팀이 수작업으로 MES 쿼리 후 Excel 제공 → 품질팀이 같은 데이터를 다시 요청 → 두 팀이 다른 집계 기준으로 숫자가 다름.

**Product화(목표):** "월별 수율 Product"를 한번 정의(집계 기준·갱신 주기·Owner 명시) → 영업·품질·AI 학습 모두 동일 SQL 뷰 소비 → 숫자 불일치 제거, 중복 집계 작업 제거.

### OEE 배경 지식 (⚠️ 일반 제조 상식, 두산 확인 불필요)

OEE(Overall Equipment Effectiveness) = 가용성(Availability) × 성능(Performance) × 품질(Quality). 제조 현장에서 설비 효율을 측정하는 핵심 지표로, 생산관리·설비관리·AI 예지보전 등 다수 팀이 동일 데이터를 소비하는 대표적 "Product화 후보 데이터".

출처: [factbird.com/blog/quick-guide-to-oee](https://www.factbird.com/blog/quick-guide-to-oee)

---

## 참고 URL 목록

| 출처 | URL | 신뢰도 |
|-----|-----|--------|
| Data Mesh 원칙 (Zhamak Dehghani / martinfowler) | https://martinfowler.com/articles/data-mesh-principles.html | ★★★ 1차 권위 |
| Data Mesh Architecture (datamesh-architecture.com) | https://www.datamesh-architecture.com/ | ★★★ 커뮤니티 표준 |
| Data Product Canvas | https://www.datamesh-architecture.com/data-product-canvas | ★★★ |
| Data Mesh Manager — What is a Data Product | https://www.datamesh-manager.com/learn/what-is-a-data-product | ★★★ |
| Open Data Product Specification (ODPS) v2.0 | https://opendataproducts.org/v2.0/ | ★★★ Linux Foundation 오픈 표준 |
| ODPS v3.1 | https://opendataproducts.org/v3.1/ | ★★★ |
| Open Data Mesh Product Descriptor (DPDS) | https://dpds.opendatamesh.org/concepts/data-product-descriptor/ | ★★★ |
| Thoughtworks — Data as a Product | https://www.thoughtworks.com/en-us/insights/e-books/modern-data-engineering-playbook/data-as-a-product | ★★★ |
| Alation — Data Product Types | https://www.alation.com/blog/data-product-types/ | ★★ |
| OvalEdge — Data Product Strategy | https://www.ovaledge.com/blog/data-product-strategy-guide | ★★ |
| Atlan — Data Product Lifecycle | https://atlan.com/know/data-product-lifecycle/ | ★★ |
| Medium: Data Product vs. Data Contract | https://medium.com/data-mesh-learning/data-product-vs-data-contract-whats-the-difference-d39e82cf8ed3 | ★★ |
| Medium: Data Contract vs. Data Product Specs | https://medium.com/@andrea_gioia/data-contract-vs-data-product-specifications-8ffa3cc16725 | ★★ |
| arxiv: Self-Serve Platform Design Decisions | https://arxiv.org/pdf/2402.04681 | ★★ 학술 |
| dbt Labs: Data products vs. data as a product | https://www.getdbt.com/blog/data-product-data-as-product | ★★ |
| Alation: Data Product Types | https://www.alation.com/blog/data-product-types/ | ★★ |
| O'Reilly Data Mesh Book | https://www.oreilly.com/library/view/data-mesh/9781492092384/ | ★★★ (책, 유료) |

---

*⚠️ 표시가 없는 URL은 위 리서치 세션에서 접근해 내용을 확인한 것. 가격·버전 정보는 공식 문서에서 직접 재확인 권장.*
