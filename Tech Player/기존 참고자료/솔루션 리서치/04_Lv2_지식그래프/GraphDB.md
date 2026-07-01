# GraphDB (Graphwise) — RDF 지식그래프 & 시맨틱 AI 플랫폼

> 작성일: 2026-06-10 | 카테고리: Lv.2 지식그래프/온톨로지

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Graphwise (Ontotext + Semantic Web Company 합병, 2025.02) |
| 라이선스 | 상용 + Free Edition (기능 제한) |
| 배포 형태 | 셀프호스팅 + 클라우드 배포 + GraphDB Cloud (관리형) |
| 최신 동향 | 2025.02: Ontotext + Semantic Web Company → Graphwise 합병 발표; 2025.07: GraphDB 11 GA 출시 (MCP 지원, 다중 LLM 통합, Talk-to-Graph 2.0 강화); GraphDB 11.3: Talk-to-Graph 4가지 검색 방법 |

---

## 한 줄 포지셔닝

**"W3C 표준 RDF/OWL 온톨로지 추론과 Talk-to-Graph 자연어 인터페이스로 제조·산업 지식 모델의 의미론적 정확성을 보장하는 그래프 DB"**

---

## 주요 기능

### 1. RDF 트리플 스토어 & SPARQL
- W3C RDF 표준 기반 트리플(주어-서술어-목적어) 저장
- SPARQL 1.1 완전 지원, SPARQL 업데이트·Federated Query
- 다중 온톨로지 관리: OWL, RDFS, SKOS 형식 임포트·편집·버전 관리

### 2. OWL/RDFS 온톨로지 추론 (Reasoning)
- 내장 추론 엔진: 클래스 계층, 속성 전파, 등가성, 역방향 관계 자동 추론
- 인퍼런스된 사실(Inferred Facts)이 쿼리에 직접 참여
- 도메인 온톨로지(FMEA, ISO 13374 등) 임포트 및 확장 가능

### 3. Talk-to-Graph (자연어 인터페이스)
- GraphDB 10.4 최초 도입 → 10.8 Talk-to-Graph 2.0 재설계 → 11.x 확장
- OpenAI ChatGPT Assistants API 연동, 그래프 데이터에 자연어 질의
- **4가지 검색 방법(Retriever)**:
  1. SPARQL 자동 생성 (정형 질의)
  2. 전문 검색(Full-Text Search)
  3. 시맨틱 유사도 검색(벡터 기반)
  4. SPARQL + 전문/시맨틱 복합 — 개방형·폐쇄형 질문 모두 처리

### 4. GraphDB 11 신기능 (2025.07 GA)
- **MCP(Model Context Protocol) 지원**: AI 에이전트가 GraphDB를 데이터 소스로 직접 접근
- **다중 LLM 통합**: OpenAI, Anthropic Claude, Mistral 등 복수 LLM 동시 연결
- **Data Fabric 지원**: 기업 전사 데이터를 그래프로 통합하는 엔터프라이즈 Data Fabric 기반
- 멀티 애플리케이션 지원으로 인프라 비용 절감 및 운영 단순화

### 5. 시맨틱 유사도 검색 & GraphRAG
- 그래프 노드에 벡터 임베딩 저장, SPARQL 내에서 유사도 검색 실행
- GraphRAG 패턴: SPARQL 검색 + 벡터 유사도를 결합해 LLM 컨텍스트 구성
- Graphwise + PoolParty(Semantic Web Company 제품) 통합으로 Taxonomy/Thesaurus 관리 강화

---

## AI-Ready Data 주제 매핑

| 주제 코드 | 주제명 | 지원 수준 |
|---|---|---|
| B-3 | 온톨로지 | ○ OWL/RDFS 추론 핵심 강점 |
| GraphRAG | AI 지식 검색 | ○ Talk-to-Graph + 시맨틱 검색 |

---

## 강점

- **OWL 추론 최고 성숙도**: 제조 도메인 온톨로지(결함-원인-조치 관계) 의미론적 모델링에 최적
- **W3C 표준 준수**: 상호운용성 보장, 외부 온톨로지(Schema.org, SOSA, OWL-S 등) 직접 임포트
- **Graphwise 합병 시너지**: PoolParty(분류체계·시소러스 관리) + GraphDB 통합 → 엔터프라이즈 지식 관리 플랫폼
- **Talk-to-Graph 성숙도**: LLM 기반 자연어 인터페이스가 가장 성숙한 RDF 플랫폼
- **MCP 표준 지원 선도**: GraphDB 11에서 AI 에이전트 연동 표준 프로토콜 지원

---

## 약점 및 주의점

- **SPARQL 학습 곡선**: SQL 경험자도 SPARQL 적응에 시간 필요 — 개발 생산성 초반 낮음
- **LPG 불지원**: Cypher, Gremlin 불가 — Neo4j 전환 시 마이그레이션 필요
- **대규모 분산 처리 제한**: TigerGraph·Neo4j AuraDB 대비 수십억 노드 처리 시 성능 한계
- **가격 비투명**: 엔터프라이즈 가격 공개 없음, 견적 필수
- **브랜드 전환 리스크**: Ontotext → Graphwise 리브랜딩 진행 중 — 일부 문서·통합이 구 브랜드 참조

---

## 가격 모델

- **Free Edition**: 기능 제한, 소규모 비상업 사용 가능
- **Developer Edition**: 개발 목적
- **Enterprise**: 기능 완전, 대용량, 고가용성 — 견적 필요
- **GraphDB Cloud**: 관리형 클라우드 배포 — 견적 필요
- 구체적 공개 가격 없음, 공식 사이트 문의 필요

---

## 연동 생태계

| 카테고리 | 연동 도구 |
|---|---|
| LLM | OpenAI GPT-4, Anthropic Claude, Mistral |
| AI/GraphRAG | LangChain, LlamaIndex, Talk-to-Graph |
| MCP | GraphDB 11 MCP Server |
| 데이터 통합 | R2RML (RDB→RDF 매핑), SPARQL 연합 쿼리 |
| 온톨로지 도구 | Protégé, TopBraid Composer, PoolParty (Graphwise 통합) |
| 파이프라인 | Apache Kafka, REST API |
| 클라우드 | AWS, Azure, GCP |
| 시각화 | 내장 WorkBench, GraphDB Studio, 외부 D3.js |

---

## 출처

- https://www.ontotext.com/products/graphdb/
- https://graphwise.ai/
- https://graphdb.ontotext.com/documentation/11.3/talk-to-graph.html
- https://www.prnewswire.com/news-releases/graphwise-launches-graphdb-11-enables-organizations-to-create-an-enterprise-wide-data-fabric-for-reliable-ai-302497224.html
- https://graphwise.ai/blog/talk-to-your-graph-2-0-a-partners-view/
- https://siliconangle.com/2025/07/08/graphwise-enhances-graph-database-become-brains-of-ai-agents/
- https://www.bloorresearch.com/2025/02/05/graph-update-ontotext-graphdb/
