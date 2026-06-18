# B-3 온톨로지 — How 클러스터 리서치

> 담당 클러스터: **구축 절차(방법론) + 솔루션·도구 맵 + AI 활용을 위한 데이터 연결 + 운영·변경관리 + 제조(두산) 예시**
> 관점 고정: "AI/Agent를 만드는 법"이 아니라 "AI가 쓸 지식 데이터를 준비·정비하는 법"
> 작성일: 2026-06-18

---

## 1. 구축 방법론 — 표준 절차 정리

### 1.1 세 가지 대표 방법론 요약

#### Ontology 101 (Noy & McGuinness, Stanford, 2001)
가장 많이 인용되는 입문 가이드. 단계가 단순하고 현업 눈높이에 적합하여 **처음 시작하는 팀에 추천**.

| 단계 | 내용 |
|------|------|
| 1. 범위 결정 | 어떤 질문에 답해야 하는가? 온톨로지가 다룰 도메인과 경계를 정한다 |
| 2. 기존 온톨로지 재사용 검토 | schema.org, FIBO, 업계 표준 온톨로지 재사용 가능한지 확인 |
| 3. 핵심 용어 열거 | 도메인의 중요한 단어들을 브레인스토밍으로 나열 (A-3 Glossary 연계) |
| 4. 클래스(개념) 정의·계층 설계 | 상위-하위 관계(is-a)를 정의하고 계층 구조를 만든다 |
| 5. 클래스 속성(Property) 정의 | 각 개념이 갖는 속성(필드)을 정의한다 |
| 6. 제약 조건(Restriction) 정의 | 속성값 범위·카디널리티 등 제약을 건다 |
| 7. 인스턴스(실제 데이터) 적재 | 개별 개체를 클래스에 분류하여 트리플로 적재 |

출처: [Ontology Development 101 (Noy & McGuinness)](https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html) (접속일: 2026-06-18)

---

#### METHONTOLOGY (Madrid Polytechnic, 1997~)
소프트웨어 공학의 생명주기를 온톨로지에 적용한 방법론. **체계적 관리·문서화가 필요한 엔터프라이즈 프로젝트에 적합**.

**생명주기 단계:**
1. **명세(Specification)** — 목적, 범위, 최종 사용자 정의
2. **개념화(Conceptualisation)** — 중간 표현(Concept Table, Attribute Table 등)으로 지식 구조화
3. **형식화(Formalisation)** — 반형식 언어(Semi-formal)로 표현
4. **통합(Integration)** — 기존 온톨로지 재사용·병합
5. **구현(Implementation)** — OWL/RDF 등 공식 언어로 변환
6. **유지보수(Maintenance)** — 변경·버전 관리 반복

**관리 활동(전 단계 공통):** 일정·품질·형상 관리, 지식 획득, 문서화, 평가

