# LLM Gateway: LiteLLM & Portkey

> 작성일: 2026-06-10 | 조사 기준: 2025~2026 최신 동향

---

## 1. LiteLLM

### 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | BerriAI |
| 라이선스 | MIT (오픈소스) |
| 배포 형태 | Python SDK / Proxy 서버 (Docker·K8s) / litellm.ai 클라우드 |
| 최신 동향 | MCP 엔드포인트 통합 (2025) / 100+ LLM 프로바이더 지원 / A2A(Agent-to-Agent) 게이트웨이로 확장 |

### 한 줄 포지셔닝

**"OpenAI 포맷으로 100+ LLM을 통합 호출하는 MIT 오픈소스 AI 게이트웨이 — MCP·비용 추적·로드밸런싱 내장"**

### 주요 기능

#### 통합 API 인터페이스 (D-2)
- **100+ LLM 프로바이더**: OpenAI, Anthropic, Google Gemini, AWS Bedrock, Azure OpenAI, VertexAI, Ollama, HuggingFace, NVIDIA NIM 등
- **OpenAI 포맷 통일**: 기존 OpenAI SDK 코드를 수정 없이 다른 모델로 전환
- 로드밸런싱: 여러 배포 간 요청 자동 분산, 장애 시 Fallback
- 스트리밍 지원

#### 비용 추적·예산 관리
- 가상 API Key별·팀별·사용자별 사용량 및 비용 추적
- 예산 한도 설정 (하드/소프트 한도), 한도 초과 시 자동 차단
- 청구 리포트 자동 생성

#### MCP 통합 (D-2)
- **중앙 MCP 엔드포인트**: LiteLLM Proxy를 통해 MCP 서버 단일 진입점 제공
- Key별 MCP 도구 접근 제어 (per-key access control)
- A2A(Agent-to-Agent) 에이전트 + MCP 도구를 하나의 게이트웨이로 통합

#### 보안·거버넌스
- 콘텐츠 필터링 (Content Filtering)
- PII 마스킹
- SSO/SAML, 감사 로그 (Enterprise)
- Rate Limiting, IP Allowlist

#### 관측성 연동
- Langfuse, Arize Phoenix, W&B Weave, MLflow, Helicone 등 주요 관측 플랫폼에 로그 전달
- OpenTelemetry 지원

### AI-Ready Data 주제 매핑

| 코드 | 주제 | 커버 수준 | 설명 |
|------|------|-----------|------|
| D-2 | API/Tool 연계 (MCP) | ○ | 100+ LLM 통합 + MCP 중앙 엔드포인트 + A2A 지원 |
| D-3 | Prompt/Harness 자산화 | × | 해당 없음 (게이트웨이 역할) |
| E-3 | AI 평가 데이터 | × | 해당 없음 |
| E-4 | Feedback Loop | × | 트레이스 로그를 관측 플랫폼에 전달하는 역할 |

### 강점
- MIT 오픈소스, 완전 셀프호스팅 가능 — 데이터 완전 통제
- 100+ 프로바이더 지원으로 멀티 LLM 전략의 핵심 인프라
- 계열사별 API Key·예산 격리 → 그룹 공통 플랫폼 운영 최적
- MCP 게이트웨이 역할 추가로 에이전트 Tool 접근도 중앙 관리

### 약점·주의점
- 트레이싱·평가·Prompt 관리 기능 없음 — 관측 플랫폼과 반드시 조합 필요
- 고가용성 프로덕션 배포 시 Redis·PostgreSQL 인프라 추가 필요
- Enterprise 기능(SSO·감사 로그)은 유료

### 가격 모델
| 플랜 | 가격 | 주요 포함 |
|------|------|-----------|
| 오픈소스 (셀프호스팅) | 무료 | 전체 기능, MIT |
| litellm.ai Enterprise | 협의 | 관리형 클라우드, SLA, 전용 지원 |

### 연동 생태계
- **LLM 프로바이더**: 100+ (OpenAI, Anthropic, AWS Bedrock, Azure, GCP Vertex, Ollama 등)
- **관측**: Langfuse, Arize Phoenix, W&B Weave, MLflow, Helicone
- **에이전트**: LangChain, LlamaIndex, OpenAI Agents SDK, MCP
- **인프라**: Docker / K8s Helm / Redis / PostgreSQL

### 출처
- https://docs.litellm.ai/docs/simple_proxy
- https://github.com/BerriAI/litellm/
- https://docs.litellm.ai/docs/
- https://agenta.ai/blog/top-llm-gateways
- https://markaicode.com/tutorial/litellm-proxy-gateway-tutorial-production/

---

## 2. Portkey

### 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Portkey AI |
| 라이선스 | Apache-2.0 (2026.03 완전 오픈소스화, 이전 SaaS 기능 포함) |
| 배포 형태 | 클라우드 SaaS (portkey.ai) / 셀프호스팅 (오픈소스화 이후) |
| 최신 동향 | 2026.03 게이트웨이 완전 오픈소스화 (거버넌스·관측성·인증·비용 제어 포함) / Agent Gateway 출시 / 2조 토큰 처리 마일스톤 |

