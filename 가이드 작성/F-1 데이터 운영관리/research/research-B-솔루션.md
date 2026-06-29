# F-1 데이터 운영관리(DataOps) — 솔루션(Tech Stack) 리서치

> 용도: F-1 가이드 "Tech Stack(솔루션)" 섹션 재료. F-1 관점(파이프라인을 "안 멈추게" 운영 — 스케줄·재시도·복구·CI/CD·변경관리)에서 필요한 만큼만 정리한다.
> 솔루션 묶음 비교·선정은 2층 정본([Tech Player/01 Tech Stack 비교](../../../Tech%20Player/01%20Tech%20Stack%20비교%20(솔루션×주제).md))이 전담하므로, 여기서는 "어떤 도구가 무엇을 잘하나 + 어떤 상황에 맞나"까지만.
> 가격·버전·정확한 기능 범위는 단정하지 않는다 — PoC·공식 문서로 확인.
> 관점 고정: AI 모델/RAG/에이전트를 만드는 도구가 아니라, **데이터 파이프라인을 운영하는 도구**다.

---

## 0. F-1에서 솔루션을 보는 축 (선정 기준)

DataOps 도구를 고를 때 보는 것:

1. **스케줄 / 재시도 / 백필(Backfill)** — 정해진 시각·이벤트로 돌리고, 실패하면 자동 재시도하고, 과거 구간을 다시 채워 넣을 수 있는가.
2. **장애 복구** — 멈춘 지점부터 이어서 재처리, 잘못된 결과 롤백·재실행이 쉬운가.
3. **CI/CD · 테스트 게이트** — 파이프라인 코드를 Git으로 관리하고, 배포 전 자동 테스트로 막아주는가(변경관리).
4. **이식성(Portability) vs 운영 위임** — 온프렘/멀티클라우드로 들고 다닐 수 있는가(오픈소스 셀프호스트) vs 운영 부담을 벤더에 맡기는가(매니지드).
5. **기존 인프라 정합** — 이미 AWS면 MWAA·Step Functions, Azure면 ADF, Databricks를 쓰면 Workflows가 자연스럽다.
6. **데이터 인식(Asset-aware) 정도** — "작업(task)"만 돌리는가, 아니면 "어떤 데이터(asset)를 만드는가"를 알고 계보·신선도까지 보는가.

두산 제약 메모: **보안 데이터·폐쇄망 가능성**이 있으면 SaaS·매니지드는 제약이 크고, **오픈소스 셀프호스트(Airflow·Dagster·Prefect·NiFi)** 가 현실적 1순위. 이미 특정 클라우드를 쓰는 영역이면 그 클라우드 내장 도구가 정합성에서 유리.

---

## 1. 오픈소스 워크플로 오케스트레이터 (셀프호스트)

파이프라인의 "지휘자". 어떤 작업을 어떤 순서로·언제 돌릴지 정의하고, 실패를 잡아 재시도·복구한다. 폐쇄망에서 직접 운영 가능.

| 솔루션 | 무엇을 잘하나 | 배포 | 데이터 인식 | 메모 |
|---|---|---|---|---|
| **Apache Airflow** | 사실상 업계 표준. Python DAG로 스케줄·의존성·재시도·백필, 풍부한 UI(상태·로그·실행이력), 거대한 커넥터 생태계 | 셀프호스트(매니지드도 다수 — 2장) | Task 중심(데이터 asset은 부가) | 가장 성숙·인력 풀 넓음. 운영 부담(메타DB·스케줄러·워커)이 큼 |
| **Dagster** | "데이터 asset 중심" — 작업이 아니라 "어떤 테이블/모델이 존재해야 하는가"로 파이프라인을 선언. 계보 시각화·테스트·신선도 관리에 강함 | 셀프호스트(+ Dagster+ 클라우드) | Asset-aware(강함) | dbt와 궁합 좋음(모델=asset). C-2 품질·A-4 리니지와 연결 자연스러움 |
| **Prefect** | 현대적 Python(@flow·@task 데코레이터)로 시작 빠름, 동적 워크플로·이벤트 트리거·하이브리드 실행(코드/데이터는 내 인프라, 메타데이터만 클라우드) | 셀프호스트(+ Prefect Cloud) | Flow 중심 | 가볍게 시작하기 좋음. 하이브리드 모델이 보안 환경에 매력적 |
| **Apache NiFi** | GUI 기반 흐름 설계. 시스템 간 실시간 데이터 이동·라우팅, 백프레셔·동적 우선순위·런타임 흐름 변경, SSL/SSH/HTTPS 등 강한 보안 | 셀프호스트 | 흐름(Flow)/스트림 중심 | 코딩보다 GUI 선호·실시간 수집/이동·강보안 환경에 적합. 복잡한 변환 오케스트레이션보다 "데이터 흐름 자동화"에 강점 |
| **Mage** | 노트북형 UI로 ETL 파이프라인을 빠르게 작성·운영. 모듈형 코드, 셀프호스트 무료 | 셀프호스트(클라우드 자가구축) | Block/Pipeline 중심 | 작은 팀·빠른 ETL 구축에. Airflow보다 가벼움 |

