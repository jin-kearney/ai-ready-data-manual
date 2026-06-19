# AI-Ready Data 매뉴얼 — Tech Stack 비교 (솔루션 × 주제)

> **목적:** 20개 주제(A-1~F-4)에 "어떤 솔루션을 써야 하는가"를 한 곳에서 비교·결정하기 위한 **마스터 Tech Stack 정본(초안 v0.1)**.
> **관점 고정:** "AI/에이전트를 만드는 도구"가 아니라 **"그 AI가 쓸 데이터를 준비·정비하는 도구"**다. (절대 원칙 — CLAUDE.md / 데이터 준비 관점)
> **읽는 법(2층 구조):**
> - **Part A — 주제별 솔루션**: "이 주제엔 뭘 쓰지?" (주제 → 솔루션). 각 주제 가이드의 '솔루션' 섹션은 여기로 연결한다.
> - **Part B — 묶음(플랫폼) × 주제 매트릭스**: "우리가 X 플랫폼을 깔면 어디까지 한 번에 되나?" (솔루션 → 주제).
> - **Part C — 묶음 스택 비교·선정 가이드**: 최종 의사결정용. 어느 스택이 어느 주제군에 강한가, 제조업(설비·OCR·비식별)엔 무엇이 중요한가.

> ⚠️ **이 표는 칸 채우기가 아니라 "필요 기능(capability)으로 고르게" 하는 표다.** 제품명은 시점에 따라 바뀐다 — 아래 **시장 변동 주의**를 반드시 함께 읽을 것. 카테고리·필요 기능을 먼저 보고, 제품은 PoC로 검증한다.

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

# Part A. 주제별 솔루션 (주제 → 솔루션)

## A군 + C-3 — 데이터 카탈로그·메타데이터·용어집·계통 (한 제품으로 묶임)

> **핵심:** A-1 카탈로그·A-2 메타데이터·A-3 용어집·C-3 계통(Lineage)은 **카탈로그/거버넌스 플랫폼 1개가 통째로 커버**하는 것이 시장 표준이다. 4개 도구를 따로 사는 게 아니다. **변별점은 ① 네이티브 비즈니스 용어집(A-3) ② 컬럼 단위 계통(C-3)** 두 가지.

