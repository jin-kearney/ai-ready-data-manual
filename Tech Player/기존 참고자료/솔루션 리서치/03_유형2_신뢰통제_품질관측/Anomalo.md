# Anomalo — AI 기반 데이터 품질 + 비정형 Observability 플랫폼

> 작성일: 2026-06-10 | 카테고리: 유형② 신뢰 통제

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Anomalo (샌프란시스코, 2018년 설립) |
| 라이선스 | 상용 SaaS |
| 배포 형태 | SaaS / VPC(Virtual Private Cloud) 배포 |
| 최신 동향 | 2025 Gartner Peer Insights "Voice of the Customer" Strong Performer (추천율 95%); 2024~2026: 비정형 데이터 품질(LLM Readiness) 기능 확장; Azure Marketplace 등재(2025); AI 에이전트 First Responder·Data Insights Agent 출시 |

---

## 한 줄 포지셔닝

**"룰 없는 비지도 ML로 구조화 데이터 이상을 탐지하고, LLM 학습용 비정형 문서 품질까지 단일 플랫폼에서 커버하는 유일한 솔루션"**

---

## 주요 기능

### 1. 비지도 머신러닝 자동 이상탐지
- 사전 정의 룰·임계값·검증 체크 없이 테이블 내용을 자동 학습
- 데이터 볼륨, 분포, 결측값, 포맷 이탈 등 다차원 이상 자동 감지
- 6대 데이터 품질 기둥(Six Pillars) 프레임워크: 완전성·정확성·일관성·유효성·유일성·시의성

### 2. 비정형 데이터 품질 (2024 신기능)
- PDF·계약서·고객 지원 로그·UGC 등 비정형 문서에 LLM 적용
- 자동 탐지: 결측 메타데이터, 파일 손상, PII 노출
- LLM 학습 데이터 품질 점수(LLM Readiness Score) 제공 — AI 파이프라인 진입 전 필터링

### 3. AI 에이전트 자동화 (2025)
- **First Responder Agent**: 알림 수신 → 영향도·긴급도 자동 평가 → 런북 기반 조치
- **Data Insights Agent**: 자율적으로 데이터 변화를 탐지하고 분석가 수준의 리포트 자동 생성
- 아직 인간 의사결정 보조 수준, 자율 실행은 제한적

### 4. 구조화 + 비정형 통합 관제
- 단일 플랫폼에서 Snowflake·Databricks 테이블과 S3/GCS 비정형 문서 동시 모니터링
- 기업 AI 파이프라인에서 데이터 입력 품질을 엔드투엔드 보장

### 5. 스마트 알림 및 Slack/Jira 연동
- 이상 심각도·영향 범위 기반 알림 우선순위화
- 기존 인시던트 관리 워크플로우에 자연스럽게 삽입

---

## AI-Ready Data 주제 매핑

| 주제 코드 | 주제명 | 지원 수준 |
|---|---|---|
| C-1 | 데이터 Observability | ○ ML 이상탐지 핵심 |
| C-2 | 품질관리 | ○ 6대 품질 기둥 + 비정형 |
| C-3 | 데이터 Lineage | △ 제한적 |

---

## 강점

- **완전 무설정 ML**: 룰 작성 없이 즉시 이상탐지 시작 — 빠른 배포
- **비정형 데이터 품질 유일성**: 구조화+비정형을 동시 커버하는 현존 유일 솔루션
- **LLM 파이프라인 준비도**: AI 학습 데이터 품질 스코어링으로 AI 신뢰 확보
- **높은 고객 만족도**: Gartner 95% 추천율, Snowflake/Databricks/BigQuery 레퍼런스 다수
- **Azure Marketplace 등재**: Microsoft 에코시스템 고객 접근성 향상

---

## 약점 및 주의점

- **비투명 가격**: 공개 가격표 없음, 테이블 수 기반 견적 — 예산 계획 어려움
- **데이터 계약 부재**: SodaCL·GX 수준의 계약 명세·집행 기능 없음
- **Lineage 약함**: 자체 컬럼 수준 Lineage 없음
- **온프레미스 지원 제한**: 주로 SaaS/VPC — 완전 온프레미스는 지원 제한
- **신생 기업 리스크**: 2018년 설립, 대형 벤더 대비 장기 안정성 불확실성

---

## 가격 모델

- **과금 기준**: 모니터링 테이블 수 기반
- **Free 티어**: 제한적 무료 사용 가능
- **유료 플랜**: 완전 커스텀 견적 (비공개)
- **비고**: G2 등 리뷰에서 "비투명 가격 구조" 지적 다수

---

## 연동 생태계

| 카테고리 | 연동 도구 |
|---|---|
| 데이터 웨어하우스 | Snowflake, Databricks, BigQuery, Redshift |
| 비정형 스토리지 | S3, GCS, Azure Blob |
| 마켓플레이스 | AWS Marketplace, Azure Marketplace |
| 알림 | Slack, PagerDuty, Jira |
| AI/LLM | LLM 품질 스코어링, AI 에이전트 프레임워크 |
| API | REST API |

---

## 출처

- https://www.anomalo.com/
- https://www.anomalo.com/product-overview/
- https://www.anomalo.com/blog/monte-carlo-vs-anomalo/
- https://www.anomalo.com/blog/anomalos-ai-powered-data-quality-platform-now-available-in-the-azure-marketplace/
- https://www.efficientlyconnected.com/trustworthy-data-for-ai-starts-with-six-non-negotiables/
- https://www.g2.com/products/anomalo/reviews
- https://www.siffletdata.com/blog/anomalo-review
