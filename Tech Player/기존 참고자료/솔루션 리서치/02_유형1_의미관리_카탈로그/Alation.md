# Alation — Agentic Data Intelligence Platform

> 작성일: 2026-06-10 | 조사 기준: 2025~2026년 최신 릴리스

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Alation, Inc. (미국, 레드우드시티) |
| 라이선스 | 상용 |
| 배포 형태 | SaaS (Alation Cloud Service) + 온프레미스 |
| 최신 주요 릴리스 | 2025-03: Documentation Agent·Data Quality Agent 출시; 2025-10: Agent Builder; 2025-11: CDE Manager; 2026: 선언적 거버넌스(Declarative Governance) 확장 |
| 시장 위치 | Gartner MQ Data & Analytics Governance Leader; Forrester Wave Leader |

---

## 한 줄 포지셔닝

**쿼리 로그(Query Log Ingestion) 기반 신뢰도 지표와 에이전틱 AI를 결합한 데이터 지식 레이어 — 분석가·데이터 엔지니어가 실제로 쓰는 카탈로그.**

---

## 주요 기능

### 1. 데이터 카탈로그
- **Query Log Ingestion (QLI)**: 실제 쿼리 이력 분석으로 "얼마나 자주 쓰이는지" 신뢰도 지표(Popularity) 자동 산출
- **자산 발견**: 100+ 커넥터로 테이블·컬럼·BI 리포트·ML 모델 자동 수집
- **Stewardship 워크플로우**: 데이터 자산 큐레이션, 인증(Endorsed/Deprecated/Warning) 상태 관리
- **Chat with Your Data (2025 신기능)**: 자연어로 데이터 질의, 답변 정확도 30% 향상 (내부 발표)

### 2. Business Glossary & 협업
- **계층적 Glossary**: 그룹→용어의 구조, 정의·동의어·관련 자산 연결
- **용어 보증 워크플로우**: 도메인 전문가 검토·승인·버전 이력
- **Wiki 형식 문서**: 자산별 Wiki 페이지로 비즈니스 컨텍스트 공유
- **댓글·Q&A**: 데이터 자산에 대해 팀 간 질문·답변 협업

### 3. 데이터 리니지
- **크로스 플랫폼 리니지**: SQL 파싱 + QLI 기반 자동 리니지 (Databricks, Snowflake, BigQuery, Redshift, dbt 등)
- **컬럼 레벨 리니지**: 원본 컬럼→변환→리포트 필드까지 세분화 추적
- **Impact Analysis**: 상위 테이블 변경 시 영향받는 하위 자산 즉시 파악
- **lineage API**: 외부 파이프라인 리니지 수동 주입 가능

### 4. 에이전틱 AI 기능 (2025~2026 핵심 업데이트)
- **Documentation Agent**: 데이터 자산 제목·설명 자동 생성, 큐레이션 자동화
- **Data Quality Agent**: 데이터 이상 자동 감지, 품질 규칙 자동 적용
- **Data Products Builder Agent**: 신뢰 데이터셋을 No-code 인터페이스로 패키징
- **Agent Builder (2025-10)**: 고객이 구조화 데이터 기반 자체 에이전트 구축·배포
- **CDE Manager (2025-11)**: 핵심 데이터 요소(CDE) 자동 식별, 거버넌스 우선순위화
- **선언적 거버넌스 (2026 확장)**: 비즈니스 성과 목표 정의 → 에이전트가 자동 실행

### 5. 데이터 품질
- **인라인 DQ 규칙**: 쿼리 실행 시 품질 체크 내장
- **관찰성 연동**: Monte Carlo, Great Expectations 등 외부 DQ 도구 통합
- **CDE 기반 품질 우선순위**: 중요 데이터 요소(CDE) 중심으로 품질 거버넌스 집중

### 6. 접근 제어 & 정책
- **정책 문서화**: 데이터 사용 정책을 카탈로그에서 문서화·게시
- **접근 요청 워크플로우**: 사용자 접근 요청→데이터 소유자 승인→플랫폼 반영
- **Stewardship 역할 관리**: 도메인 스튜어드 지정, 책임 분명화

---

## AI-Ready Data 주제 매핑

