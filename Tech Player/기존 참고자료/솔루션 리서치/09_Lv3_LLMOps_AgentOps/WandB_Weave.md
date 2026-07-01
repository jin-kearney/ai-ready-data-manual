# W&B Weave — LLM 관측·평가 플랫폼 (Weights & Biases)

> 작성일: 2026-06-10 | 조사 기준: 2025~2026 최신 동향

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Weights & Biases (W&B) |
| 라이선스 | 독점 SaaS (소스 비공개) |
| 배포 형태 | 클라우드 SaaS (wandb.ai) / Enterprise 전용 셀프호스팅 |
| 최신 동향 | Agent 1급 지원 (세션·턴·스텝·도구·서브에이전트) / Amazon Bedrock AgentCore 통합 / Guardrails 강화 |

---

## 한 줄 포지셔닝

**"ML/MLOps 전통 강자 W&B가 LLM으로 확장 — 기존 실험 추적 역량에 LLM 관측·평가·가이드레일 통합"**

---

## 주요 기능

### 트레이싱 (Observability)
- **한 줄 계측**: `weave.init()` + `@weave.op()` 데코레이터로 즉시 추적 시작
- 트레이스가 검색 가능(Searchable), 버전화(Versioned), 공유(Shareable)
- **Agent 1급 지원**: 세션(Session)·턴(Turn)·스텝(Step)·도구(Tool)·서브에이전트(Sub-agent)를 1급 개념으로 처리
- 내장 신호(Built-in Signals): 에이전트 상호작용 자동 캡처·분류
- 지연시간, 토큰 사용량, 비용, 품질 메트릭 추적

### 평가 (E-3)
- **LLM-as-judge**: 사실성, 관련성, 유해성 사전 구축 스코어러
- **Guardrails**: 안전·품질 스코어러 내장
  - 안전: 독성(Toxicity), 편향(Bias), PII 감지, 환각(Hallucination)
  - 품질: 일관성(Coherence), 유창성(Fluency), 문맥 관련성
- 커스텀 스코어러 작성 및 파이프라인 조합

### Playground & 실험
- Playground: 모델·프롬프트 탐색, 에이전트 구성 전 이터레이션
- 프로덕션 트레이스로 새 모델 성능 테스트
- 실험 비교 (W&B의 전통적 강점 계승)

### 데이터셋 관리 (E-3)
- 트레이스에서 데이터셋 예시 추출
- 데이터셋 버전 관리, 실험 연동

### 피드백 수집 (E-4)
- 온라인 스코어링으로 프로덕션 품질 모니터링
- 시계열 성능 추적, 회귀(Regression) 알림

---

## AI-Ready Data 주제 매핑

| 코드 | 주제 | 커버 수준 | 설명 |
|------|------|-----------|------|
| D-2 | API/Tool 연계 (MCP) | △ | Tool 호출 추적 가능, MCP 직접 통합은 생태계 수준 |
| D-3 | Prompt/Harness 자산화 | △ | Prompt 버전 추적·Playground 지원, 전용 Prompt Hub는 부분적 |
| E-3 | AI 평가 데이터 | ○ | 내장 Guardrails·LLM-judge·인간 평가·데이터셋 완비 |
| E-4 | Feedback Loop | ○ | 온라인 스코어링·회귀 알림·실험 재실행 지원 |

---

## 강점

- **ML/MLOps 팀 친화적**: 기존 W&B 사용 팀은 학습 비용 최소화
- Guardrails 기능이 안전·품질 모두 내장 — 책임 AI 요건 대응 용이
- Amazon Bedrock AgentCore 공식 통합 → AWS 환경 기업에 적합
- 에이전트 계층(세션·턴·스텝)이 1급 추적 개념 — 복잡한 에이전트 파악 용이

## 약점·주의점

- **소스 비공개**, 셀프호스팅은 Enterprise 전용
- Prompt Registry(Hub·버전관리·팀 협업) 기능은 LangSmith/Langfuse보다 약함
- 비용: Enterprise 계약 필요, 투명한 가격표 미공개
- LangChain 생태계 통합은 LangSmith보다 밀도 낮음

---

## 가격 모델

| 플랜 | 가격 | 주요 포함 |
|------|------|-----------|
| Free | 무료 | 개인, 기본 기능 |
| Teams | $50/월/사용자 | 협업, 고급 기능 |
| Enterprise | 커스텀 | 셀프호스팅, SSO, SLA, 전용 지원 |

---

## 연동 생태계

- **SDK**: Python (weave 패키지), TypeScript
- **프레임워크**: OpenAI, Anthropic, LangChain, LlamaIndex, Instructor
- **클라우드**: Amazon Bedrock AgentCore (공식 통합)
- **기존 W&B**: Runs, Artifacts, Reports와 연동
- **인프라 (셀프호스팅)**: Enterprise 계약 후 W&B 지원

---

## 출처

- https://wandb.ai/site/weave/
- https://docs.wandb.ai/weave
- https://github.com/wandb/weave
- https://wandb.ai/site/articles/llm-observability/
- https://aws.amazon.com/blogs/machine-learning/accelerate-enterprise-ai-development-using-weights-biases-weave-and-amazon-bedrock-agentcore/
- https://qaskills.sh/blog/weights-biases-llm-evals-guide
