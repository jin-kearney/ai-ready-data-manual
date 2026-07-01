# promptfoo & Ragas — LLM 평가 특화 도구

> 작성일: 2026-06-10 | 조사 기준: 2025~2026 최신 동향

---

## 1. promptfoo

### 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | promptfoo, Inc. → OpenAI 인수 (2026.03.09) |
| 라이선스 | MIT (오픈소스) |
| 배포 형태 | CLI 도구 / Node.js 라이브러리 / 클라우드 플랜 |
| 최신 동향 | 2025.07 Series A $86M / 2026.03 OpenAI 인수 / 350,000+ 개발자, Fortune 500 25% 채택 |

### 한 줄 포지셔닝

**"YAML 기반 LLM 평가·보안 레드팀 도구 — CI/CD 네이티브, OWASP LLM Top 10 완전 커버"**

### 주요 기능

#### 기능 평가 (Functional Evaluation)
- YAML 설정 기반: 모델·프롬프트·테스트 케이스를 선언적으로 정의
- 다중 프로바이더 동시 비교: OpenAI, Anthropic, 로컬 모델(Ollama 등) 병렬 평가
- 내장 Assertion 타입: `contains`, `llm-rubric`, `factuality`, `similar`, `javascript` 등 30+ 종
- CI/CD 완전 통합: GitHub Actions, GitLab CI, 배포 전 품질 게이트

#### 레드팀·보안 평가 (D-2 보안 측면)
- **자동 공격 생성**: 50+ 공격 플러그인 (프롬프트 인젝션, 탈옥, PII 유출, SSRF, SQL 인젝션, 환각 유발 등)
- **프레임워크 매핑**: OWASP LLM Top 10, NIST AI RMF, MITRE ATLAS
- **에이전트 보안**: 과도한 에이전시(Excessive Agency), 도구 남용 시나리오

#### 데이터셋 관리 (E-3)
- 평가 케이스 YAML 파일로 관리, 버전 제어 가능
- 출력 비교 리포트 자동 생성

### AI-Ready Data 주제 매핑

| 코드 | 주제 | 커버 수준 | 설명 |
|------|------|-----------|------|
| D-2 | API/Tool 연계 (MCP) | △ | 에이전트 도구 호출 보안 평가 (레드팀) |
| D-3 | Prompt/Harness 자산화 | △ | YAML 기반 Prompt 테스트 케이스 관리 |
| E-3 | AI 평가 데이터 | ○ | LLM-judge·코드 Assertion·보안 평가 완비 |
| E-4 | Feedback Loop | △ | CI/CD 통합으로 자동 회귀 탐지 |

### 강점
- CI/CD 네이티브 설계 — 배포 파이프라인에 LLM 테스트 즉시 삽입
- 오픈소스 MIT, 완전 로컬 실행 가능 (데이터 외부 전송 없음)
- 보안·레드팀 평가 기능이 업계 최강 수준
- OpenAI 인수 이후 생태계 지원 강화 전망

### 약점·주의점
- 트레이싱·Prompt Registry·비용 추적 기능 없음 (단일 목적 도구)
- OpenAI 인수로 장기 오픈소스 지속 가능성 모니터링 필요
- 설정이 YAML 기반 → 비개발자 접근 어려움

### 가격 모델
| 플랜 | 가격 | 주요 포함 |
|------|------|-----------|
| 오픈소스 | 무료 | 전체 CLI 기능, 로컬 실행 |
| 클라우드 | 별도 협의 | 팀 협업, 클라우드 실행 |

### 연동 생태계
- **모델 프로바이더**: OpenAI, Anthropic, Google Gemini, Ollama, HuggingFace, AWS Bedrock
- **CI/CD**: GitHub Actions, GitLab CI, Jenkins
- **평가 기준**: OWASP LLM Top 10, NIST AI RMF, MITRE ATLAS

### 출처
- https://www.promptfoo.dev/docs/intro/
- https://www.promptfoo.dev/docs/red-team/
- https://www.toxsec.com/p/promptfoo-red-teaming
- https://yuv.ai/blog/promptfoo

---

## 2. Ragas

### 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | explodinggradients |
| 라이선스 | MIT (오픈소스) |
| 배포 형태 | Python 라이브러리 (pip install ragas) |
| 최신 동향 | 에이전트 평가 메트릭 추가 (Tool Call Accuracy, Agent Goal Accuracy) / LLM-as-judge 정렬(Alignment) 가이드 강화 (2025) |

### 한 줄 포지셔닝

