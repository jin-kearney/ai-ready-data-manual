# OpenMetadata — Open Context Layer for Data and AI

> 작성일: 2026-06-10 | 조사 기준: 2025~2026년 최신 릴리스 (v1.12 포함)

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Collate, Inc. (미국) — OpenMetadata OSS 메인테이너 |
| 라이선스 | OSS: Apache License 2.0 / 상용: Collate (관리형 서비스) |
| 배포 형태 | 자체 호스팅 (Docker/Kubernetes) + 관리형 서비스 (Collate Cloud) |
| 최신 주요 릴리스 | v1.12 (2026): Metadata AI SDK + MCP Server 출시; 시맨틱 검색 GA; v1.12.8: 보안 강화·커넥터 개선 |
| 전략 방향 | "Feed AI agents with metadata" — MCP + AI SDK를 AI 에이전트 인프라로 포지셔닝 |

---

## 한 줄 포지셔닝

**배포 단순성과 MCP·AI SDK 네이티브 통합을 앞세운 오픈소스 메타데이터 플랫폼 — 4개 컴포넌트만으로 하루 만에 구동 가능.**

---

## 주요 기능

### 1. 데이터 카탈로그 & 자산 관리
- **포괄적 엔티티 타입**: Tables, Topics (Kafka), Pipelines, Dashboards, ML Models, Containers, Queries, Glossary, Tags 등
- **자동 메타데이터 수집**: 80+ 커넥터 (Databricks, Snowflake, BigQuery, Unity Catalog, Athena, Datalake 등)
- **Tier 분류**: Gold/Silver/Bronze/Not Set으로 데이터 자산 중요도 분류
- **데이터 제품 관리**: 데이터 제품 정의·게시·구독 워크플로우

### 2. MCP Server & AI SDK (v1.12 신기능, 2026 핵심)
- **Native MCP Server**: MCP 호환 클라이언트(Claude, Cursor 등)가 OpenMetadata 메타데이터 그래프를 자연어로 직접 조회
- **Metadata AI SDK**: 외부 에이전트가 OpenMetadata 기능을 프로그래밍적으로 호출
- **시맨틱 컨텍스트 그래프**: 데이터셋의 의미·출처·신뢰도를 에이전트에 구조적으로 제공
- **End-to-End Agentic Data Modeling**: MCP를 통한 영향 분석, 스키마 변경 예측 활용 사례 실증

### 3. 시맨틱 검색 (v1.12 GA)
- **의미 기반 검색**: 정확한 키워드 없이도 개념적으로 유사한 자산 반환
- **자연어 질의**: "3개월 이상 사용되지 않은 고객 테이블"과 같은 자연어 필터 지원
- **AI 보조 발견**: LLM이 연관 자산·용어를 자동 추천

### 4. Business Glossary
- **계층 Glossary**: 카테고리→용어 구조, 다국어 정의 지원
- **태그 시스템**: 계층형 태그·분류 체계 (PII, 민감도, 도메인 등)
- **용어-자산 자동 연결**: AI가 Glossary 용어와 데이터 자산 매핑 제안
- **Glossary Import/Export**: CSV 기반 대량 Glossary 가져오기·내보내기

### 5. 데이터 리니지
- **자동 리니지 수집**: SQL 파싱 + OpenLineage + 커넥터 기반 리니지 자동 수집
- **컬럼 레벨 리니지**: 지원 커넥터(Databricks, BigQuery, dbt 등)에서 컬럼 단위 추적
- **비주얼 리니지 그래프**: 인터랙티브 리니지 시각화, 드릴다운 탐색
- **영향 분석**: 상위 변경의 하위 자산 영향 범위 파악

### 6. 데이터 품질 & 프로파일링
- **컬럼 프로파일링**: 통계(null 비율, 유일값 수, 분포) 자동 계산
- **테스트 스위트**: 내장 DQ 테스트 (값 범위, 패턴, 중복, 완전성 등) + 커스텀 SQL 테스트
- **자동 알림**: 품질 위반 발생 시 슬랙·이메일 자동 알림
- **AI Agent용 경량 프로파일링**: 에이전트 응답 기반 데이터에 적합한 빠른 프로파일 제공

### 7. 협업 & 워크플로우
- **활동 피드**: 메타데이터 변경 이력, 댓글, 태스크 알림
- **태스크 시스템**: 데이터 문서화·품질 문제 수정 태스크 생성·할당·추적
- **공지 & 알림**: 데이터 자산 변경 구독, 알림 채널 설정

