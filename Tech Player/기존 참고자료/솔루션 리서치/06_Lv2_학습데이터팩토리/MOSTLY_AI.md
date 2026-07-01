# MOSTLY AI

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | MOSTLY AI (오스트리아·미국, Syntho 인수로 모회사 변경) |
| 라이선스 | 상용 SaaS + 오픈소스 SDK (mostlyai Python 패키지) |
| 배포 형태 | SaaS 클라우드, 온프레미스, 오픈소스 SDK |
| 최신 동향 | 오픈소스 Synthetic Data SDK 공개(2025); TabularARGN 아키텍처 기반 차등 프라이버시 내장; 100배 빠른 학습; DHS(미국 국토부) 계약($196,800) 체결; Syntho 인수 이후 "MOSTLY AI powered by Syntho" 브랜딩 |

---

## 한 줄 포지셔닝

> **글로벌 선도 정형 합성 데이터 플랫폼 — TabularARGN 차등 프라이버시·100배 빠른 학습·오픈소스 SDK로 엔터프라이즈 데이터 접근성 민주화**

---

## 주요 기능

### 핵심 모델: TabularARGN
- **TabularARGN (Tabular Autoregressive Generative Network)**: MOSTLY AI 독자 개발 모델
- 기존 CTGAN 대비 **100배 빠른 학습** 속도
- 고충실도(High-Fidelity) 합성 — 통계적 패턴, 상관관계, 분포 보존
- 복잡한 정형·텍스트 혼합 데이터셋 지원

### 차등 프라이버시 (Differential Privacy)
- **수학적 차등 프라이버시 내장**: ε(엡실론) 제어 가능
- 개인 노출 없는 데이터 공유 보장
- 프라이버시 보호 수준 정량 평가 리포트

### 합성 데이터 유형
- 정형 테이블 (단일·다중)
- 시계열 데이터
- 텍스트 포함 혼합 데이터셋

### 오픈소스 SDK
- **mostlyai** Python 패키지 (GitHub: mostly-ai/mostlyai)
- 차등 프라이버시, 공정성 인식 데이터 생성(Fairness-aware), 자동 품질 보증 내장
- 표준화된 프라이버시·충실도 리포트 자동 생성

### 품질 보증 (QA)
- 합성 데이터 vs 실 데이터: 통계 유사도, 상관관계, 분포 비교
- 프라이버시 공격 시뮬레이션 (멤버십 추론, 속성 재식별)
- 공정성 지표 평가 (Fairness Metrics)

### MOSTLY AI Platform (SaaS/온프레미스)
- No-code UI로 비기술 사용자도 합성 데이터 생성 가능
- 프로젝트 관리, 팀 협업, 버전 관리

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 관련도 | 비고 |
|---|:---:|---|
| E-2 합성 데이터 | ★★★ | 핵심 기능, 글로벌 1위 정형 합성 |
| 데이터 프라이버시·보안 | ★★★ | 차등 프라이버시 최강급 |
| 데이터 품질 | ★★★ | 자동 품질 보증 리포트 |
| 데이터 접근성·민주화 | ★★★ | No-code UI + OSS SDK |
| GDPR/HIPAA 컴플라이언스 | ★★★ | DHS 계약, 프라이버시 보장 |

---

## 강점

- **TabularARGN**: 학습 속도 100배 향상 — 빠른 실험 사이클
- **차등 프라이버시 최강급**: 수학적 보장, 정량 평가 — 금융·의료·공공 규정 준수
- **오픈소스 SDK**: pip install mostlyai 설치 → Python 워크플로 직접 통합
- **No-code UI**: 데이터 과학자뿐 아니라 비즈니스 분석가도 사용 가능
- **DHS 계약**: 미국 국토부 프라이버시 강화 기술 프로젝트 — 신뢰성 인증
- **공정성 인식**: 편향 없는 AI 학습 데이터 생성 지원

---

## 약점·주의점

- **순수 텍스트 합성 제한**: 텍스트 포함 데이터 일부 지원하나 Gretel 수준의 전용 텍스트 합성은 아님
- **가격**: 엔터프라이즈 플랜은 고가 — 소규모 팀은 OSS SDK 활용 권장
- **Syntho 인수 후 변화**: 브랜딩·제품 로드맵 통합 과정에서 일부 불확실성
- **완전 관계형 다중 테이블**: SDV HMA 수준의 복잡 다중 테이블 스키마 처리 제한

---

## 가격 모델

| 플랜 | 가격 | 주요 내용 |
|---|---|---|
| OSS SDK | 무료 (오픈소스) | mostlyai Python 패키지, 기본 합성 |
| SaaS (Free) | 무료 (제한) | 소규모 데이터셋 테스트 |
| SaaS (Pro) | 월 구독 (문의) | 팀 사용, 대용량 |
| Enterprise | 연간 계약 (문의) | 온프레미스, SLA, 전용 지원 |

---

## 연동 생태계

```
Python: pip install mostlyai (오픈소스 SDK)
Pandas: DataFrame 직접 입력·출력
API: REST API (플랫폼)
클라우드: AWS, Azure (엔터프라이즈 배포)
컴플라이언스: GDPR, HIPAA, CCPA 지원
데이터 포맷: CSV, Parquet, 직접 DB 커넥터
```

---

## 최신 동향 (2025~2026)

- **2025.02**: 오픈소스 Synthetic Data SDK 출시 발표 (tech.eu 보도)
- **2025**: **mostlyai** GitHub 공개 — 차등 프라이버시·공정성·품질 보증 내장 SDK
- **2025**: 미국 DHS(국토부) $196,800 계약 — 프라이버시 강화 합성 데이터 기술 개발
- **2025**: TabularARGN 아키텍처 업데이트 — 100배 학습 속도, 고급 샘플링
- **2026**: Syntho 인수 이후 "MOSTLY AI powered by Syntho" 재브랜딩
- **지속**: 금융·의료·보험 업계 엔터프라이즈 고객 확대

---

## 제조업 활용 예시

- **품질 DB 안전 공유**: 생산 품질 DB(MES, QMS)를 개발·외부 협업 환경에 GDPR 준수 형태로 안전하게 공유
- **불균형 불량 데이터 증강**: 정상 데이터 99% vs 불량 1% 불균형 → MOSTLY AI로 불량 클래스 합성 증강
- **AI 모델 편향 방지**: 특정 라인·시프트 데이터 과대 대표 문제를 공정성 인식 합성으로 균형 조정

---

## 출처

- https://mostly.ai/
- https://github.com/mostly-ai/mostlyai
- https://tech.eu/2025/02/03/the-future-of-ai-innovation-starts-with-synthetic-data-and-an-open-source-sdk/
- https://www.hpcwire.com/bigdatawire/this-just-in/mostly-ai-unveils-open-source-toolkit-for-synthetic-data-generation/
- https://arxiv.org/html/2508.00718v1
- https://www.g2.com/products/mostly-ai-synthetic-data-platform/reviews
- https://averroes.ai/blog/synthetic-data-generation-tools
