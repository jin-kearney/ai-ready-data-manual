# Unstructured.io

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Unstructured Inc. (미국) |
| 라이선스 | Apache 2.0 (OSS 코어) / 상용 엔터프라이즈 플랜 |
| 배포 형태 | 오픈소스 라이브러리, Serverless API, Azure/AWS 마켓플레이스, 온프레미스 |
| 최신 동향 | 2025년 Fast Company 가장 혁신적인 기업 선정; v0.18 시리즈(2025 여름) PDF 파티셔닝 가속화 및 청킹 API 개편; MotherDuck 통합(2025.02) |

---

## 한 줄 포지셔닝

> **비정형 문서를 RAG·LLM용 구조화 요소로 변환하는 Document ETL 플랫폼 — 오픈소스 생태계 최다 통합**

---

## 주요 기능

### 파일 파싱 및 파티셔닝
- 지원 형식: PDF, HTML, DOCX, PPTX, XLSX, EML, MSG, Markdown, 이미지(PNG/JPG/TIFF) 등 30종 이상
- 문서를 논리적 요소(Title, NarrativeText, Table, ListItem, Image, PageBreak, Header, Footer)로 분리
- 고해상도 레이아웃 ML + 생성형 정제(generative refinement)로 정확도 향상
- **표 추출 Table Score 0.844** (셀 콘텐츠 0.795, 셀 공간 정확도 0.786) — 경쟁사 대비 최상위

### RAG 최적화 청킹
- 전략: by-page, by-similarity, semantic chunking 선택 가능
- 청킹 후 임베딩 생성(선택 가능한 모델 지정)
- 인텔리전트 라우팅: 페이지별 최적 처리 전략 자동 선택

### 문서 농축(Enrichment)
- Named Entity Recognition(NER): 인물·기관·위치·날짜 자동 태깅
- 이미지 OCR 내장: 이미지 내 텍스트 추출
- 환각 제어: Tokens Added Rate 0.027 (경쟁사 최저)

### 파이프라인 통합
- 커넥터: S3, Azure Blob, GCS, SharePoint, Salesforce, Slack, GitHub, Confluence 등 50+ 소스
- 목적지: Pinecone, Weaviate, Qdrant, Elasticsearch, MotherDuck, Databricks 등

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 관련도 | 비고 |
|---|:---:|---|
| B-1 비정형 문서 파싱/전처리 | ★★★ | 핵심 기능 |
| F-3 종이·수기 OCR 디지털화 | ★★☆ | 이미지 OCR 내장, 수기 인식 제한적 |
| 데이터 파이프라인/ETL | ★★★ | Document ETL 포지셔닝 |
| 벡터 임베딩/RAG | ★★★ | 청킹·임베딩 내장 |
| 메타데이터 관리 | ★★☆ | NER 태깅, 요소별 좌표 메타데이터 |

---

## 강점

- **오픈소스 Apache 2.0**: 내부 커스터마이징 및 온프레미스 배포 자유
- **최고 수준 표 추출**: Table Score 0.844로 경쟁사 최상위
- **RAG 파이프라인 풀스택**: 파싱→청킹→임베딩→벡터스토어 적재까지 단일 플랫폼
- **생태계 폭**: LangChain, LlamaIndex, Haystack, 50+ 데이터 소스·목적지 커넥터
- **환각 억제**: Tokens Added Rate 최저 수준으로 LLM 품질 보호

---

## 약점·주의점

- **한국어 성능**: 영어 대비 한국어·CJK 처리 품질 낮음 (Upstage·NAVER 대비 열세)
- **수기 인식**: 인쇄 문서에 강점, 복잡 수기체는 별도 OCR 엔진 필요
- **HWP 미지원**: 국내 공공·제조업 다수 사용 HWP 형식 처리 불가
- **도면 전문 해석**: P&ID·기계도면의 심볼·라인 의미 해석은 미지원
- **엔터프라이즈 비용**: 대용량 처리 시 서버리스 API 비용 증가

---

## 가격 모델

| 플랜 | 가격 | 주요 내용 |
|---|---|---|
| OSS (오픈소스) | 무료 | 자체 호스팅, API 없음 |
| Serverless API (Free) | 무료 | 제한된 페이지/월 |
| Serverless API (Pay-as-you-go) | 페이지 단위 과금 | 용량별 차등 |
| Enterprise | 연간 계약 (문의) | 무제한 처리, SLA, 전용 지원 |

---

## 연동 생태계

```
LangChain: UnstructuredLoader (langchain-community)
LlamaIndex: UnstructuredReader
Haystack: UnstructuredFileConverter
API: REST API (Python/TypeScript SDK 제공)
데이터 소스: S3, Azure Blob, GCS, SharePoint, Confluence, Slack, GitHub, Salesforce, OneDrive
벡터 스토어: Pinecone, Weaviate, Qdrant, Chroma, Elasticsearch, OpenSearch, MotherDuck
```

---

## 최신 동향 (2025~2026)

- **2025.02**: MotherDuck(DuckDB 클라우드)와 통합, 문서 → 데이터 웨어하우스 직접 적재 지원
- **2025 여름**: v0.18 시리즈 — PDF 파티셔닝 속도 대폭 개선, 청킹 API 재설계
- **2025**: Fast Company 가장 혁신적인 기업 선정
- **2025**: 표 추출·레이아웃 ML 정확도 벤치마크 업데이트 (경쟁사 대비 표 점수 1위)
- 인텔리전트 라우팅(페이지별 최적 전략 자동 선택) 기능 추가

---

## 출처

- https://unstructured.io/blog/unstructured-leads-in-document-parsing-quality-benchmarks-tell-the-full-story
- https://unstructured.io/blog/simpler-faster-and-more-powerful-way-to-transform-documents-in-unstructured
- https://unstructured.io/blog/mastering-pdf-transformation-strategies-with-unstructured-part-2
- https://unstructured.io/problems-we-solve
- https://unstructured.io/blog/benchmarking-document-parsing-and-what-actually-matters
- https://neurlcreators.substack.com/p/tuesday-tool-review-16-llm-ready
- https://intelligenttools.co/tools/unstructured
