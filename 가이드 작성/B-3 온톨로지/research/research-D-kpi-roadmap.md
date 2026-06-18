# B-3 온톨로지 — KPI·Roadmap·주제 경계 리서치

> 클러스터 D: 성과 지표(KPI) + 고도화 Roadmap + 다른 주제와의 경계
> 조사 기준일: 2026-06-18

---

## 1. 성과 지표(KPI)

온톨로지의 성과는 "AI가 맥락·연결성을 이해하는 데 필요한 지식 데이터가 얼마나 잘 준비되어 있는가"로 측정한다. 아래 4개 지표로 충분하다 — 부풀리지 않는다.

---

### KPI-1. 핵심 개념 모델링 비율 (Concept Coverage Rate)

**쉬운 의미**
업무에서 실제로 쓰이는 핵심 개념(제품·공정·결함·원인·조치 등) 중 온톨로지에 정의된 비율.
예: 품질 RCA에 필요한 개념 50개 중 40개가 모델링되어 있으면 80%.

**측정 방법**
> 모델링된 핵심 개념 수 ÷ 전체 식별된 핵심 개념 수 × 100

- 분모: 도메인 전문가와 SME가 "RCA·추천에 반드시 필요하다"고 식별한 개념 수
- 분자: 온톨로지에 클래스/개체(entity)로 등록된 개념 수

**측정 목적(왜 재나)**
온톨로지가 실제 업무 지식을 빠짐없이 포괄하는지 확인. 커버리지가 낮으면 AI가 "모르는 개념"이 생겨 추론 오류 발생.

**방향 / 기대효과**
↑ 목표치 80% 이상 → 핵심 도메인 내 AI 추론 공백 최소화.

**제조(두산) 예시**
두산밥캣 유압 계통 RCA 온톨로지: 설비-부품-결함-원인-SOP 개념 60개 중 48개 모델링 → 커버리지 80%. 나머지 12개는 2단계 AI 보조 단계에서 추가 목표.

