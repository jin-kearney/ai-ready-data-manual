# ArangoDB (Arango) — 멀티모델 그래프 & GraphRAG 플랫폼

> 작성일: 2026-06-10 | 카테고리: Lv.2 지식그래프/온톨로지

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | ArangoDB GmbH → Arango AI (독일 쾰른, 2014년 설립) |
| 라이선스 | 상용 + 오픈소스 Community Edition (Apache 2.0) |
| 배포 형태 | SaaS (AMP, Arango Managed Platform) + 셀프호스팅 + OEM 임베딩 |
| 최신 동향 | 2025~2026: Arango AI Suite 출시 (AutoGraph, AutoRAG, AIOps); FAISS 기반 벡터 검색 강화; HybridGraphRAG 공식화; 브랜드 "Arango"로 리포지셔닝; GPU 가속 추가 |

---

## 한 줄 포지셔닝

**"그래프·문서·KV·벡터를 AQL 단일 언어로 통합 처리하는 멀티모델 오픈소스 DB + AutoGraph으로 지식그래프를 자동 구축하는 GraphRAG 플랫폼"**

---

## 주요 기능

### 1. 네이티브 멀티모델 엔진
- 단일 DB 인스턴스에서 그래프(LPG), 문서, 키-값, 벡터 데이터 동시 저장·처리
- AQL (ArangoDB Query Language): 모든 모델을 단일 쿼리 언어로 조회
- 전문 검색(Full-Text), 지리공간(Geospatial) 검색 내장
- "System of Context" 포지셔닝: 기업 데이터와 LLM을 연결하는 맥락 인식 계층

### 2. 벡터 검색 (FAISS 기반)
- FAISS 라이브러리 통합, Approximate Nearest Neighbor (ANN) 검색
- AQL 내에서 벡터 검색 실행: SELECT + GRAPH TRAVERSAL + VECTOR SEARCH 단일 쿼리
- 그래프 순회 + 벡터 유사도 결합 — 단순 벡터 DB 대비 관계 컨텍스트 추가

### 3. HybridGraphRAG
- 벡터 검색 + 그래프 순회 + 전문 검색을 단일 멀티모델 접근으로 통합
- LangChain과 자연어 쿼리 연동
- 단순 벡터 RAG의 한계(관계 컨텍스트 부재)를 그래프 구조로 보완

### 4. Arango AI Suite (2025 신기능)
- **AutoGraph**: 조직 데이터에서 지식 도메인 자동 발견 → 도메인별 컨텍스트 지식그래프 자동 구축
- **AutoRAG**: 도메인별로 최적 처리 깊이 자동 할당
- **AIOps**: 데이터 파이프라인 자동화, MLOps 지원
- **GPU 가속**: 대규모 그래프 분석 및 ML 가속
- 자연어 지원 (NL2AQL): 자연어 → AQL 자동 변환
- Agentic Framework: 컨텍스트 인식 GraphRAG 에이전트 구현

### 5. Smart Graphs & Sharding
- SmartGraph: 그래프 파티셔닝으로 분산 환경에서 네트워크 홉 최소화
- EnterpriseGraph: 기업 환경 최적화 분산 그래프
- 수평 확장 클러스터링

---

## AI-Ready Data 주제 매핑

| 주제 코드 | 주제명 | 지원 수준 |
|---|---|---|
| B-3 | 온톨로지 | △ LPG 기반, OWL 추론 미지원이나 유연한 스키마 |
| GraphRAG | AI 지식 검색 | ○ HybridGraphRAG + AutoGraph |

---

## 강점

- **멀티모델 단일 플랫폼**: 그래프+문서+벡터를 하나의 DB로 — 복잡한 멀티 DB 아키텍처 없이 GraphRAG 구현
- **오픈소스 Community Edition**: Apache 2.0 라이선스, 상업적 사용 가능, 제한 없음
- **AutoGraph 자동 지식그래프**: 도메인 전문가 없이도 데이터에서 지식구조 자동 발견
- **AQL 단일 언어**: 모든 데이터 모델 단일 쿼리 언어 — 팀 역량 분산 없음
- **유연한 스키마**: 문서 저장 기반으로 제조 데이터의 비정형 구조도 수용

---

## 약점 및 주의점

- **OWL/RDFS 추론 없음**: 의미론적 온톨로지 추론(GraphDB·Stardog 수준) 미지원
- **SPARQL 미지원**: W3C RDF 표준 연동 어려움
- **대규모 처리 성능**: TigerGraph 대비 수십억 노드 딥 멀티홉 분석 성능 한계
- **엔터프라이즈 레퍼런스 성장 중**: Neo4j·TigerGraph 대비 대형 제조업 레퍼런스 적음
- **AQL 고유 언어**: Cypher/SPARQL 전환 시 재학습 필요 (openCypher 미지원)

---

## 가격 모델

| 티어 | 특징 |
|---|---|
| Community Edition | 무료 (Apache 2.0), 모든 핵심 기능, 상업 사용 가능 |
| AMP (Managed Cloud) | 리소스 기반 과금 (노드·스토리지·SLA), 견적 |
| Enterprise (셀프호스팅) | HA, RBAC, 스마트그래프 등 엔터프라이즈 기능, 견적 |
| OEM/Embedded | 제품 내 임베딩, 별도 계약 |

- AWS Marketplace에서 ArangoGraph(관리형) 사용 가능
- 구체적 공개 가격 없음, 설정 기반 견적

---

## 연동 생태계

| 카테고리 | 연동 도구 |
|---|---|
| LLM/AI | LangChain (AQL + GraphRAG), LlamaIndex, OpenAI, Anthropic |
| GraphRAG | HybridGraphRAG, AutoGraph, AutoRAG |
| 데이터 파이프라인 | Apache Kafka, Spark, Flink |
| ETL | ArangoDB Connectors, REST API |
| 클라우드 | AWS (ArangoGraph), GCP, Azure, AWS Marketplace |
| 드라이버 | Python, Java, JavaScript, Go, PHP |
| 시각화 | ArangoDB Web UI, D3.js, Gephi |
| MCP | ArangoDB MCP Server (Labs) |

---

## 출처

- https://arango.ai/
- https://arango.ai/pricing/
- https://arango.ai/resources/comparison-rag-with-vector-databases-vs-arangodb-graphrag-with-knowledge-graphs/
- https://docs.arango.ai/
- https://app.daily.dev/posts/vector-search-in-arangodb-insights-hands-on-examples-v1dm6cmak
- https://pdpspectra.com/blog/neo4j-vs-arangodb-2026/
- https://aws.amazon.com/marketplace/pp/prodview-keoythdz3ffv6
- https://www.g2.com/products/arango/reviews
