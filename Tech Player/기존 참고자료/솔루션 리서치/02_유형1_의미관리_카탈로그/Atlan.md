# Atlan — Context Layer for AI

> 작성일: 2026-06-10 | 조사 기준: 2025~2026년 최신 릴리스

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Atlan Technologies Pvt. Ltd. (싱가포르 설립, 미국·인도 운영) |
| 라이선스 | 상용 (SaaS 전용) |
| 배포 형태 | SaaS 전용 |
| 최신 주요 릴리스 | 2025: MCP Server 출시; Context Agents GA (690K+ 설명 자동 생성); 2026: Iceberg 기반 메타데이터 레이크하우스 아키텍처 |
| 시장 위치 | Gartner MQ 2025 Metadata Management Leader; 2026 Data & Analytics Governance Leader |

---

## 한 줄 포지셔닝

**80+ 데이터 시스템을 연결하는 AI 에이전트의 컨텍스트 레이어 — MCP 네이티브로 Claude·Cursor·Copilot 등 모든 AI 도구에 신뢰 메타데이터를 즉시 제공.**

---

## 주요 기능

### 1. Active Metadata & 데이터 카탈로그
- **실시간 Active Metadata**: 80+ 시스템의 메타데이터가 실시간으로 업데이트 — AI 에이전트가 항상 최신 컨텍스트 확보
- **Iceberg 기반 메타데이터 레이크하우스**: 메타데이터 자체를 Apache Iceberg 기반으로 관리, 시계열 추적 및 쿼리 가능
- **GraphQL API**: AI 에이전트가 메타데이터 그래프를 직접 쿼리
- **Context Catalog**: AI·BI·데이터 팀이 공유하는 통합 맥락 카탈로그

### 2. MCP 네이티브 통합 (2025 핵심 차별점)
- **Atlan MCP Server**: Claude Desktop, Cursor, 내부 에이전트 프레임워크가 Atlan 메타데이터를 자연어로 직접 조회
- **지원 기능**: 자산 검색, 리니지 추적, DSL 기반 쿼리, 메타데이터 업데이트(설명·인증 상태)
- **100+ 커넥터 연동**: 모든 커넥터 데이터가 MCP를 통해 AI 도구에 노출
- **A2A (Agent-to-Agent)**: 에이전트 간 프로토콜도 지원

### 3. Context Agents (2025~2026 핵심 기능)
- **자동 컨텍스트 생성**: 80+ 시스템 통합 컨텍스트에서 설명·지표·온톨로지 자동 생성
- **2026-04 실적**: 50+ 엔터프라이즈 고객에 690K+ 자산 설명 자동 생성, 87%가 인간 작성 수준 이상 평가
- **사람 검증 후 활성화**: Context Agents 생성 → 전문가 인증 → MCP·SQL·API로 활성화
- **Context Engineering Studio**: 컨텍스트 생성·검증·배포를 위한 워크스페이스

### 4. Business Glossary & 시맨틱 레이어
- **계층 Glossary**: 카테고리→용어의 구조, 비즈니스 정의·동의어·예시 관리
- **용어-자산 자동 연결**: Context Agents가 Glossary 용어를 관련 데이터 자산에 자동 연결 제안
- **공인 지표 관리**: 비즈니스 KPI·지표를 Glossary로 정의하고 BI 시스템에 전파
- **도메인 기반 거버넌스**: 팀·도메인별 분산 Glossary 관리 지원

### 5. 데이터 리니지
- **크로스 플랫폼 자동 리니지**: SQL 파싱·API 수집·OpenLineage 통합으로 엔드투엔드 리니지
- **컬럼 레벨 리니지**: 세분화된 변환 추적
- **Propagated Certification**: 리니지 따라 인증 상태·분류 태그 자동 전파
- **AI 에이전트용 리니지 API**: MCP를 통해 에이전트가 리니지 그래프 탐색

### 6. 데이터 품질 연동
- **DQ 파트너 통합**: Monte Carlo, Great Expectations, dbt Tests, Soda 연동
- **품질 배지**: 카탈로그 자산에 DQ 상태 자동 표시
- **자체 DQ 규칙**: 기본 수준의 인라인 품질 체크 지원

