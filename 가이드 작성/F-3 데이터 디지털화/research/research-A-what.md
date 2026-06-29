# F-3 데이터 디지털화 — What 클러스터 리서치
> 작성일: 2026-06-29 | 관점: AI가 쓸 데이터를 준비·정비하는 법 (AI 구축법 ✕)

---

## 1. 디지털화(Digitization)의 정의와 경계

### 1-1. 세 개념의 차이

| 용어 | 정의 | 제조 예시 |
|------|------|-----------|
| **Digitization(디지털화)** | 아날로그 정보를 0·1 디지털 포맷으로 변환하는 행위 그 자체. "데이터를 컴퓨터가 읽을 수 있게 만드는 것" | 종이 검사표 스캔 → PDF; 수기 일지 OCR → 텍스트 파일 |
| **Digitalization(디지털라이제이션)** | 이미 디지털화된 데이터를 활용해 업무 프로세스를 자동화·개선하는 것 | 디지털 검사 데이터를 MES와 연동해 불량 자동 집계 |
| **Digital Transformation(디지털 전환)** | 디지털 기술로 사업 전략·조직 전체를 근본적으로 바꾸는 것 | 공장 운영 모델 전체를 데이터 중심으로 재설계 |

**경계 규칙 (F-3의 범위):**
- F-3 = **Digitization**만. 아날로그→디지털로 변환하는 행위.
- 이미 디지털인 문서의 정제·구조화 = **B-1 전처리**가 담당.
- 업무 프로세스 품질 판정 = **C-2**가 담당.

**출처:**
- Yokogawa, "The Differences Between Digitization, Digitalization, and Digital Transformation in Manufacturing" — https://www.yokogawa.com/library/resources/white-papers/the-differences-between-digitization-digitalization-and-digital-transformation-in-manufacturing/
- ATS Global, "Digitalization vs. Digitization" — https://www.ats-global.com/resources/blogs/digitalization-vs-digitization-differences-and-impact-on-it-ot-convergence/
- Agility CMS, "Digitization, Digitalization and Digital Transformation Explained" — https://agilitycms.com/blog/digitization-digitalization-and-digital-transformation-explained

### 1-2. Digitization vs Digitalization — 한 줄 구분

> **Digitization**: "아날로그를 디지털 포맷으로 변환한다"  
> **Digitalization**: "디지털 데이터를 이용해 프로세스를 자동화한다"

제조 현장에서 혼동이 잦은 이유: 두 단어 모두 "디지털화"로 번역되기 때문. F-3 가이드에서는 Digitization만 다루고, 이 구분을 첫 문단에서 명시해야 한다.

---

## 2. 아날로그 자산 인벤토리 (제조 현장 대상 목록)

### 2-1. 유형별 분류표

| 자산 유형 | 구체적 예시 (두산에너빌리티 맥락) | 특징·어려움 |
|-----------|----------------------------------|-------------|
| **종이 문서·출력물** | 검사성적서, 시험 보고서, 납품 기록, 도면 출력본 | 수량 많음, 보존 상태 다양, 중요 정보가 손글씨로 추가된 경우 多 |
| **수기 검사표·일지** | 치수 측정 기록지, 용접 검사 체크리스트, 설비 점검 일지 | ICR 난이도 높음, 약식 기호·약어 다수 |
| **도면 (청사진·마이크로필름)** | 배관도(P&ID), 전기 계통도, 부품 조립도, 설비 레이아웃도 | 대형 용지, 기술 기호·치수 복잡, 층층이 겹친 뷰(View) |
| **현장 메모·포스트잇** | 작업자가 SOP에 추가한 판단 메모, 불량 원인 메모 | 단편적, 맥락 의존적, 구조화 어려움 |
| **사진 (비정형 이미지)** | 설비 이상 부위 사진, 납품 현물 사진, 공정 현황 촬영본 | 메타정보 없음, 분류 기준 없이 저장 |
| **작업자 암묵지(노하우)** | 특정 소음으로 이상 판단, 육안 기준, "느낌으로" 아는 가공 조건 | 언어화·구조화 자체가 어려움 |
| **마이크로필름·마이크로피시** | 1960~80년대 설계 도면, 과거 검사 기록 | 전용 스캐너 필요, 열화 위험 |
| **SOP·FMEA에 누락된 판단 기준** | 베테랑 기술자의 불문율 기준, 경험으로만 전달되는 검수 기준 | 인터뷰·관찰 없이는 포착 불가 |

