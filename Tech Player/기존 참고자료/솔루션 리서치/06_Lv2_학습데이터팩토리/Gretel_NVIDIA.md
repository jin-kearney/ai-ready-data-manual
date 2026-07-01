# Gretel (NVIDIA 인수)

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Gretel Inc. → **NVIDIA 인수 완료 (2025년 3월)** |
| 라이선스 | 상용 (NVIDIA 클라우드 서비스로 통합) |
| 배포 형태 | NVIDIA 클라우드 API·서비스 (통합 진행 중), 기존 Gretel API 유지 |
| 최신 동향 | NVIDIA가 $320M+ 규모의 9자리 금액으로 2025.03 인수; 직원 ~80명 NVIDIA 편입; NVIDIA 생성형 AI 개발자 서비스 스위트에 통합 예정; 개인정보보호 합성 데이터 + NVIDIA GPU 생태계 결합 |

---

## 한 줄 포지셔닝

> **NVIDIA가 인수한 합성 데이터 플랫폼 — 정형+텍스트 합성과 차등 프라이버시를 NVIDIA 클라우드 AI 생태계에 통합**

---

## NVIDIA 인수 배경 및 전략적 의미

| 항목 | 내용 |
|---|---|
| 인수 발표 | 2025년 3월 19일 (Wired 보도) |
| 인수 금액 | $320M+ (Gretel 최근 기업 가치 이상의 9자리 금액) |
| 인수 목적 | NVIDIA AI 생태계에 합성 데이터 툴 추가 — 실 데이터 부족·프라이버시 문제 해결 |
| 통합 방향 | NVIDIA의 클라우드 기반 생성형 AI 개발자 서비스 스위트로 통합 |

합성 데이터는 실세계 데이터 부족·수집 비용·프라이버시 문제를 해결하며, NVIDIA의 AI 학습 인프라(GPU·NIM)와 결합 시 시너지가 크다.

---

## 주요 기능

### 정형(테이블) 합성 데이터
- CTGAN·ACTGAN: 범주형·수치형 테이블 데이터 합성
- 복잡 스키마·관계형 데이터 지원
- 단일 테이블 및 다중 테이블 (SDV 대비 제한적)

### 텍스트 합성 데이터 (Gretel 차별점)
- **GPT 기반 텍스트 합성**: 실 텍스트 데이터 패턴을 학습하여 새 합성 텍스트 생성
- NLP 학습 데이터 보강
- 조건부 텍스트 생성 (도메인 특화)

### 차등 프라이버시 (Differential Privacy)
- 수학적 프라이버시 보장
- ε(엡실론) 파라미터 설정 — 프라이버시-유틸리티 트레이드오프 제어
- GDPR·HIPAA·CCPA 컴플라이언스 지원

### 시계열 데이터
- 시계열 패턴 학습 및 합성

### 데이터 품질 평가
- 합성 데이터 유사도 리포트
- 프라이버시 공격 시뮬레이션 (멤버십 추론, 속성 추론)

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 관련도 | 비고 |
|---|:---:|---|
| E-2 합성 데이터 | ★★★ | 핵심 기능, 정형+텍스트 합성 |
| 데이터 프라이버시·보안 | ★★★ | 차등 프라이버시(DP), 규정 준수 |
| 텍스트 데이터 증강 | ★★★ | NLP 학습 데이터 합성 (SDV 미지원) |
| 학습 데이터 파이프라인 | ★★★ | NVIDIA NIM·DGX 생태계 연계 |

---

## 강점

- **텍스트 합성**: 경쟁사(SDV, MOSTLY AI) 대부분이 정형 데이터 전용인 반면, Gretel은 텍스트 합성 지원
- **차등 프라이버시**: 수학적 DP 보장 — 엄격한 규정 준수 요구사항 충족
- **NVIDIA 생태계**: NVIDIA GPU·NIM·DGX·Clara 등과의 통합으로 AI 학습 파이프라인 가속화
- **클라우드 API**: REST API로 간편 통합

---

## 약점·주의점

- **NVIDIA 인수 후 전략 불확실성**: 서비스 통합 방향·가격 정책이 2026년 현재도 확정되지 않은 부분 존재
- **오픈소스 후퇴 우려**: NVIDIA 편입 후 오픈소스 접근성 축소 가능성
- **다중 테이블 관계형 합성**: SDV의 HMA 수준의 관계형 합성은 제한적
- **가격 상승 가능성**: NVIDIA 서비스 패키지 통합 시 단독 접근 비용 증가 우려
- **온프레미스 불명확**: NVIDIA 통합 이후 온프레미스 배포 옵션 명확화 필요

---

## 가격 모델

| 구분 | 내용 |
|---|---|
| 기존 Gretel API | 데이터 행 기반 종량제 (인수 이후 변동 가능) |
| NVIDIA 통합 이후 | NVIDIA AI Enterprise 라이선스 번들 예상 (문의) |
| 무료 티어 | 소규모 테스트 용량 제공 (변동 가능) |

> **주의**: NVIDIA 인수 후 정확한 가격 정책은 NVIDIA 영업 문의 필요

---

## 연동 생태계

```
NVIDIA: NIM API, DGX 클라우드, NVIDIA AI Enterprise 생태계 (통합 진행)
Python: gretel-client 패키지
API: REST API
데이터 포맷: CSV, Parquet, Pandas DataFrame
컴플라이언스: GDPR, HIPAA, CCPA
```

---

## 최신 동향 (2025~2026)

- **2025.03.19**: NVIDIA가 $320M+ 규모로 Gretel 인수 발표 (Wired·TechCrunch 보도)
- **2025.03~**: Gretel 직원 ~80명 NVIDIA 조직에 편입
- **2025~2026**: NVIDIA의 클라우드 기반 생성형 AI 개발자 서비스 스위트에 합성 데이터 기능 통합 예정
- **2026 현재**: 기존 Gretel API 서비스는 유지 중이나 장기 통합 로드맵은 NVIDIA 정책에 따라 변동
- **전략적 의의**: NVIDIA의 GPU 학습 인프라 + 합성 데이터 = AI 학습 데이터 병목 해소

---

## 출처

- https://finance.yahoo.com/news/report-nvidia-acquires-synthetic-data-184229935.html
- https://techcrunch.com/2025/03/19/nvidia-reportedly-acquires-synthetic-data-startup-gretel/
- https://siliconangle.com/2025/03/19/nvidia-reportedly-acquires-gretel-320m-strengthen-ai-training-tools/
- https://opentools.ai/news/nvidia-leaps-into-synthetic-data-with-gretel-acquisition
- https://theaiinsider.tech/2025/03/23/gretel-acquired-by-nvidia-to-power-synthetic-data-advancements-in-generative-ai-according-to-sources/
- https://softices.capital/news/nvidia-acquires-synthetic-data-startup-gretel
