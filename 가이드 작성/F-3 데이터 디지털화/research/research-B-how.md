# F-3 데이터 디지털화 — How + Tech Stack 리서치

> 작성일: 2026-06-29 | 관점: "AI가 쓸 데이터를 준비·정비하는 법" | 눈높이: 제조 현업(두산에너빌리티)

---

## 1. 디지털화 전환 절차

### 일반적인 문서/기록 디지털화 프로젝트 단계

| 단계 | 하는 일 | 제조 예시 |
|------|---------|----------|
| **①자산 조사** (인벤토리) | 어떤 종류의 문서가 얼마나 있는지 파악. 법령 보존 의무·업무 중요도·이용 빈도 기준으로 목록 작성. | 설비 점검 일지, 도면 원본, 품질 검사 기록, 납품 서류 등 전수 조사 |
| **②우선순위 선정** | 필수 보존(법령) → 자주 쓰는 문서 → 활용 가능성 높은 순으로 배치 우선순위 결정. 훼손·노화 위험 문서 긴급 처리. | 안전사고 기록, 설비 이력, 하자 클레임 서류를 최우선으로 |
| **③물리 준비** | 스테이플·클립 제거, 구겨진 종이 펴기, 묶음 해체. 문서 정돈(연·월 순, 설비 번호 순 등). | 수십 년치 보관 문서를 박스 단위로 분류 |
| **④스캔·변환** | 산업용 스캐너로 고해상도(300dpi 이상) 이미지 생성. 종류별 도구 선택: 종이→스캔, 음성→STT, 수기→ICR(필기 인식). | 도면·표 포함 문서는 컬러·고해상도 스캔 필수 |
| **⑤OCR/ICR 처리** | 이미지에서 기계가 읽을 수 있는 텍스트·데이터로 변환. 인쇄체 = OCR, 수기 = ICR, 음성 = STT | 검사 성적서의 수기 측정값 → 구조화된 텍스트로 변환 |
| **⑥검수(QA)** | 변환 결과의 정확도·완전성 확인. 누락·오독 보정. 샘플링 또는 전수 검토. | AI가 1차 변환 → 현업 담당자가 주요 수치(측정값, 설비번호) 이중 확인 |
| **⑦메타데이터 등록** | 문서 유형, 작성일, 설비 코드, 담당자, 보존 기한 등 식별 정보 태깅. 검색·분류 기반. | `설비코드=GT-001`, `문서유형=점검기록`, `작성일=2023-03` |
| **⑧자산 적재** | 중앙 저장소(ECM, DMS, 데이터 레이크)에 업로드. 접근 권한 설정 후 공식 자산으로 등록. | SharePoint / 사내 DMS에 폴더 구조 맞춰 적재 |

**출처**
- Athento, "Document digitization: steps to follow and best practices" — https://www.athento.com/document-digitization-steps-to-follow-and-best-practices/
- Emerald Document, "A Step By Step Guide To Planning a Document Scanning Project" — https://emeralddocument.com/step-by-step-guide-to-planning-a-scanning-project/
- Label Your Data, "Document Digitization with OCR: Process, Benefits, and Best Practices for 2026" — https://labelyourdata.com/articles/document-digitization-with-ocr

---

## 2. 지속 수집(승급) — Shadow Data / Dark Data 관리

### 개념

| 용어 | 정의 |
|------|------|
| **Shadow Data(그림자 데이터)** | 공식 관리 시스템 밖에서 생성·저장·공유되는 데이터. 개인 PC Excel, 팀 공유폴더, 비승인 SaaS 등. |
| **Dark Data(어두운 데이터)** | 수집은 됐지만 분류·관리되지 않아 활용되지 않는 데이터. 백업 서버에 잠든 파일, 삭제되지 않은 이메일 첨부 파일 등. |

### 왜 문제인가
- 동일 데이터가 여러 버전으로 분산 → 정본 불명확
- 접근 권한·보안 통제 밖 → 데이터 유출·규정 위반 위험
- AI 학습에 활용 불가능 — 어디 있는지 모르는 데이터는 쓸 수 없다

