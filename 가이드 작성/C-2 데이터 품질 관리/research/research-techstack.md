# C-2 데이터 품질 관리(Data Quality Management) — Tech Stack 리서치 원자료

> 작성일: 2026-06-24 | 조사 범위: 공식 사이트·문서·발표 자료(2024~2026-06 기준)
> 용도: 가이드 작성자용 원자료 — 추측 없이 확인된 사실만 기재, 미확인은 명시
> 관점: "AI/모델을 만드는 법"이 아니라 "AI에 넣을 **데이터를 점검·판정·통제하는 도구**"
> 가격·버전·지원 범위는 단정하지 않는다(PoC·공식 문서 확인 권장)

---

## 주제 경계 메모 (C-2가 무엇을 보는가)

- **C-2 = 품질 판정(Quality Gate).** 데이터가 AI 활용 기준을 충족하는지 "쓸 수 있는가"를 판정하고, AI 투입 전 합/불을 강제하는 통제 체계.
- **C-1 Observability와 겹침:** 데이터 관측(observability) 솔루션은 "운영 중 실시간 이상 감지"가 본업이지만, 같은 엔진이 품질 점검·룰 검증도 수행하므로 본 리서치에 함께 정리한다. **경계:** C-2는 "AI에 써도 되는가" 사전 판정(게이트), C-1은 운영 중 상시 모니터링·이상 알림. 같은 제품(Monte Carlo·Anomalo·Bigeye·Soda Cloud·Databand 등)이 두 역할을 겸한다.
- **C-3 Lineage와 겹침:** 품질 사고가 나면 어디서 왔는지 추적(C-3), 어떤 하위 자산이 영향받는지 파악할 때 계보가 필요. 다수 엔터프라이즈 DQ 제품(Collibra·Informatica·Ataccama)이 계보·카탈로그를 함께 묶는다 — C-3 리서치(`가이드 작성/C-3 데이터 계통 Lineage/research/research-techstack.md`)와 솔루션 명단이 상당 부분 겹친다.

**"규칙 기반 vs ML 이상탐지" 축 (C-2 선정의 핵심):**
- **규칙 기반(Rule-based):** 사람이 "이 컬럼은 NULL 금지·값은 0~100" 같은 합/불 기준을 명시적으로 선언 → 통과/실패가 결정적이고 설명 가능. AI 투입 게이트로 쓰기에 명확. 단 룰을 일일이 작성·유지해야 함. (Great Expectations·Soda·dbt test·Deequ·Glue DQ·DLT expectations)
- **ML 이상탐지(ML/Unsupervised):** 도구가 과거 데이터 패턴을 학습해 "평소와 다른" 변화(분포 이동·볼륨 급감·스키마 변경)를 자동 감지 → 룰을 미리 못 짜는 대규모 테이블에 유리. 단 초기 오탐(false positive)·학습 기간 필요, 합/불 임계가 결정적이지 않을 수 있음. (Monte Carlo·Anomalo·Bigeye·Databand·Collibra DQ·Lakehouse Monitoring)
- 실무는 둘을 **혼합**: 핵심 컬럼·규정 항목은 규칙 게이트로 강제하고, 나머지 넓은 테이블은 ML 이상탐지로 자동 감시.

---

## 목차