공식 URL:
- Apache Airflow — https://airflow.apache.org/
- Dagster — https://dagster.io/
- Prefect — https://www.prefect.io/
- Apache NiFi — https://nifi.apache.org/
- Mage — https://www.mage.ai/  (소스: https://github.com/mage-ai/mage-ai )

선택 가늠:
- 표준·인력 풀·생태계 우선 → **Airflow**
- 데이터 asset·계보·품질 통합 관점 → **Dagster**
- 가볍게·Python 친화·하이브리드 → **Prefect**
- GUI·실시간 흐름·강보안 수집 → **NiFi**

---

## 2. 클라우드 내장(매니지드 오케스트레이션)

이미 쓰는 클라우드 안에서 오케스트레이션을 제공. 인프라 운영 부담을 벤더에 위임. 폐쇄망·온프렘에는 부적합(클라우드 종속).

| 솔루션 | 유형 | 잘하는 것 | 적합 상황 |
|---|---|---|---|
| **Amazon MWAA** (Managed Workflows for Apache Airflow) | AWS 매니지드 Airflow | 오픈소스 Airflow를 그대로, 인프라(스케일·가용성·보안) 위임 | 이미 AWS·Airflow 자산이 있고 운영 부담을 줄이고 싶을 때 |
| **AWS Step Functions** | AWS 서버리스 워크플로 | AWS 서비스 220+ 연결, 상태 추적·에러 핸들링·정확히 한 번 실행(Standard), 멈춘 지점 재개 | AWS 서비스 중심 서버리스 워크플로·강한 상태/에러 처리 |
| **Google Cloud Composer** | GCP 매니지드 Airflow | GCP 호스팅 Airflow. GCP 서비스와 네이티브 통합 | 이미 GCP를 쓰고 Airflow를 매니지드로 원할 때 |
| **Azure Data Factory (ADF)** | Azure 데이터 통합/ETL | 데이터 이동·변환 파이프라인을 GUI로 구성·스케줄, Azure DevOps/GitHub로 CI/CD, Workflow Orchestration Manager(Airflow 기반 DAG)도 제공 | Azure 중심·GUI 선호·하이브리드 데이터 통합 |
| **Databricks Workflows** | Databricks 내장 | Databricks(Lakehouse) 작업(노트북·dbt·SQL·Python)을 스케줄·의존성·재시도로 오케스트레이션 | 이미 Databricks를 데이터 플랫폼으로 쓸 때 — 별도 도구 없이 통합 |
| **Google Cloud Dataflow** | GCP 매니지드 처리(Apache Beam) | 대규모 배치/스트리밍 처리 실행·오토스케일 | 순수 오케스트레이터라기보다 처리 엔진. Composer로 트리거 |

공식 URL:
- Amazon MWAA — https://aws.amazon.com/managed-workflows-for-apache-airflow/
- AWS Step Functions — https://aws.amazon.com/step-functions/
- Google Cloud Composer — https://cloud.google.com/composer
- Azure Data Factory — https://azure.microsoft.com/en-us/products/data-factory  (문서: https://learn.microsoft.com/en-us/azure/data-factory/introduction )
- Databricks Workflows — https://www.databricks.com/product/workflows
- Google Cloud Dataflow — https://cloud.google.com/dataflow

정합 원칙(가이드용 핵심): **이미 쓰는 인프라를 따라간다** — AWS면 MWAA/Step Functions, Azure면 ADF, GCP면 Composer/Dataflow, Databricks면 Workflows. 폐쇄망이면 이 카테고리 대신 1장(셀프호스트).

---

## 3. 매니지드 SaaS / 상용 DataOps 플랫폼

