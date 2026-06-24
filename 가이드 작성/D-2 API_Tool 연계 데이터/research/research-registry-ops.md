# D-2 API/Tool 연계 데이터 — 리서치 (등록소·위험도·호출 로그·버전)

작성일: 2026-06-24 · 검증 기준일: 2026-06 (MCP 레지스트리·툴링은 빠르게 변하므로 URL 라이브 여부 직접 확인함)

> 이 문서의 관점 고정: **에이전트를 "만드는 법"이 아니라, 에이전트가 외부 시스템·도구를 안전하게 호출하도록 떠받치는 "데이터/자산"을 준비·관리·거버넌스하는 법**이다. 즉 관리 대상은 ① 도구 명세 등록소(Tool spec registry), ② 도구별 위험 메타데이터(risk metadata) + 승인 규칙, ③ 호출 로그 스키마(call-log schema), ④ 명세 버전·오류 규칙이다. 가드레일 엔진·에이전트 구현 자체는 이 주제 밖이다.

---

## 1. Tool Registry / 명세 등록소 — "도구 명세가 사는 데이터 저장소 + 버전 관리"

### 핵심 내용
- 여러 에이전트가 같은 도구를 **일관되게 발견·호출**하려면, 도구 명세(이름·설명·입력/출력 스키마·엔드포인트·버전)가 흩어져 있으면 안 되고 **한 곳에 등록·검색·버전관리**되어야 한다. 이 "한 곳"이 등록소다.
- 등록소는 두 계열로 본다.
  - **(가) MCP 레지스트리/서버 디렉터리** — 에이전트가 붙을 수 있는 MCP 서버(=도구 묶음)의 메타데이터 목록. "MCP 서버용 앱스토어"에 비유된다. **메타데이터(패키지 정보)만 보관하고, 코드/바이너리는 보관하지 않는다**는 점이 핵심(=명세 카탈로그). 공식 레지스트리는 REST API + OpenAPI 스펙을 제공해 다른 레지스트리/호스트가 같은 인터페이스를 구현할 수 있게 한다. 2026-03 기준 약 3,012개 서버 등록(반년 전 ~2,500개에서 증가). 운영체는 Anthropic·GitHub·PulseMCP·Microsoft 등.
  - **(나) 기업 API 카탈로그 / API 게이트웨이 / 개발자 포털** — 사내에서 "호출 가능한 API"를 **등록·문서화·접근통제·거버넌스**하는 기존 인프라. 게이트웨이는 호출의 단일 관문(인증·레이트리밋·로깅)을, 개발자 포털/서비스 카탈로그는 "어떤 API가 있고 누가 쓸 수 있나"의 등록·검색을 맡는다. 에이전트 시대엔 이 카탈로그가 "에이전트가 부를 수 있는 도구"의 정본 목록 역할로 확장된다(Kong·Apigee 모두 MCP 서버/AI 트래픽까지 카탈로그·거버넌스 대상에 포함).

### 대표 솔루션·표준 (공식 URL)
- **공식 MCP 레지스트리(Official MCP Registry)** — 공개 MCP 서버 메타데이터 중앙 저장소. 서버 메타데이터 + 버전("최신 버전만 보기" 기능 확인) 관리. https://registry.modelcontextprotocol.io/ (라이브) · 소개 https://modelcontextprotocol.io/registry/about · 코드(커뮤니티 운영 레지스트리 서비스) https://github.com/modelcontextprotocol/registry
- **Kong Konnect — Service Catalog / Dev Portal** — 조직 내 모든 서비스·API의 중앙 카탈로그. 게이트웨이 뒤가 아닌 서비스까지 문서화, 미등록(shadow) API 발견, 스코어카드로 거버넌스 강제. https://konghq.com/products/kong-konnect/features/api-service-catalog · 개발자 포털 https://konghq.com/products/kong-konnect/features/developer-portal · 카탈로그 문서 https://developer.konghq.com/catalog/apis/
- **Google Apigee API hub** — 배포 위치와 무관하게 조직의 모든 API를 한 카탈로그로 등록·검색·의존성 추적·명세 린팅·거버넌스. https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub · API 등록 가이드 https://docs.cloud.google.com/apigee/docs/apihub/quickstart-api
- **AWS API Gateway** — REST/HTTP API를 생성·배포하고 **스테이지(stage: dev/prod/v2 등)**로 버전·라이프사이클 관리. 배포 스냅샷 + 스테이지 경로 조합으로 "어느 버전을 호출하게 할지" 통제. https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html · 스테이지 https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-stages.html