### 공식 자산으로 승급하는 방법

1. **자동 탐색(Data Discovery)**: 조직 내 SQL DB·SharePoint·개인 드라이브·S3를 스캔해 비관리 데이터 목록 자동 생성.
2. **원천 일원화**: 신규 데이터는 처음부터 지정 폴더·시스템에만 생성하도록 정책 수립.
3. **입력 표준화**: Excel 자유 양식 대신 정해진 템플릿·드롭다운 코드 기반 입력 양식으로 전환.
4. **이전(Migration)**: 기존 Shadow Data를 데이터 카탈로그에 등록하거나 폐기 결정(보존 필요 없으면 삭제).
5. **지속 모니터링**: 비승인 저장소에 다시 쌓이지 않도록 정기 감사.

> 예시: 품질팀 각자 PC에 흩어진 Excel 품질 기록 → 표준 데이터 입력 양식(e-form)으로 전환 후 중앙 DMS에 자동 저장 → 공식 품질 데이터 자산으로 등록

**출처**
- SealPath, "Shadow Data Basics - How to Prevent its Risks in Organizations" — https://www.sealpath.com/blog/shadow-data-organizations/
- Lightbeam AI, "Discovering Shadow Data Across SQL, SharePoint, and S3 with DSPM" — https://www.lightbeam.ai/resources/blogs/discovering-shadow-data-across-sql-sharepoint-and-s3-with-dspm/
- CloudHew, "Shadow Data in Enterprise: Risks, Governance & Control Strategies" — https://cloudhew.com/blogs/shadow-data-in-the-enterprise-the-hidden-risk-undermining-your-data-strategy/

---

## 3. Digital-first(처음부터 디지털) 정착

### 핵심 개념
종이 양식을 디지털화하는 것이 아니라, **처음부터 디지털로만 기록**하는 방식으로 전환. 현장 작업자가 태블릿·스마트폰으로 데이터를 입력 → 중앙 시스템에 실시간 적재.

### 핵심 기능

| 기능 | 설명 | 효과 |
|------|------|------|
| **드롭다운·코드 선택** | 자유 입력 대신 허용값 목록에서 선택 | 오타·비표준 표기 제거 |
| **필수 입력 강제** | 공란으로 제출 불가 | 누락 데이터 방지 |
| **자동 타임스탬프** | 제출 시각 자동 기록 | 수기 날짜 변조 방지 |
| **QR/바코드 스캔** | 설비 코드·부품 번호 자동 입력 | 입력 오류 근절 |
| **사진 첨부** | 현장 상태 이미지 함께 제출 | 불량 증적 자동 보관 |
| **전자서명** | 검수자 서명 디지털화 | 종이 결재 불필요 |
| **오프라인 모드** | 인터넷 불안정한 현장에서도 입력 후 나중에 동기화 | 제조 현장 적용 가능 |

> 제조 예시: 터빈 블레이드 치수 검사 시 검사원이 태블릿에 측정값 입력 → 설비 코드 QR 스캔으로 자동 연결 → 기준값 초과 시 즉시 알람 → 담당자 전자서명 후 품질 DB에 자동 저장

### 대표 솔루션
- **OpsTrakker eForms** (제조·의약품 GMP 특화, FDA 21 CFR Part 11 준수) — https://opstrakker.com/solutions/eforms/
- **FastField Forms** (모바일 현장 데이터 수집, 오프라인 지원) — https://www.fastfieldforms.com/digital-forms.html
- **QR Mobile Data** (스마트폰·태블릿 제조 현장 양식) — https://www.ahg.com/qr-mobile-data/ready-to-use-business-digital-forms/digital-forms-workflow-for-manufacturing/

**출처**
- OpsTrakker, "Electronic GMP Forms and Digital Work Instructions" — https://opstrakker.com/solutions/eforms/
- FastField Forms, "Digital Forms App" — https://www.fastfieldforms.com/digital-forms.html

---

## 4. 역할·책임 (R&R)