오픈소스 오케스트레이터를 "운영까지 통째로" 맡기는 상용 서비스. 운영 위임·관측성·엔터프라이즈 지원이 강점, 대신 클라우드 종속(폐쇄망 제약).

| 솔루션 | 기반 | 잘하는 것 | 적합 상황 |
|---|---|---|---|
| **Astronomer (Astro)** | Apache Airflow | Airflow를 매니지드 + 통합 DataOps 플랫폼(빌드·실행·관측), 엔터프라이즈 지원 | Airflow를 쓰되 운영·관측·지원을 통째로 위임하고 싶을 때 |
| **Prefect Cloud** | Prefect | Prefect 매니지드. 메타데이터는 클라우드, 코드·데이터는 고객 인프라(하이브리드) | Prefect 셀프호스트 운영을 줄이되 데이터는 내 환경에 둘 때 |
| **Dagster+ (Cloud)** | Dagster | Dagster 매니지드/엔터프라이즈. asset·계보·신선도 관측 강화 | asset 중심·dbt 통합을 매니지드로 |
| **dbt Cloud** | dbt | SQL 변환을 빌드·테스트·문서·배포(스케줄러 포함). AI-ready 파이프라인 강조 | 변환(Transform) 레이어 표준화·테스트·배포 자동화 |
| **Databricks** (통합 플랫폼) | Lakehouse | 수집·변환·오케스트레이션(Workflows)·품질을 한 플랫폼에서 | 데이터 플랫폼 자체를 통합으로 갈 때 |

공식 URL:
- Astronomer (Astro) — https://www.astronomer.io/  (DataOps 플랫폼: https://www.astronomer.io/dataops-platform/ )
- Prefect Cloud — https://www.prefect.io/cloud
- Dagster+ — https://dagster.io/plus
- dbt Cloud — https://www.getdbt.com/  (제품: https://www.getdbt.com/product/dbt-cloud )
- Databricks — https://www.databricks.com/

메모: SaaS는 폐쇄망에서 보통 불가. 두산 보안 데이터 시나리오에서는 1장(셀프호스트) 우선, SaaS는 "비밀 데이터가 아닌 영역·운영 인력 부족 시" 검토.

---

## 4. 변경 관리 · 데이터 계약 · 배포 테스트 게이트 보조 도구

오케스트레이터 옆에서 "바꿔도 안 깨지게" 받쳐주는 도구. F-1 관점에서는 **배포 전 테스트 게이트·스키마 변경 호환성·데이터 계약** 측면으로만 본다(데이터 품질 자체의 정의·운영은 C-2 품질 주제).

| 솔루션 | 역할(F-1 관점) | 메모 |
|---|---|---|
| **dbt** | 변환 모델에 테스트(assertion)를 붙여 `dbt test`로 배포 전 검증, 문서·DAG 자동 생성, 환경별 배포(promote) | 변환 레이어의 변경관리·테스트 게이트 핵심. (오픈소스 dbt Core / 매니지드 dbt Cloud) |
| **Great Expectations** | 데이터에 대한 기대(assertion)를 코드로 정의 → 파이프라인 배포/실행 단계의 검증 게이트로 사용 | 품질 정의는 C-2 영역. F-1에선 "통과 못 하면 배포·진행 차단" 게이트로만 |
| **Soda (Soda Core)** | 데이터 품질 체크를 코드로(SodaCL) 정의·실행, 파이프라인에 끼워 게이트화 | 위와 동일 — F-1에선 게이트 관점 |
| **Confluent Schema Registry** | 스키마(Avro/JSON/Protobuf) 버전 관리 + 호환성 모드(backward 등)로 **스키마 변경이 소비자를 깨는지** 차단. 데이터 계약(Data Contracts) 기능 포함 | 스트리밍/Kafka 환경의 스키마 변경관리 핵심. "깨지는 변경 자동 차단" |
| **Data Contract (오픈 표준)** | 생산자-소비자 간 스키마·SLA·품질 기대를 명문화. 계약 위반·breaking change 탐지, SQL DDL·dbt·Avro 등으로 내보내기 | 표준·도구가 여럿(예: Data Contract Specification). 변경관리의 "약속" 레이어 |

공식 URL:
- dbt (Core/문서) — https://www.getdbt.com/  /  https://docs.getdbt.com/docs/build/data-tests
- Great Expectations — https://greatexpectations.io/
- Soda — https://www.soda.io/
- Confluent Schema Registry (문서) — https://docs.confluent.io/platform/current/schema-registry/index.html  (데이터 계약: https://docs.confluent.io/platform/current/schema-registry/fundamentals/data-contracts.html )
- Data Contract Specification — https://datacontract.com/