1. [솔루션 유형 4분류 개요](#1-솔루션-유형-4분류-개요)
2. [유형 1 — 오픈소스 검증 프레임워크](#2-유형-1--오픈소스-검증-프레임워크)
3. [유형 2 — 데이터 플랫폼 내장형 품질](#3-유형-2--데이터-플랫폼-내장형-품질)
4. [유형 3 — 데이터 관측(Observability, ML 이상탐지)](#4-유형-3--데이터-관측-observability-ml-이상탐지)
5. [유형 4 — 엔터프라이즈 DQ(규칙+정제+거버넌스 통합)](#5-유형-4--엔터프라이즈-dq-규칙정제거버넌스-통합)
6. [솔루션 종합 비교표](#6-솔루션-종합-비교표)
7. [선정 기준 정리 (실무가 고를 때의 축)](#7-선정-기준-정리-실무가-고를-때의-축)
8. [Quality Gate로 파이프라인에 끼우는 패턴](#8-quality-gate로-파이프라인에-끼우는-패턴)
9. [출처 URL 목록](#9-출처-url-목록)
10. [미확인·주의 항목](#10-미확인주의-항목)

---

## 1. 솔루션 유형 4분류 개요

| 유형 | 한 줄 정의 | 대표 솔루션 | 규칙/ML | 대표 배포 |
|------|-----------|------------|---------|----------|
| ① 오픈소스 검증 프레임워크 | 코드/YAML로 품질 규칙을 선언해 파이프라인에서 합·불 판정 | Great Expectations, Soda Core, dbt test/dbt-expectations, Amazon Deequ | 규칙 기반(중심) | 오픈소스·자체 호스팅 |
| ② 플랫폼 내장형 | 이미 쓰는 데이터 플랫폼 안에서 품질 점검 | AWS Glue DQ, Databricks DLT expectations·Lakehouse Monitoring, Google Dataplex AutoDQ, Microsoft Purview/Fabric | 규칙+추천+(일부 ML) | 해당 클라우드 |
| ③ 데이터 관측(ML 이상탐지) | 룰을 일일이 안 짜도 ML이 이상 자동 감지 | Monte Carlo, Anomalo, Bigeye, Soda Cloud, Metaplane | ML 이상탐지(중심) | SaaS(일부 in-VPC) |
| ④ 엔터프라이즈 DQ | 규칙·정제·거버넌스를 한 플랫폼에 통합 | Collibra DQ, Informatica DQ, Ataccama ONE, Qlik Talend, SAP, IBM Databand | 규칙+ML 혼합 | SaaS/온프레/하이브리드 |

---

## 2. 유형 1 — 오픈소스 검증 프레임워크

> 공통 성격: "코드/선언으로 품질 규칙을 정의 → 데이터셋에 돌려 합·불 판정." Quality Gate에 가장 직접적으로 끼우는 도구군. 대부분 규칙 기반이지만 Deequ처럼 메트릭 이력 기반 이상탐지를 겸하는 경우도 있음.

### 2-1. Great Expectations (GX)

| 항목 | 내용 |
|------|------|
| 유형 | 오픈소스 데이터 검증 프레임워크 (Python) + 상용 클라우드(GX Cloud) |
| 라이선스 | Apache 2.0 (GX Core) |
| 관리 주체 | Great Expectations (GX) |
| 공식 사이트 | https://greatexpectations.io/ |
| GX Cloud | https://greatexpectations.io/gx-cloud/ |
| 문서 | https://docs.greatexpectations.io/ |

**무엇을 하나:** 데이터에 대한 기대치(Expectation)를 선언적 단언(assertion)으로 정의 → 데이터셋(Data Asset)에 검증(Validation) 실행 → 합·불 판정 + Data Docs로 결과 문서화. "데이터 품질을 사후 디버깅이 아니라 사전 테스트 규율로" 전환하는 것이 핵심 포지셔닝.

**규칙 vs ML:** **규칙 기반(선언적 Expectation 중심).** ML 자동 이상탐지가 주력은 아님.

**배포:**
- **GX Core(오픈소스):** Python 라이브러리. Apache 2.0, 영구 무료. Jupyter·Python 환경에서 사용.
- **GX Cloud(SaaS):** 완전 관리형 호스팅 + UI + 역할·인증 + 정책 관리. 기본은 GX가 3개 컴포넌트 전부 호스팅, 오케스트레이션 백엔드를 조직/로컬에 두는 대안 배포는 요청 시 제공(공식 문서 명시 — PoC 확인 권장).

**Quality Gate 연결:** Airflow·Spark·Prefect·dbt·Luigi·Jupyter와 통합 → 배치/스트리밍 파이프라인에 검증 단계로 삽입, 실패 시 게이트로 차단 가능.

---

### 2-2. Soda Core / Soda Cloud

| 항목 | 내용 |
|------|------|
| 유형 | 오픈소스 검증 엔진(Soda Core) + SaaS(Soda Cloud) |
| 라이선스 | Apache 2.0 (Soda Core) |
| 관리 주체 | Soda Data (soda.io) |
| 공식 사이트 | https://soda.io/ |
| GitHub | https://github.com/sodadata/soda-core |
| 문서 | https://docs.soda.io/ |

**무엇을 하나:** **SodaCL** — 선언적 YAML 언어로 품질 체크를 정의(스키마·데이터 값 검증). "modern data stack을 위한 Data Contracts 엔진"으로 포지셔닝.

**규칙 vs ML:** **규칙 기반(SodaCL 중심)**, 단 **Soda Cloud(SaaS)에서 이상탐지(anomaly detection)·데이터 계약 추가.**

**배포:**
- **Soda Core(오픈소스):** 무료 Python 라이브러리·CLI. dbt·Airflow·CI/CD 안에서 로컬 실행. **OSS에는 GUI 없음** — YAML + CLI 중심.
- **Soda Cloud(SaaS):** UI·대시보드·알림·이상탐지·데이터 계약 관리. Soda Core 또는 Soda Agent가 결과를 Cloud로 보고. (대시보드·알림·이상탐지·데이터 계약은 다수 기능이 Soda Cloud 필요)

**Quality Gate 연결:** dbt·Airflow·CI/CD 파이프라인에서 체크 실행 → 실패 시 차단. 데이터 계약(Data Contract)으로 게이트화.

---

### 2-3. dbt test / dbt-expectations

| 항목 | 내용 |
|------|------|
| 유형 | 변환 도구 내장 테스트(dbt) + 커뮤니티 테스트 패키지 |
| 라이선스 | Apache 2.0 (dbt Core), 상용(dbt Cloud) / dbt-expectations는 오픈소스 |
| 관리 주체 | dbt Labs / dbt-expectations는 Datadog 유지 |
| dbt 데이터 테스트 문서 | https://docs.getdbt.com/docs/build/data-tests |
| dbt-expectations GitHub | https://github.com/metaplane/dbt-expectations |
| 공식 사이트 | https://www.getdbt.com/ |

**무엇을 하나:**
- **dbt 내장 generic test 4종:** `not_null`, `unique`, `accepted_values`, `relationships` — 변환 모델에 붙여 합/불 판정.
- **dbt-expectations:** Great Expectations 스타일 단언을 dbt에 이식한 오픈소스 패키지(GX 기반 다수 테스트 — 스키마·정규식, 시계열 신선도·완전성, 통계 분포·이상치, 교차 컬럼 로직 등). dbt 기본 테스트가 못 다루는 복잡 검증을 보강.
- (참고) **dbt-utils** — 추가 generic test 다수 제공.

**규칙 vs ML:** **규칙 기반(선언적 테스트).**

**배포:** dbt Core(오픈소스 CLI) / dbt Cloud(SaaS). 패키지는 `packages.yml`로 설치.

**Quality Gate 연결:** `dbt test`로 변환 파이프라인 실행 중 검증 → 실패 시 빌드 중단(게이트). dbt 변환을 쓰는 조직이면 별도 도구 없이 품질 게이트 구성 가능.

> 주의: dbt-expectations는 본래 calogica가 시작, 이후 Metaplane/Datadog 계열이 유지. 깃허브 경로는 이관 이력이 있으니 최신 README로 확인 권장.

---

### 2-4. Amazon Deequ / PyDeequ

| 항목 | 내용 |
|------|------|
| 유형 | Apache Spark 기반 "데이터 단위 테스트" 라이브러리 (오픈소스) |
| 라이선스 | Apache 2.0 |
| 관리 주체 | AWS Labs (awslabs) |
| GitHub (Deequ) | https://github.com/awslabs/deequ |
| GitHub (PyDeequ) | https://github.com/awslabs/python-deequ |
| AWS 블로그 | https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/ |

**무엇을 하나:** 대규모 데이터셋(수십억 행)에 "데이터 단위 테스트(unit tests for data)"를 정의·검증. 선언적 제약(`isComplete`, `isUnique`, `isContainedIn` 등) + 메트릭 분석기/프로파일러 + **MetricsRepository(메트릭 이력 저장)**.

**규칙 vs ML:** **규칙 기반 + 메트릭 이력 기반 이상탐지(anomaly check).** 과거 메트릭과 현재값을 비교해 이상 변화 감지(통계적 임계 기반 — 본격 ML보다는 통계 기반). 즉 두 모드를 다 가짐.

**배포:** Spark 위에서 실행되는 오픈소스 라이브러리(Scala=Deequ, Python=PyDeequ). 자체 Spark/EMR/Glue 환경에 설치. **AWS Glue Data Quality가 이 Deequ를 기반으로 만든 관리형 서비스**(2-5 참조).

**Quality Gate 연결:** Spark 배치 파이프라인·데이터 레이크 적재 단계에서 검증 → 실패 시 차단. PyDeequ + AWS Glue로 데이터 레이크 품질 모니터링 패턴이 AWS 공식 블로그에 정리됨.

---

## 3. 유형 2 — 데이터 플랫폼 내장형 품질

> 공통 성격: 이미 쓰는 데이터 플랫폼(AWS·Databricks·GCP·Azure) 안에서 품질 점검. 별도 도구 도입·데이터 반출 없이 게이트 구성 가능 → "이미 그 플랫폼을 쓰면" 1순위. C-3 리서치의 플랫폼 내장 계통(Unity Catalog·Dataplex·Purview)과 같은 플랫폼 안 기능.

### 3-1. AWS Glue Data Quality (DQDL)

| 항목 | 내용 |
|------|------|
| 유형 | AWS Glue 내장 관리형 데이터 품질 (서버리스) |
| 공식 문서 | https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html |
| DQDL 레퍼런스 | https://docs.aws.amazon.com/glue/latest/dg/dqdl.html |
| 배포 | AWS (관리형·서버리스) |

**무엇을 하나:** **DQDL(Data Quality Definition Language)** — 도메인 특화 언어로 품질 규칙 정의(`RowCount > 5` 등 분석기+불리언 표현식). 데이터셋에 규칙을 평가해 신선도·무결성 등 측정. **오픈소스 Deequ 위에 구축된 관리형·서버리스** 경험.

**규칙 vs ML:** **규칙 기반 + 규칙 자동 추천.** "Recommend rules" 2-클릭으로 컬럼별 데이터를 분석해 후보 규칙 자동 생성. (2024년 DQDL 강화: NOT 연산자, NULL/EMPTY/WHITESPACES_ONLY 키워드, 복합 규칙, WHERE 절 등 추가)

**배포:** AWS Glue/Glue Studio·Data Catalog 내장(서버리스). AWS 밖 반출 없음.

**Quality Gate 연결:** Glue Studio ETL 잡에 품질 평가 노드 삽입 → 규칙 통과/실패에 따라 분기·차단. Data Catalog 테이블 대상 품질 규칙도 지원.

---

### 3-2. Databricks — Delta Live Tables(Lakeflow) Expectations & Lakehouse Monitoring

| 항목 | 내용 |
|------|------|
| 유형 | Databricks 플랫폼 내장 품질(파이프라인 expectations + 테이블 모니터링) |
| DQ 개요 | https://www.databricks.com/discover/pages/data-quality-management |
| Expectations 문서 | https://learn.microsoft.com/en-us/azure/databricks/ldp/expectations |
| Lakehouse Monitoring | https://learn.microsoft.com/en-us/azure/databricks/lakehouse-monitoring/ |
| 배포 | Databricks 플랫폼 (AWS/Azure/GCP) |

**무엇을 하나 — 두 축:**
- **DLT(현 Lakeflow) Expectations:** 파이프라인 정의에 선언적 품질 체크(expectation)를 넣어 레코드별 검증. **`ON VIOLATION` 절**로 위반 데이터 처리 방식 3가지 선택 — 유지(retain) / 폐기(drop) / 실패(fail). → 적재 시점(write-time) 게이트.
- **Lakehouse Monitoring:** Unity Catalog 테이블을 모니터링하면 프로파일링·드리프트(drift) 메트릭을 자동 생성. 분석 3종 — 시계열(time series)·스냅샷(snapshot)·추론(inference, 모델 입력·예측 모니터링). 메트릭 테이블 2개 + 대시보드 생성.

**규칙 vs ML:** Expectations는 **규칙 기반(선언)**, Lakehouse Monitoring은 **프로파일·드리프트 메트릭 자동 생성(통계 기반 모니터링)** → 두 성격 모두.

**배포:** Databricks 플랫폼 내장. 데이터가 플랫폼 안에 머묾.

**Quality Gate 연결:** DLT expectations의 `ON VIOLATION fail`로 bad data 적재를 차단(게이트). Lakehouse Monitoring 추론 분석으로 모델 입력 데이터를 상시 점검 → AI 투입 데이터 품질 감시.

---

### 3-3. Google Cloud Dataplex — Auto Data Quality(AutoDQ) & Data Profiling

| 항목 | 내용 |
|------|------|
| 유형 | Google Cloud Dataplex 내장 데이터 품질·프로파일링 |
| AutoDQ 문서 | https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview |
| GA 블로그 | https://cloud.google.com/blog/products/data-analytics/dataplex-data-profiling-and-automatic-data-quality-are-ga |
| 배포 | Google Cloud (관리형·서버리스) |

**무엇을 하나:** 테이블에 "데이터 스캔(data scan)" 생성 — **데이터 프로파일 스캔**(컬럼 통계·분포 자동 산출) + **AutoDQ 스캔**(품질 규칙). **규칙 자동 추천 + UI 규칙 빌더**, 사전 정의 규칙 타입 또는 SQL로 규칙 작성. 행 필터(row filter)로 세그먼트·컴플라이언스 대상 좁히기 가능. 메트릭을 BigQuery 테이블로 내보내 다운스트림(드리프트 감지 등) 구축.

**규칙 vs ML:** **규칙 기반 + 규칙 자동 추천 + 프로파일링.**

**배포:** GCP 내장(서버리스). 데이터 GCP 내 유지.

**Quality Gate 연결:** BigQuery 중심 GCP 스택의 적재·변환 후 품질 스캔 → 결과를 BigQuery로 내보내 게이트·드리프트 감지 파이프라인 구성. (참고: Dataplex는 컬럼 단위 계통도 제공 — C-3와 연계)

---

### 3-4. Microsoft Purview / Microsoft Fabric — Data Quality

| 항목 | 내용 |
|------|------|
| 유형 | Microsoft Purview Unified Catalog 내장 데이터 품질 (Fabric 연동) |
| DQ 문서 | https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality |
| Fabric Lakehouse DQ | https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-fabric-lakehouse |
| DQ 스캔 실행 | https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-scan |
| 배포 | Azure / Microsoft Fabric (관리형 SaaS) |

**무엇을 하나:** Purview Unified Catalog에서 **6개 표준 품질 차원 기본 규칙** 제공 — 완전성(completeness)·일관성(consistency)·적합성(conformity)·정확성(accuracy)·신선도(freshness)·고유성(uniqueness). **AI 통합 경험으로 규칙 자동 생성**, 사용자 정의 규칙은 함수·표현식으로 작성. 데이터 프로파일링(AI가 프로파일 대상 컬럼 추천, 사람이 보정) → 규칙 적용 → DQ 스캔 실행.

**규칙 vs ML:** **규칙 기반 + AI 보조 규칙 생성·프로파일링.**

**배포:** Azure/Microsoft Fabric SaaS. (Fabric 테이블은 Delta 또는 Iceberg 형식 요구)

**Quality Gate 연결:** Fabric Lakehouse 연결 → 프로파일·규칙·DQ 스캔. 카탈로그(Purview)와 묶여 거버넌스·품질 통합 — A-1 카탈로그 묶음(C-3 리서치 묶음①)과 동일 플랫폼.

> 주의: 크로스 테넌트(cross-tenant) 시나리오에서 원격 Delta 테이블 직접 프로파일링·DQ 규칙 적용에 제약이 보고됨(커뮤니티) — PoC 확인 권장.

---

## 4. 유형 3 — 데이터 관측 (Observability, ML 이상탐지)

> 공통 성격: 룰을 일일이 안 짜도 **ML이 과거 패턴을 학습해 이상을 자동 감지**(신선도·볼륨·스키마·분포 변화). 대규모 테이블·"무엇이 틀릴지 모르는" 영역에 강함. **C-1 Observability와 정확히 겹치는 영역** — C-2 관점에서는 "AI 투입 전·중 데이터가 평소와 다른가"를 자동 판정하는 보조 게이트로 본다. 대부분 SaaS(일부 in-VPC).

### 4-1. Monte Carlo

| 항목 | 내용 |
|------|------|
| 유형 | 엔터프라이즈 데이터+AI 관측 플랫폼 (SaaS) |
| 공식 사이트 | https://www.montecarlodata.com/ |
| 플랫폼 페이지 | https://www.montecarlodata.com/platform/ |
| 배포 | SaaS (AWS Marketplace 제공) |

**무엇을 하나:** ML 기반 이상탐지로 데이터 품질을 모니터링·알림. 데이터 웨어하우스·레이크·ETL·BI·AI 도구 전반에 걸친 엔드투엔드 관측. 다섯 기둥(신선도 Freshness·볼륨 Volume·스키마 Schema·품질·계통). ML로 데이터 기준선(baseline)을 학습해 임계 설정·룰 작성 없이 이상 감지. 필드 단위 계통 자동 생성.

**규칙 vs ML:** **ML 이상탐지 중심**(룰도 병행 가능). "circuit breaker(회로 차단기)" — 룰/모니터 실패 시 파이프라인 자동 정지로 bad data 전파 차단(Monte Carlo가 해당 패턴을 제품화).

**배포:** SaaS(에이전트 메타데이터 수집 기반).

**Quality Gate 연결:** circuit breaker로 다운스트림(대시보드·모델) 적재 전 차단. AI 투입 데이터 상시 감시.

---

### 4-2. Anomalo

| 항목 | 내용 |
|------|------|
| 유형 | ML 네이티브 데이터 품질 모니터링 (SaaS / in-VPC / 온프레) |
| 공식 사이트 | https://www.anomalo.com/ |
| 배포 | SaaS, in-VPC, 온프레미스, 하이브리드 |

**무엇을 하나:** **비지도 ML(unsupervised)**로 데이터의 비정상 패턴(스키마·볼륨·분포·이상치)을 자동 감지. "no code·no SQL" — 룰을 미리 작성하지 않아도 정상 패턴을 자율 학습해 편차를 표면화. 자연어로 정의한 기준에서의 이탈을 Data Quality Agent가 모니터링.

**규칙 vs ML:** **ML(비지도) 이상탐지 중심.** 룰 작성 부담이 가장 적음 — 단 초기 오탐을 피드백으로 학습시켜야 함.

**배포:** **유연한 배포 — SaaS / in-VPC("fully in your VPC") / 온프레 / 하이브리드. "데이터가 환경 밖으로 나가지 않아도 됨"** → 사외 반출 제한 환경에 적합한 ML 관측 옵션.

**Quality Gate 연결:** 대규모(수천 테이블) 데이터 자산에서 룰 유지가 비현실적일 때 자동 감지 게이트. AI 투입 데이터의 분포 이상 감시.

> 포지셔닝 비교: Monte Carlo = 넓은 관측(broad observability), Anomalo = 깊은 이상탐지(deep anomaly detection)로 시장에서 대비됨.

---

### 4-3. Bigeye

| 항목 | 내용 |
|------|------|
| 유형 | 데이터 관측·품질 플랫폼 (SQL-native), 최근 "AI Trust Platform" 포지셔닝 |
| 공식 사이트 | https://www.bigeye.com/ |
| 배포 | SaaS (상세는 영업/문서 확인 — 홈에 명시 적음) |

**무엇을 하나:** 데이터 파이프라인 모니터링·이상 감지. 모든 것을 쿼리 가능한 메타데이터로 노출하는 **SQL-native** 접근 — 기존 엔지니어링 도구·CI/CD에 관측을 통합. 정밀 이상탐지·계통 추적·자동 추천·모니터링 로직 완전 제어. (최근 페이지는 PII/PHI/PCI 민감 데이터 분류, AI 앱 접근 정책, AI Guardian 런타임 강제 등 AI 신뢰 모듈로 확장)

**규칙 vs ML:** **ML/AI 기반 이상탐지 + 코드화된 모니터(SQL)**. 엔지니어링 팀이 모니터링 로직을 코드로 관리·제어하기 좋음.

**배포:** SaaS(홈에 배포 옵션 명시 적음 — PoC/문서 확인). Snowflake·Claude Code 통합 무료 체험 언급.

**Quality Gate 연결:** CI/CD·코드화 파이프라인에 관측 통합 → 메타데이터 임계로 게이트.

---

### 4-4. Soda Cloud (→ 2-2 Soda 참조)

오픈소스 Soda Core(규칙 기반)에 **이상탐지·데이터 계약·UI·알림**을 더한 SaaS 층. 규칙(SodaCL)과 ML 이상탐지를 한 제품에서 겸함 → 유형①(OSS)과 유형③(관측)에 걸침. 공식: https://soda.io/ · 문서 https://docs.soda.io/

---

### 4-5. Metaplane

| 항목 | 내용 |
|------|------|
| 유형 | 경량 메타데이터 기반 데이터 관측 (SaaS), Datadog가 인수 |
| 공식 사이트 | https://www.metaplane.dev/ |
| 배포 | SaaS (read-only 메타데이터 기반) |

**무엇을 하나:** 빠른 셋업(자칭 15~30분)·자가 서비스형 관측. 웨어하우스+변환 도구(dbt 등)에 연결하면 테이블 신선도·행 수·스키마 변경 등 모니터를 자동 생성. read-only 메타데이터 기반 → 엔지니어링 부담 적음. (Datadog 인수 — Datadog 데이터 관측으로 통합 진행)

**규칙 vs ML:** **ML 기반 자동 모니터 + 메타데이터 중심.** 중견·소규모 팀, 빠른 셀프서비스에 적합.

**배포:** SaaS(read-only).

**Quality Gate 연결:** dbt 파이프라인에 자동 모니터 → 이상 시 알림·게이트.

---

## 5. 유형 4 — 엔터프라이즈 DQ (규칙+정제+거버넌스 통합)

> 공통 성격: 대기업용. 품질 **규칙 + 데이터 정제(cleansing) + 프로파일링 + 거버넌스/카탈로그/계통**을 한 플랫폼에 통합. 규칙과 ML을 혼합하고, 온프레/하이브리드 배포가 가능한 경우가 많아 규제·사외 반출 제한 환경에 자주 채택. C-3 리서치의 통합 거버넌스 플랫폼(Collibra·Informatica·Ataccama)과 솔루션이 겹침.

### 5-1. Collibra Data Quality & Observability (구 OwlDQ)

| 항목 | 내용 |
|------|------|
| 유형 | 엔터프라이즈 데이터 품질·관측 (Collibra 플랫폼) |
| 공식 사이트 | https://www.collibra.com/products/data-quality-and-observability |
| 출처(OwlDQ 인수) | https://www.prnewswire.com/news-releases/collibra-acquires-predictive-data-quality-vendor-owldq-301220863.html |
| 배포 | 고객 자체 환경(self-hosted) 등 — 유연 |

**무엇을 하나:** 2021년 2월 **OwlDQ(예측형 데이터 품질) 인수** → Collibra Data Quality로 통합. ML로 이상 감지·**품질 규칙 자동 생성**·복제 오류 보정. **적응형 규칙(adaptive rules)** — ML이 SQL 기반·설명 가능·적응형 규칙을 자동 생성해 데이터 변화에 맞춰 진화(수기 룰 부담↓, 커버리지↑). 자동·사용자 정의 모니터링 + 상세 프로파일링 + 즉시 알림. 데이터 구조 변화·분포 이동 자동 플래그.

**규칙 vs ML:** **규칙 + ML 혼합(자동생성 적응형 규칙).** Collibra 카탈로그·거버넌스·계통(C-3)과 통합.

**배포:** 고객 자체 환경 배포 등 유연(공식 — 상세는 PoC 확인).

**Quality Gate 연결:** 자동 규칙으로 광범위 커버리지 + 거버넌스 워크플로 안에서 품질 게이트.

---

### 5-2. Informatica Data Quality (CLAIRE)

| 항목 | 내용 |
|------|------|
| 유형 | 엔터프라이즈 데이터 품질 (IDMC 클라우드) + AI 엔진 CLAIRE |
| 공식 사이트 | https://www.informatica.com/products/data-quality/cloud-data-quality-radar.html |
| CLAIRE DQ | https://www.informatica.com/resources/articles/claire-gpt-data-quality.html |
| 배포 | Intelligent Data Management Cloud(IDMC) — 클라우드(멀티) |

**무엇을 하나:** **CLAIRE AI 엔진**이 프로파일에 자동 실행되어 품질 이슈 탐지 + **규칙 자동 추천·생성**(완전성·고유성·유효성 등). 사용자가 승인하면 규칙을 적용. CLAIRE가 핵심 비즈니스 요소·이식 가능한 규칙·물리 자산 메타데이터를 결합해 Cloud Data Quality에서 규칙 실행 잡 생성. **CLAIRE Data Quality Agents(Public Preview)** — 자연어 비즈니스 명세로 규칙 생성·평가·운영화.

**규칙 vs ML:** **규칙 + AI(CLAIRE) 자동 추천/생성.** MDM·카탈로그·거버넌스와 통합되는 대형 스위트.

**배포:** IDMC 클라우드(멀티클라우드). (온프레/하이브리드 세부는 PoC·영업 확인 권장)

**Quality Gate 연결:** 프로파일 기반 규칙을 파이프라인 품질 잡으로 실행. 대규모 거버넌스 환경의 표준 게이트.

---

### 5-3. Ataccama ONE

| 항목 | 내용 |
|------|------|
| 유형 | 통합 데이터 신뢰 플랫폼 (품질+관측+계통+카탈로그+MDM) |
| 공식 사이트 | https://www.ataccama.com/platform/data-quality |
| 플랫폼 | https://www.ataccama.com/platform |
| 문서 | https://docs.ataccama.com/one/latest/overview.html |
| 배포 | SaaS / PaaS / 온프레 / 하이브리드 |

**무엇을 하나:** **데이터 품질·관측·계통·카탈로그·참조데이터(MDM)를 한 플랫폼에 통합.** **ONE AI Agent("디지털 데이터 스튜어드")**가 품질 규칙을 생성·테스트·배포. Agentic AI로 검증·모니터링·정제(remediation) 워크플로를 엔드투엔드 자동화. 데이터셋 프로파일링으로 패턴·분포 감지 → 정밀 규칙 생성. (2026 Gartner Augmented Data Quality Solutions Magic Quadrant 리더 — 5년 연속, 벤더 주장)

**규칙 vs ML:** **규칙 + Agentic AI(자동 생성·정제) 혼합.**

**배포:** **SaaS/PaaS(Ataccama 운영) + 온프레 + 하이브리드(분산·엣지, "데이터를 이동하지 않고 처리").** 사외 반출 제한·온프레 요구에 적합.

**Quality Gate 연결:** AI 에이전트가 규칙 생성·배포 → 파이프라인 품질 게이트 + 정제 자동화.

---

### 5-4. Qlik Talend Data Quality (Trust Score / Trust Score for AI)

| 항목 | 내용 |
|------|------|
| 유형 | 데이터 통합·품질·거버넌스 (Qlik Talend Cloud) |
| 공식 사이트 | https://www.qlik.com/us/products/data-quality-governance |
| Talend DQ | https://www.talend.com/products/data-quality/ |
| Trust Score for AI(보도자료) | https://www.qlik.com/us/news/company/press-room/press-releases/qlik-releases-trust-score-for-ai-in-qlik-talend-cloud |
| 배포 | Qlik Talend Cloud(클라우드 네이티브) / Talend Studio |

**무엇을 하나:** **Talend Trust Score™** — 여러 품질 메트릭을 0~5 단일 점수로 집계하는 전역 품질 지표. 지속적 프로파일링·정제(cleansing)·이상탐지. **Qlik Trust Score™ for AI(GA)** — 데이터가 "AI에 정말 준비됐는가"를 AI 특화 차원으로 점수화(Qlik Talend Cloud 포함). ← **C-2 "AI 투입 적합성 판정" 관점에 직접 부합.**

**규칙 vs ML:** **규칙 + 자동 프로파일링/이상탐지 + 점수화.**

**배포:** Qlik Talend Cloud(클라우드 네이티브) + Talend Studio(데이터 프로파일링·DQ). (온프레 세부는 확인 권장)

**Quality Gate 연결:** Trust Score 임계로 AI/분석 투입 적합성 게이트. point-and-click 파이프라인.

---

### 5-5. IBM Databand

| 항목 | 내용 |
|------|------|
| 유형 | 데이터 파이프라인 관측·이상탐지 (IBM) |
| 공식 사이트 | https://www.ibm.com/products/databand |
| 파이프라인 모니터링 | https://www.ibm.com/products/databand/data-pipeline-monitoring |
| 이상탐지 | https://www.ibm.com/products/databand/data-anomaly-detection |
| 배포 | IBM (데이터 fabric·modern data stack 연동) |

**무엇을 하나:** 데이터 파이프라인·웨어하우스 관측 — 메타데이터 자동 수집, 파이프라인/런/태스크 모니터링으로 이상 감지·알림 분류·품질 이슈 보정. **ML 기반 자가학습(self-learning) 모니터링** — 과거 데이터 행동을 관측해 임계 초과 편차 식별(룰 최소 구성). Airflow·IBM DataStage 등과 통합. 심각도순 알림 단일 뷰 + 즉시 사용 메트릭(런 시간·입력/출력 수) + 사용자 정의 임계.

**규칙 vs ML:** **ML 자가학습 이상탐지 중심 + 사용자 정의 임계.** (유형③ 관측과 성격이 같으나 IBM 거버넌스 스택 일부 — watsonx 연계)

**배포:** IBM(클라우드/연동 — 세부 PoC 확인).

**Quality Gate 연결:** 파이프라인 런 이상·품질 편차 감지 → AI 투입 전 데이터 신뢰 확보.

---

### 5-6. SAP — Information Steward / Datasphere

| 항목 | 내용 |
|------|------|
| 유형 | SAP 데이터 품질·스튜어드십 (온프레 Information Steward + 클라우드 Datasphere) |
| Information Steward | https://www.sap.com/products/technology-platform/data-profiling-steward.html |
| Datasphere | https://www.sap.com/products/technology-platform/datasphere.html |
| 배포 | 온프레(Information Steward) / 클라우드(Datasphere, BTP) |

**무엇을 하나:**
- **SAP Information Steward:** 데이터 프로파일링·모니터링·정보정책 관리 단일 플랫폼 — 품질 발견·평가·정의·모니터·개선. 대시보드·스코어카드로 품질 리포트, cleansing package builder로 정제 배포. 데이터 프로파일링+계통+메타데이터 결합.
- **SAP Datasphere:** BTP 기반 차세대 데이터 서비스(구 Data Warehouse Cloud) — 카탈로그·시맨틱 모델링·통합·거버넌스. 온프레 Information Steward 자산을 클라우드로 확장하는 방향(SAP 발표).

**규칙 vs ML:** 규칙·프로파일링 기반(전통적 DQ). SAP 데이터 중심 환경에 적합.

**배포:** Information Steward(온프레) / Datasphere(클라우드 BTP).

**Quality Gate 연결:** SAP 데이터(ERP 등) 품질 스코어카드·정제로 SAP 중심 AI/분석 투입 데이터 정비.

---

## 6. 솔루션 종합 비교표

| 솔루션 | 유형 | 규칙/ML | 배포 | Quality Gate 연결 | 잘하는 것 | 공식 URL |
|--------|------|---------|------|------------------|----------|---------|
| **Great Expectations** | ① OSS 프레임워크 | 규칙(선언 Expectation) | OSS(Python) / GX Cloud(SaaS) | Airflow·Spark·dbt 검증 단계 삽입 | 선언적 품질 테스트·문서화(Data Docs), 생태계 넓음 | https://greatexpectations.io/ |
| **Soda Core / Cloud** | ① OSS + ③ 관측 | 규칙(SodaCL) + Cloud 이상탐지 | Core(OSS) / Cloud(SaaS) | dbt·Airflow·CI/CD, 데이터 계약 | YAML 선언 품질·데이터 계약, OSS+SaaS 이중 | https://soda.io/ |
| **dbt test / dbt-expectations** | ① OSS 프레임워크 | 규칙(테스트) | dbt Core(OSS) / dbt Cloud | `dbt test` 빌드 중 검증·차단 | dbt 변환 파이프라인 내장 품질 게이트 | https://docs.getdbt.com/docs/build/data-tests |
| **Amazon Deequ / PyDeequ** | ① OSS 프레임워크 | 규칙 + 메트릭 이력 이상탐지 | OSS(Spark/Scala·Python) | Spark 배치·레이크 적재 검증 | 대규모 Spark "데이터 단위 테스트", Glue DQ의 기반 | https://github.com/awslabs/deequ |
| **AWS Glue Data Quality** | ② 플랫폼 내장 | 규칙(DQDL) + 자동 추천 | AWS(서버리스) | Glue Studio ETL 노드 분기·차단 | AWS 내장·서버리스, Deequ 기반 관리형 | https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html |
| **Databricks DLT Expectations + Lakehouse Monitoring** | ② 플랫폼 내장 | 규칙(expectation) + 프로파일·드리프트 | Databricks(AWS/Azure/GCP) | `ON VIOLATION fail`로 적재 차단 | Databricks 내 write-time 게이트 + 모델 입력 모니터 | https://www.databricks.com/discover/pages/data-quality-management |
| **Google Dataplex AutoDQ** | ② 플랫폼 내장 | 규칙 + 자동 추천 + 프로파일 | GCP(서버리스) | 스캔 결과 BigQuery 내보내 게이트 | BigQuery·GCP 스택 자동 품질·프로파일 | https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview |
| **Microsoft Purview / Fabric DQ** | ② 플랫폼 내장 | 규칙(6차원) + AI 보조 | Azure/Fabric SaaS | Fabric Lakehouse 프로파일·규칙·스캔 | Azure·Fabric 카탈로그+품질 통합 | https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality |
| **Monte Carlo** | ③ 관측(ML) | ML 이상탐지(룰 병행) | SaaS | circuit breaker로 파이프라인 정지 | 넓은 데이터+AI 관측, ML 기준선 자동 | https://www.montecarlodata.com/ |
| **Anomalo** | ③ 관측(ML) | ML 비지도 이상탐지 | SaaS / in-VPC / 온프레 / 하이브리드 | 자동 감지 게이트, no-code | 룰 없이 깊은 이상탐지, 사외 반출 제한 가능 | https://www.anomalo.com/ |
| **Bigeye** | ③ 관측(ML) | ML 이상탐지 + SQL 모니터 | SaaS(상세 확인) | CI/CD·메타데이터 임계 게이트 | SQL-native, 모니터 코드 제어, AI 신뢰 모듈 | https://www.bigeye.com/ |
| **Metaplane** | ③ 관측(ML) | ML 자동 모니터 | SaaS(read-only) | dbt 자동 모니터·알림 | 15~30분 빠른 셋업, 중견·소규모 팀(Datadog 인수) | https://www.metaplane.dev/ |
| **Collibra Data Quality** | ④ 엔터프라이즈 | 규칙 + ML 적응형 자동생성 | 고객 자체 환경 등 | 자동 규칙 + 거버넌스 워크플로 게이트 | 적응형 규칙 자동생성, 카탈로그·거버넌스 통합 | https://www.collibra.com/products/data-quality-and-observability |
| **Informatica Data Quality (CLAIRE)** | ④ 엔터프라이즈 | 규칙 + AI 자동 추천/생성 | IDMC 클라우드 | 프로파일 기반 규칙 잡 실행 | CLAIRE AI 규칙 생성, MDM·거버넌스 대형 스위트 | https://www.informatica.com/products/data-quality/cloud-data-quality-radar.html |
| **Ataccama ONE** | ④ 엔터프라이즈 | 규칙 + Agentic AI | SaaS/PaaS/온프레/하이브리드 | AI 에이전트 규칙 생성·배포 + 정제 | 품질+관측+계통+카탈로그+MDM 통합, 온프레 가능 | https://www.ataccama.com/platform/data-quality |
| **Qlik Talend Data Quality** | ④ 엔터프라이즈 | 규칙 + 프로파일/이상탐지 + 점수 | Qlik Talend Cloud / Studio | Trust Score 임계로 AI 적합성 게이트 | Trust Score(0~5)·**Trust Score for AI**, AI 준비도 점수화 | https://www.qlik.com/us/products/data-quality-governance |
| **IBM Databand** | ④ 엔터프라이즈(관측) | ML 자가학습 이상탐지 | IBM(연동) | 파이프라인 런 이상 감지·알림 | 파이프라인 관측·자가학습, Airflow·DataStage 연동 | https://www.ibm.com/products/databand |
| **SAP Information Steward / Datasphere** | ④ 엔터프라이즈 | 규칙·프로파일링 | 온프레(IS) / 클라우드(Datasphere) | SAP 데이터 품질 스코어카드·정제 | SAP 데이터(ERP) 중심 품질·스튜어드십 | https://www.sap.com/products/technology-platform/data-profiling-steward.html |

> 범례: 유형① 오픈소스 검증 프레임워크 / ② 플랫폼 내장형 / ③ 데이터 관측(ML) / ④ 엔터프라이즈 DQ

---

## 7. 선정 기준 정리 (실무가 고를 때의 축)

| 축 | 핵심 질문 | 어느 쪽이면 무엇 |
|----|----------|----------------|
| ① 규칙 vs ML | 합/불 기준을 명시할 수 있나, 아니면 "무엇이 틀릴지" 모르나 | 명시 가능·규정 항목 → **규칙 기반**(GX·Soda·dbt·Deequ·Glue DQ·DLT). 대규모·미지 패턴 → **ML 이상탐지**(Monte Carlo·Anomalo·Bigeye·Databand). 보통 **혼합** |
| ② 배포 | 데이터 사외 반출이 제한되나 | 제한 시 → **오픈소스 자체 호스팅**(GX·Soda Core·Deequ·dbt) 또는 **온프레/in-VPC 가능 상용**(Anomalo in-VPC·Ataccama 온프레·Collibra 자체환경·SAP IS 온프레). 제한 없으면 SaaS도 가능 |
| ③ 기존 플랫폼 연동 | 이미 Databricks/AWS/GCP/Azure를 쓰나 | 쓰면 → **내장형 1순위**(Databricks DLT·Glue DQ·Dataplex·Purview) — 도구 추가·반출 없이 게이트 |
| ④ Quality Gate 삽입 | 파이프라인에 합/불로 끼울 수 있나 | DLT `ON VIOLATION fail`·dbt test 빌드 중단·Monte Carlo circuit breaker·Glue Studio 분기 등 — "실패 시 차단"이 되는지 확인 |
| ⑤ 계보·카탈로그 연계 | 사고 추적(C-3)·자산 등록(A-1)과 묶을까 | 묶을 거면 → **통합 거버넌스형**(Collibra·Informatica·Ataccama·Purview) — 품질+계통+카탈로그 한 플랫폼. C-3 리서치 솔루션과 겹침 |

**추가 판단 메모:**
- "AI 준비도 판정"을 점수로 명시하고 싶으면 **Qlik Trust Score for AI**가 그 관점에 가장 직접적(단 Qlik Talend Cloud 종속).
- 오픈소스 4종은 무료지만 **UI·알림·이상탐지·협업은 대체로 상용/Cloud 층 필요**(GX Cloud·Soda Cloud·dbt Cloud) — "코드로 게이트만" 필요하면 OSS로 충분.
- 유형③ 관측은 C-1과 같은 제품 — 가이드에서 "C-2는 게이트, C-1은 상시 모니터링" 경계를 명시하고 솔루션 중복은 2층 정본으로 링크 권장.

---

## 8. Quality Gate로 파이프라인에 끼우는 패턴

C-2의 핵심은 "점검"이 아니라 "**합/불로 막는 것**"이다. 솔루션이 게이트가 되는 대표 패턴:

- **검증 단계 삽입(validation step):** ETL/변환 파이프라인 중간에 검증 작업을 두고, 실패 시 후속 단계 중단. 예) `dbt test`, Great Expectations Checkpoint, Soda scan, Glue Studio 품질 노드.
- **적재 시점 게이트(write-time):** 적재(write) 직전 레코드별 검증 → 위반 시 폐기/격리/실패. 예) Databricks DLT expectations `ON VIOLATION`(retain/drop/fail).
- **회로 차단기(circuit breaker):** 오류율·불량 레코드가 임계 초과 시 잡을 자동 정지 → bad data가 공유 데이터셋·다운스트림·모델로 전파되기 전 차단하고 사람 판단을 강제. 예) Monte Carlo circuit breaker.
- **격리/검역(quarantine):** 실패 데이터를 버리지 않고 별도 영역으로 보내 사람 검토 → AI 학습에 조용히 들어가지 않게. (Databricks 격리 패턴, 일반 ingestion 패턴)
- **AI 준비도 점수 임계:** 데이터 신뢰 점수(예 Trust Score)가 기준 미달이면 AI/분석 투입 보류. 예) Qlik Trust Score for AI.

> 업계 정리(개념): 품질 게이트는 "스키마·필수 필드·기본 분포 규칙을 검증해 production을 떠받치는 sink에 쓰기 전 bad data 전파를 막는 검사"로 설명됨(CI/CD 단계마다 자동 검증 권장). AI 학습 관점: "검증 실패 데이터는 조용히 학습에 들어가지 않고 검토로 플래그"가 권장 패턴.

---

## 9. 출처 URL 목록

아래 URL은 WebSearch 결과 또는 WebFetch로 내용 확인한 것. 미확인·주의는 표시.

| 솔루션/출처 | URL | 상태 |
|------------|-----|------|
| Great Expectations 공식 | https://greatexpectations.io/ | 검색 결과 확인(공식) |
| GX Cloud | https://greatexpectations.io/gx-cloud/ | 검색 결과 확인 |
| GX 문서 | https://docs.greatexpectations.io/ | 검색 결과 확인 |
| Soda 공식 | https://soda.io/ | 검색 결과 확인 |
| Soda Core GitHub | https://github.com/sodadata/soda-core | 검색 결과 확인 |
| Soda 문서 | https://docs.soda.io/ | 검색 결과 확인 |
| dbt 데이터 테스트 문서 | https://docs.getdbt.com/docs/build/data-tests | 검색 결과 확인 |
| dbt-expectations GitHub | https://github.com/metaplane/dbt-expectations | 검색 결과 확인(이관 이력 — README 재확인 권장) |
| dbt 공식 | https://www.getdbt.com/ | 기지 |
| Amazon Deequ GitHub | https://github.com/awslabs/deequ | 검색 결과 확인 |
| PyDeequ GitHub | https://github.com/awslabs/python-deequ | 검색 결과 확인 |
| Deequ AWS 블로그 | https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/ | 검색 결과 확인 |
| AWS Glue Data Quality 문서 | https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html | 검색 결과 확인 |
| AWS Glue DQDL 레퍼런스 | https://docs.aws.amazon.com/glue/latest/dg/dqdl.html | 검색 결과 확인 |
| Databricks DQ 개요 | https://www.databricks.com/discover/pages/data-quality-management | 검색 결과 확인 |
| Databricks(Azure) Expectations 문서 | https://learn.microsoft.com/en-us/azure/databricks/ldp/expectations | 검색 결과 확인 |
| Databricks Lakehouse Monitoring | https://learn.microsoft.com/en-us/azure/databricks/lakehouse-monitoring/ | 검색 결과 확인(경로 재확인 권장) |
| Google Dataplex AutoDQ 개요 | https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview | 검색 결과 확인 |
| Dataplex 프로파일·AutoDQ GA 블로그 | https://cloud.google.com/blog/products/data-analytics/dataplex-data-profiling-and-automatic-data-quality-are-ga | 검색 결과 확인 |
| Microsoft Purview Unified Catalog DQ | https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality | 검색 결과 확인 |
| Purview Fabric Lakehouse DQ | https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-fabric-lakehouse | 검색 결과 확인 |
| Purview DQ 스캔 실행 | https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-scan | 검색 결과 확인 |
| Monte Carlo 공식 | https://www.montecarlodata.com/ | 검색 결과 확인 |
| Monte Carlo circuit breaker 블로그 | https://www.montecarlodata.com/blog-announcing-circuit-breakers-a-new-way-to-automatically-stop-broken-data-pipelines-and-avoid-backfilling-costs/ | 검색 결과 확인 |
| Anomalo 공식 | https://www.anomalo.com/ | **확인(WebFetch 200, 공식)** |
| Bigeye 공식 | https://www.bigeye.com/ | **확인(WebFetch 200, 공식)** |
| Metaplane 공식 | https://www.metaplane.dev/ | 검색 결과 확인 |
| Collibra Data Quality & Observability | https://www.collibra.com/products/data-quality-and-observability | 검색 결과 확인 |
| Collibra OwlDQ 인수(보도) | https://www.prnewswire.com/news-releases/collibra-acquires-predictive-data-quality-vendor-owldq-301220863.html | 검색 결과 확인 |
| Informatica Cloud Data Quality | https://www.informatica.com/products/data-quality/cloud-data-quality-radar.html | 검색 결과 확인 |
| Informatica CLAIRE DQ | https://www.informatica.com/resources/articles/claire-gpt-data-quality.html | 검색 결과 확인 |
| Ataccama 품질 플랫폼 | https://www.ataccama.com/platform/data-quality | 검색 결과 확인 |
| Ataccama 문서 | https://docs.ataccama.com/one/latest/overview.html | 검색 결과 확인 |
| Qlik Talend Data Quality & Governance | https://www.qlik.com/us/products/data-quality-governance | 검색 결과 확인 |
| Talend Data Quality | https://www.talend.com/products/data-quality/ | 검색 결과 확인 |
| Qlik Trust Score for AI(보도) | https://www.qlik.com/us/news/company/press-room/press-releases/qlik-releases-trust-score-for-ai-in-qlik-talend-cloud | 검색 결과 확인 |
| IBM Databand 공식 | https://www.ibm.com/products/databand | 검색 결과 확인 |
| IBM Databand 파이프라인 모니터링 | https://www.ibm.com/products/databand/data-pipeline-monitoring | 검색 결과 확인 |
| IBM Databand 이상탐지 | https://www.ibm.com/products/databand/data-anomaly-detection | 검색 결과 확인 |
| SAP Information Steward | https://www.sap.com/products/technology-platform/data-profiling-steward.html | 검색 결과 확인(지역 경로 sea/ 등 변형 있음) |
| SAP Datasphere | https://www.sap.com/products/technology-platform/datasphere.html | 검색 결과 확인(경로 재확인 권장) |

---

## 10. 미확인·주의 항목

1. **dbt-expectations GitHub 경로:** calogica → Metaplane/Datadog 계열로 유지 주체·리포 경로 이관 이력 있음. 본문은 `github.com/metaplane/dbt-expectations`로 적었으나 최신 README로 정확한 정규 경로 재확인 권장.
2. **Databricks Lakehouse Monitoring 문서 URL:** Azure Databricks 경로(`/azure/databricks/lakehouse-monitoring/`)로 적음. AWS/GCP·docs.databricks.com 경로와 제품명(현 Lakeflow 리브랜딩)이 갱신 중 — 작성 시 현행 공식 문서 URL 재확인 권장.
3. **Microsoft Purview DQ 크로스 테넌트 제약:** 원격 Delta 테이블 직접 프로파일링·DQ 규칙 적용에 제약 보고(커뮤니티) — 환경별 PoC 확인.
4. **Bigeye 배포 옵션:** 홈에 SaaS 외 온프레/in-VPC 명시 적음 — 영업/문서 확인 필요. 최근 "AI Trust Platform" 포지셔닝으로 메시지 변화 중.
5. **Informatica·SAP·IBM Databand 온프레/하이브리드 세부:** 배포·가격·지원 범위는 단정 금지 — PoC·영업 확인.
6. **Qlik Trust Score for AI:** "AI 준비도 차원 점수화"가 C-2 관점에 부합하나, 구체 차원·임계·게이트 연동 방식은 공식 문서/데모 확인 권장.
7. **유형③ 관측 솔루션의 C-1 중복:** Monte Carlo·Anomalo·Bigeye·Soda Cloud·Metaplane·Databand는 C-1 Observability와 동일 제품군. 가이드에서 경계(게이트 vs 상시 모니터링)를 명시하고, 솔루션 묶음 비교는 2층 정본(`전체 목차/01 Tech Stack 비교 (솔루션×주제).md`)으로 링크 권장.
8. **SAP 공식 URL 지역 경로:** 검색 결과에 `sap.com/sea/...`(동남아) 등 지역 경로가 섞임 — 글로벌 경로(`sap.com/products/...`)로 정규화해 적었으나 접속 확인 권장.

---

*리서치 완료: 2026-06-24 | 확인 방법: WebSearch(전 항목) + WebFetch(Anomalo·Bigeye 직접 200 확인). 가격·버전·지원 범위·일부 배포 옵션은 단정하지 않음 — PoC·공식 문서 확인 권장.*
