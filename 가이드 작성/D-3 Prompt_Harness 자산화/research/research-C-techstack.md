# D-3 Prompt/Harness 자산화 — Tech Stack 리서치 (C 클러스터: 솔루션 검토)

> 작성일: 2026-06-24 | 리서치 범위: Prompt Management / Registry 솔루션, 명세·형식 표준, 선정 기준

---

## 1. 유형 개요

Prompt 자산을 **등록·버전관리·평가 연계**하는 도구는 크게 세 유형으로 나뉜다.

| 유형 | 특징 | 대표 제품 |
|---|---|---|
| **오픈소스 셀프호스트형** | 온프레미스 배포 가능, 라이선스 비용 없음, 운영 인력 필요 | Langfuse, Agenta, Helicone, Pezzo, Portkey(OSS) |
| **상용 SaaS형** | 즉시 사용, 관리 부담 없음, 외부 데이터 전송 | LangSmith, PromptLayer, Vellum(LLM DevOps 특화) |
| **평가 특화형** | Prompt 관리보다 eval/red-teaming 중심 | Promptfoo(MIT) |

> **주의**: Humanloop은 Anthropic에 인수되어 플랫폼을 종료(sunset) 중(2025년 기준). 고객사 마이그레이션 안내 중. 신규 도입 후보에서 제외.

---

## 2. 솔루션 비교표

### 2-A. 오픈소스 셀프호스트형

| 제품 | 한 줄 성격 | 라이선스 / 셀프호스트 | Prompt 버전관리·롤백 | Eval 연계 | 비개발자 UI 편집 | 가격(클라우드) |
|---|---|---|---|---|---|---|
| **Langfuse** | LLM Observability + Prompt 관리 통합 플랫폼 | MIT / Docker Compose·템플릿 지원 | ✅ 버전 자동 생성, `production`/`staging` 레이블로 환경 분리, 특정 버전 직접 호출 가능 | ✅ 트레이스와 Prompt 버전 연결, 성능 분석 | ✅ Langfuse UI에서 Prompt 생성·편집 가능 | Hobby 무료(50k units/월) → Core $29/월 → Pro $199/월 → Enterprise $2,499/월 |
| **Agenta** | Prompt 관리·평가·모니터링 통합 오픈소스 LLMOps | MIT / Docker Compose, 원격 호스트 지원 | ✅ 완전한 버전 히스토리, 브랜치·환경 관리, 프로덕션 배포 | ✅ LLM-as-Judge·내장 평가자·휴먼 평가(도메인 전문가 피드백) 모두 지원 | ✅ SME(Subject Matter Expert)가 코드 없이 Prompt 편집 가능한 UI 명시 제공 | Hobby 무료(2인·5k traces) → Pro $49/월(3인·10k traces) → Business $399/월 → Enterprise 별도 협의·셀프호스트 |
| **Helicone** | AI Gateway + 관찰성 + Prompt 버전관리 | Apache 2.0 / Docker Compose·Helm 차트·Kubernetes | ✅ "생산 데이터 기반 Prompt 버전관리", Gateway 통해 코드 수정 없이 배포 가능 | 공식 페이지에서 eval 연계 명시 없음 — 공식 문서 PoC 확인 권장 | 공식 페이지에서 비개발자 UI 편집 명시 없음 — 공식 문서 PoC 확인 권장 | GitHub 5.9k stars, 별도 클라우드 요금 구조 — 공식 pricing 페이지 확인 |
| **Pezzo** | 클라우드 네이티브 오픈소스 LLMOps (Prompt 설계·버전관리·모니터링) | Apache 2.0 / 셀프호스트 가능 | ✅ Prompt 버전관리·즉시 변경 배포 명시 | 비용·지연 최적화 연계 명시, eval 구체 기능 — 공식 문서 PoC 확인 권장 | 협업 도구 언급 있으나 비개발자 전용 UI 명시 없음 — 공식 문서 PoC 확인 권장 | 오픈소스 무료; GitHub 3.2k stars, 최근 릴리즈(v0.9.2, 2024.05) — 유지보수 속도 모니터링 권장 |
| **Portkey** | AI Gateway + Prompt 라이브러리 + 거버넌스 통합 플랫폼 | MIT / 셀프호스트 오픈소스(무료); 관리형 클라우드 별도 | ✅ Prompt 변경 시 자동 버전 생성, 구버전 전환(롤백) 가능, Prompt 템플릿·변수 지원 | 공식 페이지에서 eval 연계 구체 기능 명시 없음 — 공식 문서 PoC 확인 권장 | "Prompt Engineering Studio" UI 존재; 비개발자 전용 여부 — 공식 문서 PoC 확인 권장 | Developer 영구 무료(10k logs/월) → Production $49/월(100k logs) → Enterprise 별도; 셀프호스트 무료 |