---

## AI-Ready Data 주제 매핑

| 주제코드 | 주제명 | 커버 수준 | 비고 |
|---------|--------|-----------|------|
| A-1 | 데이터 카탈로그 | ○ 완전 | 80+ 커넥터, AI 검색, 시맨틱 그래프 |
| A-2 | 메타데이터 관리 | ○ 완전 | MCP + AI SDK, 자동 수집·큐레이션 |
| A-3 | 데이터 리니지 | ○ 완전 | OpenLineage 네이티브, 컬럼 레벨 |
| C-3 | Business Glossary | ○ 완전 | 계층 Glossary, AI 자동 연결, CSV 임포트 |
| E-1 | 데이터 품질 | ○ 완전 | 내장 DQ 테스트, 프로파일링, 알림 |
| C-1 | 접근 제어 | △ 부분 | 메타데이터 접근 정책, 데이터 직접 접근은 소스 플랫폼 |
| C-2 | 데이터 분류 | ○ 완전 | 태그 분류 체계, Tier 시스템 |

---

## 강점

1. **배포 단순성**: 4개 컴포넌트(PostgreSQL/MySQL + Elasticsearch + OpenMetadata 서버 + UI) — DataHub 대비 훨씬 간단, 반나절이면 PoC 구동
2. **MCP + AI SDK 선도**: 오픈소스 데이터 카탈로그 중 가장 완성도 있는 AI 에이전트 인프라
3. **내장 DQ**: 외부 도구 없이도 기본 데이터 품질 테스트 실행 가능
4. **오픈소스 무료**: Apache 2.0, 전체 기능 자체 호스팅 무료 사용
5. **커뮤니티 성장**: AI-Ready Data Stack 포지셔닝으로 커뮤니티·관심 급성장

---

## 약점·주의점

1. **커뮤니티 규모**: DataHub(10,000+ stars) 대비 상대적으로 작은 커뮤니티 (단, 빠르게 성장 중)
2. **엔터프라이즈 워크플로우**: Collibra 수준의 복잡한 거버넌스 워크플로우·정책 엔진 미흡
3. **상용 지원**: SLA 기반 엔터프라이즈 지원은 Collate Cloud 구독 필요
4. **AI 거버넌스**: ML 모델·AI 에이전트 전용 거버넌스는 DataHub, Collibra 대비 미흡
5. **Elasticsearch 의존**: 검색 레이어로 Elasticsearch 필수 — 운영 부담 존재

---

## 가격 모델

- **OSS (자체 호스팅)**: 완전 무료 (Apache 2.0), 인프라 비용만 발생
- **Collate Cloud (관리형)**: 소규모 팀용 유료 플랜 + 엔터프라이즈 협의 가격
- **엔터프라이즈 지원**: 보안 인증, SLA, 전담 지원팀은 유료 구독 필요
- OSS는 비용 없음, 엔터프라이즈 가격은 영업 채널 문의

---

## 연동 생태계

- **커넥터**: 80+ (Databricks Unity Catalog, Snowflake, BigQuery, Redshift, Athena, Datalake, MySQL, PostgreSQL, SQL Server, Oracle, dbt, Airflow, Kafka, Tableau, Looker, Power BI 등)
- **오픈 표준**: OpenLineage, Apache Atlas (마이그레이션 지원)
- **API**: REST API, Python SDK, Java SDK
- **MCP**: 네이티브 MCP Server (v1.12) — Claude Desktop, Cursor, 에이전트 프레임워크 연동
- **AI SDK**: Python 기반 Metadata AI SDK (v1.12) — 외부 에이전트 통합
- **알림**: Slack, Microsoft Teams, Webhook
- **CI/CD**: GitHub Actions, Jenkins 통합

---

## 출처

- https://open-metadata.org/
- https://github.com/open-metadata/openmetadata
- https://docs.open-metadata.org/v1.12.x
- https://blog.pebblous.ai/report/openmetadata-ai-ready-data-2026-04/en/
- https://pipeline2insights.substack.com/p/end-to-end-agentic-data-modeling-with-openmetadata-and-mcp
- https://www.toolworthy.ai/tool/openmetadata
- https://www.modern-datatools.com/tools/openmetadata
