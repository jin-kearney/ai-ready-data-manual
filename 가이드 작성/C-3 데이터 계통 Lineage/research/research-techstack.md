# C-3 데이터 계통(Data Lineage) — Tech Stack 리서치 원자료

> 작성일: 2026-06-24 | 조사 범위: 공식 사이트·문서·발표 자료(2024~2026-06 기준)  
> 용도: 가이드 작성자용 원자료 — 추측 없이 확인된 사실만 기재, 미확인은 명시  
> 관점: "AI/모델을 만드는 법"이 아니라 "데이터 흐름·근거를 추적·기록하는 도구"

---

## 목차

1. [2층 정본(01 Tech Stack 비교) C-3 반영 현황](#1-2층-정본-c-3-반영-현황)
2. [수집 방식 3가지 — 정의·장단점](#2-수집-방식-3가지)
3. [컬럼 단위 vs 테이블 단위 계통](#3-컬럼-단위-vs-테이블-단위-계통)
4. [유형 1 — 계통 오픈 표준·오픈소스](#4-유형-1--계통-오픈-표준오픈소스)
5. [유형 2 — 데이터 플랫폼 내장 계통](#5-유형-2--데이터-플랫폼-내장-계통)
6. [유형 3 — 전용 상용 계통·거버넌스 솔루션](#6-유형-3--전용-상용-계통거버넌스-솔루션)
7. [솔루션 종합 비교표](#7-솔루션-종합-비교표)
8. [출처 URL 목록](#8-출처-url-목록)

---

## 1. 2층 정본 C-3 반영 현황

`Tech Player/01 Tech Stack 비교 (솔루션×주제).md` 파일에 이미 C-3 Lineage 관련 내용이 기재되어 있음. 주요 내용:

- **묶음 ① (통합 거버넌스·카탈로그 플랫폼)**: A-1·A-2·A-3 + C-3 계통을 한 제품이 함께 커버함이 명시됨. 대상 솔루션: Collibra, Microsoft Purview, Atlan, Databricks Unity Catalog, OpenMetadata, DataHub
- **계통(Lineage, 컬럼단위)** 행이 별도로 존재
- **C-3 열**이 이미 설정되어 있고 각 솔루션에 ✓ 표시
- **OpenLineage + Marquez**가 OSS 계통 특화 솔루션으로 별도 행에 있음

→ **가이드 작성 시 주의:** 이 정본과 내용이 중복되지 않게, C-3 가이드의 솔루션 섹션은 "계통 기능" 중심 비교로 초점을 맞추고 2층 정본으로 링크 처리할 것

---

## 2. 수집 방식 3가지

### 방식 ① 코드·SQL 파싱(정적 분석, Static Analysis)

**정의:** 실행 전에 SQL 스크립트·ETL 코드·저장 프로시저를 파싱해 데이터 흐름을 추론하는 방식. 실행 없이 소스코드에서 계통을 추출한다.

**장점:**
- 실행 없이도 계통 파악 가능 → 사전 영향도 분석에 유리
- 레거시 ETL·저장 프로시저처럼 런타임 에이전트 설치가 어려운 환경에 적합
- 변환 로직을 코드 수준에서 상세히 추출 가능

**단점:**
- 동적 SQL(변수로 테이블명이 결정되는 경우)은 파싱 불가 또는 오류
- 복잡한 중첩 쿼리·UDF에서 정확도 저하
- 실제 실행 경로와 다를 수 있음(코드는 있지만 실제로 실행 안 되는 경로 포함)

**대표 도구:** IBM Manta(정적 분석 특화), Collibra Data Lineage, Alation(SQL 로그 파싱 병행), Spline(Spark 실행 계획 분석)

---

### 방식 ② 런타임·실행 로그 기반(Dynamic/Runtime Lineage)

**정의:** 데이터 파이프라인이 실제로 실행될 때, 실행 엔진 또는 오케스트레이터가 계통 이벤트를 자동으로 수집·전송하는 방식. OpenLineage 이벤트가 대표적이다.

**핵심 개념 — OpenLineage 이벤트 구조:**
- **Run:** 잡의 특정 실행 인스턴스 (시작·완료·실패 상태 포함)
- **Job:** 데이터를 처리하는 작업(쿼리, ETL 태스크, 노트북 등)
- **Dataset:** 잡이 읽거나 쓰는 데이터 자산(테이블, 파일, 토픽 등)

**장점:**
- 실제 실행 경로만 기록 → 불필요한 계통 없음
- 동적 SQL·런타임 결정 경로도 추적 가능
- OpenLineage 표준 채택 시 도구 교체해도 계통 데이터 재활용 가능

**단점:**
- 에이전트·플러그인 설치 필요 (환경별 설정 비용)
- 실행 안 된 경로는 계통 없음 → 초기 구축 전 사전 분석 불가
- 레거시 시스템·배치 스크립트에서 지원 미흡한 경우 있음

**대표 도구:** OpenLineage(표준) + Marquez(저장·시각화), Databricks Unity Catalog(런타임 자동), Airflow OpenLineage 플러그인, Spark OpenLineage 통합

---

### 방식 ③ 수기 선언(Manual Declaration)

**정의:** 데이터 담당자가 직접 데이터 흐름을 입력·기술하는 방식. 메타데이터 플랫폼 UI에서 관계를 직접 그리거나, YAML·CSV로 계통을 선언한다.

**장점:**
- 자동화가 어려운 레거시 시스템·엑셀·공유 드라이브 계통 표현 가능
- 비즈니스 맥락(개념적 계통)을 정확히 반영
- 도구 비의존적 — 어떤 플랫폼에서도 기본 지원

**단점:**
- 관리 비용이 높음 — 파이프라인 변경 시 수동 갱신 필요
- 실제 흐름과 불일치 위험(문서화 누락·지연)
- 대규모 환경에서 현실적으로 전수 관리 불가

**사용 맥락:** 자동화를 보조하는 용도(공백 채우기), 초기 수동 계통 수립, 레거시 환경 브릿지

---

## 3. 컬럼 단위 vs 테이블 단위 계통

### 테이블 단위(Table-Level) 계통

- 어떤 테이블이 어떤 테이블에서 왔는지만 기록
- "orders 테이블 → revenue_summary 테이블" 수준
- 구현이 단순하고 대부분 도구에서 기본 지원
- **한계:** 테이블 안의 어떤 컬럼이 문제인지, 어떤 PII 필드가 어디로 흘렀는지 알 수 없음

### 컬럼 단위(Column-Level) 계통

- 소스 컬럼 → 변환 규칙 → 타겟 컬럼까지 추적
- "orders.amount → (집계: SUM) → revenue_summary.total_revenue" 수준
- **영향도 분석 중요성:**
  - 스키마 변경(컬럼 삭제·이름 변경) 전에 어떤 하위 보고서·모델이 영향을 받는지 정확히 파악 가능
  - 테이블 단위: "이 테이블을 쓰는 것들" → 컬럼 단위: "이 컬럼을 쓰는 것들"로 범위를 좁힘
- **AI·컴플라이언스 필요성:**
  - AI 모델 입력 데이터의 특정 피처(feature)가 어떤 원천 컬럼에서 왔는지 추적
  - PII 필드(개인식별정보)가 어디로 흘렀는지 컬럼 단위로 추적 → 규정 준수 증빙
  - GDPR·금융 규제 감사 시 "이 필드가 어떻게 생성됐는가"를 증명

### 2025년 시장 현황

컬럼 단위 계통이 거버넌스 요건에서 사실상 필수로 자리잡고 있음. Google Dataplex, Databricks Unity Catalog, Snowflake, Atlan, DataHub 등 주요 플랫폼들이 모두 컬럼 단위 계통을 GA(일반 제공) 또는 지원 중.

---

## 4. 유형 1 — 계통 오픈 표준·오픈소스

### 4-1. OpenLineage

| 항목 | 내용 |
|------|------|
| 유형 | 오픈 표준 (사양, 구현체 아님) |
| 라이선스 | Apache 2.0 |
| 관리 주체 | LF AI & Data Foundation (Graduate project) |
| 공식 사이트 | https://openlineage.io/ |
| GitHub | https://github.com/OpenLineage/OpenLineage |
| 핵심 역할 | 계통 메타데이터 수집의 **공통 API 표준** 정의 |

**표준화 범위:**
- 3개 핵심 엔티티: **Run**(실행 인스턴스), **Job**(처리 작업), **Dataset**(입출력 데이터)
- 이벤트 스펙: JSON Schema 기반 OpenLineage.json으로 정형화
- OpenAPI 스펙도 제공 (HTTP 기반 구현 지원)
- **Facets** 개념: 확장 가능한 사용자 정의 메타데이터 — 기본 스펙에 커스텀 속성 추가 가능

**지원 도구(OpenLineage 이벤트 방출):**
- Apache Airflow, Apache Spark, Apache Flink
- dbt (dbt Cloud 및 Core 연동)
- Dagster, Astronomer
- Amazon SageMaker Unified Studio (AWS)
- IBM, Databricks, Snowflake 등 상용 플랫폼에서 수집 지원

**2023년 추가:** Static Lineage 개념 도입 — 런타임 없이 코드에서 정적으로 계통 모델링 가능

**수집 방식:** 런타임 이벤트 기반 (기본), 정적 계통 (2023년 추가)  
**컬럼 단위 지원:** 표준 스펙 내 컬럼 단위 패싯(facet) 정의 가능 (구현은 각 통합 도구에 따라 다름)

---

### 4-2. Marquez

| 항목 | 내용 |
|------|------|
| 유형 | OpenLineage 참조 구현 (오픈소스) |
| 라이선스 | Apache 2.0 |
| 관리 주체 | LF AI & DATA (incubation) |
| 원래 개발 | WeWork |
| 공식 사이트 | https://marquezproject.ai/ |
| GitHub | https://github.com/MarquezProject/marquez |

**역할:** OpenLineage 이벤트를 수신·저장·시각화하는 참조 구현체.

**주요 기능:**
- OpenLineage 호환 엔드포인트 (이벤트 수집)
- PostgreSQL 기반 계통 메타데이터 저장
- 웹 UI: 잡·데이터셋 간 의존관계 그래프 시각화
- 계통 API: 백필(backfill)·근본 원인 분석용 메타데이터 쿼리
- OpenLineage 커뮤니티의 모든 통합(Airflow, Spark, Flink, dbt, Dagster)과 바로 연동

**수집 방식:** 런타임 이벤트 기반 (OpenLineage 이벤트 수신)  
**컬럼 단위 지원:** OpenLineage 이벤트의 컬럼 단위 패싯 저장 지원 (시각화 수준은 구현에 따라 상이)  
**배포:** 자체 호스팅 (Docker Compose 지원), 클라우드 없음  
**잘하는 것:** OpenLineage 표준 계통 이벤트 저장·시각화 참조 구현, 경량 계통 저장소

---

### 4-3. Apache Atlas

| 항목 | 내용 |
|------|------|
| 유형 | 오픈소스 메타데이터 관리·거버넌스 프레임워크 |
| 라이선스 | Apache 2.0 |
| 관리 주체 | Apache Software Foundation |
| 공식 사이트 | https://atlas.apache.org/ |
| 최신 버전 | 2.4.0 (2025년 1월), 2.5.0 추가 중 (Trino extractor·PostgreSQL 백엔드) |
| 주요 대상 | Hadoop 생태계 (HBase, Hive, Kafka, Sqoop, Storm) |

**계통 기능:**
- Hadoop 네이티브 소스에 대한 컬럼 단위 계통 자동 추적
- Type-and-Entity 모델로 데이터 자산 카탈로그화
- Apache Ranger 연동 → 분류 기반 접근 정책 적용
- REST API로 계통 메타데이터 접근

**한계:**
- Hadoop/HBase/Hive 외 현대 클라우드 데이터 스택(Snowflake, Databricks 등)과의 연동은 추가 커스텀 작업 필요
- UI 현대화 수준이 상용 솔루션 대비 낮음

**수집 방식:** 런타임 훅(Hive Hook 등) + 커넥터 기반  
**컬럼 단위 지원:** Hive·Spark SQL 기반 컬럼 단위 계통 지원  
**배포:** 자체 호스팅 (온프레미스)  
**잘하는 것:** Hadoop 생태계 거버넌스·계통 — Hive·Spark SQL 환경에서 무료 사용

---

### 4-4. DataHub

| 항목 | 내용 |
|------|------|
| 유형 | 오픈소스 메타데이터 플랫폼 (상용 클라우드 버전 있음) |
| 라이선스 | Apache 2.0 (Core) |
| 관리 주체 | datahub-project (LinkedIn 개발 → 독립 커뮤니티) |
| 상용 버전 | DataHub Cloud (Acryl Data 운영) |
| 공식 사이트 | https://datahub.com/ |
| 문서 | https://docs.datahub.com/ |

**계통 기능:**
- 80+ 프로덕션 커넥터 (Snowflake, BigQuery, Databricks, Redshift, Teradata, Looker, Power BI, Tableau 등)
- SQL 파싱 기반 컬럼 단위 계통 자동 추출 (v0.14.1부터 Databricks·BigQuery·Snowflake 등 네이티브 지원)
- Airflow 플러그인: 스키마 인식 SQL 파싱으로 정확도 향상
- 그래프 기반 메타데이터 모델 — 통합 엔티티 프레임워크
- 3,000+ 조직에서 프로덕션 사용 (2026 기준)

**수집 방식:** SQL 파싱(정적) + 커넥터 기반 자동 수집 + API  
**컬럼 단위 지원:** ✓ (Databricks·BigQuery·Snowflake 등 주요 플랫폼)  
**배포:** 오픈소스 자체 호스팅 또는 DataHub Cloud (SaaS)  
**잘하는 것:** 현대 데이터 스택 전반 커버, 컬럼 계통 + 사용량 통계 + 데이터 품질을 한 플랫폼에서

---

### 4-5. dbt (data build tool)

| 항목 | 내용 |
|------|------|
| 유형 | 변환 도구 (계통은 부산물로 노출) |
| 라이선스 | Apache 2.0 (Core), 상용(dbt Cloud) |
| 관리 주체 | dbt Labs |
| 공식 사이트 | https://www.getdbt.com/ |
| 컬럼 단위 계통 문서 | https://docs.getdbt.com/docs/explore/column-level-lineage |

**계통 기능:**
- **DAG 자동 생성:** 모든 dbt 모델 간 의존관계를 방향성 비순환 그래프(DAG)로 자동 시각화
- **dbt Explorer:** 소스·모델·익스포저·메트릭 전반의 계통 그래프 제공
- **컬럼 단위 계통(CLL):** 엔터프라이즈 플랜 전용 — 어떤 컬럼이 어떻게 변환·전달됐는지 추적
  - Transformed(변환됨) / Passthrough(그대로 전달) / Renamed(이름 변경) 구분
  - `dbt docs generate` 실행마다 갱신
- **한계:** `SELECT` 문만 추적 (JOIN·FILTER 반영 제한), Python 모델 미지원, 복잡한 UDF 파싱 오류 가능

**수집 방식:** 정적 분석 (SQL 모델 DAG에서 파생)  
**컬럼 단위 지원:** ✓ 단, Enterprise 플랜 이상 필요  
**배포:** Core(오픈소스 CLI) / Cloud(SaaS)  
**잘하는 것:** SQL 변환 레이어의 모델 의존관계·계통 → 분석 엔지니어링 파이프라인 계통

---

### 4-6. Apache Spline

| 항목 | 내용 |
|------|------|
| 유형 | Apache Spark 계통 추적 오픈소스 |
| 라이선스 | Apache 2.0 |
| 관리 주체 | ABSA OSS (AbsaOSS) |
| 공식 사이트 | https://absaoss.github.io/spline/ |
| GitHub | https://github.com/AbsaOSS/spline |
| Spark Agent GitHub | https://github.com/AbsaOSS/spline-spark-agent |
| 현재 버전 | 0.7 (최신 0.7.9) |

**계통 기능:**
- Spark 실행 계획(Logical Execution Plan) 인터셉트 → 계통 자동 수집
- SQL·Scala·Python Spark 잡 모두 지원 (Spark 3.0+)
- ArangoDB 기반 그래프 저장
- Producer API / Consumer API / Spline UI 3계층 아키텍처
- Docker 기반 배포

**수집 방식:** 런타임 (Spark 이벤트 리스너 기반)  
**컬럼 단위 지원:** 기본적으로 테이블/데이터셋 단위 추적, 컬럼 단위는 제한적  
**배포:** 자체 호스팅  
**잘하는 것:** Spark 파이프라인 특화 계통 — 무료로 Spark 계통 시각화

---

## 5. 유형 2 — 데이터 플랫폼 내장 계통

### 5-1. Databricks Unity Catalog

| 항목 | 내용 |
|------|------|
| 유형 | 데이터 플랫폼 내장 거버넌스·계통 |
| 공식 사이트 | https://www.databricks.com/product/unity-catalog |
| 계통 문서 | https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage |
| 배포 | Databricks 플랫폼 (클라우드: AWS/Azure/GCP) |

**계통 기능:**
- **자동 런타임 수집:** Spark 실행 계획을 런타임에 인터셉트 → 에이전트·설정 없이 자동
- **컬럼 단위 지원:** ✓ SQL·R·Python·Scala 모든 언어, Spark SQL·Databricks SQL 대상
- **크로스 워크스페이스 집계:** 동일 metastore에 연결된 모든 워크스페이스 계통을 통합 조회
- **영향도 분석 UI:** 테이블·컬럼 변경 전 다운스트림 의존관계 사전 확인
- **컴플라이언스 추적:** 민감 데이터 흐름을 컬럼 단위로 추적
- **추가 자산:** 노트북, 워크플로, 대시보드의 계통도 캡처

**수집 방식:** 런타임 (쿼리 플랜 자동 인터셉트)  
**컬럼 단위 지원:** ✓ (단, 경로 기반 참조·UDF에서 일부 제한)  
**한계:**
- 2024년 9월 1일 이전 계통 데이터 없음
- 이름 바뀐 객체는 이전 계통 유지 안 됨
- RDD·전역 임시 뷰·시스템 테이블 미캡처
- Databricks 플랫폼 외부 데이터 소스는 별도 External Lineage 설정 필요

---

### 5-2. Microsoft Purview

| 항목 | 내용 |
|------|------|
| 유형 | Microsoft Azure 기반 통합 거버넌스·계통 |
| 공식 사이트 | https://learn.microsoft.com/en-us/purview/ |
| 계통 가이드 | https://learn.microsoft.com/en-us/purview/data-gov-classic-lineage |
| 배포 | Azure 클라우드 (관리형 SaaS) |

**계통 기능:**
- **자동 수집 범위:** Azure Data Factory(ADF), Azure Synapse, Azure Databricks, Azure SQL, Data Share 등 Azure 네이티브 서비스 계통 자동 수집
- ADF Copy·Data Flow·SSIS 패키지 실행 시 계통 자동 캡처 (추가 설정 없음)
- 소스·싱크가 지원 데이터 스토어라면 자동으로 Data Map에 메타데이터 추가
- 온프레미스·멀티클라우드·SaaS 환경까지 자동화 범위 확대 중
- **수동 계통:** 자동화 미지원 소스는 수동 계통 입력 가능

**수집 방식:** 런타임 이벤트 기반 (Azure 서비스 연동) + 수동  
**컬럼 단위 지원:** 미확인 (공식 문서에서 컬럼 단위 GA 여부 명확히 확인 못 함 — PoC 확인 권장)  
**잘하는 것:** Azure 스택 완전 연동, Azure 데이터 흐름의 엔드투엔드 계통 자동 수집

---

### 5-3. Snowflake (ACCESS_HISTORY 기반 계통)

| 항목 | 내용 |
|------|------|
| 유형 | 클라우드 데이터 플랫폼 내장 계통 |
| 공식 문서 | https://docs.snowflake.com/en/user-guide/ui-snowsight-lineage |
| ACCESS_HISTORY 문서 | https://docs.snowflake.com/en/user-guide/access-history |
| 배포 | Snowflake Cloud (SaaS) |

**계통 기능:**
- **ACCOUNT_USAGE.ACCESS_HISTORY 뷰:** SQL 쓰기 작업(INSERT·CTAS·MERGE)에서 소스→타겟 컬럼 매핑을 JSON 배열로 기록
- **Snowsight 내 시각 계통:** 객체 단위 계통 그래프를 UI에서 시각화
- 컬럼 단위 계통: Snowsight 그래프에서는 객체 단위만 표시, 컬럼 단위는 사이드 패널에서 확인 (2025년 3월 기준)
- Snowflake는 "최초로 네이티브 컬럼 단위 계통을 제공한 데이터 플랫폼"으로 포지셔닝

**수집 방식:** 런타임 (SQL 실행 시 자동 기록)  
**컬럼 단위 지원:** ✓ (단, 시각화는 현재 사이드 패널 수준 — 풀 그래프 시각화는 미확인)  
**잘하는 것:** Snowflake 내부 객체 계통 내장 제공 — 추가 도구 없이 SQL 기반 계통 조회

---

### 5-4. Google Cloud Dataplex (BigQuery 계통)

| 항목 | 내용 |
|------|------|
| 유형 | Google Cloud 내 데이터 거버넌스·계통 |
| 공식 문서 | https://docs.cloud.google.com/dataplex/docs/about-data-lineage |
| 컬럼 계통 블로그 | https://cloud.google.com/blog/products/data-analytics/dataplex-supports-column-level-lineage-for-bigquery-data |
| 배포 | Google Cloud (관리형) |

**계통 기능:**
- Data Lineage API 활성화 후 BigQuery 잡의 계통 자동 수집
- **컬럼 단위 계통 GA:** BigQuery 잡에서 컬럼 단위 계통 일반 제공 (현재는 BigQuery 잡 한정)
- AI 모델 입력 데이터의 특정 피처 원천 추적, PII 필드 흐름 추적 등 활용 가능
- 영향도 분석: 컬럼 변경 전 다운스트림 영향 범위 파악

**수집 방식:** 런타임 (BigQuery 쿼리 실행 시 자동)  
**컬럼 단위 지원:** ✓ (BigQuery 잡 한정 — 다른 소스로 확장 중)  
**잘하는 것:** BigQuery 중심 GCP 데이터 스택의 컬럼 단위 계통

---

## 6. 유형 3 — 전용 상용 계통·거버넌스 솔루션

### 6-1. Collibra Data Lineage

| 항목 | 내용 |
|------|------|
| 유형 | 전용 엔터프라이즈 거버넌스·계통 플랫폼 |
| 공식 사이트 | https://www.collibra.com/products/data-lineage |
| 제품 문서 | https://productresources.collibra.com/docs/collibra/latest/Content/CollibraDataLineage/ |
| 배포 | SaaS / 자체 호스팅 (온프레미스 포함) |

**계통 기능:**
- 약 40개 데이터 소스 커버 (ETL·BI 도구·데이터 웨어하우스 포함)
- AI 기반 계통 자동 추출: 코드 파싱·메타데이터 스캔으로 임시 테이블·컬럼·에지까지 연결
- **컬럼 단위 계통:** ✓ (테이블↔컬럼 계통 전환 가능, Google Dataplex 컬럼 계통 지원 추가)
- 비즈니스 계통(Business Lineage)과 기술 계통(Technical Lineage) 레이어 전환
- OpenLineage 표준 지원 ("블라인드 스팟" 커버)
- 인라인 코드 컨텍스트 보기, PDF/PNG/CSV 내보내기
- 간접 계통(조건문·조인 포함) 시각화

**수집 방식:** 정적 분석(코드 파싱) + OpenLineage(런타임) 병용  
**컬럼 단위 지원:** ✓  
**잘하는 것:** 엔터프라이즈급 엔드투엔드 계통, 비즈니스·기술 계통 통합 뷰, 레거시 ETL 파싱

---

### 6-2. IBM Manta Data Lineage

| 항목 | 내용 |
|------|------|
| 유형 | 전용 자동화 데이터 계통 플랫폼 (IBM 인수) |
| 공식 페이지 | https://www.ibm.com/products/manta-data-lineage |
| IBM 발표 | https://newsroom.ibm.com/IBM-acquires-Manta-Software-Inc-to-complement-data-and-AI-governance-capabilities |
| 원래 회사 | Manta Software Inc. (2016년 설립, 체코 프라하) — IBM에 2023년 인수 |
| 배포 | IBM Cloud Pak for Data / IBM Software Hub (온프레미스·클라우드) |

**계통 기능:**
- **정적 분석 특화:** SQL·ETL 스크립트·BI 보고서·저장 프로시저를 자동 파싱해 계통 추출
- 데이터 소스·변환·의존관계의 포괄적 맵 제공
- watsonx.ai·watsonx.data·watsonx.governance와 통합 — AI 모델이 올바른 데이터를 썼는지 추적
- T-Mobile, BMO 등 대형 금융·통신 기업 레퍼런스

**주의:** IBM Manta 공식 페이지(ibm.com/products/manta-data-lineage)는 403 응답 — 직접 접근 불가. 발표·문서 페이지에서 내용 확인.

**수집 방식:** 정적 분석 (코드·SQL·ETL 파싱)  
**컬럼 단위 지원:** ✓ (확인 — 소스→타겟 컬럼 매핑이 핵심 기능)  
**잘하는 것:** 레거시 ETL(Informatica, SSIS, DataStage 등) + SQL 스크립트의 자동 정적 계통 추출

---

### 6-3. Atlan

| 항목 | 내용 |
|------|------|
| 유형 | 전용 액티브 메타데이터 플랫폼 (SaaS) |
| 공식 사이트 | https://atlan.com/ |
| 계통 페이지 | https://atlan.com/data-lineage/ |
| 배포 | SaaS 전용 |

**계통 기능:**
- 4가지 수집 방법 병행: ① SQL 파싱, ② 네이티브 API 크롤링, ③ OpenLineage 이벤트 수신, ④ REST API/SDK/CSV/비주얼 빌더
- **컬럼 단위 계통:** ✓ 80+ 시스템 (Snowflake·BigQuery·Redshift·Databricks 등)
- OpenLineage 네이티브 연동: Airflow·Spark·dbt Cloud·Astronomer의 런타임 계통 수집
- MCP Server 제공 → AI 에이전트가 계통 그래프 쿼리 가능
- **Gartner 2025 Critical Capabilities:** 메타데이터 관리 5개 사용 사례 중 3위 이내, 2개 항목 1위

**수집 방식:** SQL 파싱 + API 크롤링 + OpenLineage 런타임 + 수동 혼합  
**컬럼 단위 지원:** ✓  
**잘하는 것:** 가장 넓은 수집 범위, 최고 수준 UX, AI 에이전트 연동(MCP), 제조 레퍼런스

---

### 6-4. Alation

| 항목 | 내용 |
|------|------|
| 유형 | 전용 데이터 카탈로그·계통·거버넌스 플랫폼 |
| 공식 사이트 | https://www.alation.com/ |
| 계통 페이지 | https://www.alation.com/product/data-lineage/ |
| 배포 | 클라우드 SaaS / 온프레미스 (확인 중 — 공식 페이지에서 명시 없음) |

**계통 기능:**
- **자동 SQL 로그 분석:** 웨어하우스·BI 도구의 쿼리 로그를 지속적으로 수집, 자연어 파싱으로 테이블·컬럼 단위 변환 관계 추론
- 2024.1.2부터: Tableau·Power BI 등 BI 시스템 SQL 쿼리 자동 캡처 → 컬럼 단위 계통 생성
- 비즈니스 메타데이터·데이터 품질·신뢰 플래그 오버레이 → "Google Maps 같은" 시각화
- 수동 주석 보완 가능

**수집 방식:** SQL 로그 파싱(쿼리 로그 분석) + 커넥터 자동 수집 + 수동  
**컬럼 단위 지원:** ✓ (2024.1.2 이후 BI 포함 컬럼 계통)  
**잘하는 것:** 자동 SQL 로그 기반 계통, 비즈니스 컨텍스트(신뢰도·품질) 통합 뷰

---

### 6-5. Cloudera Data Lineage (구 Octopai)

| 항목 | 내용 |
|------|------|
| 유형 | 전용 계통 플랫폼 (SaaS, Cloudera 인수) |
| 공식 사이트 | https://www.octopai.com/ (Cloudera로 리다이렉트) |
| 배포 | SaaS |

**계통 기능:**
- 60+ 네이티브 커넥터: 레거시 ETL(Informatica·SSIS·Talend·DataStage·Ab Initio·SAS DI), 엔터프라이즈 BI(Tableau·Power BI·Cognos·MicroStrategy·Qlik·SAP BO), 현대 클라우드 웨어하우스
- 완전 자동 수집 (수동 태깅 없음)
- 계약 후 24시간 이내 첫 계통 그래프 제공 표방
- 온프레미스·클라우드·하이브리드 환경 모두 지원

**수집 방식:** 자동 수집 (커넥터 기반)  
**컬럼 단위 지원:** 확인 필요 (레거시 ETL에서 컬럼 계통 지원 여부 PoC 권장)  
**잘하는 것:** 레거시 ETL 환경(Informatica·SSIS·DataStage 등) 계통 — 비 Hadoop 레거시 특화

---

### 6-6. Select Star

| 항목 | 내용 |
|------|------|
| 유형 | 자동화 데이터 카탈로그·계통 (SaaS) |
| 공식 사이트 | https://www.selectstar.com/ |
| 계통 페이지 | https://www.selectstar.com/product/data-lineage |
| 배포 | SaaS |

**계통 기능:**
- 모든 통합에서 **컬럼 단위 계통 자동 제공**
- 자동 엔티티-관계 다이어그램(ERD) 생성
- dbt 영향도 분석 + GitHub CI 연동

**수집 방식:** 자동 수집 (SQL 파싱·커넥터)  
**컬럼 단위 지원:** ✓  
**잘하는 것:** 쉬운 설정, 자동 ERD 생성, dbt 연동 계통

---

### 6-7. Secoda

| 항목 | 내용 |
|------|------|
| 유형 | AI 기반 엔터프라이즈 데이터 거버넌스·카탈로그 (SaaS) |
| 공식 사이트 | https://www.secoda.co/ |
| 배포 | SaaS |

**계통 기능:**
- 80+ 통합 도구에서 자동 컬럼 단위 계통
- 2025 로드맵: Airflow 계통, 세분화된 역할 기반 접근(RBAC) 추가
- AI 우선 설계 — 메타데이터 탐색·컨텍스트가 빠름

**수집 방식:** 자동 수집 (커넥터 기반)  
**컬럼 단위 지원:** ✓  
**잘하는 것:** AI 우선 UX, 빠른 메타데이터 거버넌스 구축

---

## 7. 솔루션 종합 비교표

| 솔루션 | 유형 | 배포 | 자동수집 방식 | 컬럼단위 | 잘하는 것 | 공식 URL |
|--------|------|------|--------------|---------|----------|---------|
| **OpenLineage** | 오픈 표준 | — (표준 사양) | 런타임 이벤트 (표준) | △ (표준 정의만, 구현은 도구에 따라) | 도구 간 계통 상호운용 표준 | https://openlineage.io/ |
| **Marquez** | OSS 참조구현 | 자체 호스팅 | 런타임 (OpenLineage 이벤트 수신) | △ (이벤트 패싯 저장) | OpenLineage 계통 저장·시각화 참조 | https://marquezproject.ai/ |
| **Apache Atlas** | 오픈소스 | 자체 호스팅 (온프레) | 런타임 훅·커넥터 | ✓ (Hive/Spark SQL) | Hadoop 생태계 거버넌스·계통 | https://atlas.apache.org/ |
| **DataHub** | OSS/상용 | 자체 호스팅 / SaaS | SQL 파싱 + 커넥터 + API | ✓ (v0.14.1+) | 현대 데이터 스택 전반, 80+ 커넥터 | https://datahub.com/ |
| **dbt** | 변환 도구 | CLI (OSS) / SaaS | 정적 분석 (SQL DAG) | ✓ (Enterprise 플랜) | SQL 변환 레이어 모델 DAG·계통 | https://www.getdbt.com/ |
| **Apache Spline** | OSS (Spark 특화) | 자체 호스팅 | 런타임 (Spark 이벤트 리스너) | △ (제한적) | Spark 파이프라인 계통 무료 시각화 | https://absaoss.github.io/spline/ |
| **Databricks Unity Catalog** | 플랫폼 내장 | 클라우드 (Databricks) | 런타임 (쿼리 플랜 자동) | ✓ (SQL·R·Python·Scala) | Databricks 내 전 언어 컬럼 계통 무설정 자동 | https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage |
| **Microsoft Purview** | 플랫폼 내장 | Azure SaaS | 런타임 (Azure 서비스 연동) | 미확인 (PoC 권장) | Azure 스택 엔드투엔드 계통 자동 수집 | https://learn.microsoft.com/en-us/purview/ |
| **Snowflake (내장)** | 플랫폼 내장 | SaaS | 런타임 (SQL 실행 시 자동) | ✓ (사이드 패널 수준) | Snowflake 내 SQL 계통 추가 도구 없이 내장 | https://docs.snowflake.com/en/user-guide/ui-snowsight-lineage |
| **Google Dataplex** | 플랫폼 내장 | GCP SaaS | 런타임 (BigQuery 잡 자동) | ✓ (BigQuery 잡 한정) | GCP·BigQuery 스택 컬럼 계통 GA | https://docs.cloud.google.com/dataplex/docs/about-data-lineage |
| **Collibra Data Lineage** | 전용 상용 | SaaS / 온프레 | 정적 파싱 + OpenLineage | ✓ | 엔터프라이즈 엔드투엔드, 레거시 ETL, 비즈니스·기술 이중 계통 | https://www.collibra.com/products/data-lineage |
| **IBM Manta** | 전용 상용 (IBM) | 온프레 / IBM Cloud | 정적 파싱 (코드·ETL) | ✓ | 레거시 ETL·SQL 정적 파싱 특화, AI 계통 증빙 | https://www.ibm.com/products/manta-data-lineage |
| **Atlan** | 전용 상용 | SaaS | SQL 파싱 + API + OpenLineage + 수동 | ✓ (80+ 시스템) | 최넓은 수집 범위, AI 에이전트 연동(MCP), Gartner 상위 | https://atlan.com/data-lineage/ |
| **Alation** | 전용 상용 | SaaS / 미확인 | SQL 로그 파싱 + 커넥터 + 수동 | ✓ (2024.1.2+) | 자동 SQL 로그 계통, 비즈니스 컨텍스트 통합 | https://www.alation.com/product/data-lineage/ |
| **Cloudera (Octopai)** | 전용 상용 (SaaS) | SaaS | 자동 수집 (60+ 커넥터) | 확인 필요 | 레거시 ETL(Informatica·SSIS 등) + BI 계통 특화 | https://www.octopai.com/ |
| **Select Star** | 전용 상용 (SaaS) | SaaS | SQL 파싱 + 커넥터 | ✓ | 쉬운 설정, 자동 ERD, dbt 연동 | https://www.selectstar.com/product/data-lineage |
| **Secoda** | 전용 상용 (SaaS) | SaaS | 커넥터 기반 자동 | ✓ | AI 우선 UX, 빠른 거버넌스 구축 | https://www.secoda.co/ |

---

## 8. 출처 URL 목록

아래 URL은 WebSearch 결과 또는 WebFetch로 내용 확인한 것. 403 오류·미확인은 표시.

| 솔루션/출처 | URL | 상태 |
|------------|-----|------|
| OpenLineage 공식 사이트 | https://openlineage.io/ | 확인 (WebFetch 200) |
| OpenLineage GitHub | https://github.com/OpenLineage/OpenLineage | 검색 결과 확인 |
| OpenLineage 스펙 문서 | https://openlineage.io/docs/ | 검색 결과 확인 |
| Marquez 공식 사이트 | https://marquezproject.ai/ | 확인 (WebFetch 200) |
| Marquez GitHub | https://github.com/MarquezProject/marquez | 검색 결과 확인 |
| Apache Atlas 공식 | https://atlas.apache.org/ | WebFetch 내용 제한적 (헤더만) — 검색으로 내용 보완 |
| DataHub 공식 | https://datahub.com/ | 확인 (WebFetch 200) |
| DataHub 계통 문서 | https://docs.datahub.com/docs/features/feature-guides/lineage | 확인 (WebFetch 200) |
| dbt 컬럼 계통 문서 | https://docs.getdbt.com/docs/explore/column-level-lineage | 확인 (WebFetch 200) |
| Apache Spline 공식 | https://absaoss.github.io/spline/ | 확인 (WebFetch 200) |
| Spline GitHub | https://github.com/AbsaOSS/spline | 검색 결과 확인 |
| Databricks Unity Catalog 계통 | https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage | 확인 (WebFetch 200) |
| Microsoft Purview 계통 | https://learn.microsoft.com/en-us/purview/data-gov-classic-lineage | 검색 결과 확인 |
| Snowflake 계통 문서 | https://docs.snowflake.com/en/user-guide/ui-snowsight-lineage | 검색 결과 확인 |
| Snowflake ACCESS_HISTORY | https://docs.snowflake.com/en/user-guide/access-history | 검색 결과 확인 |
| Google Dataplex 계통 | https://docs.cloud.google.com/dataplex/docs/about-data-lineage | 검색 결과 확인 |
| Google Dataplex 컬럼 계통 블로그 | https://cloud.google.com/blog/products/data-analytics/dataplex-supports-column-level-lineage-for-bigquery-data | 검색 결과 확인 |
| Collibra Data Lineage | https://www.collibra.com/products/data-lineage | 확인 (WebFetch 200) |
| Collibra 제품 문서 | https://productresources.collibra.com/docs/collibra/latest/Content/CollibraDataLineage/ | 검색 결과 확인 |
| IBM Manta 공식 페이지 | https://www.ibm.com/products/manta-data-lineage | **403 Forbidden — 직접 접근 불가** |
| IBM 인수 발표 | https://newsroom.ibm.com/IBM-acquires-Manta-Software-Inc-to-complement-data-and-AI-governance-capabilities | 검색 결과 확인 |
| Atlan 계통 페이지 | https://atlan.com/data-lineage/ | 확인 (WebFetch 200) |
| Alation 계통 페이지 | https://www.alation.com/product/data-lineage/ | 확인 (WebFetch 200) |
| Cloudera (Octopai) | https://www.octopai.com/ | 검색 결과 확인 (Cloudera로 리다이렉트) |
| Select Star 계통 | https://www.selectstar.com/product/data-lineage | 검색 결과 확인 |
| Secoda | https://www.secoda.co/ | 검색 결과 확인 |

---

## 미확인·주의 항목 정리

1. **Microsoft Purview 컬럼 단위 계통 GA 여부:** Azure 문서에서 테이블 단위는 명확하나 컬럼 단위 GA 범위가 불명확 — PoC 직접 확인 권장
2. **IBM Manta 공식 페이지:** 403 응답으로 직접 접근 불가 — IBM 뉴스룸 발표 및 IBM Docs 기반으로 내용 파악. 현재 IBM Cloud Pak for Data / Software Hub 내 통합 제품으로 운영 중
3. **Cloudera (Octopai) 컬럼 단위 지원 세부:** 레거시 ETL(Informatica, DataStage 등)에서 컬럼 단위 계통 추출 깊이는 PoC 확인 권장
4. **Apache Atlas Hive 외 지원 범위:** Hadoop 외 현대 클라우드 데이터 스택 연동 시 커스텀 개발 필요성 여부 — 공식 문서에서 상세 확인 권장
5. **dbt Core 컬럼 단위 계통:** Enterprise 플랜 전용 — OSS Core에서는 컬럼 단위 계통 비제공
6. **Alation 배포 모델(온프레미스 가능 여부):** 공식 페이지에서 명확히 확인 못 함 — 영업 문의 권장
7. **Egeria(Apache Egeria):** 조사 범위에 포함했으나 Lineage 특화 도구라기보다 메타데이터 상호운용 표준 프레임워크 — 가이드 포함 여부는 작성자 판단 필요

---

*리서치 완료: 2026-06-24 | 확인 방법: WebSearch + WebFetch (직접 URL 접근 또는 검색 결과 교차 확인)*
