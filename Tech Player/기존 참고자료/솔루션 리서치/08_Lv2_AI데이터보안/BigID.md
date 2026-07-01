# BigID — AI 데이터 보안 솔루션

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | BigID, Inc. (뉴욕 기반; 2016 설립) |
| 라이선스 | 상용 |
| 배포 형태 | SaaS / 온프레미스 / 하이브리드 |
| 최신 동향 | **BigID Next** 플랫폼 출시 (2025.02) — AI 기반 차세대 데이터 보안·컴플라이언스; RSA Conference 2026: DLP Prism, AskBigID GPT, Agentic Access Governance 등 4가지 AI 보안 신기능 발표; Forrester Wave Leader (Q2 2026) — 민감 데이터 탐지·분류 리더 |

## 한 줄 포지셔닝

> **AI 시대를 위한 전사 데이터 보안·프라이버시·거버넌스 플랫폼**. 100+ 데이터 소스에서 PII·민감 데이터를 AI로 탐지·분류하고, AI 학습 데이터 관리부터 Agent 접근 거버넌스까지 AI 라이프사이클 전반을 보호한다.

---

## 주요 기능

### 데이터 탐지·분류 (Discovery & Classification)
- **100+ 데이터 소스 커넥터**: 클라우드 스토리지(S3, Azure Blob, GCS), 데이터 웨어하우스(Snowflake, Redshift, BigQuery), 온프레미스 DB(Oracle, SQL Server, MySQL), 비정형 스토리지(SharePoint, Confluence, Box), 이메일, Slack 등
- **AI/ML 기반 분류**: NLP, NER, 딥러닝으로 정형·비정형 데이터의 PII, PHI, 금융 정보, 기밀 문서 자동 탐지. 문맥 인식(Contextual Classification)으로 오탐 최소화
- **데이터 인벤토리**: 발견된 민감 데이터의 전체 목록, 위치, 분류 레이블, 위험 점수 자동 생성

### AI 거버넌스 (AI Governance — 2025~2026 핵심)
- **AI 학습 데이터 감사**: LLM/ML 모델 학습셋에 포함된 PII·과노출 레코드 탐지. GDPR·PIPA 학습 동의 여부 확인
- **Shadow AI 탐지**: 조직 내 무허가 AI 도구 사용 현황 파악·정책 적용
- **Agentic Access Governance (RSA 2026)**: AI Agent의 데이터 접근 권한 가시성 확보 및 정책 기반 통제
- **Employee AI Governance (RSA 2026)**: 임직원의 AI 도구(ChatGPT, Copilot 등) 사용 시 민감 데이터 유출 모니터링

### 데이터 보안 포지션 관리 (DSPM)
- **실시간 위험 스코어링**: 노출된 민감 데이터의 위험도를 실시간 점수화. 우선순위 기반 대응 가이드
- **DLP Prism (RSA 2026)**: AI 기반 컨텍스트 인식 DLP — 기존 규칙 기반 DLP의 오탐률을 AI로 감소
- **데이터 유출 경보**: 민감 데이터 이상 접근·대량 다운로드 이상 행위 실시간 알림

### 프라이버시 자동화
- **DSAR(정보주체 열람 요청) 자동화**: 정보주체 요청 시 관련 개인정보 자동 검색·리포팅
- **데이터 최소화**: 보존 기간 초과 PII 자동 식별·삭제 워크플로
- **동의 관리 연동**: OneTrust, TrustArc 등 동의 관리 플랫폼과 연동

### AskBigID GPT (RSA 2026)
- **자연어 보안 쿼리**: "Snowflake에서 마스킹 안 된 주민번호가 몇 개인가?" 같은 자연어 질의로 데이터 보안 현황 즉시 파악

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 매핑 방식 |
|---|---|
| F-4 AI 데이터 보안 | DSPM + AI 거버넌스 + Agentic 접근 통제 전체 커버 |
| 데이터 분류 | AI 기반 정형·비정형 PII·민감 데이터 자동 분류 |
| AI 학습 데이터 관리 | 학습셋 PII 감사, 과노출 레코드 탐지 |
| 데이터 카탈로그 연계 | 탐지된 데이터 자산 목록 → 카탈로그 메타데이터 보강 |
| 규제 컴플라이언스 | GDPR, PIPA, HIPAA, CCPA 등 자동 매핑 |

---

## 강점

- **데이터 소스 폭**: 100+ 커넥터로 클라우드·온프레미스·비정형 데이터 소스를 단일 플랫폼에서 전수 탐지
- **AI 기반 정확도**: Forrester Wave Q2 2026 리더 — 탐지 정확도·AI 거버넌스 기능에서 최고 점수(11개 항목 5/5)
- **Agentic AI 거버넌스**: AI Agent가 데이터에 접근하는 2025~2026 트렌드에 맞춰 가장 빠르게 대응
- **DSPM 통합**: 탐지→분류→위험 평가→대응을 단일 플랫폼으로 통합

---

## 약점·주의점

- **비용**: 엔터프라이즈 수준 가격. 데이터 소스 수·스캔 볼륨 기반 구독으로 대규모 환경에서 상당한 비용
- **토큰화 직접 기능 제한**: Protegrity 수준의 필드 수준 vaultless 토큰화 기능은 약함 → 마스킹·분류 중심
- **설치·구성 복잡도**: 스캐너 배포, 크리덴셜 관리, 분류 정책 튜닝에 초기 공수 필요
- **한국 PIPA 로컬라이제이션**: 100+ 규제 중 한국 PIPA는 포함되나 로컬 지원 성숙도 확인 필요

---

## 가격 모델

| 모델 | 내용 |
|---|---|
| 구독 (SaaS) | 데이터 소스 수 + 스캔 볼륨 기반 연간 구독; 엔터프라이즈 계약 |
| 온프레미스 | 별도 계약; 인프라 자체 제공 |
| 모듈형 | 데이터 탐지, DSPM, 프라이버시, AI 거버넌스 모듈별 선택 구매 가능 |

---

## 연동 생태계

- **데이터 플랫폼**: Snowflake, Databricks, BigQuery, Redshift, Azure Synapse
- **클라우드 스토리지**: AWS S3, Azure Blob, Google GCS
- **ITSM/SIEM**: ServiceNow, Splunk, IBM QRadar
- **DLP/보안**: Microsoft Purview, Palo Alto DSPM, Wiz
- **프라이버시 플랫폼**: OneTrust, TrustArc, Securiti
- **AI 플랫폼**: AWS SageMaker, Azure ML, Databricks ML

---

## 출처

- [BigID 공식 홈페이지](https://bigid.com/)
- [BigID Next 플랫폼 출시 (PR Newswire 2025.02)](https://www.prnewswire.com/news-releases/bigid-unveils-bigid-next-its-next-gen-ai-powered-data-security-compliance--privacy-platform-302382052.html)
- [RSA 2026 AI 보안 4가지 신기능 (Dealroom)](https://app.dealroom.co/news/feed/bigid-named-leader-in-sensitive-data-discovery-unveils-four-new-ai-security-capabilities-at-rsa-conference-2026)
- [Forrester Wave Leader 2026](https://bigid.com/blog/bigid-forrester-wave-leader-sensitive-data-discovery-classification-2026/)
- [BigID Agentic AI 거버넌스 (DZone)](https://dzone.com/articles/from-llms-to-agents-how-bigid-is-enabling-secure-a-1)
- [Identity Governance for AI Systems 2026](https://bigid.com/blog/identity-governance-for-ai-systems/)