### 7. 접근 제어 & 데이터 제품
- **메타데이터 기반 접근 정책**: 카탈로그에서 접근 요청→승인→실행 워크플로우
- **데이터 제품 게시**: 도메인 팀이 데이터 제품을 마켓플레이스 형태로 게시
- **소유권·스튜어드십**: 자산별 오너·스튜어드 지정, 책임 분명화

---

## AI-Ready Data 주제 매핑

| 주제코드 | 주제명 | 커버 수준 | 비고 |
|---------|--------|-----------|------|
| A-1 | 데이터 카탈로그 | ○ 완전 | Active Metadata, Context Catalog, AI 자동화 |
| A-2 | 메타데이터 관리 | ○ 완전 | 실시간 업데이트, 80+ 커넥터, GraphQL API |
| A-3 | 데이터 리니지 | ○ 완전 | 크로스 플랫폼, 컬럼 레벨, MCP 노출 |
| C-3 | Business Glossary | ○ 완전 | Context Agents 자동 연결, 도메인 분산 관리 |
| E-1 | 데이터 품질 | △ 부분 | 파트너 통합 중심, 자체 DQ는 제한적 |
| C-1 | 접근 제어 | △ 부분 | 접근 요청 워크플로우, 직접 정책 실행은 플랫폼 의존 |
| C-2 | 데이터 분류 | △ 부분 | AI 분류 제안, 자동 민감정보 분류는 제한적 |

---

## 강점

1. **MCP 네이티브 선도**: 데이터 카탈로그 중 가장 성숙한 MCP 서버 — Claude·Cursor 등 AI 도구와 즉시 연동
2. **빠른 온보딩**: SaaS 전용으로 설치 부담 없음, 커넥터 연결 후 수일 내 운영
3. **Context Agents**: 자동 설명 생성 품질이 인간 작성 수준 — 큐레이션 공수 대폭 절감
4. **Active Metadata**: 실시간 메타데이터로 AI 에이전트가 항상 최신 컨텍스트 확보
5. **현대 데이터 스택 최적**: dbt, Fivetran, Airbyte, Looker, Modern Data Stack 환경에서 강점

---

## 약점·주의점

1. **SaaS 전용**: 온프레미스·하이브리드 배포 불가 — 데이터 주권 요구 환경 제약
2. **엔터프라이즈 워크플로우 미흡**: Collibra 수준의 복잡한 거버넌스 워크플로우·정책 엔진 부족
3. **자체 DQ 약함**: 데이터 품질 기능이 파트너 통합에 의존적
4. **온프레미스 데이터 소스 제한**: 방화벽 내 온프레미스 DB 커넥터는 별도 에이전트 설치 필요
5. **가격 불투명**: 공개 가격 없어 예산 계획 수립 어려움

---

## 가격 모델

- **공개 가격 없음**: 사용자 수·커넥터 수·계약 구조에 따라 맞춤 견적
- **시작 가격**: ~$100K+/년 (소규모 팀)
- **엔터프라이즈 MCP 서버**: ~$1,200/월 (소규모), ~$5,000/월+ (엔터프라이즈)
- **커스텀 커넥터**: $5,000~$20,000+ (복잡도에 따라)
- **벤더 데이터**: 연간 계약 $15,000~$150,000+ 범위 (규모에 따라 크게 차이)

---

## 연동 생태계

- **커넥터**: 80+ (Snowflake, Databricks, BigQuery, Redshift, dbt, Fivetran, Airbyte, Airflow, Tableau, Looker, Power BI, Monte Carlo, Soda 등)
- **AI 도구**: Claude Desktop, Cursor, GitHub Copilot, Frontier Agents, 내부 에이전트 프레임워크
- **API**: REST API, GraphQL API
- **MCP**: 네이티브 MCP Server — 자산 검색, 리니지, 메타데이터 업데이트 지원
- **오픈 표준**: Apache Iceberg(메타데이터 레이크하우스), OpenLineage
- **AWS Marketplace**: AWS 마켓플레이스 등재로 통합 과금 가능

---

## 출처

- https://atlan.com/
- https://blog.atlan.com/announcements/atlan-mcp-ai-metadata/
- https://atlan.com/know/what-is-atlan-mcp/
- https://atlan.com/active-metadata-101/
- https://atlan.com/know/context-catalog/
- https://atlan.com/modern-data-catalog/
- https://datastackindex.com/data-observability/tools/atlan/
- https://aws.amazon.com/marketplace/pp/prodview-4qh23e5eiqwow
