# DataHub (+Acryl / DataHub Cloud)

> 작성일: 2026-06-10 | 조사 기준: 2025~2026년 최신 릴리스

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Acryl Data, Inc. (미국, 샌프란시스코) — DataHub OSS 메인테이너 |
| 라이선스 | OSS: Apache License 2.0 / 상용: DataHub Cloud (Acryl) |
| 배포 형태 | 자체 호스팅 (Docker/Kubernetes) + SaaS (DataHub Cloud) |
| 최신 주요 릴리스 | 2025-05: $35M Series B 펀딩 (Bessemer 주도); AI 컨텍스트 관리 플랫폼으로 전략 전환 |
| 커뮤니티 | GitHub Stars 10,000+, 슬랙 13,000+ 멤버, LinkedIn 기원 프로젝트 |

---

## 한 줄 포지셔닝

**LinkedIn에서 시작한 오픈소스 데이터 카탈로그 — AI·데이터 스택의 컨텍스트 플랫폼으로 진화 중이며 MCP·AI 거버넌스를 오픈 생태계로 제공.**

---

## 주요 기능

### 1. 데이터 카탈로그 & 메타데이터
- **Entity 모델 기반**: Dataset, Dashboard, Pipeline, ML Model, Feature, Chart 등 다양한 엔티티 타입 지원
- **자동 메타데이터 수집 (Ingestion)**: 100+ 소스 커넥터 (Snowflake, Databricks, BigQuery, Redshift, Oracle, dbt, Airflow, Kafka 등)
- **메타데이터 이벤트 스트리밍**: Kafka 기반 실시간 메타데이터 변경 이벤트 처리
- **자연어 검색**: AI 기반 의미 검색, 정확한 키워드가 없어도 유사 개념 자산 탐색
- **자동 문서화**: LLM 보조 테이블·컬럼 설명 자동 생성

### 2. Business Glossary & 분류
- **계층적 Glossary**: 노드→용어 구조, 비즈니스 정의 관리
- **용어-엔티티 연결**: Glossary 용어를 데이터셋·컬럼에 태그로 연결
- **분류 체계(Classification)**: 민감도·규정 준수 분류 태그 관리 및 자산 전파
- **도메인 관리**: 데이터 도메인 정의, 도메인별 자산 그룹핑

### 3. 데이터 리니지
- **크로스 플랫폼 리니지**: SQL 파싱·OpenLineage·커스텀 API로 엔드투엔드 리니지 수집
- **컬럼 레벨 리니지**: 컬럼 단위 변환 추적 (지원 소스 범위 제한 있음)
- **Impact Analysis**: 상위 자산 변경의 하위 영향 범위 시각화
- **OpenLineage 네이티브 지원**: Airflow, Spark, dbt의 OpenLineage 이벤트 직접 수집

### 4. AI 및 ML 자산 거버넌스
- **ML 자산 카탈로그**: ML 모델, 피처, 피처 그룹, 실험 자동 카탈로그화
- **벡터 DB·LLM 파이프라인**: AI 시대 신규 자산 타입 지원 확장 중
- **AI 데이터 카탈로그**: 자연어 검색 + 자동 문서화 + 지능형 분류 + 관계 발견 + 이상 탐지 기능 통합
- **MCP 지원**: AI 어시스턴트가 메타데이터를 대화형으로 조회하는 표준 프로토콜 지원

### 5. 데이터 품질 & 관찰성
- **Assertions**: 데이터셋에 대한 기대값(Expectation) 정의 및 자동 실행
- **외부 DQ 통합**: Great Expectations, Monte Carlo, Bigeye 등 연동
- **데이터 상태 표시**: 카탈로그 자산에 품질 상태 배지 자동 표시

### 6. 접근 제어 & 정책
- **메타데이터 접근 정책**: 역할 기반 메타데이터 열람·수정 권한
- **데이터 그룹**: 사용자 그룹별 자산 접근 관리
- **소유권 관리**: Technical Owner / Business Owner 역할 지정

### 7. 확장성 (주요 차별점)
- **플러그인 아키텍처**: 커스텀 엔티티 타입, 커스텀 ingestion 소스, 커스텀 액션 개발 가능
- **Actions Framework**: 메타데이터 이벤트에 반응하는 자동화 액션 트리거 (Slack 알림, Jira 이슈 생성 등)
- **GraphQL API**: 모든 메타데이터 데이터를 프로그래밍적으로 읽기/쓰기

