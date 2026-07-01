# LangSmith — AI Agent 관측·평가 플랫폼

> 작성일: 2026-06-10 | 조사 기준: 2025~2026 최신 동향

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | LangChain, Inc. |
| 라이선스 | 독점 SaaS (소스 비공개) |
| 배포 형태 | 클라우드 SaaS / Enterprise 셀프호스팅 (VPC/온프레미스) |
| 최신 동향 | LangSmith Engine (AI 자동 진단, 2025 공개 베타) / Agent Ops 기능 대폭 강화 (2025~2026) |

---

## 한 줄 포지셔닝

**"LangChain 생태계의 기본 관측 플랫폼 — Agent 실행 트리를 완전 추적하고 평가·Prompt 관리를 하나로 통합"**

---

## 주요 기능

### 트레이싱 (Observability)
- LLM 호출, 도구 호출(Tool Invocation), 검색(Retrieval), 추론 경로 전체를 **실행 트리(Execution Tree)** 형태로 시각화
- 대화 스레드·서브에이전트 위임·메모리를 1급 객체(first-class concept)로 처리
- 프레임워크 무관(Framework Agnostic): LangChain/LangGraph 외 OpenAI, Anthropic, Vercel AI SDK 등 자동 계측
- **Polly AI 어시스턴트**: 대용량 트레이스를 AI가 자동 분석해 문제 원인 지목 (2025 추가)
- **LangSmith Engine** (공개 베타, 2025): 프로덕션 트레이스를 모니터링 → 실패 클러스터링 → 코드 원인 진단 → 수정 제안 자동화

### Prompt 관리 (D-3)
- **Prompt Hub**: 중앙화된 Prompt Registry, 버전 관리, 팀 협업
- Prompt 변경사항 diff, rollback, A/B 테스트 지원
- 코드 ↔ UI 양방향 동기화 (엔지니어-PM 협업 워크플로)

### 평가 (E-3)
- LLM-as-judge 평가기(Evaluator) 내장: 사실성, 유해성, 관련성 등
- 커스텀 평가 코드 작성 및 데이터셋 기반 자동 실행
- 인간 어노테이션 UI: 레이블링, 코멘트, 평점 수집
- **Online Scoring**: 프로덕션 트레이스 실시간 자동 평가

### 데이터셋 관리 (E-3/E-4)
- 프로덕션 트레이스에서 평가 예시(example) 자동 수집
- 데이터셋 버전 관리, 실험 비교 (A/B Prompt 간 점수 비교)
- CI/CD 통합: 배포 전 평가 게이트(Quality Gate)

### 피드백 수집 (E-4)
- 사용자 Thumbs Up/Down 등 피드백 API
- 실패 클러스터 → 데이터셋 보강 → 재평가 Feedback Loop

---

## AI-Ready Data 주제 매핑

| 코드 | 주제 | 커버 수준 | 설명 |
|------|------|-----------|------|
| D-2 | API/Tool 연계 (MCP) | △ | Tool 호출 추적은 완전 지원, MCP 서버 직접 통합은 생태계 수준 |
| D-3 | Prompt/Harness 자산화 | ○ | Prompt Hub · 버전관리 · A/B 실험 · 팀 협업 모두 지원 |
| E-3 | AI 평가 데이터 | ○ | 데이터셋 관리, LLM-judge, 인간 어노테이션 완비 |
| E-4 | Feedback Loop | ○ | Online Scoring + LangSmith Engine 자동 진단 + 데이터셋 보강 |

---

## 강점

- LangChain/LangGraph 프로젝트와 완전 통합 (Zero-config 트레이싱)
- Agent 실행 트리 시각화가 업계 최고 수준 (멀티에이전트·서브에이전트 지원)
- Prompt Hub + 평가 + 트레이싱이 단일 UI에 통합되어 팀 협업 워크플로 최적화
- **LangSmith Engine**: AI 기반 자동 진단 → 운영 비용 절감

## 약점·주의점

- **소스 비공개**: 셀프호스팅은 Enterprise 플랜에서만 가능, 독점 제품 의존성
- **비용**: 트레이스 볼륨 증가 시 비용 급증 (월 수천 달러 가능)
- LangChain 외 프레임워크는 수동 계측 코드 필요 (SDK 제공하지만 Zero-config 아님)
- 기업 셀프호스팅 최소 인프라: 16+ vCPU / 64+ GB RAM / K8s 필수

---

## 가격 모델

| 플랜 | 가격 | 주요 포함 |
|------|------|-----------|
| Developer | 무료 | 월 5,000 트레이스, 14일 보존 |
| Plus | $39/월/사용자 | 월 50,000 트레이스, 30일 보존 |
| Enterprise | 커스텀 (연간 계약) | 셀프호스팅, SSO, RBAC, 무제한 트레이스, SLA |

> Enterprise 셀프호스팅 총비용: 소규모 배포 기준 $950~$1,150/월 (인프라 포함) 예상

---

## 연동 생태계

- **네이티브**: LangChain, LangGraph, LangSmith SDK (Python/TS)
- **프레임워크**: OpenAI, Anthropic, Vercel AI SDK, DSPy, LlamaIndex
- **평가**: AutoEvals 내장 (사실성·유해성·관련성 등)
- **CI/CD**: GitHub Actions, pytest 통합
- **MCP**: Tool 호출 추적 가능, MCP 서버 Registry 직접 통합은 로드맵

---

## 출처

- https://www.langchain.com/langsmith-platform
- https://www.langchain.com/langsmith/observability
- https://www.langchain.com/blog/introducing-langsmith-engine
- https://docs.langchain.com/langsmith/observability
- https://www.langchain.com/articles/agent-observability
- https://medium.com/@sehaj23chawla/langsmith-and-langgraph-in-2026-how-langchains-agent-stack-quietly-became-the-default-f1609af5d658
- https://pecollective.com/blog/langsmith-pricing/
- https://checkthat.ai/brands/langsmith/pricing
