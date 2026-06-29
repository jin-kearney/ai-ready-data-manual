# E-3 AI 평가 데이터 — Tech Stack 리서치 (클러스터 B)
> 평가 솔루션 검토: 유형 분류 · 대표 도구 · 선정 기준

작성일: 2026-06-26  
관점: 제조 대기업(두산) 현업 도입 검토 — **온프레미스/폐쇄망 가능 여부** 최우선 기준  
주의: 가격·버전·라이선스는 빠르게 변한다. 도입 전 공식 문서 및 PoC 확인 필수.

---

## 1. 평가 솔루션 유형 분류

| 유형 | 설명 | 대표 사례 |
|------|------|-----------|
| **① 정답 매칭 / 정량 지표** | 기대 답변과 모델 출력을 자동 비교. BLEU·ROUGE·Exact Match 등 전통 NLP 지표 + 사실성·충실도 같은 LLM 특화 지표 | RAGAS, MLflow LLM Evaluate |
| **② 사람 평가(Human Eval)** | 어노테이터·도메인 전문가가 직접 점수 매기는 방식. 평가 UI·과제 배정·이견 관리·합의 기능 필요 | Langfuse(어노테이션 큐), Braintrust(Human review), LangSmith |
| **③ LLM-as-a-Judge** | 다른 LLM(심사 모델)이 출력을 채점. 사람 평가를 자동화·확장. 심사 기준 커스텀 가능 | DeepEval(G-Eval), RAGAS, Langfuse, Arize Phoenix, TruLens |
| **④ RAG / Agent 전용 프레임워크** | 검색-생성 파이프라인 또는 에이전트 워크플로의 단계별 품질(검색 정밀도·충실도·컨텍스트 재현율 등) 측정 전문 도구 | RAGAS, DeepEval, TruLens, Arize Phoenix |

> 실무에서는 유형 ①②③④가 혼합된다. 정량 지표로 1차 필터 → LLM-as-a-Judge로 2차 채점 → 사람이 최종 검증하는 3단계 파이프라인이 권장 모범 사례다.

---

## 2. 대표 솔루션 비교표

