# SDV (Synthetic Data Vault) by DataCebo

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | DataCebo Inc. (미국, MIT CSAIL 스핀오프) |
| 라이선스 | BSL(Business Source License) Community + 상용 Enterprise |
| 배포 형태 | Python 오픈소스 라이브러리, SDV Enterprise (클라우드·온프레미스) |
| 최신 동향 | SDV 최대 오픈소스 정형 합성 데이터 생태계; Community 버전 무료 제공; Enterprise 번들로 추가 모델·기능 제공; GaussianCopula(통계)~CTGAN(딥러닝) 다양한 모델 제공 |

---

## 한 줄 포지셔닝

> **오픈소스 Python 정형 합성 데이터의 사실상 표준 — 단일 테이블, 다중 테이블(관계형), 시계열 데이터를 GaussianCopula~CTGAN으로 합성**

---

## 주요 기능

### 지원 데이터 유형 및 합성 모델

| 데이터 유형 | 모델 | 특징 |
|---|---|---|
| **단일 테이블** | GaussianCopula | 통계적 공분산 구조 보존 |
| 단일 테이블 | CTGAN | 심층 학습, 불균형 범주형 처리 |
| 단일 테이블 | CopulaGAN | CTGAN + Copula 결합 |
| 단일 테이블 | TVAE | Variational Autoencoder 기반 |
| **다중 테이블** | HMA1 | 계층적 모델, 외래키 관계 보존 |
| **시계열** | PAR | 자기회귀 모델, 시간 패턴 보존 |

### 데이터 생성
- 단일 테이블, 다중 연결 테이블(관계형), 순차(시계열) 데이터 생성
- 합성 데이터 샘플링: 원본 크기 대비 확장·축소 가능

### 데이터 평가 (Quality Report)
- 합성 데이터 vs 실 데이터 유사도 측정
- 컬럼별 분포 비교, 상관관계 보존 여부
- 프라이버시 보호 수준 측정 (멤버십 추론 공격 시뮬레이션)
- **진단(Diagnostic)**: 문제 탐지 → 품질 리포트 자동 생성

### 데이터 전처리 및 제약 조건
- 민감 컬럼 익명화 옵션
- 비즈니스 규칙 제약 조건 정의 (논리적 일관성 보장)
- 결측값 처리, 데이터 타입 자동 감지

### SDV Community vs Enterprise

| 기능 | Community | Enterprise |
|---|:---:|:---:|
| 기본 합성 모델 | ○ | ○ |
| 다중 테이블 HMA1 | ○ | ○ |
| 고급 합성 모델 | × | ○ (Bundle) |
| 엔터프라이즈 지원 | × | ○ |
| SLA | × | ○ |

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 관련도 | 비고 |
|---|:---:|---|
| E-2 합성 데이터 | ★★★ | 핵심 기능, 정형 데이터 합성 |
| 데이터 프라이버시·보안 | ★★★ | 익명화, 프라이버시 평가 |
| 데이터 품질 | ★★★ | 품질 리포트, 진단 |
| 학습 데이터 증강 | ★★★ | 부족 데이터·희귀 케이스 생성 |
| 데이터 파이프라인 | ★★☆ | Python scikit-learn 스타일 API |

---

## 강점

- **오픈소스 Python 표준**: pip install sdv 한 줄 설치, scikit-learn 스타일 API — 진입 장벽 최저
- **다중 테이블 관계형 합성**: 외래키 관계·참조 무결성 보존 합성 (경쟁사 대부분 미지원)
- **다양한 합성 모델**: 통계(GaussianCopula)~딥러닝(CTGAN·TVAE) 선택 가능
- **품질 평가 내장**: 합성 vs 실 데이터 유사도·프라이버시 리포트 자동 생성
- **MIT 기원**: 학술 검증 기반, 논문·벤치마크 풍부

---

## 약점·주의점

- **텍스트/비정형 데이터 미지원**: 정형 테이블 전용 (텍스트 합성 필요 시 Gretel 사용)
- **대규모 테이블 성능**: 컬럼 수 많고 복잡한 테이블에서 학습 시간·메모리 증가
- **차등 프라이버시(DP) 제한**: 엄격한 수학적 DP 보장은 제한적 (MOSTLY AI 대비)
- **엔터프라이즈 기능**: 고급 모델·지원은 유료 Bundle 필요
- **GUI 없음**: CLI/Python API 전용 — 비기술 사용자 접근성 낮음

---

## 가격 모델

| 플랜 | 가격 | 주요 내용 |
|---|---|---|
| SDV Community | 무료 (BSL) | PyPI 설치, 기본 모델 전부 |
| SDV Enterprise | 연간 계약 (문의) | 고급 모델 Bundle, SLA, 전용 지원 |

> BSL 라이선스: 비상업적 및 소규모 상업 사용 무료, 대규모 상업 배포 시 상용 라이선스 필요 (DataCebo 문의)

---

## 연동 생태계

```
Python: pip install sdv, scikit-learn 스타일 fit/sample API
Pandas: DataFrame 직접 입력·출력
데이터베이스: CSV, Parquet, 직접 DB 커넥터(Enterprise)
Jupyter Notebook: 인터랙티브 탐색 지원
평가: sdv.evaluation 모듈 (품질·프라이버시 리포트)
```

---

## 최신 동향 (2025~2026)

- **지속**: SDV 최대 정형 합성 생태계로 성장 — GitHub 스타 증가, 활발한 기여
- **지속**: GaussianCopula~CTGAN~TVAE 모델 지속 개선 (정확도·속도)
- **지속**: 다중 테이블 HMA 알고리즘 강화 — 복잡 스키마 지원 확대
- **Enterprise Bundle**: 추가 고급 모델 신규 출시 지속
- **커뮤니티**: MOSTLY AI 비교 벤치마크 포함 다수 학술 논문에서 기준선(Baseline) 역할

---

## 제조업 활용 예시

- **희귀 불량 데이터 증강**: 정상 데이터 과다, 불량 케이스 희소 → SDV CTGAN으로 불량 클래스 합성 증강
- **설비 센서 시계열 합성**: 고장 직전 센서 패턴이 데이터 부족 시 PAR 모델로 시계열 합성
- **MES DB 프라이버시 보호**: 생산 DB를 개발·테스트 환경에 공유 시 다중 테이블 합성으로 실 데이터 노출 없이 구조·통계 보존

---

## 출처

- https://sdv.dev/
- https://github.com/sdv-dev/SDV
- https://docs.sdv.dev/sdv
- https://datacebo.com/blog/intro-to-sdv/
- https://mostly.ai/blog/a-comparison-of-synthetic-data-vault-and-mostly-ai-part-1-single-table-scenario
- https://pypi.org/project/sdv/