### 한 줄 포지셔닝

**"엔터프라이즈 AI 거버넌스에 특화된 LLM 게이트웨이 — 2026.03 완전 오픈소스화로 셀프호스팅 가능"**

### 주요 기능

#### 통합 API·라우팅 (D-2)
- 1,600+ LLM 엔드포인트 지원 (LiteLLM보다 광범위)
- 모델 간 동적 전환, 로드밸런싱, 가중치 기반 분산
- Fallback 자동화: 장애 시 대체 모델로 자동 전환

#### 보안·거버넌스 (엔터프라이즈 특화)
- **PII 자동 처리**: 이메일·전화번호·SSN 등 민감 데이터를 LLM 전달 전 표준 식별자로 치환
- JWT 인증, SSO 통합
- 종합 감사 로그 (Audit Logs)
- **Agent Gateway**: AI 에이전트에 대한 거버넌스·관측성·제어 전담 레이어

#### 비용·사용량 추적
- 실시간 API 요청, 비용, 가이드레일 위반 기록
- 프로젝트·팀·사용자별 비용 추적
- 예산 한도 및 알림

#### 관측성
- 실시간 요청/응답 로그, 지연시간, 오류율 대시보드
- LLM 요청 세부 인스펙션

#### 가이드레일 (Guardrails)
- 50+ AI 가이드레일 내장 (콘텐츠 필터, 안전, 규정 준수)

### AI-Ready Data 주제 매핑

| 코드 | 주제 | 커버 수준 | 설명 |
|------|------|-----------|------|
| D-2 | API/Tool 연계 (MCP) | ○ | 1,600+ LLM + Agent Gateway + 가이드레일 통합 |
| D-3 | Prompt/Harness 자산화 | × | 해당 없음 (게이트웨이 역할) |
| E-3 | AI 평가 데이터 | × | 해당 없음 |
| E-4 | Feedback Loop | × | 로그를 관측 플랫폼에 전달하는 역할 |

### 강점
- **엔터프라이즈 거버넌스 강점**: PII 처리, JWT 인증, 감사 로그, Agent Gateway
- 2026.03 완전 오픈소스화 → 셀프호스팅으로 데이터 완전 통제 가능
- 가이드레일 50+ 내장 — 규정 준수·안전 요건 즉시 대응
- 1,600+ 엔드포인트 지원으로 LiteLLM보다 광범위한 모델 커버리지

### 약점·주의점
- 오픈소스화(2026.03) 이후 셀프호스팅 운영 성숙도는 LiteLLM보다 낮을 수 있음
- 트레이싱·평가·Prompt 관리 기능 없음 — 관측 플랫폼과 조합 필수
- 한국어 문서·커뮤니티 상대적으로 적음

### 가격 모델
| 플랜 | 가격 | 주요 포함 |
|------|------|-----------|
| 오픈소스 (셀프호스팅) | 무료 (2026.03~) | Apache-2.0, 거버넌스·관측 포함 |
| 클라우드 Free | 무료 | 기본 할당량 |
| 클라우드 Pro | $49/월~ | 더 많은 요청, 팀 기능 |
| Enterprise | 협의 | 전용 지원, SLA, 고급 보안 |

### 연동 생태계
- **LLM 프로바이더**: OpenAI, Anthropic, Google, Deepseek, AWS Bedrock, Azure, 로컬 모델
- **에이전트**: OpenAI Agents SDK, LangChain, CrewAI
- **관측**: 자체 대시보드, 외부 플랫폼 로그 전달
- **인프라**: Docker / K8s (오픈소스화 이후)

### 출처
- https://portkey.ai/
- https://portkey.ai/features/ai-gateway
- https://github.com/portkey-ai/gateway
- https://portkey.ai/docs/changelog/2025/jan
- https://www.infoworld.com/article/3835182/portkey-an-open-source-ai-gateway-for-easy-llm-orchestration.html

---

## LiteLLM vs Portkey 비교

| 구분 | LiteLLM | Portkey |
|------|---------|---------|
| 라이선스 | MIT | Apache-2.0 (2026.03~) |
| 오픈소스화 시점 | 처음부터 오픈소스 | 2026.03 완전 오픈소스화 |
| LLM 지원 | 100+ 프로바이더 | 1,600+ 엔드포인트 |
| MCP 통합 | ○ (중앙 MCP 엔드포인트) | △ (Agent Gateway 경유) |
| 엔터프라이즈 거버넌스 | △ (Enterprise 기능 유료) | ○ (PII·JWT·감사 로그 내장) |
| 비용 추적 | ○ | ○ |
| 커뮤니티·성숙도 | 높음 (먼저 오픈소스) | 성장 중 |
| 한국 레퍼런스 | 상대적으로 많음 | 적음 |

> **권장 조합 (기업 셀프호스팅)**:
> - **기본**: LiteLLM (MIT, 안정적) + Langfuse (관측·평가)
> - **보안 강화**: Portkey (PII·거버넌스) 또는 LiteLLM + Langfuse 보안 설정 강화
> - **MCP 에이전트**: LiteLLM MCP Gateway + Langfuse 트레이싱
