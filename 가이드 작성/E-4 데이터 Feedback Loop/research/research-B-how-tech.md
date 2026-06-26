# E-4 데이터 Feedback Loop — How(구축·운영) + Tech Stack 리서치

> 작성일: 2026-06-26  
> 관점: "AI가 쓸 데이터를 준비·정비하는 법" — AI/에이전트 구축법이 아니라 피드백 데이터 파이프라인·운영 절차

---

## 1. How — 수집·분류·라우팅·반영 표준 파이프라인

### 1-1. 파이프라인 4단계 개요

AWS Prescriptive Guidance(GenAI Lifecycle Operational Excellence)는 생산 피드백 루프를 다음 4단계로 정의한다. [[출처: AWS]](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-feedback.html)

| 단계 | 명칭 | 무엇을 하나 |
|------|------|------------|
| 1 | **수집(Collect)** | AI 응답 화면 및 로그에서 사용자 피드백(좋아요/싫어요·수정·코멘트)과 시스템 로그(Tool 호출 기록·오류 코드·응답 지연)를 자동 수집해 중앙 서비스로 집계 |
| 2 | **분류(Classify)** | 수집된 피드백을 원인 유형(데이터 누락·라벨 오류·Prompt 부정확·Tool 오작동·권한 문제 등)으로 태깅. LLM-as-a-Judge 또는 규칙 기반으로 1차 자동 분류, 저신뢰도 케이스는 전문가 수동 분류 |
| 3 | **라우팅(Route)** | 원인 유형 태그를 기준으로 해당 개선 주제(A-1~F-4)의 담당 팀에 Backlog 과제로 배분. 라우팅 테이블로 규칙을 명시 관리 |
| 4 | **반영(Apply)** | 저위험 케이스는 자동 반영(프롬프트 패치·데이터 주석 추가 등), 고위험·고객영향·보안 케이스는 전문가 검토 게이트 통과 후 반영 |

