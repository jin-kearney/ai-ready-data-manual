# E-2 합성데이터 생성 방식 — 리서치 노트 (클러스터 R1)

> 작성 목적: §3.2 합성데이터 생성 방식을 보강·정정·출처보강하기 위한 리서치 원자료.
> 독자 = 가이드 작성자. 제조 현업(두산전자, CCL Delamination 사례) 관점 고정.
> 조사일: 2026-06-22

---

## 요약 — 기존 초안 §3.2와의 주요 차이점

| 항목 | 기존 초안 | 리서치 보강 내용 |
|---|---|---|
| Copula | 원리 간략, 출처 없음 | Sklar 정리 기반 가우시안 Copula 원리, SDV GaussianCopulaSynthesizer 출처 확보 |
| CTGAN | "범주형 특화"만 언급 | 2019 NeurIPS 논문 출처, 3대 기술 혁신(Mode-Specific Normalization·Conditional Generator·Training-by-Sampling) 상세 |
| TVAE | "잠재 공간 기반"만 언급 | VAE 프레임워크 적용 원리, ELBO 최적화, 소규모 데이터 강점 근거 |
| 시뮬레이션 | Digital Twin 나열만 | NVIDIA Omniverse Replicator 구체 사례(97.7% precision), 도메인 랜덤화 방식 |
| Diffusion | "고품질 이미지"만 언급 | 2024 논문: steel 결함 mIoU +4.95~+4.31pp, 최적 합성비율 37% 근거, 한계 |
| 시계열 | 누락 | TimeGAN 추가(NeurIPS 2019), 에너지 데이터 제조 적용 사례 |
| 정형 Diffusion | 누락 | TabDDPM 추가(ICLR 2024), 수치형+범주형 혼합 처리 방식 |
| 방식 비교표 | 설명가능성/현실성 등 6항목 | SDV 공식 비교 + 2025년 논문 벤치마크 결과 추가 |

---

## 1. 통계 기반 생성 (Statistical-Based)

### 1.1 원리

실제 데이터의 **분포(marginal distribution)와 변수 간 상관관계(dependency structure)** 를 학습하여 새 샘플을 생성한다. 복잡한 딥러닝 없이 통계 수식으로 구현하므로 설명 가능성이 높다.

### 1.2 Copula (코풀라)

**원리 한 줄:** Sklar 정리를 기반으로 각 변수의 주변분포(marginal distribution)와 변수 간 의존 구조를 분리하여 학습한 후, 의존 구조에서 새 상관 패턴을 샘플링한다.

**핵심 메커니즘:**
- 1단계: 각 열(변수)의 분포를 독립적으로 학습
- 2단계: 정규화된 열 간의 공분산 행렬(n×n)을 학습
- 결과: 각 변수 분포는 유지하면서 변수 간 관계도 함께 보존된 데이터 생성

**제조 예시:**
- CCL 공정 데이터: 온도·압력·수분 함량 3개 변수의 분포와 상관관계를 동시에 학습 → Delamination과 관련된 복합 조건 데이터를 생성
- ERP/MES 정형 생산 이력 데이터 증강에 적합

**장점:**
- 빠른 학습, 적은 계산 비용
- 소규모 데이터(수백~수천 건)에도 적용 가능
- 설명 가능성 높음(통계적 해석 가능)
- GaussianCopulaSynthesizer: SDV 공식 지원, 빠른 프로토타이핑 권장

**한계:**
- 고차원 데이터(변수 100개 이상)에서 공분산 행렬 추정 품질 저하
- 비선형 복잡 패턴 표현 제한
- 순수 범주형 필드 처리에 제약

