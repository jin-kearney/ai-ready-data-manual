# B-3 온톨로지 — What 클러스터 리서치 원자료

> **작성 목적**: B-3 온톨로지 가이드의 "무엇을 갖추나(What)" 섹션 집필을 위한 원자료.
> 가이드 본문이 아니라 리서치 메모다. 메인에 넣을 내용 vs 백업/별첨용을 구분 표기.
> **조사일**: 2026-06-18

---

## 목차
1. [온톨로지 정의 — 쉬운 한 줄 설명](#1-온톨로지-정의)
2. [분류체계·시소러스·Glossary·지식그래프와의 차이](#2-인접-개념과-차이)
3. [정본 구성요소(Canonical Model)](#3-정본-구성요소)
4. [관계 모델링 — Triple 구조](#4-관계-모델링)
5. [공통/계열사 확장 구조](#5-공통계열사-확장-구조)
6. [표준 및 기술 (얕게)](#6-표준-및-기술)
7. [개념-데이터-문서 매핑](#7-개념-데이터-문서-매핑)
8. [제조(두산) 도메인 예시](#8-제조두산-도메인-예시)
9. [정본 모델 후보 제안](#9-정본-모델-후보-제안)
10. [출처 목록](#10-출처-목록)

---

## 1. 온톨로지 정의

### 1.1 핵심 정의 (메인용)

**쉬운 한 줄 정의**: 온톨로지(Ontology)는 업무 개념들 사이의 **관계·계층·인과 구조를 명시적으로 정의한 지식 지도**다.

- "결함(Defect)이 무엇인지"는 Glossary가 말한다.
- "결함이 어떤 공정에서 발생하고, 어떤 원인으로 생기며, 어느 설비와 연관되는지"를 연결하는 것이 온톨로지다.

**공식 정의**: "특정 도메인에 대한 공유된 개념화(conceptualization)를 명시적으로 형식화(formal specification)한 것" — Gruber(1993) [출처 1]

**데이터 준비 관점 정의**: AI가 데이터의 맥락과 연결성을 이해할 수 있도록, 업무 개념과 그 관계를 구조화된 데이터 자산으로 만드는 작업. 온톨로지는 AI가 "관계 기반 추론"을 하기 위해 쓰는 **지식 데이터**다.

출처: Gruber(1993), Wikipedia Ontology components [출처 2]

---

## 2. 인접 개념과 차이

### 2.1 Glossary vs Taxonomy vs Thesaurus vs Ontology vs Knowledge Graph (메인용)

아래 표는 현업 눈높이로 정리한 한 줄 구분이다.

| 개념 | 한 줄 설명 | 포함 관계 |
|---|---|---|
| **Glossary (용어사전)** | 단어의 뜻을 풀어쓴 목록 | 단어 1개의 정의 |
| **Taxonomy (분류체계)** | 개념을 위계(상위-하위)로 나눈 트리 구조 | 계층적 is-a 관계 |
| **Thesaurus (시소러스)** | Taxonomy + 동의어·유사어 등 비계층 관계 추가 | 계층 + 유사 관계 |
| **Ontology (온톨로지)** | Thesaurus + 관계 유형 명시(has-part, causes, measured-by…) + 논리 규칙 | 위 세 개 모두 포함 가능 |
| **Knowledge Graph (지식그래프)** | 온톨로지 구조에 실제 인스턴스(데이터) 채워 넣은 네트워크 | 온톨로지 + 실제 데이터 |

**현업 비유**:
- Glossary = 사전 (결함 = 제품이 기준을 벗어난 상태)
- Taxonomy = 결함 분류표 (치수불량 > 두께불량 / 외관불량 > 스크래치)
- Thesaurus = 분류표 + "스크래치 = 긁힘 = Scratch" 동의어 연결
- Ontology = "스크래치는 [공정 B 연삭 단계에서 발생하고] [치구 마모가 원인이며] [연삭 조건 조정으로 조치한다]"
- Knowledge Graph = 위 구조에 "2025년 3월 17일 라인 3에서 발생한 스크래치 건 #KR-2345" 실제 데이터가 연결된 것

출처: [출처 3, 4, 5, 6]

### 2.2 MECE 경계 (메인용)

B-3 온톨로지의 범위:
- **포함**: 개념 간 관계·계층·인과 구조를 정의하는 지식 자산
- **제외(A-3 Glossary 소관)**: 단일 용어의 정의·동의어·약어
- **제외(A-2 메타데이터 소관)**: 데이터 필드(컬럼) 속성 설명
- **제외(A-1 카탈로그 소관)**: 데이터 자산의 위치·접근 경로

---

## 3. 정본 구성요소

### 3.1 핵심 7요소 (메인용 — 정본 모델)

아래가 **정본 구성요소 7가지**다. 가이드 본문에서 이 7가지로 일관되게 설명한다.

#### ① 엔티티/개념(Entity / Class)
- **뜻**: 온톨로지에서 다루는 사물·현상의 범주(종류). 같은 특성을 공유하는 집합.
- **예시**: `결함(Defect)`, `공정(Process)`, `설비(Equipment)`, `원인(Cause)`, `조치(Action)`, `검사항목(InspectionItem)`, `고객불만(CustomerComplaint)`
- 출처: Wikipedia Ontology components [출처 2], Atlan [출처 7]

#### ② 인스턴스(Instance / Individual)
- **뜻**: 특정 엔티티(클래스)에 속하는 구체적인 개별 사례.
- **예시**: `스크래치`(결함 클래스의 인스턴스), `진동센서 #VB-303`(설비 클래스의 인스턴스), `표면조도 측정`(검사항목 클래스의 인스턴스)
- 출처: Grokipedia [출처 8]

#### ③ 속성(Attribute / Property)
- **뜻**: 엔티티나 인스턴스가 가지는 특성값. 데이터 속성(값)과 객체 속성(다른 개념으로 연결)으로 구분.
  - 데이터 속성(Data Property): 결함의 심각도 = 3 (숫자·문자 값)
  - 객체 속성(Object Property): 결함이 발생한 공정 = "성형 공정" (다른 개념을 연결)
- **예시**: `결함.심각도`, `결함.발생빈도`, `설비.가동률`, `검사항목.측정단위`
- 출처: Wikipedia Ontology components [출처 2], Atlan [출처 7]

#### ④ 관계(Relationship)
- **뜻**: 두 개념 사이의 연결을 명시적으로 이름 붙인 것. 온톨로지의 핵심.
- **관계 유형 예시**:
  - `is-a` (종류이다): 스크래치 is-a 외관결함
  - `has-part` (부품이다): 엔진 has-part 크랭크샤프트
  - `causes` (원인이다): 치구마모 causes 스크래치
  - `detected-by` (검출된다): 스크래치 detected-by 비전검사
  - `occurs-in` (발생한다): 스크래치 occurs-in 연삭공정
  - `remediated-by` (조치된다): 스크래치 remediated-by 연삭조건조정
- 출처: Atlan [출처 7], PuppyGraph [출처 9]

#### ⑤ 계층(Hierarchy / Taxonomy)
- **뜻**: 상위-하위 개념 구조. "A는 B의 한 종류다(is-a)" 관계로 형성.
- **예시**:
  ```
  결함(Defect)
  ├── 외관결함(AppearanceDefect)
  │   ├── 스크래치(Scratch)
  │   └── 변색(Discoloration)
  └── 치수결함(DimensionalDefect)
      ├── 두께불량(ThicknessDefect)
      └── 진원도불량(RoundnessDefect)
  ```
- 출처: Semantic Web Company [출처 5]

#### ⑥ 규칙/공리(Axiom / Rule)
- **뜻**: 온톨로지가 지켜야 할 논리적 제약 조건. AI가 이 규칙으로 새로운 사실을 **추론(inference)** 할 수 있다.
- **예시**: "만약 결함 A가 원인 B에 의해 발생하고, 원인 B가 조치 C로 해결된다면 → 결함 A는 조치 C로 해결 가능하다" (추론 규칙)
- **현업 비유**: PFMEA의 "발생 원인 → 고장 모드" 연결 로직을 AI가 자동으로 따라갈 수 있게 형식화한 것.
- 출처: Grokipedia [출처 8], 온톨로지-기반 인과 추론 논문 [출처 10]

#### ⑦ 인과 구조(Causal Structure)
- **뜻**: 원인→결과 방향이 있는 관계 체인. 단순 연결이 아니라 방향성과 조건이 있음.
- **예시**: `진동 증가 → [원인이 된다] → 베어링 마모 → [결과로] → 치수 불량 → [영향] → 고객 불만`
- 출처: 온톨로지 기반 인과 추론 [출처 10], 제조 지식그래프 FMEA 논문 [출처 11]

### 3.2 구성요소 간 관계 요약 (메인용)

```
[클래스/엔티티]  ← 인스턴스가 속함
     ↑↓ 계층(is-a)
[클래스/엔티티] ─[관계(동사)]─ [클래스/엔티티]
     │                              │
  [속성값]                       [속성값]
     └─────── [공리/규칙] ─────────┘
                  ↓
             [인과 구조] (방향+조건)
```

---

## 4. 관계 모델링 — Triple 구조

### 4.1 Triple(트리플) 개념 (메인용)

온톨로지의 모든 관계는 **"주어(Subject) — 관계(Predicate) — 목적어(Object)"** 3개로 표현된다. 이것을 **트리플(Triple)**이라 한다.

```
(주어)         [관계]         (목적어)
베어링 마모  ─[원인이 된다]─▶  치수 불량
스크래치    ─[검출된다]────▶  비전 검사
진동 센서   ─[측정한다]────▶  베어링 진동값
공정 B      ─[생산한다]────▶  제품 A
```

**왜 Triple인가**: 모든 지식은 "누가/무엇이 — 어떤 관계로 — 무엇과 연결되는가" 3가지로 표현 가능. AI가 이 구조를 따라 경로를 탐색(Graph Traversal)하면서 추론한다.

출처: Semantic Triples — FatRank [출처 12], RDF Knowledge Graphs PuppyGraph [출처 13]

### 4.2 제조 현업 관계 유형 (메인용)

| 관계 이름 | 영문 | 설명 | 예시 Triple |
|---|---|---|---|
| 원인이 된다 | causes | A가 B의 원인 | (치구마모) causes (스크래치) |
| 검출된다 | detected-by | A가 B에 의해 검출 | (스크래치) detected-by (비전검사) |
| 발생한다 | occurs-in | A가 B 공정에서 발생 | (스크래치) occurs-in (연삭공정) |
| 조치한다 | remediated-by | A가 B로 조치됨 | (치구마모) remediated-by (치구교체) |
| 영향을 준다 | affects | A가 B에 영향 | (진동이상) affects (베어링수명) |
| 선행한다 | precedes | A가 B 전에 발생 | (연삭) precedes (도금) |
| 측정한다 | measured-by | A가 B 센서로 측정됨 | (베어링진동) measured-by (진동센서#VB303) |
| 포함한다 | has-part | A가 B를 부품으로 포함 | (터빈) has-part (로터블레이드) |

출처: 제조 FMEA 온톨로지 논문 [출처 11], FMEA 온톨로지 ScienceDirect [출처 14]

---

## 5. 공통/계열사 확장 구조

### 5.1 상위 온톨로지(Upper Ontology)와 도메인 온톨로지(Domain Ontology) (메인용)

**상위 온톨로지(Upper / Foundational Ontology)**
- 모든 도메인에 공통으로 쓰이는 가장 일반적인 개념들을 정의.
- 예: `사물(Object)`, `이벤트(Event)`, `상태(State)`, `관계(Relation)`, `시간(Time)`, `장소(Location)`
- 기업 관점에서는 "전사 공통 온톨로지" = 지주사 수준에서 모든 계열사가 공유하는 상위 개념 구조.

**도메인/로컬 온톨로지(Domain / Local Ontology)**
- 특정 산업·업무·계열사에 특화된 개념과 관계를 정의.
- 상위 온톨로지의 개념을 **확장(Extension)**하여 현장 용어와 관계를 추가.
- 예: 두산에너빌리티는 상위 `설비(Equipment)` → 도메인 `터빈(Turbine)`, `로터(Rotor)`, `블레이드(Blade)` 확장.

**공통/계열사 확장 구조 그림**:

```
전사 공통 온톨로지 (지주 관리)
├── 제품(Product)
├── 공정(Process)
├── 결함(Defect)
├── 설비(Equipment)
├── 원인(Cause)
└── 조치(Action)
      │
      ├── [두산에너빌리티 확장]
      │   └── 터빈, 로터, 블레이드, 가스발전결함, 가스발전공정...
      ├── [두산밥캣 확장]
      │   └── 굴착기, 유압계통, 차체결함, 조립라인공정...
      └── [테스나 확장]
          └── 반도체웨이퍼, 패키지결함, 테스트항목, 반도체공정...
```

**연결 방식**: 계열사 온톨로지의 개념이 전사 공통 온톨로지의 개념을 `rdfs:subClassOf` 관계로 상속. 공통 개념 위에 계열사 특화 개념을 덧쌓는 방식.

출처: Upper ontology Wikipedia [출처 15], 온톨로지 구축 방법론 Brunch [출처 16]

### 5.2 전사 표준 관계 모델 (메인용)

지주가 정의하는 것: 공통 엔티티 목록 + 공통 관계 유형 (위 4.2 표의 관계들)
계열사가 추가하는 것: 현장 특화 엔티티 + 현장 특화 관계

예: 공통에서 `결함 occurs-in 공정` 관계를 정의하면, 계열사는 `스크래치(결함의 하위) occurs-in 연삭공정(공정의 하위)` 관계를 자동으로 상속.

---

## 6. 표준 및 기술

> ★ **[메인용 — 한 줄 풀이만]** vs **[백업/별첨 — 상세 스펙]** 구분

### 6.1 메인에 쓸 한 줄 풀이 (현업이 겁먹지 않게)

| 약어 | 풀이 | 한 줄 설명 |
|---|---|---|
| **RDF** | Resource Description Framework (자원 기술 프레임워크) | "주어-관계-목적어" 3개 짝으로 모든 지식을 표현하는 국제 표준 형식. W3C 권고. |
| **OWL** | Web Ontology Language (웹 온톨로지 언어) | 온톨로지의 규칙·제약을 컴퓨터가 읽고 추론할 수 있도록 쓰는 언어. RDF 위에 얹는다. |
| **SKOS** | Simple Knowledge Organization System (간단한 지식 조직 시스템) | 분류체계·시소러스를 RDF로 표현하는 간단한 표준. 복잡한 추론 없이 계층·동의어 관리할 때 적합. |
| **Triple Store** | (한글 병기 불필요) | RDF 트리플을 저장하고 SPARQL 쿼리로 검색하는 데이터베이스. |
| **Property Graph** | 속성 그래프 | 노드(Node)와 엣지(Edge)에 속성값을 직접 붙일 수 있는 그래프 모델. Neo4j 같은 도구가 대표적. RDF보다 단순하고 빠르지만 추론 기능은 약하다. |
| **SPARQL** | SPARQL Protocol and RDF Query Language | RDF/Triple Store를 검색하는 쿼리 언어. SQL의 그래프 버전. |
| **Knowledge Graph** | 지식그래프 | 온톨로지 구조(설계도)에 실제 데이터(인스턴스)를 채워 넣은 것. |

출처: OWL/RDF/SKOS Medium [출처 17], RDF vs Property Graph TigerGraph [출처 18], Neo4j [출처 19]

### 6.2 백업/별첨 — 표준 상세 스펙 (가이드 본문에 넣지 말 것)

**RDF 스펙**:
- W3C 표준. URI/IRI로 모든 자원 식별. 트리플 집합으로 Graph 형성.
- Turtle, JSON-LD, N-Triples 등 직렬화 포맷 다양.
- URL: https://www.w3.org/RDF/

**OWL 스펙**:
- OWL 2(2009 W3C Recommendation). DL(Description Logic) 기반.
- Profiles: OWL 2 EL / QL / RL (계산 복잡도 별로 제한)
- URL: https://www.w3.org/TR/owl2-overview/

**SKOS 스펙**:
- W3C Recommendation 2009. skos:Concept, skos:broader, skos:narrower, skos:related, skos:altLabel 등.
- Thesaurus, Classification Scheme 표현에 최적.
- URL: https://www.w3.org/TR/skos-reference/

**ISO 15926**:
- 플랜트·오일·가스 산업 대상 상위 온톨로지 표준.
- 설비 생애주기 데이터 통합에 사용.
- 제조 FMEA 지식 표현에 응용 사례 있음 [출처 14]
- URL: https://www.iso.org/standard/50798.html

**Property Graph (Neo4j 등)**:
- 노드에 레이블(Label), 엣지에 관계 유형(Relationship Type), 양쪽에 속성(Properties) 부여.
- RDF보다 직관적. 복잡한 추론보다는 탐색·패턴 매칭에 강함.
- URL: https://neo4j.com/developer/graph-database/

---

## 7. 개념-데이터-문서 매핑

### 7.1 온톨로지 개념이 연결되는 계층 (메인용)

온톨로지는 **개념 구조(설계도)**이고, 실제 데이터·문서는 그 설계도에 연결되는 **콘텐츠**다.

```
[온톨로지 개념]           ↔  [연결 대상]
─────────────────────────────────────────────────
결함(Defect) 엔티티       ↔  A-3 Glossary의 "결함" 표준 정의
결함.유형(Attribute)      ↔  A-2 메타데이터의 DEF_CD 필드 설명
결함 인스턴스             ↔  A-1 카탈로그에 등록된 품질 데이터셋
(결함)-[발생]->(공정)     ↔  SOP(표준작업지침서)의 해당 공정 섹션
(결함)-[원인]->(설비마모) ↔  PFMEA의 Failure Mode→Cause 매핑
(결함)-[조치]->(교체)     ↔  C/S Report의 조치 이력 레코드
```

### 7.2 구체적 매핑 예시 — 제조 현장 (메인용)

| 온톨로지 요소 | 연결 데이터/문서 | 연결 방법 |
|---|---|---|
| `결함(Defect)` 클래스 | A-3 Glossary의 결함 용어 항목 | 개념 ID → Glossary 용어 ID 매핑 |
| `스크래치` 인스턴스 | QMS의 DEF_CODE = 'SCR001' | 인스턴스 URI ↔ 코드값 매핑 |
| `공정(Process)` 클래스 | MES의 PROC_CD 컬럼 | A-2 메타데이터 필드 설명과 연결 |
| `결함 causes 원인` 관계 | PFMEA 시트의 Cause 컬럼 | PFMEA 행 → Triple (결함, causes, 원인) 변환 |
| `결함 occurs-in 공정` 관계 | MES 불량 발생 로그 (PROC_ID + DEF_ID) | 로그 레코드 → Triple 자동 추출 |
| `설비 measured-by 센서` 관계 | IoT 플랫폼 센서 메타데이터 | 설비 ID + 센서 ID → Triple 매핑 |
| `결함 detected-by 검사` 관계 | QMS 검사 기록 (INSP_TYPE + DEF_ID) | 검사 기록 → Triple 변환 |

출처: Atlan [출처 7], data.world [출처 20], Ontoforce [출처 21]

### 7.3 온톨로지-카탈로그 연동 (메인용)

데이터 카탈로그(A-1)에 등록된 데이터 자산에 온톨로지 개념을 태깅하면:
- "결함 관련 데이터"를 검색할 때 → `결함(Defect)` 개념에 연결된 모든 데이터셋 탐색 가능
- 의미 기반 검색(Semantic Search): 단순 키워드가 아니라 개념 확장(하위 개념도 함께 검색)

출처: data.world Knowledge Graph Data Catalog [출처 20]

---

## 8. 제조(두산) 도메인 예시

### 8.1 제조 온톨로지 핵심 엔티티 목록 (메인용)

두산 계열사 제조 현장에서 우선 정의할 엔티티:

| 그룹 | 엔티티(한글) | 엔티티(English) | 예시 인스턴스 |
|---|---|---|---|
| 제품 | 제품 | Product | 터빈, 굴착기, 웨이퍼 |
| 공정 | 공정 | Process | 연삭, 도금, 조립, 테스트 |
| 결함 | 결함 | Defect | 스크래치, 치수불량, 균열 |
| 설비 | 설비 | Equipment | 연삭기, 로봇팔, 측정기 |
| 센서 | 센서 | Sensor | 진동센서, 온도센서, 비전카메라 |
| 원인 | 원인 | Cause | 치구마모, 과부하, 소재이상 |
| 조치 | 조치 | Action | 치구교체, 조건조정, 소재교환 |
| 검사 | 검사항목 | InspectionItem | 표면조도, 치수, 경도 |
| 고객 | 고객불만 | CustomerComplaint | 조기파손, 소음, 치수이탈 |

### 8.2 제조 Triple 예시 (메인용)

**결함-원인-조치 인과 체인**:
```
(균열)     ─[원인이 된다]─▶  (과부하 조작)
(균열)     ─[검출된다]────▶  (초음파 검사)
(균열)     ─[발생한다]────▶  (단조 공정)
(과부하)   ─[조치한다]────▶  (가공 조건 재설정)
```

**설비-센서-이상 탐지 체인**:
```
(진동센서#VB303)  ─[측정한다]─▶  (베어링 진동값)
(진동센서#VB303)  ─[부착된다]─▶  (연삭기 #G-07)
(진동 이상)       ─[시사한다]─▶  (베어링 마모)
(베어링 마모)     ─[원인이 된다]─▶  (치수 불량)
(치수 불량)       ─[영향을 준다]─▶  (고객 조기파손 불만)
```

**공정-제품-결함 관계**:
```
(도금 공정)  ─[생산한다]─▶  (도금 레이어)
(도금 공정)  ─[발생시킨다]─▶  (변색 결함)
(변색 결함)  ─[is-a]───▶  (외관 결함)
(외관 결함)  ─[is-a]───▶  (결함)
```

### 8.3 PFMEA 연결 예시 (메인용)

PFMEA 시트 한 행:

| 공정 기능 | 고장 모드 | 고장 영향 | 고장 원인 | 현재 관리 방법 |
|---|---|---|---|---|
| 베어링 가공 | 치수 불량 | 조립 불량 | 치구 마모 | 치구 정기 교체 |

→ 온톨로지 Triple 변환:
```
(치수불량) ─[occurs-in]───▶  (베어링가공공정)
(치수불량) ─[causes]───────▶  (조립불량)
(치구마모) ─[causes]───────▶  (치수불량)
(치구정기교체) ─[prevents]─▶  (치구마모)
(치수불량) ─[managed-by]──▶  (치구정기교체)
```

이 Triple들이 누적되면 AI가 "치수 불량이 발생했을 때 → 치구 마모가 원인일 확률이 높고 → 치구 정기 교체로 예방 가능"을 추론할 수 있다.

출처: 제조 FMEA 온톨로지 논문 [출처 11], 설비 고장 Knowledge Graph Springer [출처 22]

### 8.4 산업 온톨로지 사례 (메인용 — 요약만)

**FMEA + LLM + Knowledge Graph (2024)**:
- 제조 라인별 FMEA 워크시트에서 엔티티(Action, State, Component, Parameter)를 추출해 통합 지식그래프 구성.
- 관계: `acts_on`, `affects`, `has_Cause`, `happens_At`, `precedes`
- 목적: 서로 다른 라인의 고장 원인을 동일한 그래프 구조로 비교·추론.
- 출처: arxiv 2510.15428 [출처 11]

**제조 지식그래프 기반 품질 관리 (2024)**:
- Human-Cyber-Physical 지식그래프로 제조 공정 품질 관리.
- 출처: Engineering journal [출처 23]

**ISO 15926 기반 제조 온톨로지**:
- 플랜트·설비 생애주기 데이터 통합에 사용되는 상위 온톨로지 국제 표준.
- 설비 유지보수 이력, FMEA 지식 표현에 응용.
- 출처: [출처 14]

---

## 9. 정본 모델 후보 제안

### 9.1 가이드 본문에 쓸 정본 모델 (제안)

**구성요소: 6개** (7번째 인과 구조는 관계의 특수 유형으로 통합)

| 번호 | 요소명(한국어) | 요소명(English) | 한 줄 정의 |
|---|---|---|---|
| 1 | 개념/클래스 | Entity / Class | 온톨로지에서 다루는 사물·현상의 범주 |
| 2 | 인스턴스 | Instance | 특정 개념에 속하는 구체적 사례 |
| 3 | 속성 | Attribute / Property | 개념이나 인스턴스가 가지는 특성값 |
| 4 | 관계 | Relationship | 두 개념 사이의 연결을 명시적으로 이름 붙인 것 |
| 5 | 계층 | Hierarchy | "A는 B의 한 종류(is-a)" 상위-하위 구조 |
| 6 | 규칙/공리 | Axiom / Rule | AI가 새로운 사실을 추론하기 위한 논리 제약 |

> 인과 구조는 "방향이 있는 관계"의 특수 유형으로 관계(4번) 내에서 설명하고, 별도 요소로 분리하지 않는 것을 권장. (7개보다 6개가 현업 눈높이에 맞음)

### 9.2 제조 정본 엔티티 목록 (제안)

B-3 가이드에서 예시로 쓸 핵심 엔티티 7개:
`제품(Product)`, `공정(Process)`, `결함(Defect)`, `설비(Equipment)`, `원인(Cause)`, `조치(Action)`, `검사항목(InspectionItem)`

핵심 관계 유형 7개:
`원인이 된다(causes)`, `검출된다(detected-by)`, `발생한다(occurs-in)`, `조치한다(remediated-by)`, `포함한다(has-part)`, `측정한다(measured-by)`, `영향을 준다(affects)`

### 9.3 섹션 구성 권고 (What 섹션)

```
## 무엇을 갖추나 — 온톨로지 구성요소
  3.1 핵심 6요소 (개념/클래스·인스턴스·속성·관계·계층·공리)
  3.2 관계 모델링 — Triple(주어-관계-목적어) 구조
  3.3 제조 엔티티·관계 목록 (두산 예시)
  3.4 인접 개념과의 차이 (Glossary·Taxonomy·Knowledge Graph)
```

---

## 10. 출처 목록

| # | 제목 | URL | 접속일 |
|---|---|---|---|
| 1 | Gruber 1993, Ontology Definition | (학술 논문, 직접 링크 없음) | — |
| 2 | Ontology components — Wikipedia | https://en.wikipedia.org/wiki/Ontology_components | 2026-06-18 |
| 3 | Intro to Taxonomy, Thesaurus, Ontology, Knowledge Graph — Medium | https://medium.com/@joehoeller/intro-to-taxonomy-to-thesaurus-to-ontology-to-knowledge-graph-0b3546d8b38c | 2026-06-18 |
| 4 | Ontologies vs Taxonomies vs Thesauri — T/DG Blog | https://blog.thedigitalgroup.com/ontologies-vs-taxonomies-vs-thesauri-and-its-place-on-the-semantic-web | 2026-06-18 |
| 5 | From Taxonomies over Ontologies to Knowledge Graphs — Semantic Web Company | https://semantic-web.com/from-taxonomies-over-ontologies-to-knowledge-graphs/ | 2026-06-18 |
| 6 | Knowledge Graphs and Taxonomies — Hedden Information Management | https://www.hedden-information.com/knowledge-graphs-and-taxonomies/ | 2026-06-18 |
| 7 | What Is Ontology? Definition, Components & AI Use Cases — Atlan | https://atlan.com/know/ontology-101-explainer/ | 2026-06-18 |
| 8 | Ontology components — Grokipedia | https://grokipedia.com/page/Ontology_components | 2026-06-18 |
| 9 | Knowledge Graph vs Ontology: Know Differences — PuppyGraph | https://www.puppygraph.com/blog/knowledge-graph-vs-ontology | 2026-06-18 |
| 10 | Ontology-based inference for causal explanation — arXiv | https://arxiv.org/pdf/1004.4801 | 2026-06-18 |
| 11 | Fault Cause Identification across Manufacturing Lines through Ontology-Guided FMEA Graph Learning — arXiv | https://arxiv.org/html/2510.15428 | 2026-06-18 |
| 12 | Semantic Triples — FatRank | https://www.fatrank.com/semantic-triples/ | 2026-06-18 |
| 13 | RDF Knowledge Graphs: Structure & Benefits — PuppyGraph | https://www.puppygraph.com/blog/rdf-knowledge-graph | 2026-06-18 |
| 14 | An ontology approach to support FMEA studies — ScienceDirect | https://www.sciencedirect.com/science/article/abs/pii/S0957417409005715 | 2026-06-18 |
| 15 | Upper ontology — Wikipedia | https://en.wikipedia.org/wiki/Upper_ontology | 2026-06-18 |
| 16 | 온톨로지(Ontology) 구축 방법론 — Brunch | https://brunch.co.kr/@writerjeong/290 | 2026-06-18 |
| 17 | Ontology, Taxonomy, and Graph standards: OWL, RDF, RDFS, SKOS — Medium | https://medium.com/@jaywang.recsys/ontology-taxonomy-and-graph-standards-owl-rdf-rdfs-skos-052db21a6027 | 2026-06-18 |
| 18 | RDF vs. Property Graph — TigerGraph | https://www.tigergraph.com/blog/rdf-vs-property-graph-choosing-the-right-foundation-for-knowledge-graphs/ | 2026-06-18 |
| 19 | RDF vs. Property Graphs — Neo4j | https://neo4j.com/blog/knowledge-graph/rdf-vs-property-graphs-knowledge-graphs/ | 2026-06-18 |
| 20 | What does it mean for a data catalog to be powered by a knowledge graph? — data.world | https://data.world/blog/data-catalog-knowledge-graph/ | 2026-06-18 |
| 21 | The role and synergies of ontologies, data catalogs, knowledge graphs — Ontoforce | https://www.ontoforce.com/blog/the-role-and-synergies-of-ontologies-data-catalogs | 2026-06-18 |
| 22 | Research on knowledge graph-driven equipment fault diagnosis — Springer | https://link.springer.com/article/10.1007/s00170-024-12998-x | 2026-06-18 (인증 필요, 직접 접근 불가) |
| 23 | An Intelligent Quality Control Method Based on Human-Cyber-Physical Knowledge Graph — Engineering journal | https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2024.03.022 | 2026-06-18 |
| 24 | Ontologies: Blueprints for Knowledge Graph Structures — FalkorDB | https://www.falkordb.com/blog/understanding-ontologies-knowledge-graph-schemas/ | 2026-06-18 |
| 25 | Data Ontology: 3 Key Types — ER Studio | https://erstudio.com/blog/harmonizing-the-data-ontologies-of-the-organization/ | 2026-06-18 |

---

> **리서치 완료 메모**: Springer 논문(출처 22)은 인증 벽으로 직접 접근 불가. ISO 15926 전문도 인증 필요. 대신 arXiv 2510.15428(PFMEA+LLM+KG)를 주 제조 사례 출처로 활용 권장. 온톨로지 기반 인과 추론(출처 10)은 아카이브 직접 접근 가능, 추가 정독 필요시 참고.