| 역할 | 주요 책임 |
|------|----------|
| **현업 오너(Data Owner)** | 디지털화할 자산 목록 확인·우선순위 결정. 변환 결과 검수(내용 정확성 판단). 메타데이터 정의(어떤 항목이 필요한가). |
| **데이터 조직** | 표준 포맷·메타데이터 스키마 설계. 중앙 저장소 운영. 전체 프로젝트 조율·품질 기준 관리. |
| **IT** | 스캔·OCR 인프라 구성·운영. 저장소·파이프라인 구축. 보안 및 접근 권한 설정. |
| **외주 스캔업체** | 대량 물리 문서 스캔·이미지 변환 실행. 장비 운영, 이미지 품질 1차 보증. |
| **외주 데이터 입력업체** | OCR 후 오독 보정, 구조화 입력 작업(필요 시). |

> 외주를 활용할 때도 **메타데이터 정의와 검수 기준 결정은 반드시 내부(현업+데이터조직)**가 해야 한다. 외주는 실행만.

**출처**
- Atlan, "Data Governance Roles & Responsibilities 2026" — https://atlan.com/data-governance-roles-and-responsibilities/
- Umbrex, "Roles, Responsibilities, and RACI That Actually Works" — https://umbrex.com/resources/data-governance-playbook/roles-responsibilities-and-raci-that-actually-works/

---

## 5. Tech Stack — 솔루션 플레이어 맵

### 5-1. IDP(지능형 문서 처리) vs OCR 개념 구분

| 구분 | 특징 | 적합한 경우 |
|------|------|------------|
| **OCR** (문자 인식) | 이미지 → 텍스트 변환. 단순 읽기. | 정형 인쇄 문서, 대량 단순 변환 |
| **IDP** (지능형 문서 처리) | OCR + AI(분류·추출·검증·워크플로우 자동화). 의미 이해. | 비정형 문서, 표·양식 자동 추출, 여러 문서 유형 처리 |

> IDP = OCR은 기초 기술이고 그 위에 AI가 더해진 상위 개념. 단순 텍스트 추출이면 OCR 충분, 문서 유형 분류·항목 자동 추출이 필요하면 IDP.

**출처**: ABBYY, "OCR vs. IDP: What's the difference?" — https://www.abbyy.com/blog/ocr-vs-idp/

---

### 5-2. 클라우드 OCR / 문서 AI 솔루션

| 솔루션 | 제공사 | 강점 | 온프렘 | 한글 |
|--------|--------|------|--------|------|
| **Azure AI Document Intelligence** | Microsoft | 폼·인보이스 등 사전학습 모델 풍부. MS 생태계(SharePoint·Teams) 연동. | 불가(클라우드 전용) | 지원 |
| **Google Document AI** | Google | 200개+ 언어 지원. 복잡 레이아웃. Vertex AI 연동. | 불가(클라우드 전용) | 지원 |
| **AWS Textract** | Amazon | 표 추출 강점(셀 관계 매핑). AWS 생태계 연동. | 불가(클라우드 전용) | 제한적 |
| **ABBYY FineReader Server** | ABBYY | **온프렘 설치 가능**. 한국어 포함 200개+ 언어. 대량 배치 처리. 구성 유연. | **가능** | 지원 |
| **ABBYY Vantage** | ABBYY | IDP 플랫폼. Kubernetes 기반. 클라우드 또는 **프라이빗 클라우드/온프렘** 선택. 2024 IDP 어워드 수상. | **가능**(프라이빗 클라우드) | 지원 |

**출처**
- Azure AI Document Intelligence — https://azure.microsoft.com/en-us/pricing/details/document-intelligence/
- Google Document AI vs AWS Textract 비교 — https://invoicedataextraction.com/blog/aws-textract-vs-google-document-ai-vs-azure-document-intelligence
- ABBYY Vantage — https://www.abbyy.com/vantage/
- ABBYY FineReader Server — https://easydataworld.com/abbyy-finereader-server/

---

### 5-3. 국내 OCR / 한글·수기 인식 솔루션