### 제조 적용 메모 (두산 계열사)
- 사내 MES·ERP·PLM·품질시스템·설비 API가 부서·시스템별로 흩어져 있으면 에이전트가 같은 기능을 중복·오호출한다. **"도구 명세 등록소"를 정본으로 두고**(사내 API는 API hub/Service Catalog, MCP화한 도구는 사내 MCP 레지스트리), 항목은 도구명·한 줄 설명·입력/출력·엔드포인트·소유부서·버전으로 통일.
- 외부 공개 MCP 레지스트리는 **메타데이터만** 모은 곳이므로 그대로 사내 정본으로 쓰지 말고, 사내 게이트웨이/카탈로그를 정본으로 두고 검증된 도구만 등록(공급망·shadow API 리스크 관리).
- 인접 주제 포인터: 도구 명세의 항목·의미 표준화는 [A-2 메타데이터], 무엇을 정본으로 등록할지는 [A-1 데이터 카탈로그]와 경계 공유.

---

## 2. Tool 위험도 분류(Risk classification) & 사람 승인(Human-in-the-loop) 끼우기 — "명세에 위험 메타데이터 + 승인 규칙을 붙인다"

### 핵심 내용
- 도구는 **부작용(side-effect) 크기로 분류**한다. 권장 4단계:
  - **조회(read-only)** — 데이터만 읽음. 부작용 없음 → 자동 허용.
  - **추천(recommend)** — 안을 제시하지만 시스템을 바꾸지 않음 → 대체로 자동, 단 출력 책임 표시.
  - **실행/쓰기(execute/write)** — 기록 변경·워크플로 트리거·파일 수정 등 시스템 상태를 바꿈 → **사람 승인(confirmation gate) 후 실행**.
  - **외부 전송(external-send)** — 메일·메시지·발주 등 조직 밖으로 나감(되돌리기 어려움) → **사람 승인 필수**, 가장 높은 위험.
- 이 분류는 **도구 명세에 붙는 위험 메타데이터(risk tier)**로 관리하고, "이 tier 이상은 승인 필요"라는 **승인 규칙(approval rule)**을 데이터로 정의한다. (가드레일 엔진을 만드는 게 아니라, *명세에 등급·규칙을 채워 넣는* 작업이 D-2 범위.)
- OWASP는 이 위험을 **과도한 자율성/권한(Excessive Agency)**으로 정식화하고, 완화책으로 **최소권한(least privilege)·도구 최소화·고위험 행동에 사람 승인(human-in-the-loop) 끼우기**를 1순위로 제시한다. (예: 메일 "초안"까지만 에이전트가 만들고 발송 전 사람이 확인.)
- 에이전트 프레임워크의 일반 패턴도 동일하다 — **read 도구는 자동, write 도구는 인터럽트(interrupt)로 멈춰 사람이 승인/수정/거부**. LangGraph의 HITL 미들웨어가 도구별로 승인 정책을 다르게 거는 대표 예(write_file=중단, read_data=자동). 이는 "도구를 위험도로 분류하고 그에 맞는 승인 규칙을 건다"는 명세-데이터 관점과 정확히 맞물린다.

### 대표 표준·근거 (공식 URL)
- **OWASP Top 10 for LLM Applications (2025) — LLM06:2025 Excessive Agency** — 위험도 분류·사람 승인의 1차 근거. 세 뿌리(과도한 기능/권한/자율) + 완화책(최소권한·고위험 행동 사람 승인·활동 로깅). 공식(OWASP GenAI Security Project): https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ (라이브) · 목록 https://genai.owasp.org/llm-top-10/ · OWASP 재단 프로젝트 페이지 https://owasp.org/www-project-top-10-for-large-language-model-applications/ · 2025 PDF https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf
  - **주의(번호 혼동)**: 2025판 공식 번호는 **LLM06 = Excessive Agency**, **LLM08 = Vector and Embedding Weaknesses**다. 일부 블로그가 LLM08로 잘못 표기하니 공식 genai.owasp.org 번호를 쓸 것.
- **NIST AI RMF (AI Risk Management Framework) + Generative AI Profile(NIST AI 600-1)** — 위험을 거버넌스·관리하는 상위 프레임워크 포인터(분류·통제를 조직 리스크관리에 정렬). 메인 https://www.nist.gov/itl/ai-risk-management-framework · GenAI Profile https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence · 본문 PDF https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **LangChain/LangGraph — Human-in-the-loop** (도구별 승인 정책·인터럽트 패턴의 구체 레퍼런스, "엔진"이 아니라 *분류→규칙* 패턴 근거로 인용): https://docs.langchain.com/oss/python/langchain/human-in-the-loop

### 제조 적용 메모 (두산 계열사)
- 도구 명세 등록 시 **위험등급 열(조회/추천/실행/외부전송)**과 **승인필요 여부·승인자**를 필수 항목으로 둔다. 예: "재고 조회"=조회·자동 / "공정 파라미터 변경"=실행·반장 승인 / "협력사 발주 메일"=외부전송·구매팀장 승인.
- 되돌리기 어려운 설비 제어·발주·대외 통지는 무조건 외부전송/실행 등급으로 묶어 사람 승인 게이트를 명세에 명시. 라벨이 곧 운영 규칙이 되게 한다.
- 데이터 준비 관점 유지: 여기서 만드는 산출물은 "승인 시스템"이 아니라 **도구별 위험등급·승인규칙이 채워진 명세 표**다.