### 2-B. 상용 SaaS형

| 제품 | 한 줄 성격 | 라이선스 / 셀프호스트 | Prompt 버전관리·롤백 | Eval 연계 | 비개발자 UI 편집 | 가격 |
|---|---|---|---|---|---|---|
| **LangSmith** | LLM 애플리케이션 추적·모니터링·평가·Prompt 관리 통합 플랫폼 | 비공개 / 셀프호스트·BYOC·관리형 클라우드 3가지 옵션 | ✅ Prompt Hub에서 태그·커밋·버전·컨텍스트 승격(promote) 지원; 커뮤니티 Prompt 허브 공유 가능 | ✅ Observability와 Eval 독립 사용 또는 통합 사용; LLM-as-Judge·코드 eval 지원 | 공식 페이지 명시 없음 — 공식 문서 PoC 확인 권장 | 개발 무료 → 유료 플랜 trace 볼륨 기반 과금; Enterprise 별도 |
| **PromptLayer** | Prompt CMS + eval 하네스 + 관찰성 통합 — AI 엔지니어링팀 협업 레이어 | SaaS(셀프호스트 옵션 있음 — 세부 조건 공식 확인 권장) | ✅ Prompt Registry에서 버전·레이블·릴리즈 상태 관리; 코드 변경 없이 버전 승격(release labels) | ✅ eval 하네스 내장, A/B 테스트·성능 기반 프로덕션 라우팅 | ✅ "도메인 전문가가 코드베이스 없이 협업" 명시 — 비개발자 UI 편집 지원 | "Sign up for free" 무료 시작; Enterprise는 Sales 문의 — 공식 pricing 페이지 확인 |
| **Vellum** (LLM DevOps 플랫폼) | ⚠️ 현재 공식 사이트가 개인 AI 비서 제품으로 전환된 것으로 보임 — 기존 Vellum AI(LLM 앱 개발 플랫폼)와 별개 제품일 가능성. **공식 확인 필수.** | 공식 확인 필요 | 공식 확인 필요 | 공식 확인 필요 | 공식 확인 필요 | 공식 확인 필요 |

