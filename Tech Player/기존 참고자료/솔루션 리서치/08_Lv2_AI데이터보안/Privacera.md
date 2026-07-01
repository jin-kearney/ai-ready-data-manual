# Privacera (Trust3 AI) — AI 데이터 보안 솔루션

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Privacera (캘리포니아; 2016 설립 — Apache Ranger 창시자 팀) |
| 라이선스 | 상용 |
| 배포 형태 | SaaS / 셀프 관리(온프레미스 또는 VPC) |
| 최신 동향 | **Trust3 AI** 플랫폼으로 브랜드 재정립 (2025); **PAIG(Privacera AI Governance)** — GenAI 보안·거버넌스 특화 제품 출시; GigaOm Radar 데이터 접근 거버넌스 4년 연속 리더 (2025.07); Big Data London 2025 발표 — AI 시대 데이터 거버넌스 재정의 |

## 한 줄 포지셔닝

> **Apache Ranger 기반 오픈소스 DNA의 통합 데이터 접근 거버넌스 + AI 거버넌스 플랫폼**. 온프레미스 Hadoop·HDFS부터 클라우드 데이터 플랫폼까지 폭넓은 지원과 PAIG를 통한 GenAI·LLM 접근 보안으로 전통적 데이터 거버넌스와 AI 거버넌스를 단일 플랫폼에서 제공한다.

---

## 주요 기능

### 데이터 접근 거버넌스 (핵심)
- **Apache Ranger 기반 정책 엔진**: HDFS, Hive, HBase, Kafka, YARN 등 Hadoop 생태계 + 클라우드 데이터 플랫폼 통합 정책 관리
- **세분화 접근 제어(FGAC)**: 테이블·컬럼·행 수준 접근 제어. 사용자·그룹·역할·속성 기반 정책
- **동적 데이터 마스킹**: 역할에 따라 실시간 마스킹 적용. 이메일 주소, 전화번호, 신용카드 등 엔티티 유형별 마스킹 규칙
- **속성 기반 접근 제어(ABAC)**: 데이터 태그 + 사용자 속성 조합으로 세분화 정책 동적 평가

### PAIG (Privacera AI Governance)
- **AI 학습 데이터 접근 제어**: ML 모델 학습에 사용되는 데이터셋 접근 정책 적용. 누가 어떤 학습 데이터에 접근하는지 감사
- **Prompt 보안**: LLM API 호출 시 사용자 Prompt에 포함된 민감 데이터 탐지·마스킹·차단
- **AI 응답 거버넌스**: LLM 응답에서 민감 데이터 필터링. 사용자 역할에 따른 응답 마스킹
- **RAG 데이터 보안**: Retrieval-Augmented Generation 파이프라인에서 검색·인용되는 문서의 접근 권한 검증
- **AI 사용 감사 로그**: AI 시스템의 데이터 접근·응답 이력 전체 기록. 규제 감사 대응

### 데이터 카탈로그 통합
- **자동 태그 기반 정책**: 데이터 카탈로그(Collibra, Alation)의 민감도 태그를 자동으로 접근 정책에 반영
- **데이터 마켓플레이스**: 사용 가능한 데이터 자산 검색·접근 요청·승인 워크플로

### 멀티 클라우드·플랫폼 지원
- **지원 플랫폼**: Snowflake, Databricks, AWS S3/Glue/EMR, Azure Data Lake Storage/Synapse, Google BigQuery, Hadoop, Hive, Kafka
- **클라우드 네이티브 통합**: AWS Lake Formation, Azure Purview와 통합으로 기존 클라우드 거버넌스 보강

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 매핑 방식 |
|---|---|
| F-4 AI 데이터 보안 | PAIG로 AI/LLM 파이프라인 전 구간 접근 통제·로그 |
| 접근 권한 최소화 | ABAC + FGAC 세분화 정책 |
| AI 학습 데이터 거버넌스 | 학습 데이터 접근 정책·목적 제한 |
| 데이터 거버넌스 | 멀티 플랫폼 통합 정책 관리 |
| Prompt 보안 | PAIG Prompt/응답 PII 탐지·차단 |

---

## 강점

- **온프레미스 Hadoop 지원**: Apache Ranger DNA로 레거시 온프레미스 Hadoop 환경 최강 지원 — 온프레미스 데이터 레이크 보안에 특화
- **PAIG GenAI 거버넌스**: LLM Prompt 보안·AI 사용 감사를 데이터 거버넌스와 통합한 선진적 접근
- **멀티 플랫폼 폭**: Hadoop에서 Snowflake까지 가장 넓은 데이터 플랫폼 지원
- **오픈소스 신뢰성**: Apache Ranger 기반으로 오픈소스 커뮤니티 신뢰도 높음

---

## 약점·주의점

- **UI/UX 성숙도**: Immuta, BigID 대비 관리 콘솔 UI가 상대적으로 복잡. 학습 곡선 존재
- **PII 탐지 기능 제한**: Presidio, BigID 수준의 독립적 PII 탐지 엔진 없음 → 외부 분류 도구 연동 필요
- **브랜드 전환기 혼선**: Trust3 AI로 리브랜딩 중 — 기존 Privacera 문서·지원과의 일관성 확인 필요
- **엔터프라이즈 지원 네트워크**: 한국 내 공식 지원 파트너·레퍼런스 제한적

---

## 가격 모델

| 모델 | 내용 |
|---|---|
| SaaS 구독 | 데이터 소스 수·사용자 수 기반 연간 구독 |
| 셀프 관리 | VPC 또는 온프레미스 배포; 별도 인프라 비용 |
| PAIG 모듈 | AI 거버넌스 기능 별도 구독 옵션 |

---

## 연동 생태계

- **데이터 플랫폼**: Snowflake, Databricks, AWS S3/EMR/Glue, Azure ADLS/Synapse, BigQuery, Hadoop/Hive/HBase
- **데이터 카탈로그**: Collibra, Alation, Apache Atlas
- **클라우드 거버넌스**: AWS Lake Formation, Microsoft Purview
- **AI/ML**: AWS SageMaker, Databricks ML, Azure ML (PAIG 경유)
- **SIEM/모니터링**: Splunk, AWS CloudTrail, Azure Monitor
- **LLM/GenAI**: OpenAI API, Azure OpenAI, Bedrock (PAIG 프록시)

---

## 출처

- [Privacera (Trust3 AI) 공식 홈페이지](https://privacera.com/)
- [Privacera 2025 Vision: GenAI Governance](https://www.prnewswire.com/news-releases/privaceras-2025-vision-generative-ai-governance-at-the-forefront-302331595.html)
- [Privacera AI Governance 플랫폼 (Intellyx 분석)](https://intellyx.com/2025/03/12/privacera-leveraging-data-access-governance-expertise-and-open-source-cred-to-deliver-ai-governance-platform/)
- [GigaOm Radar Leader 2025](https://privacera.com/resource-center/analyst-reports/gigaom-radar-for-data-access-governance-2025/)
- [Big Data London 2025 — AI 거버넌스 미래](https://privacera.com/blog/rethinking-data-governance-ai-big-data-london-2025/)
- [Privacera 2026 프로필 (Tracxn)](https://tracxn.com/d/companies/privacera/__g0XkY1XpcBjqZQZAF3b9ROS-xxNek6e2-6dMtF-O-9g)
