# Upstage Document Parse

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Upstage AI (한국, 서울) |
| 라이선스 | 상용 SaaS API |
| 배포 형태 | Cloud API (REST), AWS 마켓플레이스, 온프레미스 가능(문의) |
| 최신 동향 | Document Parse Enhanced 출시(2025.12.17) — 복잡 표·차트·이미지·체크박스 심층 이해; LangChain 공식 통합; 비동기 처리(최대 1,000페이지) 지원 |

---

## 한 줄 포지셔닝

> **한국어·CJK + HWP 문서에 최강, LLM이 바로 읽을 수 있는 HTML/Markdown으로 변환하는 한국산 Document Parse API**

---

## 주요 기능

### 텍스트 인식 (OCR + PDF 파싱)
- 디지털 PDF(native) 및 스캔 이미지 모두 처리
- **영어·한국어·일본어·중국어(CJK) 특화** 고정확도 인식
- HWP(한글 워드프로세서) 포맷 지원 — 경쟁사 대부분 미지원

### 레이아웃 요소 감지 (Layout Element Detection, LED)
- 단락, 그림, 표, 캡션, 제목, 머리글/바닥글, 목록 등 감지
- **인간 독서 순서(reading order)** 재정렬 — 다단 레이아웃·단 혼재 문서에서 강점

### 표 구조 인식 (Table Structure Recognition, TSR)
- 복잡 표(병합 셀, 숨겨진 그리드라인)를 **HTML로 변환**
- LLM이 표 데이터를 바로 이해할 수 있는 구조화 출력

### Document Parse Enhanced (2025.12 출시)
- 차트·이미지 심층 이해 (단순 OCR 초월)
- 체크박스 상태 인식 (폼·검사표 자동화)
- 복잡 PDF 워크플로 대상 신뢰도 높은 문서 처리

### 입력 형식
- PDF, 이미지(PNG/JPG/TIFF/BMP/WEBP), DOCX, PPTX, XLSX, **HWP**
- 동기 처리(소형 문서) + 비동기 처리(최대 1,000페이지)

### 출력 형식
- **HTML** (표·레이아웃 구조 보존)
- **Markdown** (LLM/RAG 파이프라인 직접 투입)
- JSON (좌표·신뢰도 포함)

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 관련도 | 비고 |
|---|:---:|---|
| B-1 비정형 문서 파싱/전처리 | ★★★ | 핵심 기능, LLM용 HTML/MD 변환 |
| F-3 종이·수기 OCR 디지털화 | ★★☆ | 스캔 문서 OCR, 수기 인식 제한 |
| 데이터 파이프라인 연동 | ★★☆ | LangChain·LlamaIndex 공식 커넥터 |
| 벡터 임베딩/RAG | ★★☆ | Solar LLM과 Solar Embedding 연계 |

---

## 강점

- **한국어 1위**: 한국어·HWP 지원에서 글로벌 경쟁사 대비 압도적 우위
- **LLM 친화 출력**: HTML/Markdown 직접 출력 — 추가 후처리 최소화
- **CJK 복합 문서**: 한·영·일·중 혼재 문서 처리
- **체크박스 인식**: 검사표·폼 문서 자동화에 활용 가능
- **간단한 API**: REST API로 몇 줄 코드로 통합, LangChain 공식 지원

---

## 약점·주의점

- **수기 인식**: 고도의 수기체(손글씨)에서는 NAVER CLOVA OCR 또는 Azure Document Intelligence 대비 제한
- **온프레미스**: 완전 온프레미스 배포는 별도 문의 필요, 표준 제공 아님
- **청킹 미내장**: 청킹 전략은 사용자가 직접 구현 (Unstructured.io 대비)
- **가격 투명성**: 상세 공개 가격 체계 없음, 사용량 기반 문의
- **도면 전문 처리**: 공학 도면(P&ID) 심볼 해석은 전문 솔루션 필요

---

## 가격 모델

| 구분 | 내용 |
|---|---|
| 기본 플랜 | 사용량 기반 과금(페이지 단위), 무료 크레딧 제공 |
| API 콘솔 | console.upstage.ai에서 직접 가입·사용 가능 |
| AWS 마켓플레이스 | AWS 결제 통합 가능 |
| 엔터프라이즈 | 볼륨 할인·SLA·온프레미스 별도 협의 |

---

## 연동 생태계

```
LangChain: UpstageDocumentParseLoader (langchain-upstage 패키지)
LlamaIndex: UpstageDocumentParseReader
API: REST API (Python 예제 공식 제공)
연계 모델: Upstage Solar LLM, Solar Embedding
AWS: AWS Marketplace 등록
```

---

## 최신 동향 (2025~2026)

- **2025.12.17**: Document Parse Enhanced 출시 — 차트·이미지·체크박스 심층 이해, 복잡 워크플로 신뢰성 강화
- **지속**: LangChain 공식 통합(UpstageDocumentParseParser), LlamaIndex 파서 통합 유지
- **지속**: 비동기 처리(최대 1,000페이지) 지원으로 대용량 배치 가능
- **Upstage Solar 생태계**: Document Parse + Solar LLM + Solar Embedding을 함께 사용하는 한국어 RAG 풀스택 가능

---

## 출처

- https://www.upstage.ai/products/document-parse
- https://www.upstage.ai/blog/en/document-parse-enhanced
- https://www.upstage.ai/blog/en/let-llms-read-your-documents-with-speed-and-accuracy
- https://console.upstage.ai/docs/capabilities/document-digitization/document-parsing
- https://python.langchain.com/api_reference/upstage/document_parse_parsers/langchain_upstage.document_parse_parsers.UpstageDocumentParseParser.html
- https://aws.amazon.com/marketplace/pp/prodview-lv5bnpdco7xoq
- https://www.upstage.ai/blog/ko/introduce-upstage-document-parse