**참고**
- Instantiated Class Ratio(ICR) 개념: 온톨로지에 정의된 클래스 중 실제 인스턴스가 있는 비율 ([Structural Quality Metrics to Evaluate Knowledge Graphs, arXiv 2022](https://arxiv.org/pdf/2211.10011))
- Manufacturing ontology success metrics ([ScienceDirect, 2020](https://www.sciencedirect.com/science/article/pii/S2351978920301177))

---

### KPI-2. 개념-데이터-문서 연결 비율 (Relation Fill Rate)

**쉬운 의미**
온톨로지에 등록된 개념이 실제 데이터(테이블·필드)·문서(SOP·PFMEA·C/S Report)와 연결된 비율.
예: "결함" 개념이 QMS 결함 테이블·PFMEA 항목·C/S Report 섹션과 3개 모두 연결되어 있으면 100%.

**측정 방법**
> 연결이 완성된 (개념, 데이터/문서) 매핑 수 ÷ 목표 매핑 전체 수 × 100

- 목표 매핑: 온톨로지 설계 시 "연결해야 한다"고 지정한 개념-자산 쌍
- 연결 완성: 카탈로그·메타데이터·문서 청크와 실제 링크가 존재

**측정 목적(왜 재나)**
개념과 데이터가 연결되어야 RAG 검색·원인분석 추천이 실제로 작동함. 연결 비율이 낮으면 온톨로지가 "지도만 있고 도로가 없는" 상태.

**방향 / 기대효과**
↑ 목표치 70% 이상 → GraphRAG 기반 문서 검색 적중률 향상. 제조 도메인 GraphRAG 실험에서 온톨로지 기반 KG가 20문항 중 18개 정답(90%) 달성 ([MDPI Electronics, 2025](https://www.mdpi.com/2079-9292/14/11/2102)).

**제조(두산) 예시**
두산테스나 반도체 공정 온톨로지: "불량 모드" 개념을 MES 불량 테이블·공정 SOP·C/S Report 3개 자산과 매핑. 초기 매핑 60% → 1단계 완료 후 75% → 2단계 AI 보조 추출로 90% 목표.

**참고**
- Interlinking completeness 개념 ([AAAI-SS KG Quality, 2025](https://ojs.aaai.org/index.php/AAAI-SS/article/download/36888/39026/40965))
- Ontology-guided GraphRAG accuracy ([arXiv 2511.05991](https://arxiv.org/html/2511.05991v1))

---

### KPI-3. 관계 기반 추천·검색 적중률 (Relation-based Retrieval Accuracy)

**쉬운 의미**
온톨로지 관계를 활용한 검색·추천이 실제로 맞는 비율. 키워드 검색 대비 얼마나 더 정확한가.
예: "용접부 균열" 입력 시 온톨로지가 "소재 결함→열처리 공정→SOP-042" 경로를 따라 추천한 문서가 전문가 기준 맞는 비율.

**측정 방법**
> AI 추천·검색 결과 중 전문가가 "관련 있다"고 평가한 건수 ÷ 전체 추천 건수 × 100

- 측정 주기: 분기별 샘플 평가 (전문가 20~30건 검수)
- 비교 기준: 동일 질의에 대한 키워드 검색 적중률

**측정 목적(왜 재나)**
온톨로지가 실제 업무 추론에 기여하는지 직접 검증. 커버리지가 높아도 추천이 틀리면 온톨로지 구조·관계 정의에 문제.

**방향 / 기대효과**
↑ 키워드 검색 대비 10~20%p 이상 개선 → 원인분석·조치 추천 신뢰도 향상, 전문가 재검토 공수 감소.

**제조(두산) 예시**
밥캣 서비스 매뉴얼 검색: 키워드 검색 적중률 55% → 온톨로지 기반 GraphRAG 적용 후 75% 목표. "유압 누유" 검색 시 "시일 결함→압력 초과→점검 항목" 경로로 연관 SOP 자동 추천.

**참고**
- GraphRAG manufacturing QA accuracy 90% ([MDPI Electronics 2025](https://www.mdpi.com/2079-9292/14/11/2102))
- SemRAG: Semantic Knowledge-Augmented RAG ([arXiv 2507.21110](https://arxiv.org/pdf/2507.21110))

---

### KPI-4. 전문가 검수 반영 속도 (Expert Review Cycle Time)

**쉬운 의미**
온톨로지 변경 요청(신규 개념·관계 추가, 오류 수정)이 제기된 후 전문가 검토를 거쳐 반영·배포되는 데 걸리는 평균 시간(일).
예: 평균 14일 → 7일 이하로 단축.

**측정 방법**
> 온톨로지 변경 요청 접수일 ~ 승인·배포 완료일의 평균(일)

- 대상: 신규 개념 등록, 관계 수정, 오류 수정, AI 추출 후보 검수 요청 모두 포함
- 운영 시스템: Ontology Registry(변경 이력·버전 관리)

**측정 목적(왜 재나)**
온톨로지는 살아있는 지식이다. 변경이 느리면 AI 추론에 낡은 지식이 남아 오류 발생. 2단계(AI 보조) 이후에는 AI가 대량 후보를 추출하므로 검수 속도가 병목.

**방향 / 기대효과**
↓ 목표 7일 이내 → 지식 최신성 유지, AI 품질 저하 방지. ML 기반 품질 평가 프레임워크 적용 시 온톨로지 개발 시간 42% 단축 사례 ([Ontology Quality Improvement, MDPI 2025](https://www.mdpi.com/2079-8954/14/2/154)).

**제조(두산) 예시**
두산에너빌리티 설비 온톨로지: 현장 정비팀이 신규 결함 유형 제안 → 데이터 스튜어드 검토 → 온톨로지 관리자 승인. 현재 평균 21일 → 목표 7일(2단계: AI 초안 자동 생성으로 검수 부담 감소).

**참고**
- Ontology governance and stewardship ([Enterprise Knowledge, 2024](https://enterprise-knowledge.com/how-to-optimize-data-governance-with-enterprise-knowledge-graphs/))
- Ontology quality improvement cycle time ([MDPI Systems 2025](https://www.mdpi.com/2079-8954/14/2/154))

---

## 2. 고도화 Roadmap — 단계별 발전 서사

온톨로지는 한 번에 완성하는 것이 아니라 단계적으로 키운다. 아래 3단계는 "준비되는 것"을 중심으로 기술한다.

---

### 1단계: 수기 핵심 정의 (도메인 시드 구축)

**언제:** 온톨로지 착수 초기 (0~6개월)

**무엇을 하나**
- 도메인 전문가(SME)와 데이터 오너가 직접 핵심 개념·관계를 화이트보드에서 정의
- 작은 범위 집중: 한 계열사의 한 도메인(예: 품질 RCA) 먼저
- 수작업으로 개념 목록 작성 → Glossary 연결 → 핵심 데이터 매핑

**준비되는 것**
- 핵심 개념 20~50개, 관계 정의서
- 공통 온톨로지 골격 (지주-계열사 공통 상위 개념)
- 개념-데이터 매핑표 초안

**제약**
- 전문가 시간 투입 필요
- 커버리지 낮음 (40~60%), 갱신 속도 느림

**참고**
- Manual ontology curation → AI-assisted evolution ([arXiv 2412.00608](https://arxiv.org/pdf/2412.00608))

---

### 2단계: AI 보조 확장 (Human-in-the-loop 추출)

**언제:** 핵심 시드가 안정된 후 (6~18개월)

**무엇을 하나**
- LLM이 사내 문서(SOP·PFMEA·C/S Report·기술 매뉴얼)에서 개념·관계 후보를 자동 추출
- 전문가는 AI 초안을 검수·승인·수정하는 역할로 전환
- Ontology Registry에서 버전 관리·변경 이력 추적

**준비되는 것**
- 커버리지 70~85%: 문서 기반 개념·관계 대폭 확충
- 개념-문서 자동 링크 (RAG 소스 연결)
- 검수 사이클 단축 (AI 초안 → 전문가 확인)

**기술 배경**
LLM을 활용한 자동 온톨로지 추출: 세 에이전트(온톨로지 생성·확장 → 정제 → KG 채우기) 구조로 수작업 대비 80% 시간 단축 가능 ([arXiv 2511.11017](https://www.arxiv.org/pdf/2511.11017)).

**제조(두산) 예시**
두산밥캣: 서비스 매뉴얼 800건을 LLM으로 분석 → "부품-결함-원인" 관계 후보 200개 자동 추출 → 서비스 엔지니어 2명이 2주 내 검수·확정. 1단계 대비 커버리지 +25%p.

---

### 3단계: 자율 확장·GraphRAG 본격 활용 (Continuous KG)

**언제:** 온톨로지 운영 성숙 후 (18개월 이상)

**무엇을 하나**
- 신규 문서가 유입되면 온톨로지 자동 업데이트 (Continuous Ingestion)
- 지식그래프(Knowledge Graph) 기반 GraphRAG로 원인분석·유사 사례 추천 본격 서비스
- 피드백 루프: 추천 오류 → 온톨로지 자동 개선 후보 생성 → 경량 검수

**준비되는 것**
- 커버리지 90% 이상: 계열사 전 도메인 확장
- 자율 갱신 파이프라인: 문서 → 개념·관계 추출 → 자동 등록 → 전문가 경량 검수
- GraphRAG 적중률 85% 이상 목표

**기술 배경**
Agentic KG: 지속적으로 데이터를 흡수하고 온톨로지를 진화시키며 오류를 자기 수정하는 구조 ([Educative.io, 2025](https://www.educative.io/blog/how-to-build-an-agentic-knowledge-graph)).

**제조(두산) 예시**
두산에너빌리티: 매월 발행되는 정비 이력 보고서가 자동으로 온톨로지 후보를 생성 → 데이터 스튜어드가 월 1회 일괄 검수 → 지식그래프 자동 갱신. 설비 고장 원인분석 소요시간 50% 단축 목표.

---

## 3. 다른 주제와의 경계(역할 분담)

온톨로지(B-3)는 "개념 간 관계 구조를 준비"하는 것이다. 아래 인접 주제와 혼동하지 않는다.

---

| 인접 주제 | 그 주제의 역할 | B-3 온톨로지의 역할 | 핵심 경계 |
|---|---|---|---|
| **A-3 비즈니스 Glossary** | 단일 용어의 "뜻"을 표준화 (단어 → 정의) | 개념 간 "관계"를 구조화 (개념 A → 관계 → 개념 B) | Glossary는 단어 사전, 온톨로지는 관계 지도 |
| **A-2 메타데이터** | 데이터 필드·테이블의 속성(타입·단위·단위) 설명 | 업무 개념과 데이터 필드를 의미적으로 연결 | 메타데이터는 "이 필드가 무엇인가", 온톨로지는 "이 개념이 저 개념과 어떻게 연결되는가" |
| **A-1 데이터 카탈로그** | 데이터 자산의 위치·소재·접근 경로 파악 | 개념과 데이터 자산을 의미 기반으로 연결 | 카탈로그는 "어디 있는가", 온톨로지는 "왜 연결되는가" |
| **B-2 데이터 해설/주석** | AI 학습용 라벨·분류 부여 (학습 데이터 준비) | 개념 간 관계 구조 정의 (지식 준비) | 주석은 학습 데이터 라벨링, 온톨로지는 개념 관계망 |
| **D계열 AI 검색·에이전트** | 온톨로지를 "사용"해 추론·검색·추천 실행 | AI가 사용할 지식 구조를 "준비" | B-3은 준비·정의 담당, D계열은 활용·실행 담당 |

---

### 세부 경계 설명

#### A-3 Glossary vs B-3 온톨로지
- Glossary: "결함(Defect) = 제품이 요구 사양을 충족하지 못하는 상태" (단어 → 정의 1개)
- 온톨로지: "결함 → 원인이 된다 → 공정 조건 / 결함 → 검출된다 → 검사 항목 / 결함 → 조치한다 → SOP" (개념 → 관계 → 개념 N개)
- Glossary의 표준 용어가 온톨로지 개념의 이름(label)으로 쓰인다 — Glossary가 먼저, 온톨로지가 그 위에서 관계를 연결.

**참고:** [Data Catalog vs Glossary vs Ontology, data.world 2022](https://data.world/blog/data-catalog-knowledge-graph/), [ER/Studio Glossary guide](https://erstudio.com/blog/making-data-work-the-role-of-glossaries-dictionaries-and-catalogs/)

#### A-2 메타데이터 vs B-3 온톨로지
- 메타데이터: QMS 결함 테이블의 DEF_CD 컬럼 → "결함 유형 식별 코드, 문자열, 허용값: A~Z"
- 온톨로지: "결함 유형 개념 → is-a → 품질 결함 / 결함 유형 → caused-by → 공정 조건"
- 메타데이터는 필드 수준, 온톨로지는 개념 수준. 온톨로지가 메타데이터를 "의미 있는 개념"으로 승격시킨다.

**참고:** [What's the Difference Between an Ontology and a Knowledge Graph?, Enterprise Knowledge](https://enterprise-knowledge.com/whats-the-difference-between-an-ontology-and-a-knowledge-graph/)

#### A-1 데이터 카탈로그 vs B-3 온톨로지
- 카탈로그: "결함 데이터 → QMS 시스템 → 담당: 품질팀 → 접근: VPN 필요"
- 온톨로지: "결함 개념 → 연결된 데이터: QMS 결함 테이블, PFMEA 항목, C/S Report → 관계: '발생한다' '원인이 된다'"
- 카탈로그가 자산을 찾아주면, 온톨로지가 그 자산이 다른 개념과 어떻게 연결되는지를 설명한다. 온톨로지 기반 카탈로그가 KG-powered catalog로 발전하는 것이 이 관계.

**참고:** [Data Catalog powered by Knowledge Graph, data.world 2022](https://data.world/blog/data-catalog-knowledge-graph/)

#### B-2 데이터 해설/주석 vs B-3 온톨로지
- B-2: 결함 이미지에 "긁힘/함몰/균열" 라벨을 붙인다 → AI 학습용 분류 체계
- B-3: "긁힘(개념) → is-a → 표면 결함 / 긁힘 → caused-by → 이송 장치 접촉" → 개념 간 관계 정의
- B-2의 라벨 taxonomy가 B-3 온톨로지의 개념 계층으로 연결될 수 있다 — 라벨 체계가 먼저 안정되면 온톨로지 구조에 반영.

#### D계열(AI 검색·에이전트) vs B-3 온톨로지
- D계열: 온톨로지를 사용해 GraphRAG 쿼리를 실행하거나, 에이전트가 관계 기반 추론을 수행
- B-3: 그 에이전트가 "읽을" 개념·관계 구조 데이터를 준비·정의·유지
- B-3은 식재료 준비, D계열은 요리 실행. B-3이 없으면 D계열 추론은 단순 키워드 검색 수준에 머문다.

---

## 참고자료 종합

| # | 제목 | URL | 접속일 |
|---|---|---|---|
| 1 | Metrics to gauge the success of a manufacturing ontology | https://www.sciencedirect.com/science/article/pii/S2351978920301177 | 2026-06-18 |
| 2 | A Brief Overview of Key Quality Metrics for Knowledge Graph Solution (AAAI-SS) | https://ojs.aaai.org/index.php/AAAI-SS/article/download/36888/39026/40965 | 2026-06-18 |
| 3 | Structural Quality Metrics to Evaluate Knowledge Graphs (arXiv 2022) | https://arxiv.org/pdf/2211.10011 | 2026-06-18 |
| 4 | Document GraphRAG for Manufacturing Domain (MDPI Electronics 2025) | https://www.mdpi.com/2079-9292/14/11/2102 | 2026-06-18 |
| 5 | Ontology Learning and Knowledge Graph Construction — Impact on RAG Performance (arXiv 2511.05991) | https://arxiv.org/html/2511.05991v1 | 2026-06-18 |
| 6 | AI Agent-Driven Automated Product Knowledge Graph Construction (arXiv 2511.11017) | https://www.arxiv.org/pdf/2511.11017 | 2026-06-18 |
| 7 | Leveraging LLM for Automated Ontology Extraction and KG Generation (arXiv 2412.00608) | https://arxiv.org/pdf/2412.00608 | 2026-06-18 |
| 8 | How to Build an Agentic Knowledge Graph (Educative.io 2025) | https://www.educative.io/blog/how-to-build-an-agentic-knowledge-graph | 2026-06-18 |
| 9 | Ontology Quality Improvement in Educational KGs (MDPI Systems 2025) | https://www.mdpi.com/2079-8954/14/2/154 | 2026-06-18 |
| 10 | What's the Difference Between an Ontology and a Knowledge Graph? (Enterprise Knowledge) | https://enterprise-knowledge.com/whats-the-difference-between-an-ontology-and-a-knowledge-graph/ | 2026-06-18 |
| 11 | How to Optimize Data Governance with Enterprise KGs (Enterprise Knowledge) | https://enterprise-knowledge.com/how-to-optimize-data-governance-with-enterprise-knowledge-graphs/ | 2026-06-18 |
| 12 | What Does It Mean for a Data Catalog to Be Powered by a Knowledge Graph? (data.world) | https://data.world/blog/data-catalog-knowledge-graph/ | 2026-06-18 |
| 13 | The Difference Between a Data Catalogue and a Glossary (LinkedIn) | https://www.linkedin.com/pulse/difference-between-data-catalogue-glossary-nicola-askham | 2026-06-18 |
| 14 | SemRAG: Semantic Knowledge-Augmented RAG (arXiv 2507.21110) | https://arxiv.org/pdf/2507.21110 | 2026-06-18 |
| 15 | Knowledge Graph vs Ontology: Know Differences (PuppyGraph) | https://www.puppygraph.com/blog/knowledge-graph-vs-ontology | 2026-06-18 |