가이드 작성 주의: Great Expectations·Soda는 **C-2 데이터 품질**에 더 가깝다. F-1에서는 "배포·실행 전에 통과 못 하면 막는 게이트" 한 줄로만 인용하고, 품질 정의·룰 운영은 C-2로 포인터.

---

## 5. CI/CD · 버전관리 연계 (변경관리의 토대)

위 도구들을 "Git으로 관리하고 자동 배포"하는 토대. 파이프라인을 코드로 두면(Code-as-pipeline) 변경 이력·리뷰·롤백·테스트가 가능해진다.

개념:
- **버전관리(Git)** — 파이프라인 정의(DAG·dbt 모델·계약)를 코드로 저장. 누가·언제·무엇을 바꿨는지 추적, 문제 시 이전 버전으로 롤백.
- **CI(지속적 통합)** — Push/PR 때 자동으로 테스트(dbt test·스키마 호환성·린트) 실행해 깨지는 변경을 사전 차단(테스트 게이트).
- **CD(지속적 배포)** — 통과한 변경을 운영 환경으로 자동 승격(promote), 환경별 승인·롤백 전략 적용.

대표 도구·공식 URL:
- **GitHub Actions** — https://github.com/features/actions  (YAML 워크플로로 테스트·빌드·배포 자동화, 시크릿 관리·환경별 승인·롤백)
- **GitLab CI/CD** — https://docs.gitlab.com/ee/ci/
- **Git (버전관리)** — https://git-scm.com/
- 클라우드 내장 CI/CD 연계 예: **Azure DevOps/GitHub로 ADF 배포** — https://learn.microsoft.com/en-us/azure/data-factory/continuous-integration-delivery ; **Databricks CI/CD(GitHub Actions)** — https://docs.databricks.com/aws/en/dev-tools/ci-cd/github

가이드용 한 줄: "파이프라인을 코드로 두고(Git) → Push마다 자동 테스트(CI)로 깨지는 변경을 막고 → 통과한 것만 운영으로 자동 배포(CD)" — 이것이 DataOps 변경관리의 골격. 폐쇄망이면 **GitLab(셀프호스트)·내부 Git + 자체 러너**로 동일 구성 가능.

---

## 6. F-1 가이드용 비교표 (요약 — 그대로 쓸 수 있는 형태)

| 솔루션 | 유형 | 배포 | 잘하는 것 | 적합 상황 |
|---|---|---|---|---|
| Apache Airflow | 오픈소스 오케스트레이터 | 셀프호스트 | 표준 DAG·스케줄·재시도·백필·넓은 생태계 | 표준·인력풀·폐쇄망 직접운영 |
| Dagster | 오픈소스 오케스트레이터 | 셀프호스트(+클라우드) | 데이터 asset·계보·신선도·dbt 통합 | 데이터 중심·품질/계보 연계 |
| Prefect | 오픈소스 오케스트레이터 | 셀프호스트(+클라우드) | 가벼운 Python·동적·하이브리드 실행 | 빠른 시작·데이터는 내 환경 |
| Apache NiFi | 오픈소스(흐름) | 셀프호스트 | GUI 흐름·실시간 이동·강보안 | GUI 선호·실시간 수집·강보안 |
| Mage | 오픈소스 | 셀프호스트 | 노트북형 빠른 ETL | 작은 팀·빠른 구축 |
| Amazon MWAA | 클라우드 내장(매니지드) | 클라우드(AWS) | 매니지드 Airflow | AWS·Airflow 운영위임 |
| AWS Step Functions | 클라우드 내장 | 클라우드(AWS) | 서버리스·상태/에러 처리·재개 | AWS 서비스 중심 워크플로 |
| Google Cloud Composer | 클라우드 내장(매니지드) | 클라우드(GCP) | 매니지드 Airflow·GCP 통합 | GCP 환경 |
| Azure Data Factory | 클라우드 내장 | 클라우드(Azure) | GUI 데이터통합·CI/CD·DAG | Azure·GUI·하이브리드 |
| Databricks Workflows | 클라우드 내장(플랫폼) | 클라우드 | Lakehouse 통합 오케스트레이션 | Databricks 사용 시 |
| Astronomer (Astro) | 매니지드 SaaS | 클라우드 | Airflow 운영·관측 통째 위임 | Airflow 엔터프라이즈 위임 |
| Prefect Cloud | 매니지드 SaaS | 클라우드(하이브리드) | Prefect 운영 위임·하이브리드 | Prefect 위임 |
| Dagster+ | 매니지드 SaaS | 클라우드 | Dagster 운영·asset 관측 | Dagster 위임 |
| dbt (Core/Cloud) | 변환·테스트·배포 | 셀프호스트/클라우드 | 변환 테스트 게이트·문서·배포 | 변환 레이어 변경관리 |
| Great Expectations / Soda | 테스트 게이트(주로 C-2) | 셀프호스트/클라우드 | 데이터 검증을 배포 게이트로 | 진행 전 검증 차단 |
| Confluent Schema Registry | 스키마 변경관리/계약 | 셀프호스트/클라우드 | 스키마 호환성·breaking change 차단 | 스트리밍·스키마 변경관리 |
| GitHub Actions / GitLab CI | CI/CD | 클라우드/셀프호스트 | 코드 테스트·자동 배포·롤백 | 파이프라인 변경관리 토대 |

