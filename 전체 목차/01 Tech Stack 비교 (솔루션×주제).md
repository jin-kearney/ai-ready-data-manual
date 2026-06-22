# AI-Ready Data 매뉴얼 — Tech Stack 비교 (솔루션 × 주제)

> **목적:** 20개 주제(A-1~F-4)에 "어떤 솔루션을 써야 하는가"를 한 곳에서 비교·결정하기 위한 **마스터 Tech Stack 정본(초안 v0.1)**.
> **관점 고정:** "AI/에이전트를 만드는 도구"가 아니라 **"그 AI가 쓸 데이터를 준비·정비하는 도구"**다. (절대 원칙 — CLAUDE.md / 데이터 준비 관점)
> **읽는 법(2층 구조):**
> - **Part A — 주제별 솔루션**: "이 주제엔 뭘 쓰지?" (주제 → 솔루션). 각 주제 가이드의 '솔루션' 섹션은 여기로 연결한다. **솔루션을 "제품명"이 아니라 "어떤 기능을 하느냐(capability)"로 비교한다** — 자동 메타 수집·동의어 매핑·표 구조 보존·AI 1차 라벨·그래프 추론처럼 *기능 열*을 축으로.
> - **Part A0 — 기능 기준 묶음 한눈에**: "이 기능을 하는 제품군은?" + "한 제품이 여러 주제를 묶어서 커버하나?"를 먼저 본다(이번에 새로 추가 — A·B 6개 주제). 핵심 인사이트 = **A-1 카탈로그·A-2 메타데이터·A-3 용어집은 별도 제품이 아니라 통합 거버넌스 플랫폼 1개가 함께 해결**한다.
> - **Part B — 묶음(플랫폼) × 주제 매트릭스**: "우리가 X 플랫폼을 깔면 어디까지 한 번에 되나?" (솔루션 → 주제).
> - **Part C — 묶음 스택 비교·선정 가이드**: 최종 의사결정용. 어느 스택이 어느 주제군에 강한가, 제조업(설비·OCR·비식별)엔 무엇이 중요한가.

> ⚠️ **이 표는 칸 채우기가 아니라 "필요 기능(capability)으로 고르게" 하는 표다.** 제품명은 시점에 따라 바뀐다 — 아래 **시장 변동 주의**를 반드시 함께 읽을 것. 카테고리·필요 기능을 먼저 보고, 제품은 PoC로 검증한다.

> ### 📌 운영 규칙 — 이 문서는 "살아있는 정본"이다
> **역할 분담:**
> - **1층 = 각 주제 가이드의 '솔루션' 섹션** — *그 주제 관점에서 솔루션의 **기능**을 비교*한다(예: 카탈로그라면 커넥터 범위·자동 메타 수집). 깊은 PoC·기능 상세는 가이드에 둔다.
> - **2층 = 이 문서** — *솔루션 **자체**를 주제 가로질러 묶어 평가·선정*한다(Part B 매트릭스·Part C 묶음 비교).
>
> **반영(reflect-back) 규칙 — 게이트(중요):** 이 문서는 **매 가이드 수정마다 자동 갱신하지 않는다**(낭비). **사용자가 해당 주제 가이드를 최종 승인하면서 "정본/Tech Stack에 반영해줘"라고 명시 요청할 때만** Part A 표(필요 시 Part B 매트릭스)를 갱신하고 별도 커밋으로 남긴다. 즉 가이드는 기능을 비교하고, 정본은 **승인된 결과만** 누적해 묶음 평가를 가능하게 한다. (작성 절차: `ai-ready-manual-guide` 스킬 / 표준: `공통 규칙/01 가이드 작성 표준.md`)
>
> **상태:** 현재 Part A는 사전 리서치 기반 초안. 가이드가 작성된 주제(**A군·B-2·B-3**)는 가이드와 상호 링크됨. 나머지는 가이드 작성 시 채워진다.

**표기:** ✓ 네이티브로 강함 · △ 부분/외부 보강 필요 · ✗ 없음(외부 도구 필수)

---

## 시장 변동 주의 (2025~2026, 인용 전 확인)

장표에 제품명을 적기 전 반드시 상태를 확인한다 — 매뉴얼 신뢰도에 직결된다.

| 구분 | 내용 |
|---|---|
| **서비스 종료** | **Humanloop**(프롬프트/평가) 2025-09-08 종료(Anthropic acqui-hire) · **OpenAI `v1/prompts`** 2026-11-30 종료 예정 · **Google Vertex AI 데이터 라벨링** 종료(2024-10) · **Google IoT Core** 종료(2023-08) |
| **인수·브랜드 변경** | Gretel→**NVIDIA**(2025) · Hazy→**SAS**(2024) · Syntho가 **MOSTLY AI 브랜드** 인수(2026) · Informatica→**Salesforce** · data.world→**ServiceNow** · Metaplane→**Datadog** · RDFox→**삼성전자** |
| **제품명 변경** | Databricks DLT→**Lakeflow Declarative Pipelines** · Azure Form Recognizer→**Document Intelligence** · Google Dataplex Universal Catalog→**Knowledge Catalog**(2026-04) · Alation Glossary→**Glossary Hub** · Atlan Glossary→**Business Graph** |

---

# Part A0. 기능 기준 묶음 한눈에 (A·B 6개 주제)

> 👉 **한 줄 요약:** 6개 주제(A-1·A-2·A-3·B-1·B-2·B-3)에 등장하는 솔루션을 **① 어떤 기능을 하느냐**로 묶고, **② 한 제품이 여러 주제를 함께 커버하면 한 줄로** 보여준다. **가장 중요한 결론 = A-1·A-2·A-3은 따로 사는 게 아니라 통합 거버넌스 플랫폼 1개가 통째로 한다.**

## A0-1. 4개 솔루션 묶음 (한 제품군이 무슨 기능으로 어느 주제를 덮나)

| 묶음 | 핵심 기능(capability) | 커버 주제 | 대표 제품(군) |
|---|---|---|---|
| **① 통합 데이터 거버넌스·카탈로그 플랫폼** | 자동 메타 수집(커넥터) · 검색/탐색 · **비즈니스 용어집(Glossary)+동의어 매핑** · 승인 워크플로 · **컬럼단위 계통(Lineage)** · AI 자연어 탐색 | **A-1·A-2·A-3** (+C-3 계통) **한 제품으로 묶임** | Collibra · Microsoft Purview · Atlan · Databricks Unity Catalog · (OSS) OpenMetadata · DataHub |
| **② 문서 전처리 / Document AI** | 레이아웃 인식 OCR · **표 구조 보존** · 마크다운/JSON 출력 · 청킹·임베딩 · 온프레미스/망분리 · 한국어 | **B-1** | Docling · Unstructured · LlamaParse · Camelot/pdfplumber · Azure Document Intelligence · Google Document AI · AWS Textract · (국내) Upstage |
| **③ 데이터 라벨링 / 주석 플랫폼** | **AI 1차 라벨(pre-label)** · 능동학습 · 프로그래매틱(약지도) 라벨링 · 라벨 오류 탐지 · 합의/검수(HITL) · 온프레미스 | **B-2** | Label Studio · CVAT · Snorkel Flow · Labelbox · Scale AI · Roboflow · Prodigy · Cleanlab · SageMaker Ground Truth · (보조) SAM 2 |
| **④ 그래프DB / 온톨로지** | **그래프 추론**(OWL/SHACL) · 다중 홉 경로 탐색 · SPARQL/Cypher 질의 · 벡터·GraphRAG · 온톨로지 저작 | **B-3** | Neo4j · Amazon Neptune · TigerGraph · Memgraph · Ontotext GraphDB · Stardog · Apache Jena · Protégé |

