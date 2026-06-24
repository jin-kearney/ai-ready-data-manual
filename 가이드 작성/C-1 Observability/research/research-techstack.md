# C-1 데이터 Observability — Tech Stack 리서치

> 작성일: 2026-06-24  
> 관점: 데이터 파이프라인·데이터셋의 이상을 운영 중에 감지·알림하는 **데이터 관측(Data Observability)** 솔루션. APM/인프라 모니터링(서버 CPU 등)이나 MLOps 모델 서빙 자체는 제외.

---

## 1. 전용 Data Observability 플랫폼

| 제품 | 공식 URL | 한 줄 포지셔닝 | 이상탐지 방식 | 데이터 계보(Lineage) 연계 | 컬럼/필드 단위 모니터링 | 알림 연동 | 배포 형태 |
|---|---|---|---|---|---|---|---|
| **Monte Carlo** | https://montecarlo.ai | 자율 에이전트 기반 데이터·AI 관측 플랫폼. 메타데이터·쿼리 이력으로 이상을 자동 감지 | ML 자동 베이스라인 (임계값 설정 불필요) | ✅ 자동 필드 수준 계보. 영향 범위(blast radius) 분석 | ✅ 컬럼 단위 분포·스키마 변경 감지 | Slack, PagerDuty, Teams, Jira 등 | SaaS (Scale) / 하이브리드(Enterprise: 고객 측 Object Storage 허용) |
| **Anomalo** | https://www.anomalo.com | ML 기반 비지도 이상탐지에 특화. 비정형 데이터(PDF·계약서) 품질 관측도 지원 | ML 비지도학습 자동 베이스라인 | ✅ 자동 계보 추적·루트코즈 분석 | ✅ 컬럼 수준 이상·유효값 검증 | Slack, Teams, 이메일 등 | SaaS / VPC 온프렘(규제 환경) |
| **Bigeye** | https://www.bigeye.com | 컬럼 단위 계보 연동 자동화 모니터링. 70종+ 품질 지표 라이브러리 | bigAI 자동 임계값(계절성·트렌드 학습) | ✅ 교차 소스 컬럼 계보. 영향 분석 | ✅ 컬럼 단위 70종+ 지표 | Slack, PagerDuty, Teams, Jira, ServiceNow (30종+) | SaaS (AWS/GCP Marketplace) |
| **Soda** | https://www.soda.io | 코드형(SodaCL) 데이터 품질 체크 + 운영 관측. 레코드 수준 이상탐지 지원 | 적응형 스마트 임계값(ML) + 규칙(SodaCL YAML) 혼용 | 제한적(dbt 연동 시 강화) | ✅ 컬럼 단위 체크(SodaCL) | Slack, Teams, PagerDuty, 이메일 | SaaS (Soda Cloud) / 오픈소스(Soda Core) |
| **Metaplane** | https://www.metaplane.dev | 메타데이터만 읽어 ML 베이스라인 탐지. 15분 내 설정, 코드 불필요 | ML 자동 베이스라인(계절성 학습, 임계값 불필요) | ✅ 엔드투엔드 컬럼 수준 계보 (소스→BI 무설정) | ✅ 컬럼 단위 이상 자동 감지 | Slack (기본), 기타 표준 알림 | SaaS (Datadog가 2024년 인수) |
| **Acceldata** | https://www.acceldata.io | 하이브리드(Hadoop+클라우드) 인프라 및 데이터 관측 통합. 자율 치유(self-healing) 표방 | ML 기반 통계 이상탐지 + 룰 정책 | ✅ 엔드투엔드 계보(파이프라인 전체) | ✅ 파이프라인 전체 데이터 품질 정책 | 표준 모니터링 도구 연동(Slack 등) | SaaS / 온프렘 / 하이브리드 클라우드 |
| **Sifflet** | https://www.siffletdata.com | 데이터·AI 컨트롤 플레인. 계보+카탈로그+품질 관측 통합. 비즈니스-기술 팀 브리지 | AI 기반 ML 이상탐지 + 커스텀 체크 | ✅ 필드 수준 계보(웨어하우스→BI) | ✅ 동적 품질 모니터링, 컬럼 단위 | Slack, Teams, PagerDuty 등 표준 | SaaS / 온프렘 |
| **Datafold** | https://www.datafold.com | 데이터 Diff + ML 이상탐지. CI/CD 파이프라인 내 데이터 변경 검증에 강점 | ML 이상탐지 + Data Diff(값 수준 비교) | ✅ Data Knowledge Graph (계보+비즈니스 로직) | ✅ 컬럼 단위 Diff·이상 감지 | 표준 CI/CD 통합(GitHub Actions 등) | SaaS / VPC 단일 테넌트(AWS·GCP·Azure) |

---

## 2. 데이터 플랫폼 내장형