| 솔루션 | 제공사 | 강점 | 온프렘 | 특이사항 |
|--------|--------|------|--------|---------|
| **CLOVA OCR** | 네이버 클라우드 | 한국어·일어·영어 인식. **한글 수기 인식** 지원. 영수증·명함 등 특화 모델. | 미확인(클라우드 주력) | API Gateway 연동 |
| **Document Parse** | 업스테이지(Upstage) | 복잡 테이블·다단 레이아웃 처리. HTML/Markdown 출력(LLM 연동 최적). **온프렘 제공**. AWS·MS보다 정확도 5%+ 높다고 자체 발표. 100페이지/분 처리. | **가능** | 보험업계(삼성생명) 레퍼런스 |

> 주의: 업스테이지의 정확도 비교 수치는 자사 발표 기준. 독립 검증 필요.

**출처**
- CLOVA OCR — https://www.ncloud.com/product/aiService/ocr
- 업스테이지 Document Parse — https://www.upstage.ai/products/document-parse
- 업스테이지 공식 발표 — https://www.aitimes.kr/news/articleView.html?idxno=32466

---

### 5-4. 오픈소스 OCR (온프렘·폐쇄망 특화)

| 솔루션 | 강점 | 한글 | 수기 | 비고 |
|--------|------|------|------|------|
| **Tesseract** | 가장 오래되고 가벼움. CPU에서 빠름(0.77초). 10MB 바이너리. | 지원 | 미흡 | Google 유지보수 |
| **PaddleOCR** | 복잡 레이아웃·다열 문서 강점. PP-StructureV3(표·수식). **완전 오프라인(데이터 외부 전송 없음)**. GPU 불필요. | 지원 | 제한적 | 바이두 개발. 2026년 v5 출시 |
| **EasyOCR** | 설치·사용 쉬움. 80+ 언어. | 지원 | PaddleOCR보다 미흡 | Python 기반 |
| **docTR / Surya** | 최신(2024+). 딥러닝 기반 정확도 향상. | 제한적 | 개선 중 | 소규모 커뮤니티 |

> 폐쇄망 환경(보안 구역 제조 현장)에는 PaddleOCR 또는 Tesseract가 현실적 대안. 단, 수기·한글 특수 폰트는 추가 학습(Fine-tuning) 필요할 수 있음.

**출처**
- PaddleOCR vs Tesseract — https://www.koncile.ai/en/ressources/paddleocr-analyse-avantages-alternatives-open-source
- 오픈소스 OCR 비교 (2025) — https://www.mailxaminer.com/blog/best-open-source-ocr-models/

---

### 5-5. STT(음성→텍스트) 솔루션

| 솔루션 | 제공사 | 강점 | 온프렘 | 한국어 |
|--------|--------|------|--------|--------|
| **Whisper** | OpenAI | 99개 언어. 오픈소스(자체 설치 가능). 강인한 잡음 환경. | **가능**(오픈소스 자체 배포) | 지원(학습 데이터 부족 → 정확도 제한) |
| **CLOVA Speech / CLOVA Note** | 네이버 클라우드 | 한국어 최고 수준 인식률. 미디어·PSTN 환경 특화. 회의록 자동 생성. | 미확인 | **한국어 최적화** |
| **리턴제로 STT(VITO API)** | 리턴제로 | 1,500만 시간 한국어 학습. 오류율 4.66%(업계 최저 자체 발표). **클라우드+온프렘 선택 가능**. 화자 분리(10명). 배치 처리(1시간 음성 → 38초). | **가능** | **한국어 최적화** |
| **Google STT** | Google | 다국어 광범위 지원. Google Cloud 연동. | 불가(클라우드 전용) | 지원 |

> 회의록 자동화, 현장 작업 지시 구술 기록에 유용. 제조 현장 소음 환경에서는 전처리(노이즈 필터링) 필수.

**출처**
- 리턴제로 STT — https://www.rtzr.ai/stt
- CLOVA Speech — https://www.ncloud.com/product/aiService/clovaSpeech
- OpenAI Whisper — https://openai.com/index/whisper/

