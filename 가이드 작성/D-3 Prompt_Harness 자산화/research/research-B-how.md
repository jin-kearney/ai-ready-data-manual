# D-3 Prompt/Harness 자산화 — How·When 클러스터 리서치
> 작성 목적: D-3 가이드 작성 에이전트용 리서치 원자료. How(구축·운영)·When(적용 판단) 클러스터 전담.
> 관점 고정: "Prompt·Harness를 조직의 재사용 가능한 데이터 자산으로 구조화·등록·버전관리·재사용·운영하는 법" — 에이전트 구축법이 아님.
> 작성일: 2026-06-24

---

## 목차
1. [When — 무엇을 자산화 대상으로 삼나](#1-when--무엇을-자산화-대상으로-삼나)
2. [How A — 구축 절차 (End-to-End)](#2-how-a--구축-절차-end-to-end)
3. [How B — Prompt 버전 관리 (Prompt Versioning)](#3-how-b--prompt-버전-관리-prompt-versioning)
4. [How C — 의존성 관리 (Prompt Dependency)](#4-how-c--의존성-관리-prompt-dependency)
5. [How D — 성능 저하 감지·개선](#5-how-d--성능-저하-감지개선)
6. [How E — Before→After 작성 규칙 (현업 실행 키트 재료)](#6-how-e--beforeafter-작성-규칙-현업-실행-키트-재료)
7. [How F — 역할 (RACI)](#7-how-f--역할-raci)
8. [Harness 패키징 — 재사용 단위 정의](#8-harness-패키징--재사용-단위-정의)
9. [제조 맥락 End-to-End 사례 — 두산전자 품질 클레임 원인 분석](#9-제조-맥락-end-to-end-사례--두산전자-품질-클레임-원인-분석)
10. [Prompt Registry 도구 참고](#10-prompt-registry-도구-참고)
11. [출처 목록](#11-출처-목록)

---

## 1. When — 무엇을 자산화 대상으로 삼나

### 1-1. 자산화 판단 기준 (4가지 필터)

베스트프랙티스([출처: Segev Shmueli, Medium — "Managing Prompts as Enterprise Assets"](https://medium.com/@segev_shmueli/managing-prompts-as-enterprise-assets-a-portfolio-approach-e9552e24f327), [출처: Prompt Orchestration Governance Whitepaper](https://enjtorian.github.io/prompt-orchestration-governance-whitepaper/))에서 공통으로 제시하는 자산화 대상 선별 기준은 4가지다.

| 기준 | 설명 | 예시 (제조·두산) |
|---|---|---|
| **반복성** | 같은 업무에 주기적으로 쓰이는 Prompt | 주간 C/S Report 분류, 월별 불량 원인 요약 |
| **업무 영향도** | 의사결정·품질 판정·고객 대응에 직접 영향 | 클레임 원인 분류, CCL Delamination 판정 지원 |
| **재사용 가능성** | 타 부서·계열사에서도 유사 목적으로 쓸 수 있음 | 품질 원인 분석 → 두산에너빌리티 용접 결함에도 적용 |
| **노하우 함축도** | 현업 전문가의 판단 기준·제외 규칙이 담겨 있음 | "소재 결함 vs 공정 결함" 구분 기준이 명문화된 Prompt |

**자산화 제외 대상:**
- 1회성 실험·탐색용 Prompt
- 개인이 임시로 쓰는 챗봇 질문
- 특정 데이터셋에만 동작하고 일반화 불가능한 Prompt
- 아직 평가(E-3)를 거치지 않아 품질 미검증 상태인 Prompt

### 1-2. 자산화 성숙도 단계 (POG 5단계)

POG(Prompt Orchestration Governance) 프레임워크([출처](https://enjtorian.github.io/prompt-orchestration-governance-whitepaper/))는 모든 Prompt가 자산이 될 필요는 없으며, 조직 필요에 따라 다음 단계를 밟는다고 정의한다.

```
[대화형] → [발굴됨] → [정규화됨] → [검증됨] → [기술 자산(Skill Prompt)]
Ad-hoc       보존 가치    파라미터화·    평가셋 통과·   배포 가능한
대화          식별됨       일반화됨        반복 개선됨    조직 자산
```

단계 설명:
1. **Interaction Prompt** — 일회성 대화, 보존 불필요
2. **Discovered Prompt** — 재사용 가치가 있어 보존 결정
3. **Normalized Prompt** — 특정 맥락에서 일반화·파라미터화 (`{{입력변수}}` 형식)
4. **Validated Prompt** — 평가셋 대비 성능 검증 완료, 반복 개선 이력 존재
5. **Skill Prompt (기술 자산)** — Registry에 등록된 배포 가능한 조직 자산

> 제조 현업 적용 포인트: "C/S Report 분류" Prompt는 처음엔 개인 탐색(1단계)→반복 사용됨을 인지(2단계)→템플릿화(3단계)→테스트(4단계)→Registry 등록(5단계)으로 격상한다.

### 1-3. 우선순위 선정 — 작게 시작하는 원칙

현업 노하우가 담긴 반복 업무 3가지를 먼저 자산화한다([출처: Prompt Governance CIO Article](https://www.cio.com/article/4130960/prompt-governance-is-the-new-data-governance.html)):
1. 가장 빈번하게 쓰이는 Prompt (횟수 기준)
2. 오류 발생 시 업무 손실이 큰 Prompt (영향도 기준)
3. 여러 사람이 각자 다르게 만들어 쓰고 있는 Prompt (중복 낭비 제거 기준)

---

## 2. How A — 구축 절차 (End-to-End)

### 2-1. 6단계 구축 절차

([출처: Braintrust — "What is Prompt Versioning"](https://www.braintrust.dev/articles/what-is-prompt-versioning), [출처: Maxim AI — Prompt Versioning Best Practices](https://www.getmaxim.ai/articles/prompt-versioning-and-its-best-practices-2025/), [출처: POG Whitepaper](https://enjtorian.github.io/prompt-orchestration-governance-whitepaper/))

```
① 대상 업무 선정
   ↓
② 업무 절차 → Prompt 변환
   ↓
③ 의존성 연결
   (데이터 자산·Glossary·Tool·평가셋)
   ↓
④ 테스트·평가 (E-3 평가셋 활용)
   ↓
⑤ Harness 패키징
   (Prompt + 입력 데이터 + Tool 순서 + 출력 형식)
   ↓
⑥ Registry 등록·배포 승인
```

**각 단계의 산출물:**

| 단계 | 주요 활동 | 산출물 |
|---|---|---|
| ① 대상 선정 | 반복성·영향도 기준으로 자산화 후보 식별 | 자산화 대상 Prompt 후보 목록 |
| ② 변환 | 현업 SME 인터뷰 → 업무 절차를 Prompt 구조로 문서화 | 구조화된 Prompt 초안 (입력·판단·출력·금지 구분) |
| ③ 의존성 연결 | Prompt가 참조하는 데이터 자산·Glossary 용어·Tool·평가 기준 식별 | 의존성 맵 (Dependency Map) |
| ④ 테스트·평가 | E-3 평가셋 기반 성능 측정, 기준 이상 통과 여부 확인 | 평가 리포트 (통과/불통과 판정 포함) |
| ⑤ Harness 패키징 | Prompt + 컨텍스트 + Tool 순서 + 출력 형식을 하나의 실행 단위로 묶음 | Harness 명세서 |
| ⑥ 등록·배포 | Registry에 메타데이터 입력, 담당 승인자 검토 후 `배포(Deployed)` 상태 전환 | Registry 등록 레코드 + 배포 승인 기록 |

### 2-2. Prompt 구조화 템플릿 (업무 절차 → Prompt 변환)

([출처: LaunchDarkly — Prompt Versioning and Management](https://launchdarkly.com/blog/prompt-versioning-and-management/), [출처: Quality Magazine — LLMs for Quality Engineers](https://www.qualitymag.com/articles/99113-harnessing-the-power-of-llms-prompt-engineering-for-quality-engineers/))

업무 절차를 Prompt로 바꿀 때 4개 구획으로 분리한다:

```
[역할 정의]
당신은 두산전자 CCL 생산 품질팀의 불량 원인 분류 전문가입니다.

[입력 데이터]
- C/S Report 본문: {{cs_report_text}}
- 관련 공정 데이터: {{process_data}}
- Glossary 표준 결함 유형: {{defect_taxonomy}}

[판단 기준 (Judgment Rules)]
1. "층간 분리(Delamination)"는 소재 결함과 공정 결함 두 가지 원인으로 분류한다.
2. 소재 결함 판정 조건: ... (기준 명시)
3. 공정 결함 판정 조건: ... (기준 명시)
4. 동시에 해당하는 경우 주원인을 먼저 기재한다.

[금지 행동]
- Glossary에 없는 결함 유형을 임의로 만들지 않는다.
- 판단 근거를 생략하지 않는다.
- 추측으로 원인을 단정하지 않는다.

[출력 형식]
{
  "primary_cause": "표준 결함 유형(Glossary 코드)",
  "sub_cause": "세부 원인",
  "confidence": "high/medium/low",
  "evidence": "판단 근거 (보고서 인용)",
  "needs_review": true/false
}
```

이 4구획 구조(역할·입력·판단·금지·출력)가 "좋은 Prompt 자산"의 최소 조건이다.

---

## 3. How B — Prompt 버전 관리 (Prompt Versioning)

### 3-1. 시맨틱 버저닝 (Semantic Versioning)

([출처: Maxim AI](https://www.getmaxim.ai/articles/prompt-versioning-and-its-best-practices-2025/), [출처: Segev Shmueli Medium](https://medium.com/@segev_shmueli/managing-prompts-as-enterprise-assets-a-portfolio-approach-e9552e24f327))

Prompt에도 소프트웨어 시맨틱 버저닝(SemVer) 원칙을 적용한다: `X.Y.Z`

| 버전 자리 | 의미 | 변경 예시 |
|---|---|---|
| **Major (X)** | 업무 판단 구조·역할 정의 대폭 변경 | 분류 체계 전면 개편, 입력 구조 변경 |
| **Minor (Y)** | 기준 추가·출력 형식 변경 | 새 결함 유형 추가, 판단 조건 2개 추가 |
| **Patch (Z)** | 문구 수정·표현 개선 | 오탈자, 문장 명확화 |

예시: `claim-classification-v2.1.0`
- `claim-classification` = Prompt 식별자
- `v2.1.0` = Major 2, Minor 1, Patch 0

### 3-2. 불변성 원칙 (Immutability)

([출처: Braintrust](https://www.braintrust.dev/articles/what-is-prompt-versioning))

**배포된 Prompt 버전은 절대 수정하지 않는다.** 수정이 필요하면 반드시 새 버전을 생성한다. 이유:
- 운영 로그·추적 기록이 특정 버전에 고정되어야 신뢰 가능
- 롤백 시 "되돌아갈 버전"이 변하지 않아야 정확한 복원 보장

### 3-3. Prompt 상태(State) 관리

([출처: POG Whitepaper](https://enjtorian.github.io/prompt-orchestration-governance-whitepaper/), [출처: AISquare Medium](https://medium.com/@aisquarecommunity/prompt-governance-scale-versioning-access-and-audits-c76b58a166f1))

```
[후보(Candidate)] → [검토 중(Under Review)] → [배포(Deployed)] → [폐기(Deprecated)]
     ↑                                              ↓
     └──────────── 롤백(Rollback) ──────────────────┘
```

| 상태 | 설명 | 실행 가능 여부 |
|---|---|---|
| **후보(Candidate)** | 작성 완료, 평가 대기 중 | 테스트 환경만 |
| **검토 중(Under Review)** | 승인자 검토 진행 중 | 테스트 환경만 |
| **배포(Deployed)** | 승인 완료, 운영 환경 사용 중 | 운영 환경 전체 |
| **폐기(Deprecated)** | 더 이상 사용하지 않음. 이력 보존 | 사용 불가 (기록만) |

### 3-4. Registry 메타데이터 필드

([출처: MLflow Prompt Registry](https://mlflow.org/prompt-registry), [출처: PromptLayer](https://docs.promptlayer.com/features/prompt-registry/overview), [출처: LaunchDarkly](https://launchdarkly.com/blog/prompt-versioning-and-management/))

Registry에 저장하는 Prompt 레코드의 필수 필드:

| 필드 | 내용 | 예시 |
|---|---|---|
| `prompt_id` | 고유 식별자 | `claim-classification-doosanelec-v2` |
| `version` | 시맨틱 버전 | `2.1.0` |
| `status` | 현재 상태 | `Deployed` |
| `business_task` | 어떤 업무에 쓰이나 | "두산전자 CCL C/S Report 원인 분류" |
| `author` | 작성자 | AI팀 홍길동 |
| `approved_by` | 승인자 | 품질기술팀 책임 이름 |
| `created_at` | 최초 등록일 | 2026-03-15 |
| `deployed_at` | 배포일 | 2026-03-22 |
| `change_reason` | 이번 버전 변경 사유 | "Delamination 소재/공정 구분 기준 추가" |
| `dependencies` | 의존 자산 목록 | 데이터셋 ID, Glossary 버전, Tool ID, 평가셋 ID |
| `eval_result` | 평가 결과 요약 | "정확도 89%, E-3 평가셋 v1.2 기준 통과" |
| `model_config` | 모델·파라미터 고정값 | `model: claude-opus, temperature: 0.1` |
| `rollback_target` | 문제 시 돌아갈 버전 | `v2.0.1` |

> 모델·파라미터도 Prompt와 함께 버저닝한다. 동일 Prompt라도 모델이 바뀌면 출력이 달라질 수 있으므로 한 세트로 관리([출처: MLflow Prompt Registry](https://mlflow.org/prompt-registry)).

### 3-5. 승인-배포 흐름 (Approval Gate)

([출처: Braintrust](https://www.braintrust.dev/articles/what-is-prompt-versioning), [출처: LaunchDarkly](https://launchdarkly.com/blog/prompt-versioning-and-management/))

```
개발(Dev) 환경     →    스테이징(Staging)    →    운영(Production)
  자유 실험              최종 검증 완료              배포된 버전만
  (Candidate)        (품질 기준 통과 확인)         (Deployed 상태)
                          ↓ 승인자 승인
                       배포 승인 기록
```

업무 영향도가 큰 Prompt(분류·판정 관련)는 반드시 현업 SME 승인을 거쳐 운영 환경에 배포한다.

---

## 4. How C — 의존성 관리 (Prompt Dependency)

### 4-1. 왜 의존성 관리가 필요한가

([출처: LaunchDarkly](https://launchdarkly.com/blog/prompt-versioning-and-management/), [출처: Maxim AI](https://www.getmaxim.ai/articles/prompt-versioning-and-its-best-practices-2025/))

Prompt는 단독으로 동작하지 않는다. 특정 Glossary 용어, 데이터 자산, Tool(D-2), 평가셋(E-3)에 의존한다. 의존 대상이 바뀌면 Prompt 출력도 달라질 수 있으므로, "어떤 Prompt가 어떤 자산에 의존하는지" 명시적으로 기록해야 변경 영향도를 파악할 수 있다.

> LaunchDarkly 가이드는 "의존성은 버저닝 없이는 눈에 보이지 않다가 문제가 생겼을 때야 드러난다"고 경고한다.

### 4-2. 의존성 맵 (Dependency Map) 구조

```
claim-classification Prompt v2.1.0
  ├── 데이터 자산: cs_report_corpus (카탈로그 ID: DA-042)
  ├── Glossary: defect_taxonomy v3.2 (A-3 소관)
  ├── Tool: SAP_CS_Retrieval_Tool v1.1 (D-2 소관)
  └── 평가셋: claim_eval_gold_v1.2 (E-3 소관)
```

### 4-3. 의존성 기록 필드 (Registry 내 `dependencies` 섹션)

| 의존 대상 유형 | 식별자 | 버전 | 영향도 |
|---|---|---|---|
| 데이터 자산 | `cs_report_corpus` | DA-042 v5 | Prompt 입력 직접 연결 |
| Glossary 용어 | `defect_taxonomy` | A-3 v3.2 | 분류 라벨 기준 제공 |
| Tool | `SAP_CS_Retrieval_Tool` | D-2 v1.1 | 데이터 조회 경로 |
| 평가셋 | `claim_eval_gold` | E-3 v1.2 | 성능 판정 기준 |

### 4-4. 변경 영향도 분석 — 연쇄 점검 원칙

([출처: Maxim AI — Dependency Tracing](https://www.getmaxim.ai/articles/prompt-versioning-and-its-best-practices-2025/))

의존 자산이 변경되면 그 자산을 참조하는 모든 Prompt를 점검해야 한다.

| 변경 이벤트 | 영향 받는 Prompt 점검 필요 여부 |
|---|---|
| Glossary 결함 유형 용어 변경 (A-3) | 그 용어를 참조하는 모든 Prompt → 판단 기준 재검토 |
| Tool 입력 스키마 변경 (D-2) | 그 Tool을 호출하는 Prompt → 입력 파라미터 확인 |
| 데이터 스키마 변경 (A-2) | 그 필드를 변수로 받는 Prompt → 변수명 점검 |
| 평가셋 기준 갱신 (E-3) | 기존 통과 기록이 유효한지 재평가 필요 여부 판단 |

> 실무 원칙: 의존 자산 변경 시 "영향 받는 Prompt 목록" 자동 조회가 가능하도록 Registry에 역방향 참조(Back-reference)를 기록한다.

---

## 5. How D — 성능 저하 감지·개선

### 5-1. 성능 저하 감지 신호 4가지

([출처: Myengineeringpath.dev — Prompt Testing & CI/CD 2026](https://myengineeringpath.dev/genai-engineer/prompt-testing/), [출처: Braintrust AI Evaluation Tools 2026](https://www.braintrust.dev/articles/best-ai-evaluation-tools-2026))

| 신호 | 설명 | 측정 방법 |
|---|---|---|
| **평가셋 점수 변화** | E-3 기준 정확도·근거성이 기준 이하로 하락 | 정기 회귀 테스트 (50~200건 평가셋) |
| **사용자 수정률 상승** | 현업이 AI 출력을 직접 고치는 비율 증가 | Feedback Loop(E-4) 로그 |
| **실패 사례 누적** | 잘못된 분류, 근거 누락, 금지 행동 위반 | 운영 로그 분석 |
| **업무 정책 변경** | 판단 기준·분류 체계(Glossary)가 바뀜 | 변경 사유 문서 확인 |

### 5-2. 개선 프로세스 (회귀 테스트 포함)

([출처: Braintrust — Prompt Versioning Best Practices](https://www.braintrust.dev/articles/what-is-prompt-versioning), [출처: Aiuniverse.xyz — Top Prompt Testing Tools](https://www.aiuniverse.xyz/top-10-prompt-testing-regression-suites-features-pros-cons-comparison/))

```
성능 저하 신호 감지
      ↓
원인 분석
  - 데이터 문제? → A-1/A-2 정비 (Lineage·Observability 참조)
  - Glossary 변경? → A-3 확인 후 Prompt 기준 업데이트
  - 모델 드리프트? → 평가셋 재실행으로 확인
  - 판단 기준 변경? → 현업 SME와 재정의 후 Prompt 수정
      ↓
Prompt 수정 (새 버전 생성, 기존 버전 불변 유지)
      ↓
회귀 테스트 (E-3 평가셋 기준, 이전 버전과 점수 비교)
  - "기존에 맞던 문제가 다시 틀리지 않는지" 반드시 확인
      ↓
기준 통과 시 → 승인 → 새 버전 배포
기준 미달 시 → 추가 개선 반복
```

핵심 원칙: 회귀 테스트(Regression Test)는 "새 버전이 더 좋아진 것"만 확인하는 게 아니라 "기존에 잘 되던 것이 깨지지 않았는지"를 반드시 함께 확인한다([출처: Braintrust](https://www.braintrust.dev/articles/what-is-prompt-versioning)).

### 5-3. 자동 vs 수동 개선 기준

| 개선 유형 | 처리 방법 |
|---|---|
| 표현 개선 (Patch) | AI 팀 단독 수정 → 평가 통과 후 배포 |
| 판단 기준 추가·변경 (Minor) | 현업 SME 검토 → 승인 후 배포 |
| 분류 체계 전면 개편 (Major) | 현업 SME + 데이터 조직 + 승인자 3자 검토 |
| 업무 정책 변경 반영 | 반드시 현업 SME 주도로 내용 확정 후 AI 팀이 구조화 |

---

## 6. How E — Before→After 작성 규칙 (현업 실행 키트 재료)

가이드 작성 에이전트는 이 교정 쌍을 "나쁜 Prompt 자산 vs 좋은 Prompt 자산" 예시로 쓸 것.

### 교정 쌍 1 — 구조화 여부

**나쁜 예 (구조화 안 됨):**
```
이 C/S Report를 보고 원인을 분류해줘.
```
문제: 입력 형식 없음, 판단 기준 없음, 출력 형식 없음, 금지 행동 없음. 사람마다 다른 결과.

**좋은 예 (4구획 구조화):**
```
[역할] 두산전자 CCL 품질 클레임 원인 분류 전문가
[입력] C/S Report: {{cs_report}}, 결함 분류 기준: {{defect_taxonomy}}
[판단 기준] Delamination은 소재/공정으로 분류. 판단 불가 시 needs_review=true.
[금지] Glossary 외 임의 용어 사용 금지, 근거 없는 단정 금지
[출력] {"primary_cause": ..., "confidence": ..., "evidence": ..., "needs_review": ...}
```
개선 이유: 재현 가능, 평가 가능, 다른 담당자도 동일하게 실행 가능.

---

### 교정 쌍 2 — 버전·의존성·평가 기록 여부

**나쁜 예 (비관리 상태):**
```
파일명: prompt_최신.txt
내용: 그냥 텍스트 파일로 저장. 언제 만들었는지, 누가 승인했는지, 어떤 데이터에 쓰는지 기록 없음.
```
문제: 어느 업무에 쓰이는지 모름, 수정 이력 없음, 롤백 불가, 의존 데이터 변경 시 영향 인지 불가.

**좋은 예 (Registry 등록):**
```
prompt_id: claim-classification-doosanelec
version: 2.1.0
status: Deployed
business_task: 두산전자 CCL C/S Report 원인 분류
approved_by: 품질기술팀 책임자
change_reason: Delamination 소재/공정 구분 기준 v3.2 Glossary 반영
dependencies: [defect_taxonomy@A3-v3.2, SAP_CS_Tool@D2-v1.1, claim_eval@E3-v1.2]
eval_result: 정확도 89%, v1.2 평가셋 기준 통과
rollback_target: 2.0.1
```
개선 이유: 언제든 추적 가능, 의존 자산 변경 시 영향도 즉시 파악, 감사 대응 가능.

---

### 교정 쌍 3 — 성능 저하 감지 및 개선 이력

**나쁜 예:**
```
현업 담당자가 "요즘 분류가 이상한 것 같다"고 구두 보고. 원인 불명. 조치 이력 없음.
```
문제: 언제부터 이상해졌는지 모름, 어느 버전에서 문제인지 모름, 재발 방지 불가.

**좋은 예:**
```
[2026-05-10] E-3 회귀 테스트 결과: 정확도 89% → 76%로 하락 감지
원인 분석: Glossary v3.2에서 'CCL 층간 박리' 용어 변경이 Prompt 판단 기준과 불일치
조치: Prompt v2.1.0 → v2.2.0 (기준 업데이트), SME 승인 후 배포
검증: 회귀 테스트 통과 (정확도 91% 회복), 이전 통과 케이스 재검증 완료
```
개선 이유: 성능 저하를 숫자로 감지, 원인을 자산 변경으로 추적, 개선 이력 문서화로 재발 방지 가능.

---

## 7. How F — 역할 (RACI)

([출처: Segev Shmueli Medium](https://medium.com/@segev_shmueli/managing-prompts-as-enterprise-assets-a-portfolio-approach-e9552e24f327), [출처: AISquare Medium](https://medium.com/@aisquarecommunity/prompt-governance-scale-versioning-access-and-audits-c76b58a166f1), [출처: POG Whitepaper](https://enjtorian.github.io/prompt-orchestration-governance-whitepaper/))

| 역할 | 담당자 | 책임 내용 |
|---|---|---|
| **현업 SME** (업무 전문가) | 품질팀·생산팀 담당자 | 업무 절차·판단 기준 제공, Prompt 내용 검토·승인 |
| **AI 조직** (Prompt Engineer) | AI/디지털 팀 | Prompt 구조화, Harness 패키징, 버전 관리 |
| **데이터 조직** (Data Steward) | 데이터 거버넌스 팀 | Registry 운영, 의존성 관리, Glossary·카탈로그 연계 |
| **승인자** (Approver) | 현업 책임자 또는 AI 거버넌스 위원회 | 운영 환경 배포 최종 승인, 폐기 결정 |

**RACI 요약 매트릭스:**

| 활동 | 현업 SME | AI 조직 | 데이터 조직 | 승인자 |
|---|---|---|---|---|
| 자산화 대상 선정 | A | R | C | I |
| Prompt 구조화 작성 | C | R | I | I |
| 의존성 맵 작성 | I | R | A | I |
| 평가(E-3 기반) | C | R | I | I |
| Registry 등록 | I | R | A | I |
| 운영 배포 승인 | C | I | I | A |
| 성능 저하 대응 | A | R | C | I |
| Glossary 변경 후 점검 | C | R | A | I |

R=실행 A=책임 C=자문 I=통보

---

## 8. Harness 패키징 — 재사용 단위 정의

### 8-1. Harness란

([출처: Anthropic — Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents), [출처: Medium — AI Agentic System Harnesses for Enterprise-Grade Workflows](https://medium.com/@oracle_43885/ai-agentic-system-harnesses-for-enterprise-grade-autonomous-workflows-a3b2853b5c2a))

Harness(하네스)는 특정 업무를 AI가 반복 실행할 수 있도록 필요한 모든 요소를 하나의 단위로 묶은 패키지다.

Anthropic 가이드는 "Harness는 LLM이 제안하는 행동을 검증·승인·실행·기록하는 결정론적(Deterministic) 실행 래퍼(Runtime Layer)"라고 정의한다.

### 8-2. Harness 구성 4요소

```
Harness = [Prompt 자산] + [입력 데이터 연결] + [Tool 호출 순서] + [출력 형식·검증 기준]
```

| 구성 요소 | 내용 | 예시 |
|---|---|---|
| **Prompt 자산** | Registry에 등록된 버전 고정 Prompt | `claim-classification@v2.1.0` |
| **입력 데이터 연결** | 어떤 데이터 자산을 어떤 형식으로 주입하나 | C/S Report 텍스트 + defect_taxonomy |
| **Tool 호출 순서** | 어떤 Tool을 어떤 순서로 호출하나 (D-2) | SAP_CS_Retrieval → 분류 Prompt → 결과 저장 |
| **출력 형식·검증 기준** | 출력이 맞는 형식인지 자동 검증, 기준 미달 시 처리 방법 | JSON 스키마 검증, confidence=low 시 needs_review=true |

### 8-3. Harness 재사용성 확보 원칙

([출처: Harness Developer Hub — Worker Agents](https://developer.harness.io/docs/platform/harness-ai/harness-agents/), [출처: Medium — Production-Ready Harness Engineering 2026](https://medium.com/@tort_mario/ai-agent-best-practices-production-ready-harness-engineering-2026-guide-c1236d713fac))

1. **입력을 변수(Parameter)로 분리**: 특정 데이터셋에 고정하지 않고 `{{변수}}` 형식으로 주입점을 파라미터화
2. **Prompt와 Harness를 분리 버저닝**: Prompt가 바뀌어도 Harness 구조는 유지, Harness 구조가 바뀌어도 Prompt는 유지
3. **Tool 호출 스키마는 D-2 Registry 참조**: Harness 내에 Tool 명세를 직접 내장하지 않고 D-2 Registry에서 참조
4. **평가셋 연결 명시**: 이 Harness를 검증할 E-3 평가셋 ID를 Harness 명세에 기재

### 8-4. Harness 명세서 필수 항목

| 필드 | 예시 |
|---|---|
| `harness_id` | `claim-analysis-harness-doosanelec` |
| `version` | `1.2.0` |
| `prompt_asset` | `claim-classification@v2.1.0` |
| `input_schema` | `{cs_report_text: string, process_data: json}` |
| `tool_sequence` | `[SAP_CS_Retrieval@v1.1, Result_Save@v1.0]` |
| `output_schema` | `{primary_cause: string, confidence: enum, needs_review: bool}` |
| `eval_set` | `claim_eval_gold@E3-v1.2` |
| `owner` | 품질기술팀·AI팀 공동 |

---

## 9. 제조 맥락 End-to-End 사례 — 두산전자 품질 클레임 원인 분류

### 9-1. 배경

두산전자는 CCL(동박적층판) 제품에서 Delamination(층간 분리) 클레임이 반복 발생한다. 현업 전문가가 C/S Report를 보고 "소재 결함"인지 "공정 결함"인지 수작업으로 분류하고 있었으나, 담당자마다 기준이 달라 일관성 문제가 있었고, 동일 업무를 여러 담당자가 반복했다.

### 9-2. 자산화 절차 적용

**When (자산화 판단):**
- 반복성 O (월 30~50건 C/S Report 처리)
- 업무 영향도 O (클레임 원인 오분류 시 고객 대응 오류)
- 재사용성 O (두산에너빌리티 용접 결함 분류에도 유사 구조 적용 가능)
- 노하우 O ("소재/공정 구분 기준"이 20년 경험의 암묵지)
→ **자산화 대상 확정**

**② 업무 절차 → Prompt 변환:**
현업 SME 인터뷰로 판단 기준 추출:
- Delamination은 수지 함침 불량(소재) vs 적층 압력 불균일(공정) 구분
- 분리 면적·위치·패턴으로 1차 판단, 공정 로그 대조로 확정
- 판단 불가 시 반드시 현업 검토 플래그
→ 4구획 Prompt 초안 작성 (`claim-classification v1.0.0-candidate`)

**③ 의존성 연결:**
```
dependencies:
  - defect_taxonomy @A3 v3.2  (CCL 표준 결함 용어)
  - cs_report_corpus @DA-042  (과거 C/S Report 원문 DB)
  - SAP_CS_Retrieval_Tool @D2-v1.1 (SAP에서 Report 조회)
  - claim_eval_gold @E3-v1.2 (50건 정답 라벨셋)
```

**④ 테스트·평가:**
E-3 평가셋 50건 기준:
- v1.0.0: 정확도 73% — 기준 미달 (목표 85%)
- SME와 판단 기준 보완 → v1.1.0
- v1.1.0: 정확도 88% — 통과
→ `Candidate → Under Review` 전환

**⑤ Harness 패키징:**
```
harness: claim-analysis-harness v1.0.0
  prompt: claim-classification @v1.1.0
  input: {cs_report_text, defect_taxonomy}
  tools: [SAP_CS_Retrieval, Result_Save]
  output: {primary_cause, confidence, evidence, needs_review}
  eval_set: claim_eval_gold @E3-v1.2
```

**⑥ Registry 등록·배포:**
- 품질기술팀 책임자 검토 → 승인 → `Deployed` 상태 전환
- Registry에 전체 메타데이터 기록

### 9-3. 운영 후 개선 사례

6개월 운영 후:
- Glossary v3.2 → v3.3 업데이트: `CCL층간박리` → `CCL층간분리(Delamination)` 표준 용어 변경
- 변경 영향도 분석: `claim-classification` Prompt가 Glossary 참조 → 점검 필요 통보
- E-3 회귀 테스트: 정확도 88% → 79% 하락 확인
- SME와 판단 기준 재정의 → v1.2.0 작성·승인·배포
- 회귀 테스트 재통과 (정확도 91%)

---

## 10. Prompt Registry 도구 참고

가이드에 솔루션을 직접 소개할 때 참고할 도구 목록 (솔루션 독립 섹션 또는 How에 흡수 결정은 가이드 작성 에이전트 판단).

| 도구 | 특징 | 공식 URL |
|---|---|---|
| **MLflow Prompt Registry** | 오픈소스, 모델+Prompt 통합 버저닝, 평가 연동 | https://mlflow.org/prompt-registry |
| **PromptLayer** | SaaS, Registry + 로깅 + A/B 테스트 통합 | https://docs.promptlayer.com/features/prompt-registry/overview |
| **Braintrust** | 평가 중심 Prompt 관리, 회귀 테스트 강점 | https://www.braintrust.dev/articles/what-is-prompt-versioning |
| **Maxim AI** | Prompt 버저닝·평가·모니터링 통합 플랫폼 | https://www.getmaxim.ai/articles/prompt-versioning-and-its-best-practices-2025/ |
| **LangSmith (LangChain)** | Prompt 추적·평가·협업, LangChain 생태계와 연동 | https://www.langchain.com/langsmith |
| **SAP Generative AI Hub** | SAP 환경에서 Prompt Registry 관리 | https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/managing-prompts-with-the-prompt-registry-and-templates |

> 두산 계열사 맥락: SAP ERP 환경을 쓰는 계열사라면 SAP Generative AI Hub의 Prompt Registry와 기존 SAP 연동을 함께 검토할 수 있다.

---

## 11. 출처 목록

1. [Mastering Prompt Versioning: Best Practices for Scalable LLM Development — DEV Community](https://dev.to/kuldeep_paul/mastering-prompt-versioning-best-practices-for-scalable-llm-development-2mgm)
2. [Top 5 Prompt Versioning Tools in 2025 — Maxim AI](https://www.getmaxim.ai/articles/top-5-prompt-versioning-tools-in-2025-essential-infrastructure-for-production-ai-systems/)
3. [What is Prompt Versioning? Best Practices — Braintrust](https://www.braintrust.dev/articles/what-is-prompt-versioning)
4. [Prompt Versioning and Its Best Practices 2025 — Maxim AI](https://www.getmaxim.ai/articles/prompt-versioning-and-its-best-practices-2025/)
5. [Prompt Versioning & Management Guide — LaunchDarkly](https://launchdarkly.com/blog/prompt-versioning-and-management/)
6. [Managing Prompts as Enterprise Assets: A Portfolio Approach — Segev Shmueli, Medium](https://medium.com/@segev_shmueli/managing-prompts-as-enterprise-assets-a-portfolio-approach-e9552e24f327)
7. [Prompt Governance: Enabling Reusability and Standards — Bojan Ciric, Medium](https://medium.com/the-future-of-data/prompt-governance-enabling-reusability-and-standards-in-ai-driven-organizations-1d4dfe0a83ea)
8. [Prompt Orchestration Governance (POG) Whitepaper](https://enjtorian.github.io/prompt-orchestration-governance-whitepaper/)
9. [POG-01 What is Prompt Orchestration Governance — DEV Community](https://dev.to/enjtorian/pog-01-what-is-prompt-orchestration-governance-pog-15gp)
10. [Prompt Governance Scale: Versioning, Access, and Audits — AISquare, Medium](https://medium.com/@aisquarecommunity/prompt-governance-scale-versioning-access-and-audits-c76b58a166f1)
11. [Prompt Governance Is the New Data Governance — CIO](https://www.cio.com/article/4130960/prompt-governance-is-the-new-data-governance.html)
12. [MLflow Prompt Registry — Official Documentation](https://mlflow.org/prompt-registry)
13. [MLflow Prompt Registry Docs](https://mlflow.org/docs/latest/genai/prompt-registry/)
14. [PromptLayer — Prompt Registry Overview](https://docs.promptlayer.com/features/prompt-registry/overview)
15. [Effective Harnesses for Long-Running Agents — Anthropic Engineering](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
16. [AI Agentic System Harnesses for Enterprise-Grade Autonomous Workflows — Valdez Ladd, Medium](https://medium.com/@oracle_43885/ai-agentic-system-harnesses-for-enterprise-grade-autonomous-workflows-a3b2853b5c2a)
17. [AI Agent Best Practices: Production-Ready Harness Engineering 2026 — Tort Mario, Medium](https://medium.com/@tort_mario/ai-agent-best-practices-production-ready-harness-engineering-2026-guide-c1236d713fac)
18. [Harness Worker Agents — Harness Developer Hub](https://developer.harness.io/docs/platform/harness-ai/harness-agents/)
19. [Top 10 Prompt Testing & Regression Suites — AIUniverse](https://www.aiuniverse.xyz/top-10-prompt-testing-regression-suites-features-pros-cons-comparison/)
20. [Prompt Testing & Optimization — Evals, A/B Testing & CI/CD 2026 — MyEngineeringPath](https://myengineeringpath.dev/genai-engineer/prompt-testing/)
21. [5 Best AI Evaluation Tools for Production 2026 — Braintrust](https://www.braintrust.dev/articles/best-ai-evaluation-tools-2026)
22. [LLMOps — What is LLMOps — Databricks Glossary](https://www.databricks.com/glossary/llmops)
23. [Managing Dependencies Between Tool Calls — apxml.com](https://apxml.com/courses/building-advanced-llm-agent-tools/chapter-3-llm-tool-selection-orchestration/tool-dependency-management)
24. [LLMOps vs DevOps: Artifact Management for LLMs — Cloudsmith](https://cloudsmith.com/blog/llmops-vs-devops-what-llmops-means-for-artifact-management)
25. [Harnessing the Power of LLMs: Prompt Engineering for Quality Engineers — Quality Magazine](https://www.qualitymag.com/articles/99113-harnessing-the-power-of-llms-prompt-engineering-for-quality-engineers)
26. [SAP Generative AI Hub: Managing Prompts with Prompt Registry](https://learning.sap.com/courses/solve-your-business-problems-using-prompts-and-llms-in-sap-generative-ai-hub/managing-prompts-with-the-prompt-registry-and-templates)