---

## 3. Tool Call Log(호출 기록) 스키마 — "감사·디버깅용 호출 로그를 무엇으로 채울까"

### 핵심 내용
- 에이전트가 도구를 부를 때마다 **누가·언제·무엇을·어떻게 불렀고 결과가 무엇인지**를 한 건씩 구조화해 남긴다. 권장 필드:
  - **timestamp**(호출 시각), **caller/agent id**(부른 에이전트·세션·사용자), **tool name + version**(도구명과 버전), **input args**(입력 인자), **output/result**(결과), **success/failure**(성공·실패), **error code/type**(실패 시 오류 코드·유형), **latency/duration**(소요 시간). 필요 시 승인 여부·승인자(2장 연계)도 함께.
- **왜**: ① 감사(audit)·추적성 — 누가 무엇을 실행했는지 사후 확인(OWASP도 활동 로깅을 손상-한정 통제로 명시), ② 디버깅 — 오호출·실패 원인 추적, ③ 개선 입력. **단, 로그를 *모아 분석해 개선*하는 활동은 E-4(피드백·개선 데이터)의 주제다 — D-2는 "어떤 필드로 로그를 남길지(스키마)"까지만** 다룬다.
- 민감정보 주의: 입력/출력 전문을 인덱싱되는 속성에 통째로 넣는 것은 안티패턴. 내용은 별도(이벤트/본문) 영역에 두고, 수집 단계에서 필터·드롭 가능하게(=비식별·접근권한은 [F-4]).

### 관례·표준 (공식 URL)
- **OpenTelemetry — GenAI Semantic Conventions** (span/trace로 LLM·도구 호출을 표준 필드로 기록하는 일반 관례). 도구 실행 스팬·속성 정의: 작업명 `gen_ai.operation.name`(예: `execute_tool`), 도구 `gen_ai.tool.name`·`gen_ai.tool.type`·tool call id, 토큰 `gen_ai.usage.input_tokens`/`output_tokens`, 오류 `error.type`, 스팬 이름은 `{operation} {name}`(예: `execute_tool web_search`) 형식. 입력/출력 전문은 속성이 아니라 이벤트로.
  - **중요(URL 이동)**: 예전 경로 `opentelemetry.io/docs/specs/semconv/gen-ai/...`는 "이전됨" 안내만 뜬다. **현재 정본은 별도 저장소**: https://github.com/open-telemetry/semantic-conventions-genai (라이브, MCP 포함 명시) · 개념 소개(블로그) https://opentelemetry.io/blog/2026/genai-observability/
- (참고) 구조화 로깅 일반 원칙은 OpenTelemetry 로그/스팬 모델을 따르되, 위 GenAI 컨벤션이 LLM·도구 호출에 특화된 필드 셋을 제공.

### 제조 적용 메모 (두산 계열사)
- 호출 로그 스키마를 **공통 표(필드·의미·예시값·필수여부)**로 표준화해 모든 에이전트·도구가 같은 형식으로 남기게 한다. 최소 필드: 시각·에이전트/사용자·도구명+버전·입력·결과·성공실패·오류코드·소요시간(+승인자).
- 설비/품질 등 민감 데이터가 인자·결과에 실리므로, 전문 보관 범위·마스킹은 [F-4 데이터 접근권한·비식별]과 함께 설계. 로그 보존기간·접근권한도 명세에 같이 적는다.
- "로그로 무엇을 개선할지"(이상 호출 탐지, 도구 성능 개선)는 본 가이드에서 깊이 다루지 않고 [E-4]로 포인터만.

---

## 4. Versioning & 오류 관리 — "명세가 바뀌어도 에이전트가 오호출하지 않게"