---

## AI-Ready Data 주제 매핑

| 주제코드 | 주제명 | 커버 수준 | 비고 |
|---------|--------|-----------|------|
| A-1 | 데이터 카탈로그 | ○ 완전 | 100+ 커넥터, AI 검색, 자동 문서화 |
| A-2 | 메타데이터 관리 | ○ 완전 | Kafka 스트리밍, GraphQL API, 커스텀 확장 |
| A-3 | 데이터 리니지 | ○ 완전 | 크로스 플랫폼, OpenLineage, 컬럼 레벨 |
| C-3 | Business Glossary | ○ 완전 | 계층 Glossary, 용어-자산 연결 |
| E-1 | 데이터 품질 | △ 부분 | Assertions + 외부 도구 통합 |
| C-1 | 접근 제어 | △ 부분 | 메타데이터 접근 정책, 데이터 직접 접근 제어는 외부 플랫폼 |
| C-2 | 데이터 분류 | ○ 완전 | 분류 태그 자동 전파 |

---

## 강점

1. **오픈소스 무료**: Apache 2.0, 자체 호스팅으로 라이선스 비용 없음 — 예산 제약 조직에 최적
2. **확장성·커스터마이징**: 플러그인 아키텍처로 완전한 커스텀 메타데이터 모델·소스·액션 개발 가능
3. **LinkedIn 실전 검증**: 세계 최대 프로페셔널 네트워크의 메타데이터 인프라를 오픈소스로 공개
4. **MCP 지원**: AI 에이전트 통합 표준 프로토콜 지원으로 미래 AI 환경 대응
5. **커뮤니티**: 13,000+ 슬랙 멤버, 활발한 OSS 생태계 — 빠른 기능 추가·버그 픽스

---

## 약점·주의점

1. **운영 복잡도**: Kafka + 관계형 DB + Elasticsearch + 그래프 DB + Kafka 연결하는 멀티 컴포넌트 — 초기 설치·운영 전문성 필요
2. **Enterprise 기능**: 고급 거버넌스 워크플로우·AI 거버넌스 기능은 DataHub Cloud(유료) 필요
3. **UI/UX**: Collibra·Atlan 대비 비즈니스 사용자 친화도 낮음 — 기술 사용자 중심
4. **규정 준수 자동화**: EU AI Act, GDPR 준수 워크플로우는 별도 구축 필요
5. **엔터프라이즈 지원**: OSS는 커뮤니티 지원만; SLA 기반 지원은 DataHub Cloud 구독 필요

---

## 가격 모델

- **OSS (자체 호스팅)**: 완전 무료 (Apache 2.0), 인프라 비용만 발생
- **DataHub Cloud (SaaS)**: Free Professional 티어 (저장·알림 제한), Enterprise는 영업 채널 협의
- **Series B 이후**: 2025년 $35M 펀딩으로 AI 거버넌스·클라우드 기능 가속화 예정
- 공개 Enterprise 가격 없음

---

## 연동 생태계

- **커넥터 (Ingestion Sources)**: 100+ (Snowflake, Databricks, BigQuery, Redshift, Hive, Presto, Trino, Oracle, SQL Server, dbt, Airflow, Kafka, Looker, Tableau, Power BI, Superset 등)
- **AI/ML**: ML 모델·피처 카탈로그, OpenAI 기반 자동 문서화
- **오픈 표준**: OpenLineage, OpenTelemetry
- **API**: GraphQL API, REST API
- **MCP**: MCP 서버 지원으로 Claude, Cursor 등 AI 도구와 연동
- **Actions Framework**: Slack, Jira, PagerDuty, 커스텀 웹훅 트리거
- **파트너**: Acryl Data (상용 지원), Fivetran, dbt Labs

---

## 출처

- https://datahub.com/
- https://github.com/datahub-project/datahub
- https://siliconangle.com/2025/05/21/datahub-gets-35m-funding-provide-context-needed-ai-reliability-safety/
- https://datahub.com/aiterms/
- https://docs.datahub.com/docs/introduction
- https://datahub.com/blog/ai-assisted-data-catalogs-an-llm-powered-by-knowledge-graphs-for-metadata-discovery/
