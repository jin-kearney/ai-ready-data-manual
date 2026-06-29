# E-3 AI 평가 데이터 — 리서치 A: What(구성요소) + How(구축·운영)

> 작성일: 2026-06-26  
> 담당 클러스터: A = What(구성요소) + How(구축·운영)  
> 관점 고정: "AI 성능을 채점할 데이터(평가셋·기준)를 준비·정비하는 법"

---

## 1. What — 평가 데이터의 구성요소

### 1-1. 정답셋(Gold Set / Gold Dataset)의 표준 구성

정답셋은 AI 모델·Prompt·Agent의 성능을 객관적으로 측정하는 **기준 데이터 자산**이다. 각 항목(레코드)은 아래 필드로 구성된다.

| 필드 | 쉬운 의미 | 예시값 | 필수/선택 |
|------|-----------|--------|-----------|
| 질문(Input / Prompt) | AI에 던지는 실제 질문·요청 | "PCB 기판의 Delamination 원인은 무엇인가?" | 필수 |
| 입력 맥락(Context) | 질문과 함께 제공되는 배경 문서·데이터 | 해당 불량 검사보고서 원문 텍스트 | 필수 (RAG형) |
| 기대 답변(Expected Output) | 전문가가 승인한 올바른 답 | "PCB Delamination의 주 원인은 흡습과 급격한 열충격이며, 제조 공정 중 프리프레그 건조 불량이 주요 선행 원인이다." | 필수 |
| 정답 근거(Citation / Source) | 기대 답변의 출처 문서·페이지 | 공정표준서 QS-2024-03, 3.2절 | 필수 (RAG형) |
| 허용 답변 범위(Acceptable Answers) | 표현이 달라도 인정할 수 있는 답변 패턴 | "흡습+열충격", "수분 흡수로 인한 레이어 분리" | 선택 |
| 오류 유형 태그(Error Taxonomy Tag) | 이 문항이 잡으려는 오류 유형 | `hallucination`, `incomplete`, `irrelevant` | 선택 |
| 난이도(Difficulty) | 쉬움·보통·어려움 구분 | `hard` | 선택 |
| 작성 주체(Annotator) | 정답을 작성·승인한 담당자 역할 | 품질기술팀 엔지니어 + 검수자 | 필수 |
| 버전·타임스탬프 | 언제 만들어진 기준인지 | v1.2, 2026-03-10 | 필수 |

**왜 각 필드가 필요한가:**
- **정답 근거(Citation)**: 답변이 실제 문서에 기반한지 확인(RAG 평가의 핵심). 근거가 없으면 채점자가 임의로 판단하게 됨.
- **허용 답변 범위**: AI가 표현만 다르게 정답을 말해도 틀렸다고 처리하는 오류를 방지.
- **오류 유형 태그**: 실패 사례를 축적할 때 어떤 종류의 오류가 많은지 패턴 파악에 쓰임.

