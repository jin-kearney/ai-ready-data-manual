# research-A-what.md — E-4 데이터 Feedback Loop / What 클러스터

> 작성일: 2026-06-26 | 용도: E-4 가이드 What 섹션 초안 작성용 리서치 메모

---

## 1. Feedback Loop / Data Flywheel 개념

### 정의 및 핵심 구조

**피드백 루프(Feedback Loop)**란 AI 운영 결과(정답·오답·사용자 수정·오류 로그)를 다시 데이터·모델·Prompt·Tool 개선으로 환류하는 "닫힌 고리(closed loop)"다. 데이터 플라이휠(Data Flywheel)은 이 루프가 자체 강화되어 "더 많이 쓸수록 더 좋아지는" 선순환 구조를 강조하는 비유다.

NVIDIA 용어집은 데이터 플라이휠을 다음과 같이 정의한다:
> "AI 상호작용에서 수집된 데이터가 AI 모델을 지속적으로 개선하고, 더 나은 결과를 생성하여 추가 개선용 가치 있는 데이터를 만드는 자체 강화 루프(self-reinforcing loop)."

출처: [NVIDIA Glossary — Data Flywheel](https://www.nvidia.com/en-us/glossary/data-flywheel/)

### 6단계 순환 메커니즘 (NVIDIA 기준)

| 단계 | 내용 |
|------|------|
| 1. 데이터 처리 | 운영 데이터 수집·정제·노이즈 제거 |
| 2. 모델 커스터마이징 | 도메인 지식 반영(미세조정·DAPT 등) |
| 3. 모델 평가 | 성능 검증 및 반복 품질 개선 |
| 4. AI 가드레일 | 개인정보·보안·안전성 요구사항 준수 |
| 5. 배포 | RAG 기반 실시간 데이터 활용 |
| **6. 데이터 정제** | **사용자 피드백·시스템 동작 수집 → 루프 재시작** |

### 엔터프라이즈/제조업 맥락에서의 의미

- **데이터 준비 관점**: Feedback Loop는 "AI를 만드는 법"이 아니라 "AI가 쓸 데이터를 지속적으로 정비하는 체계"다. 피드백 데이터 자체가 라벨·Prompt·Tool·권한 주제의 입력 원재료가 된다.
- NVIDIA NVInfo(3만 명 이상 사용 사내 AI): MAPE(Monitor-Analyze-Plan-Execute) 제어 루프를 적용해 RAG 파이프라인 실패를 체계적으로 해소하는 폐쇄 루프(closed loop) 구현. 추론 비용 98% 절감 사례.
  출처: [Adaptive Data Flywheel: MAPE Control Loops — arXiv](https://arxiv.org/html/2510.27051v1)

**두산 제조 가상 예시**: 발전 설비 점검 보고서 AI 요약 시스템을 운영하면, 현장 기술자가 "터빈 베어링 마모 수치가 기준 초과인데 요약에서 빠짐"이라는 수정 편집(edit)을 남긴다. 이 편집이 피드백 데이터가 되어 → 데이터 누락(A군 카탈로그) 또는 Prompt 부재(D-3)로 분류 → 해당 주제 담당자에게 라우팅된다.

---

## 2. 피드백 수집 항목

AI 운영 중 수집 가능한 피드백 데이터 항목은 세 채널로 나뉜다.

### 채널 A — 명시적 사용자 피드백 (Explicit Human Feedback)

| 항목 | 정의 | 생성 경위 |
|------|------|-----------|
| 좋아요/싫어요(Thumbs up/down) | 응답에 대한 이진 만족도 | 사용자가 UI에서 직접 클릭 |
| 직접 수정(Direct Edit) | 사용자가 AI 출력을 편집해 저장 | "내가 고쳤다 = 틀렸다"는 가장 고신호(high-signal) 피드백 |
| 자유 텍스트 의견 | 불만·이유·개선 요청 서술 | 피드백 텍스트 박스·고객 지원 티켓 |
| 다차원 평가 점수 | 정확성·완전성·톤·규정 준수 등 항목별 점수 | 구조화 평가 폼 |
| 비교 선호도 | 여러 응답 중 더 나은 것 선택 | A/B 응답 비교 UI |

출처: [5 Steps to Build Feedback Loops for AI Models — Artech Digital](https://www.artech-digital.com/blog/5-steps-to-build-feedback-loops-for-ai-models), [Maxim AI — Incorporating HITL Feedback](https://www.getmaxim.ai/articles/incorporating-human-in-the-loop-feedback-for-continuous-improvement-of-ai-agents/)

### 채널 B — 암묵적 행동 신호 (Implicit Behavioral Signals)

| 항목 | 정의 | 생성 경위 |
|------|------|-----------|
| 응답 무시(Ignored Output) | 사용자가 AI 제안을 활용하지 않고 직접 작업 | 워크플로우 로그에서 "생성 후 미사용" 패턴 탐지 |
| 재시도(Retry) | 동일 질문을 반복하거나 다시 생성 요청 | 요청 로그에서 짧은 간격 내 동일 입력 감지 |
| 세션 이탈(Abandonment) | 응답 생성 도중 또는 직후 세션 종료 | 세션 타임스탬프 분석 |
| 재질문(Follow-up Query) | "다시 설명해줘", "더 간단하게" 등 후속 질문 | 대화 턴 분석 |

### 채널 C — 시스템 수준 운영 지표 (System-Level Metrics)

| 항목 | 정의 | 생성 경위 |
|------|------|-----------|
| Tool 호출 실패 | API 오류·타임아웃·파라미터 오류 | 에이전트 실행 로그 자동 수집 |
| 사람 승인/거절 | 에이전트 행동에 대한 사람 승인 게이트 결과 | 승인 워크플로우 상태 기록 |
| 근거 누락(Missing Grounding) | 출처 없이 답변 생성 | RAG 파이프라인 추적(trace) 분석 |
| 낮은 신뢰도 점수 | 자동 평가기(evaluator)가 임계값 미달 판정 | 평가 파이프라인 자동 태깅 |
| 응답 지연(Latency Spike) | 비정상 응답 시간 | 시스템 메트릭 모니터링 |

출처: [How to Build an AI Agent Feedback Loop — Braincuber](https://www.braincuber.com/blog/how-to-build-feedback-loop-ai-agent-improvement), [Agent Academy — Microsoft](https://microsoft.github.io/agent-academy/operative/11-obtain-user-feedback/)

> **핵심 원칙**: 단일 신호(thumbs up/down만)에 의존하면 부족하다. 복수 채널 신호를 교차 검증(cross-validate)해야 피드백이 노이즈가 아닌 근거 있는 데이터가 된다.

---

## 3. 오류 유형 분류 체계 (Error Taxonomy)

피드백 데이터를 원인별로 분류해야 적절한 개선 경로로 라우팅할 수 있다. 아래는 E-4 맥락에 맞게 정리한 6대 오류 유형이다.

### 분류 기준: 증상 → 원인 계층

```
피드백 데이터(증상)
    ↓
오류 유형 분류(원인)
    ↓
개선 경로(담당 주제/팀)
```

### 6대 오류 유형

| # | 오류 유형 | 정의 | 증상 예시 |
|---|-----------|------|-----------|
| 1 | **데이터 문제** | 학습·검색 데이터 자체의 누락·오기·구 버전 | AI가 "현재 재고 없음"이라 답했으나 실제 재고 있음. 데이터가 갱신 안 됨 |
| 2 | **라벨 문제** | 훈련 데이터의 주석·라벨이 틀렸거나 부족함 | 외관 검사 AI가 정상 제품을 불량으로 분류. 라벨링 기준 불일치 |
| 3 | **Prompt 문제** | 지시문(Prompt) 자체가 모호·불완전·업무 정책과 불일치 | "설비 점검 보고서를 요약해줘"에 핵심 지표(마모율) 기준이 없어 누락 |
| 4 | **Tool 문제** | 에이전트가 호출하는 도구의 명세 오류·파라미터 불일치·API 변경 | 부품 발주 Tool 호출 시 `quantity` 파라미터 명이 바뀌어 실패 |
| 5 | **권한 문제** | 접근 권한 부족·데이터 비식별화 설정 오류 | 에이전트가 협력사 단가 데이터를 읽지 못해 견적 산출 실패 |
| 6 | **업무 정책 문제** | AI 출력이 기술적으로는 맞지만 업무 규칙·기준과 상충 | "최소 발주량 50개" 정책이 Prompt에 없어 1개 발주 지시 생성 |

출처: [LLM Behavioral Failure Modes — ceaksan.com](https://ceaksan.com/en/llm-behavioral-failure-modes), [ErrorAtlas: Taxonomy of LLM Failure Modes — EmergentMind](https://www.emergentmind.com/topics/erroratlas), [A Taxonomy of Prompt Defects in LLM Systems — arXiv](https://arxiv.org/html/2509.14404)

### LLM 에이전트 계층별 주요 실패 패턴 (참고: ceaksan.com 기반)

**기초 실패 모드** (단일 호출에서도 발생):
- 할루시네이션(Hallucination): 없는 문서·API를 있는 것처럼 답변
- 동조성(Sycophancy): 사용자 오류를 맞다고 수용
- 맥락 부패(Context Rot): 긴 대화에서 초기 지시를 망각
- 지시문 약화(Instruction Attenuation): 규칙이 반복될수록 무시됨

**에이전트 실패 모드** (다단계·도구 사용 시):
- 목표 이탈(Task Drift): 원래 목적에서 점진적 이탈
- 도구 오류 호출: 잘못된 Tool 선택·파라미터 환각
- 버전 드리프트(Version Drift): 코드 변경 없이 출력이 달라짐

> **제조 적용 예시**: 발전소 계획 정비(PM) 일정 AI가 "베어링 교체 주기 90일"을 답했는데 실제 정책은 "가동시간 3,000시간 초과 시"다. → 업무 정책 문제(유형 6). Prompt에 가동시간 기반 조건이 없어서 발생.

---

## 4. 개선 과제 연결판 — 라우팅 지도 (Routing Map)

오류 유형이 분류되면 해당 개선 과제 담당 주제/팀으로 라우팅한다. E-4는 "증상을 모아 원인 주제로 되돌리는 허브"다.

```
피드백 데이터
    │
    ▼
[E-4 분류 게이트]
    │
    ├─ 데이터 누락·오기·구 버전        → A-1 데이터 카탈로그 (등록·갱신)
    │                                   A-2 메타데이터 (속성 보완)
    │
    ├─ 용어 혼동·개념 불일치            → A-3 Glossary (용어 표준화)
    │
    ├─ 라벨·주석 오류·부족              → B-2 데이터 해설·주석 (라벨 재작업)
    │
    ├─ 평가 실패·기준 미달              → E-3 평가 데이터 (평가셋 갱신)
    │
    ├─ Prompt 모호·정책 누락            → D-3 Prompt 지식 자산 (Prompt 수정)
    │
    ├─ Tool 명세 오류·파라미터 불일치   → D-2 Tool 명세 데이터 (명세 갱신)
    │
    └─ 권한 문제·비식별화 오류          → F-4 데이터 접근권한·비식별화
```

### 라우팅 기준 테이블

| 오류 유형 | 주요 증상 | 라우팅 목적지 | 담당 팀(예시) |
|-----------|-----------|---------------|---------------|
| 데이터 문제 | 구 버전 데이터 기반 답변, 데이터 없음 | A-1, A-2 | 데이터 엔지니어링팀 |
| 용어 혼동 | 같은 개념 다른 명칭, 번역 불일치 | A-3 | 데이터 거버넌스팀 |
| 라벨 문제 | 분류 오류, 라벨 기준 불일치 | B-2 | 도메인 전문가·QA팀 |
| 평가 실패 | 합격 기준 미달, 테스트 실패 | E-3 | AI 운영팀 |
| Prompt 문제 | 지시 모호·정책 누락 | D-3 | Prompt 엔지니어 |
| Tool 문제 | API 오류·파라미터 실패 | D-2 | 개발팀 |
| 권한 문제 | 데이터 접근 거부·비식별 오류 | F-4 | 정보보안팀 |

출처: [Own the AI Feedback Loop: Your Data Engine — Label Studio](https://labelstud.io/blog/your-data-engine-is-the-moat-here-s-how-to-own-it/), [How to Build Self-Improving AI Agents — Datagrid](https://datagrid.com/blog/7-tips-build-self-improving-ai-agents-feedback-loops/)

---

## 5. 자동 반영 vs 사람 검토 (Human-in-the-Loop 게이트)

모든 피드백이 즉시 자동 반영되면 안 된다. 위험 수준에 따라 처리 경로가 달라진다.

### 세 가지 감독 모델 (Redis HITL 아티클 기준)

| 모델 | 설명 | 적용 상황 |
|------|------|-----------|
| **Human-in-the-Loop (HITL)** | 사람이 결정, AI는 추천만. 사람 입력 없이 진행 불가 | 고위험·불가역 행동(발주·삭제·승인) |
| **Human-on-the-Loop (HOTL)** | AI가 독립 실행, 사람은 모니터링·거부권 보유 | 중위험·모니터링 가능 작업 |
| **Human-out-of-the-Loop** | 사전 정의된 경계 내에서 완전 자동 | 저위험·반복적·명확한 작업 |

출처: [AI Human in the Loop: Production Oversight Patterns — Redis](https://redis.io/blog/ai-human-in-the-loop/)

### 자동 반영 후보 조건 (저위험)

- 자동 평가기(evaluator)가 높은 신뢰도로 합격 판정
- 오류 유형이 명확하고 영향 범위가 좁음
- 반복 발생한 동일 패턴(클러스터링으로 확인됨)
- 이전에 사람이 승인한 동일 유형의 수정

### 사람 검토 필수 조건 (고위험)

- 고객·외부 영향이 있는 데이터(단가·계약·개인정보)
- 새롭거나 예상치 못한 상황(분포 변화, 신규 시나리오)
- 보안·규정 준수 관련 변경(F-4 권한·비식별화)
- 자동 평가기가 저신뢰도(low confidence) 판정
- 불가역 행동(데이터 삭제·시스템 설정 변경)

출처: [How to Design Approval Workflows — StackAI](https://www.stackai.com/insights/human-in-the-loop-ai-agents-how-to-design-approval-workflows-for-safe-and-scalable-automation), [Maxim AI — HITL Feedback](https://www.getmaxim.ai/articles/incorporating-human-in-the-loop-feedback-for-continuous-improvement-of-ai-agents/)

### 자동 반영 처리 흐름 (고위험 경우)

```
피드백 수집
    ↓
신뢰도·위험도 점수 계산
    ↓
    ├─ 저위험 → 자동 반영 (카나리 배포 10% → 72시간 모니터링 → 전체 반영)
    └─ 고위험 → 검토 큐(Review Queue) → 전문가 승인 → 반영
                                        ↘ 거절 → 재분류 or 보류
```

출처: [How to Build an AI Agent Feedback Loop — Braincuber](https://www.braincuber.com/blog/how-to-build-feedback-loop-ai-agent-improvement)

> **EU AI Act 규정 참고**: 고위험 AI 시스템은 인간이 결과를 해석하고 결정을 번복할 수 있어야 하며, 로그 자동 보존이 의무다(Article 12 — 제공자 로그 의무, Article 26 — 배포자 보존 의무). 제조업 AI는 안전·품질 관련 기능이 고위험에 해당할 가능성이 높다.
> 출처: [EU AI Act — Article 14 Human Oversight](https://artificialintelligenceact.eu/article/14/)

---

## 6. 피드백 루프 5-레이어 아키텍처 (What의 구성 요소 요약)

Braincuber의 5-Layer 구조는 Feedback Loop 구성 요소를 데이터 체계 관점으로 정리하기에 적합하다.

| 레이어 | 이름 | 역할 |
|--------|------|------|
| L1 | **계측(Instrumentation)** | 모든 결정에 타임스탬프·입력 지문·출력 해시 기록 |
| L2 | **다중 채널 수집(Multi-Source Collection)** | 사람 검토자·사용자 행동·운영 메트릭 동시 수집 |
| L3 | **지능형 라우팅(Intelligent Routing)** | 오류 유형별 담당 주제/팀으로 분기 |
| L4 | **신호 검증(Signal Validation)** | 2개 이상 출처 교차 검증 후 개선 파이프라인 진입 |
| L5 | **통제된 반영(Controlled Deployment)** | 카나리 배포(10% 트래픽·72시간) 후 전체 반영 |

출처: [How to Build an AI Agent Feedback Loop — Braincuber](https://www.braincuber.com/blog/how-to-build-feedback-loop-ai-agent-improvement)

---

## 참고 출처 목록

| # | 제목 | URL |
|---|------|-----|
| 1 | NVIDIA Glossary — Data Flywheel | https://www.nvidia.com/en-us/glossary/data-flywheel/ |
| 2 | Adaptive Data Flywheel: MAPE Control Loops — arXiv | https://arxiv.org/html/2510.27051v1 |
| 3 | Agent-in-the-Loop: A Data Flywheel for Continuous Improvement — arXiv | https://arxiv.org/html/2510.06674v2 |
| 4 | LLM Behavioral Failure Modes — ceaksan.com | https://ceaksan.com/en/llm-behavioral-failure-modes |
| 5 | ErrorAtlas: Taxonomy of LLM Failure Modes — EmergentMind | https://www.emergentmind.com/topics/erroratlas |
| 6 | A Taxonomy of Prompt Defects in LLM Systems — arXiv | https://arxiv.org/html/2509.14404 |
| 7 | AI Human in the Loop: Production Oversight Patterns — Redis | https://redis.io/blog/ai-human-in-the-loop/ |
| 8 | Human-in-the-Loop AI Agents: Approval Workflows — StackAI | https://www.stackai.com/insights/human-in-the-loop-ai-agents-how-to-design-approval-workflows-for-safe-and-scalable-automation |
| 9 | Incorporating HITL Feedback — Maxim AI | https://www.getmaxim.ai/articles/incorporating-human-in-the-loop-feedback-for-continuous-improvement-of-ai-agents/ |
| 10 | How to Build an AI Agent Feedback Loop — Braincuber | https://www.braincuber.com/blog/how-to-build-feedback-loop-ai-agent-improvement |
| 11 | Own the AI Feedback Loop: Your Data Engine — Label Studio | https://labelstud.io/blog/your-data-engine-is-the-moat-here-s-how-to-own-it/ |
| 12 | EU AI Act — Article 14 Human Oversight | https://artificialintelligenceact.eu/article/14/ |
| 13 | Data & AI Observability — Medium/Matih Labs | https://medium.com/matih-labs/data-ai-observability-why-the-feedback-loop-changes-everything-665f3a25026a |
| 14 | How to Build Self-Improving AI Agents — Datagrid | https://datagrid.com/blog/7-tips-build-self-improving-ai-agents-feedback-loops/ |