| 주제코드 | 주제명 | 커버 수준 | 비고 |
|---------|--------|-----------|------|
| A-1 | 데이터 카탈로그 | ○ 완전 | QLI 기반 신뢰도, Chat with Data, Agent |
| A-2 | 메타데이터 관리 | ○ 완전 | 자동 수집, 에이전트 자동 문서화 |
| A-3 | 데이터 리니지 | ○ 완전 | 크로스 플랫폼, 컬럼 레벨 |
| C-3 | Business Glossary | ○ 완전 | 계층 Glossary, 승인 워크플로우, Wiki |
| E-1 | 데이터 품질 | △ 부분 | DQ Agent 있음, 전용 DQ 플랫폼 대비 제한적 |
| C-1 | 접근 제어 | △ 부분 | 정책 문서화·접근 요청, 직접 정책 실행은 제한 |
| C-2 | 데이터 분류 | △ 부분 | 커스텀 태그 분류, 자동 민감정보 분류는 제한적 |

---

## 강점

1. **QLI 기반 신뢰도**: 쿼리 이력 기반 인기도·신뢰도 지표 — 어떤 데이터가 실제 쓰이는지 객관적 파악 가능
2. **분석가·엔지니어 채택 높음**: 사용자가 자주 방문하고 기여하는 실용적 카탈로그 문화 형성
3. **에이전틱 AI 선도**: Documentation/DQ/Products Builder Agent로 거버넌스 자동화 개척
4. **dbt 통합**: dbt 프로젝트 자동 임포트, SQL 기반 변환 파이프라인 거버넌스
5. **유연한 배포**: SaaS + 온프레미스 모두 지원

---

## 약점·주의점

1. **높은 비용**: $198K+/년, 최소 25 Creator 시트 팩 → 소규모 조직 진입 장벽 높음
2. **MCP 미지원**: AI 에이전트 통합 표준 프로토콜 공식 미지원 (2026 기준)
3. **AI 거버넌스 한계**: Collibra 수준의 AI 모델·에이전트 전용 거버넌스 기능 부족
4. **접근 정책 직접 실행 불가**: 카탈로그에서 정책 정의 후 플랫폼 실행은 별도 연동 필요
5. **대규모 커스터마이징**: 매우 특수한 요구사항은 전문 파트너 필요

---

## 가격 모델

- **구독 기반**: Creator/Steward/Viewer 페르소나 구분
- **최소 25 Creator 팩**: 시작 비용 높음
- **일반 기업 배포**: $198,000+/년 (중간값), 대기업은 수억 원 수준
- **SaaS vs. 온프레미스**: 온프레미스는 별도 인프라 비용 추가
- **추가 모듈**: Data Quality, Open Connector Framework 별도 과금 가능
- 공개 가격 없음, 영업 채널 견적 필수

---

## 연동 생태계

- **커넥터**: 100+ (Snowflake, Databricks, BigQuery, Redshift, Oracle, SQL Server, SAP, Tableau, Power BI, Looker, dbt, Airflow, Fivetran 등)
- **DQ 도구**: Monte Carlo, Great Expectations, dbt 테스트 통합
- **AI/ML**: 에이전트 통합(Agent Builder SDK), OpenAI API 연동
- **API**: REST API, Open Connector Framework (커스텀 커넥터 개발)
- **MCP**: 공식 MCP 서버 미제공 (2026 기준)
- **파트너**: Informatica, Collibra와 상호 보완 운영 사례 존재

---

## 출처

- https://www.alation.com/news-and-press/alation-announces-agentic-platform-reinventing-the-data-catalog-for-ai-era/
- https://www.techtarget.com/searchdatamanagement/news/366634209/Alation-unveils-agentic-AI-suite-for-governing-critical-data
- https://www.techtarget.com/searchdatamanagement/news/366639805/Alation-automates-governance-with-latest-AI-powered-suite
- https://www.techtarget.com/searchdatamanagement/news/366619841/Alation-unveils-AI-agents-plus-SDK-for-agentic-development
- https://venturebeat.com/data-infrastructure/alation-says-new-query-feature-offers-30-accuracy-boost-helping-enterprises-turn-data-catalogs-into-problem-solvers
- https://atlan.com/alation-pricing/
