# E-2 합성데이터 — 솔루션·도구 리서치 (R2 클러스터)

> 조사 관점: "AI를 만드는 도구"가 아니라 **합성 데이터를 만들어 AI 입력 데이터를 확보·보강하는 도구**로 분류
> 조사 기준일: 2026-06-22
> 독자: 제조 현업(두산전자) — 러닝 예시 = CCL Delamination 불량 이미지/품질 데이터

---

## 1. 정형·시계열 합성 도구 (Tabular / Time-series)

### 1-1. 오픈소스

| 도구 | 한 줄 설명 | 지원 데이터 유형 | 배포 방식 | 공식 URL |
|------|-----------|----------------|---------|---------|
| **SDV (Synthetic Data Vault)** | 정형·관계형·시계열 합성의 사실상 표준 오픈소스 프레임워크. CTGAN·TVAE·Gaussian Copula 등 복수 모델 내장. MIT 데이터·AI 연구소에서 시작, 현재 DataCebo 운영 | 단일 테이블, 관계형 DB, 시계열 | 오픈소스(Python 패키지), 온프레미스 자체 설치 가능 | [sdv.dev](https://sdv.dev/) |
| **YData (ydata-synthetic)** | 정형·시계열 합성에 특화된 오픈소스 Python 패키지. GAN·VAE 기반. YData Fabric 플랫폼의 무료 코어 | 정형, 시계열 | 오픈소스(PyPI), 온프레미스 가능 | [ydata.ai](https://ydata.ai/) · [docs.synthetic.ydata.ai](https://docs.synthetic.ydata.ai/) |
| **SmartNoise SDK (OpenDP)** | Microsoft·Harvard 공동 개발. 차분 프라이버시(Differential Privacy)를 적용한 합성데이터 생성. 개인정보 보호 강도 수치로 제어 가능 | 정형(표 형태) | 오픈소스(Python 패키지), 온프레미스 가능 | [smartnoise.org](https://smartnoise.org/) · [docs.smartnoise.org](https://docs.smartnoise.org/) |

**제조 현업 적용 포인트**
- SDV는 MES·ERP·품질 이력 등 관계형 테이블 합성에 바로 적용 가능. CTGAN·TVAE 모델로 Delamination 불량처럼 불균형 데이터 증강에 활용
- SmartNoise는 인사·급여 등 개인정보 포함 테이블에 차분 프라이버시 보장이 필요할 때 사용

---

### 1-2. 상용 플랫폼

| 도구 | 한 줄 설명 | 지원 데이터 유형 | 배포 방식 | 공식 URL |
|------|-----------|----------------|---------|---------|
| **MOSTLY AI** | TabularARGN 모델 기반 고품질 정형·텍스트 합성. 웹 UI 제공, 비데이터과학자도 사용 가능. 2026년 3월 Syntho와 합병(현황 확인 필요) | 정형, 텍스트 | 클라우드(SaaS), 온프레미스(엔터프라이즈) | [mostly.ai](https://mostly.ai/) |
| **Gretel AI** | 2025년 3월 NVIDIA가 3억 2천만 달러에 인수. gretel.ai 도메인은 현재 nvidia.com으로 리디렉션. NVIDIA Synthetic Data Generation for Agentic AI로 통합됨 | 정형, 텍스트, 코드 | 클라우드(NVIDIA 인프라로 통합) | [gretel.ai](https://www.gretel.ai/) → NVIDIA 통합 |
| **Tonic.ai** | 소프트웨어 개발·AI 훈련용 테스트 데이터 합성에 특화. Fabricate(합성 생성), Structural(마스킹+합성), Datasets(도메인별 데이터셋) 3종 제품 구성. HIPAA·GDPR 준수 | 정형, 텍스트 | 클라우드(SaaS), 온프레미스 가능(공식문서 확인) | [tonic.ai](https://www.tonic.ai/) |
| **Syntho** | AI 생성 합성 + 규칙 기반 합성 + 데이터 마스킹 통합 플랫폼. 온프레미스 배포 중심("데이터가 사내를 벗어나지 않음" 명시). PII 자동 스캐너 내장. 2025년 MOSTLY AI와 합병(현황 확인 필요) | 정형 | 온프레미스·클라우드 | [syntho.ai](https://www.syntho.ai/) |
| **Hazy (now SAS Data Maker)** | 2024년 11월 SAS가 인수, 현재 SAS Data Maker로 통합. 차분 프라이버시·익명화 기반의 금융·의료용 엔터프라이즈 합성 플랫폼 | 정형 | SAS 제품군으로 통합(공식문서 확인) | [hazy.com](https://hazy.com/) → SAS 통합 |
| **Synthesized** | 영국 기반. SAP 테스트 환경·CI/CD 파이프라인 연동에 강점. GDPR·HIPAA·CCPA 준수. "Data as Code" 접근 방식 | 정형 | 클라우드(SaaS), SDK 별도 제공 | [synthesized.io](https://www.synthesized.io/) |

> ⚠️ **M&A 현황 주의**: Gretel(NVIDIA 인수), Hazy(SAS 인수), MOSTLY AI·Syntho 합병 등 2024~2026년 사이 상용 플랫폼 M&A가 활발. 도입 전 현재 운영 상태·제품 로드맵 공식 확인 필요.

---

## 2. 이미지·비전 합성 도구 (Computer Vision / 제조 불량 이미지용)

| 도구 | 한 줄 설명 | 제조 적용 포인트 | 배포 방식 | 공식 URL |
|------|-----------|---------------|---------|---------|
| **NVIDIA Omniverse Replicator** | NVIDIA Omniverse 기반 물리 기반 렌더링 합성데이터 생성 프레임워크. 3D CAD 모델로 결함 이미지·검사 이미지 대량 생성 가능. Siemens SynthAI와 연동해 전자부품 검사에 실사용 사례 존재(2026-03 기준) | CCL Delamination 결함 텍스처를 3D 기판 모델에 적용 → 다양한 촬영 각도·조명 조건의 불량 이미지 대량 생성. "모델 개발 기간 수개월 → 수일 단축" 보고 | 온프레미스(GPU 서버), 클라우드 | [developer.nvidia.com/omniverse](https://developer.nvidia.com/omniverse) · [Replicator 문서](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html) |
| **Unity Perception** | Unity 엔진 기반 컴퓨터 비전 합성데이터 생성 패키지. 3D 씬에서 도메인 무작위화(Domain Randomization)로 다양한 조건 이미지 생성. Ground truth 자동 주석 | 제조 결함 탐지 모델용 학습 이미지 생성. 자동차·제조 분야 사용 사례 있음 | 오픈소스(GitHub), 온프레미스 | [GitHub](https://github.com/Unity-Technologies/com.unity.perception) · [Unity 문서](https://docs.unity3d.com/Packages/com.unity.perception@1.0/manual/index.html) |

### 전통적 데이터 증강(Augmentation) vs 합성 생성 — 구분

| 구분 | 전통적 증강 | 합성 생성 |
|------|-----------|---------|
| 방식 | 기존 이미지 회전·뒤집기·밝기 조정·크롭 등 변형 | 3D 렌더링·생성 모델로 없던 이미지 생성 |
| 원본 데이터 필요 | 필요(원본 존재해야 변형 가능) | 불필요(원본 0건에서 생성 가능) |
| 희귀 불량 대응 | 제한적(원본이 적으면 증강도 적음) | 우수(결함 유형·조건 설계해 생성) |
| 구현 난이도 | 낮음(albumentations 등 라이브러리) | 높음(3D 모델·렌더 환경 필요) |
| 현실성 | 원본 의존 | 물리 기반 렌더링 시 매우 높음 |

---

## 3. 검증·품질 평가 도구

| 도구 | 한 줄 설명 | 주요 기능 | 배포 방식 | 공식 URL |
|------|-----------|---------|---------|---------|
| **SDMetrics** | SDV 에코시스템의 합성데이터 품질·프라이버시 평가 라이브러리. 단일 테이블·관계형 데이터 평가. 시각화 리포트 자동 생성 | 통계 유사도(KS-test·PSI), 상관관계 보존, 프라이버시 위험(Singling Out·Linkability·Inference) 평가 | 오픈소스(Python), 온프레미스 | [docs.sdv.dev/sdmetrics](https://docs.sdv.dev/sdmetrics) · [GitHub](https://github.com/sdv-dev/SDMetrics) |
| **Great Expectations (GX Core)** | 데이터 품질 검증 오픈소스 프레임워크. 합성데이터 생성 후 업무 규칙 준수 여부·값 범위·타입 검증에 활용. Apache 2.0 라이선스(영구 무료) | Expectation 기반 규칙 정의, 배치/스트림 검증, 검증 결과 리포트(Data Docs) 자동 생성 | 오픈소스(Python), 온프레미스 | [greatexpectations.io](https://greatexpectations.io/) · [docs.greatexpectations.io](https://docs.greatexpectations.io/) |

**제조 현업 활용 포인트**
- SDMetrics: SDV로 생성한 Delamination 합성데이터의 통계 품질(분포 유사도·변수 관계 보존도) 및 재식별 위험 자동 측정
- Great Expectations: 합성데이터에 업무 규칙 검증 — `온도 > 0`, `불량률 >= 0`, `퇴사일 >= 입사일` 같은 물리적·업무적 제약 위반 자동 탐지

---

## 4. 도구 선정 기준 (제조 보안 환경 관점)

| 선정 기준 | 설명 | 제조 온프렘 중요도 |
|---------|------|---------------|
| 데이터 유형 커버리지 | 정형·시계열·이미지 중 어디까지 지원하는가 | 높음 |
| 실데이터 닮음(Fidelity) | 통계 분포·변수 관계를 얼마나 잘 보존하는가 | 높음 |
| 프라이버시 보존 | 차분 프라이버시(DP) 지원 여부 | 중간(B2B 제조는 개인정보보다 기밀정보) |
| 재식별 위험 평가 기능 | Singling Out·Linkability·Inference 평가 도구 내장 여부 | 높음 |
| **온프레미스·셀프호스트 가능** | 데이터가 사외 클라우드로 나가지 않고 사내에서 처리 가능한가 | **매우 높음** (제조 보안 환경 필수) |
| PoC 용이성 | Python 패키지 또는 Docker로 빠른 시작 가능 여부 | 높음 |
| 라이선스 | 오픈소스(무료) vs 상용(구독·계약) | 중간 |

### 제조 온프렘 환경 추천 조합 (PoC 시작용)

```
정형 데이터 합성:  SDV(오픈소스, sdv.dev) — 온프렘 Python 환경에서 즉시 설치
품질 검증:        SDMetrics(오픈소스, docs.sdv.dev/sdmetrics) — SDV 연동 내장
업무 규칙 검증:    Great Expectations(오픈소스, greatexpectations.io) — 규칙 기반 검증
이미지 합성:       NVIDIA Omniverse Replicator(GPU 서버 필요, developer.nvidia.com/omniverse)
상용 검토:         Syntho(온프렘 배포 명시, syntho.ai) — 도입 검토 시 PoC 요청
```

---

## 5. 도구 종합 비교표

| 도구 | 유형 | 정형 | 시계열 | 이미지 | 온프렘 | DP 지원 | 오픈소스 | 공식 URL |
|------|------|:---:|:----:|:----:|:----:|:------:|:------:|---------|
| SDV | 오픈소스 | ✓ | ✓ | - | ✓ | 일부 | ✓ | sdv.dev |
| YData | 오픈소스 | ✓ | ✓ | - | ✓ | - | ✓ | ydata.ai |
| SmartNoise | 오픈소스 | ✓ | - | - | ✓ | ✓ | ✓ | smartnoise.org |
| MOSTLY AI | 상용 | ✓ | - | - | 엔터프라이즈 | ✓ | - | mostly.ai |
| Gretel(→NVIDIA) | 상용 | ✓ | ✓ | - | 확인 필요 | ✓ | - | gretel.ai(리디렉션) |
| Tonic.ai | 상용 | ✓ | - | - | 확인 필요 | - | - | tonic.ai |
| Syntho | 상용 | ✓ | - | - | ✓(명시) | - | - | syntho.ai |
| Hazy(→SAS) | 상용 | ✓ | - | - | SAS 통합 | ✓ | - | hazy.com |
| Synthesized | 상용 | ✓ | - | - | SDK 제공 | - | - | synthesized.io |
| NVIDIA Replicator | 이미지 | - | - | ✓ | ✓(GPU) | - | 일부 | developer.nvidia.com/omniverse |
| Unity Perception | 이미지 | - | - | ✓ | ✓ | - | ✓ | github.com/Unity-Technologies/com.unity.perception |
| SDMetrics | 검증 | ✓ | ✓ | - | ✓ | - | ✓ | docs.sdv.dev/sdmetrics |
| Great Expectations | 검증 | ✓ | ✓ | - | ✓ | - | ✓ | greatexpectations.io |

---

## 출처 (접속일: 2026-06-22)

- [SDV 공식 사이트](https://sdv.dev/)
- [SDV 공식 문서](https://docs.sdv.dev/sdv)
- [SDV GitHub](https://github.com/sdv-dev/SDV)
- [SDMetrics 공식 문서](https://docs.sdv.dev/sdmetrics)
- [SDMetrics GitHub](https://github.com/sdv-dev/SDMetrics)
- [YData 공식 사이트](https://ydata.ai/)
- [YData Synthetic 문서](https://docs.synthetic.ydata.ai/)
- [SmartNoise 공식 사이트](https://smartnoise.org/)
- [SmartNoise 문서](https://docs.smartnoise.org/)
- [OpenDP 공식 사이트](https://opendp.org/)
- [MOSTLY AI 공식 사이트](https://mostly.ai/) ⚠️ Syntho 합병 이후 현황 확인 필요
- [Gretel AI](https://www.gretel.ai/) → NVIDIA 인수 후 통합됨
- [Tonic.ai 공식 사이트](https://www.tonic.ai/)
- [Syntho 공식 사이트](https://www.syntho.ai/) ⚠️ MOSTLY AI 합병 이후 현황 확인 필요
- [Hazy 공식 사이트](https://hazy.com/) → SAS Data Maker로 통합됨
- [Synthesized 공식 사이트](https://www.synthesized.io/)
- [NVIDIA Omniverse 개발자 허브](https://developer.nvidia.com/omniverse)
- [NVIDIA Omniverse Replicator 문서](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html)
- [Unity Perception GitHub](https://github.com/Unity-Technologies/com.unity.perception)
- [Unity Perception 공식 문서](https://docs.unity3d.com/Packages/com.unity.perception@1.0/manual/index.html)
- [Great Expectations 공식 사이트](https://greatexpectations.io/)
- [Great Expectations 문서](https://docs.greatexpectations.io/)
- [NVIDIA 기술 블로그 — 결함 탐지 합성데이터](https://developer.nvidia.com/blog/how-to-train-a-defect-detection-model-using-synthetic-data-with-nvidia-omniverse-replicator/)

---

> **솔루션 2층 구조 메모**: 이 파일(R2 클러스터)의 도구 비교는 E-2 주제 가이드의 솔루션 섹션(1층 — 이 주제 관점 기능 비교)에 반영한다. 솔루션 묶음 선정·플랫폼×주제 매트릭스는 `전체 목차/01 Tech Stack 비교 (솔루션×주제).md`(2층 정본)가 전담한다.
