# MCP (Model Context Protocol) — AI Agent Tool 연계 표준

> 작성일: 2026-06-10 | 조사 기준: 2025~2026 최신 동향

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 주도 기관 | Anthropic (초기 개발) → Linux Foundation 이관 (2025) |
| 라이선스 | MIT (사양 및 SDK) |
| 표준 성격 | 오픈 표준 (솔루션이 아닌 프로토콜 사양) |
| 최신 사양 | 2025-03-26 (Streamable HTTP 도입) / 2026-07-28 Release Candidate |
| 채택 현황 | 97M+ SDK 월간 다운로드 / 공개 서버 10,000+ / OpenAI·Google·Microsoft·AWS 지원 |

---

## 한 줄 포지셔닝

**"LLM이 외부 데이터·서비스·도구를 표준 방식으로 호출할 수 있게 하는 오픈 프로토콜 — USB-C처럼 AI와 도구 연결을 표준화"**

---

## 1. 아키텍처와 핵심 개념

### MCP 구성 요소

```
┌─────────────────────────────────────────────────────────┐
│                    MCP Host (AI 앱)                      │
│  (Claude Desktop, Cursor, VS Code, 사내 AI 플랫폼 등)     │
├─────────────────┬───────────────────────────────────────┤
│   MCP Client    │   (1:1 연결, 프로토콜 관리)              │
├─────────────────┴───────────────────────────────────────┤
│              MCP Server 1 | MCP Server 2 | ...          │
│  (파일 시스템 | DB 조회 | ERP API | 검색 | 계측 도구 등)    │
└─────────────────────────────────────────────────────────┘
```

- **MCP Host**: LLM 앱 (Claude Desktop, Cursor, 사내 AI 플랫폼)
- **MCP Client**: Host 내부에서 MCP Server와 1:1 연결을 유지하는 프로토콜 클라이언트
- **MCP Server**: 특정 데이터·서비스를 LLM에 노출하는 경량 서버

### 세 가지 핵심 프리미티브

| 프리미티브 | 역할 | 예시 |
|-----------|------|------|
| **Tools** | LLM이 실행하는 함수 (모델 제어) | DB 쿼리 실행, API 호출, 파일 쓰기 |
| **Resources** | 앱이 제공하는 데이터 (앱 제어) | 파일 내용, DB 레코드, 문서 |
| **Prompts** | 재사용 가능한 Prompt 템플릿 | 분석 워크플로, 보고서 생성 패턴 |

---

## 2. 전송 방식 (Transports)

### 현재 표준 (2025-03-26 사양)

| 방식 | 설명 | 적합 환경 |
|------|------|-----------|
| **Streamable HTTP** | HTTP POST/GET + 선택적 SSE 스트리밍 | **프로덕션 표준** (원격 서버) |
| **stdio** | 표준 입출력 파이프 | 로컬 프로세스 (개발·로컬 도구) |

> **Streamable HTTP 특징**:
> - 서버: 단일 HTTPS 엔드포인트 (POST + GET 모두 지원)
> - 세션 ID: `Mcp-Session-Id` 헤더 (암호학적으로 안전한 UUID)
> - 구버전 SSE 방식 (2024-11-05) 대비 더 유연하고 신뢰성 높음
> - 기업 환경 방화벽·프록시와 호환성 우수

---

## 3. MCP Registry (2025~2026)

### 현황

- **공식 MCP Registry API** (2026.05 기준): 9,652개 최신 서버 레코드, 28,959개 서버/버전 레코드
- Anthropic 2026 로드맵: **보안 등급이 매겨진 검증된 서버 디렉토리** 구축 중

### 주요 Registry 유형

| 유형 | 설명 | 예시 |
|------|------|------|
| 공식 Registry | Anthropic 주도 공개 서버 목록 | registry.anthropic.com |
| 플랫폼 내장 | IDE·앱에 통합된 서버 목록 | Cursor, VS Code Extensions |
| 기업 내부 Registry | 사내 승인된 MCP 서버만 허용 | **기업 권장 패턴** |

> **기업 권고**: 공개 Registry 무분별 사용 지양, **내부 승인 Registry** 구성 후 화이트리스트 관리

---

## 4. 보안 고려사항

### 주요 위협 벡터

| 위협 | 설명 | 대응 |
|------|------|------|
| **프롬프트 인젝션** | MCP 서버가 반환하는 데이터에 악의적 지시 삽입 | 출력 검증, 샌드박스 실행 |
| **도구 권한 남용** | 도구 조합으로 의도치 않은 데이터 유출 | 최소 권한 원칙, Tool 스코프 제한 |
| **유사 도구 치환** | 신뢰된 도구를 악성 유사 도구로 대체 | 서버 서명·검증, Registry 화이트리스트 |
| **자격증명 집중** | MCP 서버가 다수 엔터프라이즈 서비스 자격증명 집중 보유 | Vault 통합, 자격증명 격리, 최소 권한 |
| **mcp-remote CVE-2025-6514** | 쉘 커맨드 인젝션으로 437,000+ 개발 환경 침해 | 패키지 버전 고정, 의존성 스캔 |

