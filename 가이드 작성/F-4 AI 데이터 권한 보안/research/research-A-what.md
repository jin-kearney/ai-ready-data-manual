# F-4 AI 데이터 권한 보안 — What(구성요소) 리서치 원자료

> 작성일: 2026-06-29  
> 목적: 가이드 What 섹션(구성요소·정본 모델) 작성을 위한 리서치 원자료  
> 관점: AI가 쓸 데이터를 안전하게 준비·정비하는 법 (AI/보안 시스템 구축법 X)

---

## 1. 접근 권한 통제 모델

### 1-1. 세 가지 모델 개념 비교

**RBAC (Role-Based Access Control — 역할 기반 접근 통제)**
- 정의: 사용자를 역할(Role)에 배정하고, 역할에 권한을 부여. "사람 → 역할 → 권한" 3단계 구조.
- 특징: 단순·빠름(1ms 미만 평가). 조직 구조가 안정적이고 역할이 명확한 환경에 적합.
- 제조 예시: 설계팀 역할 = 도면 조회 가능 / 영업팀 역할 = 도면 조회 불가
- 한계: 맥락(시간·상황·목적)을 반영하지 못함. AI 환경에서 의도 없이 과도하게 공유될 위험.

**ABAC (Attribute-Based Access Control — 속성 기반 접근 통제)**
- 정의: 사용자 속성(부서·직급), 데이터 속성(민감도·분류), 환경 속성(접속 시간·위치), 행위 유형(조회vs반출)을 종합해 접근 허용 여부 결정.
- 특징: 유연·세밀. "부서==설계 AND 민감도==기밀 AND 목적==AI학습이면 허용" 형태의 정책 표현 가능.
- 평가 비용: 10~100ms. RBAC보다 느리지만 복잡한 조건 처리 가능.
- IBM 2025 데이터: 조직의 13%가 AI 모델/앱 침해 경험. 97%가 AI 접근 통제 미비.

**PBAC (Purpose-Based Access Control — 목적 기반 접근 통제)**
- 정의: 데이터의 **사용 목적**에 맞을 때만 접근 허용. GDPR "목적 제한 원칙"과 직접 연관.
- ABAC와의 관계: 대부분 ABAC의 고급 구현으로, 목적(purpose) 속성을 정책에 포함한 형태.
- 제조 AI 맥락: "AI 학습용"·"품질 분석용"·"외부 보고용" 등 목적이 데이터 접근 키.

**모델 선택 기준 요약**

| 환경 | 권장 모델 | 이유 |
|------|-----------|------|
| 조직이 안정적, 역할 100개 이하 | RBAC | 단순·빠름 |
| 복잡한 매트릭스 조직, 상황에 따라 권한 달라짐 | ABAC | 동적 조건 처리 |
| 규정 준수·목적 제한 필요 | PBAC(ABAC 상위) | 목적 기반 정책 |
| AI 학습·RAG·Agent 데이터 접근 | ABAC 또는 PBAC | 맥락·의도까지 통제 |