| 플랫폼/기능 | 공식 문서 URL | 무엇을 관측하나 | 이상탐지 방식 | 계보 연계 | 비고 |
|---|---|---|---|---|---|
| **Databricks Data Quality Monitoring** (구 Lakehouse Monitoring) | https://www.databricks.com/product/machine-learning/lakehouse-monitoring | Delta Table 신선도·완전성·분포 이상. Unity Catalog 연동 자동 프로파일링 | ML 기반 이력 패턴 분석 + 커스텀 SQL 지표 | Unity Catalog 내 계보 활용 | 클릭 1회로 활성화, Databricks 환경 전용 |
| **Snowflake Data Metric Functions (DMF)** | https://docs.snowflake.com/en/user-guide/data-quality-intro | Snowflake 테이블 품질 지표 자동 수집. 2025년 Select Star 인수로 기능 강화 | 룰 기반 (DMF) + 플랫폼 내 통계 | Snowflake Horizon 내 계보 | Snowflake 환경 전용 |
| **dbt (tests + source freshness)** | https://docs.getdbt.com/docs/build/data-tests | 변환 단계 데이터 검증(Not Null·Unique·관계무결성). source freshness로 원천 최신성 체크 | 룰 기반 (YAML 정의) | dbt 프로젝트 내 계보 그래프 | 단독으로는 운영 모니터링 부족 — Elementary와 결합 권장 |
| **AWS Glue Data Quality** | https://aws.amazon.com/glue/features/data-quality/ | S3·Glue 파이프라인 내 데이터 품질. 25종+ 내장 룰 + ML 이상탐지. Deequ 기반 | 룰 기반 + ML(통계 패턴 학습, 2024 GA) | AWS Lake Formation/DataZone 연동 | AWS 환경 전용, DataZone 통합(2024) |
| **Google Dataplex / Knowledge Catalog** | https://cloud.google.com/dataplex/docs | BigQuery 데이터 프로파일·품질 체크. CloudDQ 기반 | 룰 기반 + 경량 프로파일링(Preview) | Dataplex 내 계보 | GCP 환경 전용, 2024 Knowledge Catalog로 리브랜딩 |

---

## 3. 오픈소스

| 도구 | 공식 사이트 / GitHub | 강점 | 한계 | 배포 |
|---|---|---|---|---|
| **Great Expectations (GX)** | https://greatexpectations.io / https://github.com/great-expectations/great_expectations | 300종+ Expectation(검증 조건) 라이브러리. Apache 2.0 라이선스. CI/CD 통합(GitHub Actions). 데이터 Docs 자동 생성 | ML 이상탐지 미지원(룰 정의 필수). 운영 모니터링보다 배치 검증에 강함. 설정 복잡도 높음 | 오픈소스(GX Core) / GX Cloud(관리형 SaaS) |
| **Soda Core** | https://www.soda.io / https://github.com/sodadata/soda-core | SodaCL YAML로 직관적 체크 정의. Apache 2.0. dbt·Airflow 친화적 | 고급 ML 이상탐지는 Soda Cloud 유료 플랜 필요. 오케스트레이션 미포함 | 오픈소스(CLI) / Soda Cloud(SaaS, 공식 문서 확인) |
| **Elementary** | https://www.elementary-data.com / https://github.com/elementary-data/elementary | dbt 네이티브 관측. dbt 메타데이터·테스트 결과 자동 수집. 신선도·볼륨·스키마 이상 탐지. Slack·Teams 알림 내장 | dbt 사용 환경 필수. ML 이상탐지·컬럼 계보는 Elementary Cloud(유료) 전용 | 오픈소스(CLI 자기호스팅) / Elementary Cloud(유료 SaaS) |
| **Deequ / PyDeequ** | https://github.com/awslabs/deequ / https://github.com/awslabs/python-deequ | Apache Spark 기반 페타바이트 규모 품질 체크. Amazon이 오픈소스 공개. AWS Glue Data Quality의 기반 엔진 | Spark 환경 필수. UI·알림 없음(코드 전용). 별도 스케줄러 필요 | 오픈소스(라이브러리) |
| **Evidently** | https://www.evidentlyai.com / https://github.com/evidentlyai/evidently | 데이터 분포 드리프트·ML 예측 품질 모니터링. 100종+ 지표, 20종+ 통계 검정. 테이블형·텍스트·LLM 출력 모두 지원. HTML 리포트 자동 생성 | 실시간 파이프라인 알림보다 배치 분석·리포팅 강함. 운영 알림은 Evidently Cloud 필요 | 오픈소스(Python 라이브러리) / Evidently Cloud(관리형 SaaS) |

---

## 4. 선정 기준 체크리스트

| 선정 기준 | 확인 포인트 |
|---|---|
| **이상탐지 방식** | ML 자동 베이스라인(임계값 없이 시작 가능) vs 룰 기반(직접 정의 필요). ML형이 초기 운영 부담 낮음 |
| **계보(Lineage) 연계** | 이상 발생 시 상위 원인·하위 영향 범위를 자동으로 추적 가능한지 |
| **컬럼/필드 단위 모니터링** | 테이블 전체 통계가 아닌 특정 컬럼(예: 불량률·출하량) 수준의 이상 감지 여부 |
| **알림 연동** | Slack·Teams·PagerDuty·Opsgenie 등 기존 협업 도구에 즉시 연동 가능한지 |
| **배포 형태** | SaaS(빠른 시작) vs 온프렘/VPC(사외반출 제약 있는 제조 데이터 환경). 하이브리드 지원 여부 |
| **비용 모델** | 테이블 수·데이터 소스 수·모니터링 깊이 기반 과금. 오픈소스 + 유료 Cloud 혼용 가능 여부 |
| **dbt 연동** | dbt를 이미 사용 중이면 Elementary·Soda·Datafold와 자연스러운 연계 가능 |
| **사내 데이터 접근 방식** | Metaplane처럼 메타데이터만 읽는지(원본 데이터 비노출) vs 원본 스캔 필요한지 |

