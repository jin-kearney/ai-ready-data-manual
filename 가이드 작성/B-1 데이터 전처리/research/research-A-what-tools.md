# B-1 데이터 전처리 — 리서치 원자료 A: 도구·기법·구조화 방법

> 작성일: 2026-06-18  
> 관점: "AI(RAG·Agent)가 쓸 데이터를 준비·구조화하는 법" — AI 앱 구현법이 아님  
> 대상 독자: 두산 계열사 제조 현업

---

## 1. 문서 유형별 추출 난이도와 핵심 과제

### 1-1. PDF

PDF는 인쇄 레이아웃(PostScript) 기반이라 "논리적 구조(제목·단락·표)"가 파일에 없다. 텍스트 좌표는 있으나 단락 경계·읽기 순서(reading order)는 추론해야 한다.

**주요 난점:**
- **다단 레이아웃**: 2열 배치를 좌→우가 아닌 아래→아래로 읽는 파서가 많음. 단순 텍스트 추출 시 두 단의 내용이 뒤섞임.
- **표 구조 손실**: PDF 표는 선(line)과 좌표로만 표현. 병합셀·테두리 없는 표는 파서가 행/열 구조를 놓치고 단순 텍스트로 반환.
- **스캔 이미지 PDF**: 텍스트가 픽셀로만 존재. OCR 없이는 추출 불가.
- **수식·특수문자**: 유니코드 매핑 오류, 수식 인코딩 손실.
- **헤더/푸터 노이즈**: 쪽 번호·반복 헤더가 본문과 섞임.