출처: [METHONTOLOGY: from ontological art towards ontological engineering (ResearchGate)](https://www.researchgate.net/publication/50236211_METHONTOLOGY_from_ontological_art_towards_ontological_engineering) (접속일: 2026-06-18)

---

#### NeOn Methodology (2006~)
온톨로지 네트워크(여러 온톨로지 연결)와 재사용을 강조. **분산 팀, 계열사별 확장이 필요한 경우에 적합**.

핵심 아이디어: 온톨로지 설계 패턴(ODP, Ontology Design Pattern)을 찾아 재조합. 시나리오 기반(9개 시나리오)으로 어떤 경우에 어떤 방법으로 온톨로지를 만들지 결정.

**단계:** (1) 요구사항 식별 → (2) 기존 패턴/온톨로지 탐색 → (3) 문제 분해 → (4) 패턴 매핑·적용 → (5) 부분 설계 평가 → (6) 통합

출처: [NeOn Methodology for Building Ontology Networks (ResearchGate)](https://www.researchgate.net/publication/49911337_NeOn_Methodology_for_Building_Ontology_Networks_a_Scenario-based_Methodology) (접속일: 2026-06-18)

---

### 1.2 현업용 통합 구축 절차 (7단계 제안)

세 방법론의 장점을 현업 눈높이로 합산한 **정본 절차**. Ontology 101 뼈대에 METHONTOLOGY 개념화·유지보수, NeOn 재사용 전략을 접목.

```
[1단계] 목적·범위 설정
    ↓
[2단계] 지식 원천 취합
    ↓
[3단계] 개념 정제 (용어 충돌·중복 정리)
    ↓
[4단계] 개념·관계·계층 모델링
    ↓
[5단계] 공통/계열사 계층 설계
    ↓
[6단계] 실제 데이터·문서 연결(매핑)
    ↓
[7단계] 검증·품질 점검 → 운영·변경 관리 (반복)
```

#### 각 단계 상세

| 단계 | 핵심 작업 | 산출물 |
|------|-----------|--------|
| **1. 목적·범위 설정** | "어떤 질문에 답해야 하나?" 정의. 작은 업무 하나부터 시작(결함-원인-조치 등). 전사 거대 모델 금지 | 범위 정의서, 핵심 질문 목록 |
| **2. 지식 원천 취합** | PFMEA, SOP, C/S 리포트, 현장 작업 표준, 기존 Glossary 등 문서 수집. A-3 Glossary 연계 확인 | 문서 목록, 용어 후보 목록 |
| **3. 개념 정제** | 동의어·약어 통일(A-3 Glossary와 연계), 중복 제거, 부서별 용어 충돌 조정, 계층 후보 검토 | 정제된 개념 목록, 충돌 해소 로그 |
| **4. 개념·관계·계층 모델링** | 클래스(엔티티), 관계(Relation), 속성(Property) 정의. is-a / part-of / causes / triggers 등 관계 유형 정의 | 개념 정의서, 관계 정의서, 클래스 계층도 |
| **5. 공통/계열사 계층 설계** | 지주: 상위 공통 개념·표준 관계. 계열사: 업무 특화 개념 확장. 연결 방식(Namespace) 정의 | 공통 온톨로지 스키마, 계열사 확장 스키마 |
| **6. 실제 데이터·문서 연결(매핑)** | 개념 → 실제 데이터 필드·문서 매핑. PFMEA 항목, 검사 결과 테이블 컬럼을 온톨로지 클래스에 연결. 관계 인스턴스(트리플) 적재 | 개념-데이터 매핑표, 트리플 데이터셋 |
| **7. 검증·품질 점검** | SHACL 제약 검증, 추론 결과 검토, 현업 SME 검수, AI 검색 결과 테스트 | 검증 리포트, 변경 로그 |

---

### 1.3 "작게 시작" 원칙 — 왜 중요한가

전사 거대 온톨로지를 처음부터 만들려 하면 반드시 실패한다. 이유:

- **범위 폭발(Scope creep):** 개념이 늘어날수록 관계도 기하급수적으로 증가 → 완성 불가
- **SME 참여 피로:** 너무 넓으면 현업 전문가가 검수·확인하기 어려움
- **AI 연결 지연:** 작은 모델도 없으면 AI 활용은 시작조차 못함

**권장 시작 범위:** 한 공장·한 제품군의 결함-원인-조치 관계처럼 "인과 관계가 명확하고 AI에 자주 묻는 질문이 집중된 업무"부터.

---

## 2. 솔루션·도구 맵

### 2.1 유형별 도구 전체 목록

| 유형 | 도구명 | 한 줄 설명 | 공식 URL |
|------|--------|-----------|---------|
| **그래프 DB (Property Graph)** | Neo4j | 노드-관계 구조의 그래프 DB. Cypher 쿼리 언어. AuraDB 관리형 클라우드 제공. 커뮤니티판 오픈소스 | [neo4j.com](https://neo4j.com/product/neo4j-graph-database/) |
| **그래프 DB (완전 관리형)** | Amazon Neptune | AWS 완전 관리형. RDF(SPARQL) + 속성 그래프(Gremlin/OpenCypher) 동시 지원. 서버리스 옵션 | [aws.amazon.com/neptune](https://aws.amazon.com/neptune/) |
| **RDF 트리플스토어 (온톨로지 특화)** | Ontotext GraphDB | W3C 표준 RDF 트리플스토어. OWL 추론, Lucene/Elasticsearch 검색 커넥터. Free판 무료 | [graphdb.ontotext.com](https://graphdb.ontotext.com/) |
| **RDF 트리플스토어 (추론 특화)** | Stardog | SPARQL 1.1 + OWL 추론 + SHACL 검증. 가상 그래프(Virtual Graph)로 기존 DB 연결 | [stardog.com/platform](https://www.stardog.com/platform/) |
| **고성능 인메모리 추론 엔진** | RDFox | 세계 최고속 인메모리 추론 엔진. 삼성전자 인수(2025). 엣지·IoT 배포 지원. 실시간 증분 추론 | [oxfordsemantic.tech/rdfox](https://www.oxfordsemantic.tech/rdfox) |
| **오픈소스 Java 프레임워크** | Apache Jena + TDB | Java 기반 RDF/OWL 처리 프레임워크. TDB 네이티브 트리플스토어. Fuseki SPARQL 서버 내장. 완전 무료 | [jena.apache.org](https://jena.apache.org/) |
| **온톨로지 편집기** | Protégé | Stanford 개발 오픈소스 OWL 편집기. 데스크톱판 + 웹협업판(WebProtégé). 플러그인 생태계 풍부 | [protege.stanford.edu](https://protege.stanford.edu/) |
| **엔터프라이즈 시맨틱 관리** | PoolParty Semantic Suite | SKOS/OWL 기반 온톨로지·분류체계 관리. 텍스트 마이닝·자동 태깅. 상용 | [poolparty.biz/ontology-management](https://www.poolparty.biz/ontology-management) |
| **엔터프라이즈 지식 그래프 관리** | TopBraid EDG | OWL 편집 + SHACL 검증 + 20개 이상 내장 온톨로지. 벡터 DB 내장(v8.0). 상용 | [topquadrant.com](https://www.topquadrant.com/resources/overview-of-topbraid-edg-ontologies/) |

> **가격 주의:** 위 상용 도구들은 버전·계약 조건에 따라 가격이 달라짐. 반드시 PoC 전 공식 견적 확인.

---

### 2.2 도구 선정 기준

| 기준 | 설명 |
|------|------|
| **표현력** | OWL(복잡한 논리 추론 필요)인가, SKOS(단순 분류체계)인가? 업무 복잡도에 맞게 선택 |
| **추론 지원** | is-a 계층 추론, 규칙 기반 추론이 필요한가? → RDFox, Stardog, GraphDB가 강점 |
| **현업 접근성** | GUI 편집기 필요 → Protégé, PoolParty, TopBraid EDG. 개발팀 주도 → Neo4j, Apache Jena |
| **기존 데이터 연동** | RDB·ERP 연동 필요 → Stardog 가상 그래프, Neo4j 커넥터, Neptune 다중 모델 |
| **운영 부담** | 완전 관리형(운영 부담 최소) → Amazon Neptune, Neo4j AuraDB |
| **초기 진입 비용** | PoC부터 무료로 시작 → Neo4j Community, GraphDB Free, Apache Jena, Protégé |

---

### 2.3 단계별 도구 조합 추천 (제조 중소~중견 계열사)

```
[1] 개념 모델링·편집 → Protégé (무료)
         ↓
[2] 저장·검색 (초기 PoC) → GraphDB Free 또는 Apache Jena/TDB (무료)
         ↓
[3] 운영 확장 (현업 도입) → Neo4j Community/Enterprise 또는 Amazon Neptune
         ↓
[4] 엔터프라이즈 거버넌스 필요 시 → PoolParty 또는 TopBraid EDG 검토
```

---

## 3. AI 활용을 위한 데이터 연결 관점

### 3.1 온톨로지 기반 GraphRAG — 데이터 준비 관점

전통적인 벡터 기반 RAG의 한계:
- 단순 키워드 유사도 검색 → "균열"로 검색 시 "표면 균열"·"내부 균열"·"열 균열"을 동일하게 취급
- 다중 홉(multi-hop) 추론 불가 → "균열 원인 → 열처리 불량 → 온도 제어 이상 → 설비 교체"로 이어지는 연쇄 관계를 따라가지 못함

온톨로지 연결로 가능해지는 것:

| 활용 시나리오 | 온톨로지 역할 | 필요한 데이터 준비 |
|-------------|------------|-----------------|
| **개념 확장 검색** | "균열(Crack)" 검색 시 하위 개념(표면균열, 내부균열) 자동 포함 | 계층 관계(is-a) 적재 |
| **원인 분석** | 결함 → 원인 → 근본 원인으로 경로 탐색 | causes / triggered-by 관계 트리플 적재 |
| **유사 사례 추천** | 동일 원인·동일 조치를 공유하는 과거 사례 연결 | 사례 인스턴스 → 결함·원인·조치 클래스 매핑 |
| **조치 추천** | 확인된 원인과 연결된 표준 조치 항목 반환 | hasAction 관계 트리플 적재 |

**GraphRAG 아키텍처에서 온톨로지의 위치:**
1. 온톨로지 스키마 정의 (클래스·관계 정의서)
2. 비정형 문서(SOP, PFMEA, C/S Report) → LLM으로 개체(entity) 추출 시 온톨로지 스키마를 제약 조건으로 사용 → 일관된 추출
3. 추출된 개체·관계 → 그래프 DB에 트리플로 적재
4. RAG 검색 시: 키워드 → 온톨로지로 개념 확장 → 확장된 개념으로 벡터 검색 + 그래프 탐색 결합

출처: [Ontology-Driven Knowledge Graph for GraphRAG (deepsense.ai)](https://deepsense.ai/resource/ontology-driven-knowledge-graph-for-graphrag/) (접속일: 2026-06-18)
출처: [Document GraphRAG for Manufacturing (MDPI Electronics, 2025)](https://www.mdpi.com/2079-9292/14/11/2102) (접속일: 2026-06-18)

---

### 3.2 관계 인스턴스 적재 — 트리플(Triple) 구조

온톨로지를 AI에 "연결"하려면 실제 데이터를 **트리플(주어-술어-목적어)** 형태로 적재해야 한다.

```
# 기본 트리플 구조
<주어(Subject)> <술어(Predicate)> <목적어(Object)>

# 예시 — 두산 계열사 결함-원인-조치
<표면균열_케이스#001> <hasDefectType> <표면균열(SurfaceCrack)>
<표면균열(SurfaceCrack)> <isSubclassOf> <결함(Defect)>
<표면균열_케이스#001> <hasCause> <열처리불량(HeatTreatmentDefect)>
<열처리불량(HeatTreatmentDefect)> <isSubclassOf> <공정결함(ProcessDefect)>
<표면균열_케이스#001> <hasAction> <열처리조건재설정(HeatTreatmentReset)>
<열처리조건재설정(HeatTreatmentReset)> <isSubclassOf> <공정조치(ProcessAction)>
```

Neo4j Cypher 예시 (속성 그래프 방식):
```cypher
// 노드 생성
CREATE (d:Defect {name: '표면균열', code: 'CRACK-001', type: 'SurfaceCrack'})
CREATE (c:Cause {name: '열처리불량', code: 'CAUSE-012'})
CREATE (a:Action {name: '열처리조건재설정', code: 'ACT-034'})
CREATE (case:Case {id: 'CASE-2024-001', date: '2024-03-15', product: 'BobcatArm'})

// 관계 생성
CREATE (case)-[:HAS_DEFECT]->(d)
CREATE (case)-[:HAS_CAUSE]->(c)
CREATE (case)-[:HAS_ACTION]->(a)
CREATE (d)-[:OFTEN_CAUSED_BY]->(c)
CREATE (c)-[:RESOLVED_BY]->(a)
```

SPARQL 조회 예시 (RDF 트리플스토어 방식):
```sparql
PREFIX mfg: <http://doosan.com/ontology/manufacturing#>

SELECT ?action WHERE {
  ?case mfg:hasDefectType mfg:SurfaceCrack .
  ?case mfg:hasCause ?cause .
  ?case mfg:hasAction ?action .
}
LIMIT 10
```

출처: [Ontologies in Neo4j: Semantics and knowledge graphs (Neo4j Blog)](https://neo4j.com/blog/knowledge-graph/ontologies-in-neo4j-semantics-and-knowledge-graphs/) (접속일: 2026-06-18)

---

## 4. 운영·변경관리

### 4.1 변경 유형별 리스크와 승인 체계

온톨로지는 AI 검색·추론의 "기반 설계도"이므로 변경이 AI 결과 전체에 영향을 준다. 이를 인식하고 변경을 세 단계로 분류하여 관리한다.

| 변경 유형 | 예시 | 리스크 | 승인 |
|----------|------|-------|------|
| **편집적 변경 (Editorial)** | 라벨 수정, 설명 추가, 동의어 추가 | 낮음 — AI 행동 영향 없음 | 도메인 스튜어드(현업 SME) 단독 |
| **추가적 변경 (Additive)** | 새 클래스·관계·속성 추가 | 중간 — 기존 쿼리 영향 없으나 새 연결 필요 | 표준 크로스 도메인 검토 |
| **파괴적 변경 (Breaking)** | 클래스 이름 변경, 관계 삭제, 계층 재편 | 높음 — 기존 AI 쿼리·추론 결과 변경 | 거버넌스 보드 승인 + 마이그레이션 계획 |

출처: [Ontology Management Operating Model: Governance, Versioning & Change Control (Galaxy)](https://www.getgalaxy.io/articles/ontology-management-semantic-modeling-operating-model-enterprise-context) (접속일: 2026-06-18)

---

### 4.2 버전 관리 방법

**시맨틱 버저닝(Semantic Versioning) 적용:**

```
X.Y.Z 형식
X (Major): 파괴적 변경 (계층 재편, 클래스 삭제)
Y (Minor): 추가적 변경 (새 클래스·관계 추가)
Z (Patch): 편집적 변경 (라벨·설명 수정)

예: 결함-원인-조치 온톨로지 v1.2.0
```

**OWL 메타데이터 기록:**
```turtle
# OWL 온톨로지 헤더 예시
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix mfg: <http://doosan.com/ontology/manufacturing#> .

mfg: a owl:Ontology ;
    owl:versionIRI <http://doosan.com/ontology/manufacturing/1.2.0> ;
    owl:versionInfo "1.2.0" ;
    rdfs:comment "결함-원인-조치 온톨로지 v1.2.0. 2024-12-01 균열 하위 유형 3종 추가." .
```

출처: [Best Practices for Implementing FAIR Vocabularies and Ontologies on the Web (arxiv)](https://arxiv.org/pdf/2003.13084) (접속일: 2026-06-18)

---

### 4.3 변경이 AI에 미치는 영향 점검 체크리스트

변경 후 반드시 아래 항목을 점검한다:

```
□ 기존 SPARQL/Cypher 쿼리 결과가 달라졌는가?
□ RAG 검색 결과(개념 확장 범위)가 달라졌는가?
□ SHACL 제약 검증 통과 여부
□ 하위 계열사 확장 온톨로지와 충돌 없는가?
□ 다운스트림 AI 서비스 담당자에게 변경 공지 완료했는가?
□ 변경 로그(이유·날짜·담당자) 기록 완료했는가?
```

---

### 4.4 역할·책임 구조 (RACI 요약)

| 역할 | 책임 |
|------|------|
| **도메인 스튜어드 (현업 SME)** | 개념 제안·비즈니스 맥락 설명·편집적 변경 승인 |
| **온톨로지 설계자 / 시맨틱 아키텍트** | 모델링·표준 준수·크로스 도메인 일관성 유지·추가적 변경 검토 |
| **거버넌스 보드** | 파괴적 변경 최종 승인·네이밍 규칙·호환성 기준 관리 |
| **플랫폼·데이터 팀** | 게시·배포·롤백·SHACL 자동 테스트 파이프라인 운영 |

---

## 5. 제조(두산) 도메인 예시 — 결함-원인-조치 온톨로지

### 5.1 한 업무에서 시작하는 구체 절차 (Bobcat 중장비 암(Arm) 표면 결함 관리 예시)

**[0단계] 시작 결정 기준:**
- Bobcat 암(Arm) 용접 품질 이슈가 반복 발생 → AI에 "이 균열 원인이 뭐지?" 물어보려 하는데 문서가 분산되어 있음
- SOP, PFMEA, C/S Report에 답이 있지만 키워드 검색으론 원인 연결이 안 됨 → 온톨로지 적용 판단

**[1단계] 범위 설정:**
- 대상: Bobcat 암(Arm) 용접 공정 결함 관리
- 핵심 질문: "이 결함 유형에 가장 자주 나오는 원인은? 지금까지 어떤 조치가 효과적이었나?"

**[2단계] 지식 원천 취합:**

| 문서 | 포함 내용 |
|------|----------|
| PFMEA (2023~2024) | 잠재적 결함 유형, 잠재 원인, 현행 관리 방법 |
| SOP #W-023 용접 표준 | 용접 온도·속도·재료 기준 |
| C/S Report 48건 | 실제 발생 결함·원인·조치 이력 |
| A-3 Glossary (기존 작성) | 표준 결함명·공정명 용어 |

**[3단계] 개념 정제:**
- C/S Report에서 "표면 크랙", "크랙 발생", "crack"이 모두 같은 개념 → A-3 Glossary 연계하여 `표면균열(SurfaceCrack)`으로 통일
- "용접 불량", "용착 불량", "용접부 결함"이 혼용 → 상위 클래스 `용접결함(WeldingDefect)` + 하위 클래스 설계

**[4단계] 개념·관계·계층 모델링:**

```
[클래스 계층]
결함(Defect)
├── 표면결함(SurfaceDefect)
│   ├── 표면균열(SurfaceCrack)
│   └── 표면기공(SurfacePorosity)
└── 용접결함(WeldingDefect)
    ├── 용접균열(WeldCrack)
    └── 용접미용착(IncompleteFusion)

원인(Cause)
├── 재료결함(MaterialDefect)
├── 공정결함(ProcessDefect)
│   ├── 열처리불량(HeatTreatmentDefect)
│   └── 용접속도불량(WeldingSpeedDefect)
└── 설비결함(EquipmentDefect)

조치(Action)
├── 공정조치(ProcessAction)
│   ├── 열처리조건재설정(HeatTreatmentReset)
│   └── 용접파라미터조정(WeldParamAdjust)
└── 설비조치(EquipmentAction)
    └── 노즐교체(NozzleReplacement)

[관계 유형]
- hasCause: 결함 → 원인
- hasAction: 결함 또는 원인 → 조치
- isSubclassOf: 하위 개념 → 상위 개념
- OFTEN_CAUSED_BY: 결함 유형 → 자주 발생하는 원인 (통계 기반)
- RESOLVED_BY: 원인 → 효과적인 조치 (이력 기반)
```

**[5단계] 공통/계열사 계층 설계:**
- 지주 공통: `결함(Defect)`, `원인(Cause)`, `조치(Action)` 상위 클래스 + 표준 관계 유형
- Bobcat 특화: `용접결함`, `열처리불량` 등 현장 특화 하위 클래스

**[6단계] 실제 데이터 연결(매핑) 및 트리플 적재:**

```
C/S Report #2024-083:
  - 결함: 표면균열(SurfaceCrack) → 클래스 인스턴스로 적재
  - 원인: 열처리불량(HeatTreatmentDefect) → 클래스 인스턴스로 적재
  - 조치: 열처리조건재설정(HeatTreatmentReset) → 클래스 인스턴스로 적재
  - 관계 트리플: CASE-083 hasCause 열처리불량
                CASE-083 hasAction 열처리조건재설정

PFMEA 항목 #W-023-F-3:
  - 결함 유형: 표면균열 → 온톨로지 클래스 연결
  - 잠재 원인: 용접속도불량 → 온톨로지 클래스 연결
```

**[7단계] 검증:**
- Protégé의 Reasoner로 계층 일관성 확인
- SHACL 규칙으로 "모든 Case는 hasCause를 반드시 가져야 한다" 검증
- 현업 품질 담당자가 50건 샘플 검수

---

### 5.2 그래프 DB 적재 후 AI 활용 흐름 (데이터 준비 관점)

**시나리오: AI에게 "이 균열 원인과 조치 추천해줘"라고 물었을 때**

```
[현장 작업자 질문]
"암(Arm) 표면에 균열이 생겼는데 원인이 뭔가요?"

[데이터 준비 관점의 흐름]
1. 온톨로지에서 '균열(Crack)' → 'SurfaceCrack', 'WeldCrack' 등 하위 개념 확인
   (이 매핑이 사전에 그래프 DB에 적재되어 있어야 함)

2. 그래프 DB에서 관계 탐색:
   SurfaceCrack → [OFTEN_CAUSED_BY] → HeatTreatmentDefect (48건 중 31건)
   SurfaceCrack → [OFTEN_CAUSED_BY] → WeldingSpeedDefect (48건 중 12건)

3. 원인 확인 후 조치 연결:
   HeatTreatmentDefect → [RESOLVED_BY] → HeatTreatmentReset (성공률 87%)

4. RAG에 전달: 그래프에서 가져온 관계 정보 + 관련 SOP/PFMEA 문서 청크 결합
   → AI가 구체적인 조치 답변 생성
```

**이 흐름에 필요한 데이터 준비:**
- C/S Report 48건의 결함-원인-조치를 트리플로 변환하여 적재 ✓
- PFMEA 항목을 온톨로지 클래스에 매핑 ✓
- 각 관계에 발생 빈도·성공률 등 통계 속성 기록 ✓
- 연결된 SOP 문서를 청크로 분할·임베딩하여 벡터 DB에 저장 ✓

---

## 6. 참고 자료 (References)

| 출처 | URL | 접속일 |
|------|-----|--------|
| Ontology Development 101 (Noy & McGuinness, Stanford) | https://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html | 2026-06-18 |
| NeOn Methodology (ResearchGate) | https://www.researchgate.net/publication/49911337_NeOn_Methodology_for_Building_Ontology_Networks_a_Scenario-based_Methodology | 2026-06-18 |
| METHONTOLOGY (ResearchGate) | https://www.researchgate.net/publication/50236211_METHONTOLOGY_from_ontological_art_towards_ontological_engineering | 2026-06-18 |
| Neo4j 공식 제품 페이지 | https://neo4j.com/product/neo4j-graph-database/ | 2026-06-18 |
| Ontotext GraphDB 공식 | https://graphdb.ontotext.com/ | 2026-06-18 |
| Stardog 플랫폼 | https://www.stardog.com/platform/ | 2026-06-18 |
| RDFox (Oxford Semantic Technologies) | https://www.oxfordsemantic.tech/rdfox | 2026-06-18 |
| Apache Jena 공식 | https://jena.apache.org/ | 2026-06-18 |
| Protégé (Stanford) | https://protege.stanford.edu/ | 2026-06-18 |
| PoolParty Ontology Management | https://www.poolparty.biz/ontology-management | 2026-06-18 |
| TopBraid EDG (TopQuadrant) | https://www.topquadrant.com/resources/overview-of-topbraid-edg-ontologies/ | 2026-06-18 |
| Amazon Neptune | https://aws.amazon.com/neptune/ | 2026-06-18 |
| Ontology Management Operating Model: Galaxy | https://www.getgalaxy.io/articles/ontology-management-semantic-modeling-operating-model-enterprise-context | 2026-06-18 |
| Ontology-Driven GraphRAG (deepsense.ai) | https://deepsense.ai/resource/ontology-driven-knowledge-graph-for-graphrag/ | 2026-06-18 |
| Document GraphRAG for Manufacturing (MDPI Electronics) | https://www.mdpi.com/2079-9292/14/11/2102 | 2026-06-18 |
| Best Practices for FAIR Vocabularies (arxiv) | https://arxiv.org/pdf/2003.13084 | 2026-06-18 |
| Ontologies in Neo4j Blog | https://neo4j.com/blog/knowledge-graph/ontologies-in-neo4j-semantics-and-knowledge-graphs/ | 2026-06-18 |
| Graph RAG Guide 2025 (Salfati Group) | https://salfati.group/topics/graph-rag | 2026-06-18 |
| AWS Neptune vs Neo4j (PuppyGraph) | https://www.puppygraph.com/blog/aws-neptune-vs-neo4j | 2026-06-18 |
| Knowledge Graph Database Comparison (db-engines) | https://db-engines.com/en/system/Amazon+Neptune%3BGraphDB%3BNeo4j | 2026-06-18 |