**출처:**
- AAXIS, "From Filing Cabinets to Factory Intelligence" — https://aaxis.ai/blog/from-filing-cabinets-to-factory-intelligence-digitizing-manufacturing-assets/
- eRecordsUSA, "How to Digitize Engineering Drawings and As-Built Plans" — https://www.erecordsusa.com/how-to-digitize-engineering-drawings-as-built-plans/
- NRX AssetHub, "Digitizing Documents for Asset Management" — https://www.nrx.com/digitizing-documents-asset-management/

### 2-2. 규모 맥락

- 전 세계 기업의 21%가 아직도 종이 양식을 주요 운영 수단으로 사용 (출처: AAXIS 인용)
- 제조·산업 플랜트의 42%가 현재 모바일 점검 앱 사용 중 (출처: GoAudits 인용)
- 초기 인벤토리 단계: 문서 상태 검토 → 미디어 유형 파악 → 매수 확인 → 도면 크기 매핑 → 출력 목적 확인

---

## 3. 전환 방식별 기술

### 3-1. 전환 기술 비교표

| 방식 | 개념 | 적합 대상 | 정확도·한계 |
|------|------|-----------|-------------|
| **스캔(이미지화)** | 물리 문서를 고해상도 이미지(TIFF·PDF)로 변환. 최초 단계. | 도면, 검사성적서, 보고서 등 모든 종이 자산 | 이미지 자체는 정확, 그러나 검색·구조화 불가. 해상도 200~400 DPI 권장 |
| **OCR (Optical Character Recognition)** | 인쇄·타이핑된 글자를 기계가 읽을 수 있는 텍스트로 변환 | 인쇄된 검사성적서, 표준 양식, 타이핑 보고서 | 인쇄체 95~99% 정확도. 손글씨·기울기·얼룩에 취약 |
| **ICR (Intelligent Character Recognition)** | 수기·필기체 인식. 신경망·머신러닝으로 필체를 학습 | 수기 검사표, 현장 일지, 손으로 쓴 메모 | 평균 85~95%; 흘림체·알아보기 어려운 메모는 60~80%로 하락 |
| **STT (Speech-to-Text, 음성→텍스트)** | 음성을 텍스트 데이터로 변환 | 인터뷰 녹취, 현장 구술 작업 지시, 클린룸처럼 입력 어려운 환경 | 제조 전용 어휘(기술 용어·제품명) 없으면 인식률 저하. 커스텀 모델 필요 |
| **모바일·태블릿 현장 입력** | 처음부터 디지털 입력. 종이를 아예 배제 | 신규 점검 항목, 신규 공정의 기록 | 100% 디지털 출발. 기존 아날로그 자산에는 미적용 (미래 예방책) |
| **현장 인터뷰 구조화** | 질문지·템플릿으로 암묵지를 언어화·데이터화 | SOP에 없는 판단 기준, 베테랑 기술자 노하우 | 언어화 품질은 인터뷰어 역량에 의존. 반구조화 인터뷰 권장 |
| **사진 + 메타정보 입력** | 촬영 시점에 장소·설비ID·담당자·이상 유형 등 태그 추가 | 설비 이상 부위, 현물 검사 사진 | 촬영 후 태그 없으면 분류 불가. 촬영 시점 입력이 핵심 |

### 3-2. 방식별 보완 설명

**스캔 → 품질 요소:**
- 엔지니어링 도면 디지털화 8단계: ① 수집·평가 → ② 문서 준비(펼치기·고정) → ③ 고해상도 스캔 → ④ 포맷 선택(PDF/A·TIFF·DWG) → ⑤ CAD 변환 → ⑥ 품질 검수 → ⑦ 인덱싱·납품 → ⑧ 원본 보안 폐기
- 출력 포맷: 보관용=PDF/A·TIFF; 편집용=DWG/DXF; GIS 활용=GeoTIFF

**OCR vs ICR — 결정 기준:**
- "인쇄체인가 손글씨인가"로 결정.
- 인쇄+손글씨 혼합(예: 인쇄 양식 위에 수기 기입) → ICR 엔진 필요.
- OCR만 쓰면 손글씨 인식률 20~90%로 들쭉날쭉.

**STT(음성→텍스트):**
- 제조 현장 특화 어휘(부품명·규격·공정 코드)가 없는 범용 STT는 인식률 낮음.
- 클린룸처럼 장갑 착용 환경에서 키보드 입력 대체 수단으로 효과적.
- 현장 인터뷰 녹취→STT→텍스트 정제→구조화 순서로 암묵지 포착 가능.

**암묵지 인터뷰 구조화:**
- 반구조화 인터뷰(semi-structured): "마지막으로 X 상황을 처리했을 때 어떻게 하셨나요? 무엇을 먼저 확인하셨나요?" 식 시나리오 질문.
- MAKMOSE 기법: 동작 순서(motion sequence) 관찰로 암묵지를 추출.
- 브레인스토밍, 파레토 차트, 이시카와 다이어그램 등 품질 도구를 인터뷰와 결합.
- AI 보조 연구 사례: 인텔리전트 어시스턴트가 현장 작업자에게 질문을 던지며 지식을 구조화 (CHI 2023).