| 솔루션 | 유형 | 한 줄 설명 | 오픈소스/상용 | 셀프호스트(온프레미스) | 공식 URL |
|--------|------|-----------|--------------|----------------------|----------|
| **RAGAS** | ①③④ | RAG 파이프라인 전용 평가 프레임워크. 충실도·답변 관련성·컨텍스트 정밀도 지표가 사실상 업계 표준 | 오픈소스(MIT) | 가능 — 로컬 Python 실행, 외부 서버 불필요 | [ragas.io](https://ragas.io) |
| **DeepEval** (Confident AI) | ①②③④ | pytest 방식으로 LLM 평가를 코드로 작성. 50+ 지표·합성 데이터 생성·CI/CD 연동 지원 | 프레임워크 오픈소스(Apache 2.0) / 플랫폼(Confident AI)은 상용 | 프레임워크 로컬 실행 가능; 협업 대시보드(Confident AI)는 별도 요금제 | [deepeval.com](https://deepeval.com) |
| **Promptfoo** | ①③ | CLI 기반 프롬프트·모델 비교 평가 + 레드팀(보안 취약점 자동 탐색). OpenAI에 인수됨(2025). | 오픈소스(GitHub 22.6k★) | 가능 — CLI 로컬 실행; 에어갭 환경 공식 지원(엔터프라이즈) | [promptfoo.dev](https://www.promptfoo.dev) |
| **OpenAI Evals** | ①③ | OpenAI가 만든 LLM 평가 프레임워크 + 벤치마크 레지스트리. 비OpenAI 모델에도 적용 가능 | 오픈소스(MIT) | 가능 — 프레임워크 로컬 실행; 채점 시 LLM API 비용 발생 | [github.com/openai/evals](https://github.com/openai/evals) |
| **MLflow LLM Evaluate** | ①③ | ML 실험 추적 플랫폼 MLflow에 내장된 LLM 평가 모듈. 50+ 내장 지표·LLM-as-a-Judge·버전 관리 통합 | 오픈소스(Apache 2.0) | 가능 — MLflow 서버 온프레미스 배포 지원 | [mlflow.org](https://mlflow.org) |
| **TruLens** (Snowflake) | ①③④ | LLM·RAG·에이전트 추적 + 평가 라이브러리. Snowflake 인수 후 오픈소스로 계속 유지. MLflow·OpenTelemetry 연동 | 오픈소스(Apache 2.0) | 가능 — 로컬 또는 자체 서버 실행; Snowflake Cortex 연동 시 클라우드 | [trulens.org](https://www.trulens.org) |
| **Phoenix** (Arize AI) | ①②③④ | Arize AI가 만든 오픈소스 LLM 관찰·평가 플랫폼. OpenTelemetry 기반, Docker 한 줄 배포 | 오픈소스(ELv2) | 가능 — Docker/Kubernetes 온프레미스; 기능 제한 없음 | [phoenix.arize.com](https://phoenix.arize.com) |
| **Langfuse** | ①②③④ | LLM 엔지니어링 플랫폼. 추적·평가(LLM-as-a-Judge·사람 어노테이션)·프롬프트 관리 통합. 2025년 전 기능 MIT로 전환 | 오픈소스(MIT) | 가능 — Docker Compose / Kubernetes; 에어갭·VPC 공식 지원 | [langfuse.com](https://langfuse.com) |
| **LangSmith** (LangChain) | ①②③④ | LangChain 생태계의 추적·평가·데이터셋 관리 플랫폼. LangChain/LangGraph 연동 가장 강력 | 상용(일부 무료 티어) | 가능 — 엔터프라이즈 전용, Kubernetes(AWS/GCP/Azure) 배포 | [smith.langchain.com](https://smith.langchain.com) |
| **Braintrust** | ①②③④ | 평가 중심 AI 품질 관리 플랫폼. CI/CD 연동·LLM-as-a-Judge·사람 리뷰·버전 추적 통합 | 상용(무료 티어 있음) | 가능 — 엔터프라이즈 티어; AWS/GCP/Azure VPC 또는 온프레미스(에어갭 포함) | [braintrust.dev](https://www.braintrust.dev) |
| **Arize AI (AX)** | ①②③④ | 엔터프라이즈급 ML+LLM 관찰·평가 플랫폼. Phoenix(오픈소스)와 AX(상용)의 2층 구조 | 상용(Phoenix OSS 별도) | AX: 클라우드 관리형(VPC 옵션); Phoenix: 완전 셀프호스트 가능 | [arize.com](https://arize.com) |
| **W&B Weave** (Weights & Biases) | ①②③④ | ML 실험 추적 플랫폼(W&B)의 LLM 평가·관찰 모듈. Humanloop 종료(2025.9) 이후 마이그레이션 대상으로 부상 | 상용(무료 티어 있음) | 가능 — SaaS·단일 테넌트·고객 VPC(AWS) 배포 지원; 완전 온프레미스는 엔터프라이즈 문의 | [wandb.ai/site/weave](https://wandb.ai/site/weave/) |
| **Fiddler AI** | ①②③④ | ML+LLM 통합 관찰·거버넌스 플랫폼. 환각·독성·PII·프롬프트 인젝션 실시간 탐지 특화. 제조·금융 등 규제 산업 대상 | 상용 | 가능 — VPC·온프레미스·에어갭 환경 공식 지원; Trust Models가 고객 환경 내 실행 | [fiddler.ai](https://www.fiddler.ai) |

> **Humanloop**: 2025년 9월 8일 서비스 종료. 현재 W&B로 마이그레이션 권고.

---

## 3. 셀프호스트 / 온프레미스 가능 여부 요약

폐쇄망 제조사(두산) 환경에서 **데이터 반출 없이 운영** 가능한지를 기준으로 정리.

| 구분 | 솔루션 | 셀프호스트 가능 여부 |
|------|--------|-------------------|
| **완전 오픈소스 + 로컬 실행** | RAGAS, DeepEval(프레임워크), OpenAI Evals, MLflow, TruLens | 가능 — 코드만 설치, 외부 통신 없음 (단, LLM Judge 사용 시 LLM API 엔드포인트 필요) |
| **오픈소스 + 셀프호스트 서버** | Langfuse(MIT), Phoenix(ELv2), Promptfoo | 가능 — Docker/K8s 배포, 에어갭 환경도 지원 |
| **상용 엔터프라이즈 (VPC/온프레미스 옵션)** | Braintrust, LangSmith, W&B Weave, Fiddler AI | 엔터프라이즈 계약 필요 — VPC 또는 온프레미스 배포 가능; 도입 전 공식문서·PoC 확인 필수 |
| **상용 클라우드 관리형 (셀프호스트 제한)** | Arize AX | 클라우드 관리형 기본; Phoenix OSS를 셀프호스트 대안으로 병용 가능 |

> LLM-as-a-Judge 기능은 내부 LLM(온프레미스 배포된 오픈소스 모델) 또는 사내 API 게이트웨이와 연결해야 데이터가 외부로 나가지 않는다. 채점 모델 선택이 폐쇄망 운영 성패의 핵심 변수.

---

## 4. 제조 현업용 선정 기준

아래 기준은 두산 같은 제조 대기업의 폐쇄망·도메인 특수성을 반영한 우선순위 순이다.

### 4-1. 셀프호스트 / 온프레미스 (최우선)
- 사내 망에서 전체 파이프라인 실행 가능한지.
- 에어갭(인터넷 완전 차단) 환경 공식 지원 여부.
- 데이터(프롬프트·출력·정답셋)가 외부 서버로 전송되지 않는지.
- **권고:** Langfuse, Phoenix, DeepEval(프레임워크), MLflow는 오픈소스로 온프레미스 구축 시 가장 낮은 리스크.

### 4-2. 정답셋 및 실험 버전 관리
- 평가 데이터셋(정답·기대 출력)을 버전별로 등록·추적·비교할 수 있는지.
- 모델·프롬프트 변경 이력과 평가 점수를 연결해 회귀 여부를 확인할 수 있는지.
- **권고:** MLflow(실험 추적 네이티브), Braintrust, Langfuse, LangSmith가 강점.

### 4-3. 채점 기준 커스터마이즈
- 제조 도메인 전용 평가 기준(예: 설비 점검 답변의 정확도, 품질 기준 준수 여부)을 직접 정의할 수 있는지.
- LLM-as-a-Judge의 판정 프롬프트를 자유롭게 수정할 수 있는지.
- **권고:** DeepEval(G-Eval), Langfuse(커스텀 스코어러), RAGAS(커스텀 메트릭)이 유연.

### 4-4. CI/CD 연동 (회귀 테스트 자동화)
- GitHub Actions·Jenkins 등 사내 CI 파이프라인에 평가 단계를 삽입할 수 있는지.
- 품질 기준 미달 시 배포를 자동 차단(Fail gate)할 수 있는지.
- **권고:** DeepEval(pytest 네이티브), Promptfoo(CLI·GitHub Actions 내장), Braintrust(CI/CD 강점).

### 4-5. 한국어 및 도메인 적합성
- 한국어 텍스트 평가에서 충실도·관련성 지표가 제대로 작동하는지.
- 채점 LLM으로 한국어 강점 모델(예: 사내 배포 LLM, Claude, GPT-4o 등)을 유연하게 교체할 수 있는지.
- **참고:** 어떤 도구도 한국어 최적화를 공식 보장하지 않는다. PoC 단계에서 한국어 채점 정확도를 반드시 검증할 것.

### 4-6. 데이터 반출 여부 / 컴플라이언스
- 정답셋·실험 결과가 벤더 서버에 전송·저장되지 않는지.
- SOC 2·ISO 27001 등 컴플라이언스 인증 필요 여부(상용 SaaS 사용 시).
- **권고:** 오픈소스 셀프호스트 우선; 상용 SaaS는 데이터 처리 계약(DPA) 필수 확인.

---

## 5. 요약 시사점

- **폐쇄망 1순위 조합:** MLflow(버전 관리) + Langfuse(평가·어노테이션 UI) + RAGAS 또는 DeepEval(채점 라이브러리) — 전부 오픈소스, Docker/K8s 셀프호스트.
- **상용 플랫폼 고려 시:** Braintrust·LangSmith·Fiddler AI 모두 온프레미스 옵션 제공하나 엔터프라이즈 계약 필요. 규제 환경에선 Fiddler AI가 에어갭 지원이 가장 명확.
- **LLM-as-a-Judge 채점 모델:** 사내 배포 오픈소스 LLM(예: Llama, EXAONE) + LiteLLM 프록시로 내부 엔드포인트 통일하면 어느 도구든 외부 API 없이 운영 가능.
- **Humanloop는 종료(2025.9):** 이미 도입 중이라면 W&B Weave 또는 Langfuse로 마이그레이션 계획 수립 필요.
- 도구 시장은 빠르게 변한다. **선정 전 최신 릴리스 노트·라이선스·가격 정책을 공식 사이트에서 직접 확인**하고, 후보 도구에 대해 사내 환경 PoC를 수행해 한국어 채점 품질과 온프레미스 안정성을 실측할 것.

---

## 6. 출처 목록

| 이름 | URL |
|------|-----|
| RAGAS 공식 사이트 | https://ragas.io |
| RAGAS 문서 | https://docs.ragas.io |
| RAGAS GitHub | https://github.com/vibrantlabsai/ragas |
| DeepEval 공식 사이트 | https://deepeval.com |
| DeepEval — LLM-as-a-Judge 가이드(2026) | https://deepeval.com/guides/guides-llm-as-a-judge |
| Promptfoo 공식 사이트 | https://www.promptfoo.dev |
| OpenAI Evals GitHub | https://github.com/openai/evals |
| OpenAI Evals 시작 가이드 | https://developers.openai.com/cookbook/examples/evaluation/getting_started_with_openai_evals |
| MLflow 공식 사이트 | https://mlflow.org |
| MLflow LLM Evaluate 문서 | https://mlflow.org/docs/latest/llms/llm-evaluate/index.html |
| TruLens 공식 사이트 | https://www.trulens.org |
| TruLens GitHub | https://github.com/truera/trulens |
| Arize Phoenix 공식 사이트 | https://phoenix.arize.com |
| Arize Phoenix OSS | https://arize.com/phoenix-oss |
| Arize AI 공식 사이트 | https://arize.com |
| Langfuse 공식 사이트 | https://langfuse.com |
| Langfuse 셀프호스트 가이드 | https://langfuse.com/self-hosting |
| Langfuse GitHub | https://github.com/langfuse/langfuse |
| LangSmith 공식 사이트 | https://smith.langchain.com |
| LangSmith 셀프호스트 문서 | https://docs.langchain.com/langsmith/self-hosted |
| Braintrust 공식 사이트 | https://www.braintrust.dev |
| Braintrust — 셀프호스트 평가 도구 비교(2026) | https://www.braintrust.dev/articles/best-self-hosted-ai-evals-tools-2026 |
| W&B Weave 공식 사이트 | https://wandb.ai/site/weave/ |
| W&B Weave 문서 | https://docs.wandb.ai/weave |
| Fiddler AI 공식 사이트 | https://www.fiddler.ai |
| Humanloop 종료 안내(W&B) | https://wandb.ai/wandb_fc/product-announcements-fc/reports/Humanloop-is-Sunsetting-Migrate-to-Weights-Biases-as-an-alternative--VmlldzoxMzk4ODc1Nw |
| LLM 평가 프레임워크 비교(helpmetest, 2026) | https://helpmetest.com/blog/llm-evaluation-frameworks/ |
| LLM 평가 플랫폼 비교(Arize, 2025) | https://arize.com/llm-evaluation-platforms-top-frameworks/ |
| LangSmith vs Arize vs Braintrust 비교(Medium) | https://anudeepsri.medium.com/langsmith-vs-arize-vs-braintrust-e397e4728a76 |
| Langfuse vs LangSmith(Techsy) | https://techsy.io/en/blog/langfuse-vs-langsmith |