### 핵심 내용
- 도구/API 명세가 바뀌면(인자 추가, 동작 변경) 옛 방식으로 부르던 에이전트가 깨진다. 그래서 **버전을 의미 있게 매기고**, **하위호환(backward compatibility)**을 지키며, **지원 종료(deprecation)는 예고**한다.
- **시맨틱 버저닝(Semantic Versioning, SemVer) X.Y.Z**: 하위호환 깨는 변경=메이저(X)↑, 하위호환 기능 추가=마이너(Y)↑, 버그픽스=패치(Z)↑. "공개 API를 선언해야 하며, 한 번 릴리스한 버전 내용은 바꾸지 않는다"가 핵심 규칙 → 에이전트가 "어떤 버전을 부르는지"로 호환을 판단할 수 있게 한다.
- **MCP의 버전 방식은 날짜형 `YYYY-MM-DD`** — "마지막으로 하위호환을 깬 날짜"를 뜻한다. 하위호환 변경이면 버전을 올리지 않음(점진 개선 + 상호운용 유지). 현재 버전 2025-11-25(차기 RC 2026-07-28). **버전 협상(negotiation)**은 초기화 단계에서 클라이언트·서버가 한 버전에 합의하며, 합의 실패 시 명확한 오류로 연결을 안전 종료. **deprecation 정책**: 폐기 예정 기능은 마이그레이션 경로를 문서화하고 최소 12개월(예외 시 90일) 유지 후 제거.
- 오류 관리: 호출 실패 시 표준 오류코드/유형을 남기고(3장 로그의 error code/type), 버전 불일치는 협상 단계에서 거르며, 폐기 도구는 명세 등록소에서 deprecated로 표기해 신규 호출을 막는다.

### 표준 (공식 URL)
- **Semantic Versioning 2.0.0** — https://semver.org/ (라이브) · 스펙 저장소 https://github.com/semver/semver
- **MCP Versioning** — 날짜형 버전·하위호환·협상·deprecation 정책 명시. https://modelcontextprotocol.io/specification/versioning (라이브) · 기능 수명주기/폐기 정책 https://modelcontextprotocol.io/community/feature-lifecycle
- (게이트웨이 측 버전 관리) AWS API Gateway 스테이지(위 1장), Apigee/Kong의 버전·라이프사이클 기능으로 "옛 버전 유지 + 새 버전 병행" 구현.

### 제조 적용 메모 (두산 계열사)
- 도구 명세 등록 항목에 **버전·하위호환 여부·폐기예정일·대체 도구**를 넣는다. 사내 API는 SemVer, MCP화 도구는 날짜형이 자연스러우니 혼용하되 등록소에서 일관 표기.
- 메이저 변경(인자·동작 변경) 시 **옛 버전을 일정 기간 병행 유지**하고 폐기를 예고해, 에이전트·인터페이스가 따라올 시간을 준다. 폐기 도구는 등록소에서 deprecated 표시로 신규 연결 차단.

---

## 참고 URL 목록 (라이브 여부 표기 — 2026-06 확인)

### Tool Registry / 등록소
- 공식 MCP 레지스트리 https://registry.modelcontextprotocol.io/ — 라이브(운영, 사실상 preview 단계로 알려짐)
- MCP 레지스트리 소개 https://modelcontextprotocol.io/registry/about — 라이브
- MCP 레지스트리 코드(GitHub) https://github.com/modelcontextprotocol/registry — 라이브
- Kong Konnect Service Catalog https://konghq.com/products/kong-konnect/features/api-service-catalog — 라이브
- Kong Dev Portal https://konghq.com/products/kong-konnect/features/developer-portal — 라이브
- Kong API 카탈로그 문서 https://developer.konghq.com/catalog/apis/ — 라이브
- Apigee API hub https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub — 라이브
- Apigee API 등록 가이드 https://docs.cloud.google.com/apigee/docs/apihub/quickstart-api — 라이브
- AWS API Gateway 배포 https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html — 라이브
- AWS API Gateway 스테이지 https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-stages.html — 라이브

### 위험도 분류 & 사람 승인
- OWASP LLM06:2025 Excessive Agency (공식) https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ — 라이브
- OWASP LLM Top 10 목록 https://genai.owasp.org/llm-top-10/ — 라이브
- OWASP 재단 프로젝트 페이지 https://owasp.org/www-project-top-10-for-large-language-model-applications/ — 라이브
- OWASP 2025 PDF https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf — 라이브
- NIST AI RMF 메인 https://www.nist.gov/itl/ai-risk-management-framework — 라이브
- NIST GenAI Profile https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence — 라이브
- NIST AI 600-1 PDF https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf — 라이브
- LangChain/LangGraph Human-in-the-loop https://docs.langchain.com/oss/python/langchain/human-in-the-loop — 라이브

### 호출 로그 스키마
- OpenTelemetry GenAI Semantic Conventions (현 정본 저장소) https://github.com/open-telemetry/semantic-conventions-genai — 라이브
- OpenTelemetry GenAI 옵저버빌리티 소개 https://opentelemetry.io/blog/2026/genai-observability/ — 라이브
- (이전 경로 https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/ — "이전됨" 안내만, 정본 아님)

### 버전 & 오류 관리
- Semantic Versioning 2.0.0 https://semver.org/ — 라이브
- SemVer 스펙 저장소 https://github.com/semver/semver — 라이브
- MCP Versioning https://modelcontextprotocol.io/specification/versioning — 라이브
- MCP 기능 수명주기/폐기 정책 https://modelcontextprotocol.io/community/feature-lifecycle — 라이브
