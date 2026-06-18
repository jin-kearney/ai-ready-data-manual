# 리서치: 데이터 카탈로그 — 구성 체계·등록 항목·표준

> 조사 목적: "AI가 잘 쓰도록 데이터를 준비·정비하는 법" 관점에서  
> 데이터 카탈로그에 **무엇을 등록하고 어떻게 찾게 하나** (등록 항목·분류·검색) 파악  
> 접속일: 2026-06-18

---

## 목차
1. [카탈로그 등록 항목 표준](#1-카탈로그-등록-항목-표준)
2. [분류·탐색 체계](#2-분류탐색-체계)
3. [AI 활용을 위한 식별 항목 (AI-Ready 차별점)](#3-ai-활용을-위한-식별-항목)
4. [시맨틱/AI 카탈로그 동향](#4-시맨틱ai-카탈로그-동향)
5. [참고 프레임워크 요약](#5-참고-프레임워크-요약)
6. [출처](#출처)

---

## 1. 카탈로그 등록 항목 표준

### 1.1 최소 필수 필드 (Minimum Viable Catalog)

업계에서 공통적으로 권장하는 데이터 자산 1건 등록 시 최소 항목:

| 필드 | 설명 | 근거 |
|------|------|------|
| **데이터 이름(Name/Title)** | 자산의 사람이 읽을 수 있는 이름. 검색·발견용 상세 포함 | [src-002] [src-010] |
| **설명(Description)** | 데이터 자산의 내용·목적 개요(Abstract). 비기술 사용자도 이해 가능하게 | [src-002] [src-010] |
| **고유 식별자(Identifier)** | 카탈로그 내 유일한 ID. 시스템 간 데이터 참조에 사용 | [src-002] [src-006] |
| **오너/스튜어드(Owner/Steward)** | 담당자 이름·연락처. "데이터 카탈로그는 오너를 자동 추론 가능" | [src-002] [src-010] [src-009] |
| **출처/보유 시스템(Source)** | 데이터가 발생하거나 저장된 시스템(ERP, MES, IoT 플랫폼 등) | [src-003] [src-010] |
| **접근 수준(Access Level)** | public / restricted / non-public(내부 기밀) 3단계 분류 | [src-002] |
| **갱신 주기(Accrual Periodicity)** | 데이터셋 발행·갱신 주기 | [src-002] |
| **최종 수정일(Modified)** | 최근 변경·수정 일시 (ISO 8601) | [src-001] [src-002] |
| **키워드(Keyword)** | 기술·비기술 사용자 모두 지원하는 탐색용 태그 | [src-002] |
| **주제 도메인(Theme/Domain)** | 업무 도메인 분류 (예: 생산, 품질, 구매) | [src-002] [src-001] |

> 한 소스는 최소 필수 항목으로 **오너(Owner)·도메인(Domain)·민감도(Sensitivity)·라이프사이클(Lifecycle)·설명(Description)** 5개를 권장 [src-002 참고].

### 1.2 DCAT-US v1.1 데이터셋 필드 분류 (공개 표준)

미국 연방정부의 공개 데이터 카탈로그 표준. W3C DCAT 국제 표준 기반. [src-002]

**필수(Required):**
- `title`, `description`, `keyword`, `modified`, `publisher`, `contactPoint`, `identifier`, `accessLevel`

**조건부 필수(Required-if):**
- `license` (라이선스 적용 시), `rights` (접근 제한 시), `spatial` (지리 범위 있을 때), `temporal` (시간 범위 있을 때), `distribution` (다운로드/접근 URL 있을 때)

**선택(Optional):**
- `accrualPeriodicity`(갱신주기), `conformsTo`(준수표준), `dataQuality`(품질 지침 충족 여부), `describedBy`(데이터 사전 URL), `isPartOf`(부모 데이터셋), `language`, `theme` 등

### 1.3 ISO/IEC 11179 메타데이터 레지스트리 등록 필수 요건

국제 표준 ISO/IEC 11179는 데이터 요소(Data Element) 등록 시 5가지를 의무화한다 [src-006]:

1. **등록(Registered)** — 공식 등록 절차 준수
2. **고유 식별(Uniquely Identified)** — 레지스트리 내 유일 식별자
3. **명명(Named)** — 명명·식별 원칙 준수
4. **정의(Defined)** — 데이터 정의 작성 규칙 준수
5. **분류(Classified)** — 분류 체계 내 위치 지정

핵심 구조: **객체 클래스(Object Class)** + **특성(Characteristic)** = **데이터 요소 개념** → **값 영역(Value Domain)** 명시. [src-006]

### 1.4 배포(Distribution) 레벨 필드

데이터 자산의 실제 접근 경로를 기술하는 필드 [src-002]:

| 필드 | 설명 |
|------|------|
| `accessURL` | API 또는 인터페이스를 통한 간접 접근 URL |
| `downloadURL` | 직접 다운로드 URL |
| `mediaType` | IANA 미디어 타입 (기계 가독 형식) |
| `format` | 파일 형식 사람이 읽을 수 있는 설명 |
| `describedBy` | 데이터 사전(Data Dictionary) URL |

---

## 2. 분류·탐색 체계

### 2.1 3축 메타데이터 분류 체계

대부분의 엔터프라이즈 카탈로그 도구가 공통으로 채택하는 분류 [src-010] [src-003]:

| 분류 축 | 내용 | 예시 필드 |
|---------|------|----------|
| **기술 메타데이터(Technical)** | 구조적 스키마·데이터 타입·형식 | 컬럼명, 데이터 타입, 테이블 스키마 |
| **관리 메타데이터(Administrative)** | 오너십·접근 규칙·규제 정책 | 오너, RBAC 정책, 감사 로그 |
| **비즈니스 메타데이터(Business)** | 비기술 이해관계자 이해용 컨텍스트 | 비즈니스 설명, 글로서리 링크, 도메인 태그 |

### 2.2 페싯 검색(Faceted Search) 패턴

현대 데이터 카탈로그의 탐색 방식: 단순 키워드 매칭을 넘어 다차원 필터링 제공 [src-009] [src-003]:

**페싯 필터 기준:**
- 소스 시스템(MES, ERP, IoT, LIMS 등)
- 데이터 도메인(생산, 품질, 구매, 재무 등)
- 오너(사업부·팀·개인)
- 분류(민감도·규제 등급)
- 품질 점수(수치 범위 필터)
- 최신성(날짜 범위)

**추가 탐색 방식:**
- 분류 체계·계층 구조 브라우징 (taxonomy browsing)
- 역할 및 과거 사용 패턴 기반 추천
- 의미론적 검색(벡터 임베딩 기반) — 용어가 달라도 개념적 유사 자산 탐색 [src-009]
- 자연어 검색 — "Google 검색처럼" 비기술 사용자 접근 [src-010]

### 2.3 비즈니스 글로서리 연계

비즈니스 글로서리(Business Glossary)와 데이터 카탈로그는 다른 도구이나 연동 시 시너지 [src-003]:

- 글로서리: 핵심 비즈니스 용어의 표준 정의 (예: "불량률"의 정확한 계산 방식)
- 카탈로그: 해당 용어가 어느 테이블·컬럼에 저장되는지 물리적 위치
- 연계 시: 검색마다 글로서리 컨텍스트를 자산 결과에 자동 표시

### 2.4 지식 그래프(Knowledge Graph) 기반 탐색

전통 카탈로그를 넘어 자산 간 관계를 그래프로 탐색 [src-007] [src-009]:

- 비즈니스 개념 ↔ 저장 테이블 연결
- 지표 ↔ 계산 로직·원천 데이터 연결
- 도메인 모델 — 조직 전반 엔터티 관계 시각화
- "어떤 시작점에서든 관련 데이터셋·규정 언어·데이터 요소를 찾고 탐색" 가능 [src-009 참조 사례]

---

## 3. AI 활용을 위한 식별 항목

> 이 섹션이 'AI-Ready 카탈로그'의 핵심 차별점.
> "이 데이터를 AI가 재사용·재활용해도 되는지" 판단하게 돕는 항목들.

### 3.1 AI 활용 적합성 판단 5개 차원

AI-ready 데이터를 갖추기 위한 5대 차원 [src-008]:

| 차원 | 카탈로그 등록 항목 |
|------|------------------|
| **데이터 품질** | 품질 점수(정확성·완전성·일관성·최신성), 검증 타임스탬프 |
| **데이터 리니지** | 컬럼 레벨 변환 경로, 업스트림 의존성, 원천 추적 |
| **발견 가능성** | 비즈니스 설명, 오너 기록, 최신성 신호 |
| **의미론·컨텍스트** | 비즈니스 글로서리 링크, 도메인 온톨로지 참조, 스키마 문서 |
| **보안·접근 거버넌스** | RBAC/ABAC 정책, PII 마스킹, 동의(consent) 기록, 감사 로그 |

### 3.2 프로버넌스(Data Provenance) 항목

데이터 원천 추적은 AI 재사용 신뢰도의 핵심 [src-004] [src-008]:

| 필드 | 설명 |
|------|------|
| **원천 시스템** | 데이터가 최초 발생한 시스템 |
| **수집 방법** | 자동 연동·수동 입력·센서 등 수집 방식 |
| **변환 이력** | ETL/파이프라인에서 적용된 변환 로직 목록 |
| **버전 이력/변경 로그** | 추가 레코드, 제거된 오류, 주요 갱신 사항 — "AI 학습에 영향을 미칠 변경을 인지" [src-005] |
| **컬럼 레벨 리니지** | 개별 컬럼의 원천→결과 추적 경로 |

### 3.3 전처리(Preprocessing) 여부 및 AI 적합성 항목

Croissant 형식(MLCommons, 2024)은 ML-Ready 데이터셋을 위해 다음을 명시 [src-005]:

| 항목 | 설명 |
|------|------|
| **encodingFormat** | 데이터 인코딩 형식 |
| **sha256** | 파일 무결성 체크섬 |
| **dataType** | 의미론적 타입 (schema.org 어휘 매핑) |
| **ML 특화 메타데이터** | 학습/검증/테스트 분할 정보, 레이블 정보 |
| **Responsible AI 문서** | 데이터 라이프사이클·라벨링·안전성·공정성·추적성 |
| **citeAs** | 인용 정보 (재사용 시 출처 명시) |
| **license** | 사용 권리 및 라이선스 조건 |

### 3.4 AI 모델 연계 거버넌스 필드 (고급)

AI 모델이 어떤 데이터로 학습됐는지 추적하기 위한 고급 항목 [src-004]:

- ML/AI 모델 버전 및 성능 이력
- 모델 프로파일의 편향(bias) 감지 결과
- 파생 AI 모델에 특화된 데이터 리니지
- 데이터 품질 경보 → 모델 오너 자동 알림 연계

### 3.5 AI 에이전트 접근을 위한 기계 가독 속성

AI 에이전트(Agent)가 카탈로그를 프로그래밍 방식으로 소비하기 위한 속성 [src-009]:

- **구조화된 API** — JSON-LD, REST API를 통한 메타데이터 접근
- **MCP(Model Context Protocol) 서버 호환** — LLM 기반 에이전트가 카탈로그 쿼리
- **지식 그래프 관계** — 에이전트가 자산·용어·지표 간 관계를 탐색
- **메타데이터 레이크하우스** (Apache Iceberg 기반) — SQL로 메타데이터 쿼리

---

## 4. 시맨틱/AI 카탈로그 동향

### 4.1 능동 메타데이터(Active Metadata) 패러다임 전환

기존 정적 메타데이터 문서화 → **지속 갱신되는 인텔리전스 계층** [src-007]:

| 능동 메타데이터가 지속 추적하는 유형 |
|-------------------------------|
| 기술 메타데이터 — 스키마 변경, 컬럼 정의, 데이터 타입 |
| 운영 메타데이터 — 쿼리 로그, 사용 패턴, 리니지 이벤트 |
| 비즈니스 메타데이터 — 오너십 기록, 분류, 글로서리 항목 |
| 협업 신호 — 팀 대화, 문서화 업데이트 |
| 품질 지표 — 완전성, 정확성, 최신성, 이상 징후 |
| 접근 패턴 — 인기도 추이, 사용자 상호작용, 의존성 |

**AI-Ready 관점 핵심:** 능동 메타데이터는 AI 에이전트가 현재의 검증된·거버넌스된 정보를 조회하도록 보장. 수동 방식은 "장애 후 감지"지만 능동 방식은 "변경 즉시 감지·전파". [src-007]

### 4.2 지식 그래프 기반 발견 (Knowledge Graph)

자산 간 관계를 시맨틱하게 표현 [src-009]:
- 비즈니스 개념 ↔ 저장 테이블/컬럼 연결
- 지표 ↔ 계산 로직·원천 데이터
- 도메인 모델 — 조직 전반 엔터티 관계

효과 (Gartner 2024 Data & Analytics Summit 인용 [src-009]):
- 의미론 계층 구현 조직: 업무 사용자 인사이트 도출 시간 **43% 단축**
- 능동 메타데이터 적용: 엔지니어링 팀 데이터 발견 요청 **30~50% 감소**

### 4.3 자동 분류·자동 태깅

AI/ML 기반 자동화로 "데이터를 찾기 쉽게" [src-004] [src-009]:
- ML 알고리즘 — 데이터 관계 추론·민감/PII 데이터 자동 분류
- 자동 글로서리 연결 및 의미론적 태깅
- SQL 쿼리 이력·파이프라인 코드로 설명(description) 자동 생성
- 스키마 변경 자동 감지 → 메타데이터 자동 갱신

### 4.4 자연어 검색 (Natural Language Search)

비기술 사용자(제조 현업)의 데이터 발견 진입 장벽 제거 [src-010] [src-009]:
- "Google 검색처럼" — 자연어 쿼리로 데이터 자산 탐색
- 벡터 임베딩 기반 의미론적 검색 — 용어가 달라도 개념적 유사 자산 탐색
- 역할·과거 사용 패턴 기반 개인화 추천

---

## 5. 참고 프레임워크 요약

### 5.1 DCAT-US (W3C DCAT 기반)
- 출처: https://resources.data.gov/resources/dcat-us-3-catalog/ [src-001], https://resources.data.gov/resources/dcat-us/ [src-002]
- 공개 데이터 카탈로그 국제 표준. 카탈로그·데이터셋·배포 3계층으로 필드 정의.
- Required / Required-if / Optional 3단계로 구분.

### 5.2 ISO/IEC 11179 메타데이터 레지스트리
- 출처: https://en.wikipedia.org/wiki/ISO/IEC_11179 [src-006]
- 데이터 요소 등록 5대 요건: 등록·고유식별·명명·정의·분류.
- 핵심 구조: 객체 클래스 + 특성 → 데이터 요소 개념 + 값 영역.
- 최신판: ISO/IEC 11179-1:2023, ISO/IEC 11179-31:2023.

### 5.3 Croissant (MLCommons, 2024)
- 출처: https://arxiv.org/html/2403.19546v1 [src-005]
- ML-Ready 데이터셋 전용 메타데이터 형식. schema.org/Dataset 확장.
- 4계층: Dataset Metadata → Resources → Structure → Semantic.
- 전처리 요건·데이터 분할·책임 있는 AI 문서화 항목 포함.

### 5.4 DAMA-DMBOK 3.0 (2025 업데이트)
- 출처: https://dama.org/learning-resources/ [참고]
- AI 거버넌스·클라우드 네이티브 환경으로 현대화. 메타데이터 관리 챕터 데이터 카탈로그 포함.

### 5.5 EDMC DCAM v3
- 출처: https://edmcouncil.org/frameworks/dcam/ [참고]
- 클라우드 네이티브·AI/ML 통합·현대 데이터 파이프라인 대응 강화.
- 데이터 거버넌스·프라이버시·보호 역량 강조.

---

## 출처

| id | URL | 제목 | 접속일 |
|----|-----|------|-------|
| src-001 | https://resources.data.gov/resources/dcat-us-3-catalog/ | DCAT-US Schema v3.0 Catalog fields | 2026-06-18 |
| src-002 | https://resources.data.gov/resources/dcat-us/ | DCAT-US Schema v1.1 (Project Open Data Metadata Schema) | 2026-06-18 |
| src-003 | https://www.ovaledge.com/blog/ai-ready-data-catalog | What Does It Actually Take to Build an AI-Ready Data Catalog? — OvalEdge | 2026-06-18 |
| src-004 | https://barc.com/data-catalog-ai-ready/ | Is Your Data Catalog Ready for the AI Age? — BARC | 2026-06-18 |
| src-005 | https://arxiv.org/html/2403.19546v1 | Croissant: A Metadata Format for ML-Ready Datasets (MLCommons 2024) | 2026-06-18 |
| src-006 | https://en.wikipedia.org/wiki/ISO/IEC_11179 | ISO/IEC 11179 — Wikipedia | 2026-06-18 |
| src-007 | https://atlan.com/active-metadata-101/ | Active Metadata: The Complete 2026 Guide — Atlan | 2026-06-18 |
| src-008 | https://www.dawiso.com/glossary/ai-ready-data | AI-Ready Data: Complete Guide — Dawiso | 2026-06-18 |
| src-009 | https://atlan.com/know/data-catalog-for-ai/ | Data Catalog for AI: Capabilities, Uses & Tooling 2026 — Atlan | 2026-06-18 |
| src-010 | https://www.secoda.co/learn/best-practices-for-data-cataloging | Best Practices for Data Cataloging — Secoda | 2026-06-18 |
| src-ref-A | https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/ | DAMA-DMBOK (3.0 업데이트 2025 진행 중) | 2026-06-18 |
| src-ref-B | https://edmcouncil.org/frameworks/dcam/ | DCAM v3 — EDM Council | 2026-06-18 |
| src-ref-C | https://mlcommons.org/2024/03/croissant_metadata_announce/ | MLCommons Croissant 공식 발표 (2024-03) | 2026-06-18 |

---

*fetch 실패 URL:*
- https://www.ai.mil/Portals/137/Documents/Resources%20Page/Federated%20Data%20Catalog%20-%20Minimum%20Metadata%20Requirements.pdf → HTTP 403 Forbidden
- https://onlinelibrary.wiley.com/doi/10.1002/aaai.70054 → HTTP 402 Payment Required
