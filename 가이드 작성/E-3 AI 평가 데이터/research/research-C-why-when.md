# E-3 AI 평가 데이터 — 리서치 C: Why(왜) + When(언제·어떤 과제에)

> 작성일: 2026-06-26  
> 담당 클러스터: C = Why + When (선택형 주제 통합)  
> 관점: "AI 성능을 채점할 **평가 데이터를 준비**하는 법" — AI를 만드는 법이 아님  
> 독자: 제조 대기업(두산) 현업

---

## 1. 현업 Pain Point — 평가 데이터가 없을 때 생기는 문제

### 1-1. "잘 되는 것 같다"는 감(感)뿐 — 숫자가 없다

평가 데이터셋(정답셋, Ground Truth)이 없으면 AI 성능을 숫자로 표현할 방법이 없다. 담당자가 몇 가지 질문을 던져보고 "대체로 괜찮은 것 같다"는 인상(vibe check)으로 판단한다. 이 주관적 검증 방식은 확장이 불가능하고 담당자의 피로도·편향에 전적으로 의존한다.

> **핵심 문제**: "느낌이 더 좋다"는 판단으로는 프로덕션 AI를 안심하고 운용할 수 없다. 전통적 소프트웨어 테스트처럼 객관적 기준이 없으면 배포 결정 자체가 근거를 잃는다.  
> 출처: [Stop Evaluating LLMs with "Vibe Checks" — Towards Data Science](https://towardsdatascience.com/stop-evaluating-llms-with-vibe-checks/)

### 1-2. Prompt·모델을 바꿨는데 더 나빠졌는지 알 수 없다

RAG 검색 로직을 수정하거나, Prompt를 다듬거나, 모델 버전을 올렸을 때 — 전후 성능을 비교할 기준점이 없으면 개선인지 퇴보인지 알 방법이 없다. "단순한 Prompt 변경 하나가 이전에 잘 답하던 항목의 품질을 크게 떨어뜨릴 수 있지만, 회귀 테스트 파이프라인이 없으면 배포 전에 이를 잡지 못한다." [[1]](#ref1)

**두산 가상 시나리오**: 품질 결함 원인 질의응답(RAG) 시스템에서 Prompt를 수정한 뒤, 특정 결함 유형(예: Delamination)에 대한 답변 품질이 조용히 나빠졌다. 담당자는 한참 뒤 현장에서 민원이 들어오고 나서야 발견했다. 평가셋이 있었다면 배포 직전 자동으로 잡을 수 있었다.

### 1-3. 조용한 회귀(Regression) — 한 번 잘 되다가 모르게 망가진다

AI 시스템은 외부 변수(모델 API 업데이트, 데이터 변화, Prompt 조정)에 따라 특정 케이스의 성능이 조용히 저하된다. 문제를 일으키기 전까지 아무도 모른다는 점이 전통적 소프트웨어 버그와 다르다. 생산 트래픽의 일부를 지속적으로 샘플링해 자동 평가기로 점수를 매기지 않으면 드리프트(drift)를 감지할 수 없다. [[2]](#ref2)

### 1-4. 베테랑 눈검사 의존 — 사람이 매번 확인해야 해서 못 키운다

AI 과제가 늘어날수록 각 과제 산출물을 사람이 일일이 눈으로 확인하는 비용이 선형으로 늘어난다. 평가를 자동화하지 않으면 AI 과제 수를 늘릴수록 QA 비용이 같이 늘어나 결국 병목이 생긴다. "수천 개의 쿼리를 분 단위에 자동으로 실행하는 알고리즘 벤치마킹"이 가능해지려면 평가 데이터셋이 먼저 있어야 한다. [[1]](#ref1)

### 1-5. 개선의 근거가 없다 — 설명할 수가 없다

경영진·현업에 "이번 Prompt 개선으로 성능이 올랐다"고 설명하려면 비교 수치가 있어야 한다. 평가셋 없이는 "우리 팀이 테스트해보니 더 나은 것 같다"는 말 이상을 할 수 없고, AI 투자 정당화가 어렵다. [[3]](#ref3)

---

## 2. 기대 효과 — 평가 데이터를 갖추면 달라지는 것

| 문제 (Before) | 개선 (After) |
|---|---|
| 감(感)으로 성능 판단 | 정확도·재현율 등 수치로 비교 |
| Prompt 바꿨는데 더 나빠졌는지 모름 | 변경 전후 점수 자동 비교, 퇴보 즉시 확인 |
| 회귀 문제를 사용자 민원 뒤에 발견 | 배포 전 자동 회귀 테스트로 차단 |
| 사람이 매번 눈으로 검수 → 확장 불가 | 자동화 평가로 과제 수 늘려도 QA 비용 고정 |
| "더 나은 것 같다"는 구두 보고 | 수치 근거로 경영진 보고, 투자 정당화 |

> 골든 데이터셋(Golden Dataset, 정답셋)은 "모델·에이전트가 배포 전에 반드시 통과해야 하는 정식 기준점"이다. 수백~수천 건 규모, 전문가가 검토한 정답 포함, 모든 모델 버전이 배포 전에 통과해야 한다. [[4]](#ref4)

**개선 규모는 가상 예시로만**: 구체 수치(예: "정확도 X% 향상")는 회사 As-Is가 측정해야 하므로 이 가이드에서 단정하지 않는다.

---

## 3. 적용 판단 — 어떤 AI 과제에 평가 데이터가 필요한가

### 3-1. 판단 기준: 두 가지 축

```
              틀렸을 때 손해가 크다
                      ↑
      [정식 평가셋 필수]     [정식 평가셋 강권]
              |                    |
답의 옳고  ←──────────────────────────────→ 자주 바뀐다
그름이 중요          |                    (Prompt·모델 업데이트)
              [약식 체크로 가능]  [주기적 샘플 검증]
                      ↓
              틀려도 손해가 작다
```

**정식 평가셋이 필수인 과제 (둘 다 해당하는 경우)**:
- 틀리면 현업·품질·안전에 직접 영향
- 동시에 답의 옳고 그름이 명확하게 판단 가능한 과제

**약식 체크로 충분한 과제**:
- 초안 도우미, 내부 메모 요약처럼 "참고용"이고 사람이 최종 판단하는 경우
- 틀려도 재시도·사람 교정으로 쉽게 복구 가능한 경우

### 3-2. 두산 계열사 맥락: 평가셋이 필요한 과제 유형

| AI 과제 유형 | 필요 이유 | 평가 우선도 |
|---|---|---|
| **품질 결함 원인 RAG** | 잘못된 원인 제시 → 대책 방향 오류 → 불량 반복 | 높음 |
| **검사 기준 검색 시스템** | 기준 오해석 → 합격품 불합격·불합격품 합격 | 높음 |
| **설비 이상 원인 추천** | 오진단 → 잘못된 대응 → 설비 추가 손상 가능 | 높음 |
| **C/S Report 분류** | 잘못된 분류 → 유관부서 오라우팅, 대응 지연 | 중간 |
| **회의록 요약** | 참고용, 사람이 확인 후 사용 | 낮음 (약식) |
| **초안 문서 도우미** | 작성자가 최종 검토·수정 | 낮음 (약식) |

> RAG 시스템 평가는 검색 관련성(Retrieval Relevance)과 생성 충실성(Generation Faithfulness)을 함께 측정해야 하며, 도메인 특화 질문·정답·컨텍스트를 포함한 고품질 어노테이션 데이터셋이 필수다. [[5]](#ref5)

### 3-3. "답의 옳고 그름이 중요한" 과제의 공통점

다음 특성 중 하나라도 해당하면 평가 데이터셋을 만든다:

1. **정답이 존재한다** — 분류, 검색, 사실 QA처럼 맞다/틀리다를 명확히 판별할 수 있는 과제
2. **잘못된 답이 현업 의사결정에 직접 영향** — 결함 판정, 원인 분석, 안전 관련 판단
3. **Prompt·모델·데이터가 자주 바뀐다** — 변경 때마다 성능 재검증이 필요
4. **규정·기준에서 벗어나면 안 된다** — 품질 규격, 안전 기준, 법적 요건

### 3-4. LLM-as-judge만으로 부족한 이유

"AI가 AI를 평가하게 하면 되지 않나"는 생각은 일부 맞지만 한계가 있다. LLM 평가자는 "사용자 행동과 비즈니스 도메인의 특수 맥락을 이해하지 못한다." 맥락 재현율(Context Recall)처럼 기준 정답 없이는 측정 자체가 불가능한 지표도 있다. 정답셋 기반 평가(Reference-based Eval)가 없으면 "실험에서 맹목적으로 아이디어만 반복하는" 상태가 된다. [[6]](#ref6)

---

## 4. 우선순위 — 어디부터 평가셋을 만드나

### 4-1. 세 가지 축으로 우선순위 결정

**사용량 × 손해 크기 × 변경 빈도**로 우선 과제를 고른다.

| 축 | 설명 | 판단 질문 |
|---|---|---|
| 사용량 | 이 AI가 하루 몇 건 처리하나 | 사용량 많을수록 오류의 영향 범위가 넓다 |
| 손해 크기 | 틀렸을 때 결과가 얼마나 심각한가 | 안전·품질·비용에 직접 연결되는가 |
| 변경 빈도 | Prompt·모델·데이터가 얼마나 자주 바뀌나 | 자주 바뀔수록 회귀 위험이 높다 |

**우선순위 공식(단순화)**:
> 우선도 = 사용량 크기 + 손해 심각도 + 변경 빈도 → 세 가지 모두 높은 과제부터

### 4-2. 실무 시작점

기업용 LLM 평가에서 권장하는 평가셋 초기 규모는 **100~500건**의 실제 생산 데이터로 출발한다. 전문가(현업 담당자 또는 QA 엔지니어)가 직접 검토해 대표 케이스, 엣지 케이스, 어려운 케이스를 고루 포함시킨다. 일반 벤치마크(MMLU 등)는 제조 도메인의 특수 과제에는 맞지 않아 직접 구성해야 한다. [[7]](#ref7)

### 4-3. 가벼운 과제는 샘플 검증으로

초안 도우미·메모 요약처럼 우선도가 낮은 과제는 전수 정답셋 대신, 주기적으로 실제 출력 결과 중 일부를 샘플링해 사람이 검토하는 "약식 체크"로 시작한다. 정식 평가셋은 운용 중 이슈가 생기거나 사용량·중요도가 올라가면 그때 만든다.

---

## 5. 개념 보강 — AI 평가의 일반 원리

### 5-1. 왜 정답셋이 있어야 객관 평가가 되나

AI 성능을 측정하려면 "기대하는 답"이 미리 정의되어 있어야 한다. 정답셋(Ground Truth)은 입력(질문·케이스)과 그에 대응하는 기대 출력(올바른 답·판정)을 짝지어 놓은 데이터다. 이것이 없으면:
- 모델 A와 모델 B 중 어느 것이 더 낫다는 수치 비교가 불가능하다.
- 성능이 "올랐다"거나 "내려갔다"는 말을 객관적으로 증명할 수 없다.
- 자동화 테스트 파이프라인의 합격/불합격 기준 자체가 없다.

> "LLM 평가는 테스트 데이터셋의 품질만큼만 좋다. 품질이 낮거나 오래된 데이터셋으로는 평가 결과가 의미 없다." [[6]](#ref6)

### 5-2. "Vibe Check"(감으로 보기)의 구조적 한계

비브 체크는 담당자가 AI에 몇 가지 질문을 던지고 "대체로 괜찮아 보인다"고 판단하는 방식이다. 이 방식의 한계:

- **편향**: 담당자가 익숙한 케이스만 보게 된다 — 엣지 케이스·드문 결함 유형은 놓친다.
- **재현 불가**: 어제와 오늘 같은 테스트를 다시 하더라도 판단이 달라질 수 있다.
- **확장 불가**: AI 과제가 10개가 되면 10명이 각자 매번 눈으로 확인해야 한다.
- **비교 불가**: "예전보다 나아졌는가"를 수치로 말하지 못한다.

### 5-3. 회귀 테스트 — 소프트웨어 테스트와 닮은 점

전통적 소프트웨어 QA에서는 코드를 수정할 때마다 단위 테스트(Unit Test)를 돌려 기존 기능이 망가지지 않았는지 확인한다. AI 평가 데이터셋은 이 단위 테스트의 역할을 AI 성능 차원에서 한다.

| 소프트웨어 테스트 | AI 평가 데이터셋 |
|---|---|
| 단위 테스트 케이스 | 평가 질문-정답 쌍 |
| 코드 변경 시 자동 실행 | Prompt·모델 변경 시 자동 평가 |
| 합격/불합격 판정 | 점수 임계값 초과 여부 |
| 회귀 방지 | 성능 퇴보 조기 차단 |
| CI/CD 게이트 | 평가 통과 전 배포 차단 |

"LLM 회귀 테스트는 생성 AI에 표준 CI/CD 관행을 도입하는 것이다 — 수동 스팟체크는 없어진다." [[1]](#ref1)

### 5-4. 골든셋(Golden Dataset)의 구성 요소

권장 초기 규모: **100~300건** (충분히 다양하게)

포함해야 할 케이스 유형:
- **표준 케이스**: 가장 흔한 입력 유형 — 일상적인 질문·요청
- **엣지 케이스**: 드물지만 틀리면 심각한 케이스 (예: 특정 결함 코드, 예외 상황)
- **모호한 케이스**: 판단이 까다로운 중간 영역
- **부정 케이스**: AI가 "모른다" 또는 "해당 없음"을 답해야 하는 케이스

형식: 입력(질문/케이스) + 기대 출력(정답/판정) + 필요 시 정답 컨텍스트 [[1]](#ref1)

### 5-5. 평가 지표 개요 (참고)

평가 데이터셋이 있을 때 측정 가능한 주요 지표:

- **정확도(Accuracy)**: 정답과 일치하는 비율 — 분류·판정 과제
- **검색 관련성(Retrieval Relevance)**: RAG에서 가져온 문서가 질문에 맞는 비율
- **충실성(Faithfulness)**: 생성된 답이 원본 문서에 근거하는 비율 (환각 방지)
- **점수 기반 비교**: 변경 전후 점수 차이로 개선/퇴보 확인

지표 선택은 과제 유형(분류·RAG·자유형 생성)에 따라 달라진다. 이 가이드에서는 "어떤 지표를 쓰나"보다 "왜 데이터가 먼저 있어야 하나"에 집중한다.

---

## 출처 목록

<a id="ref1"></a>**[1]** LLM Regression Testing Pipeline for QA Engineers — [https://testquality.com/llm-regression-testing-pipeline/](https://testquality.com/llm-regression-testing-pipeline/)

<a id="ref2"></a>**[2]** Building an LLM Evaluation Framework: Best Practices — Datadog — [https://www.datadoghq.com/blog/llm-evaluation-framework-best-practices/](https://www.datadoghq.com/blog/llm-evaluation-framework-best-practices/)

<a id="ref3"></a>**[3]** LLM Evaluation for Enterprise — Beyond Benchmarks (2026 Guide) — Knowlee — [https://www.knowlee.ai/blog/llm-evaluation-enterprise-guide](https://www.knowlee.ai/blog/llm-evaluation-enterprise-guide)

<a id="ref4"></a>**[4]** LLM Evals Are Based on Vibes — I Built the Missing Layer — Towards Data Science — [https://towardsdatascience.com/llm-evals-are-based-on-vibes-i-built-the-missing-layer-that-decides-what-ships/](https://towardsdatascience.com/llm-evals-are-based-on-vibes-i-built-the-missing-layer-that-decides-what-ships/)

<a id="ref5"></a>**[5]** RAG Evaluation — Hugging Face Cookbook — [https://huggingface.co/learn/cookbook/en/rag_evaluation](https://huggingface.co/learn/cookbook/en/rag_evaluation)

<a id="ref6"></a>**[6]** LLM Evaluation Metrics and Methods, Explained Simply — Evidently AI — [https://www.evidentlyai.com/llm-guide/llm-evaluation-metrics](https://www.evidentlyai.com/llm-guide/llm-evaluation-metrics)

<a id="ref7"></a>**[7]** LLM Benchmarking for Enterprise Production — TrueFoundry — [https://www.truefoundry.com/blog/llm-benchmarking-enterprise-production](https://www.truefoundry.com/blog/llm-benchmarking-enterprise-production)

<a id="ref8"></a>**[8]** Stop Evaluating LLMs with "Vibe Checks" — Towards Data Science — [https://towardsdatascience.com/stop-evaluating-llms-with-vibe-checks/](https://towardsdatascience.com/stop-evaluating-llms-with-vibe-checks/)

<a id="ref9"></a>**[9]** How to Evaluate an LLM System — Thoughtworks — [https://www.thoughtworks.com/insights/blog/generative-ai/how-to-evaluate-an-LLM-system](https://www.thoughtworks.com/insights/blog/generative-ai/how-to-evaluate-an-LLM-system)

<a id="ref10"></a>**[10]** The Definitive Guide to LLM Evaluation — Arize AI — [https://arize.com/llm-evaluation/](https://arize.com/llm-evaluation/)

<a id="ref11"></a>**[11]** Ground Truth Data for AI — SuperAnnotate — [https://www.superannotate.com/blog/ground-truth-data-for-ai](https://www.superannotate.com/blog/ground-truth-data-for-ai)

<a id="ref12"></a>**[12]** RAG Evaluation Metrics: Best Practices — Patronus AI — [https://www.patronus.ai/llm-testing/rag-evaluation-metrics](https://www.patronus.ai/llm-testing/rag-evaluation-metrics)
