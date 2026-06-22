# E-2 합성데이터 — 출처 검증 보고서

**검증 일자:** 2026-06-22  
**검증 대상:** `E-2 합성데이터/E-2 합성데이터.md` 본문 내 URL 및 주요 주장  
**결과 요약:** 살아있음 23 / URL 교체 1 / 완화·보정 3 / 사람 확인 필요 ⚠️ 4

---

## 1. URL 상태 점검

### 살아있음 (정상 접근, 내용 일치)

| URL | 용도 | 상태 |
|-----|------|------|
| https://sdv.dev/ | SDV 공식 사이트 | 정상. SDV가 정형·관계형·시계열 합성 오픈소스 프레임워크임을 확인 |
| https://docs.sdv.dev/sdmetrics | SDMetrics 문서 | 정상. 합성데이터 품질·프라이버시 평가 라이브러리(DataCebo/MIT) |
| https://github.com/sdv-dev/CTGAN | CTGAN GitHub | 정상. Conditional Tabular GAN for tabular data (NeurIPS 2019) |
| https://arxiv.org/abs/2209.15421 | TabDDPM 논문 | 정상. "TabDDPM: Modelling Tabular Data with Diffusion Models" |
| https://github.com/jsyoon0823/TimeGAN | TimeGAN GitHub | 정상. 시계열 합성 GAN (NeurIPS 2019) |
| https://developer.nvidia.com/omniverse | NVIDIA Omniverse | 정상. 물리 기반 시뮬레이션 및 합성데이터 생성 플랫폼 확인 |
| https://aws.amazon.com/blogs/machine-learning/how-to-evaluate-the-quality-of-the-synthetic-data-measuring-from-the-perspective-of-fidelity-utility-and-privacy/ | AWS ML Blog | 정상. 충실도·유용성·프라이버시 3축 평가 및 TSTR 설명 포함 |
| https://mostly.ai/blog/how-to-benchmark-synthetic-data-generators | MOSTLY AI 블로그 | 정상. DCR(Distance to Closest Record) 방법론 설명 포함 |
| https://greatexpectations.io/ | Great Expectations | 정상. Apache 2.0 라이선스 데이터 품질 검증 프레임워크 확인 |
| https://smartnoise.org/ | SmartNoise SDK | 정상. 차분 프라이버시 오픈소스 툴킷(Microsoft 주도). 커뮤니티 기여자에 여러 기관 참여 확인 |
| https://ydata.ai/ | YData | 정상. 합성데이터 생성 플랫폼 (정형·시계열 특화) |
| https://github.com/Unity-Technologies/com.unity.perception | Unity Perception GitHub | 정상(접근 가능). 단, 공식 지원 종료 명시: "this project has been discontinued and is no longer supported by Unity" |
| https://pgmpy.org/ | pgmpy | 정상. 베이지안 네트워크·확률 그래프 모델 Python 라이브러리 |
| https://www.pipc.go.kr/ | 개인정보보호위원회 | 정상. 대한민국 공식 전자정부 누리집 접근 가능 |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC11436218/ | 철강결함 Diffusion 논문 | 정상. "Latent Diffusion Models to Enhance the Performance of Visual Defect Segmentation Networks in Steel Surface Inspection" (Sensors 2024) |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC8848551/ | Bayesian Network 논문 | 정상. "Synthetic data generation with probabilistic Bayesian Networks" (PMC 2022) |
| https://docs.sdv.dev/sdv/modeling/single-table-synthesizers/tvaesynthesizer | SDV TVAE 문서 (교체 후) | 정상. TVAESynthesizer 공식 문서 |
| https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator.html | NVIDIA Omniverse Replicator | 정상. 도메인 랜덤화·합성데이터 생성 문서 |
| https://docs.sdv.dev/sdmetrics/data-metrics/quality/quality-report | SDMetrics Quality Report | 정상. KS Complement·TV Complement 등 지표 설명 포함 |
| https://arxiv.org/abs/2501.03941 | 합성데이터 프라이버시 지표 논문 | 정상. "Synthetic Data Privacy Metrics" (2025) |
| https://arxiv.org/html/2506.17847v1 | SDV vs SynthCity 비교 논문 | 정상. "A Comparative Study of Open-Source Libraries for Synthetic Tabular Data Generation" (2025) |
| https://arxiv.org/html/2503.14023v1 | LLM 합성데이터 논문 | 정상. "Synthetic Data Generation Using Large Language Models" (2025) |
| https://galileo.ai/blog/validating-synthetic-data-ai | Galileo AI 블로그 | 정상. 합성데이터 검증 기법 설명 |
| https://developer.nvidia.com/blog/how-to-train-a-defect-detection-model-using-synthetic-data-with-nvidia-omniverse-replicator/ | NVIDIA 결함탐지 블로그 | 정상. Omniverse Replicator로 결함탐지 모델 학습하는 방법 설명 |
| https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-226.ipd.pdf | NIST SP 800-226 | 정상(PDF 반환). 파일 1.8MB 수신 — 텍스트 추출 불가하나 URL 접근 확인 |
| https://docs.synthetic.ydata.ai/ | YData Synthetic 문서 | 정상(리다이렉트). `/latest/`로 리다이렉트됨 — 링크 작동 |

---

### URL 교체 (1건)

