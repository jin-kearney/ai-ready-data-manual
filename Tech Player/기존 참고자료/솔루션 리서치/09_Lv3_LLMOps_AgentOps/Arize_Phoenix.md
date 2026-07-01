# Arize Phoenix — 오픈소스 AI 관측·평가 플랫폼

> 작성일: 2026-06-10 | 조사 기준: 2025~2026 최신 동향

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Arize AI |
| 라이선스 | Apache-2.0 (오픈소스) |
| 배포 형태 | 로컬 Python 라이브러리 / Docker·K8s / 클라우드 (app.phoenix.arize.com) |
| 최신 동향 | OpenInference + Open Agent Specification 통합 (2025) / Claude Agent SDK·OpenAI Agents SDK 1급 지원 / Oracle AI 연동 |

---

## 한 줄 포지셔닝

**"OpenTelemetry 기반 벤더 중립 오픈소스 관측 플랫폼 — Agent 그래프 시각화와 RAG 평가를 로컬부터 클라우드까지"**

---

## 주요 기능

### 트레이싱 (Observability)
- **OpenTelemetry(OTLP) 기반**: 표준 계측, 자동 계측 지원 (Auto-instrumentation)
- 지원 프레임워크: OpenAI Agents SDK, **Claude Agent SDK**, LangGraph, LlamaIndex, DSPy, Vercel AI SDK, AWS Bedrock 등
- **Agent Graph & Path Visualization**: 개별 Span을 노드 그래프로 추상화 → 에이전트 실행 흐름 직관적 시각화, 디버깅 시간 단축
- 지연시간, 토큰 사용량, 런타임 예외, LLM 파라미터 인스펙션

### Prompt 관리 (D-3)
- Prompt 버전 관리, 실제 프로덕션 예시 기반 이터레이션
- 프롬프트 변형 테스트 (Prompt Variant A/B)
- 프로덕션 호출 재실행(Replay) — 프롬프트 변경 효과 확인

### 평가 (E-3)
- **LLM-as-judge**: 내장 평가기, 커스텀 평가기 작성 가능
- 코드 기반 평가 체크 + 인간 레이블(Human Labels)
- 트레이스·Span 단위 점수 부여
- RAG 전용 평가: 문맥 관련성, 충실성(Faithfulness), 응답 관련성

### 에이전트 특화 (D-2/E-3)
- **OpenInference**: Arize가 주도하는 AI 추적 표준 (OTel 기반)
- **Open Agent Specification**: 에이전트 간 통신 표준화, Oracle AI 연동
- MCP 도구 호출 추적 지원

### 데이터셋 관리 (E-3/E-4)
- 트레이스에서 데이터셋 예시 추출
- 데이터셋 기반 실험 실행, 모델·프롬프트 비교

---

## AI-Ready Data 주제 매핑

| 코드 | 주제 | 커버 수준 | 설명 |
|------|------|-----------|------|
| D-2 | API/Tool 연계 (MCP) | ○ | MCP Tool 호출 추적, OpenInference 표준으로 에이전트 Tool 통합 |
| D-3 | Prompt/Harness 자산화 | ○ | Prompt 버전관리·변형 테스트·재실행 지원 |
| E-3 | AI 평가 데이터 | ○ | LLM-judge·인간 레이블·RAG 전용 메트릭 완비 |
| E-4 | Feedback Loop | △ | 트레이스 → 데이터셋 환류 지원, 자동화 수준은 LangSmith보다 낮음 |

---

## 강점

- **Apache-2.0 라이선스**: 상업적 이용 무제한, 완전 오픈소스
- 로컬 실행 가능 (Jupyter Notebook, 개발 환경에서 즉시 시작)
- Claude Agent SDK, OpenAI Agents SDK 등 최신 에이전트 프레임워크 1급 지원
- Agent Graph 시각화가 직관적 — 복잡한 멀티에이전트 디버깅에 효과적
- OpenTelemetry 표준 완전 준수 → 기존 관측 인프라와 통합 용이

## 약점·주의점

- Prompt Registry 기능이 LangSmith/Langfuse 대비 상대적으로 단순
- 비용 추적 기능 제한적 (LiteLLM·Portkey와 조합 권장)
- 클라우드 SaaS(app.phoenix.arize.com)는 Arize AI에 데이터 전송
- 셀프호스팅 시 운영 가이드가 Langfuse보다 상대적으로 적음

---

## 가격 모델

| 플랜 | 가격 | 주요 포함 |
|------|------|-----------|
| OSS (셀프호스팅) | 무료 | Apache-2.0, 기능 제한 없음 |
| 클라우드 Free | 무료 | app.phoenix.arize.com, 기본 할당량 |
| 클라우드 유료 | 협의 | 더 많은 보존, 팀 기능 |
| Arize Platform | 별도 엔터프라이즈 | Phoenix + 모델 모니터링 통합 |

---

## 연동 생태계

- **자동 계측(Auto-instrumentation)**: openinference-instrumentation-* 패키지 시리즈
- **프레임워크**: OpenAI, Anthropic (Claude SDK), LangChain, LangGraph, LlamaIndex, DSPy, Bedrock, Vertex AI
- **표준**: OpenTelemetry (OTLP), OpenInference, Open Agent Specification
- **MCP**: Tool 호출 Span 추적 가능
- **인프라**: Python 라이브러리 / Docker Hub / K8s

---

## 출처

- https://arize.com/docs/phoenix
- https://github.com/arize-ai/phoenix
- https://arize.com/
- https://www.statsig.com/perspectives/arize-phoenix-ai-observability
- https://blogs.oracle.com/ai-and-datascience/agent-spec-phoenix-integration
- https://docs.litellm.ai/docs/observability/phoenix_integration
- https://vap1231.medium.com/phoenix-open-source-langsmith-alternative-platform-for-ai-agent-observability-and-evaluation-b22618219e3d
