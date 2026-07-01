# 솔루션 리서치 INDEX

AI-Ready Data 기술 아키텍처의 **솔루션 레벨링(Lv.1 통합 플랫폼 / Lv.2 전문 솔루션 5종 / Lv.3 LLMOps)** 구분별 솔루션 조사 자료.
기준일: 2026-06 (웹 리서치 기반, 각 파일에 출처 URL 포함)

## 폴더 구조

각 구분 폴더는 `00_개요.md`(구분 정의 + 솔루션 비교 매트릭스 + 선택 가이드) + 솔루션별 상세 .md(기능 디테일·주제 매핑·강약점·가격·출처)로 구성.

| 폴더 | 구분 | 커버 주제 | 조사 솔루션 |
|---|---|---|---|
| `01_Lv1_통합데이터플랫폼` | Lv.1 통합 데이터 플랫폼 | A-1·A-2·A-3·C-3·E-1·C-1·C-2·F-1·F-2 | Databricks(Unity Catalog), Snowflake(Horizon), MS Fabric(+Purview), BigQuery+Dataplex, Cloudera CDP, Dremio |
| `02_유형1_의미관리_카탈로그` | 유형① 분리 옵션 — 전문 카탈로그 | A-1·A-2·A-3·C-3 | Collibra, Alation, Atlan, DataHub(Acryl), OpenMetadata, Informatica CDGC |
| `03_유형2_신뢰통제_품질관측` | 유형② 보강 옵션 — 품질·Observability | C-1·C-2·C-3 | Monte Carlo, Soda, GX Cloud, Anomalo, Bigeye, Acceldata |
| `04_Lv2_지식그래프` | Lv.2 지식그래프·온톨로지 | B-3 | Neo4j, GraphDB(Graphwise), Amazon Neptune, Stardog, TigerGraph, ArangoDB |
| `05_Lv2_문서AI_디지털화` | Lv.2 문서 AI·디지털화 | B-1·F-3 | Unstructured.io, Upstage DP, Azure DI, AWS Textract, Google Document AI, CLOVA OCR, ABBYY |
| `06_Lv2_학습데이터팩토리` | Lv.2 라벨링·합성데이터 | B-2·E-2 | Label Studio, Labelbox, Encord, CVAT / SDV, Gretel(NVIDIA), MOSTLY AI |
| `07_Lv2_OT_IoT수집` | Lv.2 OT/IoT 수집 | D-1 | Confluent(Kafka), AVEVA PI, Azure IoT, AWS IoT SiteWise, Ignition, HighByte, InfluxDB |
| `08_Lv2_AI데이터보안` | Lv.2 보안 전문 (횡단) | F-4 | Presidio, BigID, Protegrity, Immuta, Privacera, Securiti.ai |
| `09_Lv3_LLMOps_AgentOps` | Lv.3 LLMOps·Agent Ops | D-2·D-3·E-3·E-4 | LangSmith, Langfuse, Arize Phoenix, Braintrust, W&B Weave, promptfoo+Ragas, LiteLLM+Portkey, MCP(표준) |

총 68개 파일 (개요 9 + 솔루션 상세 58 + 본 인덱스).

## 구분별 핵심 발견 요약

**01 통합 플랫폼.** 2026년 현재 전 플랫폼이 Apache Iceberg 상호운용 중심으로 경쟁. AI Agent 거버넌스(Agent 신원·감사)가 Databricks·Snowflake 중심으로 성숙. 온프레미스·하이브리드 필수 환경에서는 Cloudera가 유일한 완전 하이브리드 선택지.

**02 전문 카탈로그.** MCP 지원이 새 격전지 — Atlan·DataHub·OpenMetadata가 네이티브 MCP 서버로 선도. 비용 격차가 커서(OSS 무료 vs Collibra·Informatica 연 수억) 그룹 표준 상용 + 계열사 OSS 하이브리드 전략이 현실적.

**03 품질·관측.** 비정형/LLM 학습 데이터 품질 스코어링은 Anomalo가 유일. Hadoop 레거시 관측은 Acceldata가 사실상 유일. 계열사 간 데이터 품질 SLA 집행은 Soda 데이터 계약 엔진이 가장 성숙.

**04 지식그래프.** OWL 추론 필요(제품-공정-결함 온톨로지) 시 GraphDB·Stardog, 빠른 GraphRAG PoC는 Neo4j, AWS 환경은 Neptune+Bedrock — 용도별 분리 전략이 현실적. GraphDB 11은 MCP·Talk-to-Graph 지원.

**05 문서 AI.** 한국어는 투트랙: Upstage(HWP·CJK 문서 파싱 — RAG 전처리 1순위) + CLOVA OCR(수기체 97~99% — 현장 수기 검사표 1순위). 망분리·에어갭 환경은 ABBYY가 독보적, OSS 대안은 Unstructured.

**06 학습데이터.** 라벨링은 OSS(Label Studio·CVAT) vs 엔터프라이즈(Encord·Labelbox) 양극화. 합성데이터는 데이터 유형으로 선택: 정형 관계형=SDV, 차등 프라이버시=MOSTLY AI, 텍스트=Gretel(2025 NVIDIA 인수 — 가격·정책 유동적).

**07 OT/IoT.** IBM의 Confluent 인수(2026.03)로 Kafka 생태계 변동 가능성. 망분리 공장 환경에는 Ignition Edge + HighByte(코드리스 컨텍스트화) 조합이 실용적. AVEVA CONNECT Flows로 PI의 클라우드 연결 자동화.

**08 AI 보안.** 전 벤더가 2025~2026 GenAI·Agent 특화 기능 출시(LLM Firewall, Agentic Access Governance 등). 한국 PIPA 대응+AI 규제 통합은 Securiti.ai가 가장 포괄적. 실무는 역할 분담 조합: Presidio(비정형 탐지)+Protegrity(토큰화)+Immuta/Privacera(접근제어)+BigID/Securiti(거버넌스).

**09 LLMOps.** 셀프호스팅 최적 조합: Langfuse(MIT) + LiteLLM(MIT) + Ragas/promptfoo. MCP는 사실상 표준 정착(주요 4사 모두 지원)이나 보안(프롬프트 인젝션·자격증명)이 도입 최대 장벽. promptfoo는 OpenAI에, Langfuse는 ClickHouse에 인수되는 등 시장 재편 중.

## 활용 가이드

도입 검토 순서: ① 구분 폴더의 `00_개요.md`에서 비교 매트릭스·선택 가이드 확인 → ② 후보 2~3개의 상세 .md에서 기능·가격·주제 매핑 검토 → ③ 출처 URL로 최신 정보 재확인(가격·인수합병은 변동 잦음).

주의: 2025~2026 인수합병이 많아(Gretel→NVIDIA, Confluent→IBM, promptfoo→OpenAI, Langfuse→ClickHouse, Ontotext+SWC→Graphwise) 계약 전 반드시 재확인 필요.