---

## 6. 솔루션 선정 기준

| 기준 | 확인 사항 | 우선 후보 |
|------|----------|----------|
| **한글·수기 처리** | 한글 인식 정확도, 수기 ICR 지원 여부 | CLOVA OCR, 업스테이지 Document Parse, ABBYY |
| **표·도면 처리** | 복잡 레이아웃, 다단 표, 기술 도면 처리 | 업스테이지 Document Parse, AWS Textract(표 강점), ABBYY |
| **온프렘(폐쇄망) 가능** | 클라우드 데이터 전송 없이 사내 설치 가능 여부 | ABBYY FineReader/Vantage, 업스테이지 Document Parse, PaddleOCR(오픈소스), 리턴제로 STT |
| **STT 포함 여부** | 음성 파일(회의록·구술 기록) 변환 필요 시 | CLOVA Speech, 리턴제로 STT, Whisper(오픈소스) |
| **대량 처리** | 수만 장 이상 배치 처리 성능 | ABBYY FineReader Server, 업스테이지(100페이지/분), AWS Textract |
| **기존 시스템 연동** | SAP·SharePoint·DMS 등과 API 연동 | Azure AI Document Intelligence(MS 생태계), ABBYY |

---

## 핵심 Take (5줄)

1. **디지털화 절차는 8단계**: 자산 조사 → 우선순위 → 물리 준비 → 스캔 → OCR/ICR → 검수 → 메타데이터 등록 → 자산 적재. 현업 오너의 검수(내용 정확성 판단)가 핵심 병목.
2. **Shadow/Dark Data 관리가 전제 조건**: 개인 PC·공유폴더에 흩어진 Excel·파일을 공식 자산으로 승급하지 않으면 AI가 활용 가능한 데이터는 빙산의 일각뿐. 원천 일원화 + 입력 표준화로 지속 수집.
3. **Digital-first(e-form) 전환이 장기 해법**: 과거 자료는 디지털화하고, 신규 데이터는 처음부터 드롭다운·타임스탬프·전자서명 기반 디지털 양식으로 생성해 추후 디지털화 부담 제거.
4. **제조 현장(폐쇄망) 환경에서는 온프렘 가능 솔루션 필수**: ABBYY FineReader/Vantage, 업스테이지 Document Parse, 오픈소스 PaddleOCR이 현실적 선택지. 클라우드 SaaS는 보안 검토 선행.
5. **한국어 특화 솔루션이 별도로 존재**: 네이버 CLOVA OCR(수기 포함), 업스테이지 Document Parse(표·복잡 레이아웃 강점), 리턴제로 STT(온프렘 가능, 한국어 오류율 최저 자체 주장) — 글로벌 솔루션으로 한글·수기를 처리하면 정확도 저하 위험.

---

## 불확실/검증 필요 항목

| 항목 | 불확실 내용 | 검증 방법 |
|------|-----------|----------|
| **업스테이지 Document Parse 정확도 수치** | "AWS·MS보다 5%+ 높다"는 자체 발표 기준. 독립 벤치마크 미확인. | 업스테이지 직접 PoC 또는 제3자 평가 보고서 확인 |
| **리턴제로 STT 온프렘 구성** | 온프렘 가능하다고 하나 구성 방식·비용 미공개 | 리턴제로 영업팀 직접 문의 필요 |
| **CLOVA OCR 온프렘 여부** | 공식 페이지에서 온프렘 언급 미확인 (클라우드 주력으로 보임) | NAVER Cloud 파트너 채널 확인 |
| **ABBYY 한글 수기 인식 정확도** | 한국어 수기에 대한 구체적 정확도 수치 없음 | PoC 테스트 필요 |
| **오픈소스 OCR 한글 Fine-tuning 난이도** | PaddleOCR의 한글 특수 폰트·수기 처리를 위한 추가 학습 비용·기간 미파악 | 내부 AI 팀 또는 SI 파트너와 검토 |

---

*리서치 완료: 2026-06-29*
