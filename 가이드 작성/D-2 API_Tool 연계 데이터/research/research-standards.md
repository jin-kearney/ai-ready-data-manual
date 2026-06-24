# D-2 API/Tool 연계 데이터 — 명세 표준 리서치

> 조사 관점 고정: 이 문서는 **AI 에이전트가 외부 시스템을 안전하게 호출하도록 "명세 데이터(Tool 설명·입력/출력 스키마 등)를 준비·표준화하는 법"**을 다룬다. "에이전트를 만드는 법"이 아니다. 아래 표준들은 모두 *Tool/API를 어떻게 데이터로 기술하는가*의 규약이다.
>
> 조사일: 2026-06-24. 버전·"latest"는 빠르게 바뀌므로 **PoC 시점에 재확인** 표시를 붙였다.

핵심 한 줄: 에이전트가 읽는 Tool 명세는 결국 **`이름(name) + 설명(description) + 입력/출력 스키마(JSON Schema)`** 세 가지로 수렴한다. MCP는 이 명세를 에이전트↔도구 사이에 노출·교환하는 *프로토콜*, OpenAPI는 기존 REST API를 기술하는 *문서 표준*, JSON Schema는 두 표준이 공통으로 깔고 쓰는 *타입·형태 언어*다.

---

## 1. MCP (Model Context Protocol, 모델 컨텍스트 프로토콜)

### 정의
LLM 애플리케이션과 외부 데이터·도구를 연결하는 **개방형 표준 프로토콜**(Anthropic 주도, 2024-11 공개). AI 애플리케이션(호스트)이 MCP 서버에 연결해 그 서버가 노출하는 **도구(Tools)·리소스(Resources)·프롬프트(Prompts)**를 표준 방식으로 발견·호출한다. "프로그래밍 언어 생태계의 표준을 LSP가 만들었듯, AI 도구 연동의 표준을 만든다"는 위치. 컨텍스트 교환 *프로토콜*만 규정하며 LLM을 어떻게 쓸지는 규정하지 않는다.

### 핵심 개념·필드
- **3주체 구조**: 호스트(Host, AI 앱 예: Claude Code·VS Code) ─ 클라이언트(Client, 서버당 1개 연결) ─ 서버(Server, 컨텍스트·도구 제공). 메시지 형식은 **JSON-RPC 2.0**.
- **서버가 노출하는 3가지(primitives)**: **Tools**(모델이 실행하는 함수 — API 호출·DB 조회 등), **Resources**(읽을 데이터·문맥), **Prompts**(재사용 프롬프트 템플릿). 발견은 `*/list`, 실행은 `tools/call`.
- **Tool 정의에 들어가는 필드**(D-2의 핵심 — 이게 "준비할 명세 데이터"):
  - `name` — 서버 네임스페이스 내 고유 식별자(예: `weather_current`, `calculator_arithmetic`). 명확한 네이밍 권장.
  - `title` — (선택) 사람이 읽는 표시용 이름.
  - `description` — 도구가 무엇을 하고 언제 쓰는지 사람이 읽는 설명. 모델이 호출 여부를 판단하는 근거.
  - `inputSchema` — **JSON Schema**로 기술한 입력 파라미터(타입·필수·허용값). 타입 검증과 문서 역할을 동시에.
  - `outputSchema` — (선택) 구조화 출력의 JSON Schema. 있으면 서버는 이에 맞는 결과를 줘야 하고(MUST) 클라이언트는 검증해야 한다(SHOULD).
  - `annotations` — (선택) 도구 동작을 설명하는 부가 속성. **신뢰할 수 없는 서버의 annotation은 신뢰하지 말 것**(보안 주의).
