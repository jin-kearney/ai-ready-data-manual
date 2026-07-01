# Neo4j — 그래프 데이터베이스 & GraphRAG 플랫폼

> 작성일: 2026-06-10 | 카테고리: Lv.2 지식그래프/온톨로지

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Neo4j Inc. (스웨덴 말뫼 + 미국 샌프란시스코, 2007년 설립) |
| 라이선스 | 상용 (AuraDB, Enterprise) + 오픈소스 Community Edition (GPL-3.0) |
| 배포 형태 | SaaS (Neo4j AuraDB) + 셀프호스팅 + 주요 클라우드 마켓플레이스 |
| 최신 동향 | 2026.01: SEARCH Clause 도입(벡터 인덱스 인-인덱스 필터링 대폭 성능 개선); 공식 neo4j-graphrag-python 패키지 v1.x 안정화; NODES AI 2026 컨퍼런스에서 Agentic GraphRAG 발표 |

---

## 한 줄 포지셔닝

**"세계 최대 그래프 DB 생태계와 공식 GraphRAG 패키지로 LLM 지식 그라운딩의 표준 경로를 제시하는 그래프 플랫폼"**

---

## 주요 기능

### 1. LPG (Label Property Graph) 네이티브 엔진
- 노드·관계에 레이블과 속성을 직접 저장하는 직관적 모델
- 인덱스-프리 인접성(index-free adjacency) 기반 O(1) 이웃 탐색
- Cypher 쿼리 언어: SQL과 유사한 그래프 전용 선언형 언어

### 2. 네이티브 벡터 인덱스 (2025~2026)
- 그래프 노드에 벡터 임베딩 직접 저장 및 유사도 검색
- 2026.01 SEARCH Clause: 인-인덱스 필터링으로 벡터 검색 성능 대폭 향상
- 그래프 순회(traversal) + 벡터 유사도 검색을 단일 Cypher 쿼리로 결합

### 3. GraphRAG 공식 패키지 (neo4j-graphrag-python)
- 1st-party 라이브러리, 장기 지원(LTS) 보장
- 구성 요소: Knowledge Graph Builder, SimpleKGPipeline, GraphRAG Retriever, LLM 연동
- LangChain, LlamaIndex 통합 지원
- 엔티티 추출 → 그래프 구축 → 벡터+그래프 복합 검색 → LLM 응답 생성 풀 파이프라인

### 4. Agentic GraphRAG (2026 발표)
- 자율적 지식그래프 구축: 문서 스트림에서 엔티티·관계 자동 추출
- 적응형 검색(Adaptive Retrieval): 쿼리 복잡도에 따라 검색 전략 자동 선택
- 멀티홉 추론 지원 — 단순 벡터 RAG 대비 복잡한 관계 질의에 강점

### 5. Neo4j Bloom (시각화)
- 코딩 없이 그래프 탐색·시각화하는 비즈니스 사용자 도구
- 자연어 검색으로 그래프 탐색
- 패턴 기반 강조·필터링

### 6. Neo4j AuraDB (관리형 클라우드)
- 완전 관리형 서버리스 옵션, 자동 스케일
- Free → Professional → Business Critical → Virtual Dedicated Cloud 티어

---

## AI-Ready Data 주제 매핑

| 주제 코드 | 주제명 | 지원 수준 |
|---|---|---|
| B-3 | 온톨로지 | △ LPG 모델, OWL 추론 미지원 |
| GraphRAG | AI 지식 검색 | ○ 공식 1st-party 패키지 |

---

## 강점

- **생태계 압도적 1위**: 그래프 DB 시장 점유율 1위, 가장 많은 튜토리얼·커뮤니티·레퍼런스
- **GraphRAG 가장 빠른 시작 경로**: 공식 패키지, LangChain/LlamaIndex 통합 완성도 최고
- **벡터+그래프 통합**: 별도 벡터 DB 없이 그래프 노드에 임베딩 저장·검색
- **Cypher 직관성**: SQL 경험자도 빠르게 학습 가능, 풍부한 예제

---

## 약점 및 주의점

- **OWL/RDF 온톨로지 추론 미지원**: W3C 표준 온톨로지 명세(OWL, RDFS) 기반 추론 없음 — 의미론적 상속·등가성 자동 추론 불가
- **대규모 분산 처리 한계**: TigerGraph 대비 수십억 노드 분산 처리 성능 제한
- **SPARQL 미지원**: RDF 표준 기반 연동 어려움
- **엔터프라이즈 비용**: Business Critical 이상 시 비용 급등, 다계열사 환경에서 예산 관리 필요

---

## 가격 모델

| 티어 | 비용 | 특징 |
|---|---|---|
| AuraDB Free | $0 | 학습·소규모, 기능 제한 |
| Professional | $0.09/시간~ (~$65/월) | 소규모 프로덕션 |
| Business Critical | $146/GB/월 | 99.95% SLA, HA 3-zone 클러스터 |
| Virtual Dedicated Cloud | 견적 | VPC 전용, 최고 커스터마이제이션 |
| Enterprise (셀프호스팅) | $15,000~$100,000+/년 | 코어 수 기반 구독 |

---

## 연동 생태계

| 카테고리 | 연동 도구 |
|---|---|
| LLM 프레임워크 | LangChain (Neo4j Vector Index), LlamaIndex, LlamaIndex KG Index |
| AI/GraphRAG | neo4j-graphrag-python (공식), OpenAI, Anthropic, Cohere |
| 데이터 파이프라인 | Apache Kafka (Kafka Connector), Spark (GraphX), Airflow |
| ETL | dbt (Graph Materialization), Fivetran |
| BI | Tableau, Power BI, Grafana |
| 클라우드 | AWS, Azure, GCP (AuraDB) |
| MCP | Neo4j MCP Server (Labs) |
| 시각화 | Neo4j Bloom, yFiles, Linkurious |

---

## 출처

- https://neo4j.com/
- https://neo4j.com/pricing/
- https://neo4j.com/docs/neo4j-graphrag-python/current/
- https://neo4j.com/labs/genai-ecosystem/graphrag/
- https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/
- https://github.com/neo4j/neo4j-graphrag-python
- https://neo4j.com/videos/nodes-ai-2026-agentic-graphrag-autonomous-knowledge-graph-construction-and-adaptive-retrieval-2/
- https://agentmarketcap.ai/blog/2026/04/07/graph-rag-vs-vector-rag-agent-memory-neo4j-pgvector
- https://www.vendr.com/marketplace/neo4j