> 가격·세부 기능은 버전마다 변동. 도입 전 공식 문서 확인 및 PoC(개념 검증) 권장.

---

## 5. 출처 URL 목록

| 제품/도구 | URL | 비고 |
|---|---|---|
| Monte Carlo (공식) | https://montecarlo.ai | 2024년 도메인 이전(montecarlodata.com → montecarlo.ai) |
| Monte Carlo (AWS Marketplace) | https://aws.amazon.com/marketplace/pp/prodview-hikicsfohm3gg | - |
| Monte Carlo (Docs) | https://docs.getmontecarlo.com/docs/architecture | 아키텍처 문서 |
| Anomalo (공식) | https://www.anomalo.com | - |
| Anomalo (Monte Carlo 비교) | https://www.anomalo.com/blog/monte-carlo-vs-anomalo/ | - |
| Bigeye (공식) | https://www.bigeye.com | - |
| Bigeye (Observability 기능) | https://www.bigeye.com/platform/data-observability | - |
| Bigeye (Lineage) | https://www.bigeye.com/platform/data-lineage | - |
| Soda (공식) | https://www.soda.io | - |
| Soda Core (GitHub) | https://github.com/sodadata/soda-core | Apache 2.0 |
| Metaplane (공식) | https://www.metaplane.dev | 2024년 Datadog 인수 |
| Metaplane (State of Data Quality 2024) | https://www.metaplane.dev/state-of-data-quality-monitoring-2024 | - |
| Acceldata (공식) | https://www.acceldata.io | - |
| Acceldata (TechTarget 기사) | https://www.techtarget.com/searchdatamanagement/news/366617023/Acceldata-unveils-AI-powered-data-observability-tools | AI 기능 발표 |
| Sifflet (공식) | https://www.siffletdata.com | - |
| Sifflet (Monte Carlo 리뷰) | https://www.siffletdata.com/blog/monte-carlo-data-review | 경쟁사 리뷰 |
| Datafold (공식) | https://www.datafold.com | - |
| Databricks Data Quality Monitoring | https://www.databricks.com/product/machine-learning/lakehouse-monitoring | 구 Lakehouse Monitoring |
| Databricks Blog (GA 발표) | https://www.databricks.com/blog/lakehouse-monitoring-ga-profiling-diagnosing-and-enforcing-data-quality-intelligence | - |
| Snowflake Data Quality (공식 문서) | https://docs.snowflake.com/en/user-guide/data-quality-intro | DMF 설명 |
| dbt Tests (공식 문서) | https://docs.getdbt.com/docs/build/data-tests | - |
| AWS Glue Data Quality (공식) | https://aws.amazon.com/glue/features/data-quality/ | - |
| AWS Glue Data Quality (Docs) | https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html | - |
| Deequ (AWS Big Data Blog) | https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/ | - |
| Google Dataplex/Knowledge Catalog | https://cloud.google.com/dataplex/docs | - |
| Great Expectations (공식) | https://greatexpectations.io | - |
| Great Expectations (GitHub) | https://github.com/great-expectations/great_expectations | Apache 2.0 |
| Great Expectations (Docs) | https://docs.greatexpectations.io/docs/ | - |
| Soda Core (공식) | https://www.soda.io | - |
| Elementary (GitHub) | https://github.com/elementary-data/elementary | - |
| Elementary (dbt package GitHub) | https://github.com/elementary-data/dbt-data-reliability | - |
| Deequ (GitHub) | https://github.com/awslabs/deequ | Apache 2.0 |
| PyDeequ (GitHub) | https://github.com/awslabs/python-deequ | Apache 2.0 |
| Evidently AI (공식) | https://www.evidentlyai.com | - |
| Evidently AI (GitHub) | https://github.com/evidentlyai/evidently | Apache 2.0 |
| 비교 리소스: Basedash | https://www.basedash.com/blog/best-data-observability-tools-compared-2026 | - |
| 비교 리소스: DataKitchen 2026 | https://datakitchen.io/blog/the-2026-data-quality-and-data-observability-commercial-software-landscape/ | - |
| 비교 리소스: DataKitchen OSS | https://datakitchen.io/blog/the-2026-open-source-data-quality-and-data-observability-landscape/ | - |
| 비교 리소스: Dagster | https://dagster.io/learn/data-observability-tools | - |
| 비교 리소스: Alation | https://www.alation.com/blog/data-observability-tools/ | - |

---

*가격·버전·기능 세부사항은 변동 가능 — 도입 시 각 공식 문서·PoC로 최신 정보 확인.*
