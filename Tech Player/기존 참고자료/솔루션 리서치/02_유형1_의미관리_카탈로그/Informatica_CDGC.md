# Informatica — Cloud Data Governance & Catalog (CDGC)

> 작성일: 2026-06-10 | 조사 기준: 2025~2026년 최신 릴리스 (IDMC Spring 2026 포함)

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Informatica Inc. (미국, 레드우드시티) — Salesforce 전략 파트너 |
| 라이선스 | 상용 |
| 배포 형태 | SaaS (Informatica Intelligent Data Management Cloud, IDMC) + 일부 하이브리드 |
| 최신 주요 릴리스 | 2025-07: AI 거버넌스 인벤토리·워크플로우; 2025-10: 비정형 데이터 거버넌스(Private Preview); 2026-05: CLAIRE GPT GA (Google Cloud), Google Cloud 전략 파트너십 확대 |
| AI 브랜드 | CLAIRE® (Cloud-Leveraging AI for Intelligent Recognition and Extraction) |

---

## 한 줄 포지셔닝

**CLAIRE AI 기반으로 데이터 통합(ETL/ELT)·품질·거버넌스·MDM을 단일 IDMC 플랫폼에 통합 — 기존 Informatica 투자 조직의 자연스러운 거버넌스 확장 경로.**

---

## 주요 기능

### 1. Cloud Data Governance & Catalog (CDGC)
- **자동 메타데이터 수집**: 100+ 커넥터로 클라우드·온프레미스 데이터 자산 자동 카탈로그화
- **비즈니스 용어 사전(Glossary)**: 전사 표준 용어 정의, 계층 구조, 승인 워크플로우
- **데이터 분류**: 시스템 정의 분류체계 + 커스텀 분류 태그
- **데이터 제품 관리**: 데이터 제품 정의·게시·거버넌스
- **비정형 데이터 거버넌스 (2025 Private Preview)**: 비정형 파일을 분류·카탈로그화하여 GenAI 사용 사례에 큐레이션

### 2. CLAIRE® AI (핵심 차별점)
- **CLAIRE GPT (GA 2026-05)**: 자연어로 데이터 자산 발견, 메타데이터 보강, 품질 평가, 거버넌스 이슈 해결
- **CLAIRE Copilot for MDM**: 마스터 데이터 이해·탐색을 자연어 쿼리로 간소화
- **자동 메타데이터 생성**: AI 기반 테이블·컬럼 설명 자동 생성, 분류 자동화
- **이상 탐지**: 데이터 드리프트·품질 저하 자동 탐지 및 알림

### 3. 데이터 리니지
- **크로스 플랫폼 엔드투엔드 리니지**: Informatica PowerCenter·IICS 파이프라인부터 BI 리포트까지 완전한 리니지
- **컬럼 레벨 리니지**: 소스→변환→타겟까지 컬럼 단위 추적
- **AI 모델 리니지 (2025 신기능)**: ML 모델 학습 데이터, 평가 지표, 배포 이력 추적
- **Impact Analysis**: 상위 변경이 하위 리포트·데이터셋에 미치는 영향 즉시 파악

### 4. AI 거버넌스 (2025~2026 핵심 투자 영역)
- **AI 사용 사례 카탈로그**: AI 모델·데이터셋·승인 이력을 CDGC에서 중앙 관리
- **멀티에이전트 시스템 모델링 (2025 신기능)**: 복잡한 AI 에이전트 시스템을 CDGC에서 모델링·거버넌스
- **Vertex AI 스캔 (2025 신기능)**: Google Vertex AI AI 자산 인벤토리를 CDGC로 자동 스캔
- **평가 지표 커스터마이징**: AI 모델 성능·편향·공정성 지표 커스텀 정의
- **비즈니스 친화적 워크플로우 빌더**: AI 모델 승인 워크플로우를 코드 없이 구성

### 5. 데이터 품질
- **Cloud Data Quality (CDQ)**: 전사 데이터 품질 규칙 정의, 자동 체크, 스코어카드
- **프로파일링**: 컬럼 통계, 패턴 분석, 완전성·정확성·유일성 자동 계산
- **CLAIRE 기반 이상 탐지**: AI가 데이터 패턴 변화를 자동 탐지
- **DQ와 거버넌스 통합**: DQ 결과가 CDGC 자산 신뢰도 점수에 자동 반영

### 6. 접근 제어 & 정책
- **역할 기반 접근 제어**: IDMC 내 세분화된 역할·권한 관리
- **정책 템플릿**: GDPR, CCPA 등 규정 준수 정책 템플릿 제공
- **승인 워크플로우**: 데이터 접근 요청→도메인 소유자 승인→자동 반영

### 7. Master Data Management (MDM) 통합
- **단일 IDMC 플랫폼**: ETL/ELT + DQ + CDGC + MDM을 동일 플랫폼에서 운영
- **CLAIRE GPT for MDM**: 마스터 데이터 자연어 탐색
- **MDM ↔ Catalog 연계**: 마스터 데이터 엔티티가 카탈로그 자산에 자동 연결

