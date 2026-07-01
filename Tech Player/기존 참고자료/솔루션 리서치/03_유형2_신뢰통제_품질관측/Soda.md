# Soda — AI-Native 데이터 품질 플랫폼

> 작성일: 2026-06-10 | 카테고리: 유형② 신뢰 통제

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Soda Data (벨기에 앤트워프 + 뉴욕, 2020년 설립) |
| 라이선스 | 상용 SaaS + 오픈소스 (Apache 2.0) |
| 배포 형태 | SaaS (Soda Cloud) + CLI/Python SDK (soda-core OSS) |
| 최신 동향 | 2025~2026: Soda AI 출시(자연어→SodaCL 변환), 데이터 계약(Data Contract) 엔진 강화, 비정형 관측 로드맵 |

---

## 한 줄 포지셔닝

**"SodaCL YAML 코드로 파이프라인에 데이터 계약을 심고, AI가 체크를 자동 생성하는 개발자 우선 품질 플랫폼"**

---

## 주요 기능

### 1. SodaCL (Soda Checks Language)
- YAML 기반 선언형 데이터 품질 체크 언어
- null, freshness, row count, distribution, custom SQL 체크를 코드로 명세
- 파이프라인 코드와 동일한 버전 관리(Git) 가능
- 빌드 실패 게이트(fail-fast) 패턴으로 불량 데이터 downstream 차단

### 2. Soda AI (생성형 AI 통합, 2025)
- 자연어 설명 → SodaCL 체크 자동 생성
- 기존 체크 자동 정제·최적화 제안
- Facebook Prophet 대비 70% 적은 오탐(false positives)으로 알림 피로 최소화
- 10억(1B) 행 데이터를 64초 내 처리하는 고속 이상탐지 알고리즘

### 3. 데이터 계약(Data Contract) 엔진
- YAML 기반 계약 명세: 데이터 제공자-소비자 간 품질 SLA 코드화
- 계약 검증 단계: dbt 실행 전 사전 검증(pre-transformation)으로 변환 전 게이트
- soda-core CLI로 로컬/파이프라인 어디서나 계약 검증 실행
- 기술 팀과 비즈니스 팀 간 협업 워크플로우 지원

### 4. 데이터 Observability
- 데이터셋 모니터링, 파이프라인 테스팅, 메트릭 Observability 통합
- 알림 및 티켓팅 연동(Slack, PagerDuty, Jira)
- 카탈로그 연동으로 메타데이터와 품질 상태 통합 뷰

### 5. 파이프라인 통합
- Airflow, Dagster, Prefect, Glue, Spark와 원클릭 연동
- dbt 테스트와 병행 실행 또는 대체 운영
- GitHub Actions로 CI/CD 파이프라인 데이터 품질 게이트 삽입

---

## AI-Ready Data 주제 매핑

| 주제 코드 | 주제명 | 지원 수준 |
|---|---|---|
| C-1 | 데이터 Observability | ○ 파이프라인 모니터링 강점 |
| C-2 | 품질관리 | ○ SodaCL 핵심 + Data Contract |
| C-3 | 데이터 Lineage | △ 플랫폼 연동 수준 |

---

## 강점

- **코드로서의 품질(Quality-as-Code)**: 체크·계약을 Git 관리 가능한 YAML로 명세 — 감사추적, DevOps 파이프라인 통합에 최적
- **오픈소스 코어**: soda-core(Apache 2.0)로 어느 환경에서나 무료로 실행 가능 — 온프레미스·제약 환경에 적합
- **데이터 계약 성숙도**: 계열사 경계·팀 경계에서 데이터 품질 SLA 코드화·집행 기능이 현존 솔루션 중 가장 성숙
- **AI 정확도**: 70% 적은 오탐 — 알림 피로 없이 실제 문제에만 집중 가능
- **투명 가격**: Free → $750/월 Team → Enterprise 공개 티어로 예산 계획 용이

---

## 약점 및 주의점

- **ML 자동탐지 의존도**: Monte Carlo 수준의 완전 자율 ML 이상탐지보다는 체크 명세 선행 필요
- **대시보드 기능**: Soda Cloud 없이는 시각화·알림 기능 제한 — 대부분 주요 기능이 클라우드 의존
- **Lineage 미약**: 자체 Lineage 기능 없음, 외부 카탈로그(Atlan·DataHub)와 연동 필요
- **비정형 데이터 미지원**: PDF·비정형 문서 품질 점검은 로드맵 단계

---

## 가격 모델

| 티어 | 비용 | 주요 포함 기능 |
|---|---|---|
| Free | $0/월 | 파이프라인 테스팅, 메트릭 Observability, 알림 연동 |
| Team | $750/월 ~ | 무제한 사용자, SPU Pay-as-you-go, 카탈로그 연동 |
| Enterprise | 견적 | 데이터 계약, AI 품질 기능, SSO, RBAC, 프라이빗 배포 |

- **SPU(Soda Processing Units)**: 처리 데이터 행수 기반 과금 단위, 사용량 예측 가능

---

## 연동 생태계

| 카테고리 | 연동 도구 |
|---|---|
| 데이터 소스 | Snowflake, BigQuery, Redshift, Databricks, PostgreSQL, MySQL 등 |
| 파이프라인 | Airflow, Dagster, Prefect, Glue |
| 변환 | dbt (soda-dbt 패키지) |
| CI/CD | GitHub Actions, GitLab CI |
| 카탈로그 | Atlan, DataHub, Alation |
| 알림 | Slack, PagerDuty, Jira, Teams |
| API | Python SDK (soda-core), REST API |
| LLM/AI | Soda AI (자연어 → SodaCL 변환) |

---

## 출처

- https://soda.io/
- https://soda.io/product/soda-ai
- https://soda.io/pricing
- https://github.com/sodadata/soda-core
- https://www.modern-datatools.com/tools/soda/pricing
- https://www.siffletdata.com/blog/soda-review
- https://docs.soda.io/soda-documentation/soda-v3/use-case-guides/quick-start-prod