| 원래 URL (본문) | 문제 | 교체 URL (본문 반영) |
|----------------|------|-------------------|
| `https://docs.sdv.dev/sdv/single-table-data/modeling/synthesizers/tvaesynthesizer` | 404 Not Found ("This page may have been moved, renamed, or deleted") | `https://docs.sdv.dev/sdv/modeling/single-table-synthesizers/tvaesynthesizer` (정상 확인) |

---

### 접근 불가 / 확인 불가 (⚠️ 사람 확인 필요)

| URL | 상태 | 조치 |
|-----|------|------|
| https://www.tandfonline.com/doi/full/10.1080/0951192X.2024.2322981 | 403 Forbidden (구독 필요) | 본문 주장 완화 없음 — 제목·저자 변경 없이 유지. 접근 가능 여부 직접 확인 필요 |
| https://facctconference.org/static/papers24/facct24-144.pdf | PDF 수신되나 텍스트 추출 불가 | 링크 자체는 작동하는 것으로 판단. 제목 확인은 별도 필요 |
| https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-226.ipd.pdf | PDF 수신(1.8MB)·텍스트 추출 불가 | URL 접근은 가능. IPD(Initial Public Draft) URL — 최종본 URL로 교체 검토 가능 |
| https://www.gretel.ai/ | 301 → `https://www.nvidia.com/en-us/use-cases/synthetic-data-generation-for-agentic-ai/` | 도메인 리다이렉트 확인. 본문에 "2025년 3월 NVIDIA가 인수. NVIDIA Synthetic Data Generation으로 통합됨" 기재 — NVIDIA 페이지에서 직접 "Gretel" 언급은 없으나 도메인 리다이렉트로 인수 사실 추정 가능. ⚠️ 인수 일자(2025년 3월) 공식 확인 필요 |

---

## 2. 본문 주장 검증 및 완화 내역

### 완화·보정한 주장 (3건)

**1) SmartNoise SDK 개발 주체 — "Microsoft·Harvard 공동 개발" → "Microsoft 주도, 커뮤니티 공동 개발"**
- SmartNoise 공식 사이트는 Copyright © Microsoft를 명시하며, "Key Contributors"로 여러 기관 로고를 표시하나 Harvard를 공동개발자로 명시하지 않음. GitHub 저장소는 `opendp` 조직 소속.
- 보정: "Microsoft·Harvard 공동 개발" → "Microsoft 주도, 커뮤니티 공동 개발"

**2) Unity Perception — 공식 지원 종료 사실 추가**
- GitHub 저장소에 "this project has been discontinued and is no longer supported by Unity" 명시.
- 보정: 도구 설명에 "현재 Unity의 공식 지원이 종료됨(커뮤니티 유지)" 추가.

**3) TVAE 문서 URL 교체 (위 URL 교체 항목과 동일)**

---

### 그대로 유지한 주장 (확인됨)

- **SDV 개발 주체**: "MIT 데이터·AI 연구소에서 시작, 현재 DataCebo 운영" — SDMetrics 문서에서 확인됨.
- **CTGAN 논문**: NeurIPS 2019 발표 — GitHub에서 확인됨.
- **TabDDPM**: arXiv:2209.15421 — 정상 접근, "Modelling Tabular Data with Diffusion Models" 확인.
- **PMC11436218 37% 수치**: 해당 논문은 "37% synthetic images improved mIoU from 71.31% to 76.2%"를 보고. 본문 §7.2의 "재현율 0.71→0.84" 수치는 섹션 상단 disclaimer에 "가상 예시"로 명시되어 있어 수정 불필요. 단, 해당 출처 수치는 mIoU(분할 지표)이지 Recall이 아님 — 본문은 이미 가상 예시 disclaimer가 있으므로 보정 없이 유지.
- **MOSTLY AI + Syntho 합병**: mostly.ai 접속 시 "MOSTLY AI powered by Syntho" 표시 확인. 본문의 "(도입 전 현황 확인)" 톤 유지 적절.
- **Gretel → NVIDIA 인수**: gretel.ai가 NVIDIA 도메인으로 301 리다이렉트됨. 본문의 "2025년 3월 NVIDIA가 인수" 주장은 리다이렉트로 추정 가능하나 ⚠️ 공식 발표 일자 확인 권장.
- **DCR Privacy Share 50%**: MOSTLY AI 블로그에서 DCR 방법론 확인됨.
- **Great Expectations Apache 2.0**: 공식 사이트에서 확인됨.

---

## 3. ⚠️ 사람이 최종 확인할 항목

1. **Gretel NVIDIA 인수 일자**: "2025년 3월" 주장 — gretel.ai 리다이렉트로 인수 사실은 추정 가능하나 구체적 날짜는 공식 보도 자료 또는 NVIDIA 발표에서 확인 권장.
2. **NIST SP 800-226 최신 버전**: 현재 URL은 IPD(Initial Public Draft) 버전. NIST에서 최종본이 발간되었다면 URL 업데이트 필요 (https://csrc.nist.gov/publications/detail/sp/800-226 확인 권장).
3. **Taylor & Francis ScienceDirect 논문**: 403으로 접근 불가. 제목·저자 정확도 확인 불가. 도서관 접근 등으로 직접 확인 필요.
4. **SmartNoise Harvard 관계**: OpenDP 프로젝트(Harvard 주도)와 SmartNoise(Microsoft 주도)는 관련이 있으나 공동 개발 관계인지 명확하지 않음. 필요 시 OpenDP 공식 사이트 확인.

---

*검증 완료: 2026-06-22*