- **도구를 서버가 노출하는 방식**(데이터 흐름):
  1. `tools/list` 요청 → 서버가 위 필드를 담은 `tools` 배열로 응답(도구 발견).
  2. `tools/call` 요청(`name` + `arguments`) → 서버가 `content` 배열(텍스트·이미지 등)로 결과 반환. 오류는 `isError: true` 또는 JSON-RPC 오류.
  3. 도구 목록이 바뀌면 `notifications/tools/list_changed` 알림(서버가 `listChanged: true` 선언 시).
- **전송(transport)**: ① stdio(로컬 프로세스) ② Streamable HTTP(원격, 인증은 OAuth 토큰·API 키 등 권장).
- **보안 원칙(명세에 명시)**: 도구는 임의 코드 실행이므로 ① 사용자 동의·통제, ② 호출 전 입력을 사용자에게 노출, ③ 서버는 모든 입력 검증·접근통제·레이트리밋. "사람이 개입(human in the loop)해 호출을 거부할 수 있어야 한다"가 SHOULD.

### 공식 URL
- 공식 사이트: https://modelcontextprotocol.io/ (confirmed-live)
- 최신 사양(stable): https://modelcontextprotocol.io/specification/2025-11-25 (confirmed-live) — **현행 안정 버전 = 2025-11-25**
- 사양 'latest' 별칭: https://modelcontextprotocol.io/specification/latest (별칭, latest 라벨은 변동 가능 — PoC 시 재확인)
- 아키텍처 개요(호스트/클라이언트/서버·tools/list·tools/call 예시 포함): https://modelcontextprotocol.io/docs/learn/architecture (confirmed-live)
- 사양·스키마 GitHub: https://github.com/modelcontextprotocol/modelcontextprotocol (confirmed-live)
- 공식 레지스트리(공개 MCP 서버 목록): https://registry.modelcontextprotocol.io/ (검색결과상 존재 — 직접 확인 안 함)

### 버전·상태 (PoC 시 재확인)
- **2025-11-25**: 현행 안정 사양(2024-11 첫 공개 이후 1주년 시점 릴리스). (confirm at PoC)
- **2026-07-28 릴리스 후보(Release Candidate)**: 공개 이후 최대 개정이라고 블로그가 예고 — *stateless 코어*, 서버 렌더 UI(MCP Apps), 장기 실행 작업(Tasks 확장) 등. 아키텍처 문서에도 **Tasks (Experimental)** 가 "지연 결과 회수·상태 추적용 durable 실행 래퍼"로 등장. **2026-06 기준 후보 단계이므로 채택 전 확정 여부 확인.** (confirm at PoC)
- 채택 현황: VS Code·Claude Desktop 등이 호스트로 동작, Sentry·파일시스템 등 다수 참조 서버 존재 — 사실상 업계 표준으로 확산 중(근거: 아키텍처 문서의 예시·레지스트리).

### 제조 적용 메모
- 두산 계열 ERP·MES·QMS를 에이전트가 호출하게 하려면, **각 시스템 동작을 "Tool 명세 데이터"로 만들어 MCP 서버가 `tools/list`로 노출**하는 형태가 표준 경로다. 준비할 산출물 = 도구별 `name·description·inputSchema(필수/타입/허용값)·outputSchema`.
- D-2의 데이터 준비 범위는 **"이 명세를 누가·어떻게 채우고·표준값을 어떻게 관리하는가"**까지. 에이전트 오케스트레이션·서버 구현 코드는 범위 밖(데이터 준비 관점 고정).
- `description`이 부실하면 에이전트가 도구를 잘못 고르므로, **설명문 자체가 품질 관리 대상 데이터**다(Anthropic 권장: 도구당 3~4문장 이상, 무엇을·언제·각 파라미터 의미·한계).

---

## 2. OpenAPI Specification (OpenAPI 사양, OAS)

### 정의
HTTP/REST API의 구조·문법을 **프로그래밍 언어와 무관하게 JSON 또는 YAML 문서로 기술하는 개방형 표준**(OpenAPI Initiative 관리, 옛 Swagger 사양). API 제공자→소비자에게 "이 API가 무엇을 받고 무엇을 돌려주는지"를 전달하는 계약서 역할.

