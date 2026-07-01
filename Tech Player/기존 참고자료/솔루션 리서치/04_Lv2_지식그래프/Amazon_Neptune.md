# Amazon Neptune — AWS 완전 관리형 그래프 데이터베이스

> 작성일: 2026-06-10 | 카테고리: Lv.2 지식그래프/온톨로지

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Amazon Web Services (AWS) |
| 라이선스 | 상용 (AWS 관리형 서비스) |
| 배포 형태 | AWS 완전 관리형 (온프레미스 없음) |
| 최신 동향 | 2025.03: Amazon Bedrock Knowledge Bases GraphRAG GA 출시 (Neptune Analytics 연동); Neptune Analytics 벡터 검색 + 그래프 알고리즘 통합; Strands AI Agents SDK 연동 |

---

## 한 줄 포지셔닝

**"AWS 생태계 안에서 완전 관리형으로 GraphRAG와 Bedrock를 직접 연결하는 멀티모델 그래프 서비스"**

---

## 주요 기능

### 1. Neptune Database (OLTP 그래프)
- **멀티 쿼리 언어 지원**: Gremlin(프로퍼티 그래프), openCypher, SPARQL(RDF) 동시 지원
- 단일 그래프 인스턴스에서 세 언어 모두 사용 가능 — 마이그레이션 유연성
- 인메모리 최적화 아키텍처: 100,000+ TPS(초당 쿼리) 처리
- 고가용성: 3개 AZ에 6개 복사본 자동 유지

### 2. Neptune Analytics (OLAP 그래프 + 벡터)
- **인메모리 그래프 분석 엔진**: 대용량 그래프를 메모리에 적재해 저지연 분석
- **내장 벡터 검색**: 그래프 쿼리와 벡터 유사도 검색을 단일 쿼리로 결합
- 그래프 알고리즘 내장: 경로 탐색, 커뮤니티 탐지(클러스터링), 중심성(Centrality), 유사도
- 일시 정지(Paused) 시 10% 요금 — 배치/분석 워크로드에 비용 효율

### 3. Amazon Bedrock GraphRAG 통합 (2025.03 GA)
- Bedrock Knowledge Bases에서 Neptune Analytics를 그래프 스토어로 직접 사용
- 자동 파이프라인: 문서 임베딩 생성 → Neptune에 벡터+그래프 자동 저장
- 검색 시: 벡터 유사도 + 그래프 순회를 자동 결합하여 LLM 컨텍스트 구성
- 추가 소프트웨어 라이선스 없음 — Bedrock·Neptune·S3 비용만 발생

### 4. Neptune ML
- Amazon SageMaker와 통합된 그래프 머신러닝
- 그래프 신경망(GNN) 기반 노드 분류, 링크 예측, 그래프 분류
- 제조 도메인 예: 결함 유형 예측, 공급망 이상 탐지

### 5. 서버리스 옵션
- Neptune Serverless: 워크로드에 따라 자동 스케일 업/다운
- 최소 선불 없음, 사용량 기반 과금
- 개발·테스트 환경 비용 최적화에 적합

---

## AI-Ready Data 주제 매핑

| 주제 코드 | 주제명 | 지원 수준 |
|---|---|---|
| B-3 | 온톨로지 | △ SPARQL/RDF 지원이나 OWL 추론은 GraphDB/Stardog 대비 제한 |
| GraphRAG | AI 지식 검색 | ○ Bedrock 네이티브 GraphRAG |

---

## 강점

- **운영 부담 제로**: 완전 관리형, 패치·백업·복구·HA 자동 — 소규모 운영 팀에 최적
- **AWS 생태계 최고 통합**: Bedrock, SageMaker, S3, Lambda, Glue 등 완전 네이티브 연동
- **멀티 쿼리 언어**: Gremlin + openCypher + SPARQL 동시 지원 — 기존 팀 쿼리 언어 그대로 사용
- **Bedrock GraphRAG GA**: 추가 코드 없이 문서 → 지식그래프 → LLM RAG 자동 파이프라인
- **가격 투명성**: AWS 표준 요금표 공개, 예산 예측 용이

---

## 약점 및 주의점

- **AWS 종속**: AWS 전용, 멀티클라우드·온프레미스 불가
- **OWL 추론 제한**: SPARQL 지원하나 OWL/RDFS 추론 엔진 없음 — 의미론적 온톨로지 추론 한계
- **대형 그래프 비용**: Neptune Analytics 인메모리 비용이 대규모 그래프에서 급등 가능
- **커뮤니티 생태계 부재**: 오픈소스 없음, Neo4j·ArangoDB 대비 개발자 커뮤니티 작음
- **Cypher 제한**: openCypher 지원이나 Neo4j Cypher 전체 기능과 차이 있을 수 있음

---

## 가격 모델

| 서비스 | 과금 방식 | 참고 단가 |
|---|---|---|
| Neptune Database | 인스턴스 타입 + I/O + 스토리지 | r6g.large ~$0.182/시간 |
| Neptune Serverless | Neptune Capacity Units (NCU) | 사용량 기반 |
| Neptune Analytics | 메모리 최적화 Capacity Units | ~$0.48/시간 (메모리 단위) |
| Bedrock GraphRAG | Bedrock 토큰 + Neptune 비용 | 추가 라이선스 없음 |

- 파우즈(Pause) 시 Neptune Analytics 10% 요금 (데이터·설정 보존)
- Savings Plans(1년/3년 약정)으로 최대 40% 할인

---

## 연동 생태계

| 카테고리 | 연동 도구 |
|---|---|
| AWS 서비스 | Amazon Bedrock, SageMaker, S3, Lambda, Glue, Step Functions |
| AI/LLM | Bedrock Knowledge Bases GraphRAG, Strands AI Agents SDK |
| 쿼리 언어 | Gremlin, openCypher, SPARQL |
| 노트북 | Amazon SageMaker Studio (그래프 분석) |
| 파이프라인 | AWS Glue, AWS Data Pipeline |
| 시각화 | Graph Notebook (Jupyter 기반), Tom Sawyer Perspectives |
| LangChain | LangChain Neptune 통합 |

---

## 출처

- https://aws.amazon.com/neptune/
- https://aws.amazon.com/neptune/pricing/
- https://aws.amazon.com/neptune/features/
- https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html
- https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-bedrock-knowledge-bases-graphrag-generally-available/
- https://aws.amazon.com/blogs/machine-learning/announcing-general-availability-of-amazon-bedrock-knowledge-bases-graphrag-with-amazon-neptune-analytics/
- https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-graphs.html