---

## 7. 가이드 작성에 쓸 핵심 메시지(요지)

1. F-1 솔루션의 중심은 **오케스트레이터**(Airflow/Dagster/Prefect/NiFi)다 — 스케줄·재시도·백필·복구가 본체.
2. 선택의 1차 분기는 **이식성 vs 운영 위임**: 폐쇄망·보안데이터 → 오픈소스 셀프호스트 / 운영부담 최소화 → 매니지드·SaaS.
3. 2차 분기는 **기존 인프라 정합**: AWS→MWAA/Step Functions, Azure→ADF, GCP→Composer, Databricks→Workflows.
4. 변경관리는 도구 하나가 아니라 **Git + CI/CD(테스트 게이트) + 스키마 호환성/데이터 계약**의 조합으로 완성된다.
5. Great Expectations·Soda는 **C-2 품질** 영역 — F-1에서는 "배포 게이트"로만 짧게.
6. 묶음 비교·최종 선정 매트릭스는 **2층 정본(Tech Player/01)** 으로 넘긴다.

---

## 참고자료 (확인한 공식 URL)

오픈소스 오케스트레이터
- Apache Airflow — https://airflow.apache.org/
- Dagster — https://dagster.io/
- Prefect — https://www.prefect.io/
- Apache NiFi — https://nifi.apache.org/
- Mage — https://www.mage.ai/ , https://github.com/mage-ai/mage-ai

클라우드 내장(매니지드 오케스트레이션)
- Amazon MWAA — https://aws.amazon.com/managed-workflows-for-apache-airflow/
- AWS Step Functions — https://aws.amazon.com/step-functions/
- Google Cloud Composer — https://cloud.google.com/composer
- Azure Data Factory — https://azure.microsoft.com/en-us/products/data-factory , https://learn.microsoft.com/en-us/azure/data-factory/introduction
- Databricks Workflows — https://www.databricks.com/product/workflows
- Google Cloud Dataflow — https://cloud.google.com/dataflow

매니지드 SaaS / 상용 DataOps
- Astronomer (Astro) — https://www.astronomer.io/ , https://www.astronomer.io/dataops-platform/
- Prefect Cloud — https://www.prefect.io/cloud
- Dagster+ — https://dagster.io/plus
- dbt Cloud — https://www.getdbt.com/product/dbt-cloud
- Databricks — https://www.databricks.com/

변경관리 · 데이터 계약 · 테스트 게이트
- dbt 문서(데이터 테스트) — https://docs.getdbt.com/docs/build/data-tests
- Great Expectations — https://greatexpectations.io/
- Soda — https://www.soda.io/
- Confluent Schema Registry — https://docs.confluent.io/platform/current/schema-registry/index.html , https://docs.confluent.io/platform/current/schema-registry/fundamentals/data-contracts.html
- Data Contract Specification — https://datacontract.com/

CI/CD · 버전관리
- GitHub Actions — https://github.com/features/actions
- GitLab CI/CD — https://docs.gitlab.com/ee/ci/
- Git — https://git-scm.com/
- ADF CI/CD — https://learn.microsoft.com/en-us/azure/data-factory/continuous-integration-delivery
- Databricks CI/CD (GitHub Actions) — https://docs.databricks.com/aws/en/dev-tools/ci-cd/github
