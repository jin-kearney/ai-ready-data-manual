# Acceldata — Autonomous Data & AI 플랫폼

> 작성일: 2026-06-10 | 카테고리: 유형② 신뢰 통제

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Acceldata (산호세, 2018년 설립) |
| 라이선스 | 상용 |
| 배포 형태 | SaaS + 온프레미스 + 하이브리드 |
| 최신 동향 | 2025.08: Agentic Data Management(ADM) GA 출시; 2026.05: Autonomous Data & AI Platform 론칭; xLake MCP-DC(Model Context Protocol Distributed Compute) 발표; Hadoop·온프레미스 관측 강점 유지하며 클라우드 Agentic AI로 진화 |

---

## 한 줄 포지셔닝

**"Hadoop·온프레미스부터 Snowflake·Databricks 클라우드까지 하이브리드 환경을 단일 Agentic 플랫폼으로 통합 관측하는 엔터프라이즈 솔루션"**

---

## 주요 기능

### 1. Acceldata Pulse (인프라·파이프라인 Observability)
- Hadoop(HDFS, YARN, Hive, Spark) 클러스터 전층 관측
- 데이터 파이프라인 실패·지연·리소스 낭비 실시간 감지
- 레거시 온프레미스 환경에서 유일하게 검증된 Observability 레이어

### 2. Acceldata Torch (데이터 품질)
- 데이터 레이크·데이터 웨어하우스용 다차원 품질 솔루션
- 포맷·신선도·조정(Reconciliation)·완전성 등 포괄적 품질 규칙
- No-code/Low-code 품질 룰 생성 + 스마트 제안
- Snowflake, Databricks 네이티브 통합

### 3. Agentic Data Management Platform (ADM, 2025 GA)
- 10개 이상 AI 에이전트: 데이터 품질, 프로파일링, 이상탐지, 데이터 드리프트, 비용, 쿼리 최적화
- 반응적 모니터링 → 선제적 자율 운영으로 패러다임 전환
- 이상 탐지 → 자동 조사 → 권고 조치 → 실행 워크플로우

### 4. xLake MCP-DC (2025 신기능)
- 최초의 분산 데이터 제어 플레인, 지능형 에이전트 전용 설계
- AWS, GCP, Azure, Snowflake, Databricks, 온프레미스 환경을 단일 API로 제어
- MCP(Model Context Protocol) 표준 지원으로 LLM 에이전트와 데이터 계층 연결

### 5. 다차원 비용 최적화
- 데이터 인프라 비용(컴퓨팅·스토리지) 가시성 + 최적화 권고
- Snowflake, Databricks 지출 분석 및 낭비 자원 탐지

---

## AI-Ready Data 주제 매핑

| 주제 코드 | 주제명 | 지원 수준 |
|---|---|---|
| C-1 | 데이터 Observability | ○ Pulse(인프라) + Torch(품질) 통합 |
| C-2 | 품질관리 | ○ Torch 핵심 기능 |
| C-3 | 데이터 Lineage | ○ 파이프라인 Lineage |

---

## 강점

- **하이브리드 환경 유일성**: Hadoop·온프레미스부터 모던 클라우드까지 단일 플랫폼 — 레거시 환경 많은 대기업에 최적
- **인프라 + 데이터 품질 통합**: 데이터 문제의 인프라 원인(클러스터 과부하 등)까지 연결 분석
- **Agentic AI 선도**: 10개 이상 전문 에이전트로 자율 데이터 운영 구현 최전선
- **MCP 표준 지원**: LLM 에이전트 프레임워크와 표준 방식으로 연동 — 미래 호환성
- **대기업 검증**: 복잡한 하이브리드·고규제 환경에서의 엔터프라이즈 레퍼런스 보유

---

## 약점 및 주의점

- **복잡성**: 모듈 수가 많아 초기 도입·설정 복잡도 높음
- **비투명 가격**: 공개 가격표 없음, 규모·환경별 견적 필요
- **오픈소스 없음**: 완전 상용 플랫폼
- **SME(중소기업) 부적합**: 기능·가격 모두 엔터프라이즈 중심 — 소규모 팀에 과잉
- **데이터 계약 제한**: SodaCL 수준의 계약 명세 엔진 없음

---

## 가격 모델

- **완전 커스텀 견적**: 조직 규모·환경·모듈 조합에 따라 차등
- AWS Marketplace 등재 (Acceldata Data Observability Cloud)
- 무료 데모·POC 제공

---

## 연동 생태계

| 카테고리 | 연동 도구 |
|---|---|
| 레거시 인프라 | Hadoop (HDFS, YARN, Hive), Spark, Kafka |
| 데이터 웨어하우스 | Snowflake, Databricks, BigQuery, Redshift |
| 파이프라인 | Airflow, dbt |
| 마켓플레이스 | AWS Marketplace |
| 에이전트/AI | xLake MCP-DC, LLM 에이전트 연동 |
| 알림 | Slack, PagerDuty, Jira |
| API | REST API, Python SDK |

---

## 출처

- https://www.acceldata.io/
- https://www.acceldata.io/pulse
- https://docs.acceldata.io/torch/
- https://www.acceldata.io/newsroom/acceldata-launches-industrys-first-agentic-data-management-platform
- https://www.acceldata.io/newsroom/acceldata-unveils-agentic-data-management-platform-at-autonomous-25
- https://www.businesswire.com/news/home/20260519971551/en/Acceldata-Launches-Autonomous-Data-AI-Platform-for-Agentic-AI-Era
- https://aws.amazon.com/marketplace/pp/prodview-p2wjjciztguf6