### 핵심 개념·필드
- **Paths(경로) 객체**: 서버 URL에 붙는 엔드포인트(예: `/orders/{id}`).
- **Operation(오퍼레이션) 객체**: 경로별 HTTP 메서드(GET·POST·DELETE 등)와 그 동작.
- **Parameters(파라미터) 객체**: query·path·header·cookie 파라미터.
- **Request Body(요청 본문) 객체**: 들어오는 요청의 콘텐츠·스키마.
- **Responses(응답) 객체**: 상태코드별 응답·콘텐츠 타입.
- **Components / Schemas(재사용 스키마)**: 재사용 가능한 데이터 모델. **데이터 타입은 JSON Schema로 기술**.
- 부가: `operationId`(오퍼레이션 고유 식별자 — 도구 매핑 시 유용), `summary`·`description`(사람·모델이 읽는 설명), `tags`, `security`(인증 방식).

### 공식 URL
- OpenAPI Initiative 공식 사이트: https://www.openapis.org/ (confirmed-live)
- "What is OpenAPI" 설명: https://www.openapis.org/what-is-openapi (confirmed-live)
- 사양 허브: https://spec.openapis.org/oas/ (검색결과상 존재)
- 'latest' 사양(현재 3.2.0으로 해석됨): https://spec.openapis.org/oas/latest.html (confirmed-live)
- v3.2.0(현행 최신): https://spec.openapis.org/oas/v3.2.0.html (confirmed-live, 2025-09-19 공개)
- v3.1.0: https://spec.openapis.org/oas/v3.1.0.html (검색결과상 존재, 2021-02 공개)
- GitHub: https://github.com/OAI/OpenAPI-Specification (검색결과상 존재)

### 버전·상태 (PoC 시 재확인)
- **3.2.0** = 현행 최신(2025-09-19). 3.1의 JSON Schema 2020-12 정렬 위에 문서화·스트리밍·보안 기능을 추가한 기능 릴리스이며 **기존 3.1 문서는 그대로 동작**(하위호환). (confirm at PoC)
- **3.1.0**(2021-02): 데이터 타입을 **JSON Schema Draft 2020-12와 완전 정렬**한 분기점. 3.2도 "OAD의 각 문서는 JSON Schema Draft 2020-12에 따라 파싱돼야 한다(MUST)"고 규정. (confirm at PoC)
- 사내에선 보통 3.1을 쓰던 곳이 많음 — 버전은 도구 체인 호환성에 따라 PoC에서 확정.

### 제조 적용 메모
- 두산 계열 **기존 엔터프라이즈 API(ERP·MES·QMS)가 이미 OpenAPI 문서를 갖고 있다면**, 그것이 "API를 데이터로 기술한 1차 자산"이다. 이를 입력으로 **MCP Tool 명세로 감싸(wrap)** 에이전트에 노출하는 것이 자연스러운 경로(OpenAPI의 path+operation+schema → MCP tool의 name+description+inputSchema로 매핑).
- OpenAPI가 없는 레거시는 **먼저 OpenAPI 문서를 만들어 두는 것**이 D-2 데이터 준비의 첫 단계가 될 수 있다(나중에 도구 자동 생성·테스트·문서화에 모두 재사용).
- "데이터 준비" 산출물 = 시스템별 OpenAPI 문서(paths·schemas)와 그중 에이전트에 노출할 오퍼레이션 선별 목록.

---

## 3. JSON Schema (JSON 스키마)

### 정의
JSON 데이터의 **구조·필수 항목·타입·허용값을 선언하고 검증하는 표준 어휘(vocabulary)**. MCP의 `inputSchema`/`outputSchema`와 OpenAPI의 Schema가 **공통으로 깔고 쓰는 타입·형태 언어**다. 사양은 Core(기초)와 Validation(검증 키워드) 두 문서로 나뉜다.

