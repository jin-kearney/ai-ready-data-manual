# Google Document AI

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Google Cloud |
| 라이선스 | 상용 (GCP 종량제·엔터프라이즈) |
| 배포 형태 | GCP 클라우드 API (완전 관리형, 온프레미스 미지원) |
| 최신 동향 | Layout Parser v1.6(Gemini 3 Flash 기반, 2026.01 Preview); Custom Extractor v1.6(Gemini 3 Flash); Layout Parser Pro(Gemini 3 Pro); 레거시 프로세서 2026.06.30 종료 |

---

## 한 줄 포지셔닝

> **Gemini 3 LLM 기반 레이아웃 파서로 문서 구조를 "이해"하는 차세대 Document AI — Google Cloud 생태계 통합**

---

## 주요 기능

### OCR 엔진
- Enterprise OCR v2.1 (2024.08 GA): 고정확도 텍스트 인식
- OCR v2.1.1 (2025.01 RC): 아시아·유럽 지역 추가 지원
- 단어 수준 폰트 속성 인식(폰트 종류, 스타일, 수기 여부, 굵기, 색상)

### 레이아웃 파서 (Gemini 기반)
- **Layout Parser v1.5** (GA): 기존 안정 버전
- **Layout Parser v1.6** (2026.01 Preview): **Gemini 3 Flash** LLM 탑재 — 레이아웃 이해도 대폭 향상
- **Layout Parser v1.6 Pro** (2025.12 Preview): **Gemini 3 Pro** — 최고 정확도
- 처리 용량: Provisioned Tier 120페이지/분(Flash), 30페이지/분(Pro)

### 커스텀 모델
- **Custom Classifier v1.5** (GA): 문서 종류 자동 분류
- **Custom Extractor v1.6** (2026.01 Preview): Gemini 3 Flash 기반 학습 가능한 필드 추출기
- 훈련 데이터 최소화 — Few-shot 학습 지원

### 사전 구축 프로세서 (Specialized Parsers)
- Invoice Parser, Expense Parser, Contract Parser, Payslip Parser
- Identity Document Parser, Procurement Parser, Form Parser
- Lending Document Parser

### Human-in-the-Loop (HITL)
- Document AI Workbench: 인간 검토·교정 워크플로 내장
- 저신뢰도 결과 자동 라우팅 및 교정 데이터로 모델 재학습

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 관련도 | 비고 |
|---|:---:|---|
| B-1 비정형 문서 파싱/전처리 | ★★★ | Gemini 기반 레이아웃 이해 |
| F-3 종이·수기 OCR 디지털화 | ★★☆ | 수기 인식 가능, 한국어 제한 |
| Human-in-the-loop | ★★★ | Document AI Workbench HITL 내장 |
| 데이터 파이프라인 | ★★★ | GCS, BigQuery, Pub/Sub, Dataflow 연계 |
| 벡터 임베딩/RAG | ★★☆ | Vertex AI Search와 통합 |

---

## 강점

- **Gemini LLM 통합**: 단순 OCR을 넘어 문서 "이해" — 구조적 맥락 파악, 시각 요소 해석
- **GCP 생태계 완전 통합**: GCS, BigQuery, Vertex AI, Pub/Sub, Dataflow
- **Gemini Vision**: 차트·그림·도면 시각적 이해 능력
- **HITL 내장**: Document AI Workbench로 인간-기계 협업 파이프라인
- **커스텀 확장성**: 자체 데이터로 추출기 학습 → 특수 문서 도메인 적응

---

## 약점·주의점

- **온프레미스 미지원**: GCP 클라우드 전용, 에어갭 환경 불가
- **한국어 특화 부족**: 한국어·HWP 처리에서 Upstage·NAVER 대비 열세
- **레거시 프로세서 종료**: 2026.06.30 기존 레거시 프로세서 종료 — 마이그레이션 필요
- **비용 예측성**: Gemini Pro 기반 처리는 단가가 높음
- **규정 준수**: GDPR·한국 클라우드 컴플라이언스 요구사항 사전 확인 필요
- **청킹 미내장**: RAG 파이프라인용 청킹은 별도 구현 필요

---

## 가격 모델

| 프로세서 | 가격 |
|---|---|
| Enterprise OCR | $1.50 / 1,000페이지 |
| Layout Parser (Flash 기반) | 별도 공시 (Preview 기간 변동 가능) |
| Form Parser | $1.50 / 1,000페이지 |
| Specialized Parsers | $10~30 / 1,000페이지 |
| Custom Processor Training | 훈련 시간 기준 |
| 무료 티어 | 300페이지/월 (기본 OCR) |

---

## 연동 생태계

```
GCP: GCS, BigQuery, Pub/Sub, Dataflow, Vertex AI, Looker
LangChain: DocAIParser
LlamaIndex: GoogleDocumentAI 커넥터
API: Python, Java, Node.js, Go SDK
Document AI Workbench: 인간 검토 UI
Vertex AI Search: 파싱 결과 → 엔터프라이즈 검색 직접 연계
```

---

## 최신 동향 (2025~2026)

- **2025.08**: Custom Classifier v1.5 GA
- **2025.12**: Layout Parser Pro v1.6 (Gemini 3 Pro 기반) Preview
- **2026.01**: Layout Parser v1.6 (Gemini 3 Flash) Preview; Custom Extractor v1.6 Preview
- **2026.06.30**: 레거시 프로세서 서비스 종료 — 신규 프로세서 마이그레이션 권고
- **처리 용량 확대**: Gemini 2.0 Flash 기반 120페이지/분 → 확장 계획
- **Google I/O 2026**: 멀티모달 문서 이해 기능 강화 발표

---

## 출처

- https://docs.cloud.google.com/document-ai/docs/release-notes
- https://cloud.google.com/document-ai
- https://docs.cloud.google.com/document-ai/docs/overview
- https://docs.cloud.google.com/document-ai/docs/enterprise-document-ocr