**출처:**
- GDPicture, "ICR vs OCR" — https://www.gdpicture.com/blog/icr-vs-ocr/
- Recrew, "ICR vs OCR: Key Differences, Accuracy Benchmarks" — https://www.recrew.ai/blog/the-difference-between-ocr-and-icr
- MobiDev, "OCR System Development for Blueprints and Engineering Drawings" — https://mobidev.biz/blog/ocr-system-development-blueprints-engineering-drawings
- ACM, "Application of Speech to Text Solutions for Manufacturing Environment" (2024) — https://dl.acm.org/doi/10.1145/3704137.3704179
- Augmentir, "Tacit Knowledge in Manufacturing" — https://www.augmentir.com/glossary/tacit-knowledge
- Poka, "Tacit Tribal Knowledge in Factory Efficiency" — https://www.poka.io/en/use-cases/manufacturing-tacit-knowledge-digital-capture
- ASME IMECE, "Tacit Knowledge Elicitation Techniques Applied to Complex Manufacturing Processes" — https://asmedigitalcollection.asme.org/IMECE/proceedings-abstract/IMECE2017/58356/265641
- ResearchGate, "Tacit Knowledge Elicitation Process for Industry 4.0" — https://www.researchgate.net/publication/356883567_Tacit_Knowledge_Elicitation_Process_for_Industry_40
- eRecordsUSA, "How to Digitize Engineering Drawings" — https://www.erecordsusa.com/how-to-digitize-engineering-drawings-as-built-plans/
- GoAudits, "Best Mobile Inspection Apps 2026" — https://goaudits.com/blog/best-mobile-inspection-apps/

---

## 4. 전환 품질 검증

### 4-1. 핵심 개념: 신뢰도(Confidence Score) 기반 라우팅

| 신뢰도 구간 | 처리 방식 |
|-------------|-----------|
| 95% 이상 | 자동 승인 |
| 80~95% | 샘플링 검수 (일부만 사람 확인) |
| 80% 미만 | 전량 사람 검수 큐로 이동 |

- 90% 신뢰도 임계치 설정 시: 전체 문서의 15~20%가 사람 검수로 라우팅 (출처: LlamaIndex)
- 임계치를 높이면 검수량↑·오류율↓; 낮추면 검수량↓·오류율↑ — 트레이드오프

### 4-2. 품질 검증 단계

1. **원본 대비 시각 검수**: 스캔 이미지 ↔ 원본 비교. 잘림·흐림·회전 없는지 확인.
2. **인식률(Character Error Rate, CER) 측정**: 출력 텍스트 중 오인식된 문자 비율. 인쇄체 목표 CER < 1%.
3. **필수 항목 누락 확인**: 검사표의 측정값·일자·서명 등 핵심 필드 채워졌는지.
4. **샘플링 검수**: 전수 검수가 불가할 때, 무작위 샘플 추출 후 100% 검수. 예: 1,000건 중 100건.
5. **사람 검수 피드백 루프**: 검수자가 수정한 내용 → OCR/ICR 모델 재학습에 반영 → 정확도 점진 향상.
6. **필드 수준 신뢰도 모니터링**: 총계·날짜·ID 같은 중요 필드별로 목표 정확도 설정·월별 추적.

**출처:**
- LlamaIndex, "OCR Accuracy Explained: How to Improve It" — https://www.llamaindex.ai/blog/ocr-accuracy
- Docsumo, "Analysis and Benchmarking of OCR Accuracy" — https://www.docsumo.com/blogs/ocr/accuracy
- arXiv, "Confidence-Aware Document OCR Error Detection" — https://arxiv.org/pdf/2409.04117
- Medium, "OCR Accuracy Benchmarks: The 2026 Digital Transformation Revolution" — https://medium.com/@info_59976/ocr-accuracy-benchmarks-the-2026-digital-transformation-revolution-2f7095c2696f

---

## 5. 수기·한글 문서·표·도면 인식의 어려움

### 5-1. 한글(수기) OCR 특이사항

- 한글은 자음·모음이 모여 음절 블록을 형성하는 복잡한 구조 → 글자간 시각적 유사성 높아 인식 난이도 ↑
- 일부 문서에 한자(漢字)가 혼재 → 한글·한자 동시 인식 알고리즘 필요
- 손글씨 한글: 인쇄체 대비 정확도 현저히 낮음. 흘림체·저해상도·저대비 이미지에서 품질 급락.
- 기울기·눈부심·낮은 해상도 → 어떤 언어든 인식률 저하

