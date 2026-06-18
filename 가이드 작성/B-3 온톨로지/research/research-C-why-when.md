# B-3 온톨로지 — Why(왜 필요한가) + When(언제/무엇을 하나) 리서치

> 작성일: 2026-06-18  
> 담당 클러스터: Why(현업 Pain Point + 기대 효과) + When(적용 판단 기준 + 우선 영역)  
> 관점: "AI가 쓸 지식 데이터 준비" — AI/에이전트 구축법 X, 지식 구조 준비법 O

---

## 목차

1. [현업 Pain Point (개념적)](#1-현업-pain-point-개념적)
2. [온톨로지가 푸는 것 / 기대 효과](#2-온톨로지가-푸는-것--기대-효과)
3. [적용 판단 기준 (When)](#3-적용-판단-기준-when)
4. [우선 만들 영역 고르기](#4-우선-만들-영역-고르기)
5. [제조·산업 사례](#5-제조산업-사례)
6. [용어 정리: 온톨로지 vs 글로서리 vs 택소노미](#6-용어-정리-온톨로지-vs-글로서리-vs-택소노미)
7. [출처 목록](#7-출처-목록)

---

## 1. 현업 Pain Point (개념적)

### 1-1. 키워드 검색·문서 검색의 한계

단순 키워드 검색은 **"이 단어가 들어간 문서"**를 찾아줄 뿐, "이 현상이 왜 생겼고 어떻게 조치하나"를 찾아주지 않는다. 예를 들어 제조 현장에서 "균열(crack)"을 검색하면 균열이 언급된 보고서 목록이 나오지만, 균열의 **원인**(과부하·피로·재료 결함)이나 **조치**(보강·교체·검사 주기 조정)로 자동 이어지지 않는다.

**구조적 원인:**
- 지식이 문서(보고서, 매뉴얼, 이메일)로 존재할 뿐 **개념 간 관계**로 저장되어 있지 않다.
- 검색 엔진은 "텍스트 매칭" 또는 "벡터 유사도"를 사용하므로, 명시적으로 적힌 내용만 찾는다. 관계를 따라 추론하지 못한다.

### 1-2. 지식이 흩어져 연결되지 않는 문제

실제 업무에서 하나의 현상(예: 품질 불량)에 관한 지식은 여러 곳에 분산되어 있다:
- 품질 검사 시스템 — 불량 유형 데이터
- ERP/MES — 공정 파라미터, 설비 이력
- 정비 기록 — 설비 교체·보수 이력
- 엔지니어링 문서 — 설계 기준, 허용 범위

이 데이터들은 **서로 다른 용어, 서로 다른 시스템**에 존재한다. "공정 파라미터 이상"이 "품질 불량"으로 이어지는 인과 고리를 컴퓨터가 자동으로 연결하지 못한다.

출처: [Mindbreeze — Demystifying Ontologies in Knowledge Graphs](https://www.mindbreeze.com/blog/demystifying-ontologies-in-knowledge-graphs-building-a-semantic-backbone-for-enterprise-ai) (접속: 2026-06-18)

### 1-3. 글로서리(A-3)만으로 부족한 지점

글로서리(Glossary)는 "용어 정의 + 동의어"를 제공한다. 예: "균열 = crack = 표면 파손". 이는 **용어 통일**에는 충분하지만, 다음에는 한계가 있다:

| 상황 | 글로서리로 해결 가능? | 온톨로지 필요? |
|---|---|---|
| "균열"이 어디서나 같은 뜻으로 쓰이도록 | ✅ 가능 | 불필요 |
| "균열" → 원인(과부하·피로)을 자동 연결 | ❌ 불가 | **필요** |
| "균열" → 유사 과거 사례 자동 추천 | ❌ 불가 | **필요** |
| "과부하" → 관련 조치(보강·교체) 자동 추론 | ❌ 불가 | **필요** |

**핵심 구분:** 글로서리는 *단어의 의미*를 정의한다. 온톨로지는 *개념 간 관계·인과 구조*를 정의한다.

출처: [Atlan — What Is Ontology? Definition, Components & AI Use Cases in 2026](https://atlan.com/know/ontology-101-explainer/) (접속: 2026-06-18)

### 1-4. AI 에이전트가 도메인을 모르는 문제

LLM(Large Language Model)은 공개 데이터로 학습되어 일반적인 지식을 갖추고 있지만, **회사·공장 고유의 개념 구조**는 모른다. 예:
- "당사 압연 설비 R3 롤러 균열" → LLM은 R3가 무엇인지, 당사 품질 기준이 무엇인지 모른다.
- 같은 단어 "policy"도 고객 정책, 운영 정책, 규정 정책으로 문맥마다 달라지는데, 온톨로지가 없으면 AI가 잘못 해석한다.

온톨로지는 회사·도메인 고유의 **지식 지도(Shared Map)**를 AI에게 제공하는 역할을 한다.

출처: [Enterprise Knowledge — Ontology and Knowledge Graph in the Age of AI and Agents](https://enterprise-knowledge.com/ontology-and-knowledge-graph-in-the-age-of-ai-and-agents/) (접속: 2026-06-18)

---

## 2. 온톨로지가 푸는 것 / 기대 효과

### 2-1. 관계 기반 추론으로 원인 분석 가능

온톨로지에 "균열 —[원인]→ 과부하", "균열 —[원인]→ 피로파괴", "과부하 —[조치]→ 하중 재분배" 같은 관계가 정의되면:
- "균열 발생" 보고가 들어올 때 AI가 **원인 후보**를 자동으로 제시한다.
- 과거 유사 사례에서 어떤 조치가 효과적이었는지 **추천**이 가능해진다.
- 단순 키워드 매칭이 아닌 **개념 확장 검색**(균열 → 파괴역학 → 피로 → 반복 하중)이 가능해진다.

### 2-2. 흩어진 지식의 연결

온톨로지는 서로 다른 시스템에 있는 데이터를 **공통 개념 구조**로 연결하는 다리 역할을 한다:
- MES의 "공정 이상" 이벤트와 품질 시스템의 "불량 유형"을 온톨로지의 "결함 원인" 개념으로 연결
- 설비 정비 이력과 품질 불량 발생 이력을 "설비 상태 → 공정 조건 → 품질 결과"의 인과 체인으로 연결

출처: [Mindbreeze](https://www.mindbreeze.com/blog/demystifying-ontologies-in-knowledge-graphs-building-a-semantic-backbone-for-enterprise-ai) (접속: 2026-06-18)

### 2-3. AI 응답의 신뢰성·일관성 향상

온톨로지 없이 AI를 사용하면:
- 동일한 질문에 AI가 맥락에 따라 다른 답을 낸다(정의 불일치 때문).
- 조직 내부 규칙을 모르는 AI가 "그럴듯하지만 틀린" 답변을 자신 있게 내놓는다(환각).

온톨로지를 갖추면:
- 모든 AI 에이전트가 **동일한 개념 정의·관계**를 공유하여 일관된 답변.
- 정의된 규칙에 어긋나는 추론을 자동으로 걸러낼 수 있다.

벤치마크: 온톨로지 기반 지식 검증을 LLM에 결합했을 때 **응답 정확도 4.2배 향상** (17% → 72.6%).  
출처: [Cyberhillpartners — Ontologies & Knowledge Graphs for Enterprise AI](https://cyberhillpartners.com/enterprise-ai-ontologies-knowledge-graphs/) (접속: 2026-06-18)

### 2-4. AI 프로젝트 재사용성 향상

온톨로지 없이는 새 AI 프로젝트마다 도메인 맥락을 처음부터 구축해야 한다. 온톨로지를 한 번 구축해두면:
- 새 AI 에이전트·RAG 시스템이 **기존 온톨로지를 재사용**하여 구축 시간 단축.
- 조직 내 지식 자산이 누적·공유되어 확장성이 생긴다.

---

## 3. 적용 판단 기준 (When)

> ★ B-3 온톨로지는 모든 데이터·문서에 적용하는 것이 아니다. 아래 기준으로 "구축해야 하는 영역"을 선별한다.

### 3-1. 온톨로지가 필요한 경우 (적용)

| 판단 기준 | 설명 | 제조 예시 |
|---|---|---|
| **다중 시스템 지식 연결이 필요할 때** | 여러 문서·시스템의 지식을 관계로 엮어야 AI가 맥락을 파악할 수 있을 때 | MES 공정 이상 + 품질 불량 + 설비 정비 이력 연결 |
| **원인-결과 관계가 핵심일 때** | "왜 이 현상이 발생했는가"를 AI가 추론해야 할 때 | 균열 발생 원인 분석, 품질 불량 근본원인 진단 |
| **AI Agent가 추천·판단을 해야 할 때** | 단순 검색이 아니라 원인 분석·유사 사례 추천·조치 제안을 AI에게 시킬 때 | 결함 발생 시 유사 과거 사례 + 조치 자동 추천 |
| **도메인 특수 용어·개념이 복잡할 때** | 업계·회사 고유의 개념 체계가 있어서 일반 LLM이 잘못 해석할 때 | 특수 합금 소재, 자체 설비 코드, 사내 공정 명칭 |
| **여러 부서·팀이 같은 개념을 다르게 쓸 때** | 용어 통일(글로서리)만으로 부족하고, 개념 간 관계·계층도 통일해야 할 때 | 품질팀의 "결함 분류"와 엔지니어링팀의 "파손 분류"를 연결 |

출처: [Enterprise Knowledge](https://enterprise-knowledge.com/ontology-and-knowledge-graph-in-the-age-of-ai-and-agents/) (접속: 2026-06-18), [Cyberhillpartners](https://cyberhillpartners.com/enterprise-ai-ontologies-knowledge-graphs/) (접속: 2026-06-18)

### 3-2. 온톨로지가 불필요한 경우 (비적용)

| 상황 | 대신 쓸 수 있는 것 | 이유 |
|---|---|---|
| 용어 정의·동의어 통일만 필요한 경우 | A-3 비즈니스 용어 사전(Glossary) | 관계·추론이 불필요하므로 온톨로지 오버엔지니어링 |
| 단순 문서 분류·태그 검색 | 택소노미(Taxonomy) / 카탈로그 태그 | 계층적 분류만 필요, 복잡한 관계 불필요 |
| 정형 데이터 단순 집계·통계 | SQL 쿼리, BI 도구 | 데이터가 이미 구조화되어 있고 관계 추론이 불필요 |
| 단일 시스템 내 데이터만 다루는 경우 | 시스템 내 메타데이터 관리 | 여러 시스템 연결 문제가 없으므로 온톨로지 효과 낮음 |
| 데이터양이 적고 도메인이 단순한 경우 | 스프레드시트, 간단한 데이터베이스 | 구축 비용 대비 효과 낮음 |

핵심 판단 질문:
> "AI가 단순히 '이 단어가 있는 문서를 찾아라'를 넘어서, '이 현상의 원인이 뭐고 어떻게 조치하나'를 **추론**해야 하는가?"  
> → **YES**: 온톨로지 필요  
> → **NO**: 글로서리·택소노미로 충분

출처: [PuppyGraph — Knowledge Graph vs Ontology](https://www.puppygraph.com/blog/knowledge-graph-vs-ontology) (접속: 2026-06-18), [Hedden Information Management — Knowledge Graphs and Taxonomies](https://www.hedden-information.com/knowledge-graphs-and-taxonomies/) (접속: 2026-06-18)

### 3-3. 전체 vs 선택 적용

온톨로지는 **"전사 모든 데이터"가 아니라 "지식 연결이 가치 있는 영역"**에 선택 적용한다:

- 모든 문서·데이터에 온톨로지를 만들면 구축·유지 비용이 과도해진다.
- 먼저 AI가 원인 분석·추천·판단을 해야 하는 **핵심 업무 영역**을 식별하고, 그 영역의 지식 구조를 만든다.
- 작게 시작해서 효과를 확인 후 확장하는 방식을 권장한다.

---

## 4. 우선 만들 영역 고르기

우선 적용 영역 선정 기준 (모두 높을수록 우선):

| 기준 | 설명 |
|---|---|
| **지식의 복잡도** | 개념 간 관계·인과 구조가 복잡할수록 온톨로지 효과 큼 |
| **AI 활용 가치** | AI 에이전트가 원인 분석·추천·판단에 쓰일 영역 |
| **다중 시스템 연결 필요성** | 여러 시스템·부서 데이터를 연결해야 의미 있는 영역 |
| **재사용 빈도** | 반복적으로 쓰이는 지식일수록 온톨로지 ROI 높음 |
| **오류 비용** | AI 판단 오류 시 비용·리스크가 큰 영역 우선 |

**제조업(두산) 맥락 우선 후보 영역:**

1. **품질 결함 근본원인 분석(RCA)** — 결함 유형 → 원인(공정·설비·소재) → 조치의 인과 구조
2. **설비 정비·고장 진단** — 고장 증상 → 원인 → 정비 조치의 지식 체계
3. **공정 이상 분석** — 공정 파라미터 이상 → 품질 영향 → 조정 방안
4. **안전 사고 조사** — 사고 유형 → 원인 체인 → 예방 조치

**시작하지 말아야 할 영역:**  
- 단순 부품 카탈로그 (카탈로그+택소노미로 충분)
- 표준 작업 절차서 목록 관리 (문서 카탈로그로 충분)
- 단순 이름·코드 테이블 (마스터 데이터 관리로 충분)

---

## 5. 제조·산업 사례

### 5-1. 전력 변압기 RCA — 지식그래프 활용 사례

**적용 영역:** 전력 변압기(Power Transformer) 고장 원인 분석  
**문제:** 변압기 고장은 원인이 다양하고 복잡하게 얽혀 있어 전통적 방법으로 근본원인 진단이 어렵다.  
**접근:** 온톨로지로 변압기 구성 요소(절연유·코일·코어 등)와 고장 유형·원인의 관계 구조를 정의하고, 지식그래프(Knowledge Graph)로 실제 고장 사례 데이터를 연결.  
**효과:** AI가 새 고장 증상을 입력받으면 지식그래프를 탐색하여 원인 후보와 유사 사례를 추론.

출처: [Root Cause Analysis in the Industrial Domain using Knowledge Graphs (ResearchGate)](https://www.researchgate.net/publication/359090856_Root_Cause_Analysis_in_the_Industrial_Domain_using_Knowledge_Graphs_A_Case_Study_on_Power_Transformers) (접속: 2026-06-18)

### 5-2. Root-KGD — 화학공정 근본원인 진단 프레임워크

**적용 영역:** 화학·제조 공정(Tennessee Eastman Process, Multiphase Flow Facility)  
**문제:** 기존 AI 방법은 도메인 지식(공정 설계 구조)과 운전 데이터를 통합하지 못해 근본원인 진단이 부정확했다.  
**접근 (Root-KGD):**
1. 도메인 전문가 지식으로 온톨로지 구성 — 공정 장치(devices)와 흐름(streams)의 관계·인과 구조 정의
2. 지식그래프로 개념 구조를 실제 공정 데이터와 연결
3. 그래프 추론으로 어떤 장치·파라미터가 원인인지 자동 진단

**효과:** 기존 방법 대비 더 높은 정확도 + **해석 가능성(Explainability)** — "왜 이 결론인가"를 추적 가능.

출처: [Root-KGD: A Novel Framework for Root Cause Diagnosis Based on Knowledge Graph and Industrial Data (arXiv)](https://arxiv.org/abs/2406.13664) (접속: 2026-06-18)

### 5-3. 제조 품질 관리 — 지식그래프 기반 결함 진단

**논문:** An Intelligent Quality Control Method for Manufacturing Processes Based on a Human-Cyber-Physical Knowledge Graph  
**적용:** 제품 가공 결함 진단에 지식그래프 활용  
**구조:** 관련 지식 온톨로지를 그래프 엔티티와 관계로 표현 → 과거 가공 결함 사례 지식베이스 구축 → 새 결함 발생 시 원인 추론·추천  
**효과:** 지식베이스 기반으로 잠재적 결함 원인 식별 및 추론 가능

출처: [Engineering journal — Quality Control Knowledge Graph](https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2024.03.022) (접속: 2026-06-18)

### 5-4. 두산 맥락 Before / After 대비 예시

**상황:** 압연 공정에서 "롤러 균열(crack)" 발생

**Before (온톨로지 없음):**
- 작업자가 "균열"로 정비 시스템·보고서 검색 → 균열이 언급된 문서 100건 목록
- 담당자가 문서를 일일이 읽고 유사 사례 수작업 파악
- 원인(과부하? 피로? 소재 결함?) 추론은 전문가 경험에 의존
- 공정 이상 이력(MES), 소재 검사 이력(QMS), 설비 정비 기록(CMMS)이 연결되지 않음

**After (온톨로지 있음):**
- "롤러 균열"이 입력되면 온톨로지가 정의한 인과 관계를 따라 원인 후보 자동 제시
  - 원인 후보: 반복 하중(피로) / 과부하 / 소재 취성 불량
- 지식그래프가 MES 공정 이상 이력 + 소재 검사 결과 + 유사 과거 사례를 자동 연결
- AI가 유사도 기반으로 가장 유력한 원인과 조치 방안 추천
- 조치 후 재발 방지를 위한 모니터링 포인트도 제안

---

## 6. 용어 정리: 온톨로지 vs 글로서리 vs 택소노미

| 구분 | 글로서리(Glossary) | 택소노미(Taxonomy) | 온톨로지(Ontology) |
|---|---|---|---|
| **역할** | 용어 정의·동의어 통일 | 계층적 분류 체계 | 개념·관계·규칙 전체 구조 |
| **관계 표현** | 없음 (단어↔정의만) | "상위-하위(is-a)"만 | "원인-결과", "소유", "의존" 등 다양 |
| **추론 능력** | 없음 | 최소한 | 자동 추론 가능 |
| **예시** | "균열 = crack = 표면 파손" | "균열 > 피로균열 > 횡방향 피로균열" | "균열 —[원인]→ 과부하 —[조치]→ 하중 재분배" |
| **적합한 상황** | 용어 통일이 목적 | 문서 분류·검색 개선 | AI 원인분석·추천·추론 |
| **AI Ready Data 주제** | A-3 비즈니스 용어 사전 | A-1 데이터 카탈로그 태그 | **B-3 온톨로지** |

**관계:** 글로서리 ⊂ 택소노미 ⊂ 온톨로지 (온톨로지가 가장 포괄적이고 표현력이 강함)  
**오해 주의:** 온톨로지가 항상 더 좋은 것이 아니다 — 목적에 맞는 도구를 고르는 것이 핵심.

출처: [Atlan — Ontology 101](https://atlan.com/know/ontology-101-explainer/) (접속: 2026-06-18), [PuppyGraph — Knowledge Graph vs Ontology](https://www.puppygraph.com/blog/knowledge-graph-vs-ontology) (접속: 2026-06-18)

---

## 7. 출처 목록

| # | 제목 | URL | 접속일 |
|---|---|---|---|
| 1 | Mindbreeze — Demystifying Ontologies in Knowledge Graphs | https://www.mindbreeze.com/blog/demystifying-ontologies-in-knowledge-graphs-building-a-semantic-backbone-for-enterprise-ai | 2026-06-18 |
| 2 | Enterprise Knowledge — Ontology and Knowledge Graph in the Age of AI and Agents | https://enterprise-knowledge.com/ontology-and-knowledge-graph-in-the-age-of-ai-and-agents/ | 2026-06-18 |
| 3 | Atlan — What Is Ontology? Definition, Components & AI Use Cases in 2026 | https://atlan.com/know/ontology-101-explainer/ | 2026-06-18 |
| 4 | Cyberhillpartners — Ontologies & Knowledge Graphs for Enterprise AI | https://cyberhillpartners.com/enterprise-ai-ontologies-knowledge-graphs/ | 2026-06-18 |
| 5 | PuppyGraph — Knowledge Graph vs Ontology | https://www.puppygraph.com/blog/knowledge-graph-vs-ontology | 2026-06-18 |
| 6 | Hedden Information Management — Knowledge Graphs and Taxonomies | https://www.hedden-information.com/knowledge-graphs-and-taxonomies/ | 2026-06-18 |
| 7 | Root Cause Analysis in the Industrial Domain using Knowledge Graphs (ResearchGate) | https://www.researchgate.net/publication/359090856_Root_Cause_Analysis_in_the_Industrial_Domain_using_Knowledge_Graphs_A_Case_Study_on_Power_Transformers | 2026-06-18 |
| 8 | Root-KGD: A Novel Framework for Root Cause Diagnosis Based on Knowledge Graph and Industrial Data (arXiv) | https://arxiv.org/abs/2406.13664 | 2026-06-18 |
| 9 | Knowledge graph-driven equipment fault diagnosis method for intelligent manufacturing (Springer) | https://link.springer.com/article/10.1007/s00170-024-12998-x | 2026-06-18 |
| 10 | An Intelligent Quality Control Method for Manufacturing Processes Based on a Human-Cyber-Physical Knowledge Graph | https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2024.03.022 | 2026-06-18 |
| 11 | Atlan — Ontology vs Knowledge Graph: Key Differences, Explained | https://atlan.com/know/ai-agent/knowledge-graph/ontology-vs-knowledge-graph/ | 2026-06-18 |