| 솔루션 | 카테고리 | A-1 | A-2 | A-3 | C-3 | 핵심 (출처) |
|---|---|:--:|:--:|:--:|:--:|---|
| **Collibra** | 전용 거버넌스 | ✓ | ✓ | ✓ | ✓ | 카탈로그·용어집·리니지를 의미계층으로 묶은 엔터프라이즈 정본 ([catalog](https://www.collibra.com/products/data-catalog)) |
| **Alation** | 전용 카탈로그 | ✓ | ✓ | ✓ Glossary Hub | ✓ 컬럼단위 | 액티브 메타데이터 그래프·신뢰 신호 ([catalog](https://www.alation.com/product/data-catalog/)) |
| **Atlan** | 전용(액티브 메타) | ✓ | ✓ | ✓ Business Graph | ✓ 컬럼·OpenLineage | MCP/REST로 AI 연동, 제조 레퍼런스 ([catalog](https://atlan.com/data-discovery-catalog/)) |
| **Microsoft Purview** | 플랫폼 내장 | ✓ | ✓ | ✓ | ✓ | 멀티클라우드 페더레이션 거버넌스 ([unified-catalog](https://learn.microsoft.com/en-us/purview/unified-catalog)) |
| **Databricks Unity Catalog** | 플랫폼 내장 | ✓ | ✓ | △ 시맨틱레이어 | ✓ 컬럼단위 자동 | 데이터·모델·에이전트 단일 거버넌스 ([UC](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)) |
| **OpenMetadata** | 오픈소스 | ✓ | ✓ | ✓ | ✓ 컬럼단위 | 단일 시맨틱 그래프·네이티브 MCP ([open-metadata.org](https://open-metadata.org/)) |
| **DataHub** | 오픈소스 | ✓ | ✓ | △ | ✓ 컬럼단위 | 실시간 메타데이터 그래프 ([docs](https://docs.datahub.com/docs/introduction)) |
| **OpenLineage + Marquez** | 오픈소스(계통 표준) | △ | ✓ | ✗ | ✓ **계통 특화** | C-3 계통을 표준 이벤트로 자동 수집 ([OpenLineage](https://openlineage.io/)) |

**선정 포인트:** 단일 클라우드면 플랫폼 내장(Unity Catalog·Purview)으로 충분. 멀티소스·전사 거버넌스면 전용(Collibra·Alation·Atlan). 폐쇄망·무료 시작은 **OpenMetadata 또는 DataHub + 계통은 OpenLineage** 조합. A-3 용어집이 중요하면 Databricks·Snowflake(△)는 보완 필요.

## B-1 — 데이터 전처리 (문서 파싱·추출)

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **Unstructured** | 전용+OSS | 64종+ 파싱·청킹·임베딩 ETL 파이프라인 ([unstructured.io](https://unstructured.io/)) |
| **LlamaParse** | 전용(API) | 레이아웃 인식 OCR·표 구조 보존·마크다운 출력 ([docs](https://developers.llamaindex.ai/python/cloud/llamaparse/overview)) |
| **Azure AI Document Intelligence** | 클라우드 내장 | Read·Layout, RAG용 결정적 추출 ([overview](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview)) |
| **Amazon Textract / Google Document AI** | 클라우드 내장 | 표·폼·질의 기반 추출 ([Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)) |
| **Docling** (IBM) / **Apache Tika** | 오픈소스 | 온프렘 가능, gen-AI 파이프라인 연동 ([Docling](https://github.com/docling-project/docling)) |
| **Upstage Document Parse** (한국) | 전용(온프렘) | 국내 벤더·온프렘, RAG용 구조화 출력 ([product](https://www.upstage.ai/products/document-parse)) |

**선정 포인트:** 망분리면 OSS(Docling·Tika)·온프렘(Upstage). 사내 클라우드 표준이 있으면 그 생태계 내장형. RAG 적재 목표면 마크다운/JSON + 청킹 내장 여부.

## B-2 — 데이터 해설·주석 (라벨링/Annotation)

| 솔루션 | 카테고리 | AI 1차 라벨 · 온프레미스 (출처) |
|---|---|---|
| **Label Studio** (HumanSignal) | OSS+엔터프라이즈 | AI 1차 ✓ · 온프렘 ✓(에어갭) ([labelstud.io](https://labelstud.io/)) |
| **CVAT** | 오픈소스 | AI 1차 ✓(SAM/YOLO) · 온프렘 ✓(완전 셀프호스트) ([github](https://github.com/cvat-ai/cvat)) |
| **Encord** | 전용 | AI 1차 ✓(SAM 2) · 온프렘 ✓(에어갭 명시) ([docs](https://docs.encord.com/platform-documentation/Other/deployment-options.md)) |
| **Snorkel Flow** | 전용(프로그래매틱) | AI 1차 ✓(대량 초벌) · 온프렘 ✓ ([snorkel.ai](https://snorkel.ai/snorkel-flow/)) |
| **Labelbox / SuperAnnotate / Scale AI** | 전용(SaaS) | AI 1차 ✓ · 온프렘 **미확인**(계약 확인 필요) ([Labelbox](https://labelbox.com/product/annotate/)) |
| **SageMaker Ground Truth** (AWS) | 클라우드 내장 | AI 1차 ✓ · 온프렘 ✗(AWS 전용) ([groundtruth](https://aws.amazon.com/sagemaker/ai/groundtruth/)) |

**선정 포인트:** **공정·품질 데이터를 외부 반출 못 하면 후보가 좁혀진다** — 온프렘 공식 확인된 곳은 **CVAT(무료)·Encord·Snorkel·Label Studio**. AI 1차 라벨은 사실상 전 제품 지원하나 정확도는 PoC로 검증.

## B-3 — 온톨로지·지식그래프

> **1차 분기 = 데이터 모델:** 표준 온톨로지·추론(OWL/SKOS)이면 **RDF/트리플스토어**, 대규모 관계 탐색·GraphRAG면 **속성 그래프(LPG)**. Neptune만 둘 다.

| 솔루션 | 모델 | 카테고리 | 핵심 (출처) |
|---|---|---|---|
| **Neo4j** | LPG | 전용(Community OSS) | Cypher·벡터·GraphRAG·LLM KG Builder ([use-case](https://neo4j.com/use-cases/knowledge-graph/)) |
| **Amazon Neptune** | **RDF+LPG** | 클라우드 내장 | 한 서비스에 SPARQL·Gremlin·openCypher ([userguide](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)) |
| **Stardog / Ontotext GraphDB** | RDF | 전용 | OWL 추론·SHACL·가상 그래프 ([Stardog](https://www.stardog.com/platform/)) |
| **RDFox** (삼성) | RDF | 전용(인메모리) | 증분 추론·Datalog 룰 ([rdfox](https://www.oxfordsemantic.tech/rdfox)) |
| **Protégé + Apache Jena** | RDF/OWL | 오픈소스 | 온톨로지 저작(Protégé) + 저장·추론(Jena) ([Protégé](https://protege.stanford.edu/)) |

**선정 포인트:** 추론(인과·논리 도출) 필요하면 RDFox·Stardog·GraphDB. 관계 적재·GraphRAG만이면 Neo4j·Memgraph(LPG+벡터). AWS면 관리형 Neptune, 폐쇄망·무료면 Protégé+Jena.

## C-1 — 데이터 Observability

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **Monte Carlo** | 전용 | ML 기반 데이터+AI 관측 선두, 인시던트/RCA ([platform](https://www.montecarlodata.com/)) |
| **Sifflet / Bigeye** | 전용 | 계보 중심·필드 단위, 동적 임계값 ([Sifflet](https://www.siffletdata.com/)) |
| **Anomalo** | 전용 | 규칙 없이 데이터 내용을 보는 무규칙 ML ([data-observability](https://www.anomalo.com/)) |
| **Soda** | OSS+상용 | SodaCL(YAML) 규칙 + ML 이상탐지 하이브리드 ([soda.io](https://www.soda.io/)) |
| **Acceldata** | 전용 | 데이터·파이프라인·인프라·비용까지 ([acceldata](https://www.acceldata.io/)) |

**선정 포인트:** OSS는 사실상 Soda Core 단독. 컬럼 단위 계보 연계가 강한 곳(Monte Carlo·Sifflet)이 RCA에 유리. C-2(합·불 판정)와 경계를 흐리지 말 것 — C-1은 "지금 정상으로 흐르나".

## C-2 — 데이터 품질 + 접근 게이트 (두 축)

**품질 (합·불 판정):**

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **Great Expectations** | 오픈소스 | "기대값=코드" 검증 표준 ([greatexpectations.io](https://greatexpectations.io/)) |
| **Soda Core** | 오픈소스+SaaS | YAML 선언형 체크·데이터 계약 ([github](https://github.com/sodadata/soda-core)) |
| **Informatica / Collibra / Ataccama / Qlik Talend** | 엔터프라이즈 | 프로파일링→규칙→스코어카드→DQ 차원 ([Ataccama](https://www.ataccama.com/platform/data-quality)) |

**접근 게이트 (누가 쓸 수 있나):**

| 솔루션 | 카테고리 | 핵심 (출처) |
|---|---|---|
| **Immuta / Privacera** | 전용 | 멀티플랫폼 ABAC·동적 마스킹·행/열/셀 통제 ([Immuta](https://www.immuta.com/product/data-access-governance/)) |
| **Unity Catalog / Snowflake Horizon / AWS Lake Formation** | 플랫폼 내장 | ABAC·태그 기반 행/열 통제 ([Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html)) |
| **Apache Ranger** | 오픈소스 | 빅데이터 표준 권한·감사(상용 도구의 기반) ([ranger](https://ranger.apache.org/)) |

**선정 포인트:** 단일 클라우드면 플랫폼 내장으로 충분. **여러 플랫폼을 한 정책으로 가로질러** 통제하려면 전용(Immuta·Privacera). 추세는 ABAC+태그 기반.

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

## F-4 — AI 데이터 보안 (비식별)

> **관점 고정:** 접근차단/방화벽이 아니라 **데이터 자체 변환**. 흐름 = 발견 → 변환 → 합성.

| 솔루션 | 카테고리 | 역할 (출처) |
|---|---|---|
| **Microsoft Presidio** | 오픈소스 | 탐지+마스킹+가명화(텍스트·이미지) 무료 SDK ([presidio](https://microsoft.github.io/presidio/)) |
| **Google Cloud Sensitive Data Protection (DLP)** | 클라우드 내장 | 탐지~가명화·토큰화·FPE 한 서비스 ([DLP](https://cloud.google.com/security/products/sensitive-data-protection)) |
| **Protegrity / Skyflow** | 전용 | 토큰화·볼트 중심 비식별 변환 ([Protegrity](https://www.protegrity.com/)) |
| **Amazon Macie / BigID** | 클라우드/전용 | **탐지·분류 전용**(변환은 짝지어야) ([Macie](https://aws.amazon.com/macie/)) |
| **Tonic.ai / Gretel** | 전용 | 비식별+합성으로 안전 데이터화 ([Tonic](https://www.tonic.ai/)) |
| **파수(Fasoo)** (한국) / **ARX** (OSS) | 전용/OSS | 국내 레퍼런스 / k-익명성 ([ARX](https://arx.deidentifier.org/)) |

**선정 포인트:** **Macie·BigID는 발견 전용** — 단독으로 F-4 못 채움, 변환 도구와 짝지어야. Presidio(OSS)는 강력하나 "모든 PII 탐지 보장 안 됨"을 문서가 명시 → 사람 검수 병행.

---

# Part B. 묶음(플랫폼) × 20개 주제 커버리지 매트릭스

> "우리가 이 플랫폼을 깔면 어디까지 한 번에 되나"를 한눈에. ✓ 네이티브 강함 / △ 부분·외부 보강 / ✗ 없음.

| 주제 | Databricks | MS/Azure | AWS | Google Cloud | Snowflake | OSS 조합 | Collibra/Alation |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| A-1 카탈로그 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-2 메타데이터 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| A-3 용어집 | △ | ✓ | ✓ | ✓ | △ | △ | ✓ |
| B-1 전처리 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | △ |
| B-2 라벨링 | △ | ✓ | ✓ | ✗ | △ | ✓ | ✗ |
| B-3 온톨로지 | △ | △ | ✓ | ✓ | △ | ✓ | △ |
| C-1 Observability | ✓ | ✓ | △ | △ | ✓ | ✓ | ✓ |
| C-2 품질·게이트 | ✓ | ✓ | ✓ | △ | ✓ | △ | ✓ |
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
| F-4 보안/비식별 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | △ |

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

1. **A·C·F(거버넌스) 계열은 어느 대형 플랫폼이든 강하다.** 카탈로그·메타데이터·계통·품질·보안은 평준화됐다 — 여기서 스택을 가르는 건 "이미 어느 클라우드를 쓰는가"다. 단일 클라우드면 그 내장 거버넌스로 시작하는 게 합리적.

2. **B·E(처리·생성) 계열에서 갈린다.** 라벨링(B-2)·온톨로지(B-3)·합성(E-2)은 **어느 통합 플랫폼도 약하다** — 사실상 전용/OSS 도구를 붙여야 한다(Label Studio·Neo4j·SDV/Omniverse). 거버넌스 플랫폼(Collibra/Alation)은 이 영역이 통째로 비어 있다.

3. **제조업에 특히 중요한 D-1·F-3·F-4는 누가 메우나.**
   - **D-1(설비·IoT):** 통합 플랫폼보다 **산업 historian(AVEVA PI·Ignition) + 표준(OPC UA·Sparkplug)**이 본질. 클라우드는 적재·분석을 보조. (Google은 IoT Core 폐기로 갭)
   - **F-3(디지털화):** 한글 손글씨·도면엔 **국내 특화(CLOVA·Upstage)**가 글로벌 OCR보다 유리할 수 있음. 음성은 STT 별도.
   - **F-4(비식별):** 플랫폼 내장 마스킹(Unity Catalog·Snowflake·DLP)으로 기본은 되나, 활용성 보존·재식별 점검엔 전용(Presidio·Tonic)·국내(파수) 보강.

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

> 주제별 개별 제품 출처 URL은 각 Part A 표의 인라인 링크 참조. 모든 링크는 리서치 시점(2026-06)에 실제 확인했으며, **시장 변동 주의** 표의 인수·종료·개명 사항을 인용 전 재확인할 것.

---

## 변경 이력 / 피드백 반영

| 버전 | 일자 | 내용 |
|---|---|---|
| v0.1 | 2026-06-19 | 초안 — 2층 구조(주제별 솔루션 + 플랫폼×주제 매트릭스 + 묶음 비교). 6개 주제군·7개 플랫폼 웹 리서치(출처 검증) 기반. |