출처: [Building a Golden Dataset for AI Evaluation — Maxim AI](https://www.getmaxim.ai/articles/building-a-golden-dataset-for-ai-evaluation-a-step-by-step-guide/) / [Golden Datasets: The Foundation of Reliable AI Evaluation — Medium](https://medium.com/@federicomoreno613/golden-datasets-the-foundation-of-reliable-ai-evaluation-486ce97ce89d)

---

### 1-2. 채점 기준(Rubric / Evaluation Criteria)

채점 기준은 "답변의 어떤 측면을, 어떤 기준으로 몇 점 줄 것인가"를 정의한 표다. 항목별 점수에 행동 기준(Behavioral Anchor)을 붙여야 채점자 간 편차가 줄어든다.

#### 공통 평가 차원

| 평가 차원 | 쉬운 의미 | 채점 예시 (0~4점) |
|----------|-----------|-------------------|
| 정확성(Accuracy) | 답변이 사실과 맞는가 | 4=모두 정확, 2=사소한 오류 1건, 0=주요 사실 오류 |
| 근거성(Groundedness) | 제공된 문서에서 나온 내용인가 | 4=100% 문서 근거, 2=일부 추정 혼재, 0=문서와 무관한 답 |
| 완전성(Completeness) | 질문의 모든 요소에 답했는가 | 4=전부 커버, 2=핵심 누락 1건, 0=절반 이상 누락 |
| 일관성(Consistency) | 여러 번 물어도 같은 답이 나오는가 | 반복 실행 후 답변 분산 측정 |
| 안전성(Safety) | 위험하거나 규정에 어긋난 내용이 없는가 | 4=완전 준수, 0=명백한 위반 |
| 실행가능성(Actionability) | 현업이 바로 쓸 수 있는 구체적 내용인가 | 업무 맥락에 따라 설계 |

#### RAG 전용 평가 지표 (RAGAS 프레임워크)

RAG(Retrieval-Augmented Generation)는 "문서를 검색해서 답하는" 방식이다. 이 방식은 두 단계(검색·생성)를 각각 채점한다.

| 지표 | 쉬운 의미 | 높으면 좋은 것? |
|------|-----------|----------------|
| 충실성(Faithfulness) | 답이 검색된 문서 내용에만 근거하는가 (문서에 없는 말을 지어내지 않는가) | 예 |
| 답변 관련성(Answer Relevancy) | 답이 질문에 정확히 대응하는가 | 예 |
| 맥락 정밀도(Context Precision) | 검색된 문서 중 실제로 유용한 것의 비율 | 예 |
| 맥락 재현율(Context Recall) | 정답에 필요한 정보가 검색 결과에 포함되었는가 | 예 |
| 소음 민감도(Noise Sensitivity) | 불필요한 문서가 섞여도 답이 흔들리지 않는가 | 높을수록 취약 |

출처: [RAGAS 공식 문서 — Metrics](https://docs.ragas.io/en/v0.1.21/concepts/metrics/) / [RAG Evaluation Metrics — Confident AI](https://www.confident-ai.com/blog/rag-evaluation-metrics-answer-relevancy-faithfulness-and-more) / [Ragas Metrics Explained — saulius.io](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge)

출처: [LLM Evaluation Rubrics — Twine Blog](https://www.twine.net/blog/llm-evaluation-rubrics/) / [What is an LLM evaluation rubric? — Twine Blog](https://www.twine.net/blog/what-is-an-llm-evaluation-rubric/)

---

### 1-3. 전문가 코멘트 / 판단 근거 & 오류 유형 분류(Error Taxonomy)

단순 O/X를 넘어 **"왜 틀렸는가"**를 기록하면 평가셋이 개선 데이터로 기능한다.

#### 오류 유형 분류 예시

| 오류 유형 | 쉬운 설명 | 예시 |
|----------|-----------|------|
| 환각(Hallucination) | 문서에 없는 내용을 지어낸 답 | "Delamination 원인이 전압 불안정"이라고 답했으나 문서에 없음 |
| 불완전(Incomplete) | 질문 일부만 답하고 나머지 누락 | 원인은 맞췄지만 대처 방법 누락 |
| 무관(Irrelevant) | 질문과 관계없는 답 | "불량률 통계"를 물었는데 "검사 절차"를 답함 |
| 오래된 정보(Outdated) | 개정 전 기준을 답변 | 구버전 공정표준서 기준 적용 |
| 관계 오류(Relation Error) | 인과·수식 관계를 잘못 연결 | 원인과 결과를 뒤바꾸어 설명 |

#### 평가자 간 일치도(IAA, Inter-Annotator Agreement)

두 명 이상의 전문가가 같은 항목을 채점할 때 **얼마나 의견이 일치하는지** 측정하는 개념이다. 일치도가 낮으면 채점 기준이 모호하다는 신호이므로 기준을 재조정한다.

- **Cohen's κ(카파)**: 두 평가자 간 일치율을 측정하는 대표 지표 (0 = 우연 수준, 1 = 완전 일치)
- κ ≥ 0.7이면 신뢰할 수 있는 평가 기준으로 간주
- 불일치 항목은 토론·기준서 참조로 조정. 조정 후 남은 불일치는 별도 추적

출처: [Inter-Annotator Agreement — Rise Data Labs](https://risedatalabs.com/blog/inter-annotator-agreement) / [Counting on Consensus — arXiv](https://arxiv.org/abs/2603.06865)

---

### 1-4. AI 과제 유형별 평가 데이터 차이

| 과제 유형 | 무엇을 채점하나 | 정답셋의 특징 | 두산 계열사 예시 |
|----------|----------------|--------------|----------------|
| **RAG (문서 검색·답변)** | 충실성·맥락 정밀도·답변 관련성 | 질문 + 참조 문서 + 기대 답변 + 출처 필수 | 설비 점검 매뉴얼 QA, 결함 원인 질의응답 |
| **분류·예측** | 예측값 vs. 정답 레이블 일치 | 입력 + 정답 클래스 레이블 | C/S Report 자동 분류(불량 유형: Delamination·CCL 박리 등) |
| **보고서 생성** | 완전성·정확성·형식 준수 | 입력 + 기대 보고서 요소(항목 목록) + 채점 루브릭 | 설비 이상 분석 보고서 자동 생성 |
| **Agent (다단계 행동)** | 도구 선택 정확성·단계 순서·최종 완료 여부 | 목표 + 기대 행동 경로(Golden Trajectory) + 중간 체크포인트 | 설비 이상 원인 추천 → 작업지시서 생성 → 담당자 알림 Agent |

**Agent 평가의 특이점:**
- 단일 입출력이 아니라 **행동 경로 전체(Trajectory)**가 정답
- 같은 입력이라도 실행 경로가 매번 달라질 수 있어 평가가 어려움(비결정성)
- 평가 레벨: ① 최종 완료 여부, ② 경로 효율성, ③ 개별 도구 호출 정확도

출처: [LLM Agent Evaluation — Confident AI](https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide) / [RAG Evaluation Frameworks — AI Exponent](https://aiexponent.com/the-complete-enterprise-guide-to-rag-evaluation-and-benchmarking/)

---

## 2. How — 구축 절차

### 2-1. 평가 데이터 만드는 절차 (5단계)

#### 1단계: 실제 업무 사례 수집

- 운영 중인 AI 시스템의 실제 질문 로그에서 대표 사례 추출 (개인정보 마스킹 후)
- 전문가가 직접 "이런 질문은 반드시 맞아야 한다"는 **필수 통과 시나리오** 작성
- 경계·실패 사례(Edge Case)도 의도적으로 포함: 애매한 질문, 정보 부족한 질문, 중의적 표현

> 예시 (두산 맥락): CCL 기판 제조 공정에서 Delamination이 발생했을 때 AI 챗봇에 실제로 들어온 질의 100건을 수집 → 다양한 표현 패턴(증상별·공정별)을 커버하도록 대표 30건 선별

#### 2단계: 정답셋 작성

- 각 질문에 대해 **해당 분야 전문가**가 기대 답변 초안 작성
- 참조 문서(공정표준서·기술 매뉴얼)에서 근거 구절 발췌해 Citation 필드에 기록
- 표현이 다른 허용 답변 범위도 함께 정의

**품질 확보 방법:**
- 합성 데이터(Synthetic Data) 도구로 초안 생성 후 전문가가 검수·승인하는 방식도 가능 ("실버 → 골드" 승급)
- 통계적으로 충분한 샘플 수 확보 필요 (일반적으로 시나리오당 200~250건 수준 권장, PoC/공식문서 확인)

출처: [Building a Golden Dataset — Maxim AI](https://www.getmaxim.ai/articles/building-a-golden-dataset-for-ai-evaluation-a-step-by-step-guide/) / [Building a Golden Dataset for Model Evaluation — Twine](https://www.twine.net/blog/building-a-golden-dataset-for-model-evaluation/)

#### 3단계: 채점 기준 합의

- 평가 차원과 점수 기준(0~4 또는 Pass/Fail)을 팀이 함께 정함
- 기준 초안을 가지고 **노밍 세션(Norming Session)**: 샘플 5~10건을 같이 채점해보며 점수 해석 통일
- 평가자 간 일치도(Cohen's κ) 측정 → 0.7 미만이면 기준 재조정

#### 4단계: (자동) 채점 연결

- **결정론적 채점**: 숫자·코드·형식 등 정확히 비교 가능한 항목은 코드로 자동 채점
- **LLM-as-a-Judge**: 텍스트 품질(완전성·근거성 등)은 다른 LLM이 채점. 규모 있는 평가에 적합
- **사람 채점**: 전문 판단이 필요한 항목, LLM 채점 불확실 구간에서 병행

**LLM-as-a-Judge 한계 (반드시 인지):**

| 한계 | 설명 |
|------|------|
| 길이 선호 편향 | 짧고 정확한 답보다 긴 답을 더 좋게 채점하는 경향 |
| 자기 편향 | 같은 계열 모델 답변을 더 높게 채점 |
| 위치 편향 | 비교 시 먼저 나온 답을 선호 |
| 비결정성 | 같은 답변도 실행할 때마다 점수가 달라질 수 있음 |
| 전문 분야 한계 | 반도체·화학·기계 등 전문 도메인에서 사람과의 일치율 60~70%로 낮아짐 |

→ **대응**: 전문가 사람 검수를 병행하고, 단일 LLM이 아닌 여러 모델 패널(Panel of LLM Evaluators)로 편향 완화

출처: [LLM-as-a-Judge Complete Guide — Confident AI](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method) / [LLM-as-a-Judge vs Human Evaluation — Galileo](https://galileo.ai/blog/llm-as-a-judge-vs-human-evaluation)

---

### 2-2. 운영: 회귀 테스트와 평가셋 성장

#### 회귀 테스트(Regression Test)란

모델·Prompt를 변경했을 때 **이전에 맞던 항목이 다시 틀리지 않는지** 확인하는 절차다. 소프트웨어 개발의 "기존 기능이 안 망가졌나" 테스트와 동일한 개념이다.

**운영 흐름:**
```
Prompt 변경 또는 모델 업그레이드
        ↓
전체 평가셋 대상 자동 채점 실행
        ↓
이전 버전과 점수 비교 (delta 리포트)
        ↓
점수 하락 항목 식별 → 원인 분석
        ↓
수정 후 재실행 → 점수 회복 확인
```

> 예시: 설비 이상 원인 추천 Agent의 Prompt를 수정했을 때, 기존 30개 테스트 항목 중 3개에서 점수가 0.85→0.62로 하락 → 해당 질문 유형에 대한 Prompt 재조정

출처: [Building an Evaluation Harness — Towards Data Science](https://towardsdatascience.com/building-an-evaluation-harness-for-production-ai-agents-a-12-metric-framework-from-100-deployments/) / [Prompt Regression Testing — DEV Community](https://dev.to/novaelvaris/prompt-regression-testing-ship-ai-workflows-without-surprises-4449)

#### 실패 사례를 평가셋에 추가해 키우기

- 운영 중 발생한 오답·실패 사례를 정기적으로 수집
- 원인 분류(오류 유형 태그) 후 정답 달아서 평가셋에 추가
- "AI가 처음 틀렸던 것은 다음엔 안 틀린다"가 목표

> 실천 원칙: "AI가 당황스러운 실수를 할 때마다 그것을 회귀 테스트 항목으로 만들어라"  
> 출처: [LLM Agent Evaluation — Confident AI](https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide)

#### 버전 관리

- 평가셋 자체를 코드처럼 버전 관리 (v1.0, v1.1, v2.0…)
- 모델 버전·Prompt 버전과 평가셋 버전을 연결해서 "어떤 설정에서 어떤 성능이었는지" 추적
- 항목 추가·수정 이력을 기록해 비교 가능성 유지

출처: [Prompt Regression Testing — statsig](https://www.statsig.com/perspectives/slug-prompt-regression-testing) / [Best AI Evaluation Tools 2026 — Confident AI](https://www.confident-ai.com/knowledge-base/compare/best-ai-evaluation-tools-for-prompt-experimentation-2026)

---

### 2-3. Evaluation Harness 개념

**Evaluation Harness(평가 하네스)**란 평가셋 + 채점 로직 + 실행 파이프라인을 하나로 묶어 **언제든 반복 실행할 수 있게 한 틀**이다.

쉬운 비유: 공장 품질 검사 지그(Jig)처럼, AI 출력물을 자동으로 통과시켜 여러 항목을 한 번에 측정한다.

**구성 요소:**

| 구성 요소 | 역할 |
|----------|------|
| 평가셋(Gold Dataset) | 기준 질문·정답이 담긴 데이터 자산 |
| 채점 로직(Scorer) | 각 항목을 자동·반수동으로 점수 내는 코드/규칙 |
| 실행 엔진(Runner) | 평가셋 전체를 AI에 일괄 입력하고 출력 수집 |
| 결과 리포트 | 항목별 점수·전체 평균·이전 버전 대비 delta |
| 버전 관리 | 평가셋 버전·모델 버전·Prompt 버전 연결 |

**12개 측정 지표 프레임워크 예시 (Agent 기준):**
- 검색 4개: 맥락 관련성·재현율·정밀도·지연시간
- 생성 3개: 충실성·관련성·환각율
- Agent 전용 3개: 도구 선택 정확도·도구 실행 성공률·다단계 일관성
- 운영 2개: 쿼리당 비용·P99 응답시간

출처: [Top 10 LLM Evaluation Harnesses — DevOps School](https://www.devopsschool.com/blog/top-10-llm-evaluation-harnesses-features-pros-cons-comparison/) / [Building an Evaluation Harness — Towards Data Science](https://towardsdatascience.com/building-an-evaluation-harness-for-production-ai-agents-a-12-metric-framework-from-100-deployments/)

---

## 3. 현업 실행 키트 재료

### 3-1. 정답셋 1건 항목 사전

| 항목명 | 쉬운 의미 | 예시값 (두산 맥락) | 필수/선택 | 작성 주체 |
|--------|-----------|-------------------|-----------|----------|
| 질문 ID | 항목 고유 번호 | `EQ-2026-001` | 필수 | 시스템 자동 |
| 질문 텍스트 | 실제 질문 내용 | "PCB CCL 기판 Delamination 발생 시 우선 점검 항목은?" | 필수 | 현업 엔지니어 |
| 과제 유형 | RAG·분류·생성·Agent 중 하나 | `RAG` | 필수 | 평가 설계자 |
| 입력 맥락 | 질문과 함께 제공할 문서 조각 | 공정표준서 QS-2024-03 3.2절 원문 | 필수(RAG) | 현업 엔지니어 |
| 기대 답변 | 전문가 검증 정답 | "1) 프리프레그 수분 함량 확인 2) 리플로우 온도 프로파일 점검 3) 기판 보관 환경(온습도) 이력 조회" | 필수 | 품질기술팀 선임 |
| 정답 근거 | 출처 문서·절 | 공정표준서 QS-2024-03, §3.2.1, p.14 | 필수(RAG) | 현업 엔지니어 |
| 허용 답변 패턴 | 인정 가능한 다른 표현 | "수분 점검·온도 프로파일·보관 이력" 세 가지를 모두 언급하면 허용 | 선택 | 품질기술팀 선임 |
| 채점 기준 | 이 항목의 채점 루브릭 ID | `RUB-RAG-001` | 필수 | 평가 설계자 |
| 오류 유형 태그 | 잡으려는 오류 유형 | `hallucination`, `incomplete` | 선택 | 평가 설계자 |
| 난이도 | 쉬움·보통·어려움 | `medium` | 선택 | 현업 엔지니어 |
| 검수자 | 정답을 최종 승인한 사람 | 품질기술팀 김△△ 책임 | 필수 | - |
| 버전 | 이 항목의 버전 | v1.0 | 필수 | 시스템 자동 |
| 생성일 | 작성 날짜 | 2026-03-10 | 필수 | 시스템 자동 |

---

### 3-2. Before → After: 나쁜 평가 문항 vs. 좋은 평가 문항

#### 사례 1: 질문 품질

| | 나쁜 예 | 좋은 예 |
|---|---------|---------|
| 질문 | "불량에 대해 설명해줘" | "CCL 기판 제조 공정에서 Delamination이 발생했을 때, 원인 파악을 위해 확인해야 할 3가지 항목을 우선순위 순으로 설명하라." |
| 문제 | 범위가 너무 넓어 어떤 답이 정답인지 정의 불가 | 범위·형식·기준이 명확해 채점 가능 |
| 허용 답변 범위 | 정의 불가 | 수분 함량·온도 프로파일·보관 이력 세 가지 언급 여부로 채점 |

#### 사례 2: 채점 기준 품질

| | 나쁜 예 | 좋은 예 |
|---|---------|---------|
| 채점 기준 | "1~5점으로 채점" | "4점=문서 근거 있고 3항목 모두 언급, 2점=근거 있으나 1항목 누락, 0점=문서 근거 없거나 2항목 이상 누락" |
| 문제 | 채점자마다 기준이 달라 재현 불가 | 채점 기준이 명확해 누가 해도 같은 결과 |

#### 사례 3: 회귀 테스트 항목 추가 (Before = 놓치는 사례 / After = 잡는 사례)

| | Before (평가셋에 없을 때) | After (평가셋에 추가 후) |
|---|--------------------------|-------------------------|
| 상황 | AI가 C/S Report 분류 시 "불량 원인 미상"을 "기타"로 분류 → 놓침 | 동일 케이스를 평가셋에 추가 + 정답="원인미상(Unknown)" |
| 결과 | 다음 모델 업데이트 때 같은 오류 재발 | 회귀 테스트에서 잡혀 배포 전 수정 |

출처: [Prompt Regression Testing — statsig](https://www.statsig.com/perspectives/slug-prompt-regression-testing) / [LLM Evaluation Rubrics — Twine](https://www.twine.net/blog/llm-evaluation-rubrics/)

---

### 3-3. 빈 템플릿 + 완성 1건 예시

#### 빈 템플릿

```
질문 ID: [자동 생성]
질문 텍스트: 
과제 유형: [RAG / 분류 / 생성 / Agent]
입력 맥락: [참조 문서 원문 또는 N/A]
기대 답변: 
정답 근거: [출처 문서명·절·페이지]
허용 답변 패턴: 
채점 기준 ID: 
오류 유형 태그: 
난이도: [쉬움 / 보통 / 어려움]
검수자: 
버전: v1.0
생성일: 
```

#### 완성 예시 1건 (두산 계열사 — RAG 과제)

```
질문 ID: EQ-2026-042
질문 텍스트: "두산에너빌리티 가스터빈 Hot Gas Path 부품 점검 주기는 몇 시간인가?"
과제 유형: RAG
입력 맥락: [가스터빈 유지보수 매뉴얼 GT-MNT-2025-01, §4.3 Hot Gas Path Inspection 원문]
기대 답변: "Hot Gas Path 부품의 정기 점검 주기는 24,000 운전시간(EOH 기준)이며, 고온·고부하 조건 이력이 있는 경우 16,000 EOH로 단축된다."
정답 근거: GT-MNT-2025-01, §4.3.2, p.47
허용 답변 패턴: "24,000 EOH" 언급 + 단축 조건(고온·고부하) 언급이면 허용. 단위 누락 시 감점.
채점 기준 ID: RUB-RAG-001
오류 유형 태그: hallucination, incomplete
난이도: 보통
검수자: 가스터빈 정비팀 이△△ 책임
버전: v1.0
생성일: 2026-03-15
```

#### 완성 예시 2건 (두산 계열사 — 분류 과제)

```
질문 ID: EQ-2026-087
질문 텍스트: [C/S Report 원문] "기판 표면에 하얀 반점이 발생하고 레이어 간 분리 징후가 보임. 리플로우 후 발생."
과제 유형: 분류
입력 맥락: N/A (분류 모델은 문서 참조 없이 분류)
기대 답변: Delamination
허용 답변 패턴: "Delamination" 또는 "층간 분리"
채점 기준 ID: RUB-CLS-002
오류 유형 태그: 오분류(Misclassification)
난이도: 어려움 (Blister와 혼동 가능)
검수자: PCB 품질기술팀 박△△ 선임
버전: v1.0
생성일: 2026-04-02
```

---

## 4. 제조 현업(두산) 예시 소재 정리

| AI 과제 | 평가 데이터 관점 필요 항목 | 비고 |
|---------|--------------------------|------|
| 품질 결함 원인 QA (RAG) | 불량 증상 질문 + 공정표준서 맥락 + 기대 원인 답변 + 출처 절번호 | Delamination·CCL 박리·Void·Blister 등 결함명 그대로 사용 |
| C/S Report 자동 분류 | Report 원문 + 정답 불량 유형 레이블 | 레이블 체계는 기존 분류 코드표 기준 |
| 설비 이상 원인 추천 Agent | 이상 증상 입력 + 기대 행동 경로(진단→원인파악→대안 제시) + 최종 결론 | Agent 특성상 경로 전체가 정답 |
| 검사 기준 문서 검색 (RAG) | "○○ 기준은 얼마인가" + 해당 규격서 맥락 + 기대 답변 + 규격서 조항 | 공차·규격 수치 정확성이 핵심 |

> **가상 예시 표기**: 위 수치(24,000 EOH 등)는 설명용 가상 예시이며, 실제 점검 주기는 해당 설비 제조사 매뉴얼을 확인한다.

---

## 5. 출처 목록

| 번호 | 이름 | URL |
|------|------|-----|
| 1 | Building a Golden Dataset for AI Evaluation — Maxim AI | https://www.getmaxim.ai/articles/building-a-golden-dataset-for-ai-evaluation-a-step-by-step-guide/ |
| 2 | Golden Datasets: The Foundation of Reliable AI Evaluation — Medium | https://medium.com/@federicomoreno613/golden-datasets-the-foundation-of-reliable-ai-evaluation-486ce97ce89d |
| 3 | Building a Golden Dataset for Model Evaluation — Twine | https://www.twine.net/blog/building-a-golden-dataset-for-model-evaluation/ |
| 4 | What Is a Golden Dataset in AI — DAC.digital | https://dac.digital/what-is-a-golden-dataset/ |
| 5 | RAGAS 공식 문서 — Metrics | https://docs.ragas.io/en/v0.1.21/concepts/metrics/ |
| 6 | RAG Evaluation Metrics — Confident AI | https://www.confident-ai.com/blog/rag-evaluation-metrics-answer-relevancy-faithfulness-and-more |
| 7 | Ragas Metrics Explained — saulius.io | https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge |
| 8 | LLM Evaluation Rubrics — Twine Blog | https://www.twine.net/blog/llm-evaluation-rubrics/ |
| 9 | What is an LLM evaluation rubric? — Twine Blog | https://www.twine.net/blog/what-is-an-llm-evaluation-rubric/ |
| 10 | Rubric-Based Evaluations & LLM-as-a-Judge — Medium (Adnan Masood PhD) | https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80 |
| 11 | LLM-as-a-Judge Complete Guide — Confident AI | https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method |
| 12 | LLM-as-a-Judge vs Human Evaluation — Galileo | https://galileo.ai/blog/llm-as-a-judge-vs-human-evaluation |
| 13 | Inter-Annotator Agreement — Rise Data Labs | https://risedatalabs.com/blog/inter-annotator-agreement |
| 14 | Counting on Consensus (IAA) — arXiv | https://arxiv.org/abs/2603.06865 |
| 15 | LLM Agent Evaluation Complete Guide — Confident AI | https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide |
| 16 | Building an Evaluation Harness — Towards Data Science | https://towardsdatascience.com/building-an-evaluation-harness-for-production-ai-agents-a-12-metric-framework-from-100-deployments/ |
| 17 | Top 10 LLM Evaluation Harnesses — DevOps School | https://www.devopsschool.com/blog/top-10-llm-evaluation-harnesses-features-pros-cons-comparison/ |
| 18 | Prompt Regression Testing — DEV Community | https://dev.to/novaelvaris/prompt-regression-testing-ship-ai-workflows-without-surprises-4449 |
| 19 | Prompt Regression Testing — statsig | https://www.statsig.com/perspectives/slug-prompt-regression-testing |
| 20 | RAG Evaluation Frameworks — AI Exponent | https://aiexponent.com/the-complete-enterprise-guide-to-rag-evaluation-and-benchmarking/ |
| 21 | RAG Evaluation 2026 — Label Your Data | https://labelyourdata.com/articles/llm-fine-tuning/rag-evaluation |
| 22 | Best AI Evaluation Tools 2026 — Confident AI | https://www.confident-ai.com/knowledge-base/compare/best-ai-evaluation-tools-for-prompt-experimentation-2026 |
| 23 | Ensuring Reproducibility in Generative AI — arXiv | https://arxiv.org/pdf/2505.02854 |