출처: [RBAC vs ABAC vs PBAC 비교 가이드 — Promethium AI](https://promethium.ai/guides/rbac-vs-abac-pbac-access-control-comparison/)  
출처: [RBAC vs ABAC vs FGAC — Velotix](https://www.velotix.ai/data-access-control/rbac-vs-abac-vs-fgac/)  
출처: [ABAC vs RBAC for AI Agent Access Control — Kiteworks](https://www.kiteworks.com/cybersecurity-risk-management/abac-rbac-ai-access-control/)

---

### 1-2. 세분화 접근 통제 (Fine-Grained Access Control, FGAC)

RBAC·ABAC는 "어느 테이블/파일까지"를 정하지만, **행·열·셀 수준**의 세분화가 필요할 때 FGAC를 쓴다.

**행 수준 보안 (Row-Level Security, RLS)**
- 같은 테이블에서 본인 데이터만 보이게 차단. 예: A/S 보고서 테이블에서 각 딜러는 자기 딜러코드 행만 조회 가능.

**열 수준 보안 (Column-Level Security, CLS)**
- 특정 컬럼을 숨김. 예: 클레임 테이블에서 딜러명·계약가격 컬럼은 영업팀만, 고장코드·수리내용 컬럼은 엔지니어팀도 조회 가능.

**셀 수준 보안**
- 개별 셀 단위 통제. 가장 세밀하지만 관리 복잡도 높음.

**동적 마스킹 (Dynamic Data Masking, DDM)**
- 원본 데이터는 그대로 저장되지만, 조회 시점에 권한에 따라 실시간으로 마스킹·치환·별표처리.
- 예: 일반 직원이 고객 전화번호 컬럼 조회 시 `010-****-1234`로 보이고, 개인정보 담당자는 원본 보임.
- 데이터 원본을 바꾸지 않으므로 정적 마스킹과 달리 **원본 복구 불필요**. 권한 기준이 변하면 바로 반영.

출처: [Fine-Grained Access Control — Velotix](https://www.velotix.ai/data-access-control/rbac-vs-abac-vs-fgac/)  
출처: [Dynamic Data Masking — NextLabs](https://www.nextlabs.com/products/data-access-enforcer/what-is-dynamic-data-masking/)  
출처: [Static vs Dynamic Data Masking — ALTR](https://altr.com/blog/static-vs-dynamic-data-masking-which-to-use-where/)

---

## 2. 민감정보(보호 대상) 분류 체계

### 2-1. 일반 민감정보 유형

**개인식별정보 (PII — Personally Identifiable Information)**
- 특정 개인을 식별할 수 있는 정보: 이름, 주민등록번호, 주소, 전화번호, 이메일, 생년월일 등.
- 한국 개인정보보호법 적용 대상.

**민감정보 (Sensitive Personal Information)**
- 개인정보 중 더 엄격하게 보호되는 유형: 건강·의료정보, 종교·신념, 노동조합 가입 여부, 유전정보, 범죄경력 등.

**임직원정보**
- 급여·인사고과·징계이력·연락처. 내부 AI(HR 챗봇 등) 학습 시 특히 주의.

### 2-2. 제조업 특유 보호 대상 (두산밥캣 맥락)

**계약/거래 정보**
- 고객사명(딜러명·최종 고객명), 납품 단가·할인율·계약 조건.
- 클레임 데이터의 딜러코드·고객코드도 재식별 가능성 → 보호 필요.
- 법적 위험: AI가 "A사 납품 단가가 B사보다 15% 낮다"는 패턴을 학습하면 계약 기밀 노출.

**설계·기술 정보 (기술 기밀)**
- 도면(CAD 파일), BOM(Bill of Materials — 부품 구성표), 공정조건(용접 파라미터·코팅 조건·조립 토크값), 소재 배합비율.
- 이 정보를 외부 LLM API에 전달하면 학습 데이터로 흡수될 위험.

**운영/품질 데이터**
- 불량률·불량코드·공정 이상 패턴 → 경쟁사 분석 시 활용 가능.
- A/S 보고서의 고장 빈도·부위 → 제품 약점 노출 위험.

**영업 비밀 (Trade Secret)**
- 특정 고객의 요구사항, 기술 로드맵, 원가 구조.

**데이터 민감도 등급 예시 (4등급)**

| 등급 | 설명 | 예시 (두산밥캣) |
|------|------|----------------|
| 공개(Public) | 누구나 볼 수 있음 | 제품 카탈로그, 공개 사양 |
| 내부(Internal) | 임직원 범위 내 | 일반 매뉴얼, 내부 절차서 |
| 기밀(Confidential) | 담당 부서·역할만 | 고객사명 포함 A/S 보고서, 계약 단가 |
| 극비(Restricted) | 최소 인원, 엄격 통제 | 도면·BOM·공정조건·원가 구조 |

출처: [Sensitive Data Classification — Strac](https://www.strac.io/blog/sensitive-data-classification)  
출처: [Data Classification — Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/data-classification)  
출처: [Legal Considerations for IP in Smart Manufacturing — Foley & Lardner](https://www.foley.com/insights/publications/2026/05/legal-considerations-ip-in-smart-manufacturing-data-ownership-trade-secret-risks-and-patenting-ai-assisted-inventions/)  
출처: [Trade Secrets and AI — Bloomberg Law](https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/trade-secrets-risk-exiting-a-one-way-door-when-data-is-fed-to-ai)

---

## 3. 비식별(De-identification) 기법

### 3-1. 6종 기법 정본 모델 (제안)

비식별 기법은 **가역성(복원 가능 여부)**과 **형식 유지 여부**에 따라 구분한다.

| 기법 | 한 줄 정의 | 가역성 | 형식 유지 | 제조 예시 |
|------|------------|--------|-----------|-----------|
| **삭제(Suppression)** | 해당 값을 완전히 지움 | 불가 | X | 고객명 컬럼 전체 삭제 |
| **마스킹(Masking)** | 일부 문자를 별표·고정값으로 대체 | 불가(정적) / 가능(동적) | 부분 | 딜러코드 `DCR-0412` → `DCR-****` |
| **가명화(Pseudonymization)** | 식별자를 다른 값(코드·난수)으로 교체. 매핑 테이블 별도 보관 | 가능(키 필요) | 유사 | 고객명 `두산인프라코어` → `CUST_A047` |
| **익명화(Anonymization)** | 재식별이 불가능하도록 영구 변환 | 불가 | X | 지역 `경기도 용인시` → `경기도` (일반화) |
| **토큰화(Tokenization)** | 원본 값을 의미 없는 토큰(난수)으로 교체. 금고(vault)에서만 역변환 가능 | 가능(금고 접근 시) | X | 계약번호 → `TKN-8f3a9c21` |
| **형식보존암호화(FPE — Format-Preserving Encryption)** | 암호화하되 원본과 같은 길이·형식 유지. 복호화 키 필요 | 가능(키 필요) | O | 주민번호 `901201-1234567` → `823491-7651203` (같은 형식 유지) |

> FPE는 DB 스키마·애플리케이션 코드를 변경하지 않고 암호화할 수 있어, 레거시 시스템에 특히 유용하다.

출처: [Data Anonymization vs Data Masking — Tonic.ai](https://www.tonic.ai/guides/data-anonymization-vs-data-masking-is-there-a-difference)  
출처: [Pseudonymization vs Tokenization — K2view](https://www.k2view.com/blog/pseudonymization-vs-tokenization/)  
출처: [Format-Preserving Encryption — IRI](https://www.iri.com/solutions/data-masking/static-data-masking/encrypt/format-preserving-encryption)  
출처: [FPE in Data Masking — DataSunrise](https://www.datasunrise.com/professional-info/fpe-for-data-masking/)  
출처: [De-identification vs Pseudonymization — K2view](https://www.k2view.com/blog/de-identification-vs-pseudonymization/)

---

### 3-2. 가명화 vs 익명화 (한국 법 맥락)

**개인정보보호법 정의**
- **가명정보**: 추가 정보(매핑 테이블·키) 없이는 특정 개인을 알아볼 수 없도록 처리한 정보. 추가 정보와 결합하면 재식별 가능 → 여전히 개인정보로 취급되나, 특정 목적(통계·연구·AI 학습 등)으로 동의 없이 활용 가능.
- **익명정보**: 어떤 수단을 써도 특정 개인을 알아볼 수 없는 정보 → 개인정보보호법 적용 제외.

**실무 구분 포인트**
- 가명화는 매핑 테이블을 별도 보관하고, 결합키·재식별 가능성을 관리해야 함.
- 익명화는 일반화·삭제·노이즈 추가 등 여러 기법 조합으로 재식별을 불가능하게 만들어야 함.
- 단순 마스킹이나 이름 교체는 대부분 가명화에 해당 (익명화 아님).

**2024년 가이드라인 추가 내용**
- 이미지·영상·음성·텍스트에 대한 가명처리 기준 포함.
- AI 시대 비정형 데이터 가명처리 절차 명시.

출처: [가명정보 처리 가이드라인 (KISA)](https://www.kisa.or.kr/2060301/form?postSeq=24&lang_type=KO)  
출처: [가명정보 처리 가이드라인 2024 개정 — CELA](https://www.cela.kr/4/?bmode=view&idx=5524120)  
출처: [Data Pseudonymisation vs Anonymisation — GDPR Local](https://gdprlocal.com/data-pseudonymisation-vs-anonymisation/)

---

## 4. 민감정보 탐지 방식

### 4-1. 탐지 방식 4종 비교

| 방식 | 작동 원리 | 강점 | 약점 | 적합 데이터 유형 |
|------|-----------|------|------|-----------------|
| **정규식(Regex)** | 패턴 규칙(전화번호 형식, 이메일 형식 등)으로 매칭 | 빠름·결정론적·감사 가능 | 패턴이 없는 이름·회사명 탐지 불가 | 정형(DB 필드·구조화 텍스트) |
| **사전(Keyword)** | 보호 대상 키워드 목록(딜러명 목록·고객사명 목록)과 비교 | 도메인 특화 가능 | 목록 관리 부담·문맥 미고려 | 정형·비정형 혼합 |
| **NER (개체명 인식)** | 문장에서 사람·회사·지명 등 개체를 자동 식별하는 ML 모델 | 비정형 텍스트에서 이름·조직명 탐지 | 문맥 의존도 높음·도메인 미세조정 필요 | 비정형(보고서·로그·이메일) |
| **LLM 기반 문맥 탐지** | 대형 언어모델이 문맥 전체를 이해해 민감 정보 판단 | 복잡한 맥락 이해 가능 | 속도 느림·외부 전송 위험·비용 높음 | 복잡한 비정형(계약서·설계 문서) |

**권장 조합**: 정규식(빠른 1차 필터) → NER(2차 비정형 탐지) → 필요 시 LLM(고위험 문서 정밀 검증).

### 4-2. 정형 vs 비정형 탐지 차이

**정형 데이터(DB 필드·테이블)**
- 컬럼명·데이터 타입이 명확 → 메타데이터 기반으로 민감 컬럼 자동 분류 가능.
- 예: `customer_name`, `contract_price` 컬럼은 자동으로 기밀로 태그.

**비정형 데이터(문서·A/S 보고서·Prompt 텍스트·로그)**
- 구조 없음 → NER 또는 LLM으로 탐지.
- RAG 파이프라인 인제스천 시점, LLM API 호출 게이트웨이, 프롬프트 로그에서 탐지·차단.
- "두산밥캣 용인 딜러 김철수 씨의 굴착기 325번 계약 조건이..." → NER로 고객명·딜러명·계약 연관 패턴 탐지.

출처: [PII Detection for AI — OpenRedaction](https://openredaction.com/blog/pii-detection-for-ai)  
출처: [Why NER Models Fail at PII Detection in LLM Workflows — Protecto](https://www.protecto.ai/blog/ner-models-pii-detection-llm-workflows/)  
출처: [LLM Masking — QED42](https://www.qed42.com/insights/llm-masking-protecting-sensitive-information-in-ai-applications)  
출처: [CAPID: Context-Aware PII Detection — arXiv](https://arxiv.org/pdf/2602.10074)

---

## 5. AI 학습 가능 등급

### 5-1. 4등급 정본 모델 (제안)

데이터를 AI 모델 학습·추론·RAG에 사용할 수 있는지를 4등급으로 분류.

| 등급 | 명칭 | 정의 | 적용 조건 | 제조 예시 |
|------|------|------|-----------|-----------|
| **L1** | 원본 사용 가능 | 민감정보 없음. 비식별 처리 없이 학습 가능 | 공개 데이터, 민감정보 미포함 내부 데이터 | 제품 공개 사양, 일반 공정 타이밍 데이터 |
| **L2** | 가명화 후 사용 | 직접 식별자 제거·교체 후 학습 가능. 매핑 키 별도 보관 | 개인정보·고객정보 포함 데이터 | 고객명 가명화한 A/S 보고서, 딜러코드 익명화한 클레임 데이터 |
| **L3** | 익명화 후 사용 | 재식별 불가 수준으로 변환 후 사용. 외부 모델에도 투입 가능 | 고위험 개인정보·기밀 포함 데이터 | 지역·기간만 남기고 모두 삭제한 불량 패턴 통계 |
| **L4** | 학습 금지 | 어떤 처리 후에도 AI 학습에 투입 불가 | 법적 제한·극비 기술·계약상 사용 제한 데이터 | 도면 원본, 핵심 공정 파라미터, 특정 고객 계약 조건 |

### 5-2. 외부 LLM API 사용 시 추가 제한

내부 모델 학습보다 외부 모델(ChatGPT, Copilot, Gemini 등) 사용이 더 엄격.

- **L1 데이터만 허용**: 외부 LLM API에는 민감정보·기밀 데이터 입력 금지.
- **Shadow AI 위험**: 직원이 승인 안 된 AI 도구에 도면·BOM·계약 조건을 직접 입력 → 외부 학습 데이터로 흡수 위험.
- 연구에 따르면 공개 AI 사용 시 임직원 프롬프트의 1/12이 기밀 정보 포함.
- **데이터 처리 계약(DPA)** 필수: 외부 LLM 벤더와 데이터 처리 계약 체결, "학습에 사용하지 않는다"는 조항 명시.

출처: [AI Data Classification: What Is Safe for ChatGPT — IntuitionLabs](https://intuitionlabs.ai/articles/ai-data-classification-chatgpt-copilot-gemini-policies)  
출처: [GDPR ML Training Data Anonymization — anonym.legal](https://anonym.legal/blog/gdpr-compliant-ml-training-data-anonymization-2025)  
출처: [LLM Data Privacy — Lasso Security](https://www.lasso.security/blog/llm-data-privacy)  
출처: [Data Security and Privacy for Third-Party LLM APIs — Rohan Paul](https://www.rohan-paul.com/p/data-security-and-privacy-precautions)

---

## 6. 재식별(Re-identification) 위험

### 6-1. 재식별 개념과 메커니즘

**재식별(Re-identification)** — 직접 식별자(이름·주민번호)를 제거했더라도, 간접 속성들의 조합으로 특정 개인이나 고객사를 다시 찾아낼 수 있는 위험.

예시:
- "경기도 용인시 / 40대 / 굴착기 5대 보유 / 2022년 구매" → 딜러사가 소수라면 거의 특정 가능.
- "A/S 보고서에서 특정 부품 교체 빈도 + 지역 조합" → 해당 딜러나 고객 추정 가능.

### 6-2. 세 가지 통계적 보호 모델 (쉬운 한 줄 정의)

| 모델 | 쉬운 정의 | 의미 |
|------|-----------|------|
| **k-익명성(k-anonymity)** | "이 사람과 똑같아 보이는 사람이 데이터셋에 k명 이상 있어야 한다" | k=5이면 구별 확률 최대 1/5. 값이 클수록 안전하지만 정보 손실 증가 |
| **l-다양성(l-diversity)** | "같은 그룹 안에서도 민감 속성 값이 최소 l가지 달라야 한다" | 동질성 공격 차단. 그룹 내 모두 같은 값이면 k-익명성 뚫림 |
| **t-근접성(t-closeness)** | "그룹 내 민감 속성 분포가 전체 데이터와 비슷해야 한다" | 배경지식 공격 차단 |

### 6-3. 활용성(Utility) vs 보호수준 트레이드오프

- 보호 수준을 높일수록(k 값↑, l 값↑) 데이터 왜곡이 커져 AI 학습 정확도 저하.
- 제조 맥락에서 현실적 접근: 학습용 데이터는 **집계·통계 형태**로 제공 (행 단위 원본 대신 부품별 평균 고장 간격 등) → 개별 재식별 위험 낮추면서 패턴 학습 가능.

출처: [K-anonymity, l-diversity, t-closeness — Utrecht University Data Privacy Handbook](https://utrechtuniversity.github.io/dataprivacyhandbook/k-l-t-anonymity.html)  
출처: [K-anonymity Guide — Immuta](https://www.immuta.com/blog/k-anonymity-everything-you-need-to-know-2021-guide/)  
출처: [L-diversity: Privacy beyond k-Anonymity — ResearchGate](https://www.researchgate.net/publication/304007758_L-diversity_Privacy_beyond_k-AnonymityJ)

---

## 7. 항목 사전 재료 — "민감정보 처리 대장/정책"

### 7-1. 항목 후보 (정형 데이터용)

아래는 "AI 학습용 데이터 민감정보 처리 대장"에 들어갈 항목 후보다.

| 항목명 | 쉬운 의미 | 예시값 | 필수/선택 | 작성 주체 |
|--------|-----------|--------|-----------|-----------|
| 데이터셋명 | 어떤 데이터인지 이름 | `클레임_이력_2020-2024` | 필수 | 데이터 관리자 |
| 테이블/파일명 | 시스템 내 위치 | `CLAIM_MASTER`, `as_report_raw.csv` | 필수 | 데이터 관리자 |
| 필드(컬럼)명 | 어떤 항목인지 | `DEALER_NM`, `CONTRACT_PRICE` | 필수 | 데이터 관리자 |
| 민감정보 유형 | 어떤 종류의 민감정보인지 | `고객식별정보`, `계약기밀`, `기술기밀` | 필수 | 개인정보·법무 담당 |
| 민감도 등급 | 4등급 중 어느 수준인지 | `기밀(Confidential)` | 필수 | 데이터 오너 |
| 적용 비식별 기법 | 어떤 기법으로 처리했는지 | `가명화(딜러코드 → 난수ID)` | 필수 | 데이터 엔지니어 |
| 학습 가능 등급 | AI 학습에 사용 가능한지 | `L2 — 가명화 후 내부 학습 가능` | 필수 | 데이터 오너 + 법무 |
| 활용 목적 | 왜 이 데이터가 필요한지 | `A/S 예측 모델 학습` | 필수 | AI 프로젝트 담당 |
| 외부 LLM 사용 가능 여부 | 외부 AI 서비스에 넣을 수 있는지 | `불가 — 계약 기밀 포함` | 필수 | 법무·정보보안 |
| 승인자 | 누가 이 활용을 허가했는지 | `정보보안팀장 홍길동` | 필수 | 승인권자 |
| 처리 일시 | 비식별 처리를 언제 했는지 | `2024-03-15` | 필수 | 데이터 엔지니어 |
| 보관 위치 | 처리된 데이터가 어디 있는지 | `내부 데이터 레이크 /ai-ready/claim/` | 필수 | 데이터 관리자 |
| 매핑 키 보관 위치 | 가명화 역변환 키가 어디 있는지 | `보안 금고(별도 서버), 접근자 2인` | 가명화 시 필수 | 정보보안팀 |
| 재검토 주기 | 민감도 등급·활용 적정성 재확인 일정 | `1년 (매년 1월)` | 선택 | 데이터 거버넌스 담당 |

### 7-2. 비정형 데이터(문서·프롬프트)용 추가 항목

| 항목명 | 쉬운 의미 | 예시값 |
|--------|-----------|--------|
| 문서 유형 | 어떤 종류의 문서인지 | `A/S 작업지시서`, `도면 PDF`, `고객 요청 이메일` |
| 탐지 방식 | 민감정보를 어떻게 찾는지 | `NER(고객명·딜러명) + 정규식(계약번호)` |
| RAG 인제스천 허용 여부 | 지식 베이스에 넣을 수 있는지 | `비식별 후 허용` |
| 프롬프트 전달 허용 여부 | LLM 입력에 포함 가능한지 | `내부 모델만, 외부 불가` |

출처: [개인정보처리방침 작성지침 2025 — 개인정보보호위원회](https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20806)  
출처: [Sensitive Data Classification — Securiti](https://securiti.ai/sensitive-data-classification/)  
출처: [Data Classification Policy — Securiti](https://securiti.ai/data-classification-policy/)

---

## 8. 핵심 요약 — 정본 모델 제안

### 비식별 기법 6종 (가이드 What 섹션용)
1. **삭제(Suppression)** — 완전 제거, 비가역
2. **마스킹(Masking)** — 일부 문자 치환, 정적(비가역)·동적(가역) 두 종류
3. **가명화(Pseudonymization)** — 식별자 코드 교체, 매핑 키로 복원 가능
4. **익명화(Anonymization)** — 재식별 불가 수준으로 영구 변환, 비가역
5. **토큰화(Tokenization)** — 의미 없는 난수 토큰 교체, 금고에서만 역변환
6. **형식보존암호화(FPE)** — 암호화 후 원본 형식 그대로 유지

근거: GDPR, 개인정보보호법 가명처리 가이드라인(2024), NIST SP 800-188 비식별화 기준.

### AI 학습 가능 4등급 (가이드 What 섹션용)
- **L1** 원본 사용 가능 → **L2** 가명화 후 내부 학습 → **L3** 익명화 후 외부 포함 사용 → **L4** 학습 금지

### 접근 통제 3모델 + 1정밀화 (가이드 What 섹션용)
- RBAC(역할 기반) → ABAC(속성 기반) → PBAC(목적 기반) + FGAC(행/열/셀 세분화)

---

## 참고자료 전체 목록

1. [RBAC vs ABAC vs PBAC — Promethium AI](https://promethium.ai/guides/rbac-vs-abac-pbac-access-control-comparison/)
2. [RBAC vs ABAC vs FGAC — Velotix](https://www.velotix.ai/data-access-control/rbac-vs-abac-vs-fgac/)
3. [ABAC vs RBAC for AI Agent Access Control — Kiteworks](https://www.kiteworks.com/cybersecurity-risk-management/abac-rbac-ai-access-control/)
4. [Dynamic Data Masking — NextLabs](https://www.nextlabs.com/products/data-access-enforcer/what-is-dynamic-data-masking/)
5. [Static vs Dynamic Data Masking — ALTR](https://altr.com/blog/static-vs-dynamic-data-masking-which-to-use-where/)
6. [Format-Preserving Encryption — IRI](https://www.iri.com/solutions/data-masking/static-data-masking/encrypt/format-preserving-encryption)
7. [FPE in Data Masking — DataSunrise](https://www.datasunrise.com/professional-info/fpe-for-data-masking/)
8. [Data Anonymization vs Data Masking — Tonic.ai](https://www.tonic.ai/guides/data-anonymization-vs-data-masking-is-there-a-difference)
9. [Pseudonymization vs Tokenization — K2view](https://www.k2view.com/blog/pseudonymization-vs-tokenization/)
10. [De-identification vs Pseudonymization — K2view](https://www.k2view.com/blog/de-identification-vs-pseudonymization/)
11. [Data Pseudonymisation vs Anonymisation — GDPR Local](https://gdprlocal.com/data-pseudonymisation-vs-anonymisation/)
12. [Sensitive Data Classification — Strac](https://www.strac.io/blog/sensitive-data-classification)
13. [Data Classification — Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/data-classification)
14. [Legal IP in Smart Manufacturing — Foley & Lardner](https://www.foley.com/insights/publications/2026/05/legal-considerations-ip-in-smart-manufacturing-data-ownership-trade-secret-risks-and-patenting-ai-assisted-inventions/)
15. [Trade Secrets Risk and AI — Bloomberg Law](https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/trade-secrets-risk-exiting-a-one-way-door-when-data-is-fed-to-ai)
16. [PII Detection for AI — OpenRedaction](https://openredaction.com/blog/pii-detection-for-ai)
17. [Why NER Models Fail at PII Detection — Protecto](https://www.protecto.ai/blog/ner-models-pii-detection-llm-workflows/)
18. [LLM Masking — QED42](https://www.qed42.com/insights/llm-masking-protecting-sensitive-information-in-ai-applications)
19. [CAPID: Context-Aware PII Detection — arXiv](https://arxiv.org/pdf/2602.10074)
20. [AI Data Classification: ChatGPT/Copilot — IntuitionLabs](https://intuitionlabs.ai/articles/ai-data-classification-chatgpt-copilot-gemini-policies)
21. [GDPR ML Training Data Anonymization — anonym.legal](https://anonym.legal/blog/gdpr-compliant-ml-training-data-anonymization-2025)
22. [LLM Data Privacy — Lasso Security](https://www.lasso.security/blog/llm-data-privacy)
23. [Data Security for Third-Party LLM APIs — Rohan Paul](https://www.rohan-paul.com/p/data-security-and-privacy-precautions)
24. [K-anonymity, l-diversity, t-closeness — Utrecht University Data Privacy Handbook](https://utrechtuniversity.github.io/dataprivacyhandbook/k-l-t-anonymity.html)
25. [K-anonymity Guide — Immuta](https://www.immuta.com/blog/k-anonymity-everything-you-need-to-know-2021-guide/)
26. [L-diversity: Privacy beyond k-Anonymity — ResearchGate](https://www.researchgate.net/publication/304007758_L-diversity_Privacy_beyond_k-AnonymityJ)
27. [가명정보 처리 가이드라인 (KISA)](https://www.kisa.or.kr/2060301/form?postSeq=24&lang_type=KO)
28. [가명정보 처리 가이드라인 2024 개정 — CELA](https://www.cela.kr/4/?bmode=view&idx=5524120)
29. [개인정보처리방침 작성지침 2025 — 개인정보보호위원회](https://www.privacy.go.kr/front/bbs/bbsView.do?bbsNo=BBSMSTR_000000000049&bbscttNo=20806)
30. [Data Governance in Manufacturing — Atlan](https://atlan.com/data-governance-in-manufacturing/)