**핵심 인사이트:**
- **묶음 ①이 곧 이 매뉴얼 A군의 정답 구조다.** A-1·A-2·A-3을 도구 3개로 따로 사는 게 아니라, **카탈로그/거버넌스 플랫폼 1개**가 카탈로그 + 메타데이터 작성·승인 + 비즈니스 용어집을 함께 제공한다(계통 C-3까지). 6개 가이드 본문이 모두 같은 벤더 집합(Collibra·Purview·Atlan·Unity Catalog·OpenMetadata·DataHub)으로 수렴한다.
- **묶음 ②③④는 서로 다른 시장이다 — 한 제품으로 다 안 된다.** 전처리(B-1)·라벨링(B-2)·온톨로지(B-3)는 각각 전용/OSS 도구를 붙여야 하고, 묶음 ①의 거버넌스 플랫폼은 이 영역이 통째로 비어 있다.

## A0-2. 기능(capability) × 묶음 매트릭스 — "이 기능을 하는 건 어느 묶음인가"

> 행=기능, 열=4개 솔루션 묶음. ● 그 묶음의 핵심 기능 / ◐ 일부 제품만·부분 / ○ 연동·플러그인으로 / 공백=아님.

| 기능 (capability) | ① 거버넌스·카탈로그 | ② 문서 전처리 | ③ 라벨링·주석 | ④ 그래프·온톨로지 |
|---|:--:|:--:|:--:|:--:|
| 자동 메타데이터 수집(커넥터) | ● | | | ○ |
| 검색·탐색(자연어·필터) | ● | | | ◐ |
| 비즈니스 용어집·동의어 매핑 | ● | | | ◐(어휘 통합) |
| 데이터 계통(Lineage, 컬럼단위) | ● | | | |
| 승인·거버넌스 워크플로 | ● | | ◐(검수 큐) | ◐(거버넌스 에디션) |
| 문서 파싱·OCR | | ● | ○(문서 라벨링 전처리) | |
| 표 구조 보존(table structure) | | ● | | |
| 마크다운/JSON·청킹(RAG 적재) | | ● | | |
| AI 1차 라벨(pre-label)·능동학습 | | | ● | |
| 프로그래매틱/약지도 라벨링 | | | ◐(Snorkel) | |
| 라벨 합의·품질(IAA·오류탐지) | | | ●(도구+방법론) | |
| 그래프 추론(OWL·SHACL·Datalog) | | | | ◐(RDF 계열만) |
| 다중 홉 경로 탐색·GraphRAG | | | | ●(LPG 계열) |
| 온프레미스·망분리 배포 | ◐(OSS·일부 전용) | ●(Docling 등 로컬) | ◐(OSS·Prodigy) | ◐(자체호스팅·인메모리) |

> ⚠️ ●/◐는 **묶음의 일반적 성격**이다 — 같은 묶음 안에서도 제품마다 다르다(예: 그래프 추론은 RDF 트리플스토어[GraphDB·Stardog·Jena]는 강하나 LPG[Neo4j·Memgraph]는 약함). 제품 단위 차이는 아래 Part A 각 주제 표에서 본다.

---

# Part A. 주제별 솔루션 (주제 → 솔루션)

## A군 + C-3 — 데이터 카탈로그·메타데이터·용어집·계통 (한 제품으로 묶임) = 묶음 ①

> 📄 **주제 가이드(1층):** [A-1 데이터 카탈로그](../가이드%20작성/A-1%20데이터%20카탈로그/A-1%20데이터%20카탈로그.md) · [A-2 메타데이터](../가이드%20작성/A-2%20메타데이터/A-2%20메타데이터.md) · [A-3 비즈니스 Glossary](../가이드%20작성/A-3%20비즈니스%20Glossary/A-3%20비즈니스%20Glossary.md) (모두 작성됨) · C-3 Lineage (작성 예정)
> **핵심(= 묶음 ①):** A-1 카탈로그·A-2 메타데이터·A-3 용어집·C-3 계통(Lineage)은 **카탈로그/거버넌스 플랫폼 1개가 통째로 커버**하는 것이 시장 표준이다. 도구를 따로 사는 게 아니다. **세 가이드(A-1·A-2·A-3)가 모두 같은 벤더 집합으로 수렴**한다(A-2 §7.1·A-3 §6.1·§7.3에 명시). **변별점은 ① 네이티브 비즈니스 용어집·동의어 매핑(A-3) ② 컬럼 단위 계통(C-3)** 두 가지.
>
> **기능(capability)으로 비교 — 열이 곧 "무엇을 하느냐":**

