# GX Cloud (Great Expectations) — 데이터 품질 테스트 플랫폼

> 작성일: 2026-06-10 | 카테고리: 유형② 신뢰 통제

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Great Expectations (샌프란시스코) |
| 라이선스 | 상용 SaaS (GX Cloud) + 오픈소스 (GX Core, Apache 2.0) |
| 배포 형태 | SaaS (GX Cloud) + 로컬/셀프호스팅 (GX Core OSS) |
| 최신 동향 | 2025.01: Hernan Alvarez CEO 취임, AI 통합·성장 전략 발표; ExpectAI 기능 론칭 (2025.02); 2025.06 릴리스: 스키마·볼륨·null 비율 자동 Expectation 생성 |

---

## 한 줄 포지셔닝

**"Expectation(품질 기대치)을 AI로 자동 생성하고 Data Asset 단위로 관리하는 투명 가격의 협업 품질 플랫폼"**

---

## 주요 기능

### 1. Expectations (품질 기대치 프레임워크)
- 데이터 품질 요구사항을 Expectation 단위로 정의 (예: expect_column_values_to_not_be_null)
- 300개 이상 기본 제공 Expectation + 커스텀 Expectation 작성 가능
- 모든 플랜에서 무제한 Expectations 허용, 행 수 제한 없음

### 2. ExpectAI (AI 자동 체크 생성, 2025.02 론칭)
- 데이터 스키마 자동 분석 → 컬럼별 패턴 학습 → Expectation 제안
- 분 단위 초기 설정 — 수 시간 수작업 없이 즉시 품질 커버리지 확보
- 오탐 방지를 위해 실제 데이터 패턴 기반 임계값 자동 설정

### 3. 자동 Observability Expectation
- Data Asset 생성 시 스키마 감지, 볼륨 변화(히스토리 기반), null 비율 변화를 자동 생성
- 컬럼 변경, 대규모 볼륨 이탈, null 급증을 즉시 알림

### 4. 협업 워크플로우
- 무제한 사용자 시트 — 기술/비즈니스 팀 모두 참여 가능
- 데이터 품질 결과·트렌드 공유 대시보드
- Data Asset 단위 책임자 지정 및 알림 라우팅

### 5. GX Core (오픈소스)
- Python 라이브러리, 로컬 또는 CI/CD에서 직접 실행
- Airflow, dbt, Spark 등 파이프라인 안에 삽입 가능
- GX Cloud와 연결하면 클라우드에 실행 결과 집계

---

## AI-Ready Data 주제 매핑

| 주제 코드 | 주제명 | 지원 수준 |
|---|---|---|
| C-1 | 데이터 Observability | ○ 자동 Observability Expectation |
| C-2 | 품질관리 | ○ Expectation 프레임워크 핵심 |
| C-3 | 데이터 Lineage | × 자체 Lineage 없음 |

---

## 강점

- **테스트 자동화 생산성**: ExpectAI로 초기 설정 시간 대폭 단축 — 빠른 ROI
- **투명하고 예측 가능한 비용**: Data Asset 수 기반 과금, 무제한 사용자·행·체크 — 대규모 팀에 유리
- **강력한 OSS 커뮤니티**: GX Core는 데이터 품질 OSS 중 GitHub 최다 스타, 광범위한 커넥터 생태계
- **CI/CD 친화**: Python 네이티브 → 데이터 파이프라인·MLOps 파이프라인에 자연스럽게 삽입
- **무제한 사용자 정책**: 계열사 전체 공유 비용 예측 용이

---

## 약점 및 주의점

- **ML 자동 이상탐지 제한**: Expectations 설정 선행 필요, Monte Carlo·Anomalo 수준의 완전 무설정 ML 탐지 아님
- **Lineage 부재**: 자체 Lineage 없음, 외부 도구 연동 필요
- **SaaS 전용**: GX Cloud는 완전 관리형 SaaS — 온프레미스 배포 불가 (GX Core는 어디서나 가능)
- **데이터 계약 기능 제한**: Soda 수준의 Data Contract 엔진 없음

---

## 가격 모델

| 티어 | 대상 | 주요 특징 |
|---|---|---|
| Developer | 개인·소규모 학습 | 무료, 제한된 Data Asset 수 |
| Team | 팀 단위 | Data Asset 수 기반 월정액, 무제한 사용자·체크·행 |
| Enterprise | 대기업 | SSO, RBAC, 보안 강화, SLA, 견적 |

- 핵심 원칙: **무제한 사용자 시트** — 조직 전체 협업 비용 증가 없음
- 구체적 금액은 Data Asset 수에 따라 차등, 공식 사이트에서 계산기 제공

---

## 연동 생태계

| 카테고리 | 연동 도구 |
|---|---|
| 데이터 소스 | Snowflake, BigQuery, Redshift, Databricks, PostgreSQL, Athena 등 |
| 파이프라인 | Airflow, Dagster, Prefect |
| 변환 | dbt |
| CI/CD | GitHub Actions, CircleCI |
| API | Python SDK (GX Core), REST API |
| 알림 | Slack, Email, PagerDuty |
| LLM/AI | ExpectAI (AI 기반 Expectation 제안) |

---

## 출처

- https://greatexpectations.io/
- https://greatexpectations.io/pricing/
- https://greatexpectations.io/gx-cloud/
- https://docs.greatexpectations.io/docs/cloud/overview/gx_cloud_overview/
- https://greatexpectations.io/blog/whats-new-in-gx-may-2025/
- https://greatexpectations.io/blog/whats-new-in-gx-february-2025/
- https://www.g2.com/products/great-expectations/reviews
