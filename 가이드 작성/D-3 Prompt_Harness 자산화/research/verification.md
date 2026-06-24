# D-3 가이드 출처 검증 보고서

검증 일시: 2026-06-24  
검증 방법: WebFetch 직접 접속  
검증 대상: 참고자료 URL 15개 + 추가 확인 항목

---

## 1. URL 상태 일람

| # | 출처 설명 | URL | 상태 | 비고 |
|---|-----------|-----|------|------|
| 1 | Anthropic — Effective Harnesses for Long-Running Agents | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | ✅ 정상 | 제목·내용 일치 |
| 2 | Databricks — What is an AI agent harness? | https://www.databricks.com/blog/ai-harness | ✅ 정상 | 제목·내용 일치 |
| 3 | MLflow — Prompt Registry | https://mlflow.org/docs/latest/genai/prompt-registry/ | ✅ 정상 | 제목·내용 일치 |
| 4 | Braintrust — What is prompt management? | https://www.braintrust.dev/articles/what-is-prompt-management | ✅ 정상 | 제목·내용 일치 |
| 5 | Braintrust — What is prompt versioning? | https://www.braintrust.dev/articles/what-is-prompt-versioning | ✅ 정상 | 제목·내용 일치 |
| 6 | Martin Fowler — Structured Prompt-Driven Development | https://martinfowler.com/articles/structured-prompt-driven/ | ✅ 정상 | 제목·내용 일치. 실제 저자는 Wei Zhang·Jessie Jie Xia(Thoughtworks), martinfowler.com 게재 |
| 7 | JSON Schema | https://json-schema.org | ✅ 정상 | 공식 사이트 정상 운영 |
| 8 | OpenAI — Structured Outputs | https://platform.openai.com/docs/guides/structured-outputs | ⚠️ 리다이렉트됨 | 301 → https://developers.openai.com/api/docs/guides/structured-outputs 로 이전. 새 URL 정상. **URL 교체 권장** |
| 9 | Anthropic — Tool Use overview | https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview | ⚠️ 리다이렉트됨 | 301 → https://platform.claude.com/docs/en/docs/build-with-claude/tool-use/overview 로 이전. 새 URL 정상. **URL 교체 권장** |
| 10a | Langfuse 홈 | https://langfuse.com | ⚠️ 접속불안정 | 직접 WebFetch에서 404 반환(CDN 차단으로 추정). Prompt Management docs(10b)는 정상. 홈 링크는 삭제하거나 docs로 대체 권장 |
| 10b | Langfuse — Prompt Management | https://langfuse.com/docs/prompt-management/overview | ✅ 정상 | 제목·버전관리 기능 일치 |
| 11 | Agenta | https://agenta.ai | ✅ 정상 | 오픈소스 LLMOps, Prompt 버전관리 확인 |
| 12 | Helicone | https://helicone.ai | ✅ 정상 | "Open-source LLM observability" 명시, GitHub 5.8K★. helicone.ai 직접 접속(www 없이)은 CDN 차단 있으나 www.helicone.ai 정상 |
| 13 | Portkey | https://portkey.ai | ✅ 정상 | "We're open source" 명시, GitHub 10.2K★. Prompt 버전관리·롤백 기능 확인 |
| 14 | LangSmith | https://www.langchain.com/langsmith | ✅ 정상 | 제목·내용 일치. 셀프호스트(BYOC) 옵션 확인 |
| 15 | PromptLayer | https://www.promptlayer.com | ✅ 정상 | "Prompt CMS, eval harness, observability" — 제목·내용 일치 |

---

## 2. 문제 항목 상세

### [교체 권장] #8 OpenAI — Structured Outputs

- 기재 URL: `https://platform.openai.com/docs/guides/structured-outputs`
- 상태: 301 영구 이전
- 새 URL: `https://developers.openai.com/api/docs/guides/structured-outputs`
- 조치: 가이드 본문·참고자료 URL을 새 주소로 교체

### [교체 권장] #9 Anthropic — Tool Use overview

- 기재 URL: `https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview`
- 상태: 301 영구 이전
- 새 URL: `https://platform.claude.com/docs/en/docs/build-with-claude/tool-use/overview`
- 조치: 가이드 본문·참고자료 URL을 새 주소로 교체
- 참고: 페이지 내용은 "Tool use with Claude" — Tool 명세 정의·agentic loop·pricing 포함, D-3 가이드 Tool 명세 섹션 출처로 적합

### [주의] #10a Langfuse 홈

- 기재 URL: `https://langfuse.com`
- 상태: WebFetch 404 (CDN 봇 차단 추정 — docs 하위 페이지는 정상 접속됨)
- 조치: 참고자료에 홈 단독 링크 대신 `https://langfuse.com/docs/prompt-management/overview` 로 대체하거나, 홈 링크는 "공식 홈(접속 확인 권장)" 표기로 남김

---

## 3. 추가 확인 결과

### Humanloop — 서비스 종료(sunset) 상태 확인

- URL: https://humanloop.com
- 상태: **플랫폼 종료 진행 중** (Anthropic 인수)
- 공식 발표: "Humanloop 팀이 Anthropic에 합류. 플랫폼을 종료 중." 고객 마이그레이션 지원 중
- 결론: 가이드의 "신규 도입 어려울 수 있음" 주의 표기는 **적절하고 충분**. 단, 실제 종료 완료 시점은 확정되지 않으므로 "공식 확인 권장" 표기 유지 권장.

### 솔루션 4종 오픈소스·Prompt 버전관리 확인

| 솔루션 | 오픈소스 | 셀프호스트 | Prompt 버전관리 |
|--------|---------|-----------|----------------|
| Langfuse | ✅ (공식 문서 "Open Source Prompt Management" 명시) | ✅ (docs에서 셀프호스트 옵션 안내) | ✅ version control·labels 명시 |
| Agenta | ✅ ("The open-source LLMOps platform" 명시) | ⚠️ 홈 페이지에서 명시 없음 — 공식 확인 권장 | ✅ "Complete version history: Version prompts and keep track of changes" 명시 |
| Helicone | ✅ ("Open-source LLM observability platform" 헤더 명시, GitHub 5.8K★) | ⚠️ 홈 페이지에서 셀프호스트 명시 없음 — 공식 확인 권장 | ✅ Prompts 기능 메뉴 확인됨 |
| Portkey | ✅ ("We're open source" 명시, GitHub 10.2K★) | ⚠️ 홈 페이지에서 셀프호스트 명시 없음 — 공식 확인 권장 | ✅ "Built-in version control with labelled deployments and rollbacks" 명시 |

---

## 4. 조치 요약

| 우선도 | 항목 | 조치 |
|--------|------|------|
| 🔴 교체 | #8 OpenAI Structured Outputs | URL → `https://developers.openai.com/api/docs/guides/structured-outputs` |
| 🔴 교체 | #9 Anthropic Tool Use overview | URL → `https://platform.claude.com/docs/en/docs/build-with-claude/tool-use/overview` |
| 🟡 선택 | #10a Langfuse 홈 | docs URL로 대체하거나 "공식 확인 권장" 표기 |
| ✅ 현행 유지 | Humanloop 주의 표기 | 종료 사실 확인됨 — "신규 도입 어려울 수 있음" 표기 적절 |
| ✅ 현행 유지 | 솔루션 4종 오픈소스·버전관리 | 모두 실제 기능 확인됨 |
