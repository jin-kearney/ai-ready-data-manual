# Braintrust — AI 품질 중심 관측·평가 플랫폼

> 작성일: 2026-06-10 | 조사 기준: 2025~2026 최신 동향

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Braintrust Data, Inc. |
| 라이선스 | 독점 SaaS (소스 비공개) |
| 배포 형태 | 클라우드 SaaS / Enterprise 셀프호스팅 (AWS·GCP·Azure Terraform) |
| 최신 동향 | "Loop" AI 자동 최적화 기능 (Prompt·Scorer·데이터셋 자동 생성) / Notion·Stripe·Vercel 등 대형 고객사 레퍼런스 |

---

## 한 줄 포지셔닝

**"프로덕션 AI 품질을 코드처럼 관리하는 평가 중심 플랫폼 — 실험·트레이싱·인간 어노테이션을 단일 워크플로로"**

---

## 주요 기능

### 트레이싱 (Observability)
- 모든 LLM 호출, 도구 호출, 세션 추적
- 프로덕션 트레이스 검색·필터 (수백만 로그 규모)
- 지연시간, 비용, 품질 점수 실시간 추적
- 패턴 분석: 태스크·이슈·감성 분류 자동화

### 평가 (E-3)
- **Experiments**: 데이터셋 기반 프롬프트·모델 A/B 비교
- **LLM-as-judge**: 사실성, 적절성, 유해성 등 AutoEvals 제공 (autoevals 라이브러리)
- 코드 평가기 + 인간 평가기 조합
- **Online Scoring**: 프로덕션 트레이스 실시간 자동 채점
- **Quality Gate**: 배포 전 점수 임계값 통과 체크 (CI/CD 통합)

### Loop (AI 자동 최적화)
- 최적화 목표를 자연어로 기술 → Loop가 Prompt·Scorer·데이터셋 자동 생성
- 반복 실험 사이클 자동화

### Prompt 관리 (D-3)
- Playground: 모델·프롬프트 인터랙티브 실험
- 코드-UI 양방향 동기화 (Bidirectional Sync)
- 프롬프트 버전 추적 (단, 전용 Prompt Registry 기능은 LangSmith 대비 제한적)

### 데이터셋 관리 (E-3)
- 트레이스에서 예시 추출, 수동 큐레이션
- 데이터셋 버전 관리, 실험별 비교
- 인간 어노테이션 워크플로 내장

### 피드백 수집 (E-4)
- 프로덕션 신호(온라인 스코어링) → 데이터셋 보강 → 재실험 Feedback Loop

---

## AI-Ready Data 주제 매핑

| 코드 | 주제 | 커버 수준 | 설명 |
|------|------|-----------|------|
| D-2 | API/Tool 연계 (MCP) | △ | Tool 호출 추적 가능, MCP 직접 통합은 생태계 수준 |
| D-3 | Prompt/Harness 자산화 | △ | Playground·버전 추적 지원, 전용 Prompt Registry는 부분적 |
| E-3 | AI 평가 데이터 | ○ | 데이터셋·AutoEvals·인간 어노테이션·실험 완비 |
| E-4 | Feedback Loop | ○ | Online Scoring + Loop 자동 최적화로 강력한 피드백 사이클 |

---

## 강점

- 평가(Eval) 워크플로가 플랫폼 중심 설계 — AI 품질 관리 문화 정착에 효과적
- **Loop**: 자동화된 프롬프트·평가기 최적화로 엔지니어 생산성 대폭 향상
- 사용자 당 과금이 아닌 데이터 볼륨 기반 → 대형 팀에 비용 효율적
- Notion, Stripe, Vercel 등 하이프로덕션 고객사 레퍼런스
- 9개 이상 주요 프레임워크 네이티브 지원

## 약점·주의점

- **소스 비공개**: 셀프호스팅은 Enterprise 전용
- Prompt Registry(버전 관리·Prompt Hub) 기능이 LangSmith 대비 상대적으로 단순
- 셀프호스팅 Enterprise 계약 필요 → 기업 도입 초기 비용 장벽
- 트레이싱 깊이(Agent 실행 트리 시각화)는 LangSmith보다 약함

---

## 가격 모델

| 플랜 | 가격 | 주요 포함 |
|------|------|-----------|
| Starter | 무료 | 1GB/월 처리, 10,000 스코어, 무제한 사용자 |
| Pro | $249/월 | 5GB/월, 50,000 스코어, 30일 보존 |
| Enterprise | 커스텀 | 셀프호스팅 (AWS/GCP/Azure), SSO, 고급 보안, SLA |

> 초과 요금: 데이터 $3~4/GB, 스코어 $1.5~2.5/1,000건

---

## 연동 생태계

- **SDK**: Python, TypeScript
- **프레임워크**: OpenAI, Anthropic, Vercel AI SDK, LangChain, LlamaIndex, OpenAI Agents SDK
- **평가**: autoevals (오픈소스 평가기 라이브러리)
- **CI/CD**: GitHub Actions, pytest 통합
- **인프라 (셀프호스팅)**: Terraform (AWS, GCP, Azure)

---

## 출처

- https://www.braintrust.dev/
- https://www.braintrust.dev/pricing
- https://www.braintrust.dev/docs/guides/self-hosting
- https://www.braintrust.dev/articles/best-llm-evaluation-platforms-2025
- https://coverge.ai/blog/braintrust-pricing
- https://startupik.com/braintrust-ai-evaluation-and-monitoring-platform/