### 핵심 개념·필드(검증 키워드)
- `type` — 값의 타입(`string`·`number`·`integer`·`boolean`·`object`·`array`·`null`).
- `properties` — 객체의 각 필드와 그 하위 스키마.
- `required` — 반드시 있어야 하는 필드 목록(= "필수 항목").
- `enum` — 허용되는 값의 집합(= "표준값 목록", 예: `["celsius","fahrenheit"]`).
- `items` / `prefixItems` — 배열 요소의 스키마(2020-12에서 `items`/`additionalItems` → `prefixItems`/`items`로 정리).
- 기타 자주 쓰는 것: `description`(필드 설명), `default`(기본값), `format`(형식 힌트 예: date-time), `minimum`·`maximum`, `$ref`(스키마 참조·재사용).

### 공식 URL
- 공식 사이트: https://json-schema.org/ (사이트 루트)
- 사양 페이지(현행 버전 명시): https://json-schema.org/specification (confirmed-live) — **현행 = Draft 2020-12**
- Draft 2020-12 인덱스: https://json-schema.org/draft/2020-12 (검색결과상 존재)
- 학습용 시작 가이드: https://json-schema.org/learn/getting-started-step-by-step (검색결과상 존재)

### 버전·상태 (PoC 시 재확인)
- **Draft 2020-12** = 현행 안정 버전(이전은 2019-09). 사양 페이지가 "현재 버전은 2020-12"라고 명시. (confirm at PoC)
- "Draft"라는 이름이지만 OpenAPI 3.1/3.2와 MCP가 채택한 사실상의 현행 표준. 정식 RFC화 진행 중이므로 명칭 변동 가능성은 PoC에서 확인.

### 제조 적용 메모
- D-2에서 **"항목 사전·필수/선택·허용값(표준값)"을 기계가 읽는 형태로 굳히는 수단**이 바로 JSON Schema다. 현업이 엑셀로 "이 입력은 필수, 이 코드값만 허용" 식으로 정해둔 규칙을 `required`·`enum`으로 옮기면 그대로 검증 가능한 명세가 된다.
- 같은 스키마 언어를 MCP·OpenAPI가 공유하므로, **한 번 정의한 입력/출력 스키마를 두 곳에서 재사용**할 수 있다(예: MES 작업지시 코드의 enum을 OpenAPI schema와 MCP inputSchema에 동일 적용).

---

## 4. LLM 함수 호출 / 도구 사용 규약 (Function Calling / Tool Use)

### 정의
모델에게 도구를 **`이름 + 설명 + JSON-Schema 파라미터`** 형태로 알려주면, 모델이 사용자 요청과 그 설명을 보고 호출 여부·인자를 판단해 **구조화된 호출(structured call)**을 돌려주는 방식. 벤더 중립적으로 거의 동일한 모양이며(이름·설명·파라미터 스키마), MCP의 Tool 정의도 이 모양을 그대로 따른다.

### 핵심 개념·필드 (Anthropic Claude 도구 사용 기준)
- 도구 정의 = `tools` 배열의 각 항목:
  - `name` — 도구 이름. 정규식 `^[a-zA-Z0-9_-]{1,64}$` 준수.
  - `description` — 무엇을·언제·어떻게 동작하는지 상세 설명(도구 성능을 좌우하는 가장 중요한 요소).
  - `input_schema` — **JSON Schema** 객체(`type`/`properties`/`required`/`enum` 등). MCP의 `inputSchema`와 사실상 동일.
  - `input_examples` — (선택) 스키마에 맞는 입력 예시 배열(복잡한 도구 이해를 도움).