### 2026 MCP 로드맵 보안 강화 계획

- **OAuth 2.1 표준화**: 엔터프라이즈 IdP(Okta, Azure AD 등) 통합
- **멀티에이전트 인증**: 에이전트-to-에이전트 도구 호출 시 신뢰 체인 확립
- **서버 보안 등급**: Registry에 검증된 서버 보안 점수 표시

---

## 5. 기업 도입 패턴

### 패턴 1: 중앙 MCP 게이트웨이

```
[계열사 AI 앱들]
      │
      ▼
[LiteLLM MCP Gateway] ← 인증·접근제어·감사로그
      │
      ├── [내부 DB MCP Server]
      ├── [ERP API MCP Server]
      ├── [문서 검색 MCP Server]
      └── [공장 데이터 MCP Server]
```

- **장점**: 단일 제어 지점, 접근 통제, 감사 로그 중앙화
- **구현**: LiteLLM Proxy (MCP 엔드포인트) + 사내 승인 MCP 서버 Registry

### 패턴 2: 계열사별 MCP 서버 + 공통 Registry

- 계열사별 도메인 특화 MCP 서버 독립 운영
- 그룹 공통 Registry에 승인된 서버 목록 등록
- 다른 계열사 AI 앱이 Registry 참조하여 필요 서버 호출

### 패턴 3: 하이브리드 (로컬 + 원격)

- 민감 데이터 (생산 데이터, PII): stdio 또는 내부 HTTPS MCP 서버
- 범용 서비스 (웹 검색, 공개 API): 원격 Streamable HTTP 서버

---

## 6. AI-Ready Data 주제 매핑

| 코드 | 주제 | 커버 수준 | 설명 |
|------|------|-----------|------|
| D-2 | API/Tool 연계 (MCP) | ○ (핵심) | MCP가 D-2 주제의 표준 그 자체 |
| D-3 | Prompt/Harness 자산화 | △ | MCP Prompts 프리미티브로 Prompt 템플릿 배포 가능 |
| E-3 | AI 평가 데이터 | × | 해당 없음 |
| E-4 | Feedback Loop | △ | MCP Server를 통한 데이터 환류 경로 구성 가능 |

---

## 7. 산업 표준화 현황 (2026 기준)

| 플랫폼/기업 | MCP 지원 |
|------------|---------|
| Anthropic Claude | 완전 지원 (원조) |
| OpenAI ChatGPT | 지원 |
| Google Gemini | 지원 |
| Microsoft Copilot | 지원 |
| VS Code | 지원 (Extensions) |
| Cursor | 지원 (내장) |
| AWS Bedrock | 지원 |
| Linux Foundation | 거버넌스 이관 |

> MCP는 2026년 현재 AI 에이전트 Tool 연계의 **사실상 표준(de facto standard)**으로 자리잡음

---

## 8. 기업 도입 체크리스트

- [ ] MCP 서버 인벤토리 구축 (어떤 서비스를 LLM에 노출할 것인가)
- [ ] 내부 승인 MCP Registry 운영 (화이트리스트 기반)
- [ ] LiteLLM 또는 전용 게이트웨이로 중앙 MCP 엔드포인트 구성
- [ ] 각 MCP 서버에 최소 권한 원칙 적용
- [ ] 감사 로그: 어떤 에이전트가 어떤 도구를 언제 호출했는가 기록
- [ ] 의존성 취약점 스캔 (CVE-2025-6514 교훈)
- [ ] OAuth 2.1 기반 인증 계획 수립 (2026 MCP 표준 강화 대응)

---

## 출처

- https://modelcontextprotocol.io/specification/2025-03-26/basic/transports
- https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/
- https://www.digitalapplied.com/blog/mcp-adoption-statistics-2026-model-context-protocol
- https://www.mirantis.com/blog/securing-model-context-protocol-for-mass-enterprise-adoption/
- https://www.sentinelone.com/cybersecurity-101/cybersecurity/mcp-security/
- https://guptadeepak.com/the-complete-guide-to-model-context-protocol-mcp-enterprise-adoption-market-trends-and-implementation-strategies/
- https://www.cdata.com/blog/2026-year-enterprise-ready-mcp-adoption
- https://blog.fka.dev/blog/2025-06-06-why-mcp-deprecated-sse-and-go-with-streamable-http/
- https://dev.to/x4nent/complete-guide-to-mcp-model-context-protocol-in-2026-architecture-implementation-and-4a11
- https://greptime.com/blogs/2026-05-09-opentelemetry-genai-semantic-conventions
- https://opentelemetry.io/blog/2026/genai-observability/