| 솔루션 | 카테고리 | 자동 메타 수집 | 검색·탐색 | 용어집+동의어 | 계통(Lineage) | A-1 | A-2 | A-3 | C-3 | 핵심·출처 |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **Collibra** | 전용 거버넌스 | ✓ 커넥터 | ✓ | ✓ Glossary+동의어 | ✓ | ✓ | ✓ | ✓ | ✓ | 카탈로그·용어집·계통을 의미계층으로 묶은 엔터프라이즈 정본 ([catalog](https://www.collibra.com/products/data-catalog)) |
| **Alation** | 전용 카탈로그 | ✓ | ✓ | ✓ Glossary Hub | ✓ 컬럼단위 | ✓ | ✓ | ✓ | ✓ | 액티브 메타데이터 그래프·신뢰 신호 ([catalog](https://www.alation.com/product/data-catalog/)) |
| **Atlan** | 전용(액티브 메타) | ✓ | ✓ 최고 UX | ✓ Business Graph | ✓ 컬럼·OpenLineage | ✓ | ✓ | ✓ | ✓ | MCP/REST로 AI 연동, SaaS 운영부담 최저, 제조 레퍼런스 ([catalog](https://atlan.com/data-discovery-catalog/)) |
| **Microsoft Purview** | 플랫폼 내장(Azure) | ✓ 커넥터 | ✓ Copilot | ✓ Unified Catalog | ✓ | ✓ | ✓ | ✓ | ✓ | 멀티클라우드 페더레이션 거버넌스. **Azure shop이면 PoC 1순위**(A-1 §6) ([unified-catalog](https://learn.microsoft.com/en-us/purview/unified-catalog)) |
| **Databricks Unity Catalog** | 플랫폼 내장 | ✓ `information_schema` 자동 | ✓ | △ 시맨틱레이어 | ✓ 컬럼단위 자동 | ✓ | ✓ | △ | ✓ | 데이터·모델·에이전트 단일 거버넌스, 용어를 데이터와 같은 곳에서 ([UC](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)) |
| **OpenMetadata** | 오픈소스 | ✓ | ✓ | ✓ | ✓ 컬럼단위 | ✓ | ✓ | ✓ | ✓ | 단일 시맨틱 그래프·네이티브 MCP. 운영 0.5~1 FTE ([open-metadata.org](https://open-metadata.org/)) |
| **DataHub** | 오픈소스 | ✓ 활발한 커넥터 | ✓ | △ | ✓ 컬럼단위 | ✓ | ✓ | △ | ✓ | 실시간 메타데이터 그래프. 운영 0.5~1 FTE ([docs](https://docs.datahub.com/docs/introduction)) |
| **OpenLineage + Marquez** | 오픈소스(계통 표준) | △ | ✗ | ✗ | ✓ **계통 특화** | △ | ✓ | ✗ | ✓ | C-3 계통을 표준 이벤트로 자동 수집(위 제품들과 결합) ([OpenLineage](https://openlineage.io/)) |

> **A-1 추가 후보(전용 카탈로그·클라우드 네이티브 유형, A-1 §6.1 표):** [Informatica CDGC](https://www.informatica.com/products/data-governance/cloud-data-governance-and-catalog.html) · [IBM Knowledge Catalog](https://www.ibm.com/products/watsonx-data-intelligence/governance-catalog) (둘 다 Gartner MQ Leader) · [AWS Glue Data Catalog](https://aws.amazon.com/glue/features/) · [Google Knowledge Catalog (Dataplex)](https://docs.cloud.google.com/dataplex/docs/catalog-overview). **Gartner MQ for D&A Governance Platforms 2025–2026 Leaders = Collibra·Alation·Informatica·IBM(2026)·Atlan(2026 신규).** Snowflake/BigQuery/SAP는 `INFORMATION_SCHEMA` 시스템 카탈로그 제공 → 본 가이드 항목을 각 필드에 매핑만 하면 적용(A-1 §7.7·A-2 §7.4).

**기능별 동의어·약어 매핑(A-3 핵심):** 별도 엔진을 만드는 게 아니라 **거버넌스 솔루션의 동의어(Synonym) 매핑 기능**이 Glossary 데이터를 소비해 질의 확장(Query Expansion)·RAG 용어 정규화로 작동한다 — 우리 일은 그 매핑 데이터를 채우는 것(A-3 §7.4, 데이터 준비 관점). Collibra·Purview·Atlan이 네이티브 제공.

**선정 포인트:** 단일 클라우드면 플랫폼 내장(Unity Catalog·Purview)으로 충분. 멀티소스·전사 거버넌스면 전용(Collibra·Alation·Atlan). 폐쇄망·무료 시작은 **OpenMetadata 또는 DataHub + 계통은 OpenLineage** 조합. **A-3 용어집·동의어가 중요하면 Databricks·Snowflake(△)는 보완 필요.** 공통 평가축(A-1 §6.2 / A-2 §7.1): ① 우리 원천 커넥터 범위(SAP·MES·QMS·LIMS·SharePoint) ② 자동 메타 수집률 ③ 검색 UX ④ 권한·거버넌스 ⑤ 계통 연계 ⑥ AI 기능 ⑦ 계열사 확장성 + **운영형태(SaaS/온프렘·폐쇄망 적합성)**. **반드시 두산 실제 원천 2~3종 연결 PoC로 검증**(LabWare LIMS 등 커스텀 커넥터는 난이도 높음 — Purview 수동·DataHub 커스텀·Atlan API).

## B-1 — 데이터 전처리 (문서 파싱·추출) = 묶음 ②

> 📄 **주제 가이드(1층):** [B-1 데이터 전처리](../가이드%20작성/B-1%20데이터%20전처리/B-1%20데이터%20전처리.md) (작성됨 — §6.3 변환 도구·[Backup 6-A] 비교)
> **기능으로 비교 — 핵심 변별 기능 = ① 표 구조 보존 ② 온프레미스/로컬 ③ 한국어/OCR.** (표 구조 보존 ★ = B-1 가이드의 핵심 평가축; 복잡한 다중행 표를 깨뜨리지 않는가)

| 솔루션 | 카테고리 | 표 구조 보존 | 레이아웃 | 출력 | 온프렘/로컬 | 한국어·OCR | 핵심·출처 |
|---|---|:--:|:--:|---|:--:|:--:|---|
| **Docling** (IBM) | 오픈소스 | ★★★ | ★★★ | JSON(좌표)·MD·HTML | ✓ **로컬 실행** | △ | 복잡한 표 보존 + 사외 전송 제한 시 **1차 파서**(B-1 권장). 속도 느린 편 ([Docling](https://github.com/docling-project/docling)) |
| **Camelot / pdfplumber** | 오픈소스 | ★★★ **표 전용** | △ | 표(DataFrame) | ✓ 로컬 | ✗ | 까다로운 PDF **표만** 세밀 추출 — 위 파서의 보완용 ([Camelot](https://camelot-py.readthedocs.io) · [pdfplumber](https://github.com/jsvine/pdfplumber)) |
| **Unstructured** | 오픈소스+SaaS | ★★ | ★★ | JSON(요소·좌표) | ✓(OSS) | △ OCR | 다양한 포맷 통합·청킹·임베딩 ETL. 복잡한 표 컬럼 이동 오류 가능 ([unstructured.io](https://unstructured.io/)) |
| **LlamaParse** | 클라우드 API | ★★ | ★★★ | **LLM-ready MD**·JSON | ✗ 인터넷 필수 | △ | 빠른 처리·RAG용 마크다운. 크레딧 과금 ([docs](https://developers.llamaindex.ai/python/framework/llama_cloud/llama_parse/)) |
| **Azure AI Document Intelligence** | 클라우드(Azure) | ★★★ | ★★★ | JSON(좌표·신뢰도) | ✗ | ✓ **한국어·커스텀모델** | MS 인프라면 1순위. 가격 PoC 확인 ([overview](https://azure.microsoft.com/ko-kr/products/ai-services/ai-document-intelligence)) |
| **Google Document AI** | 클라우드(GCP) | ★★★ | ★★★ | JSON(좌표·신뢰도) | ✗ | ✓ 다국어(한국어) | GCP 인프라면 선택. 언어범위 공식 확인 ([Document AI](https://cloud.google.com/document-ai)) |
| **AWS Textract** | 클라우드(AWS) | ★★★ | ★★★ | JSON(블록·좌표) | ✗ | △ 범위 확인 | AWS 인프라면 선택 ([Textract](https://aws.amazon.com/textract/)) |
| **Upstage Document Parse** (한국) | 전용(국내) | ★★★ | ★★★ | RAG 구조화 출력 | △(국내 벤더) | ✓ **한글 강점** | 국내 벤더, RAG용 구조화 ([product](https://www.upstage.ai/products/document-parse)) |
| **Apache Tika** | 오픈소스 | △ | △ | 텍스트·메타 | ✓ 로컬 | △ | 1,000+ 포맷 텍스트·메타 추출(범용) ([Tika](https://tika.apache.org)) |

> **포맷별 보조 라이브러리(B-1 References):** PDF=PyMuPDF·Tabula-py / Office=python-pptx·openpyxl·python-docx·Mammoth / HWP=pyhwp(한계) / 이미지·스캔 OCR=Tesseract·pytesseract / RAG 적재 sink=pgvector·Milvus·Pinecone·Chroma·Elasticsearch·OpenSearch / 데이터셋 버전=DVC·lakeFS.

**선정 포인트:** **표 복잡도**가 높으면 전용 표 파서(Camelot·pdfplumber)로 보완, **데이터 민감도**가 높아 사외 전송 불가면 로컬(Docling·Tika), **다국어·스캔본**은 OCR 강한 클라우드, **기존 인프라**(MS=Azure DI / AWS=Textract / GCP=Document AI)에 맞춘다. 망분리면 OSS·국내(Upstage). RAG 적재 목표면 마크다운/JSON + 청킹 내장 여부. (가격·한국어 범위는 변동 → PoC/공식 문서 확인. 벤치마크 예: [Procycons PDF 추출 비교](https://procycons.com/en/blogs/pdf-data-extraction-benchmark/))

## B-2 — 데이터 해설·주석 (라벨링/Annotation) = 묶음 ③

> 📄 **주제 가이드(1층):** [B-2 데이터 해설·주석](../가이드%20작성/B-2%20데이터%20해설·주석/B-2%20데이터%20해설·주석.md) (작성됨 — 솔루션은 [Backup 6-B] 비교)
> **기능으로 비교 — 핵심 변별 기능 = ① AI 1차 라벨(pre-label) ② 데이터 유형(이미지/텍스트/음성) ③ 온프레미스/로컬 ④ 약지도(프로그래매틱).**

| 솔루션 | 카테고리 | AI 1차 라벨 | 지원 데이터 유형 | 온프렘/로컬 | 핵심·출처 |
|---|---|:--:|---|:--:|---|
| **Label Studio** (HumanSignal) | OSS(Apache-2.0)+기업판 | ✓ | **텍스트·이미지·음성·시계열** 폭넓음 | ✓ 셀프호스트 | 다중 유형 라벨링 범용 ([labelstud.io](https://labelstud.io/)) |
| **CVAT** | OSS(MIT)+클라우드 | ✓ AI 보조·QA | 비전(이미지·영상·3D) | ✓ 완전 셀프호스트 | 비전 라벨링 + AI 보조·QA ([github](https://github.com/cvat-ai/cvat)) |
| **Snorkel Flow** | 상용(프로그래매틱) | ✓ 대량 초벌 | 텍스트·문서(약지도) | △ 계약 확인 | **약지도/프로그래매틱** — 라벨링 함수로 대량 생성 ([snorkel.ai](https://snorkel.ai/)) |
| **Labelbox** | 상용(SaaS) | ✓ | 멀티모달 | 미확인(계약) | 대규모 협업·모델 평가 ([Labelbox](https://labelbox.com/)) |
| **Scale AI** (Data Engine) | 상용(SaaS) | ✓ | 멀티모달 | ✗(SaaS) | 대규모 인력+AI 큐레이션 ([Scale](https://scale.com/data-engine)) |
| **Roboflow** | 상용(코어) | ✓ | 컴퓨터 비전 | △ | 비전 올인원·포맷 변환·증강 ([Roboflow](https://roboflow.com/)) |
| **Prodigy** (Explosion) | 상용 | ✓ 능동학습 | NLP(텍스트) | ✓ **로컬 실행** | 스크립트형·spaCy 통합·로컬 ([Prodigy](https://prodi.gy/)) |
| **SageMaker Ground Truth** (AWS) | 상용(AWS) | ✓ | 멀티모달·3D | ✗(AWS) | 매니지드 인력+ML 라벨링 ([groundtruth](https://aws.amazon.com/sagemaker/ai/groundtruth/)) |

**보조 기능 도구:** **SAM 2**(Meta, Apache-2.0) = 이미지·영상 **자동 분할 프리라벨**(AI 1차 라벨 엔진) ([SAM 2](https://ai.meta.com/research/sam2/)) · **Cleanlab** = **라벨 오류 자동 탐지**(품질 보정) ([Cleanlab](https://cleanlab.ai/)) · 데이터셋 버전 = DVC·lakeFS.

> **⚠️ IAA(평가자 간 일치도)·합의·검수 워크플로는 "제품 기능"이 아니라 방법론이다** — B-2 가이드는 Cohen's κ / Fleiss' κ / Krippendorff's α 측정과 HITL(확신도 기반 라우팅)을 *작성 방법*으로 다룬다. 도구는 이를 담는 그릇일 뿐.

**선정 포인트:** **데이터 유형 × 자동화 수준**으로 고른다 — 비전이면 CVAT·Roboflow, 텍스트/NLP면 Label Studio·Prodigy, 약지도 대량이면 Snorkel. **공정·품질 데이터를 외부 반출 못 하면** OSS 셀프호스트(Label Studio·CVAT)·로컬(Prodigy)로 좁혀지고, SaaS(Labelbox·Scale·Ground Truth)는 온프렘 가부를 **계약으로 확인**한다. AI 1차 라벨은 사실상 전 제품 지원하나 정확도는 PoC로 검증.

## B-3 — 온톨로지·지식그래프 = 묶음 ④

> 📄 **주제 가이드(1층):** [B-3 온톨로지](../가이드%20작성/B-3%20온톨로지/B-3%20온톨로지.md) (작성됨 — 형식 선정·아키텍처 방법론 포함)
> **★ 1차 분기 = 데이터 모델(전환 비용 최대, 되돌리기 어려움):**
> - **LPG(속성 그래프) 선택** = 긴 경로·다중 홉(6홉+) 탐색·실시간 패턴·GraphRAG, 외부 연계가 사내(MES·ERP·QMS) 위주, 일반 개발자(SQL/NoSQL), **탐색 속도 우선**. → 관계를 일급 엣지로 저장해 깊은 홉에도 조인 폭증 없음.
> - **RDF/OWL 선택** = OWL 추론·의미적 어휘 통합이 핵심, 외부(공급망 파트너·표준기관)와 데이터 교환, 시맨틱웹/OWL 전문가 확보, **의미 정확성·표준 준수 우선**. → 깊은 경로에선 트리플 조인이 폭증할 수 있음.
> - **Amazon Neptune만 둘 다.** (Hybrid: 적재 시 RDF 추론 → 쿼리 시 LPG 탐색)
> - 🏭 **두산 프로젝트 결정(커니 수행):** 원인 탐색이 "불량→공정→설비→부품→로트→공급사" 6홉+ → **LPG 채택, RDF 배제**(B-3 §7.2).

| 솔루션 | 모델 | 카테고리 | 추론 | 질의어 | 온프렘/배포 | 핵심·출처 |
|---|---|---|:--:|---|---|---|
| **Neo4j** | LPG | 전용(Community OSS) | △ OWL 사전적재 약함 | Cypher/GQL | 자체+AuraDB | Cypher·벡터·GraphRAG·LLM KG Builder·GDS·NeoSemantics(RDF 브릿지) ([use-case](https://neo4j.com/use-cases/knowledge-graph/)) |
| **Amazon Neptune** | **LPG+RDF** | 클라우드 내장 | ✓(RDF 모드) | Gremlin·openCypher·SPARQL | AWS 관리형·서버리스 | 한 서비스에 세 질의어·두 모델 — "둘 다 필요" 시 ([userguide](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)) |
| **TigerGraph** | LPG(병렬) | 전용 | ✗ 네이티브 온톨로지 없음 | GSQL(독자) | 자체+클라우드 | 심층 분석·연산 집약 탐색 ([TigerGraph](https://www.tigergraph.com)) |
| **Memgraph** | LPG(인메모리) | 전용 | ✗ OWL 없음 | openCypher | 자체(인메모리) | 실시간 IoT 스트리밍·Kafka ([Memgraph](https://memgraph.com)) |
| **Ontotext GraphDB** | RDF | 전용 | ✓ **OWL QL/RL·사전적재·SHACL** | SPARQL 1.1 | 자체+Cloud | 시맨틱/온톨로지 앱, 안정 데이터 사전 추론 ([GraphDB](https://graphdb.ontotext.com)) |
| **Stardog** | RDF | 전용 | ✓ **전 OWL·질의 시 추론·가상화** | SPARQL 1.1 | 자체+클라우드 | 사일로 통합 KG, 실시간 데이터 질의 추론 ([Stardog](https://www.stardog.com/platform/)) |
| **RDFox** (삼성) | RDF | 전용(인메모리) | ✓ 증분 추론·Datalog 룰 | SPARQL | 자체(인메모리) | 고속 증분 추론 ([rdfox](https://www.oxfordsemantic.tech/rdfox)) |
| **Apache Jena (+TDB)** | RDF/OWL | 오픈소스(무료) | ✓ Pellet/HermiT·SHACL | SPARQL 1.1 | 자체 | 예산형 PoC·연구·RDF 탐색 ([Jena](https://jena.apache.org)) |
| **Protégé** | 편집기(OWL) | 오픈소스 | (추론기 연동) | — | 데스크톱·WebProtégé | 온톨로지 **저작**(개념·관계 수기 설계) ([Protégé](https://protege.stanford.edu)) |
| **PoolParty / TopBraid EDG** | 편집기·거버넌스 | 상용 | — | — | 엔터프라이즈 | 온톨로지 편집·거버넌스 GUI(상용 단계) ([PoolParty](https://www.poolparty.biz/ontology-management) · [TopBraid EDG](https://www.topquadrant.com/products/topbraid-edg/)) |

> **표준·프레임워크:** **IOF**(Industrial Ontologies Foundry, NIST+산업) = 제조·유지보수·공급망 표준 참조 온톨로지 — IOF Core의 `Process`·`Equipment`·`MaterialArtifact`가 B-3 7엔티티와 대응 ([IOF](https://github.com/iofoundry/ontology)) · **BFO**(ISO/IEC 21838-2) 최상위 온톨로지 · **OWL 2**(W3C) · **GQL**(ISO/IEC 39075, 2024) · **SHACL**(검증). 두산 권고 = **IOF 어휘 참조 + 기업 맞춤 온톨로지로 시작**, 외부 연계 시 점진 정렬.

**선정 포인트(권장 LPG 경로):** PoC = **Neo4j Community(무료)** → 운영 = **Amazon Neptune(AWS)** 또는 **Neo4j AuraDB** → 실시간 대량 = **Memgraph(Kafka)** → 추론 필요 시 = **GraphDB Free(PoC)→Stardog**. 편집·저작은 **Protégé/WebProtégé**, 엔터프라이즈 거버넌스는 **PoolParty/TopBraid EDG**(PoC 가치 확인 후). **추론(인과·논리 도출)이 핵심이면 RDF(GraphDB·Stardog·RDFox)** 또는 하이브리드, 관계 적재·GraphRAG만이면 LPG. 온프레미스 진단(B-3 §7.8): 내부망 격리 배포 가부·노드/트리플 단위 접근제어·벤더 잠금(openCypher/GQL 호환)·관리형 vs 자체호스팅 TCO.

## C-1 — 데이터 Observability

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **Monte Carlo** | 전용 | ML 기반 데이터+AI 관측 선두, 인시던트/RCA ([platform](https://www.montecarlodata.com/)) |
| **Sifflet / Bigeye** | 전용 | 계보 중심·필드 단위, 동적 임계값 ([Sifflet](https://www.siffletdata.com/)) |
| **Anomalo** | 전용 | 규칙 없이 데이터 내용을 보는 무규칙 ML ([data-observability](https://www.anomalo.com/)) |
| **Soda** | OSS+상용 | SodaCL(YAML) 규칙 + ML 이상탐지 하이브리드 ([soda.io](https://www.soda.io/)) |
| **Acceldata** | 전용 | 데이터·파이프라인·인프라·비용까지 ([acceldata](https://www.acceldata.io/)) |

**선정 포인트:** OSS는 사실상 Soda Core 단독. 컬럼 단위 계보 연계가 강한 곳(Monte Carlo·Sifflet)이 RCA에 유리. C-2(합·불 판정)와 경계를 흐리지 말 것 — C-1은 "지금 정상으로 흐르나".

## C-2 — 데이터 품질 게이트

**품질 (합·불 판정):**

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **Great Expectations** | 오픈소스 | "기대값=코드" 검증 표준 ([greatexpectations.io](https://greatexpectations.io/)) |
| **Soda Core** | 오픈소스+SaaS | YAML 선언형 체크·데이터 계약 ([github](https://github.com/sodadata/soda-core)) |
| **Informatica / Collibra / Ataccama / Qlik Talend** | 엔터프라이즈 | 프로파일링→규칙→스코어카드→DQ 차원 ([Ataccama](https://www.ataccama.com/platform/data-quality)) |

**선정 포인트:** OSS는 Great Expectations·Soda Core, 엔터프라이즈는 프로파일링→규칙→스코어카드 일체형(Informatica·Collibra·Ataccama). **접근 권한 통제(Immuta·Ranger·Unity Catalog 등)는 [F-4 AI 데이터 권한 보안](#f-4--ai-데이터-권한-보안-접근통제--비식별)으로 이관** — 투입 직전 품질 게이트와 권한 게이트를 함께 운영한다.

## D-1 — Physical 데이터 (IoT·시계열)

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **AVEVA PI System** | 전용 historian | 자산 모델로 설비ID·단위·계층 표준화(공정 표준) ([PI](https://www.aveva.com/en/products/aveva-pi-system/)) |
| **Ignition** | 전용 SCADA/IIoT | OPC UA·MQTT 수집, SQL DB를 historian화 ([scada](https://inductiveautomation.com/scada-software/)) |
| **InfluxDB / TimescaleDB / Apache IoTDB** | OSS 시계열 DB | 고속·고압축 시계열 적재 ([InfluxDB](https://www.influxdata.com/products/influxdb-overview/)) |
| **AWS IoT SiteWise·IoT Core / Azure IoT Hub** | 클라우드 내장 | 수집~저장을 룰 액션으로 ([SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/concept-overview.html)) |
| **OPC UA / MQTT Sparkplug B** | 표준·프로토콜 | **표준화 계층** — 데이터의 의미(설비·단위·시간) 정의 ([OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/)) |

**선정 포인트:** ★ **표준화 계층(OPC UA·Sparkplug)이 핵심.** 안 맞추면 시계열만 쌓이고 AI가 해석 못 한다. 국내 장치산업은 AVEVA PI가 전통 표준, 이산제조는 Ignition 확산.

## D-2 — API/Tool 연계 데이터 (명세 + 레지스트리)

> **2층 구도:** ① 명세 **형식 표준** + ② 그 명세를 담는 **레지스트리/카탈로그**.

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **MCP (Model Context Protocol)** | 표준·프로토콜 | 에이전트용 Tool 명세 표준(이름·설명·입출력 스키마·발견) ([modelcontextprotocol.io](https://modelcontextprotocol.io)) |
| **OpenAPI / JSON Schema** | 표준 | REST API 명세 + 입출력 규격 공통 어휘 ([OpenAPI](https://www.openapis.org/)) |
| **공식 MCP Registry** | OSS 레지스트리 | MCP 서버 명세 등록·검색(단일 정본) ([registry](https://registry.modelcontextprotocol.io/)) |
| **SwaggerHub / Postman / Backstage** | 전용/OSS | OpenAPI 명세 중앙 저장·버전관리·카탈로그화 ([SwaggerHub](https://swagger.io/tools/swaggerhub/)) |

**선정 포인트:** 현실 적재 순서 = **사내 API의 OpenAPI 명세 정비 → MCP Tool 명세로 변환·등록.** 본질은 description을 명확히 쓰고 입출력 스키마를 엄밀히 정의하는 **데이터 품질 문제**(실행 프레임워크와 무관).

## D-3 — Prompt/Harness 자산화

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **Langfuse** | **오픈소스(MIT)**+SaaS | 셀프호스트 가능, 버전·레이블·평가 ([langfuse.com](https://langfuse.com/docs/prompts)) |
| **Agenta / Helicone** | 오픈소스+SaaS | VPC 셀프호스트, 도메인 전문가용 편집 ([agenta](https://agenta.ai/)) |
| **LangSmith** | 상용(엔터 셀프호스트) | Git식 커밋 해시·승격·플레이그라운드 ([docs](https://docs.langchain.com/langsmith/prompt-engineering)) |
| **PromptLayer / Vellum / Braintrust** | 상용 SaaS | 프롬프트 CMS·환경 격리·평가 내장 ([PromptLayer](https://www.promptlayer.com/)) |

**선정 포인트:** ★ **셀프호스트 가능 여부가 제조 대기업엔 결정적** — 사내 프롬프트 자산을 외부 SaaS에 두기 어려우면 Langfuse·Agenta·Helicone(OSS). (Humanloop 종료 주의)

## E-1 — 데이터 Product화

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **dbt Mesh / Semantic Layer** | 전용(오픈코어) | 모델 계약·버전·오너 — 제품의 "스펙·계약" ([mesh](https://docs.getdbt.com/best-practices/how-we-mesh/mesh-1-intro)) |
| **Databricks Marketplace / Delta Sharing** | 플랫폼 내장 | 복사 없는 라이브 공유·마켓플레이스 ([delta-sharing](https://www.databricks.com/product/delta-sharing)) |
| **Snowflake Marketplace** | 플랫폼 내장 | 제로카피 공유·3,400+ 리스팅 ([marketplace](https://www.snowflake.com/en/product/features/marketplace/)) |
| **Collibra / Atlan Data Marketplace** | 전용(거버넌스) | 카탈로그 위 발견→요청→접근 셀프서비스 ([Collibra](https://www.collibra.com/products/data-marketplace)) |

**선정 포인트:** 공학 중심(dbt·플랫폼 공유)과 거버넌스 중심(Collibra·Atlan) 두 계층을 함께 써야 "스펙+오너+SLA+소비방식"이 완성. OSS엔 마켓플레이스·SLA·계약이 사실상 부재(최대 공백).

## E-2 — 합성데이터

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **MOSTLY AI / Syntho** | 전용 | 정형·다중테이블·시계열 고정밀 ([mostly.ai](https://mostly.ai/)) |
| **Tonic.ai / K2view** | 전용 | 운영데이터 비식별+합성(테스트데이터) ([tonic.ai](https://www.tonic.ai/)) |
| **SDV (Synthetic Data Vault)** | 오픈소스(BSL 주의) | 다중모델+품질/프라이버시 평가 내장 ([sdv.dev](https://docs.sdv.dev/sdv)) |
| **NVIDIA Omniverse Replicator** | 플랫폼 내장 | **이미지/비전** 합성(검사·로보틱스) ([docs](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html)) |

**선정 포인트:** ★ **정형·시계열과 이미지/비전은 별도 시장** — 한 도구로 다 안 됨. 제조 검사 이미지 부족이면 Omniverse, 비식별 동인이면 Tonic·Syntho, PoC면 OSS(SDV). (Gretel→NVIDIA, Hazy→SAS 흡수 확인)

## E-3 — AI 평가 데이터

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **Ragas** | 오픈소스 | RAG 평가(faithfulness·context recall) 표준 ([docs](https://docs.ragas.io/)) |
| **DeepEval** | 오픈소스 | "Pytest처럼" 단위테스트식·G-Eval 커스텀 기준 ([deepeval](https://deepeval.com/)) |
| **Langfuse / LangSmith** | OSS/상용 | Datasets·Experiments·Evaluators·Scores ([Langfuse](https://langfuse.com/docs/evaluation/overview)) |
| **Braintrust / Promptfoo** | 전용/OSS | 데이터셋 버전관리·회귀 비교 ([Braintrust](https://www.braintrust.dev/)) |

**선정 포인트:** ★ **정답셋(Gold Set) 관리가 본체** — 현업이 준비할 자산은 도구가 아니라 데이터(질문·정답·합격기준)다. RAG=Ragas, 커스텀 기준=DeepEval.

## E-4 — 데이터 Feedback Loop

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **Langfuse** | 오픈소스 | 트레이스에 Scores 부착·Annotation Queue ([user-feedback](https://langfuse.com/docs/observability/features/user-feedback)) |
| **LangSmith** | 상용 | 피드백→검수큐→웹훅 라우팅 자동화 규칙 ([rules](https://docs.langchain.com/langsmith/observability)) |
| **Arize Phoenix / Helicone** | 오픈소스 | 스팬 annotation·가벼운 피드백 API ([Phoenix](https://arize.com/docs/phoenix)) |
| **Jira 등 이슈 트래커** | 라우팅 목적지 | 분류된 피드백을 "고칠 일감"으로(웹훅 경유) |

**선정 포인트:** 표준 패턴 = 명시 피드백(👍👎)을 트레이스에 점수로 부착 + 자동화 규칙으로 원인 주제 라우팅. Jira 연동은 대부분 전용 커넥터가 아니라 **웹훅 경유**.

## F-1 — DataOps (오케스트레이션)

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **Apache Airflow** | 오픈소스 | DAG 오케스트레이션의 사실상 표준 ([airflow](https://airflow.apache.org/)) |
| **Dagster / Prefect** | 오픈소스 | 자산 중심(Dagster)·경량 파이썬(Prefect) ([dagster](https://dagster.io/)) |
| **Astronomer** | 매니지드 Airflow | Airflow 운영 위임·CI/CD ([astronomer](https://www.astronomer.io/)) |
| **Lakeflow / ADF / AWS Step Functions** | 클라우드 내장 | 각 생태계 내장 파이프라인 ([Lakeflow](https://docs.databricks.com/aws/en/ldp/)) |

**선정 포인트:** 이식성·멀티클라우드면 OSS, 운영부담↓면 클라우드 내장, Airflow는 쓰되 운영 위임이면 매니지드. (dbt는 오케스트레이터 아닌 변환 도구 — Airflow가 호출)

## F-2 — 데이터 생애주기 관리

> **역할 2층:** "정책 엔진(언제 전환·폐기)" + "스토리지 등급/자동티어링(데이터가 사는 곳)"은 별개. 둘을 조합해야 보존·티어링·아카이브·폐기 4축을 덮는다.

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **S3 Lifecycle + Glacier / S3 Intelligent-Tiering** | 클라우드 내장 | 규칙 엔진(전환·만료) + 자동 티어링 ([S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)) |
| **Azure Blob 수명주기 / GCS Autoclass** | 클라우드 내장 | 나이·접근 조건 기반 자동 전환·삭제 ([Azure](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)) |
| **Informatica ILM** | 전용 | 운영 DB·레거시 앱 아카이브·폐기 ([ILM](https://www.informatica.com/services-and-training/glossary-of-terms/information-lifecycle-management-definition.html)) |
| **Apache Iceberg (snapshot expiration)** | 오픈소스 | 레이크하우스 테이블 수명·time-travel ([iceberg](https://iceberg.apache.org/)) |

**선정 포인트:** 폐기는 사실상 Lifecycle의 expiration/delete에 집중. 거버넌스 도구(Collibra)는 보존정책 "관리"만, 실행은 스토리지가 한다.

## F-3 — 데이터 디지털화 (OCR·STT)

| 솔루션 | 카테고리 | OCR/필기/STT (출처) |
|---|---|---|
| **Naver CLOVA OCR** (한국) | 클라우드(국내) | OCR✓·한글 필기✓ — 국내 한글 강점 ([ncloud](https://www.ncloud.com/product/aiService/ocr)) |
| **Upstage Document Parse** (한국) | 전용(국내) | OCR✓·레이아웃✓·RAG 구조화 ([upstage](https://www.upstage.ai/products/document-parse)) |
| **ABBYY / Google Document AI / Azure DI / AWS Textract** | 전용·클라우드 | OCR✓·필기✓·레이아웃✓ ([Document AI](https://cloud.google.com/document-ai)) |
| **Tesseract / PaddleOCR** | 오픈소스 | OCR✓(인쇄 위주)·온프렘 ([Tesseract](https://github.com/tesseract-ocr/tesseract)) |
| **OpenAI Whisper / CLOVA Speech** | OSS/클라우드 | **STT(음성→텍스트)** ([Whisper](https://github.com/openai/whisper)) |

**선정 포인트:** ★ **STT 공백 주의** — 문서 OCR 도구는 음성을 못 한다. 한글 손글씨·도면 주석·점검표엔 국내 특화(CLOVA·Upstage)가 결정적. 음성은 Whisper/CLOVA Speech 별도.

## F-4 — AI 데이터 권한 보안 (접근통제 + 비식별)

> **두 축:** ① **접근 권한 통제** — 누가 어떤 데이터를 쓸 수 있는지 정한다. ② **비식별** — 민감정보를 가려 데이터 자체를 안전하게 바꾼다(발견 → 변환 → 합성).

**접근 권한 통제 (누가 쓸 수 있나):**

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **Immuta / Privacera** | 전용 | 멀티플랫폼 접근 통제·동적 마스킹·행/열/셀 통제 ([Immuta](https://www.immuta.com/product/data-access-governance/)) |
| **Unity Catalog / Snowflake Horizon / AWS Lake Formation** | 플랫폼 내장 | 역할·태그 기반 행/열 통제 ([Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html)) |
| **Apache Ranger** | 오픈소스 | 빅데이터 표준 권한·감사(상용 도구의 기반) ([ranger](https://ranger.apache.org/)) |

단일 클라우드면 플랫폼 내장으로 충분. **여러 플랫폼을 한 정책으로 가로질러** 통제하려면 전용(Immuta·Privacera). 추세는 역할·태그 기반 통제.

**비식별 (데이터 변환):**

| 솔루션 | 카테고리 | 역할 (출처) |
|---|---|---|
| **Microsoft Presidio** | 오픈소스 | 탐지+마스킹+가명화(텍스트·이미지) 무료 SDK ([presidio](https://microsoft.github.io/presidio/)) |
| **Google Cloud Sensitive Data Protection (DLP)** | 클라우드 내장 | 탐지~가명화·토큰화·FPE 한 서비스 ([DLP](https://cloud.google.com/security/products/sensitive-data-protection)) |
| **Protegrity / Skyflow** | 전용 | 토큰화·볼트 중심 비식별 변환 ([Protegrity](https://www.protegrity.com/)) |
| **Amazon Macie / BigID** | 클라우드/전용 | **탐지·분류 전용**(변환은 짝지어야) ([Macie](https://aws.amazon.com/macie/)) |
| **Tonic.ai / Gretel** | 전용 | 비식별+합성으로 안전 데이터화 ([Tonic](https://www.tonic.ai/)) |
| **파수(Fasoo)** (한국) / **ARX** (OSS) | 전용/OSS | 국내 레퍼런스 / k-익명성 ([ARX](https://arx.deidentifier.org/)) |

**선정 포인트:** 접근 권한은 단일 클라우드면 내장(Unity Catalog·Horizon·Lake Formation), 멀티플랫폼이면 전용(Immuta·Privacera). 비식별은 **Macie·BigID가 발견 전용** — 단독으로 못 채움, 변환 도구와 짝지어야. Presidio(OSS)는 강력하나 "모든 PII 탐지 보장 안 됨"을 문서가 명시 → 사람 검수 병행.

---

# Part B. 묶음(플랫폼) × 20개 주제 커버리지 매트릭스

> "우리가 이 플랫폼을 깔면 어디까지 한 번에 되나"를 한눈에. ✓ 네이티브 강함 / △ 부분·외부 보강 / ✗ 없음.

| 주제 | Databricks | MS/Azure | AWS | Google Cloud | Snowflake | OSS 조합 | Collibra/Alation |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| A-1 카탈로그 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-2 메타데이터 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-3 용어집 | △ | ✓ | ✓ | ✓ | △ | ✓ | ✓ |
| B-1 전처리 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| B-2 라벨링 | △ | ✓ | ✓ | ✗ | △ | ✓ | ✗ |
| B-3 온톨로지 | △ | △ | ✓ | △ | △ | ✓ | ✗ |
| C-1 Observability | ✓ | ✓ | △ | △ | ✓ | ✓ | ✓ |
| C-2 품질 게이트 | ✓ | ✓ | ✓ | △ | ✓ | △ | ✓ |
| C-3 계통 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| D-1 Physical/IoT | ✓ | ✓ | ✓ | △ | ✓ | ✓ | ✗ |
| D-2 API/Tool 명세 | ✓ | △ | △ | △ | △ | ✓ | △ |
| D-3 Prompt 자산화 | ✓ | ✓ | ✓ | ✓ | △ | ✓ | △ |
| E-1 Product화 | ✓ | ✓ | ✓ | ✓ | ✓ | △ | ✓ |
| E-2 합성데이터 | △ | △ | △ | △ | ✓ | △ | ✗ |
| E-3 AI 평가 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| E-4 Feedback Loop | ✓ | ✓ | △ | △ | △ | ✓ | △ |
| F-1 DataOps | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | △ |
| F-2 생애주기 | △ | ✓ | ✓ | ✓ | ✓ | △ | ✓ |
| F-3 디지털화/OCR | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| F-4 권한·보안 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | △ |

**대표 커버 기능(예시):** Databricks=Unity Catalog·Lakeflow·Mosaic AI / Azure=Purview·Document Intelligence·AI Foundry / AWS=Glue+DataZone·Textract·Bedrock·Neptune / Google=Dataplex Knowledge Catalog·Document AI·Vertex AI / Snowflake=Horizon·Cortex·합성데이터 / OSS=OpenMetadata+GX+Label Studio+Neo4j+Airflow+Presidio / Collibra·Alation=거버넌스 계층 전문.

---

# Part C. 묶음 스택 비교·선정 가이드

## 스택별 성격 한 줄 요약

| 스택 | 성격 | 강점 주제군 | 약점(외부 보강) |
|---|---|---|---|
| **Databricks** | 레이크하우스 단일 거버넌스 | A·C·F(카탈로그·계통·품질·보안)+D-2/D-3/E-3/E-4(Mosaic AI) | B-3 온톨로지·B-2 라벨링(Labelbox 연동)·E-2 범용 합성 |
| **MS/Azure** | 수직 통합 엔터프라이즈 | 거버넌스(Purview 단일)·문서AI(B-1/F-3)·시계열(D-1) | B-3 온톨로지·E-2 합성·D-2 명세 카탈로그화 |
| **AWS** | 폭이 가장 넓은 빌딩블록 | 거의 전 주제 1급 서비스(라벨링·그래프·OCR·PII·IoT) | C-1 Observability·E-2·E-4·D-2(단일 제품 부재) |
| **Google Cloud** | 거버넌스+생성형AI 응집 | Dataplex 거버넌스·문서AI·비식별·평가 | **B-2 라벨링 폐기**·D-1 IoT Core 폐기·E-2 파트너 의존 |
| **Snowflake** | SQL 한 곳에서 거버넌스+AI | 카탈로그·계통·품질·보안·**합성데이터 네이티브**·시계열 | B-2 라벨링·B-3 그래프·A-3 용어집(2026 H2)·D-3 |
| **OSS 조합** | 비용 0·종속 회피 | 14/20 성숙 도구 존재(✗ 없음) | **통합·거버넌스·마켓플레이스·SLA**(A-3·C-2 게이트·E-1·F-2) |
| **Collibra/Alation** | 거버넌스 계층 전문 | A군·C-3·C-2·E-1·F-2·AI 거버넌스 | **처리계 전무**(B-2·D-1·E-2·F-3 ✗), 데이터를 변환 안 함 |

## 핵심 판단

> ⭐ **A·B 6개 주제 요약(이번 갱신 범위):** 4개 묶음으로 갈린다 — **묶음 ① 거버넌스·카탈로그 플랫폼 1개가 A-1·A-2·A-3을 통째로** 덮고(따로 안 산다), **묶음 ② 전처리·③ 라벨링·④ 온톨로지는 각각 전용/OSS 도구**를 따로 붙인다(거버넌스 플랫폼엔 이 셋이 비어 있다). 즉 "**거버넌스 플랫폼 1개 + B-1·B-2·B-3용 전용 도구 3개**"가 자연스러운 조합이다.

1. **A·C·F(거버넌스) 계열은 어느 대형 플랫폼이든 강하다.** 카탈로그·메타데이터·용어집·계통·품질·보안은 평준화됐다 — A-1·A-2·A-3은 한 제품(묶음 ①)으로 함께 해결된다. 여기서 스택을 가르는 건 "이미 어느 클라우드를 쓰는가"다. 단일 클라우드면 그 내장 거버넌스로 시작하는 게 합리적. **단 A-3 네이티브 용어집·동의어 매핑은 Databricks·Snowflake가 약하므로(△)** 용어집이 중요하면 전용(Collibra·Purview·Atlan)을 본다.

2. **B(처리) 계열에서 갈린다 — 한 묶음으로 B-1·B-2·B-3을 다 못 한다.** 전처리(B-2 ②)·라벨링(B-2 ③)·온톨로지(B-3 ④)는 서로 다른 시장이고 **어느 통합 거버넌스 플랫폼도 약하다** — 사실상 전용/OSS 도구를 붙여야 한다(Docling·Label Studio·Neo4j). 거버넌스 플랫폼(Collibra/Alation)은 이 영역이 통째로 비어 있다. 이 셋 안에서도 서로 안 겹친다(파싱 ≠ 라벨링 ≠ 그래프) — B-3 안에서만 Amazon Neptune이 LPG·RDF 두 모델을 함께 덮는다.

3. **제조업에 특히 중요한 D-1·F-3·F-4는 누가 메우나.**
   - **D-1(설비·IoT):** 통합 플랫폼보다 **산업 historian(AVEVA PI·Ignition) + 표준(OPC UA·Sparkplug)**이 본질. 클라우드는 적재·분석을 보조. (Google은 IoT Core 폐기로 갭)
   - **F-3(디지털화):** 한글 손글씨·도면엔 **국내 특화(CLOVA·Upstage)**가 글로벌 OCR보다 유리할 수 있음. 음성은 STT 별도.
   - **F-4(권한·비식별):** 접근 권한은 Unity Catalog·Immuta·Ranger, 비식별은 플랫폼 내장 마스킹(Snowflake·DLP)으로 기본은 되나, 활용성 보존·재식별 점검엔 전용(Presidio·Tonic)·국내(파수) 보강.

4. **현실적 추천 = "거버넌스 베이스 1개 + 처리계 전용 도구 + 산업 historian".**
   - 두산처럼 계열사별 시스템이 흩어진 환경이면 **멀티소스 거버넌스(Collibra/Alation/Atlan 또는 OSS OpenMetadata)**를 베이스로, 클라우드는 계열사별 사정에 맞추고, **D-1은 PI/Ignition+표준, B-2·B-3·E-2·F-3는 전용/국내 도구**를 붙이는 best-of-breed가 자연스럽다.
   - 단일 클라우드로 수렴 가능한 신규 영역은 그 플랫폼 내장(Databricks/Azure/Snowflake)으로 묶어 운영 부담을 줄인다.

---

## 참고자료 (References) — 플랫폼 공식 문서 허브

- Databricks Unity Catalog — https://www.databricks.com/product/unity-catalog
- Microsoft Purview — https://learn.microsoft.com/en-us/purview/
- AWS (Glue Data Catalog · DataZone) — https://docs.aws.amazon.com/glue/ · https://aws.amazon.com/datazone/
- Google Cloud Dataplex — https://docs.cloud.google.com/dataplex/docs/introduction
- Snowflake Horizon — https://docs.snowflake.com/en/user-guide/snowflake-horizon
- OpenMetadata — https://open-metadata.org/ · DataHub — https://datahub.com/ · OpenLineage — https://openlineage.io/
- Collibra — https://www.collibra.com/ · Alation — https://www.alation.com/ · Atlan — https://atlan.com/

**A·B 6개 주제 — 묶음별 제품 공식 문서 (이번 갱신에서 추가):**
- 묶음 ① 거버넌스·카탈로그: Informatica CDGC — https://www.informatica.com/products/data-governance/cloud-data-governance-and-catalog.html · IBM Knowledge Catalog — https://www.ibm.com/products/watsonx-data-intelligence/governance-catalog
- 묶음 ② 문서 전처리: Docling — https://github.com/docling-project/docling · Unstructured — https://unstructured.io/ · LlamaParse — https://developers.llamaindex.ai/python/framework/llama_cloud/llama_parse/ · Camelot — https://camelot-py.readthedocs.io · pdfplumber — https://github.com/jsvine/pdfplumber · Azure Document Intelligence — https://azure.microsoft.com/ko-kr/products/ai-services/ai-document-intelligence · Google Document AI — https://cloud.google.com/document-ai · AWS Textract — https://aws.amazon.com/textract/ · Upstage — https://www.upstage.ai/products/document-parse · Apache Tika — https://tika.apache.org
- 묶음 ③ 라벨링: Label Studio — https://labelstud.io/ · CVAT — https://github.com/cvat-ai/cvat · Snorkel Flow — https://snorkel.ai/ · Labelbox — https://labelbox.com/ · Scale AI — https://scale.com/data-engine · Roboflow — https://roboflow.com/ · Prodigy — https://prodi.gy/ · SAM 2 — https://ai.meta.com/research/sam2/ · Cleanlab — https://cleanlab.ai/ · SageMaker Ground Truth — https://aws.amazon.com/sagemaker/ai/groundtruth/
- 묶음 ④ 그래프·온톨로지: Neo4j — https://neo4j.com · Amazon Neptune — https://aws.amazon.com/neptune/ · TigerGraph — https://www.tigergraph.com · Memgraph — https://memgraph.com · Ontotext GraphDB — https://graphdb.ontotext.com · Stardog — https://www.stardog.com/platform/ · Apache Jena — https://jena.apache.org · Protégé — https://protege.stanford.edu · PoolParty — https://www.poolparty.biz/ontology-management · TopBraid EDG — https://www.topquadrant.com/products/topbraid-edg/ · IOF — https://github.com/iofoundry/ontology

> 주제별 개별 제품 출처 URL은 각 Part A 표의 인라인 링크 참조. 모든 링크는 리서치 시점(2026-06)에 실제 확인했으며, **시장 변동 주의** 표의 인수·종료·개명 사항을 인용 전 재확인할 것.

---

## 변경 이력 / 피드백 반영

| 버전 | 일자 | 내용 |
|---|---|---|
| v0.1 | 2026-06-19 | 초안 — 2층 구조(주제별 솔루션 + 플랫폼×주제 매트릭스 + 묶음 비교). 6개 주제군·7개 플랫폼 웹 리서치(출처 검증) 기반. |
| v0.2 | 2026-06-19 | **A·B 6개 주제(A-1~A-3·B-1~B-3) 솔루션 비교를 기능 중심·묶음 중심으로 갱신.** ① 신설 **Part A0**(4개 솔루션 묶음 + 기능×묶음 매트릭스) ② Part A의 6개 주제 표를 *기능 열*(자동수집·동의어매핑·표구조보존·AI 1차 라벨·그래프 추론·온프렘 등)로 재구성 ③ 6개 가이드(1층) 본문에서 솔루션·기능 재수집 — B-1에 Camelot/pdfplumber·표구조 보존 ★, B-2에 Roboflow·Prodigy·Cleanlab·SAM 2(Encord 제거 — 가이드 미수록), B-3에 TigerGraph·Memgraph·PoolParty/TopBraid·IOF·LPG↔RDF 분기·두산 LPG 결정 반영 ④ Part C에 A·B 6주제 묶음 요약 추가. (C~F 주제는 미변경.) |
| v0.3 | 2026-06-22 | **Part B 매트릭스의 A·B 6주제 행을 v0.2 Part A0/A 결론과 정합화**(C~F 행·열 미변경). 4개 셀 수정: ① A-3 용어집 **OSS △→✓**(OpenMetadata 네이티브 용어집, Part A 라인 96·A0-1 묶음①) ② B-1 전처리 **Collibra/Alation △→✗**(거버넌스 플랫폼은 처리계 전무 — Part C "데이터를 변환 안 함", A0 기능표 문서파싱 공백) ③ B-3 온톨로지 **Google Cloud ✓→△**(Part A B-3 표에 GCP 네이티브 그래프DB 없음 — 클라우드 네이티브는 Amazon Neptune뿐) ④ B-3 온톨로지 **Collibra/Alation △→✗**(그래프 기능 전무 — A0-1 묶음④는 별도 시장). |