---

## AI-Ready Data 주제 매핑

| 주제코드 | 주제명 | 커버 수준 | 비고 |
|---------|--------|-----------|------|
| A-1 | 데이터 카탈로그 | ○ 완전 | CDGC, 100+ 커넥터, CLAIRE 자동화 |
| A-2 | 메타데이터 관리 | ○ 완전 | CLAIRE 자동 생성, 기술·비즈니스 메타데이터 |
| A-3 | 데이터 리니지 | ○ 완전 | 크로스 플랫폼, 컬럼 레벨, AI 리니지 |
| C-3 | Business Glossary | ○ 완전 | 계층 Glossary, 승인 워크플로우, 정책 연동 |
| E-1 | 데이터 품질 | ○ 완전 | CDQ 완전 통합, CLAIRE 이상 탐지 |
| C-1 | 접근 제어 | ○ 완전 | IDMC RBAC, 정책 템플릿, 승인 워크플로우 |
| C-2 | 데이터 분류 | ○ 완전 | 자동 분류, 비정형 포함(Preview) |

---

## 강점

1. **IDMC 올인원**: 데이터 통합(ETL)·품질·거버넌스·MDM을 단일 플랫폼 — 기존 Informatica 투자 조직의 최적 확장
2. **CLAIRE GPT**: 자연어로 데이터 발견·품질 해결·거버넌스 — 비기술 사용자 접근성 향상
3. **SAP 커넥터 성숙도**: SAP ERP(S/4HANA, BW, ECC) 메타데이터 수집 전문 성숙도 — SAP 기반 대기업에 강점
4. **AI 거버넌스 투자**: Vertex AI 스캔, 멀티에이전트 모델링, AI 승인 워크플로우 등 빠른 기능 확장
5. **엔터프라이즈 안정성**: 대규모 엔터프라이즈 조직의 수십 년 데이터 관리 경험 기반

---

## 약점·주의점

1. **매우 높은 비용**: 전체 IDMC 스위트 $200K~$500K+/년, 엔터프라이즈 $750K~$2M+/년
2. **IPU 모델 복잡도**: 소비 기반 IPU 과금 모델이 비용 예측을 어렵게 함
3. **MCP 미지원**: AI 에이전트 표준 프로토콜(MCP) 공식 지원 없음 (2026 기준)
4. **구현 기간**: 대규모 IDMC 구현은 수개월~1년, 전문 파트너 필수
5. **UI 복잡성**: 기능이 많은 만큼 학습 곡선 높음, 사용자 채택 교육 필요

---

## 가격 모델

- **IPU (Informatica Processing Unit)** 소비 기반: 서비스별(CDI, CDQ, CDGC, MDM) 독립 과금 또는 번들
- **중소기업**: $50K~$150K+/년 (CDGC 단독 기준)
- **대기업 (전체 IDMC)**: $200K~$500K+/년
- **엔터프라이즈 전체**: $750K~$2M+/년 (50+사용자, MDM 포함)
- **할인**: 다년 계약·볼륨 기반 10~20% 할인 일반적
- 공개 가격 없음, 영업 채널 견적 필수

---

## 연동 생태계

- **커넥터**: 100+ (Snowflake, Databricks, BigQuery, Redshift, SAP, Oracle, SQL Server, Salesforce, ServiceNow, Azure, AWS, Google Cloud 등)
- **SAP 연동**: SAP BW, S/4HANA, ECC — 메타데이터·데이터 통합 모두 성숙 (두산 환경에 강력 추천)
- **BI**: Tableau, Power BI, Looker, SAP BusinessObjects
- **AI 플랫폼**: Google Vertex AI (스캔 통합), AWS, Azure AI
- **API**: REST API, CLAIRE GPT API
- **MCP**: 공식 미지원 (2026 기준); 로드맵 대기
- **파트너**: Collibra (보완 운영), dbt, Fivetran, Google Cloud (전략 파트너)

---

## 출처

- https://www.informatica.com/products/data-governance/cloud-data-governance-and-catalog.html
- https://www.informatica.com/about-us/news/news-releases/2025/07/20250731-informatica-boosts-ai-capabilities-with-latest-intelligent-data-management-cloud-platform-release.html
- https://www.informatica.com/about-us/news/news-releases/2025/10/20251029-informatica-announces-fall-2025-release-with-latest-innovations-to-intelligent-data-management-cloud.html
- https://www.informatica.com/about-us/news/news-releases/2025/05/20250514-informatica-unveils-agentic-ai-offerings-on-industrys-first-ai-powered-cloud-data-management-platform.html
- https://www.informatica.com/about-us/news/news-releases/2026/05/20260520-informatica-deepens-strategic-partnership-with-google-cloud-bringing-headless-data-management-and-claire-conversational-ai-to-the-enterprise.html
- https://mammoth.io/blog/informatica-pricing/