**"RAG 파이프라인 품질 평가의 사실상 표준 오픈소스 라이브러리 — LLM-as-judge 기반, 참조 데이터 없이도 평가 가능"**

### 주요 기능

#### RAG 평가 메트릭 (E-3)
- **Faithfulness**: 응답이 검색된 컨텍스트에 충실한가 (환각 감지)
- **Answer Relevance**: 응답이 질문에 관련되는가
- **Context Relevance / Precision / Recall**: 검색된 컨텍스트의 품질
- **참조 없는 평가**: 인간 레이블 Ground Truth 없이도 평가 가능 → 비용·시간 절감

#### 에이전트 평가 메트릭 (E-3)
- **Agent Goal Accuracy**: 사용자 목표 달성 여부 (0~1 점수)
- **Tool Call Accuracy**: LLM이 올바른 도구를 선택·호출했는가
- **Tool Call F1**: 도구 호출 정밀도·재현율 기반 F1 점수
- **Topic Adherence**: 대화에서 사전 정의 도메인 준수 여부

#### LLM-as-judge 정렬 (E-3)
- Judge LLM의 평가 결과를 인간 전문가 판단과 체계적으로 정렬
- 불일치 패턴 분석, 재사용 가능한 평가 파이프라인 구축

#### 합성 데이터 생성 (E-3)
- RAG 평가용 합성 테스트셋 자동 생성
- 다양한 질문 유형(단순·추론·멀티홉) 커버

### AI-Ready Data 주제 매핑

| 코드 | 주제 | 커버 수준 | 설명 |
|------|------|-----------|------|
| D-2 | API/Tool 연계 (MCP) | △ | 에이전트 도구 호출 평가 메트릭 제공 |
| D-3 | Prompt/Harness 자산화 | × | 해당 없음 |
| E-3 | AI 평가 데이터 | ○ | RAG·에이전트 평가 메트릭 + 합성 데이터 생성 완비 |
| E-4 | Feedback Loop | △ | 평가 결과를 데이터셋 개선에 활용 가능, 자동화는 별도 구성 필요 |

### 강점
- RAG 품질 평가의 사실상 표준 — 문서·커뮤니티 풍부
- 참조 없는 평가로 평가 비용 대폭 절감
- MIT 오픈소스, 완전 로컬 실행
- LangChain, LlamaIndex, LangGraph, Amazon Bedrock 공식 통합
- 에이전트 평가 메트릭 지속 추가 중

### 약점·주의점
- 독립형 라이브러리 — 트레이싱·Prompt 관리·UI 없음
- LangSmith·Langfuse 등 관측 플랫폼과 조합하여 사용 권장
- LLM-as-judge 특성상 Judge 모델 선택에 따라 결과 편차 존재

### 가격 모델
| 형태 | 가격 |
|------|------|
| 오픈소스 라이브러리 | 무료 |
| Judge LLM 비용 | 사용하는 LLM API 비용에 따라 결정 |

### 연동 생태계
- **프레임워크**: LangChain, LlamaIndex, LangGraph, Haystack
- **클라우드**: Amazon Bedrock (공식 통합), Azure OpenAI
- **Judge LLM**: OpenAI GPT-4, Anthropic Claude, Google Gemini 등 모두 지원
- **플랫폼 연동**: LangSmith, Langfuse, Arize Phoenix (트레이스 기반 평가)

### 출처
- https://docs.ragas.io/en/stable/
- https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/agents/
- https://docs.ragas.io/en/stable/tutorials/agent/
- https://aws.amazon.com/blogs/machine-learning/evaluate-amazon-bedrock-agents-with-ragas-and-llm-as-a-judge/
- https://fractal.ai/blog/ai-agents-ragas

---

## promptfoo vs Ragas 비교

| 구분 | promptfoo | Ragas |
|------|-----------|-------|
| 주 목적 | LLM 기능 테스트 + 보안 레드팀 | RAG·에이전트 품질 평가 메트릭 |
| 형태 | CLI/라이브러리 | Python 라이브러리 |
| UI | 웹 리포트 (로컬 생성) | 없음 (외부 플랫폼 연동) |
| 보안 평가 | ○ (핵심 기능) | × |
| RAG 메트릭 | △ | ○ (핵심 기능) |
| CI/CD 통합 | ○ | △ (코드로 통합) |
| 라이선스 | MIT | MIT |
| 소유권 | OpenAI 인수 (2026.03) | explodinggradients |

> **조합 권장**: promptfoo (CI/CD 회귀 테스트 + 보안) + Ragas (RAG 품질 상세 평가) + Langfuse (트레이싱·데이터셋 관리)
