# Stardog — 엔터프라이즈 지식그래프 & 시맨틱 계층 플랫폼

> 작성일: 2026-06-10 | 카테고리: Lv.2 지식그래프/온톨로지

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Stardog Union Inc. (워싱턴 D.C., 2012년 설립) |
| 라이선스 | 상용 (Stardog Studio 무료) |
| 배포 형태 | 클라우드(Stardog Cloud) + 셀프호스팅 + AWS Marketplace |
| 최신 동향 | 2026: KGC(Knowledge Graph Conference) 2026 참가 "AI Data Readiness Gap 해소" 주제; Gartner Generative AI Technologies Emerging Market 인정; Voicebox "환각 없는" 버전 출시; 아gentic AI용 EKG(Enterprise Knowledge Graph) 포지셔닝 강화 |

---

## 한 줄 포지셔닝

**"이종 기업 데이터를 이동 없이 가상화하고, OWL 추론 기반 시맨틱 계층 위에 Voicebox AI로 에이전트가 이해하는 엔터프라이즈 지식그래프"**

---

## 주요 기능

### 1. 데이터 가상화 (Virtual Graphs)
- 외부 RDB·DW·레이크 데이터를 물리적으로 이동하지 않고 SPARQL로 통합 질의
- R2RML/SMS 매핑: 관계형 데이터를 RDF 뷰로 동적 변환
- Snowflake, BigQuery, Databricks, PostgreSQL, SQL Server 등 다양한 소스 지원
- 제조 계열사의 분산된 ERP·MES·PLM 데이터를 단일 SPARQL 엔드포인트로 통합

### 2. OWL/RDFS 네이티브 추론
- RDFS+, QL, RL, EL 추론 프로파일 지원
- 인퍼런스 결과가 쿼리에 직접 참여 (추론된 사실 포함 검색)
- 설명 가능한 AI: 각 결과의 추론 로직 추적·표시 → 규제·감사 환경에 필수
- 데이터 계층(DB)에서 시맨틱 정합성 집행 — 애플리케이션 로직 의존 탈피

### 3. Stardog Voicebox (AI 지식 엔지니어)
- LLM 기반 자연어 → SPARQL 자동 생성
- 지식그래프 모델 구축 및 유지 보수 자연어 지시
- "환각 없는(Hallucination-Free)" 버전: 그래프 사실에 완전 기반한 응답 생성
- 고위험 산업(금융·의료·제조 안전) 적합

### 4. Agentic AI 지원
- EKG(Enterprise Knowledge Graph)를 AI 에이전트의 문맥 인식 데이터 계층으로 연결
- 에이전트가 SPARQL로 지식그래프 자율 질의 가능
- 단편화된 엔터프라이즈 데이터에 의미론적 컨텍스트 부여 → 자율 AI 에이전트 정확도 향상

### 5. 엔터프라이즈 거버넌스
- RBAC(역할 기반 접근 제어) 완전 지원
- LDAP/AD 통합
- 데이터 마스킹, 행 수준 보안
- 감사 로그 및 규정 준수 리포팅

---

## AI-Ready Data 주제 매핑

| 주제 코드 | 주제명 | 지원 수준 |
|---|---|---|
| B-3 | 온톨로지 | ○ OWL 추론 + 데이터 가상화 핵심 강점 |
| GraphRAG | AI 지식 검색 | ○ Voicebox + 시맨틱 검색 |

---

## 강점

- **데이터 가상화 독보적 강점**: 이동 없이 이종 소스를 시맨틱 통합 — 다계열사 데이터 정합에 최적
- **설명 가능한 AI**: OWL 추론 결과의 논리 추적으로 고위험·규제 환경 적합
- **에이전트 AI 준비성**: 의미론적으로 풍부한 EKG 위에 자율 에이전트 구현 가능
- **Gartner 인정**: Generative AI Technologies Emerging Market 등재 — 엔터프라이즈 신뢰도
- **57x 가격/성능**: Stardog 자체 벤치마크 기준 경쟁사 대비 57x 가격 대비 성능 우위 주장

---

## 약점 및 주의점

- **높은 비용**: 엔터프라이즈 전용 가격, AWS AMI 기준 ~$5.55/시간 — 상당한 투자 필요
- **복잡한 초기 설정**: 지식 모델링·SPARQL·OWL 전문성 필요 — 학습 곡선 높음
- **공개 가격 없음**: 완전 커스텀 견적, 예산 계획 어려움
- **LPG 미지원**: Cypher·Gremlin 불가, RDF/SPARQL 전문성 필요
- **커뮤니티 생태계 제한**: Neo4j·ArangoDB 대비 개발자 커뮤니티·튜토리얼 적음

---

## 가격 모델

- **Stardog Studio**: 무료 (지식그래프 구축·관리 IDE)
- **Stardog Free**: 기능 제한 (HA, 캐싱, 백업, LDAP, 전체 커넥터 없음)
- **Enterprise**: 완전 기능, 견적 필요
- **AWS Marketplace**: ~$5.55/시간 (소프트웨어 비용 기준, 인프라 별도)
- 30일 무료 체험 제공

---

## 연동 생태계

| 카테고리 | 연동 도구 |
|---|---|
| 데이터 가상화 소스 | Snowflake, BigQuery, Databricks, PostgreSQL, MySQL, SQL Server, Oracle |
| LLM/AI | Voicebox (자체), LangChain, OpenAI, Anthropic Claude |
| 쿼리 | SPARQL 1.1, SPARQL* (RDF*) |
| 거버넌스 | LDAP, Active Directory, RBAC |
| 온톨로지 도구 | Protégé, TopBraid Composer |
| 클라우드 | AWS Marketplace, Azure Marketplace, GCP |
| API | REST API, Java API, SPARQL Endpoint |
| 시각화 | Stardog Studio, Stardog Explorer |

---

## 출처

- https://www.stardog.com/
- https://www.stardog.com/platform/
- https://www.stardog.com/agentic-ai-knowledge-graph/
- https://www.stardog.com/pricing/
- https://aws.amazon.com/marketplace/pp/prodview-ulfm6fel7xgjq
- https://info.stardog.com/stardog-at-kgc-2026
- https://www.g2.com/products/stardog/reviews
- https://medium.com/@appi.bh/what-i-learned-building-with-neo4j-and-stardog-a-practitioners-perspective-on-graph-technology-25d16d882587
