# D-3 Prompt/Harness 자산화 — What 클러스터 리서치 원자료

> **목적:** 가이드 작성 에이전트가 쓸 리서치 원자료. 사실·구조·출처 위주.
> **관점 고정:** "Prompt·Harness를 조직의 재사용 가능한 데이터 자산으로 구조화·등록·버전관리·재사용하는 법"
> **작성일:** 2026-06-24

---

## 목차
1. [Prompt / Harness 자산화 정의 및 체계 내 위치](#1-정의)
2. [자산 목록 — 무엇을 자산으로 관리하나](#2-자산-목록)
3. [업무→Prompt 변환 틀 (구조화 프레임)](#3-변환-틀)
4. [Harness 패키지 구조](#4-harness-구조)
5. [현업 실행 키트 재료 — Prompt 자산 항목 사전](#5-항목-사전)
6. [제조 맥락 예시 후보](#6-제조-예시)
7. [출처 목록](#7-출처-목록)

---

## 1. 정의 및 체계 내 위치 {#1-정의}

### 1-1. Prompt 자산화란

**Prompt 관리(Prompt Management)**는 프롬프트를 "정적 텍스트가 아니라 운영 자산(production asset)"으로 다루는 실천이다. 버전 관리·테스트·배포·모니터링 프로세스를 체계화해 안전하게 변경하고, 변경 이력을 명확히 추적하며, 필요 시 롤백할 수 있도록 한다.
- 출처: Braintrust — "What is prompt management?" (https://www.braintrust.dev/articles/what-is-prompt-management)

핵심 전환: 프롬프트를 애플리케이션 코드에서 분리해 중앙 레지스트리(registry)에서 관리 → 애플리케이션 재배포 없이 프롬프트만 업데이트 가능, 여러 모델·에이전트·워크플로에서 재사용 가능.

**조직 자산화의 의미:** "좋은 프롬프트는 회사의 지적재산(IP)이다"(nextagile.ai). 엔터프라이즈 스케일에서는 프롬프트 엔지니어링이 '컨텍스트 엔지니어링(context engineering)'으로 진화 — 메타데이터가 풍부한 컨텍스트를 AI에게 자동으로 조립하는 인프라.

### 1-2. Harness 자산화란

**AI 에이전트 Harness(Agent Harness)**는 LLM을 감싸 태스크를 실행하게 하는 소프트웨어 인프라다. 모델이 "응답만 하는 것"이 아니라 "행동(act)"하도록 도구·시스템·메모리·실행 환경을 연결한다.
- 출처: Databricks Blog — "What is an AI agent harness?" (https://www.databricks.com/blog/ai-harness)

**Harness의 구성 단위(패키지):** 시스템 프롬프트 + 도구 스키마 + 메모리/컨텍스트 + 대화 이력 + 입력 데이터 + 출력 형식 + (평가 기준)을 하나로 묶어 반복 실행 가능하게 만든 단위. Harness 인프라 변경만으로 에이전트 벤치마크 순위가 20위 이상 변동된 사례 존재 — 즉 Harness 자체가 핵심 변수.
- 출처: The Anatomy of an Agent Harness (https://blog.dailydoseofds.com/p/the-anatomy-of-an-agent-harness)

**Prompt vs. Harness 관계:**
| 구분 | Prompt | Harness |
|------|--------|---------|
| 역할 | 모델에게 전달하는 지시·맥락 텍스트 | 프롬프트 + 도구 + 데이터 + 실행 로직을 묶은 실행 단위 |
| 단독 존재 | 가능 (단순 지시문) | 반드시 Prompt 포함 |
| 재사용 단위 | 텍스트 템플릿 | 실행 패키지 전체 |
| 관리 대상 | 텍스트 + 메타데이터 | 컴포넌트 집합 + 의존성 |

### 1-3. D-3 체계 내 위치

- **A-1 데이터 카탈로그** — Prompt 자산도 데이터 자산의 일종으로 카탈로그에 등록
- **A-3 비즈니스 Glossary** — 프롬프트 내 용어 정의의 출처
- **D-1 Physical 데이터** — 프롬프트가 참조하는 입력 데이터 스키마 정의
- **D-2 API/Tool 연계 데이터** — Harness가 호출하는 Tool 명세 정의
- **C-3 데이터 Lineage** — 어떤 프롬프트 버전이 어떤 AI 출력을 만들었는지 계보 추적

---

## 2. 자산 목록 — 무엇을 자산으로 관리하나 {#2-자산-목록}

엔터프라이즈 환경에서 관리하는 Prompt/Harness 자산 유형:

### 2-1. 시스템 지시문 (System Prompt)
- **정의:** 대화 전체에 걸쳐 모델의 역할·목표·행동 규칙을 일관되게 정의하는 상시 지시문. 보통 대화의 최상단에 위치.
- **왜 자산인가:** 여러 대화·응용에서 동일하게 재사용되며, 변경 시 모든 관련 결과에 영향을 줌.
- **예시:** "당신은 두산전자 PCB 소재 품질 전문가입니다. 답변은 한국어로 하고 기술 용어는 영문 병기하십시오."
- 출처: Databricks Blog (https://www.databricks.com/blog/ai-harness)

### 2-2. 업무 지시 프롬프트 (Task Prompt / Instruction Prompt)
- **정의:** 특정 업무 태스크를 수행하도록 모델에게 주는 지시 텍스트 (입력 변수 포함 템플릿).
- **왜 자산인가:** 동일 업무를 반복 처리할 때 일관된 품질 보장. 검증된 버전을 공유.
- **구조:** 역할(Role) + 태스크(Task) + 맥락(Context) + 출력 형식(Format)
- 출처: RTF 프레임워크, RACE 프레임워크 등 다수 — Parloa (https://www.parloa.com/knowledge-hub/prompt-engineering-frameworks/)

### 2-3. 역할 정의 / 페르소나 (Role / Persona)
- **정의:** AI가 어떤 전문가·역할로 행동해야 하는지 정의하는 텍스트 블록.
- **왜 자산인가:** 동일 역할 정의를 여러 업무 프롬프트에서 재사용. 일관된 전문성 수준 유지.
- **예시:** "당신은 10년 경력의 PCB 라미네이션 공정 엔지니어입니다..."

### 2-4. 판단 기준 / 가이드라인 (Reasoning Guide / Decision Criteria)
- **정의:** AI가 추론 시 따라야 할 단계별 판단 기준·체크리스트. Chain-of-Thought(CoT) 지시 포함.
- **왜 자산인가:** 사람의 업무 판단 로직을 코드화. 변경 시 전체 판단 일관성 영향.
- **예시:** 클레임 원인 분석 순서 (1. 외관 이상 확인 → 2. 공정 파라미터 검토 → 3. 소재 이력 조회...)

### 2-5. 출력 형식 명세 (Output Schema / Format)
- **정의:** AI 출력의 구조를 정의하는 스키마 (JSON, 표, 정형 텍스트 등).
- **왜 자산인가:** 출력이 후속 시스템(DB, ERP, 보고서)에서 자동 처리되려면 형식 일관성이 필수.
- **예시:** `{"defect_type": "", "cause": "", "action": "", "confidence": 0.0}`
- 참고: "Return JSON exactly matching this schema: {example} 형태가 파싱 실패율을 2% 이하로 낮춘다" — Futureagi (https://futureagi.com/blog/dynamic-prompts/)

### 2-6. Few-shot 예시 (Few-shot Examples)
- **정의:** AI에게 원하는 입력→출력 패턴을 보여주는 2~10개의 예시 쌍.
- **왜 자산인가:** 검증된 예시 집합은 재사용 가능한 학습 자원. 업무별로 유지·갱신 필요.
- 출처: IBM — "What is few shot prompting?" (https://www.ibm.com/think/topics/few-shot-prompting)

### 2-7. Tool 호출 순서 / 워크플로 정의 (Tool Use Sequence)
- **정의:** Harness 내에서 어떤 도구를 어떤 순서로 호출하는지 정의한 로직.
- **왜 자산인가:** 검증된 Tool 호출 순서는 에이전트 워크플로의 핵심 IP.
- 출처: Parallel.ai (https://parallel.ai/articles/what-is-an-agent-harness)

### 2-8. 금지 행동 / 안전 제약 (Guardrails / Constraints)
- **정의:** AI가 해서는 안 되는 행동·출력을 명시한 규칙. 입력 검증·출력 검증 포함.
- **왜 자산인가:** 조직 리스크 관리 기준의 코드화. 규정 변경 시 일괄 업데이트 필요.
- 출처: Redteamer.tips (https://redteamer.tips/taming-the-beast-prompt-engineering-and-agent-guardrails)

---

## 3. 업무→Prompt 변환 틀 {#3-변환-틀}

### 3-1. 공통 구성 요소 5가지

실무에서 가장 널리 쓰이는 구조화 요소 (여러 프레임워크의 공통분모):

| 구성 요소 | 영문 명칭 | 역할 | 예시 (품질 클레임 분석) |
|-----------|-----------|------|-------------------------|
| 역할 | Role / Persona | "이 업무를 수행하는 전문가가 누구인지" 정의 | "당신은 두산전자 PCB 품질 분석 엔지니어입니다" |
| 태스크 | Task / Instruction | 수행해야 할 업무를 명확히 지시 | "다음 클레임 보고서를 읽고 원인 코드를 분류하라" |
| 맥락·참조 | Context / Reference | 판단에 필요한 배경·기준 데이터 주입 | CCL 규격서, Delamination 기준표, 유사 사례 이력 |
| 추론 단계 | Reasoning Steps / CoT | 단계별 판단 순서 지시 | "1. 외관 이상 종류 확인 → 2. 발생 공정 특정 → 3. 원인 코드 분류" |
| 출력 형식 | Output Format / Schema | 결과물의 구조 명시 | JSON / 표 / 정해진 양식 |
| 금지 행동 | Guardrails / Constraints | 하면 안 되는 것 명시 | "규격서 외 추측으로 원인 코드를 만들지 말 것" |

### 3-2. 주요 프레임워크 정리 (출처 포함)

**RTF (Role–Task–Format)**
- 가장 간결한 3요소 구조. 명확한 역할, 구체적 태스크, 원하는 출력 형식.
- 출처: Parloa Prompt Engineering Frameworks (https://www.parloa.com/knowledge-hub/prompt-engineering-frameworks/)

**RASCEF (Role–Actions–Steps–Context–Examples–Format)**
- 복잡한 업무 지시에 적합. 실행 단계·맥락·예시를 포함한 포괄 구조.
- 출처: God of Prompt (https://godofprompt.ai/blog/7-ai-prompt-structures-that-generate-perfect-content-every-time/)

**CARE (Context–Ask–Rules–Examples)**
- 규칙(Rules) 요소가 명시적으로 포함 — 제약·가이드라인 중심 업무에 적합.
- 출처: ENEB Prompt Frameworks (https://eneb.com/prompt-frameworks-to-maximize-chatgpt-results/)

**REASONS Canvas (SPDD 방법론)**
- 업무 절차를 구조화된 프롬프트로 변환하는 체계적 방법론 (Martin Fowler 게재).
- 7개 요소: Requirements(요구사항) / Entities(도메인 모델) / Approach(접근 전략) / Structure(시스템 구조) / Operations(실행 단계) / Norms(표준) / Safeguards(안전 제약)
- 핵심 원칙: "의도(intent)를 먼저 명확히 쓰고, 그 다음 모델이 구현하게 한다."
- 출처: Martin Fowler — Structured Prompt-Driven Development (https://martinfowler.com/articles/structured-prompt-driven/)

### 3-3. 업무 절차→Prompt 변환 6단계 (SPDD 기반)

1. **요구사항 정형화** — 업무를 "누가 / 무엇을 / 어떤 조건에서 / 결과는" 형태의 사용자 스토리로 작성
2. **범위 확정** — 포함할 것·제외할 것·완료 기준을 숫자·예시로 명시
3. **도메인 분석** — 업무에서 쓰는 용어(Glossary), 기존 규칙, 기술 리스크 파악
4. **캔버스 생성** — REASONS Canvas 또는 RTF/RASCEF로 구조화
5. **출력 검증** — 예상 입력으로 실행, 출력 형식·내용 검증
6. **동기화·버전 저장** — 검증된 프롬프트를 레지스트리에 등록 (버전·변경사유 기록)

출처: Martin Fowler SPDD (https://martinfowler.com/articles/structured-prompt-driven/)

---

## 4. Harness 패키지 구조 {#4-harness-구조}

### 4-1. Harness 11개 핵심 컴포넌트

출처: The Anatomy of an Agent Harness (https://blog.dailydoseofds.com/p/the-anatomy-of-an-agent-harness)

| # | 컴포넌트 | 역할 |
|---|----------|------|
| 1 | 오케스트레이션 루프 | Thought-Action-Observation 사이클 실행 엔진 |
| 2 | 도구(Tools) | API·코드 실행·DB 등 외부 능력 (이름·설명·파라미터 스키마 정의) |
| 3 | 메모리(Memory) | 단기(대화 이력) + 장기(파일, 프로젝트 컨텍스트) |
| 4 | 컨텍스트 관리 | 토큰 예산 내 맥락 조립·압축·검색 |
| 5 | **프롬프트 조립** | 시스템 지시문 + 도구 정의 + 메모리 + 대화 이력 계층적 조합 |
| 6 | 출력 파싱 | 모델 응답에서 구조화된 도구 호출 추출 |
| 7 | 상태 관리 | 에이전트 진행 상태를 타입화된 데이터 구조로 추적·체크포인팅 |
| 8 | 오류 처리 | 일시적·복구 가능·사용자 수정·예외 오류를 분류해 처리 |
| 9 | 안전 제약(Guardrails) | 입력 검증 + 출력 검증 + 도구 수준 권한 검사 3단계 |
| 10 | 검증 루프 | 자체 검증 메커니즘 (품질 2~3배 향상) |
| 11 | 하위 에이전트 오케스트레이션 | 포크·핸드오프·워크트리 격리로 서브태스크 위임 |

### 4-2. Harness 패키지를 묶는 이유 (재사용성)

- **관심사 분리:** 모델 추론 ↔ 인프라 관리를 분리 → 모델 교체 시 Harness 재설계 불필요
- **표준화:** OpenAI·Anthropic·LangChain이 유사한 컴포넌트 인터페이스로 수렴 → 플랫폼 간 이식성
- **에이전트 스프롤 방지:** 팀별로 중복 구축하는 대신 중앙 Harness 플랫폼 공유 → 일관된 거버넌스
- **거버넌스:** Worker Agent Catalog에 전체 에이전트 정의(지시문·출력·입력·환경변수) 저장
  - 출처: Harness Developer Hub (https://developer.harness.io/docs/platform/harness-ai/harness-agents/)

### 4-3. Harness 패키지 최소 구성 (자산 등록 단위)

```
Harness 패키지 {
  ID: "harness-defect-analysis-v1.2"
  시스템 프롬프트: → Prompt 자산 레지스트리 참조 (예: "sys-pcb-quality-v3")
  입력 스키마: {
    클레임_번호: string,
    제품_모델: string,
    불량_설명: string,
    첨부_이미지: base64 | null
  }
  도구 목록: [
    "search_defect_history",   // 유사 불량 이력 검색
    "lookup_spec_table",       // PCB 규격 조회
    "generate_report"          // 보고서 생성
  ]
  도구 호출 순서: [sequential | parallel | conditional]
  출력 스키마: {
    defect_code: enum["DEL","WIC","CAF","CCL_CRACK",...],
    cause_summary: string,
    recommended_action: string,
    confidence: float(0~1)
  }
  평가 기준: → 평가셋 자산 참조 (예: "eval-defect-analysis-v1")
  의존성: {
    glossary: "A-3/pcb-quality-terms",
    data_schema: "D-1/claim-report-schema-v2"
  }
}
```

---

## 5. 현업 실행 키트 재료 — Prompt 자산 항목 사전 {#5-항목-사전}

Prompt 자산 1건을 레지스트리에 등록할 때 채우는 메타 항목 (종합):

출처 종합: MLflow Prompt Registry (https://mlflow.org/docs/latest/genai/prompt-registry/), Braintrust (https://www.braintrust.dev/articles/what-is-prompt-versioning), Databricks (https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/), Medium Enterprise Prompt Registry (https://medium.com/@t.sankar85/enterprise-prompt-registry-a4113b02bb53)

| 항목 | 쉬운 의미 | 예시값 | 필수/선택 | 작성 주체(후보) |
|------|-----------|--------|-----------|----------------|
| 자산 ID | 레지스트리 내 고유 식별자 | `prompt-claim-classify-v1` | 필수 | 시스템 자동생성 |
| 이름 | 사람이 알아볼 수 있는 프롬프트 이름 | "클레임 원인 분류 프롬프트" | 필수 | AI 조직 / 현업 SME |
| 버전 | 변경될 때마다 자동 부여되는 순번 | `v1.3.0` 또는 `3` | 필수 | 시스템 자동생성 |
| 업무 카테고리 | 어떤 업무 영역의 프롬프트인지 | "품질관리 / 클레임분석" | 필수 | AI 조직 |
| 대상 모델 | 이 프롬프트를 검증한 AI 모델 | `claude-3-5-sonnet-20241022` | 필수 | AI 조직 |
| 모델 파라미터 | 온도(temperature) 등 실행 설정 | `temperature: 0.2, max_tokens: 1024` | 필수 | AI 조직 |
| 템플릿 텍스트 | 실제 프롬프트 내용 (변수 포함) | `"{{claim_report}}에서 원인 코드를 분류하라..."` | 필수 | 현업 SME + AI 조직 |
| 입력 변수 목록 | 템플릿 내 교체 가능한 변수들 | `claim_report, product_model, defect_image` | 필수 | AI 조직 |
| 출력 형식 | 기대하는 출력의 구조 | JSON 스키마 또는 텍스트 양식 | 필수 | AI 조직 + 현업 SME |
| 작성자 | 이 버전을 만든 사람 | `kim.jiyeon@doosan.com` | 필수 | 시스템 자동기록 |
| 승인자 | 배포를 승인한 사람 | `quality-lead@doosan.com` | 필수 | 현업 리더 / 데이터 조직장 |
| 상태 | 현재 생애주기 단계 | 후보(draft) / 검증중(staging) / 배포(production) / 폐기(deprecated) | 필수 | 시스템 자동 + 관리자 |
| 커밋 메시지 | 이 버전에서 무엇을 왜 바꿨는지 | "Delamination 원인코드 2개 추가, 정확도 82%→91%" | 필수 | 작성자 |
| 의존 데이터/Glossary | 이 프롬프트가 참조하는 데이터·용어 | `A-3/pcb-defect-glossary`, `D-1/claim-schema-v2` | 필수 | 데이터 조직 |
| 의존 Tool | Harness에서 호출하는 도구 | `search_defect_history`, `lookup_spec_table` | 해당시 필수 | AI 조직 |
| 평가셋 연결 | 이 프롬프트를 검증한 테스트 데이터셋 | `eval-claim-classify-v1` (정확도 91%, n=200) | 필수 | AI 조직 / QA |
| 태그 | 분류·검색을 위한 키워드 | `["pcb", "품질", "클레임", "분류"]` | 선택 | 작성자 |
| 비고/변경사유 | 이 버전 작성 배경 | "2025-03 CAF 불량 급증으로 원인코드 갱신" | 선택 | 현업 SME |

### 5-1. 생애주기 단계 정의

MLflow·Braintrust 등 주요 플랫폼의 공통 3단계:

```
개발(Development) → 검증(Staging) → 배포(Production) → [폐기(Deprecated)]
```

- **개발:** 자유로운 반복 실험, 프로덕션 영향 없음
- **검증:** 프로덕션 유사 데이터로 최종 검증, 품질 기준 통과 필요
- **배포:** 실제 업무 적용, 모니터링 + 즉각 롤백 가능
- **폐기:** 더 이상 쓰지 않지만 이력 보존

출처: Braintrust — What is prompt versioning? (https://www.braintrust.dev/articles/what-is-prompt-versioning)

### 5-2. 작성 주체 역할 분담 (후보)

| 역할 | 주체 | 담당 항목 |
|------|------|-----------|
| 업무 전문가(SME) | 현업 품질/생산 담당자 | 업무 절차 정의, 판단 기준 제공, 예시 쌍(Few-shot) 검토·승인 |
| AI 엔지니어 | AI/데이터 조직 | 템플릿 구조화, 모델 파라미터 설정, 출력 형식 설계, 평가셋 구성 |
| 데이터 스튜어드 | 데이터 조직 | 의존 데이터·Glossary 연결, 자산 ID 부여, 레지스트리 등록 |
| 관리자/검토자 | 현업 리더 또는 AI CoE | 배포 승인, 품질 기준 검토, 폐기 결정 |

---

## 6. 제조 맥락 예시 후보 {#6-제조-예시}

가이드 본문 작성 시 활용할 두산 계열사 예시 후보:

### 두산전자 (PCB 소재)

| 예시 Prompt 자산명 | 업무 | 주요 입력 변수 | 주요 출력 |
|-------------------|------|----------------|-----------|
| CCL 시험성적서 요약 | 시험성적서에서 핵심 규격값 추출·요약 | 성적서 PDF 텍스트, 제품 코드 | 규격 항목·측정값·합부판정 구조화 JSON |
| 클레임 원인 분류 | 고객 클레임 보고서에서 불량 원인 코드 자동 분류 | 클레임 본문, 제품 모델, 공정 이력 | defect_code, cause_summary, confidence |
| Delamination 원인 분석 | 층간박리 불량 원인 추론 단계별 가이드 | 외관 검사 결과, 적층 조건, 소재 이력 | 원인 후보 목록, 추가 확인 항목 |
| C/S Report 분류 | 고객 서비스 리포트를 카테고리별로 자동 분류 | C/S 본문 텍스트 | 분류 코드, 심각도, 담당 팀 |

### 두산에너빌리티 (발전·주단조)

| 예시 Prompt 자산명 | 업무 | 주요 입력 변수 | 주요 출력 |
|-------------------|------|----------------|-----------|
| 용접 검사 보고서 생성 | 용접부 검사 데이터 기반 표준 보고서 자동 작성 | 검사 수치, 기준값, 검사원 ID | 구조화된 검사 보고서 (합부·이상 항목 강조) |
| 설비 점검 이상 요약 | 설비 점검 로그에서 이상 항목 추출·요약 | 점검 로그 텍스트, 설비 ID | 이상 항목 목록, 조치 필요 여부 |

### 두산밥캣 (건설기계)

| 예시 Prompt 자산명 | 업무 | 주요 입력 변수 | 주요 출력 |
|-------------------|------|----------------|-----------|
| 결함 원인-조치 추천 | 현장 결함 신고를 읽고 원인과 조치 방안 추천 | 결함 설명, 기종, 운용 시간 | 원인 진단, 긴급도 분류, 추천 조치 |

---

## 7. 출처 목록 {#7-출처-목록}

| # | 출처명 | URL | 성격 |
|---|--------|-----|------|
| 1 | Braintrust — "What is prompt management?" | https://www.braintrust.dev/articles/what-is-prompt-management | 개념·플랫폼 문서 |
| 2 | Braintrust — "What is prompt versioning?" | https://www.braintrust.dev/articles/what-is-prompt-versioning | 버전관리·메타데이터 |
| 3 | Databricks Blog — "What is an AI agent harness?" | https://www.databricks.com/blog/ai-harness | Harness 정의·구조 |
| 4 | The Anatomy of an Agent Harness (Daily Dose of DS) | https://blog.dailydoseofds.com/p/the-anatomy-of-an-agent-harness | Harness 11컴포넌트 상세 |
| 5 | Parallel.ai — "What is an agent harness?" | https://parallel.ai/articles/what-is-an-agent-harness | Harness 개요 |
| 6 | Martin Fowler — "Structured Prompt-Driven Development" | https://martinfowler.com/articles/structured-prompt-driven/ | SPDD/REASONS Canvas 방법론 |
| 7 | MLflow Prompt Registry 공식 문서 | https://mlflow.org/docs/latest/genai/prompt-registry/ | 메타 항목·버전 스키마 |
| 8 | Databricks MLflow Prompt Registry (AWS) | https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/ | 레지스트리 필드 상세 |
| 9 | Langfuse Prompt Management Overview | https://langfuse.com/docs/prompt-management/overview | 오픈소스 CMS 구조 |
| 10 | Parloa — Prompt Engineering Frameworks | https://www.parloa.com/knowledge-hub/prompt-engineering-frameworks/ | RTF·RASCEF·CARE 등 |
| 11 | God of Prompt — 7 AI Prompt Structures | https://godofprompt.ai/blog/7-ai-prompt-structures-that-generate-perfect-content-every-time/ | 프레임워크 정리 |
| 12 | Futureagi — Dynamic Prompts (Variables, Runtime Context) | https://futureagi.com/blog/dynamic-prompts/ | 출력 형식·변수 주입 |
| 13 | IBM — What is few shot prompting? | https://www.ibm.com/think/topics/few-shot-prompting | Few-shot 개념 |
| 14 | Redteamer.tips — Prompt Engineering and Agent Guardrails | https://redteamer.tips/taming-the-beast-prompt-engineering-and-agent-guardrails | 안전 제약 구조 |
| 15 | Harness Developer Hub — Worker Agents | https://developer.harness.io/docs/platform/harness-ai/harness-agents/ | Worker Agent Catalog |
| 16 | Medium — Enterprise Prompt Registry | https://medium.com/@t.sankar85/enterprise-prompt-registry-a4113b02bb53 | 엔터프라이즈 레지스트리 설계 |
| 17 | nextagile.ai — Prompt Engineering Techniques 2026 | https://nextagile.ai/blogs/ai/prompt-engineering-techniques/ | 엔터프라이즈 컨텍스트 엔지니어링 |
| 18 | Pinecone — LangChain Prompt Templates | https://www.pinecone.io/learn/series/langchain/langchain-prompt-templates/ | 템플릿 변수·컨텍스트 주입 |
| 19 | TrueFoundry — Prompt Management Tools | https://www.truefoundry.com/blog/prompt-management-tools | 도구 비교·기능 개요 |
| 20 | arize.com — Top 5 AI Prompt Management Tools 2026 | https://arize.com/blog/top-5-ai-prompt-management-tools-for-2026/ | 플랫폼 비교 |