> **Vellum 주의**: 2025~2026년 시점 공식 사이트(https://www.vellum.ai)가 AI 비서 플랫폼(개인용)으로 표시됨. 기존 LLM 개발 플랫폼 Vellum과 동일 제품인지 혼동 가능 — **도입 전 반드시 공식 페이지 재확인** 요망.

### 2-C. 평가·보안 테스트 특화형 (참고)

| 제품 | 성격 | 비고 |
|---|---|---|
| **Promptfoo** | LLM 평가·레드팀·보안 취약점 스캔 CLI 도구 | MIT 라이선스, OpenAI 인수, 20.6k stars; Prompt 버전관리 X — **E-3(평가) 클러스터 소관** |
| **Dify** | 오픈소스 LLM 앱 개발 플랫폼, Prompt IDE 포함 | Apache 2.0 기반 커스텀 라이선스, 146k stars; Prompt 버전관리보다 앱 워크플로 구축 중심 |

---

## 3. 명세·형식 표준

### 3-1. 출력 형식 강제 표준

Prompt 자산화에서 Prompt는 단순 텍스트가 아니라 **"입력 템플릿 + 출력 스키마"의 쌍**으로 구성된다. 출력 형식 강제를 위한 주요 표준:

| 표준 | 설명 | 출처 |
|---|---|---|
| **JSON Schema** | LLM 출력이 반드시 준수해야 할 JSON 구조를 정의하는 선언적 명세. 필드명·타입·필수 여부를 정의해 출력 파싱 오류를 방지. | https://json-schema.org |
| **OpenAI Structured Outputs** | `response_format: {type: "json_schema", strict: true}` 옵션으로 JSON Schema 준수를 모델 수준에서 강제. Python Pydantic·JS Zod로 스키마 정의 후 자동 변환 지원. | https://platform.openai.com/docs/guides/structured-outputs |
| **Anthropic 도구 정의(Tool Use)** | Claude API의 `tools` 파라미터에 JSON Schema 형식으로 도구 입력 스키마 정의. `strict: true` 추가 시 스키마 완전 준수 보장. 형식: `{name, description, input_schema(JSON Schema)}` | https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview |
| **Function Calling(범용)** | OpenAI, Anthropic, Google 등 주요 LLM 공급사가 채택한 도구 호출 표준 패턴. 입력 스키마를 JSON Schema로 정의해 LLM이 구조화된 호출을 생성. | 각 공급사 공식 API 문서 |

### 3-2. Prompt 템플릿·형식 표준

| 표준/형식 | 설명 | 비고 |
|---|---|---|
| **Jinja2 템플릿** | `{{variable}}` 방식의 동적 변수 치환. Langfuse·Agenta·PromptLayer 등 다수 플랫폼이 Jinja2 또는 유사 문법 지원. | https://jinja.palletsprojects.com |
| **OpenAI Messages 형식** | `[{role: "system"/"user"/"assistant", content: "..."}]` 배열 구조. 사실상 업계 표준 메시지 포맷. 주요 Prompt 관리 도구 모두 지원. | https://platform.openai.com/docs/api-reference/messages |
| **Anthropic Messages 형식** | `system` + `messages [{role: "user"/"assistant", content: "..."}]` 구조. OpenAI와 유사하나 `system` 파라미터가 분리. | https://docs.anthropic.com/en/api/messages |
| **.prompt 파일 형식** | 특정 IDE 확장(예: VS Code LangChain 확장)에서 사용하는 Prompt 파일 형식. 업계 표준으로 확립되지는 않음. | 공식 표준 없음 — 플랫폼별 상이 |

### 3-3. D-2와의 경계 (Tool 명세)

- **Tool 명세(OpenAPI·MCP)는 D-2(API/Tool 연계 데이터) 소관.**
- D-3의 Harness는 Tool 명세를 **참조**하되, Tool 정의 자체를 관리하지 않는다.
- D-3에서 관리하는 것: Harness가 Tool을 어떤 순서·조건으로 호출하는지 기술하는 **Prompt 흐름 정의**와 Tool 호출 응답을 파싱하는 **출력 스키마(JSON Schema)**.
- 경계 요약: D-2 = Tool의 존재·계약(what/how it works), D-3 = Tool을 포함한 Agent 행동 스크립트(when/why to call it).

---

## 4. 솔루션 선정 기준

제조 현업(두산 계열사 등) 환경에서 Prompt Registry 도구를 선정할 때 고려해야 할 기준:

| 기준 | 설명 | 제조 보안 맥락 |
|---|---|---|
| **셀프호스트(온프레미스) 가능 여부** | Prompt에 내부 업무 지식·설비 정보가 포함될 경우 외부 SaaS로 전송 불가. | 최우선. Docker Compose·Helm 기반 내부 배포 필수. |
| **버전관리·롤백** | Prompt 변경 후 문제 발생 시 즉각 이전 버전으로 되돌릴 수 있는가. | AI 운영 안정성 핵심. `production`/`staging` 레이블 환경 분리 여부 확인. |
| **평가(Eval) 연계 — E-3 연동** | 새 버전 배포 전 자동 평가를 연계할 수 있는가. | 품질 보증 없이 Prompt 갱신 불가한 규칙 수립 시 필수. |
| **비개발자(현업 SME) 편집 가능** | 제조 공정 도메인 전문가(품질·생산 담당)가 코드 없이 Prompt를 수정·검토할 수 있는가. | Agenta·PromptLayer가 이 점을 명시. 현업 참여 구조 설계에 중요. |
| **접근 권한(RBAC)** | Prompt를 누가 읽고(Read), 편집하고(Write), 승인·배포(Deploy)하는지 역할별 권한 분리. | Agenta Business 플랜 이상·LangSmith Enterprise 등에서 RBAC 지원. 공식 확인 권장. |
| **기존 데이터 플랫폼·카탈로그 연계** | 카탈로그(A-1)·메타데이터(A-2)·Lineage(C-3) 시스템과 API 또는 webhook으로 연결 가능한가. | 완전 자동화 연계보다 webhook/REST API 유무 먼저 확인. |
| **오픈소스 지속성·커뮤니티 활동** | 프로젝트가 충분히 활성화되어 있는가. 인수·종료 리스크. | Humanloop 종료 사례 참고. GitHub stars/커밋 빈도·릴리즈 주기 확인. |

---

## 5. 도구별 셀프호스트 가능 여부 요약

| 도구 | 셀프호스트 | 라이선스 | 제조 보안 적합성 |
|---|---|---|---|
| Langfuse | ✅ Docker Compose·Helm | MIT | 높음 |
| Agenta | ✅ Docker Compose | MIT | 높음 |
| Helicone | ✅ Docker Compose·Helm/K8s | Apache 2.0 | 높음 |
| Portkey (OSS) | ✅ 셀프호스트 무료 | MIT | 높음 |
| Pezzo | ✅ 가능 | Apache 2.0 | 중간 (유지보수 속도 모니터링 권장) |
| LangSmith | ✅ BYOC·셀프호스트 옵션 | 비공개(상용) | 중간 (라이선스 비용 발생) |
| PromptLayer | △ 셀프호스트 옵션 존재 (세부 조건 공식 확인 요망) | 비공개(상용) | 조건부 |
| Promptfoo | ✅ CLI, 로컬 실행 | MIT | 높음 (단, eval 전용) |

---

## 6. 출처 목록 (제품명 · URL · 성격)

| # | 제품/표준 | 공식 URL | 성격 |
|---|---|---|---|
| 1 | Langfuse | https://langfuse.com | OSS LLM Observability + Prompt 관리 |
| 2 | Langfuse 가격 | https://langfuse.com/pricing | 가격 티어 |
| 3 | Langfuse Prompt 시작 가이드 | https://langfuse.com/docs/prompts/get-started | Prompt 버전관리·레이블 |
| 4 | Agenta | https://agenta.ai | OSS LLMOps + Prompt 관리·평가 |
| 5 | Agenta GitHub | https://github.com/Agenta-AI/agenta | MIT 라이선스·셀프호스트 확인 |
| 6 | Agenta 가격 | https://agenta.ai/pricing | 가격 티어·셀프호스트 조건 |
| 7 | Helicone | https://helicone.ai | OSS AI Gateway + Prompt 버전관리 |
| 8 | Helicone GitHub | https://github.com/Helicone/helicone | Apache 2.0·셀프호스트 확인 |
| 9 | Portkey | https://portkey.ai | OSS AI Gateway + Prompt 라이브러리 |
| 10 | Portkey Prompt Library | https://portkey.ai/docs/product/prompt-library | Prompt 버전관리·변수·액세스 제어 |
| 11 | Portkey 가격 | https://portkey.ai/pricing | 가격 티어·셀프호스트 무료 |
| 12 | Pezzo GitHub | https://github.com/pezzolabs/pezzo | Apache 2.0·OSS LLMOps |
| 13 | LangSmith | https://www.langchain.com/langsmith | 상용 LLM Observability + Prompt Hub |
| 14 | LangSmith Prompt Engineering | https://docs.langchain.com/langsmith/prompt-engineering | Prompt 버전·커밋·태그 |
| 15 | PromptLayer | https://www.promptlayer.com | 상용 Prompt CMS + Eval 하네스 |
| 16 | PromptLayer 문서 | https://docs.promptlayer.com/ | Prompt Registry·릴리즈 레이블·A/B |
| 17 | Humanloop (⚠️ 종료) | https://humanloop.com | Anthropic 인수 후 플랫폼 sunset 중 |
| 18 | Promptfoo | https://promptfoo.dev | MIT OSS LLM 평가·레드팀 (E-3 소관) |
| 19 | Dify GitHub | https://github.com/langgenius/dify | Apache 2.0 기반 LLM 앱 플랫폼 |
| 20 | OpenAI Structured Outputs | https://platform.openai.com/docs/guides/structured-outputs | JSON Schema 기반 출력 형식 강제 |
| 21 | Anthropic Tool Use | https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview | Claude 도구 정의·함수 호출 형식 |
| 22 | JSON Schema | https://json-schema.org | LLM 출력 스키마 정의 표준 |
| 23 | Jinja2 | https://jinja.palletsprojects.com | Prompt 템플릿 변수 치환 표준 문법 |

---

## 7. 리서치 메모 — 추가 확인이 필요한 사항

- **Vellum**: 공식 사이트가 LLM 개발 플랫폼이 아닌 개인 AI 비서로 표시됨. 리브랜딩 또는 별개 제품인지 확인 필요. 가이드 본문에 포함 여부는 추가 확인 후 결정 권장.
- **PromptLayer 셀프호스트 조건**: 자체 호스팅 가능하다는 언급이 있으나 구체적 조건(라이선스·버전) 미확인. 도입 전 영업팀 문의 권장.
- **Pezzo 유지보수 속도**: 최근 릴리즈(v0.9.2, 2024.05)가 약 1년 이상 경과. 장기 운영을 위한 대안(Langfuse·Agenta) 병행 검토 권장.
- **각 제품의 RBAC 세부 지원 범위**: Prompt 편집자(SME) / 검토자(Reviewer) / 배포 승인자(Deployer) 역할 분리 가능 여부는 제품별 공식 문서 또는 PoC로 확인 필요.
- **Promptfoo 인수**: OpenAI가 인수했으나 "MIT 라이선스를 유지한다"고 명시. 향후 정책 변동 가능성 모니터링 권장.

---

*이 문서는 D-3 가이드 작성의 Tech Stack 섹션 초안을 위한 리서치 자료다. 가격·기능 범위는 시점에 따라 변동되므로 도입 전 공식 문서·PoC 확인을 권장한다.*