- 모델 응답: 호출이 필요하면 `tool_use` 블록(`name` + `input`)을 반환 → 앱이 실행 후 `tool_result`로 회신(client tool), 또는 Anthropic이 실행(server tool).
- `tool_choice`: `auto`(기본)·`any`(아무 도구나 강제)·`tool`(특정 도구 강제)·`none`(금지).
- `strict: true` 옵션 — 도구 호출이 스키마를 정확히 따르도록 보장(스키마 적합성).
- 설계 권장: 설명 상세화(3~4문장+), 관련 동작은 `action` 파라미터로 묶어 도구 수 줄이기, 서비스 접두사 네임스페이싱(`github_list_prs`·`slack_send_message`), 응답은 고신호 정보·안정 식별자만.

### 공식 URL
- Claude 도구 사용 개요: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview (confirmed-live)
- 도구 정의(필드·예시): https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools (confirmed-live)
- 에이전트용 도구 작성 가이드: https://www.anthropic.com/engineering/writing-tools-for-agents (인용 — 직접 확인 안 함)
- MCP 커넥터(Claude에서 MCP 서버 연결): https://platform.claude.com/docs/en/agents-and-tools/mcp-connector (인용 — 직접 확인 안 함)

### 버전·상태 (PoC 시 재확인)
- 도구 정의의 3대 필드(name·description·input_schema=JSON Schema)는 안정적. `input_examples`·`strict`·`tool_search` 등 부가 기능은 계속 추가되므로 세부는 PoC에서 확인. (confirm at PoC)
- OpenAI 등 타 벤더도 "function: name + description + parameters(JSON Schema)" 동일 골격 — 벤더 중립적으로 호환되는 사고틀.

### 제조 적용 메모
- 결론: **벤더가 무엇이든 준비할 데이터는 같다** — 도구의 `이름·설명·입력 스키마(필수/타입/허용값)`. 이 명세를 잘 써두면 Claude·MCP·OpenAPI 어디에도 옮겨 쓸 수 있다.
- "에이전트를 만든다"가 아니라 **"에이전트가 읽을 도구 설명·스키마를 데이터 자산으로 정비한다"**가 D-2의 일.

---

## 표준 간 관계 (MCP vs OpenAPI vs JSON Schema)

세 표준은 경쟁이 아니라 **층위가 다르다.** JSON Schema가 맨 아래 타입 언어, 그 위에 OpenAPI(REST API 문서)와 MCP(에이전트↔도구 프로토콜)가 각각 올라간다. Function Calling 규약은 MCP가 따르는 "도구를 모델에 알리는 모양" 그 자체다.

| 구분 | JSON Schema | OpenAPI Specification | MCP (Model Context Protocol) | LLM Function Calling |
|---|---|---|---|---|
| 한 줄 정의 | 데이터의 타입·필수·허용값을 선언·검증하는 어휘 | REST API를 문서로 기술하는 표준 | 에이전트↔도구를 잇는 개방형 프로토콜 | 도구를 모델에 알려 호출시키는 규약 |
| 무엇을 기술하나 | 값의 구조(`type`·`required`·`enum`) | API 경로·메서드·요청/응답 | 서버가 노출하는 Tools·Resources·Prompts | 도구 1개(name·description·params) |
| 층위 | 최하층(타입 언어) | API 문서 층 | 에이전트 연동 프로토콜 층 | 모델↔도구 인터페이스(MCP가 채택) |
| 핵심 식별/필드 | type·properties·required·enum·items | paths·operations·parameters·schemas·operationId | name·description·inputSchema·outputSchema | name·description·input_schema |
| 현행 버전 | Draft 2020-12 | 3.2.0 (3.1과 호환) | 2025-11-25 (2026-07-28 RC 진행) | 벤더별, 골격 공통 |
| 전송/형식 | JSON | JSON·YAML 문서 | JSON-RPC 2.0 (stdio·HTTP) | API 요청 본문(JSON) |
| 서로의 관계 | OpenAPI·MCP가 **공통으로 사용** | 데이터 타입에 JSON Schema 사용 | inputSchema/outputSchema에 JSON Schema 사용 | input_schema에 JSON Schema 사용 |

