# TigerGraph — 대규모 분산 그래프 분석 플랫폼

> 작성일: 2026-06-10 | 카테고리: Lv.2 지식그래프/온톨로지

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | TigerGraph Inc. (레드우드 시티, 2012년 설립) |
| 라이선스 | 상용 + Community Edition (무료) |
| 배포 형태 | SaaS (TigerGraph Savanna) + 셀프호스팅 + 클라우드 마켓플레이스 |
| 최신 동향 | 2025.03: 차세대 그래프+벡터 하이브리드 검색 발표 (5.2x 빠른 벡터 검색, 22.4x 적은 리소스); Community Edition 출시; LDBC 감사 기반 17.9x 성능 우위 공표 |

---

## 한 줄 포지셔닝

**"수십억 노드 대규모 그래프에서 딥 멀티홉 분석과 하이브리드 벡터+그래프 검색을 병렬 처리로 구현하는 고성능 분산 그래프 플랫폼"**

---

## 주요 기능

### 1. 분산 MPP (Massively Parallel Processing) 아키텍처
- 그래프 데이터를 수평 분산, 복수 서버에서 동시 처리
- 10+ 홉 딥 트래버설을 서브초(sub-second) 시간에 처리
- 공급망 경로 분석: 수십 단계의 공급망 경로를 실시간 탐색
- LDBC 감사 기준 Neo4j 대비 17.9x 성능 우위 (대규모 분석 워크로드 기준)

### 2. GSQL (그래프 SQL)
- TigerGraph 독자 쿼리 언어, 절차형 그래프 프로그래밍 지원
- Parallel Graph Algorithm 작성 가능 — 복잡한 그래프 분석 로직 구현
- openCypher도 지원 (2024~)으로 Neo4j 전환 장벽 낮춤
- 12x~58x 빠른 데이터 로딩 속도 (Neo4j 대비)

### 3. 그래프+벡터 하이브리드 검색 (2025 신기능)
- 벡터 검색 5.2x 속도 향상 + 23% 높은 Recall (경쟁사 대비)
- 22.4x 적은 리소스 사용으로 동일 성능 달성
- 자동 증분 인덱스 업데이트: 6x 빠른 인덱싱
- 패턴 이상탐지: 그래프 패턴 + 벡터 유사도 결합 분석

### 4. GraphRAG 지원
- 지식그래프 기반 GraphRAG: 그래프 구조로 LLM 응답에 관계 컨텍스트 제공
- 할루시네이션 감소: 노드·엣지 관계 그라운딩으로 LLM 출력 정확도 향상
- 복잡한 멀티엔티티 질문에서 단순 벡터 RAG 대비 강점

### 5. 그래프 ML & AI
- 그래프 알고리즘 라이브러리: 커뮤니티 탐지, 중심성, 경로 탐색, 유사도
- 추천 시스템, 이상탐지(Fraud Detection), 공급망 최적화에 적용
- GraphML 지원: 그래프 신경망 연동

---

## AI-Ready Data 주제 매핑

| 주제 코드 | 주제명 | 지원 수준 |
|---|---|---|
| B-3 | 온톨로지 | △ LPG 기반, OWL 추론 미지원 |
| GraphRAG | AI 지식 검색 | ○ 하이브리드 벡터+그래프 검색 |

---

## 강점

- **대규모 성능 압도적**: 수십억 노드 그래프, 딥 멀티홉 쿼리에서 가장 빠른 처리 속도
- **공급망 최적화 최적**: 제조 다계열사 공급망의 복잡한 관계 분석(경로·이상·영향 분석)에 강점
- **하이브리드 벡터 검색**: 그래프+벡터를 단일 쿼리로 — 별도 벡터 DB 불필요
- **비용 효율**: 77% 인프라 비용 절감 레퍼런스 보고됨
- **Community Edition**: 무료로 핵심 기능 체험 가능

---

## 약점 및 주의점

- **GSQL 학습 곡선**: 독자 쿼리 언어 GSQL — 기존 SQL/Cypher 팀 재교육 필요
- **온톨로지 추론 없음**: OWL/RDFS 추론 미지원 — 의미론적 온톨로지 기반 지식 모델링에 한계
- **생태계 상대적 작음**: Neo4j 대비 튜토리얼·커뮤니티·통합 라이브러리 적음
- **운영 복잡성**: 분산 아키텍처 설정 및 관리가 단일 노드 DB 대비 복잡
- **가격 비투명**: 엔터프라이즈 견적 기반, 예산 예측 어려움

---

## 가격 모델

| 티어 | 특징 |
|---|---|
| Community Edition | 무료, 핵심 기능, 비상업 |
| TigerGraph Savanna | 클라우드 사용량 기반 (메모리·컴퓨트·스토리지) |
| Enterprise (셀프호스팅) | 구독 기반, 견적 |

- Savanna Cost Estimation 도구: 예상 사용량 입력 → 비용 추정 제공
- 30일 무료 체험 제공

---

## 연동 생태계

| 카테고리 | 연동 도구 |
|---|---|
| LLM/AI | LangChain, OpenAI, Anthropic Claude |
| GraphRAG | TigerGraph GraphRAG 커넥터, LlamaIndex |
| 데이터 파이프라인 | Apache Kafka, Spark |
| ETL | JDBC/ODBC Connector, REST API |
| 클라우드 | AWS, Azure, GCP (Savanna), AWS Marketplace |
| 알고리즘 | GSQL 그래프 알고리즘 라이브러리 |
| 시각화 | GraphStudio (내장), TigerGraph Insights |
| API | GSQL API, REST++ API, pyTigerGraph (Python SDK) |

---

## 출처

- https://www.tigergraph.com/
- https://www.tigergraph.com/pricing/
- https://docs.tigergraph.com/savanna/main/overview/pricing
- https://www.globenewswire.com/news-release/2025/03/04/3036461/0/en/TigerGraph-Unveils-Next-Generation-Hybrid-Search-to-its-Graph-Database-to-Power-AI-at-Scale-Also-Introduces-a-Game-Changing-Community-Edition.html
- https://www.tigergraph.com/comparison/tigergraph-vs-neo4j/
- https://www.falkordb.com/comparison/neo4j-vs-tigergraph/
- https://skillup.ccccloud.com/2025/07/01/ai-knowledge-graph-platforms-comparing-neo4j-tigergraph-and-aws-neptune-for-scalable-ai-applications/