**Maxim AI 문헌**에서는 "피드백 분석 파이프라인이 개별 판단을 전략적 통찰로 변환하여 프롬프트 개선, 모델 파인튜닝, 테스트셋 확대로 반영"된다고 설명한다. [[출처: Maxim AI]](https://www.getmaxim.ai/articles/incorporating-human-in-the-loop-feedback-for-continuous-improvement-of-ai-agents/)

---

### 1-2. 수집 데이터 스키마

AWS Prescriptive Guidance가 권고하는 피드백 1건의 스키마 필드:
[[출처: AWS 피드백 스키마]](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-feedback.html)

| 필드명 | 데이터 유형 | 설명 | 예시값 |
|--------|------------|------|--------|
| `feedback_id` | UUID | 피드백 이벤트 고유 식별자 | `fb-20240501-001` |
| `trace_id` | UUID | **가장 중요한 필드** — 이 ID로 해당 AI 실행의 전체 맥락(Prompt·검색 문서·모델 응답·지연시간·버전·Tool 호출 내역)을 연결 | `tr-abc123` |
| `timestamp` | ISO 8601 | 피드백 제출 시각 | `2024-05-01T09:32:00Z` |
| `user_id` | String | 피드백 제공 사용자 식별자 | `user-doosan-kslee` |
| `feedback_type` | Enum | 피드백 종류 (`explicit_thumb`, `implicit_copy`, `explicit_comment`, `correction`) | `explicit_thumb` |
| `feedback_value` | Numeric/Boolean | 좋아요=1, 싫어요=0, 1~5 점수 | `0` |
| `feedback_comment` | String (선택) | 사용자 자유 텍스트 의견 | "엔진 사양이 틀림" |

**추가 권장 필드** (E-4 맥락에서 원인 라우팅을 위해 필요):

| 필드명 | 데이터 유형 | 설명 |
|--------|------------|------|
| `session_id` | UUID | 동일 사용자 상호작용 세션 묶음. Langfuse 기준 "같은 사용자 상호작용의 일부인 trace들을 집계" [[Langfuse]](https://langfuse.com/docs/observability/data-model) |
| `ai_task_id` | String | 어떤 AI 과제(품질검사·부품 탐색 등)에서 발생했는지 |
| `ai_input` | String | 사용자가 AI에 입력한 내용(개인정보 마스킹 필수) |
| `ai_output` | String | AI가 생성한 응답 |
| `user_correction` | String (선택) | 사용자가 직접 수정한 정답 |
| `citation_refs` | String[] | AI 응답 생성에 참조된 문서/데이터 출처 목록 |
| `tool_call_log` | JSON (선택) | Tool 호출 기록(이름·입력·출력·오류코드) |
| `cause_type_tag` | Enum (선택) | 분류 후 추가: `DATA_GAP`·`LABEL_ERROR`·`PROMPT_ISSUE`·`TOOL_FAIL`·`PERMISSION`·`EVAL_THRESHOLD` |
| `routing_target` | String (선택) | 라우팅 후 추가: `A-1`·`B-2`·`D-2`·`D-3`·`E-3`·`F-4` |
| `status` | Enum | `OPEN`→`TRIAGED`→`ROUTED`→`IN_PROGRESS`→`RESOLVED` |

**MLflow Feedback 엔티티**는 `value`(불린/수치/텍스트/구조화 데이터), `source`(HUMAN 또는 LLM_JUDGE), `rationale`(선택 설명)을 핵심 필드로 정의한다. [[MLflow Databricks]](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/collect-user-feedback/)

---

### 1-3. 원인 유형 태깅 — 라우팅 테이블

피드백 원인 분류 후 개선 과제를 해당 주제 팀으로 라우팅하는 운영 규칙:

| 원인 유형 태그 | 의미 | 라우팅 대상 주제 | 담당 |
|--------------|------|----------------|------|
| `DATA_GAP` | 필요 데이터 없음·검색 실패 | A-1 데이터 카탈로그 / A-2 메타데이터 | 데이터 오너 |
| `LABEL_ERROR` | AI 응답 근거 라벨·주석 오류 | B-2 데이터 해설·주석 | 데이터 오너 + SME |
| `EVAL_THRESHOLD` | 평가 기준치 부적절 | E-3 AI 평가 데이터 | AI 서비스 운영자 |
| `PROMPT_ISSUE` | Prompt 설계·버전 문제 | D-3 Prompt·Harness 자산화 | AI 서비스 운영자 |
| `TOOL_FAIL` | Tool 호출 실패·명세 오류 | D-2 API·Tool 연계 데이터 | DataOps |
| `PERMISSION` | 데이터 접근권한·비식별 문제 | F-4 데이터 접근권한·비식별 | 데이터 거버넌스 |
| `DATA_QUALITY` | 데이터 오류·결측·불일치 | C-2 데이터 품질 관리 | 데이터 오너 |

> 제조(두산) 예시: 엔진 부품 탐색 AI에서 "BOM 코드 없음" 오류가 반복 → `DATA_GAP` 태깅 → A-1 카탈로그 담당팀에 Backlog 등록.

---

### 1-4. 자동/수동 반영 게이트

**저위험 자동 반영 후보** (전문가 검토 없이 자동 적용 가능):
- 텍스트성 Prompt 문구 수정 (안전성 영향 없음)
- 데이터 주석(annotation) 추가 — 기존 라벨 변경이 아닌 신규 추가
- FAQ·가이드 문서 내 오탈자 수정

**고위험 → 전문가 검토 게이트**:
- 모델 파인튜닝 데이터셋 변경
- 데이터 접근권한 정책 수정 (F-4)
- 고객·현업 직접 영향: 품질 판정 로직, 안전 기준 변경
- 보안·개인정보 관련 비식별 규칙 수정

AWS 가이드는 "저위험·잘 정의된 시나리오에만 자동 실행, 고위험·새로운 시나리오는 인간 검토 루프 포함"을 권고한다. [[AWS]](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-feedback.html)

---

### 1-5. 담당자 역할 (RACI)

| 역할 | R (실행) | A (책임) | C (협의) | I (정보) |
|------|---------|---------|---------|---------|
| **수집** | AI 서비스 운영자 | AI 팀 리더 | DataOps | 데이터 오너 |
| **분류·태깅** | DataOps | AI 팀 리더 | 현업 SME | 데이터 오너 |
| **라우팅** | AI 서비스 운영자 | AI 팀 리더 | 데이터 오너 | 개선 담당팀 |
| **반영 승인** | 데이터 오너 + SME | AI 팀 리더 / 거버넌스 | 법무·보안(고위험) | AI 서비스 운영자 |
| **효과 추적** | DataOps | AI 팀 리더 | 현업 SME | 경영진 |

**현업 SME(Subject Matter Expert)**: 부품 데이터 적절성, 공정 기준 판단 등 도메인 지식 제공.  
**데이터 오너**: 해당 데이터셋 소유·승인 권한.  
**DataOps**: 파이프라인·인프라 운영.  
[[Maxim AI HITL 참고]](https://www.getmaxim.ai/articles/incorporating-human-in-the-loop-feedback-for-continuous-improvement-of-ai-agents/)

---

## 2. Tech Stack — 솔루션 3갈래

### 2-1. AI 응답 피드백 수집 솔루션

#### LangSmith (LangChain)
- **공식 URL**: https://www.langchain.com/langsmith
- **E-4 관점 기능**:
  - Annotation Queue: 실행 결과를 검토 대기열에 자동 라우팅 → 도메인 전문가가 평가
  - 사용자 좋아요/싫어요·코멘트를 `run_id`에 연결해 프로그래밍 방식으로 기록
  - 어노테이션 큐에서 수집된 인간 피드백이 평가 데이터셋으로 자동 전환
  - LLM-as-a-judge, 휴리스틱 평가, 쌍 비교(pairwise) 등 다중 평가자 지원
- **배포**: SaaS, 온프렘 가능(LangSmith Self-Hosted)
- **가격**: 공식문서·PoC 확인 권장

#### Langfuse
- **공식 URL**: https://langfuse.com
- **E-4 관점 기능**:
  - Browser SDK(`langfuse.score()`)로 프론트엔드에서 thumbs up/down·별점·코멘트 수집
  - Score 데이터를 `trace_id`에 연결해 저장 (필드: `traceId`, `name`, `value`, `dataType`, `comment`)
  - Session 개념으로 동일 사용자 세션 내 trace 묶음 관리
  - LLM-as-a-Judge 자동 평가 파이프라인 내장
  - 오픈소스(AGPL) — 자체 호스팅 가능, 폐쇄망 환경 적합
  - OpenTelemetry 표준 기반 계측(instrumentation)
- **데이터 모델 참고**: [Langfuse Concepts](https://langfuse.com/docs/observability/data-model)

#### Humanloop
- **공식 URL**: https://humanloop.com
- **E-4 관점 기능**:
  - 사용자 좋아요/싫어요 수정 피드백 수집 + 어노테이션 파이프라인
  - Prompt 버전 관리(Git-like)와 피드백 연계 — 어떤 Prompt 버전이 낮은 평가를 받았는지 추적
  - 비기술 도메인 전문가도 UI에서 평가 참여 가능
- **주의**: 2025년 9월 8일 플랫폼 종료 예정 — 채택 시 마이그레이션 계획 필수
  [[Humanloop Alternatives 참고]](https://www.keywordsai.co/blog/humanloop-alternatives)

---

### 2-2. 로그·모니터링/관측(Observability) 연계

**E-4 관점 포커스**: "실패·저평가 케이스를 잡아 피드백 수집 파이프라인으로 보내는" 기능.

#### Arize Phoenix (오픈소스)
- **공식 URL**: https://arize.com/phoenix/
- **GitHub**: https://github.com/arize-ai/phoenix
- **E-4 관점 기능**:
  - 모든 LLM 호출·Tool 호출·검색 단계를 단계별 trace로 기록
  - LLM 기반·코드 기반·인간 라벨 평가자 지원 — 저평가 trace를 필터링해 피드백 대상 케이스 추출
  - OpenTelemetry 기반, OpenInference 계측 — OpenAI, Anthropic Claude, LangGraph, LlamaIndex 등 주요 프레임워크 자동 계측
  - 자체 호스팅 가능: Docker/Kubernetes 배포, 온프렘 폐쇄망 적합
  - 실제 운영 예시 로 "잘못된 Tool 선택" 케이스를 trace에서 필터링 → `TOOL_FAIL` 태깅 → D-2 라우팅
- **클라우드**: https://app.phoenix.arize.com

#### Langfuse (앞서 설명 동일 — 수집·관측 통합)
- 피드백 수집과 관측을 단일 플랫폼에서 처리. 오픈소스로 자체 호스팅 가능.
- [Langfuse Observability](https://langfuse.com/docs/observability/overview)

#### LangSmith (앞서 설명 동일 — 추적·평가 통합)
- 에이전트 워크플로우의 비결정적 동작 디버깅, 비용·지연·품질 대시보드
- [LangSmith Platform](https://www.langchain.com/langsmith-platform)

#### Helicone
- **공식 URL**: https://www.helicone.ai/
- **E-4 관점 기능**:
  - AI Gateway 프록시 방식으로 모든 LLM 요청을 자동 로깅 — 코드 수정 없이 observability 추가
  - 사용자별·세션별 행동 패턴 추적, 비용·지연·품질 메트릭
  - Slack/이메일 임계값 알림 — 품질 지표가 기준치 이하로 떨어지면 피드백 수집 트리거
  - 자체 호스팅 지원(Docker), 오픈소스(AGPL)
  - [Helicone GitHub](https://github.com/helicone/helicone)

#### Datadog LLM Observability (엔터프라이즈)
- **공식 URL**: https://www.datadoghq.com/products/ai/agent-observability/
- **E-4 관점 기능**:
  - 엔드-투-엔드 LLM 트레이싱 + 에이전트 모니터링 + 오프라인 실험을 단일 플랫폼에서 제공
  - Human Review & Annotation 기능 내장 (2025년 발표)
  - Python/Node SDK로 OpenAI·LangChain·Anthropic·AWS Bedrock 자동 계측
  - 기존 Datadog 인프라 모니터링과 통합 → IT 운영 조직에 친숙한 환경
  - Google ADK, Amazon Bedrock Agents 자동 계측 지원 (2026년 2월 기준)
- **가격**: 공식문서·PoC 확인 권장

---

### 2-3. 이슈·개선 Backlog 관리 (협업 도구)

**E-4 관점**: 라우팅된 개선 과제를 추적하고 상태(`ROUTED`→`IN_PROGRESS`→`RESOLVED`)를 관리.

#### Jira (Atlassian)
- **공식 URL**: https://www.atlassian.com/software/jira
- **E-4 관점 기능**:
  - 커스텀 필드로 `cause_type_tag`·`routing_target`·`feedback_id`를 이슈에 연결
  - Webhook·API로 피드백 파이프라인에서 자동 이슈 생성 가능
  - 2025~2026년 Jira AI: 이슈 요약·검색 어시스턴트 내장
  - 기존 기업 IT 환경에서 가장 범용적 사용
  - 한계: LLM 피드백 전용 라우팅 인텔리전스 부족 — 규칙 기반 자동화로 보완

#### Azure DevOps (Microsoft)
- **공식 URL**: https://azure.microsoft.com/ko-kr/products/devops
- **E-4 관점 기능**:
  - Work Items로 개선 Backlog 관리, Boards로 상태 추적
  - Microsoft 생태계(Azure OpenAI·Copilot Studio) 기반 AI 시스템 환경에서 자연스러운 연동
  - Pipelines와 연계해 반영 승인 게이트 자동화

#### Linear
- **공식 URL**: https://linear.app
- **E-4 관점 기능**:
  - 2025~2026년 Linear AI: 신규 이슈를 읽고 과거 패턴 기반으로 담당자·라벨 자동 제안 (트리아지 자동화)
  - 스프린트 리포트 자동 생성, Backlog 우선순위 제안
  - 빠른 UX로 소규모 AI 팀에 적합, API 풍부

---

### 2-4. 선정 기준 요약

| 기준 | 핵심 체크포인트 |
|------|---------------|
| 수집 지점 자동 연동 | AI 응답 UI(프론트엔드) + 시스템 로그(백엔드) 동시 수집 가능한가 |
| 원인 유형 태깅 | 자동 분류(LLM-as-a-judge) + 수동 검토 병행 지원하는가 |
| 라우팅 규칙 운영 | 태그→담당팀 자동 라우팅, Backlog 도구와 API 연동 가능한가 |
| 개선 효과 추적 | 반영 전후 품질 지표 비교 대시보드 제공하는가 |
| 기존 협업 도구 연계 | Jira/Azure DevOps/Linear Webhook·API 지원하는가 |
| 온프렘·폐쇄망 | 자체 호스팅 가능한가 (두산 환경 고려) |

---

### 2-5. C-1 Observability vs LLM Observability 경계

| 구분 | C-1 데이터 파이프라인 Observability | LLM Observability (E-4 관련) |
|------|------------------------------------|------------------------------|
| 관찰 대상 | 데이터 파이프라인 이상 감지 (데이터 드리프트·결측·지연) | AI/LLM·에이전트 실행 추적 (응답 품질·Tool 호출·지연·비용) |
| 대표 도구 | Great Expectations, dbt tests, Apache Atlas | LangSmith, Langfuse, Arize Phoenix, Datadog LLM Obs |
| 피드백 연결 | 데이터 품질 이상 → C-2 품질 관리로 라우팅 | AI 응답 실패·저평가 → E-4 피드백 루프로 수집 |

---

## 3. 참고 출처 목록

| # | 출처 | URL |
|---|------|-----|
| 1 | AWS Prescriptive Guidance — GenAI Lifecycle Operational Excellence (피드백 파이프라인·스키마) | https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-feedback.html |
| 2 | Maxim AI — HITL Feedback for AI Agents (라우팅·게이트·RACI) | https://www.getmaxim.ai/articles/incorporating-human-in-the-loop-feedback-for-continuous-improvement-of-ai-agents/ |
| 3 | LangSmith Platform (공식) | https://www.langchain.com/langsmith-platform |
| 4 | LangSmith Evaluation (공식) | https://www.langchain.com/langsmith/evaluation |
| 5 | Langfuse 공식 홈페이지 | https://langfuse.com/ |
| 6 | Langfuse Observability 개요 | https://langfuse.com/docs/observability/overview |
| 7 | Langfuse 데이터 모델(Concepts) | https://langfuse.com/docs/observability/data-model |
| 8 | Langfuse 사용자 피드백(Score) | https://langfuse.com/docs/scores/user-feedback |
| 9 | Arize Phoenix 공식 홈페이지 | https://arize.com/phoenix/ |
| 10 | Arize Phoenix 문서 | https://arize.com/docs/phoenix |
| 11 | Arize Phoenix GitHub | https://github.com/arize-ai/phoenix |
| 12 | Helicone 공식 홈페이지 | https://www.helicone.ai/ |
| 13 | Helicone GitHub (오픈소스) | https://github.com/helicone/helicone |
| 14 | Datadog LLM Observability / Agent Observability | https://www.datadoghq.com/products/ai/agent-observability/ |
| 15 | Humanloop 공식 문서 | https://humanloop.com/docs/getting-started/overview |
| 16 | Humanloop 종료 안내·대안 | https://www.keywordsai.co/blog/humanloop-alternatives |
| 17 | MLflow Feedback 수집 (Databricks) | https://docs.databricks.com/aws/en/mlflow3/genai/tracing/collect-user-feedback/ |
| 18 | Galileo — Human-in-the-Loop Agent Oversight | https://galileo.ai/blog/human-in-the-loop-agent-oversight |
| 19 | Linear vs Jira 2026 비교 | https://prompteddev.com/blog/linear-vs-jira/ |
| 20 | Issue Trackers as AI Agent Infrastructure | https://www.mindstudio.ai/blog/issue-trackers-ai-agent-infrastructure-jira-linear |
| 21 | LangSmith Cookbook — Feedback Examples | https://github.com/langchain-ai/langsmith-cookbook/blob/main/feedback-examples/nextjs/README.md |
| 22 | Langfuse Trace IDs & Distributed Tracing | https://langfuse.com/docs/observability/features/trace-ids-and-distributed-tracing |
