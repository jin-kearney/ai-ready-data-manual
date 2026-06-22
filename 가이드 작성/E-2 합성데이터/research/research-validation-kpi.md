# 합성데이터 품질 검증·위험 관리·KPI 리서치 (R3 클러스터)

> 작성일: 2026-06-22 | 대상 가이드: E-2 합성데이터 | 담당 섹션: §3.3 Utility/Security, §3.4 품질 검증, §3.5 위험관리, §7.1 KPI, Appendix C

---

## 1. 검증 3축(Three-Axis Validation Framework)

합성데이터 품질 평가는 학계·산업계 공통으로 **충실도(Fidelity)·유용성(Utility)·프라이버시(Privacy)** 세 축으로 수행한다. 세 축은 동시에 최적화하기 어려운 트레이드오프 관계이므로, 활용 목적에 따라 우선순위를 정해야 한다.

> 출처: [AWS ML Blog — How to evaluate the quality of the synthetic data](https://aws.amazon.com/blogs/machine-learning/how-to-evaluate-the-quality-of-the-synthetic-data-measuring-from-the-perspective-of-fidelity-utility-and-privacy/) (접속일 2026-06-22)

---

### 1.1 충실도(Fidelity) — 실데이터를 얼마나 닮았는가

**핵심 질문:** 합성데이터의 분포·통계·변수 간 관계가 원본과 얼마나 일치하는가?

| 지표명 | 한글(English) | 무엇을 보나 | 쉬운 설명 | 범위/기준 |
|--------|--------------|------------|---------|---------|
| KS Complement | 콜모고로프-스미르노프 보완 지수 (KS Complement) | 수치형 변수의 분포 유사성 | 원본 분포와 합성 분포가 얼마나 겹치는지. 1에 가까울수록 좋음 | 0~1 (높을수록 좋음) |
| TV Complement | 전체변동 보완 지수 (Total Variation Complement) | 범주형 변수의 분포 유사성 | 범주별 비율이 원본과 얼마나 같은지. 1에 가까울수록 좋음 | 0~1 (높을수록 좋음) |
| Correlation Similarity | 상관관계 유사도 (Correlation Similarity) | 두 수치형 변수 간 상관관계 추이 | 온도↑ → 불량↑ 같은 변수 간 관계가 합성데이터에서도 유지되는지 | 0~1 (높을수록 좋음) |
| Contingency Similarity | 분할표 유사도 (Contingency Similarity) | 범주형 변수 간 관계 | 두 범주형 변수의 조합 빈도가 원본과 일치하는지 | 0~1 (높을수록 좋음) |

**전체 Quality Score(품질 점수):** SDMetrics Quality Report는 위 지표들을 통합해 0~100% 단일 점수로 보고. 예시: 88.7%라면 원본 분포와 약 89% 일치한다고 해석.

> 출처: [SDMetrics Quality Report 문서 — SDV](https://docs.sdv.dev/sdmetrics/data-metrics/quality/quality-report) (접속일 2026-06-22)  
> 출처: [SDMetrics Correlation Similarity — SDV](https://docs.sdv.dev/sdmetrics/data-metrics/quality/correlationsimilarity) (접속일 2026-06-22)

---

### 1.2 유용성(Utility) — AI 성능을 유지하는가

**핵심 질문:** 합성데이터로 학습한 AI 모델이 실데이터 기반 모델과 비슷한 성능을 내는가?

#### 대표 방법: TSTR (Train on Synthetic, Test on Real)

- **정의:** 합성데이터로 모델을 학습(Train)한 뒤, 실제 데이터로 평가(Test)하는 방식. 합성데이터의 실용적 품질을 직접 측정하는 가장 현실적인 방법.
- **비교 기준:** TRTR(Train on Real, Test on Real) 성능과 비교. TSTR ≈ TRTR이면 합성데이터 품질이 충분하다는 의미.
- **측정 지표:** Accuracy, F1-Score, AUC-ROC, Recall 등 다운스트림(downstream) 모델 성능 지표
- **Utility Score(활용 점수) 계산 공식:**

  ```
  Utility Score = TSTR 성능 / TRTR 성능
  ```

  예: TRTR F1 = 0.90, TSTR F1 = 0.88 → Utility Score ≈ 0.978 (약 97.8% 수준 유지)

> 출처: [AWS ML Blog — Synthetic data evaluation (Utility 섹션)](https://aws.amazon.com/blogs/machine-learning/how-to-evaluate-the-quality-of-the-synthetic-data-measuring-from-the-perspective-of-fidelity-utility-and-privacy/) (접속일 2026-06-22)  
> 출처: [Greenbook — Benchmarking Synthetic Data Quality](https://www.greenbook.org/insights/data-science/synthetic-data-introduction-benchmarking-synthetic-data-quality-metrics-and-model-performance) (접속일 2026-06-22)

#### 보조 방법: Discriminator Test (판별 검정)

- 실데이터와 합성데이터를 구분하는 분류기(classifier)를 학습시켜, **분류 정확도가 50% 내외(무작위 수준)** 이면 두 데이터를 구분할 수 없다는 의미 → 충실도 우수.

---

### 1.3 프라이버시(Privacy) — 재식별 위험이 낮은가

**핵심 질문:** 합성데이터에서 원본 데이터의 개인 또는 기밀정보를 역추적할 수 있는가?

#### 지표 1: DCR (Distance to Closest Record, 최근접 거리)

- **정의:** 합성 레코드 하나와 가장 가까운 훈련 데이터 레코드 간의 거리. 거리가 가까울수록 원본을 거의 그대로 복제했다는 신호.
- **평가 방식:** 합성 데이터셋 전체의 DCR 분포를 보류 데이터셋(holdout set) DCR과 비교.
  - **DCR 비율 ≈ 1.0** → 최적 프라이버시 (합성 레코드가 훈련 데이터와 보류 데이터에 거의 동등하게 가까움)
  - **DCR 비율 < 1.0** → 합성 레코드가 훈련 데이터에 너무 가까움 → 재식별 위험
- **Privacy Share 지표:** 합성 레코드가 훈련 데이터보다 보류 데이터에 더 가까운 비율. **이상적 목표: 50%** (순수 무작위와 같은 수준).

> 출처: [MOSTLY AI — How to benchmark synthetic data generators](https://mostly.ai/blog/how-to-benchmark-synthetic-data-generators) (접속일 2026-06-22)  
> 출처: [Synthetic Data Privacy Metrics — arxiv 2501.03941](https://arxiv.org/pdf/2501.03941) (접속일 2026-06-22)

#### 지표 2: 멤버십 추론 공격 (Membership Inference Attack, MIA)

- **정의:** 공격자가 특정 레코드가 훈련 데이터에 포함되었는지 여부를 맞출 수 있는지 테스트.
- **해석:** 공격 모델 정확도 ≈ 50% → 공격 성공 불가 → 프라이버시 우수. 정확도가 50%보다 유의미하게 높으면 → 프라이버시 취약.
- **차분 프라이버시(DP) 효과:** 차분 프라이버시 적용 시 MIA 성공률이 비적용 대비 낮아짐이 연구로 확인됨.

> 출처: [Membership Inference Attacks on Synthetic Data — apxml.com](https://apxml.com/courses/evaluating-synthetic-data-quality/chapter-4-privacy-assessment-techniques/membership-inference-attacks) (접속일 2026-06-22)

#### 개념 3: 차분 프라이버시 (Differential Privacy, DP)

- **정의:** 데이터에 수학적 노이즈를 추가하여, 어떤 개인의 데이터가 포함되거나 제외되더라도 분석 결과가 크게 달라지지 않도록 보장하는 기법. "특정 개인의 데이터가 결과에 흔적을 남기지 않는다"는 수학적 보장.
- **핵심 파라미터: ε(epsilon)** — 작을수록 강한 프라이버시, 클수록 유용성 향상.
  - ε ≤ 1: 강한 프라이버시 (합성 데이터 품질 다소 저하 가능)
  - ε ≤ 10: 합리적 프라이버시 (학계·산업 적용 다수)
  - ε > 10: 약한 프라이버시 보장
- **현업 의미:** 제조 설비 데이터처럼 기밀정보가 포함된 경우, DP 적용 합성 생성기를 선택하면 합성데이터 공유 시 법적·보안적 리스크 감소.

> 출처: [NIST — Differentially Private Synthetic Data](https://www.nist.gov/blogs/cybersecurity-insights/differentially-private-synthetic-data) (접속일 2026-06-22)  
> 출처: [NIST SP 800-226 — Guidelines for Evaluating Differential Privacy Guarantees (초안)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-226.ipd.pdf) (접속일 2026-06-22)

---

## 2. 업무 타당성 검증 (Domain Validity)

통계 지표만으로는 제조 현업의 물리·업무 제약 위반을 잡아낼 수 없다. **현업 전문가(SME) 검토**와 결합해야 한다.

| 검증 유형 | 내용 | 제조 현업 예시 |
|---------|------|-------------|
| 물리적 제약 검증 | 물리적으로 불가능한 값 탐지 | 온도 = -500℃, 압력 = 음수, 처리 시간 = 0초 |
| 업무 규칙 검증 | 공정 프로세스 순서·조건 위반 탐지 | 검사 전 출하 처리, 입사일 > 퇴사일 |
| 희소 패턴 재현성 검증 | 실데이터의 희귀 이벤트가 합성데이터에도 적절히 포함되는지 | Delamination 비율 0.2%가 합성에도 유사하게 유지되는지 |
| SME 육안 검토 | 도메인 전문가가 "이 데이터가 실제처럼 보이는가" 직접 확인 | 품질혁신팀 팀장이 Delamination 샘플 50건 검토 |

**Great Expectations** 같은 도구로 업무 규칙 위반 여부를 자동화 검증 가능.

> 출처: [Galileo AI — Master Synthetic Data Validation to Avoid AI Failure](https://galileo.ai/blog/validating-synthetic-data-ai) (접속일 2026-06-22)

---

## 3. 위험 관리 — 합성데이터의 주요 위험 4가지

### 3.1 편향 증폭 (Bias Amplification)

- **현상:** 원본 데이터의 편향(예: 특정 설비·교대조 데이터 과다)이 합성 과정에서 증폭되어 AI 모델이 더 왜곡된 판단을 내리게 됨.
- **연구 확인:** 연구에 따르면 합성데이터를 반복 학습할수록 기존 편향이 누적·강화되는 "피드백 루프(feedback loop)" 발생 가능성 확인.
- **대응:** 원본 데이터 편향 사전 진단 후 합성. 합성 비율 과다 사용 금지. 합성과 실데이터를 **반드시 혼합** 사용.

> 출처: [Fairness Feedback Loops — FAccT 2024](https://facctconference.org/static/papers24/facct24-144.pdf) (접속일 2026-06-22)

### 3.2 모드 붕괴 (Mode Collapse)

- **현상:** 생성모델(GAN 계열)이 원본의 다양한 분포 중 일부만 반복적으로 생성하여 합성데이터의 다양성이 떨어지는 현상.
- **징후:** 합성데이터의 분산(variance)이 원본보다 현저히 낮음. 특정 패턴의 반복 빈도 급상승.
- **대응:** 생성 후 분포 다양성 지표(예: Coverage 지표) 확인. 원본 대비 합성데이터 레코드 다양성 측정.

> 출처: [Preventing Model Collapse — apxml.com](https://apxml.com/courses/synthetic-data-llm-pretrain-finetune/chapter-6-evaluating-synthetic-data-challenges/countering-model-performance-degradation) (접속일 2026-06-22)

### 3.3 현실 왜곡 위험 (Reality Distortion)

- **현상:** 합성데이터를 실데이터로 혼동하거나, 합성 비율이 지나치게 높아 AI 모델이 실제 현장과 괴리된 패턴을 학습.
- **핵심 대응: Synthetic Tag 의무화** — 데이터셋마다 합성 여부를 명시적으로 표시해 실데이터와 혼동 방지.
- **관리 항목:** 생성 목적, 생성 방식, 생성 일자, 버전, 합성 비율(전체 학습 데이터 중 합성 비중).

### 3.4 재식별 위험 (Re-identification Risk)

기존 초안(§3.3)의 Singling Out / Linkability / Inference 분류가 적절함. 보강 사항:

| 위험 유형 | 정의 | 평가 방법 |
|---------|------|---------|
| Singling Out | 합성 레코드가 특정 개인·설비를 유일하게 식별 가능 | DCR 이상 탐지, SME 검토 |
| Linkability | 합성 데이터 + 외부 데이터 결합으로 특정 대상 식별 | 결합 가능 키 컬럼 마스킹 여부 확인 |
| Inference | 합성 데이터에서 민감정보(급여·고장원인) 역추론 가능 | 멤버십 추론 공격 테스트 |

> 출처: [Truly anonymous synthetic data — MOSTLY AI](https://mostly.ai/blog/truly-anonymous-synthetic-data-legal-definitions-part-ii) (접속일 2026-06-22)

### 3.5 거버넌스 체계

기존 초안 §3.5의 Synthetic Tag / 접근권한 / 모니터링 / 폐기 관리 구조는 유효. 아래 항목 추가 권장:

- **합성 비율 상한 관리:** 전체 학습 데이터 중 합성 비중을 기록. 과도한 합성 의존 방지.
- **주기적 재검증:** 합성데이터 생성 후 시간이 지나면 원본 데이터 분포가 바뀌어 합성이 현실과 멀어질 수 있음 → 분기/반기 단위 품질 재점검 권장.

---

## 4. 성과 지표(KPI) 5개 — 정식 지표명·측정 방법 정리

| # | KPI 이름 | 쉬운 의미 | 측정 방법 | 방향 | 비고 |
|---|---------|---------|---------|------|------|
| 1 | **통계 유사도 점수 (Quality Score)** | 합성 분포가 원본 분포와 얼마나 같은지 | SDMetrics Quality Score (KS Complement·TV Complement·Correlation Similarity 통합) | ↑ 높을수록 좋음 | 0~100%. PoC 기준선: 프로젝트별 합의. 도구: SDMetrics |
| 2 | **변수관계 보존율 (Correlation Similarity)** | 온도·압력·품질 간 관계가 합성에도 유지되는지 | SDMetrics Correlation Similarity 지표. Pearson 또는 Spearman 기반 | ↑ 높을수록 좋음 | 0~1. 변수 쌍별 측정 후 평균. 제조 도메인 핵심 지표 |
| 3 | **모델 성능 유지율 (TSTR Utility Score)** | 합성으로 학습한 AI가 실데이터 기반 AI 성능을 얼마나 유지하는지 | TSTR / TRTR 비율. 예: F1-Score 기준 | ↑ 1에 가까울수록 좋음 | PoC에서 기준선 설정 권장. 1.0 = 완전 유지 |
| 4 | **재식별 위험도 (DCR Privacy Share)** | 합성 레코드가 원본을 얼마나 가까이 복제했는지 | MOSTLY AI DCR 방법론 기준. Privacy Share ≈ 50%가 이상적 | 50%에 가까울수록 좋음 | 민감정보 포함 데이터셋에서 필수 측정. 도구: MOSTLY AI, SDMetrics Privacy Suite |
| 5 | **합성데이터 활용률** | 생성된 합성데이터가 실제 AI 과제에 쓰이고 있는지 | (활용 과제 수) / (생성 데이터셋 수) | ↑ 높을수록 좋음 | 관리 KPI. 낮으면 생성 후 방치되는 데이터 많다는 신호 |

> ⚠️ 구체적인 목표 수치(예: "Quality Score ≥ 85%")는 데이터 특성·활용 목적·도메인 표준에 따라 다르므로 **PoC 단계에서 원본 기준선 측정 후 팀 합의로 설정**을 권장. 업계 표준 임계값은 현재 단일 기준 없음(확인 필요).

---

## 5. 도구·방법 출처 매핑

| 도구/방법 | 주요 용도 | 링크 |
|---------|---------|------|
| SDV / SDMetrics | 충실도·유용성 검증, Quality Score 생성 | [docs.sdv.dev/sdmetrics](https://docs.sdv.dev/sdmetrics/data-metrics/quality/quality-report) |
| MOSTLY AI | DCR 기반 프라이버시 평가, 벤치마크 | [mostly.ai/blog/how-to-benchmark](https://mostly.ai/blog/how-to-benchmark-synthetic-data-generators) |
| Great Expectations | 업무 규칙·데이터 유효성 자동화 검증 | [greatexpectations.io](https://greatexpectations.io) (확인 필요) |
| NIST SP 800-226 | 차분 프라이버시 평가 가이드라인 | [nvlpubs.nist.gov NIST.SP.800-226](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-226.ipd.pdf) |
| Galileo AI 가이드 | 합성데이터 검증 실무 가이드 | [galileo.ai/blog/validating-synthetic-data-ai](https://galileo.ai/blog/validating-synthetic-data-ai) |

---

## 6. 기존 초안 대비 보강·정정 사항 요약

| 초안 항목 | 보강/정정 내용 |
|---------|-------------|
| §3.4 통계적 특성 검증 — "KS-Test" | 정식명: **KS Complement** (0~1, 높을수록 좋음). SDMetrics 기준. 기존 "KS-Test"는 p-value 기준의 가설검정 개념으로 SDMetrics 구현과 다름 |
| §3.4 활용 적합성 검증 — "AI 모델 성능 비교" | **TSTR(Train on Synthetic, Test on Real)** 방법론으로 명시. TRTR 대비 비율(Utility Score)로 표현 권장 |
| §7.1 KPI "재식별 위험도" — "Singling Out/Linkability/Inference" | 정량 지표로 **DCR (Distance to Closest Record)** 와 **Privacy Share** 추가. MIA(멤버십 추론 공격) 개념 연계 |
| §7.1 KPI "변수 관계 보존율" — "Correlation Similarity" | SDMetrics 공식 지표명 확인됨. Pearson/Spearman 기반. 링크 추가 |
| Appendix C 위험 검증 | **편향 증폭(Bias Amplification)** 및 **모드 붕괴(Mode Collapse)** 위험 항목 추가 권장 |
| §3.5 위험관리 | **합성 비율 상한 관리**, **주기적 재검증** 항목 추가 권장 |

---

## 출처 목록

1. AWS Machine Learning Blog — [How to evaluate the quality of the synthetic data](https://aws.amazon.com/blogs/machine-learning/how-to-evaluate-the-quality-of-the-synthetic-data-measuring-from-the-perspective-of-fidelity-utility-and-privacy/) (접속일 2026-06-22)
2. SDV SDMetrics — [Quality Report](https://docs.sdv.dev/sdmetrics/data-metrics/quality/quality-report) (접속일 2026-06-22)
3. SDV SDMetrics — [Correlation Similarity](https://docs.sdv.dev/sdmetrics/data-metrics/quality/correlationsimilarity) (접속일 2026-06-22)
4. MOSTLY AI — [How to benchmark synthetic data generators](https://mostly.ai/blog/how-to-benchmark-synthetic-data-generators) (접속일 2026-06-22)
5. MOSTLY AI — [Truly anonymous synthetic data](https://mostly.ai/blog/truly-anonymous-synthetic-data-legal-definitions-part-ii) (접속일 2026-06-22)
6. Galileo AI — [Master Synthetic Data Validation to Avoid AI Failure](https://galileo.ai/blog/validating-synthetic-data-ai) (접속일 2026-06-22)
7. NIST — [Differentially Private Synthetic Data](https://www.nist.gov/blogs/cybersecurity-insights/differentially-private-synthetic-data) (접속일 2026-06-22)
8. NIST — [NIST Offers Draft Guidance on Evaluating DP (SP 800-226)](https://www.nist.gov/news-events/news/2023/12/nist-offers-draft-guidance-evaluating-privacy-protection-technique-ai-era) (접속일 2026-06-22)
9. FAccT 2024 — [Fairness Feedback Loops: Training on Synthetic Data Amplifies Bias](https://facctconference.org/static/papers24/facct24-144.pdf) (접속일 2026-06-22)
10. apxml.com — [Membership Inference Attacks on Synthetic Data](https://apxml.com/courses/evaluating-synthetic-data-quality/chapter-4-privacy-assessment-techniques/membership-inference-attacks) (접속일 2026-06-22)
11. apxml.com — [Preventing Model Collapse with Synthetic Data](https://apxml.com/courses/synthetic-data-llm-pretrain-finetune/chapter-6-evaluating-synthetic-data-challenges/countering-model-performance-degradation) (접속일 2026-06-22)
12. Greenbook — [Benchmarking Synthetic Data Quality](https://www.greenbook.org/insights/data-science/synthetic-data-introduction-benchmarking-synthetic-data-quality-metrics-and-model-performance) (접속일 2026-06-22)
13. arxiv 2501.03941 — [Synthetic Data Privacy Metrics](https://arxiv.org/pdf/2501.03941) (접속일 2026-06-22)