### 제조사가 "기존 시스템을 도구로 감쌀 때" 무엇을 언제 쓰나
- **이미 REST API가 있고 OpenAPI 문서가 있다 → OpenAPI를 입력으로 MCP Tool로 매핑.** path+operation+schema가 그대로 name+description+inputSchema 재료가 된다.
- **API는 있는데 OpenAPI 문서가 없다 → 먼저 OpenAPI 문서를 작성**(나중에 도구 생성·테스트·문서에 재사용). 이게 D-2 데이터 준비의 출발선이 될 수 있다.
- **에이전트가 직접 호출하게 하려면 → MCP 서버로 도구를 `tools/list`에 노출.** 표준 발견·호출·알림 경로를 그대로 쓴다.
- **입력 규칙(필수·허용 코드값)을 굳힐 때 → JSON Schema의 `required`·`enum`.** 현업 엑셀 규칙을 기계가 검증하는 명세로 옮기는 수단. MCP·OpenAPI 양쪽에서 동일 스키마 재사용.
- **벤더 종속 우려 → 도구의 이름·설명·입력 스키마만 잘 관리하면 벤더 중립.** Claude·MCP·OpenAPI 어디로도 이식 가능.

---

## 참고 URL 목록

확인 표기: [LIVE] = 이번 조사에서 직접 fetch해 내용 확인 / [검색] = 검색 결과에 URL이 나왔으나 직접 fetch 안 함.

### MCP
- https://modelcontextprotocol.io/ — 공식 사이트 [LIVE: 사양 페이지에서 참조 확인]
- https://modelcontextprotocol.io/specification/2025-11-25 — 현행 안정 사양(2025-11-25) [LIVE]
- https://modelcontextprotocol.io/specification/latest — 'latest' 별칭(라벨 변동 가능) [검색/별칭]
- https://modelcontextprotocol.io/docs/learn/architecture — 아키텍처·tools/list·tools/call 예시 [LIVE]
- https://github.com/modelcontextprotocol/modelcontextprotocol — 사양·스키마 저장소 [검색]
- https://registry.modelcontextprotocol.io/ — 공식 레지스트리 [검색]
- (MCP 도구 개념 — 명세 본문 내 `/specification/<date>/server/...` 경로로 제공; 위 아키텍처 문서가 동일 내용 포함)

### OpenAPI
- https://www.openapis.org/ — OpenAPI Initiative 공식 사이트 [LIVE]
- https://www.openapis.org/what-is-openapi — OpenAPI 정의 설명 [LIVE]
- https://spec.openapis.org/oas/latest.html — 'latest'(현재 3.2.0으로 해석) [LIVE]
- https://spec.openapis.org/oas/v3.2.0.html — v3.2.0 현행 최신(2025-09-19) [LIVE]
- https://spec.openapis.org/oas/v3.1.0.html — v3.1.0(2021-02) [검색]
- https://spec.openapis.org/oas/ — 사양 허브 [검색]
- https://github.com/OAI/OpenAPI-Specification — 저장소 [검색]

### JSON Schema
- https://json-schema.org/ — 공식 사이트 [검색/루트]
- https://json-schema.org/specification — 사양 페이지(현행 2020-12 명시) [LIVE]
- https://json-schema.org/draft/2020-12 — Draft 2020-12 인덱스 [검색]
- https://json-schema.org/learn/getting-started-step-by-step — 시작 가이드 [검색]

### LLM Function Calling / Tool Use (Anthropic)
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview — 도구 사용 개요 [LIVE]
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools — 도구 정의(필드·예시) [LIVE]
- https://www.anthropic.com/engineering/writing-tools-for-agents — 에이전트용 도구 작성 [검색]
- https://platform.claude.com/docs/en/agents-and-tools/mcp-connector — MCP 커넥터 [검색]

### 공통 기반(참조)
- https://www.jsonrpc.org/ — JSON-RPC 2.0(MCP 메시지 형식) [검색/명세 내 참조]