출처: [Unstructured — How to Parse a PDF Part 1](https://unstructured.io/blog/how-to-parse-a-pdf-part-1)

### 1-2. PPT(PPTX)

- 슬라이드 제목, 본문 텍스트박스, 도형 내 텍스트, 표, 차트 주석이 별도 XML 객체로 존재.
- `python-pptx` 라이브러리로 슬라이드 계층(제목→본문→도형)을 순서대로 추출 가능.
- **난점**: 텍스트박스 위치(Z-order)에 따라 읽기 순서가 다름. 도형 안 텍스트·아트워크 내 텍스트는 별도 처리 필요. 차트 데이터는 내장 Excel 개체로 존재.

출처: [Slide2Text: Leveraging LLMs for PPT Processing (arxiv)](https://arxiv.org/pdf/2503.17710)  
라이브러리: [python-pptx 공식](https://python-pptx.readthedocs.io/)

### 1-3. Excel(XLSX)

- `openpyxl` 또는 `pandas`로 시트·셀 값 추출.
- **난점 1 — 병합셀(merged cells)**: 병합된 영역에서 값은 첫 번째 셀에만 저장, 나머지는 `None`. 병합 해제 후 값 전파(fill) 처리가 필요.
- **난점 2 — 시각적 의미**: 테두리·배경색·들여쓰기가 데이터 계층을 나타냄. 기계는 이를 자동 파악 불가.
- **난점 3 — 다중 시트**: 보고서는 요약 시트 + 상세 시트로 분리. 시트 간 연관관계를 수동으로 정의해야 함.
- **수식**: `openpyxl`은 수식 문자열(`=SUM(A1:A5)`)을 반환하고 계산값은 캐시된 값에서 읽어야 함.

출처:  
- [openpyxl: dealing with merged cells (GitHub Gist)](https://gist.github.com/tchen/01d1d61a985190ff6b71fc14c45f95c9)  
- [A Comprehensive Guide to OpenPyxl (Medium)](https://medium.com/@Bwhiz/a-comprehensive-guide-to-openpyxl-in-python-c882c482e7b1)  
- [Excel Data Extraction with AI (Lido)](https://www.lido.app/blog/excel-data-extraction)

### 1-4. 이미지 속 텍스트/표

- 스캔 이미지, 카메라 촬영 문서, PDF 내 이미지 페이지에는 OCR 필수.
- **OCR 난점**: 기울어진 문서, 저해상도, 손글씨, 표의 셀 경계 인식.
- 이미지 속 표는 선을 인식해 행/열 구조로 재구성해야 함(Table Structure Recognition, TSR).

---

## 2. 레이아웃 인식 파싱(Layout-Aware Parsing)과 단순 텍스트 추출의 차이

| 구분 | 단순 텍스트 추출 | 레이아웃 인식 파싱(Layout-Aware) |
|------|-----------------|--------------------------------|
| 방법 | 좌표 무시, 순서대로 텍스트 연결 | 페이지 레이아웃 분석 후 블록/요소 분류 |
| 출력 | 평문 텍스트 덩어리 | 제목·단락·표·이미지·목록으로 분류된 구조 |
| 표 | 텍스트로 분해(구조 손실) | 행/열 구조 보존(HTML 또는 Markdown 표) |
| 다단 | 열 혼합(오독) | 읽기 순서 올바르게 복원 |
| 좌표(Provenance) | 없음 | 바운딩박스(페이지·X·Y·W·H) 포함 |

레이아웃 인식 파싱의 핵심 기술:
- **레이아웃 감지 모델(Layout Detection Model)**: 딥러닝으로 페이지를 텍스트 블록·표·그림·수식 영역으로 분할.
- **읽기 순서 알고리즘(Reading Order Algorithm)**: 분할된 블록을 논리적 순서로 정렬.
- **표 구조 인식(Table Structure Recognition, TSR)**: Docling의 TableFormer 등.

출처:  
- [How to Build a Parsing Pipeline with Docling Parse (MarkTechPost)](https://www.marktechpost.com/2026/06/16/how-to-build-a-parsing-pipeline-with-docling-parse-for-layout-aware-document-intelligence/)  
- [Unstructured Hi-Res Strategy — How to Parse a PDF](https://unstructured.io/blog/how-to-parse-a-pdf-part-1)

---

## 3. 문서 파싱·전처리 도구/솔루션 맵

### 3-1. 오픈소스 / 파이썬 라이브러리

#### Unstructured
- **URL**: https://unstructured.io  
- **특징**: 다양한 포맷(PDF·DOCX·HTML·이미지·PPTX·XLSX 등)을 일관된 요소 목록으로 파싱. Hi-Res 전략은 레이아웃 감지 모델 사용.
- **잘하는 것**: 텍스트·단순 표의 정확한 추출. OCR. 다양한 포맷 통합.
- **입력**: PDF, DOCX, PPTX, HTML, 이미지 등 다수
- **출력**: JSON (요소별 타입·텍스트·메타데이터·바운딩박스 좌표)
- **표 처리**: HTML 형식으로 행/열 구조 보존
- **한계**: 복잡한 다중행 표에서 컬럼 이동(column shift) 오류. 속도가 세 도구 중 가장 느림(51~141초/페이지).
- **가격**: 오픈소스 라이브러리 무료 + 상용 클라우드 API(SaaS) 유료. 공식 문서 확인 필요.

출처: [Unstructured 공식 사이트](https://unstructured.io) · [Unstructured 벤치마크 블로그](https://unstructured.io/blog/unstructured-leads-in-document-parsing-quality-benchmarks-tell-the-full-story)

---

#### Docling (IBM)
- **URL**: https://github.com/docling-project/docling  
- **특징**: IBM 오픈소스. 레이아웃 분석 + **TableFormer**로 복잡한 표 구조 인식. 로컬 실행 가능(민감 데이터 처리 적합).
- **잘하는 것**: 복잡한 표 구조 보존(계층적 중첩·컬럼 순서). PDF·DOCX·PPTX·XLSX 등 다수 지원.
- **입력**: PDF, DOCX, PPTX, XLSX, HTML, 이미지, LaTeX 등
- **출력**: JSON(바운딩박스 좌표 포함), Markdown, HTML. `DoclingDocument` 통합 표현 형식.
- **표 정확도**: 벤치마크 97.9%(복잡한 표). 가장 우수.
- **속도**: 6.28초/페이지 (선형 증가).
- **한계**: 고밀도 수치 표에서 간혹 할루시네이션(값 오인). 가장 느린 처리 속도.
- **연동**: LangChain, LlamaIndex, CrewAI, Haystack 플러그인 지원.

출처: [Docling GitHub](https://github.com/docling-project/docling) · [Docling vs LlamaParse vs Unstructured 벤치마크 (Procycons)](https://procycons.com/en/blogs/pdf-data-extraction-benchmark/)

---

#### LlamaParse
- **URL**: https://docs.llamaindex.ai/en/stable/llama_cloud/llama_parse/  
- **특징**: LlamaIndex의 클라우드 파싱 서비스. 에이전트 기반 레이아웃 인식. LLM-ready 출력에 특화.
- **잘하는 것**: 복잡한 PDF 레이아웃 의미 구조 보존. 차트·수식·다중 중첩 표. 속도 일관성.
- **입력**: 주로 PDF (복잡한 재무·의료·보험 문서)
- **출력**: Markdown (구조·계층 보존), JSON
- **속도**: 약 6초/처리 (페이지 수 관계없이 일정). 가장 빠름.
- **한계**: 인터넷 연결 필수(클라우드 서비스). 복잡한 표/병합셀에서 컬럼 정렬 오류. 크레딧 기반 과금.
- **가격**: 유료 API. 무료 체험 제공. 상세 요금은 [공식 문서](https://docs.llamaindex.ai/en/stable/llama_cloud/llama_parse/) 확인 필요.

출처: [LlamaParse 공식 문서](https://docs.llamaindex.ai/en/stable/llama_cloud/llama_parse/) · [Best AI Document Parsers 2025 (LlamaIndex)](https://www.llamaindex.ai/insights/document-parser-comparison-2025)

---

#### PyMuPDF (fitz)
- **URL**: https://pymupdf.readthedocs.io  
- **GitHub**: https://github.com/pymupdf/PyMuPDF  
- **특징**: 고성능 Python PDF 처리 라이브러리. 텍스트 블록별 좌표 추출, 표 감지, 이미지 추출.
- **잘하는 것**: 텍스트 블록 좌표·폰트 정보 포함 추출(`get_text("dict")`). 단순 테두리 표를 GitHub Markdown으로 변환.
- **입력**: PDF (및 일부 이미지 포맷)
- **출력**: 평문 텍스트, 딕셔너리(좌표·폰트·블록 구조), Markdown 표
- **좌표**: 페이지 내 픽셀 좌표(포인트 단위, 1/72인치) 포함. 출처 정보(provenance) 보존 가능.
- **한계**: 테두리 없는 표·병합셀·다중 페이지 표는 추가 개발 필요.
- **가격**: 오픈소스 무료(AGPL/상용 라이선스 옵션).

출처: [PyMuPDF 공식 문서](https://pymupdf.readthedocs.io) · [PyMuPDF GitHub](https://github.com/pymupdf/PyMuPDF)

---

#### pdfplumber
- **URL**: https://github.com/jsvine/pdfplumber  
- **특징**: PDF 페이지를 픽셀 수준 좌표 기하학으로 분석. 표 경계 시각적 디버깅 가능.
- **잘하는 것**: 복잡한 레이아웃·비표준 표 구조. 좌표 기반 세밀 제어.
- **입력**: PDF
- **출력**: Python 딕셔너리/리스트 → pandas DataFrame
- **한계**: 벤더별 수동 설정 조정 필요. 다중 페이지 표 자동 연결 없음.

출처: [Python PDF Table Extraction: pdfplumber vs Camelot vs Tabula](https://invoicedataextraction.com/blog/python-pdf-table-extraction-invoices)

---

#### Camelot
- **URL**: https://camelot-py.readthedocs.io  
- **GitHub**: https://github.com/camelot-dev/camelot  
- **특징**: PDF 표 추출 전용. Lattice(테두리 있는 표)·Stream(공백 기반 표) 두 가지 모드.
- **잘하는 것**: 테두리 있는 표의 정확한 추출. 정확도 점수(`parsing_report`) 제공.
- **입력**: 텍스트 기반 PDF (스캔 PDF는 OCR 옵션 별도 설치)
- **출력**: pandas DataFrame + 정확도 메트릭
- **한계**: 스캔 PDF 기본 미지원. 다중 페이지 표 수동 이어붙임 필요. 일부 레포 아카이브(2025년 1월 read-only 전환) → 활성 포크 확인 필요.

출처: [Camelot 공식 문서](https://camelot-py.readthedocs.io) · [Camelot GitHub](https://github.com/camelot-dev/camelot)

---

#### Tabula (tabula-py)
- **URL**: https://tabula-py.readthedocs.io  
- **특징**: Java 기반 Tabula를 Python으로 래핑. 최소 설정으로 PDF 표 추출.
- **잘하는 것**: 정형화된 표의 빠른 추출. 대용량 문서 전체 페이지 처리.
- **입력**: 텍스트 기반 PDF
- **출력**: pandas DataFrame
- **한계**: Java Runtime Environment(JRE) 필요. 테두리 없는 표에서 정확도 저하. 디버깅 정보 부족.

출처: [Python PDF Table Extraction 비교](https://invoicedataextraction.com/blog/python-pdf-table-extraction-invoices)

---

#### Apache Tika
- **URL**: https://tika.apache.org  
- **GitHub**: https://github.com/apache/tika  
- **특징**: 1,000개 이상 파일 포맷에서 텍스트·메타데이터 추출. Java 기반. MIME 타입 자동 감지.
- **잘하는 것**: 광범위한 포맷 지원(PDF·DOC·XLS·PPT·이미지·영상 등). REST API 서버 모드.
- **입력**: 1,000+ 포맷 (PDF, Office 문서, 이미지, 영상 등)
- **출력**: 평문 텍스트 + 메타데이터 (XML/JSON)
- **한계**: 표 구조 보존 약함. Tika 2.x EOL(2025년 4월), Tika 3.x는 Java 11 이상 필요. 레이아웃 인식 수준 낮음.
- **가격**: Apache 오픈소스 무료.

출처: [Apache Tika 공식](https://tika.apache.org) · [Apache Tika GitHub](https://github.com/apache/tika)

---

#### python-pptx
- **URL**: https://python-pptx.readthedocs.io  
- **특징**: PPTX 파일 읽기/쓰기 전용. 슬라이드 구조(제목·본문·도형·표·메모)를 계층적으로 접근.
- **잘하는 것**: 슬라이드 제목·본문·불릿 포인트·화자 노트 추출. 표 행/열 직접 접근.
- **입력**: .pptx
- **출력**: Python 객체(텍스트 문자열, 구조적 슬라이드 계층)
- **한계**: 도형/그림 내 텍스트는 별도 처리. .ppt(구형 바이너리) 미지원.

출처: [python-pptx 공식](https://python-pptx.readthedocs.io)

---

#### openpyxl
- **URL**: https://openpyxl.readthedocs.io  
- **특징**: XLSX 읽기/쓰기. 병합셀, 스타일, 수식 접근.
- **잘하는 것**: 셀 값·수식·스타일·병합 정보 직접 접근.
- **입력**: .xlsx
- **출력**: Python 객체 (셀 값, DataFrames via pandas)
- **한계**: 병합셀 자동 전파 없음(수동 처리 필요). 레이아웃 의미(배경색·들여쓰기) 해석은 추가 로직 필요.

출처: [openpyxl 공식](https://openpyxl.readthedocs.io) · [Merged cells 처리 예시](https://gist.github.com/tchen/01d1d61a985190ff6b71fc14c45f95c9)

---

### 3-2. 클라우드 상용 서비스

#### Azure AI Document Intelligence
- **URL**: https://azure.microsoft.com/ko-kr/products/ai-services/ai-document-intelligence  
- **특징**: Microsoft Azure의 문서 지능 서비스. OCR + 레이아웃 분석 + 사전학습 모델(인보이스·영수증·신분증 등) + 커스텀 모델.
- **잘하는 것**: 커스텀 모델 구축(5개 샘플로 시작 가능). Microsoft 환경 연동. 온프레미스/에어갭 컨테이너 옵션.
- **표 추출**: 행/열 구조 보존. 병합셀·제목 행 인식.
- **출력**: JSON (요소별 바운딩박스·신뢰도·페이지 번호)
- **강점**: 인보이스·품목 라인 추출에서 AWS Textract 대비 높은 성능 벤치마크. 한국어 지원.
- **한계**: Azure 의존. 가격은 [공식 문서](https://azure.microsoft.com/pricing/details/ai-document-intelligence/) 및 PoC 확인 필요.

출처: [AWS Textract vs Azure Document Intelligence 비교 (SparkCo)](https://sparkco.ai/blog/aws-textract-vs-azure-document-intelligence-a-deep-dive) · [Invoice Extraction Benchmark (BusinessWareTech)](https://www.businesswaretech.com/blog/research-best-ai-services-for-automatic-invoice-processing)

---

#### AWS Textract
- **URL**: https://aws.amazon.com/textract/  
- **특징**: Amazon AWS의 문서 분석 서비스. 인쇄·손글씨 텍스트 + 표 + 양식(Key-Value) 추출.
- **잘하는 것**: 인보이스·보험·영수증의 표·양식. AWS S3·Lambda 서버리스 파이프라인 연동. HIPAA 준수.
- **표 추출**: 95~99% 정확도(표준 인쇄 문서). AnalyzeExpense로 인보이스 특화.
- **출력**: JSON (블록 구조, 바운딩박스 좌표, 신뢰도 점수)
- **한계**: 동아시아 문자(한국어·중국어·일본어) 지원 제한 — **한국어 문서에는 확인 필요**. AWS 의존.
- **가격**: [공식 문서](https://aws.amazon.com/textract/pricing/) 및 PoC 확인 필요.

출처: [AWS Textract vs Azure vs Google 비교](https://invoicedataextraction.com/blog/aws-textract-vs-google-document-ai-vs-azure-document-intelligence)

---

#### Google Document AI
- **URL**: https://cloud.google.com/document-ai  
- **특징**: Google Cloud의 문서 처리 플랫폼. 200+ 언어 지원. 다양한 사전 빌드 프로세서(양식·인보이스·운전면허증 등).
- **잘하는 것**: 광범위한 언어 지원. 표준 문서 유형의 엔터프라이즈 자동화. 한국어 포함.
- **표 추출**: 레이아웃 파서가 표·키값 쌍·체크박스 인식.
- **출력**: JSON (요소별 바운딩박스·신뢰도·페이지 번호)
- **가격**: [공식 문서](https://cloud.google.com/document-ai/pricing) 및 PoC 확인 필요.

출처: [AWS vs Google vs Azure 문서 지능 비교](https://invoicedataextraction.com/blog/aws-textract-vs-google-document-ai-vs-azure-document-intelligence)

---

### 3-3. 도구 선택 요약표

| 도구 | 유형 | 잘하는 것 | 표 추출 | 레이아웃 | 좌표 | 한국어 |
|------|------|----------|---------|---------|------|-------|
| **Docling** | 오픈소스 | 복잡한 표·레이아웃, 로컬 실행 | ★★★ | ★★★ | ✓ | 확인 필요 |
| **Unstructured** | 오픈소스+SaaS | 다양한 포맷, OCR | ★★ | ★★ | ✓ | 확인 필요 |
| **LlamaParse** | 클라우드 API | 빠른 처리, LLM-ready | ★★ | ★★★ | △ | 확인 필요 |
| **PyMuPDF** | 오픈소스 | 좌표 추출, 성능 | ★(단순) | ★★ | ✓ | ✓ |
| **pdfplumber** | 오픈소스 | 세밀한 표 제어 | ★★ | ★★ | ✓ | ✓ |
| **Camelot** | 오픈소스 | 테두리 표 전문 | ★★★(테두리) | △ | △ | ✓ |
| **Apache Tika** | 오픈소스 | 광범위한 포맷 | △ | △ | △ | ✓ |
| **Azure Doc Intel** | 클라우드 | 커스텀 모델, MS 연동 | ★★★ | ★★★ | ✓ | ✓ |
| **AWS Textract** | 클라우드 | AWS 연동, 인보이스 | ★★★ | ★★ | ✓ | △ |
| **Google Doc AI** | 클라우드 | 다국어, 엔터프라이즈 | ★★★ | ★★★ | ✓ | ✓ |

★★★ 우수 / ★★ 양호 / ★ 기본 / △ 제한적  
한국어 지원은 각 서비스 공식 문서 PoC 검증 필요.

---

## 4. 구조화 출력 포맷과 출처 정보(Provenance) 보존

### 4-1. 주요 출력 포맷

| 포맷 | 용도 | 특징 |
|------|------|------|
| **JSON** | 프로그램 처리 | 요소별 타입·텍스트·좌표·메타데이터 구조화. 벡터 DB 입력용. |
| **Markdown** | LLM/RAG 입력 | 제목(#)·표(\|)·코드블록으로 계층 표현. 사람이 읽기 편함. |
| **HTML 표** | 표 구조 보존 | `<table><tr><td>` 태그로 병합셀 포함 행/열 구조 보존. |
| **pandas DataFrame** | 데이터 분석 | 표 데이터를 즉시 분석·변환 가능. |

### 4-2. 출처 정보(Provenance) 보존의 중요성

AI가 답변을 생성할 때 "이 답변의 근거가 어느 문서 몇 페이지 어느 위치에 있는가"를 추적할 수 있어야 한다. 이것이 **출처 정보(Provenance/Source Attribution)**다.

**보존해야 할 정보:**
- **문서 ID**: 파일명, 버전, 문서 고유 식별자
- **페이지 번호**: 원본 PDF의 몇 페이지에 있었는가
- **좌표(Bounding Box)**: 페이지 내 X·Y·Width·Height (픽셀 또는 포인트 단위)
- **요소 유형**: 제목인지, 본문인지, 표인지
- **청크 ID**: 이 텍스트 청크의 고유 식별자

**보존 방법:**
- Unstructured: JSON 출력에 `metadata.coordinates` (PixelSpace 기준 points 배열)
- Docling: `DoclingDocument`의 바운딩박스 + `provenance` 필드
- PyMuPDF: `page.get_text("dict")`로 블록별 bbox 좌표 반환
- Azure/AWS/Google: JSON 출력에 `boundingBox` 또는 `boundingPolygon`

**왜 중요한가:**
- RAG 시스템에서 검색 결과의 근거 문서·페이지를 사용자에게 제시 가능
- 감사(Audit) 추적: AI 답변이 어느 작업표준서 몇 페이지를 참조했는지 기록
- 품질 검증: 추출이 올바른지 원본과 대조 가능

출처:  
- [Docling: Layout-Aware Document Intelligence Pipeline (MarkTechPost)](https://www.marktechpost.com/2026/06/16/how-to-build-a-parsing-pipeline-with-docling-parse-for-layout-aware-document-intelligence/)  
- [Unstructured — PDF Parsing](https://unstructured.io/blog/how-to-parse-a-pdf-part-1)

---

## 5. 청킹(Chunking) 기준과 검색 품질

> 관점: RAG 앱을 만드는 법이 아니라, "AI가 검색할 수 있는 청크 단위로 데이터를 준비"하는 법.

### 5-1. 청킹이란

청킹(Chunking)은 전처리로 구조화된 텍스트를 **벡터 임베딩(Vector Embedding) 단위로 분할**하는 작업이다. 각 청크는 독립적으로 임베딩되어 벡터 DB에 저장된다. 검색 시 질문과 유사한 청크를 찾아 LLM에 제공한다.

### 5-2. 주요 청킹 전략

#### ① 고정 크기 청킹(Fixed-Size Chunking)
- N자(또는 N토큰)마다 자름. 겹침(overlap) 설정 가능.
- **장점**: 단순, 빠름, 구현 쉬움.
- **단점**: 문장 중간·논리 단위 중간을 자를 수 있음. 의미 손실 위험.
- **사용 권장**: 간단한 PoC, 단순 문서.
- **권장 시작값**: 약 250토큰(~1,000자) + 20~50토큰 겹침.

#### ② 구조 기반 청킹(Structure-Based / Recursive)
- 단락(`\n\n`) → 줄바꿈(`\n`) → 문장(`.`) → 단어 순으로 분리 기준 우선순위 적용.
- **장점**: 자연스러운 경계 존중.
- **단점**: 복잡한 레이아웃(표·목록·다단) 처리 미흡.

#### ③ 제목 기반 청킹(By Title / Section-Based)
- H1·H2·H3 제목을 기준으로 섹션 단위로 분리.
- **장점**: 섹션 경계를 지킴. 검색 정확도 높음.
- **단점**: 제목이 없거나 불규칙한 문서에서 효과 제한.

#### ④ 의미 단위 청킹(Semantic Chunking)
- 임베딩 유사도로 주제가 바뀌는 지점을 탐지해 분할.
- **장점**: 주제 일관성 최고. 복잡한 내용에서 검색 정밀도 높음.
- **단점**: 계산 비용 높음. 단순 데이터셋에서는 고정 크기보다 나쁜 결과도 있음(200단어 고정이 87% vs. 의미 청킹 87% 동등 사례 있음).

#### ⑤ 표(Table) 청킹 — 특별 처리
- **표는 반드시 통째로 한 청크로 유지**해야 한다. 표를 행 단위로 자르면 컬럼 헤더와 데이터가 분리되어 검색 불가.
- 표 → Markdown 또는 HTML로 직렬화(serialize) 후 단일 청크로 저장.
- 대형 표(100행 이상)는 논리적 그룹(제품 카테고리, 날짜 범위 등) 기준으로 분할.

### 5-3. 청킹이 검색 품질에 미치는 영향

| 문제 | 원인 | 결과 |
|------|------|------|
| 청크가 너무 크면 | 여러 주제가 하나의 벡터에 압축 | 유사 검색 시 관련성 희석, 정확도 저하 |
| 청크가 너무 작으면 | 문맥이 잘려나감 | LLM에 불완전한 정보 제공 |
| 표를 행으로 자르면 | 헤더-데이터 분리 | 검색 불가, 오답 생성 |
| 섹션 경계 무시하면 | 다른 주제 혼합 | 관련 없는 텍스트 혼합 검색 |

출처:  
- [Chunking Strategies for RAG (Unstructured)](https://unstructured.io/blog/chunking-for-rag-best-practices)  
- [Chunking Strategies (Weaviate)](https://weaviate.io/blog/chunking-strategies-for-rag)  
- [Ultimate Guide to Chunking (Databricks Community)](https://community.databricks.com/t5/technical-blog/the-ultimate-guide-to-chunking-strategies-for-rag-applications/ba-p/113089)  
- [Best Chunking Strategies 2026 (Firecrawl)](https://www.firecrawl.dev/blog/best-chunking-strategies-rag)

---

## 6. 제조 현업(두산 계열사) 예시

### 예시 1: 품질 검사 보고서 PDF의 표

**상황**: 두산에너빌리티 품질팀에서 생산 공정별 불량률·검사 결과를 PDF로 관리. 총 300페이지, 페이지당 2~3개 표(공정명·검사항목·합격기준·실측값·판정).

**문제**: 단순 텍스트 추출 시 표가 평문으로 분해됨. "합격기준 0.05mm 실측 0.03mm 합격"이 여러 셀의 텍스트가 나열되어 어느 행이 어느 공정 데이터인지 불명확.

**전처리 적용**:
1. Docling(오픈소스) 또는 Azure AI Document Intelligence(상용)로 레이아웃 인식 파싱
2. 표를 HTML/Markdown 구조로 추출 (행/열 보존)
3. 각 행에 출처 메타데이터 부여: `{문서ID: "QR-2024-0123", 페이지: 45, 표번호: 2, 행번호: 7}`
4. 표 전체를 단일 청크로 저장(행 단위 분리 금지)

**효과**: AI가 "2024년 3분기 터빈 블레이드 용접 불량률"을 질문하면 정확한 표 행을 찾아 수치 포함 답변 + 원본 페이지 45 링크 제시.

---

### 예시 2: 설비 점검 체크시트 Excel

**상황**: 두산밥캣 설비팀의 주간 점검 체크시트. 시트별 설비명, 병합셀로 점검 카테고리 그룹화, 셀 색상으로 이상 여부 표시.

**문제**: openpyxl로 단순 추출 시 병합셀에서 `None` 값 발생. "카테고리A - 항목1·항목2·항목3"의 관계가 데이터에서 사라짐. 배경색 의미(빨강=이상) 미포착.

**전처리 적용**:
1. openpyxl로 병합셀 범위 탐지 → 값 전파(forward-fill)로 None 채움
2. 셀 배경색 읽어 `이상여부` 컬럼 추가
3. JSON 변환: `{시트: "3월W2", 설비: "CNC선반-01", 카테고리: "윤활", 점검항목: "오일레벨", 결과: "정상", 이상여부: false}`
4. 레코드 단위(설비×항목)로 청킹

**효과**: AI가 "CNC선반-01의 최근 이상 이력"을 질문하면 이상 표시된 레코드만 정확히 찾아 반환.

---

## 7. 참고자료(References)

| 도구/문서 | URL |
|-----------|-----|
| Unstructured 공식 | https://unstructured.io |
| Unstructured — PDF 파싱 블로그 | https://unstructured.io/blog/how-to-parse-a-pdf-part-1 |
| Unstructured — 청킹 가이드 | https://unstructured.io/blog/chunking-for-rag-best-practices |
| Docling GitHub (IBM) | https://github.com/docling-project/docling |
| Docling 파이프라인 가이드 (MarkTechPost) | https://www.marktechpost.com/2026/06/16/how-to-build-a-parsing-pipeline-with-docling-parse-for-layout-aware-document-intelligence/ |
| LlamaParse 공식 문서 | https://docs.llamaindex.ai/en/stable/llama_cloud/llama_parse/ |
| Best AI Document Parsers 2025 (LlamaIndex) | https://www.llamaindex.ai/insights/document-parser-comparison-2025 |
| Docling vs LlamaParse vs Unstructured 벤치마크 (Procycons) | https://procycons.com/en/blogs/pdf-data-extraction-benchmark/ |
| PDF Table Extraction Showdown (Boring Bot) | https://boringbot.substack.com/p/pdf-table-extraction-showdown-docling |
| PyMuPDF 공식 문서 | https://pymupdf.readthedocs.io |
| PyMuPDF GitHub | https://github.com/pymupdf/PyMuPDF |
| pdfplumber GitHub | https://github.com/jsvine/pdfplumber |
| Camelot 공식 문서 | https://camelot-py.readthedocs.io |
| Camelot GitHub | https://github.com/camelot-dev/camelot |
| Apache Tika 공식 | https://tika.apache.org |
| Apache Tika GitHub | https://github.com/apache/tika |
| python-pptx 공식 | https://python-pptx.readthedocs.io |
| openpyxl merged cells 처리 (Gist) | https://gist.github.com/tchen/01d1d61a985190ff6b71fc14c45f95c9 |
| Azure AI Document Intelligence | https://azure.microsoft.com/ko-kr/products/ai-services/ai-document-intelligence |
| AWS Textract | https://aws.amazon.com/textract/ |
| Google Document AI | https://cloud.google.com/document-ai |
| AWS vs Azure 비교 (SparkCo) | https://sparkco.ai/blog/aws-textract-vs-azure-document-intelligence-a-deep-dive |
| AWS vs Google vs Azure 비교 | https://invoicedataextraction.com/blog/aws-textract-vs-google-document-ai-vs-azure-document-intelligence |
| Chunking Strategies (Weaviate) | https://weaviate.io/blog/chunking-strategies-for-rag |
| Best Chunking Strategies 2026 (Firecrawl) | https://www.firecrawl.dev/blog/best-chunking-strategies-rag |
| pdfplumber vs Camelot vs Tabula 비교 | https://invoicedataextraction.com/blog/python-pdf-table-extraction-invoices |
| Best PDF Parsers for AI 2026 (Firecrawl) | https://www.firecrawl.dev/blog/best-pdf-parsers |