**출처:**
- HandwritingOCR, "Korean Handwriting OCR: Hangul Recognition" — https://www.handwritingocr.com/blog/korean-handwriting-ocr
- LlamaIndex, "Best Multilingual OCR Software in 2026" — https://www.llamaindex.ai/blog/best-multilingual-ocr-software

### 5-2. 표(Table) 인식의 어려움

- 표 내 셀 병합·비정형 레이아웃 → 행·열 경계 인식 오류.
- 표 안의 손글씨 수치 → OCR로 인식 불가, ICR 필요.
- 부품 규격표처럼 기호·단위(㎜, kN·m, °C)가 섞인 경우 → 도메인 특화 후처리 필요.
- 벤치마크: CC-OCR 등 멀티모달 평가셋에 표 파싱 전용 샘플 300개 포함 — 표준 도전 과제로 분류됨.

**출처:**
- arXiv, "CC-OCR: A Comprehensive and Challenging OCR Benchmark" — https://arxiv.org/html/2412.02210v2

### 5-3. 도면(Blueprint/Engineering Drawing) 인식의 어려움

- 뷰(View) 중첩·손상 → 어느 치수가 어느 부품에 속하는지 판단 어려움.
- 치수 연계선(chained dimension), 누락 주석, 표준 참조로 암묵적 정의된 높이 등 → 범용 OCR 처리 불가.
- 필요 접근: ① 이미지 분할(세그멘테이션) → ② 기술 기호 전용 인식 모델 + 일반 텍스트 인식 이중 구조 → ③ 치수 검증(허용 공차 내인지)
- 권고: 기존 모델에 제조 도면 전용 데이터셋으로 미세 조정(fine-tuning). 범용 오픈소스 솔루션 단독 사용 비권장.
- 출력 포맷은 편집 가능 벡터(DWG/DXF)까지 변환해야 활용 가능 (라스터 이미지만으론 AI 활용 제한).

**출처:**
- MobiDev, "OCR Systems Development for Blueprints and Engineering Drawings" — https://mobidev.biz/blog/ocr-system-development-blueprints-engineering-drawings
- Apryse, "Handwriting OCR: How It Works, Accuracy & Best Tools" — https://apryse.com/blog/handwriting-ocr-guide

---

## 핵심 take 5줄

1. **Digitization은 변환 행위 자체, Digitalization은 그 데이터로 프로세스를 개선하는 것** — F-3은 전자만 다루고, 후자는 B-1·C-2가 담당한다는 경계를 가이드 첫머리에서 명확히 해야 한다.
2. **제조 현장 아날로그 자산은 최소 7개 유형** — 종이 문서, 수기 기록, 도면, 현장 메모, 사진, 암묵지, 마이크로필름. 두산에너빌리티 맥락에서는 검사성적서·도면·작업일지·숙련공 노하우가 핵심 대상.
3. **전환 방식은 자산 유형마다 다르다** — 인쇄문서=OCR, 수기=ICR, 음성/구술=STT, 암묵지=구조화 인터뷰, 도면=스캔+CAD 변환. 한 방식으로 모든 자산을 처리할 수 없다.
4. **신뢰도(Confidence Score) 기반 사람 검수 라우팅이 품질 확보의 핵심** — 80% 미만은 전량 사람 검수, 95% 이상은 자동 승인. 검수자 수정 내용을 피드백 루프로 모델에 반영해야 지속 개선된다.
5. **한글 손글씨·표·도면은 특히 어렵다** — 범용 OCR로는 한계. 도메인 특화 학습 데이터·후처리·검수 비율 상향이 필요하고, 도면은 라스터→벡터 변환까지 해야 AI 활용이 가능하다.

---

## 불확실 / 검증 필요 항목

| 항목 | 불확실 이유 | 권고 |
|------|-------------|------|
| ICR 97% 정확도 수치 | 제품별·언어별 편차 크고 마케팅 자료 혼재 가능 | PoC 또는 벤더 공개 벤치마크로 확인 |
| 한글 수기 OCR 정확도 | 한국어 특화 벤치마크 공개 자료 부족 | 두산에너빌리티 PoC 결과로 직접 측정 권고 |
| 신뢰도 임계치(90% → 15~20% 라우팅) | 문서 유형·복잡도에 따라 큰 편차 가능 | PoC에서 직접 임계치 캘리브레이션 |
| 마이크로필름 보유 현황·수량 | 두산에너빌리티 내부 자료 필요 | 내부 아카이브 담당자 확인 |
| 암묵지 구조화 방법론 효과 수치 | 현장 적용 사례별 편차 크고 정량 데이터 희소 | 파일럿 인터뷰 후 구조화 품질 내부 평가 |