**대표 도구:**
- [SDV GaussianCopulaSynthesizer](https://github.com/sdv-dev/SDV) — 오픈소스, pip install sdv
- [SynthCity](https://github.com/vanderschaarlab/synthcity) — Bayesian Network 포함 비교 라이브러리

**출처:**
- SDV GitHub: https://github.com/sdv-dev/SDV (접속일 2026-06-22)
- "A Comparative Study of Open-Source Libraries for Synthetic Tabular Data Generation: SDV vs. SynthCity", arXiv:2506.17847 (2025): https://arxiv.org/html/2506.17847v1

---

### 1.3 Bayesian Network (베이지안 네트워크)

**원리 한 줄:** 변수 간 인과 방향을 확률 그래프로 표현하고, 조건부 확률 분포에서 Forward Sampling으로 데이터를 생성한다.

**핵심 메커니즘:**
- 변수 간 인과관계를 방향성 비순환 그래프(DAG: Directed Acyclic Graph)로 표현
- 각 노드의 조건부 확률 분포(CPD: Conditional Probability Distribution)를 학습
- 체인 룰 P(X₁,X₂,...,Xₙ) = ∏ P(Xᵢ|Parents(Xᵢ))에 따라 순차 샘플링

**제조 예시:**
```
프리프레그 흡습
→ 수지 미경화
→ Delamination
```
이 인과 경로를 그래프로 모델링 후, "흡습률이 높을 때" 조건을 고정(conditioning)하여 후속 불량 시나리오를 생성할 수 있다.

**2024~2025 연구 결과:**
- 2025년 SDV vs. SynthCity 비교 연구(arXiv:2506.17847)에서 Bayesian Network가 1:1 비율 생성 시 통계적 유사도 96.53점(최고 성능), 예측 유용성 0.97점(최고 성능)을 기록
- 단, 1:10 확장 생성 시 성능 급락(-1.13점) — 대규모 증강 시 한계 명확

**장점:**
- 인과 구조 보존으로 "왜 이 패턴이 발생하는가" 설명 가능
- What-if 분석(특정 원인 조건 고정 후 결과 시뮬레이션) 가능
- 소규모 데이터에서 통계 기반 중 가장 높은 충실도

**한계:**
- 변수 수 증가 시 그래프 구조 설계 복잡도 급증
- 연속형 변수 처리 위해 이산화(discretization) 필요한 경우 있음
- 대규모 증강(1:10 이상)에서 품질 저하

**대표 도구:**
- [SynthCity](https://github.com/vanderschaarlab/synthcity)의 BayesianNetwork 모듈
- [pgmpy](https://pgmpy.org/) — 파이썬 확률 그래프 모델 라이브러리

**출처:**
- "Synthetic data generation with probabilistic Bayesian Networks", PMC:8848551 (2021): https://pmc.ncbi.nlm.nih.gov/articles/PMC8848551/
- "Generation and analysis of synthetic data via Bayesian networks", arXiv:2402.17915 (2024): https://arxiv.org/html/2402.17915v1
- "Synthetic data generation using Causal Models for injection molding processes", ScienceDirect (2025): https://www.sciencedirect.com/science/article/pii/S2212827125005906

---

### 1.4 기타 통계 기반 기법

| 기법 | 원리 | 적합 상황 | 비고 |
|---|---|---|---|
| Gaussian Mixture Model (GMM) | 여러 정규분포 혼합으로 복잡한 분포 근사 | 다봉 분포(multi-modal) 데이터 | ydata-synthetic 지원 |
| Marginal + Correlation | 각 열 분포를 독립 모델링 후 상관행렬로 결합 | 단순 보완 데이터 빠른 생성 | 가장 단순한 접근 |

---

## 2. 업무 규칙 기반 생성 (Rule-Based)

### 2.1 원리

**원리 한 줄:** 현업 전문가(SME: Subject Matter Expert)가 정의한 제약 조건과 규칙을 코드로 구현하여, 해당 규칙을 만족하는 데이터를 직접 생성(조건부 샘플링)한다.

### 2.2 핵심 메커니즘

```python
# 예시: 설비 과열 시나리오 규칙
if 온도 > 90°C AND 압력 < 10 bar:
    label = "과열_위험"
    generate_alarm_event()

if 냉각수_유량 < 임계치 AND 운전시간 > 6h:
    label = "냉각_이상"
```

규칙 엔진(Rule Engine) 또는 의사결정 테이블(Decision Table)을 통해 구현. 통계 학습 없이 규칙에서 직접 데이터를 생성하므로 **원본 데이터가 없어도 가능**.

### 2.3 제조 예시 (CCL/두산전자)

| 시나리오 | 규칙 | 생성 목적 |
|---|---|---|
| Delamination 위험 | 흡습률 >3% AND 경화온도 <165°C | 희귀 불량 학습 데이터 |
| 압착 불량 | 압력 편차 >5% AND 온도 균일도 <95% | 이상 탐지 모델 학습 |
| 설비 과열 | 냉각수 유량 <임계치 AND 가동시간 >N시간 | 예방정비 모델 검증 |
| 안전 비상정지 | 다수 센서 동시 이상 | 보호로직 검증 |

### 2.4 장점
- **도메인 지식 반영**: 통계 데이터가 없는 신규 설비/신규 제품에도 적용 가능
- **희귀·극한 이벤트 생성**: 실제로 거의 발생하지 않는 위험 상황을 원하는 만큼 생성
- **설명 가능성 최고**: 어떤 규칙으로 데이터가 만들어졌는지 완전히 투명
- **안전 검증 적합**: 안전 시스템·보호 로직 검증에 표준적 접근

### 2.5 한계
- **SME 의존성**: 규칙 정의를 위해 현업 전문가 시간 투자 필수
- **새 패턴 발견 불가**: 규칙에 없는 새로운 패턴은 생성 불가 (규칙 = 생성 상한)
- **규칙 유지보수 비용**: 공정 변경 시 규칙도 함께 업데이트 필요
- **변수 간 복잡 상호작용 표현 제한**: 규칙이 많아질수록 충돌·모순 위험

### 2.6 대표 도구

- Python 조건부 스크립트 (가장 단순)
- [Drools](https://www.drools.org/) — Java 오픈소스 규칙 엔진 (기업용)
- Decision Table (Excel 기반 규칙 관리)

---

## 3. 시뮬레이션 기반 생성 (Simulation-Based)

### 3.1 원리

**원리 한 줄:** 실제 물리 법칙 또는 공정 논리를 가상 환경에 구현하고, 다양한 파라미터 조합을 반복 실행하여 데이터를 생성한다.

### 3.2 핵심 방식

| 시뮬레이션 유형 | 원리 | 제조 적용 |
|---|---|---|
| **물리 기반 시뮬레이션** (Physics-based) | 열역학·유체역학·재료역학 수식을 수치적으로 풀어 거동 예측 | FEA(유한요소해석), 열-구조 해석 |
| **디지털 트윈** (Digital Twin) | 실제 설비의 가상 복제 모델. 실시간 센서와 연동되거나 독립 실행 | 설비 이상 탐지, 공정 최적화 |
| **이산 사건 시뮬레이션** (DES) | 생산 흐름을 이벤트 단위로 모델링 | 생산 스케줄링, 병목 분석 |
| **도메인 랜덤화** (Domain Randomization) | 3D 가상 환경에서 조명·텍스처·카메라 각도 등을 무작위 변경 | 비전 검사 모델용 이미지 대량 생성 |

### 3.3 도메인 랜덤화 — NVIDIA Omniverse 사례

**NVIDIA Omniverse Replicator** (공식 문서: https://developer.nvidia.com/blog/how-to-train-a-defect-detection-model-using-synthetic-data-with-nvidia-omniverse-replicator/)

워크플로우:
1. CAD 3D 모델 임포트
2. 결함(스크래치·부식·균열) 텍스처 절차적 생성
3. 도메인 랜덤화 적용: 결함 위치·크기·회전, 카메라 각도, 조명 조건을 파라미터 범위 내 무작위 변경
4. 자동 레이블(annotation) 포함 이미지 대량 생성
5. YOLOv8 등 객체 탐지 모델 학습

**실제 결과 (NVIDIA Technical Blog, 2024):**
- CAD 파일 1개만으로 합성 이미지 수천 장 생성
- 초기 모델(합성 데이터만): Precision 74%, Recall 34%, mAP 39%
- 수작업 데이터 수집 대비 비용·시간 대폭 절감
- 한계: 긴 스크래치 탐지 저조, 반사면 오탐 — 실제 데이터 보완 필요

**Databricks + NVIDIA 파이프라인 (2024):**
- 합성 데이터 생성 파이프라인을 Databricks와 통합해 확장 가능한 대규모 제조 비전 AI 데이터 준비 체계 구축
- 출처: https://www.databricks.com/blog/building-scalable-synthetic-data-generation-pipelines-perception-ai-databricks-and-nvidia

### 3.4 제조 Digital Twin 데이터 생성

2024년 Computer-Integrated Manufacturing 저널 연구(Taylor & Francis):
- 제조 생산 라인의 Digital Twin에서 생산 흐름 시뮬레이션 → 합성 생산 데이터 생성
- 실제 공장 데이터 없이도 공정 계획·분석 가능
- 전략: 랜덤 생산 라인 생성 + 거동 시뮬레이션으로 다양성 확보

**장점:**
- 실제로 만들 수 없는 극한 상황(고온·고압·안전사고) 안전하게 반복 생성
- 신규 설비·공정 설계 단계에서 사전 데이터 확보
- 비전 AI용 대량 레이블 이미지를 저비용으로 생성

**한계:**
- 구축 비용과 전문 지식 요구 수준이 높음
- 물리 모델의 현실 반영도(fidelity)에 따라 생성 데이터 품질 결정
- 시뮬레이션-현실 간격(sim-to-real gap): 합성 데이터로 학습한 모델이 실제 환경에서 성능 저하할 수 있음

### 3.5 대표 도구

| 도구 | 유형 | 용도 |
|---|---|---|
| [NVIDIA Omniverse Replicator](https://developer.nvidia.com/omniverse) | 도메인 랜덤화 | 비전 검사용 이미지 생성 |
| [AnyLogic](https://www.anylogic.com/) | 이산 사건 시뮬레이션 | 생산 흐름, 물류 |
| [Plant Simulation (Siemens)](https://www.plm.automation.siemens.com/global/en/products/manufacturing-planning/plant-simulation.html) | 디지털 팩토리 | 생산 라인 시뮬레이션 |
| [ANSYS](https://www.ansys.com/) | 물리 기반 FEA | 열-구조 해석, 재료 거동 |

---

## 4. 생성모델 기반 생성 (Generative Model-Based)

### 4.1 원리

**원리 한 줄:** 대규모 실제 데이터에서 잠재적 패턴을 학습한 딥러닝 모델이, 학습 데이터에 없는 새로운 현실적 샘플을 생성한다.

### 4.2 정형·표 데이터: CTGAN & TVAE

#### CTGAN (Conditional Tabular GAN)

**출처 논문:** "Modeling Tabular data using Conditional GAN", Xu et al., NeurIPS 2019
→ https://github.com/sdv-dev/CTGAN (공식 GitHub)

**3대 기술 혁신:**

| 혁신 | 목적 | 효과 |
|---|---|---|
| **Mode-Specific Normalization** | 연속형 변수의 다봉 분포(multi-modal) 처리 | GMM으로 각 모드를 분리 정규화 → 분포 왜곡 방지 |
| **Conditional Generator** | 범주형 변수의 불균형 처리 | 특정 범주 조건을 고정하여 균형 있게 생성 |
| **Training-by-Sampling** | 학습 중 균형 보장 | 희귀 범주 과소표현 방지 |

**적용 적합 상황:**
- 범주형 변수가 포함된 정형 데이터 (예: 불량 유형 코드, 공정 단계)
- 변수 간 비선형 복잡 패턴이 존재할 때
- 원본 데이터 규모가 어느 정도 확보될 때(수천 건 이상 권장)

**SDV 공식 권고:**
- "Large, complex datasets with non-linearities에 선호"
- 학습 불안정성(training instability), 모드 붕괴(mode collapse) 주의

#### TVAE (Tabular Variational Autoencoder)

**출처:** 동일 논문(NeurIPS 2019) — CTGAN과 함께 발표
→ https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/tvaesynthesizer

**원리:**
- VAE 프레임워크: 인코더가 데이터를 잠재 공간(latent space)으로 압축 → 디코더가 잠재 벡터에서 새 데이터 생성
- Evidence Lower Bound(ELBO) 최적화: 재구성 오류 + KL 발산의 균형
- CTGAN과 동일한 Mode-Specific Normalization 적용

**SDV 공식 권고:** "소규모 데이터에서 다양성이 중요할 때 사용"

**2025 비교 연구 결과 (arXiv:2506.17847):**
- 1:10 대규모 확장 시 SDV 내 모델 중 유일하게 양의 예측 유용성(0.31) 기록
- 즉, 원본보다 10배 많은 합성 데이터 생성이 필요할 때 CTGAN보다 TVAE가 더 안정적

#### CTGAN vs. TVAE vs. GaussianCopula 선택 기준

| 상황 | 권장 모델 | 근거 |
|---|---|---|
| 빠른 프로토타이핑, 소규모 데이터 | GaussianCopula | 빠름, 안정적, 해석 가능 |
| 범주형 변수 많고 복잡한 의존성 | CTGAN | 범주형 조건 생성 특화 |
| 소규모 데이터, 10배 이상 증강 | TVAE | 대규모 생성 시 안정성 |
| 인과 관계 보존이 중요 | Bayesian Network | 인과 구조 투명 |

*(출처: SDV 공식 문서 + arXiv:2506.17847)*

---

### 4.3 정형 데이터 Diffusion: TabDDPM

**출처:** "TabDDPM: Modelling Tabular Data with Diffusion Models", ICLR 2024
→ https://arxiv.org/abs/2209.15421

**원리:**
- 수치형 변수: Gaussian diffusion (정규 분포에서 점진적 노이즈 제거)
- 범주형 변수: Multinomial diffusion (범주 분포에서 점진적 노이즈 제거)
- Multi-layer perceptron이 각 단계의 노이즈를 학습

**GAN/VAE 대비 강점:**
- 훈련 불안정성 없음 (GAN의 mode collapse 문제 해결)
- 정형 데이터에서 CTGAN·TVAE 대비 분포 통계 보존 우수
- 클래스 컨디셔닝(class conditioning): 희귀 클래스(불량 유형)를 명시적으로 지정해 생성 가능

**한계:**
- 계산 비용 높음 (CTGAN보다 학습 시간 길다)
- 희귀 이벤트의 꼬리 분포(tail distribution) 표현에 제약

**적용 고려:**
- 정형 데이터 고품질 증강이 필요하고 계산 자원이 충분할 때
- 불균형 데이터(Delamination 0.2%)의 소수 클래스 집중 생성

---

### 4.4 이미지 데이터: Diffusion Model (확산 모델)

#### Stable Diffusion + LoRA (제조 결함 이미지)

**원리:** 사전학습된 거대 확산 모델을 적은 실제 결함 이미지(수십~수백 장)로 파인튜닝하여, 원하는 유형의 새 결함 이미지를 무제한 생성.

**2024년 제조 적용 결과 (PMC:11436218):**
- NEU-seg 스틸 표면 결함 데이터셋(긁힘·개재물·패치) 대상
- Stable Diffusion + LoRA 파인튜닝 후 합성 이미지 생성
- DeepLabV3+ mIoU: 71.31% → 76.26% (+4.95pp)
- FPN mIoU: 72.39% → 76.70% (+4.31pp)
- **최적 합성 비율: 37%** (합성 데이터가 훈련셋의 37%일 때 최고 성능)
- 50% 초과 시 성능 저하 — 과도한 합성 데이터는 오히려 악영향

**두산전자 CCL Delamination 이미지 적용 시나리오:**
- 실제 Delamination·Wicking·Void 이미지 수십 장으로 파인튜닝
- 합성 이미지 수백~수천 장 생성 → 불량 검사 AI 학습 데이터 확보
- 권장: 실제 이미지와 합성 이미지 비율 약 6:4 수준 유지

#### GAN 기반 이미지 생성

**DCGAN, CycleGAN, StyleGAN 등:**
- 2019~2022년 이전 표준. 현재는 Diffusion Model에 품질 면에서 추월됨
- 그러나 훈련 데이터 적을 때 GAN이 더 빠른 수렴 보임
- 혼합 접근: GAN으로 초기 데이터 확보 → Diffusion으로 고품질 추가 생성

**한계:**
- Diffusion: 계산 비용 높음, 도메인별 파인튜닝 데이터 최소 수십 장 필요
- GAN: mode collapse (특정 유형만 반복 생성) 위험

---

### 4.5 시계열 데이터: TimeGAN

**출처:** "Time-series Generative Adversarial Networks", NeurIPS 2019
→ https://github.com/jsyoon0823/TimeGAN

**원리:**
- 4개 네트워크 구성: Embedding Function + Recovery + Generator + Discriminator
- 잠재 공간(latent space)에서 시계열의 시간적 의존성을 학습
- Supervised loss로 실제 데이터와 합성 데이터의 시간적 패턴 동기화

**제조 적용 사례 (2024):**
- 중국 제조 공장 보드 분할 기계의 에너지 소비 데이터(2024년 9~10월 수집)
- 멀티헤드 셀프어텐션 메커니즘 추가한 개선 TimeGAN 적용
- 생성 데이터양이 원본의 2배일 때 예측 모델 정확도 최고
- RMSE·MAE 감소, R² 향상 확인

**제조 시계열 적용 사례:**
- 온도·압력·진동 센서 데이터의 이상 패턴 생성
- CCL 공정의 경화 사이클(시간-온도 프로파일) 변이 데이터 생성
- 설비 열화(degradation) 시계열 합성

**도구:**
- [ydata-synthetic](https://docs.synthetic.ydata.ai/1.3/) — TimeGAN, CTGAN, VAE 통합 지원 오픈소스

---

### 4.6 텍스트 데이터: LLM (대형 언어 모델)

**원리 한 줄:** 사전학습된 LLM에 도메인 맥락과 예시를 제공하여(Few-shot prompting), 형식과 내용이 실제와 유사한 텍스트 데이터를 생성한다.

**핵심 생성 전략 (arXiv:2503.14023, 2025):**

| 전략 | 방법 | 제조 활용 |
|---|---|---|
| **Zero-shot 생성** | 지시문만으로 생성, 예시 없음 | 작업일지 초안 생성 |
| **Few-shot 생성** | 3~5개 예시 제공 후 유사 생성 | 불량 VOC 문체 학습 |
| **Self-Instruct** | LLM이 스스로 지시문 생성 후 답변 | 다양한 점검 보고서 자동 생성 |
| **반복적 세부 생성** | 모델이 틀리는 어려운 케이스 집중 생성 | 희귀 불량 설명 텍스트 |

**제조 텍스트 적용 사례:**
- **정비 로그**: 2025년 연구(arXiv:2511.05311) — LLM 에이전트로 정비 로그의 노이즈 패턴(6가지 유형) 시뮬레이션 → 예방정비 모델 학습 데이터 정제 및 증강
- **VOC 데이터**: 개인정보 포함 고객 불만 텍스트를 LLM으로 합성 → 원본 감성·형식 유지, 개인정보 제거
- **작업일지**: 공정 이상 발생 시 작업자가 기록하는 메모 유형 합성

**한계 (실무 주의사항):**
- **할루시네이션(Hallucination)**: 실제 없는 수치·사건을 그럴듯하게 생성 — 생성 후 검토 필수
- **분포 불일치**: 합성 텍스트가 실제보다 "깔끔하고 정돈됨" — 실제 데이터의 오타·약어·구어 패턴 미반영
- **성능 한계**: 합성 vs. 실제 동일 규모 비교 시 실제 데이터 기반 모델이 대부분 우수
- **도메인 특화 노이즈**: 제조 현장 특유의 약어·전문어·스키마 지식이 부족한 경우 품질 저하

**도구:**
- GPT-4o, Claude 3.5 Sonnet (상용 API) — Few-shot 프롬프팅
- [LangChain](https://www.langchain.com/) — 프롬프트 체인·Few-shot 예시 관리
- Llama 3, Qwen 계열 (오픈소스 로컬 배포) — 기밀 데이터 외부 전송 불가 시

---

## 5. 생성 방식 선택 기준 — 의사결정 프레임워크

### 5.1 데이터 유형 × 방식 매핑

| 데이터 유형 | 1순위 | 2순위 | 주의 |
|---|---|---|---|
| 정형(표) 데이터 — 소규모 | GaussianCopula / Bayesian Network | TVAE | 딥러닝 과적합 위험 |
| 정형(표) 데이터 — 범주형 복잡 | CTGAN | TVAE | 충분한 원본 데이터 필요 |
| 정형(표) 데이터 — 고품질 증강 | TabDDPM | CTGAN | 계산 비용 높음 |
| 시계열 데이터 | TimeGAN / 시뮬레이션 | Copula | 시간 의존성 보존 확인 |
| 이미지 (결함 검사) | Diffusion (Stable Diffusion + LoRA) | NVIDIA Omniverse | 실제 이미지 수십 장 필요 |
| 이미지 (비전 3D) | NVIDIA Omniverse (도메인 랜덤화) | GAN | CAD 파일 필요 |
| 텍스트 (자연어) | LLM (Few-shot) | — | 할루시네이션 검토 필수 |
| 극한·위험 시나리오 | 업무 규칙 기반 | 시뮬레이션 | 원본 데이터 불필요 |
| 인과 관계 보존 중요 | Bayesian Network | Causal GAN | 그래프 설계 비용 |

### 5.2 목적 × 방식 매핑

| 활용 목적 | 권장 방식 | 이유 |
|---|---|---|
| 불량 데이터 불균형 해소 | CTGAN (정형) / Diffusion (이미지) | 클래스 조건 생성 지원 |
| 신규 설비 초기 데이터 | 업무 규칙 기반 + 시뮬레이션 | 실데이터 없어도 가능 |
| 개인정보 보호 | GaussianCopula / TVAE | 통계 특성 보존, 재식별 제어 용이 |
| 안전·극한 시나리오 검증 | 업무 규칙 기반 / Digital Twin | 설명 가능, 반복 가능 |
| 비전 AI 학습 이미지 대량 확보 | Diffusion / NVIDIA Omniverse | 대규모, 레이블 자동화 |
| AI 에이전트 학습용 텍스트 | LLM | 문맥·형식 유연 |

### 5.3 도메인 지식 × 원본 데이터 존재 여부

```
원본 데이터 충분?
├── YES
│   ├── 정형/시계열 → 통계 기반(Copula/BN) 또는 생성모델(CTGAN/TVAE/TabDDPM)
│   └── 이미지/텍스트 → Diffusion / LLM
└── NO (신규 설비·신규 제품)
    ├── 규칙 정의 가능? → 업무 규칙 기반
    └── 물리 모델 있음? → 시뮬레이션 기반

설명 가능성 필수?
├── YES → 통계 기반(Copula/BN) 또는 업무 규칙 기반
└── NO → 생성모델(CTGAN/TVAE/Diffusion) 가능

인과 구조 중요?
├── YES → Bayesian Network / Causal GAN
└── NO → 다른 방식 선택
```

### 5.4 실무 조합 패턴 (혼합 사용 권장)

제조 현장에서는 단일 방식보다 **두 가지 이상 조합**이 흔하다.

| 조합 패턴 | 사용 예 | 효과 |
|---|---|---|
| 통계 기반 + 업무 규칙 | ERP 데이터(Copula) + 설비 과열 규칙 주입 | 현실성 + 희귀 이벤트 보완 |
| 시뮬레이션 + Diffusion | Digital Twin → 합성 이미지 → Diffusion 다양화 | 대규모 + 고품질 이미지 |
| CTGAN + 검증(GE) | CTGAN 생성 → Great Expectations 검증 | 품질 보장된 정형 데이터 |
| LLM + 사람 검토 | LLM 초안 생성 → SME 품질 검토 | 속도 + 정확성 균형 |

---

## 6. 방식 비교표 (보강)

| 항목 | 통계 기반 | 업무 규칙 기반 | 시뮬레이션 기반 | 생성모델 기반 |
|---|---|---|---|---|
| **대표 기법** | Copula, Bayesian Network, GMM | 규칙 엔진, Decision Table | Digital Twin, Omniverse, FEA | CTGAN, TVAE, TabDDPM, Diffusion, LLM, TimeGAN |
| **원본 데이터 필요량** | 중간 (수백~수천 건) | **없어도 가능** | **없어도 가능** | 높음 (수천 건 이상 권장) |
| **설명 가능성** | 높음 | **매우 높음** | 높음 | 낮음 (블랙박스) |
| **현실성 (데이터 품질)** | 중간 | 중간 | **높음** | **매우 높음** |
| **구현 난이도** | 낮음~중간 | 중간 | **높음** | 높음 |
| **희귀 이벤트 생성** | 가능 (통계적 외삽) | **매우 우수** (직접 생성) | **매우 우수** | 가능 (조건부) |
| **비정형 데이터 처리** | 어려움 | 어려움 | 제한적 | **우수** |
| **인과 관계 보존** | Bayesian만 우수 | 설계 반영 가능 | 물리 법칙 기반 | 학습 의존적 |
| **적합 데이터 유형** | 정형·표 데이터 | 정형·규칙 기반 | 모든 유형 (비용 높음) | 정형·이미지·텍스트·시계열 |

---

## 7. 출처 목록

| 제목 | URL | 비고 |
|---|---|---|
| SDV GitHub (CTGAN, TVAE, GaussianCopula) | https://github.com/sdv-dev/SDV | 공식 오픈소스, 접속일 2026-06-22 |
| CTGAN GitHub | https://github.com/sdv-dev/CTGAN | CTGAN·TVAE 공식 저장소 |
| "Modeling Tabular data using Conditional GAN" (NeurIPS 2019) | https://github.com/sdv-dev/CTGAN | Xu et al., CTGAN·TVAE 원논문 |
| "Synthetic data generation with probabilistic Bayesian Networks" | https://pmc.ncbi.nlm.nih.gov/articles/PMC8848551/ | PMC 오픈액세스, 2021 |
| "Generation and analysis of synthetic data via Bayesian networks" (arXiv 2024) | https://arxiv.org/html/2402.17915v1 | 베이지안 네트워크 불확실성 정량화 |
| "Synthetic data generation using Causal Models for injection molding" | https://www.sciencedirect.com/science/article/pii/S2212827125005906 | ScienceDirect, 2025 |
| "A Comparative Study: SDV vs. SynthCity" (arXiv 2025) | https://arxiv.org/html/2506.17847v1 | SDV/SynthCity 벤치마크 |
| "Latent Diffusion Models for Steel Surface Defect Segmentation" | https://pmc.ncbi.nlm.nih.gov/articles/PMC11436218/ | PMC, 2024, mIoU +4.95pp |
| "TabDDPM: Modelling Tabular Data with Diffusion Models" (ICLR 2024) | https://arxiv.org/abs/2209.15421 | 정형 데이터 Diffusion |
| "Synthetic Tabular Data Generation: A Comparative Survey" (arXiv 2025) | https://arxiv.org/html/2507.11590v1 | Copula·GAN·Diffusion·Transformer 비교 |
| NVIDIA Omniverse Replicator 결함 탐지 사례 | https://developer.nvidia.com/blog/how-to-train-a-defect-detection-model-using-synthetic-data-with-nvidia-omniverse-replicator/ | NVIDIA Technical Blog |
| Databricks + NVIDIA 합성 데이터 파이프라인 | https://www.databricks.com/blog/building-scalable-synthetic-data-generation-pipelines-perception-ai-databricks-and-nvidia | Databricks Blog |
| TimeGAN GitHub (NeurIPS 2019) | https://github.com/jsyoon0823/TimeGAN | 시계열 합성 데이터 |
| "Time Series Data Augmentation with TimeGAN" (MDPI Sensors 2025) | https://www.mdpi.com/1424-8220/25/2/493 | 제조 에너지 소비 데이터 적용 |
| ydata-synthetic | https://docs.synthetic.ydata.ai/1.3/ | TimeGAN·CTGAN 통합 오픈소스 |
| "Synthetic Data Generation Using Large Language Models" (arXiv 2025) | https://arxiv.org/html/2503.14023v1 | LLM 합성 텍스트 방법론 |
| "Cleaning Maintenance Logs with LLM Agents" (arXiv 2025) | https://arxiv.org/html/2511.05311v1 | 정비 로그 LLM 적용 사례 |
| "Synthetic data generation for digital twins in manufacturing" (2024) | https://www.tandfonline.com/doi/full/10.1080/0951192X.2024.2322981 | Taylor & Francis, Digital Twin |
| "Survey of Time Series Data Generation in IoT" (PMC 2023) | https://pmc.ncbi.nlm.nih.gov/articles/PMC10422358/ | IoT 시계열 생성 방법 조사 |
