# Immuta — AI 데이터 보안 솔루션

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Immuta, Inc. (보스턴; 2015 설립) |
| 라이선스 | 상용 |
| 배포 형태 | SaaS / 셀프 관리(on-prem 또는 VPC 내 배포) |
| 최신 동향 | **Immuta AI + Copilot** 출시 (2025.03) — AI 기반 정책 자동화·접근 워크플로 가속; 2025 데이터 보안 현황 보고서 — 거버넌스 팀의 AI 스케일 대응 한계 진단; Snowflake Native App 지원 강화 |

## 한 줄 포지셔닝

> **데이터 플랫폼(Snowflake·Databricks) 네이티브 정책 기반 접근 통제 전문**. ABAC(속성 기반 접근 제어)와 동적 데이터 마스킹으로 데이터 플랫폼에서 민감 데이터를 보호하고, Immuta AI가 AI 스케일의 거버넌스 자동화를 지원한다.

---

## 주요 기능

### 정책 기반 접근 제어 (핵심)
- **ABAC(Attribute-Based Access Control)**: 사용자 속성(부서, 역할, 지역, 프로젝트)과 데이터 속성(분류 레이블, 민감도)을 조합한 세분화 접근 정책
- **정책 자동 변환**: 자연어로 작성한 정책 → 각 데이터 플랫폼의 네이티브 접근 제어(Snowflake Row Access Policy, Databricks Table ACL)로 자동 변환 및 적용
- **단일 정책 → 멀티 플랫폼**: Snowflake, Databricks, Redshift, Azure Synapse 등에 동일 정책 일관 적용
- **Just-in-Time 접근**: 임시 데이터 접근 요청·승인 워크플로 자동화

### 동적 데이터 마스킹 (Dynamic Data Masking)
- **컬럼 수준 동적 마스킹**: 사용자의 역할·목적에 따라 동일 쿼리 결과에서 다른 마스킹 적용 (분석가는 일부 마스킹, 데이터 엔지니어는 전체 노출 등)
- **k-익명성 마스킹**: 재식별 위험 높은 데이터 결합 시 자동 k-익명성 처리
- **조건부 마스킹**: 특정 목적(연구, 마케팅)에 동의한 경우에만 원본 노출

### AI 거버넌스 (2025 신기능)
- **Immuta AI**: 거버넌스 팀의 접근 요청 처리·정책 생성을 AI가 자동화. 지수적 AI 시대의 데이터 요청 폭증 대응
- **Immuta Copilot**: 자연어로 접근 정책 생성·수정 ("마케팅 팀은 이름·전화번호를 마스킹하고 이메일만 볼 수 있게 해줘")
- **AI 거버넌스 보고서**: AI 시스템·에이전트의 데이터 접근 패턴 감사 로그 가시화

### 데이터 마켓플레이스 통합
- **Immuta Data Marketplace**: 내부 데이터 사용자가 접근 가능한 데이터셋 검색·요청. 정책 기반 자동 승인
- **Data Products**: 분류·보호 정책이 적용된 데이터 제품 단위로 공유

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 매핑 방식 |
|---|---|
| F-4 AI 데이터 보안 | 데이터 플랫폼 내 정책 기반 접근 통제·동적 마스킹 |
| 접근 권한 최소화 | ABAC 정책으로 역할별 필요 데이터만 접근 |
| AI 학습 데이터 거버넌스 | 학습 데이터 접근 목적·동의 기반 정책 자동화 |
| 데이터 거버넌스 | 단일 정책 멀티플랫폼 일관 적용 |
| 컴플라이언스 | GDPR, CCPA, HIPAA 정책 템플릿 내장 |

---

## 강점

- **플랫폼 네이티브 통합**: Snowflake, Databricks에 가장 깊이 통합된 데이터 보안 플랫폼. 별도 게이트웨이 없이 플랫폼 내에서 정책 실행
- **정책 중앙화**: 수백 개 테이블·컬럼에 대한 보호 정책을 ABAC 규칙 몇 개로 관리. 정책 폭발(Policy Explosion) 방지
- **AI Copilot**: 자연어 정책 생성으로 비기술 거버넌스 담당자도 정책 관리 가능
- **Just-in-Time 접근**: AI 에이전트·분석가의 임시 데이터 접근을 안전하게 승인·만료 관리

---

## 약점·주의점

- **데이터 탐지 기능 제한**: BigID, Securiti 수준의 전수 PII 탐지·분류 기능은 약함 → 외부 분류 도구와 연동 권장
- **Snowflake/Databricks 의존**: 지원 데이터 플랫폼이 클라우드 데이터 웨어하우스 중심. 온프레미스 Oracle/SQL Server 지원은 상대적으로 제한
- **비용**: 사용자 수·데이터 소스 수 기반 구독. 대규모 조직에서 상당한 비용
- **한국어 UI/지원**: 한국 고객 전용 로컬 지원 인프라 확인 필요

---

## 가격 모델

| 모델 | 내용 |
|---|---|
| SaaS 구독 | Snowflake/Databricks 사용자 수 또는 데이터 소스 수 기반 연간 구독 |
| 셀프 관리 배포 | VPC 내 배포; 별도 인프라 비용 추가 |
| 모듈 추가 | Data Marketplace, AI 거버넌스 모듈 별도 추가 |

---

## 연동 생태계

- **데이터 플랫폼 (핵심)**: Snowflake (Native App), Databricks (Unity Catalog), Amazon Redshift, Azure Synapse Analytics
- **데이터 카탈로그**: Alation, Collibra, Atlan (분류 레이블 연동)
- **데이터 탐지**: BigID, Securiti (PII 분류 결과 → Immuta 정책 자동 생성)
- **ITSM/워크플로**: ServiceNow, Jira (접근 요청 승인 워크플로)
- **SIEM**: Splunk, Microsoft Sentinel (감사 로그 내보내기)
- **AI/ML**: Databricks ML, Snowpark ML (학습 데이터 접근 정책 적용)

---

## 출처

- [Immuta AI 및 Copilot 출시 (2025.03)](https://www.prnewswire.com/news-releases/immuta-unveils-immuta-ai-and-copilot-to-automate-and-scale-cross-platform-data-sharing-and-access-provisioning-302389880.html)
- [Immuta AI 데이터 거버넌스 강화 (Help Net Security)](https://www.helpnetsecurity.com/2025/03/04/immuta-ai/)
- [Immuta 2025 데이터 보안 현황 보고서](https://www.prnewswire.com/news-releases/immutas-2025-state-of-data-security-report-highlights-the-consequences-of-a-broken-data-provisioning-system-302368778.html)
- [Immuta AI 보안·거버넌스 보고서](https://www.immuta.com/blog/the-ai-security-governance-report/)
- [Immuta Reviews 2026 (SelectHub)](https://www.selecthub.com/p/data-governance-tools/immuta/)
