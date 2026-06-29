# F-4 AI 데이터 권한 보안 — How(구축·운영) + Tech Stack 리서치 원자료

작성일: 2026-06-29  
관점: AI가 쓸 데이터를 안전하게 준비하는 절차·도구. "보안 시스템 구축"이 아니라 "데이터 준비 전 민감정보를 가리고 접근 권한을 정하는 작업".

---

## 1. How — 구축 절차 (5~6단계 권장 구성)

### 단계 제안: AI용 데이터 비식별·권한 통제 구축 흐름

다음 6단계가 현장에서 검증된 실무 순서다.

| 단계 | 작업 | 주요 산출물 |
|------|------|------------|
| ① 접근 권한 정책 정의 | 누가(역할·부서·시스템) 어떤 데이터에 접근 가능한지 정의. AI 파이프라인·RAG·Agent 포함 | 역할-데이터 매트릭스, 정책 문서 |
| ② 보호 대상 민감정보 정의 | 개인정보(이름·연락처·주민번호)·영업비밀(설계BOM·원가)·거래처 정보 등 범위 확정 | 민감 데이터 목록, 등급 기준표 |
| ③ 탐지·분류 | 정형(DB 컬럼)·비정형(문서·이미지·로그) 전체 스캔. 자동 탐지 + 사람 검수 병행 | 탐지 결과 리포트, 컬럼/필드 민감도 태그 |
| ④ 목적별 처리(마스킹/가명화) | 용도(AI 학습/RAG/평가/로그/외부 모델)에 따라 삭제·부분마스킹·가명화·토큰화·범주화 적용 | 비식별 처리 완료 데이터셋, 처리 규칙서 |
| ⑤ 학습 가능 등급 부여 | 처리 완료 데이터에 "AI 학습 허용/RAG 검색 허용/사용 금지" 등 레이블 부착 | 데이터 등급 레이블, 카탈로그 태그 |
| ⑥ 운영·점검 | 정기 재식별 위험 점검, 접근 로그 감사, 정책 갱신, 신규 데이터 온보딩 시 재처리 | 점검 보고서, 정책 갱신 이력 |

**출처 근거:**
- Privacera: 전체 AI 애플리케이션 라이프사이클 보안(fine-tuning 데이터 → RAG → 사용자 인터랙션 → 모델 출력 → 감사)을 단계별로 커버 [[PR Newswire 2024-04](https://www.prnewswire.com/news-releases/privacera-enhances-ai-governance-solution-with-new-access-control-and-data-filtering-functionality-for-vector-dbrag-302116010.html)]
- Protegrity: 데이터 파이프라인·분석 워크플로우에 자동화된 배포로 통합 [[Protegrity](https://www.protegrity.com/product)]

---

## 2. 민감정보 탐지 실무

### 2-1. 정형 데이터(DB 컬럼) 탐지

- **패턴 매칭(정규식)**: 주민번호·전화번호·이메일·계좌번호 등 구조화된 형식에 효과적.
- **컬럼명 기반 휴리스틱**: `cust_name`, `phone_no`, `birth_dt` 등 컬럼명 사전으로 후보 식별 후 표본 검증.
- **데이터 프로파일링**: 값 분포·도메인·형식으로 의심 컬럼 플래그.

BigID는 AI 기반 분류기(1,000개 이상, 100개+ 언어) + 정형·비정형·클라우드·온프레미스(메인프레임 포함)를 통합 커버해 Forrester Wave 2026 Q2 리더로 선정됨. [[BigID](https://bigid.com/blog/bigid-forrester-wave-leader-sensitive-data-discovery-classification-2026/)]

### 2-2. 비정형 데이터 탐지 (문서·이미지·로그·Prompt·AI 출력)

#### NER(Named Entity Recognition) 방식
- spaCy, Hugging Face 기반 NER 모델로 이름·조직·장소·날짜 등 엔티티 추출.
- 한국어 NER은 별도 모델 필요(KoNLPy, KLUE 등).

#### 정규식 + 사전 조합
- 패턴(주민번호 형식, 신용카드 체계 자릿수) + 업무 용어 사전(두산 제품군명은 민감하지 않음, 딜러코드는 민감 등).

#### LLM 보조 탐지
- 문맥 이해가 필요한 경우(예: "홍 과장님 클레임 건" — 이름이 암시됨) LLM이 보조 탐지.
- 다만 LLM 자체로의 민감 데이터 전송이 또 다른 유출 경로가 될 수 있으므로 온프레미스 모델 사용 원칙.

#### Microsoft Presidio (오픈소스)
- 정형·비정형 텍스트 대상. NER + 정규식 + 체크섬 알고리즘 조합.
- 신용카드·은행계좌·이메일·IP·주민번호 유사 패턴 등 지원.
- **공식 한계 명시**: *"Presidio can help identify sensitive/PII data in un/structured text. However, because it is using automated detection mechanisms, **there is no guarantee that Presidio will find all sensitive information.**"* — 자동 탐지만으로는 충분하지 않으며 추가 보호 체계 필요.
- 출처: [presidio.dataprivacystack.org](https://presidio.dataprivacystack.org/)
- RAG 파이프라인 적용 사례: 인덱싱 전 문서를 Presidio로 처리해 PII를 플레이스홀더(`<PERSON_5>`, `<EMAIL_ADDRESS_1>`)로 교체 후 저장. 복호화 매핑은 별도 안전 보관해 인가 사용자만 원본 조회. [[Analytics Vidhya 2024](https://www.analyticsvidhya.com/blog/2024/03/pii-detection-and-masking-in-rag-pipelines/)]

### 2-3. 탐지의 한계 — 사람 검수 필요성

| 한계 유형 | 설명 | 대응 |
|-----------|------|------|
| 놓침(False Negative) | 문맥 속 이름("홍 과장"), 간접 식별자 조합 | 샘플 사람 검수 의무화 |
| 오탐(False Positive) | 제품코드·부품번호를 개인정보로 오인 | 업무 도메인 예외 사전 구축 |
| 언어 한계 | 한국어 구어체·줄임말 미인식 | 한국어 전용 NER 모델 추가 |
| 이미지/PDF | 스캔본·핸드라이팅 내 개인정보 | OCR + AI 마스킹(파수 AI-R Privacy, 엘세븐시큐리티) |

**결론**: Presidio·NER 탐지 후 고위험 데이터(클레임·딜러 계약서·인사 데이터)는 반드시 사람 검수 병행.

---

## 3. 목적별 마스킹 정책 (용도 차등)

### 핵심 원칙: 같은 원본 데이터라도 AI 활용 목적에 따라 처리 방식이 달라진다.

| AI 활용 목적 | 처리 방식 | 근거 |
|-------------|----------|------|
| **AI 학습 데이터** | 가명화(가역적 토큰화) 또는 익명화. 학습 패턴 보존이 중요하므로 필드 삭제보다 대체 값 사용. 예: 고객명 → `CUST_A001`, 딜러코드 → `DEALER_K042` | 학습 데이터 재식별 방지 + 통계적 패턴 유지 |
| **RAG 검색 인덱스** | 인덱싱 전 삭제 또는 부분마스킹. 벡터 임베딩에 개인정보가 "녹아들어" 검색 결과로 노출되는 위험 차단. 역할 기반 필터(Role 태그)로 검색 결과 접근 제한. | RAG 인덱스 PII 유출은 OWASP GenAI Top 10 위험항목 LLM02:2025 [[OWASP](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)] |
| **AI 평가 데이터** | 실제값 일부 보존(평가 정확도 측정 필요). 평가 목적 외 공유 금지. 별도 격리 환경에서만 접근. | 평가 데이터는 정답 레이블 포함 → 민감도 높음 |
| **로그 저장** | 자동 마스킹 후 저장. Prompt 입력·Agent 실행 결과·Tool 호출 파라미터 전부 대상. 원본 불필요한 경우 완전 삭제. | 로그에서 PII 재구성 가능 |
| **외부 모델 API 사용** | 전송 전 필수 마스킹. ChatGPT·Claude 등 외부 API로 나가는 데이터는 원본 전송 금지. 토큰화 후 전송, 응답 받아 복원. | 2024년 AI 데이터 프라이버시 사고 56.4% 증가. 클라우드 API 통한 데이터 유출이 핵심 위험 [[Protecto.ai](https://www.protecto.ai/blog/ai-data-privacy-concerns-risk-breaches/)] |

### 처리 기법별 특성 비교

| 기법 | 가역성 | 활용성 | 적합 목적 |
|------|--------|--------|----------|
| 삭제(Redaction) | 불가 | 낮음 | 로그, 외부 공개 |
| 부분마스킹(★★★ → ★★★) | 불가 | 중간 | 화면 표시, 검색 결과 |
| 가명화(Pseudonymization) | 가능(키 보유 시) | 높음 | AI 학습, 내부 분석 |
| 토큰화(Tokenization) | 가능(볼트 통해) | 높음 | 외부 모델 전송, 분산 시스템 |
| 범주화(Generalization) | 불가 | 중간 | 통계 분석, 리포팅 |
| 익명화(Anonymization) | 불가 | 중간 | 외부 공개 데이터셋 |

---

## 4. 활용성 보존 (Utility Preservation)

### 핵심 원칙: "식별자는 지우고, 업무 맥락은 살린다"

두산밥캣 클레임 데이터 예시:

**나쁜 비식별 (다 가려서 분석 불가)**
```
원본:  딜러 홍길동(D-1234) | 밥캣 S770 | 유압 실린더 누유 | 서비스센터 연락처: 010-1234-5678
처리후: ████████████████ | ████████ | ████████████ | ████████████████
```
→ 분석 불가. 결함 유형·제품군 정보까지 삭제됨.

**좋은 비식별 (식별자만 가림, 업무 정보 보존)**
```
원본:  딜러 홍길동(D-1234) | 밥캣 S770 | 유압 실린더 누유 | 서비스센터 연락처: 010-1234-5678
처리후: 딜러 [DEALER_K042] | 밥캣 S770 | 유압 실린더 누유 | [PHONE_MASKED]
```
→ 딜러명·연락처는 숨겨지고, 제품군(S770)·결함유형(유압 실린더 누유)은 보존 → AI 학습 가능.

### 보존해야 할 업무 맥락 (제조 현업)
- 제품군·모델명 (S770, T650 등)
- 공정 단계 코드 (용접, 도장, 조립 등)
- 결함 유형 (누유, 균열, 미접합 등)
- 불량 발생 일자 (연월 수준, 정확한 날짜 범위는 허용)
- 조치 내용 코드 (교체, 수리, 재검사 등)

### 제거해야 할 식별 정보
- 딜러명·사원명·고객명
- 전화번호·이메일·주소
- 특정 날짜+장소 조합(개인 식별 가능)
- 내부 직원 ID(시스템 식별자는 가명화)

**출처**: [PrivacyForge.ai 2025](https://www.privacyforge.ai/blog/pseudonymization-vs-anonymization-when-to-use-what-complete-guide-2025), [Privacy Analytics](https://privacy-analytics.com/resources/articles/data-privacy-ai-de-identification-anonymization-roundup)

---

## 5. AI 로그·Prompt 마스킹 운영

### 5-1. 민감정보가 섞이는 경로

AI 시스템에서 민감정보는 다음 네 지점에서 로그에 남는다:
1. **Prompt 입력값**: 사용자가 고객명·딜러코드·계약번호를 직접 타이핑
2. **RAG 검색 쿼리**: 검색어에 개인정보 포함
3. **Tool/Agent 실행 결과**: DB 조회 결과에 원본 개인정보 포함
4. **AI 모델 출력값**: 학습 데이터에 남은 PII가 AI 출력으로 재현

### 5-2. 저장 전 자동 마스킹 원칙

**4개 로그 레이어 전부 마스킹 적용**:
- Prompt 구성 로그
- 검색(Retrieval) 쿼리 로그  
- 모델 응답 로그
- 오류(Error trace) 로그

**자동화 방법**: LLM 게이트웨이(예: LiteLLM, Portkey) + 인라인 PII 필터를 통해 모든 요청/응답 스트림에서 자동 마스킹. [[RiskTemplate 2026](https://risktemplate.com/blog/2026-03-28-ai-data-leakage-prevention-llm-sensitive-data/)]

### 5-3. RAG 인덱스에 민감정보가 들어가는 위험

- 문서 원본을 그대로 벡터 DB에 올리면, 임베딩 벡터 내에 개인정보가 의미 표현으로 흡수됨.
- 검색 쿼리에 따라 개인 식별 가능 텍스트가 컨텍스트로 AI에 전달 → AI 응답에 노출.
- **대응**: 인덱싱 전 비식별 처리 필수. 역할 태그로 검색 결과 접근 제한. [[Analytics Vidhya 2024](https://www.analyticsvidhya.com/blog/2024/03/pii-detection-and-masking-in-rag-pipelines/)]

### 5-4. OWASP GenAI Top 10 — LLM02:2025 민감정보 노출

OWASP GenAI Security Project는 민감정보 노출을 LLM 시스템의 두 번째 핵심 위험으로 분류.  
핵심 위험: 학습 데이터에 남은 PII가 AI 추론 과정에서 재현되거나, RAG 검색으로 노출되는 것.  
출처: [OWASP GenAI LLM02:2025](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)

---

## 6. 재식별 위험 점검 운영

### 6-1. 재식별 위험이란

비식별 처리 후에도 다른 데이터와 결합하면 개인을 특정할 수 있는 경우. 예: 나이+직책+부서 조합 → 특정인 추론 가능.

### 6-2. 위험 평가 기준

| 평가 모델 | 설명 | 한국·EU·일본 공통 |
|-----------|------|-----------------|
| k-익명성(k-anonymity) | 같은 값을 가진 레코드가 k개 이상 존재해야 개인 특정 불가 | ✔ 공통 적용 |
| l-다양성(l-diversity) | 민감 속성이 l개 이상 다양해야 함 | 추가 보강 |
| t-근접성(t-closeness) | 민감 속성 분포가 전체와 t 이하 차이 | 고위험 데이터 |

한국 개인정보보호위원회 'AI 프라이버시 리스크 관리 모델(2025.02)' 기준 적용 권장.

### 6-3. 정기 점검 주기 및 고위험 상향 기준

- **분기 1회**: AI 학습 데이터 재식별 위험 스캔
- **즉시 점검 트리거**: 신규 데이터소스 추가, 데이터 결합, 법·규제 변경
- **고위험 상향 기준**: k값 임계치 미달, 새로운 외부 데이터와 결합 가능성 확인 시 → AI 활용 제한/재처리

### 6-4. 역할·책임 분리

| 역할 | 담당 내용 |
|------|----------|
| 데이터 오너(Data Owner) | 해당 데이터 민감도 결정, 처리 목적 승인 |
| 보안 담당(Security) | 접근 권한 정책 구현·감사, 마스킹 도구 운영 |
| 개인정보보호 담당(DPO) | 법적 근거 검토, 비식별 적정성 평가 승인 |
| AI 개발팀 | AI 파이프라인 내 처리 기준 준수, 비식별 데이터만 사용 |
| 감사/컴플라이언스 | 정기 점검, 로그 검토 |

---

## 7. Before→After 작성 규칙 (비식별/권한 설정 교정쌍)

### 사례 1 — 클레임 데이터 비식별 (두산밥캣 맥락)

| 구분 | 내용 |
|------|------|
| **나쁜 예** | 원본 그대로 AI 학습: `딜러: 홍길동 (D-1234), 전화: 010-1234-5678, 제품: S770, 결함: 유압 실린더 누유` |
| **왜 나쁜가** | 딜러 개인정보(이름·전화) 포함. 학습 후 AI가 실제 딜러 이름을 출력할 위험. |
| **좋은 예** | 가명화 적용: `딜러: [DEALER_K042], 전화: [MASKED], 제품: S770, 결함: 유압 실린더 누유` |
| **왜 좋은가** | 딜러 식별 불가. S770·유압 결함 패턴은 보존 → 예측 모델 학습 가능. |

### 사례 2 — RAG 검색 인덱스 권한 설정

| 구분 | 내용 |
|------|------|
| **나쁜 예** | 계약서·A/S 이력·직원 평가서를 비식별 없이 RAG 인덱스에 적재. 모든 AI 사용자에게 검색 허용. |
| **왜 나쁜가** | 일반 직원이 AI에 "계약 조건 알려줘"라고 물으면 계약 상대방 정보가 그대로 출력. |
| **좋은 예** | 인덱싱 전 고객명·딜러명 마스킹 + 문서 민감도 태그(Internal/Restricted) 부착. 태그 기반 역할 필터 적용(구매팀만 계약서 검색 가능). |
| **왜 좋은가** | 역할에 맞는 정보만 AI가 참조. 민감 문서는 권한자에게만. |

### 사례 3 — AI Prompt 로그 저장 규칙

| 구분 | 내용 |
|------|------|
| **나쁜 예** | Prompt 원문 그대로 로그 저장: `"딜러 홍길동(D-1234)의 S770 클레임 처리 방법 알려줘"` |
| **왜 나쁜가** | 로그 접근 권한자 누구나 딜러 이름·코드 조회 가능. 로그 유출 시 개인정보 노출. |
| **좋은 예** | 저장 전 자동 마스킹: `"딜러 [DEALER_MASKED]의 S770 클레임 처리 방법 알려줘"` |
| **왜 좋은가** | 업무 맥락(S770 클레임)은 보존, 개인 식별 정보는 제거. |

---

## 8. Tech Stack — 솔루션 분류·비교

### 8-1. 접근 권한 통제 솔루션

#### Immuta
- **특징**: 속성 기반 접근 통제(ABAC). 동일 보안 목표에 Ranger 대비 75배 적은 정책으로 운영 가능. 자연어로 정책 생성(2025년 Immuta Copilot). RAG 기반 GenAI 앱을 위한 멀티레이어 거버넌스·감사 발표(2024).
- **AI 특화**: RAG 인덱스·LLM 학습 데이터에 동일 정책 적용. 실시간 쿼리 모니터링·이상 행위 알림.
- **배포**: 클라우드(Snowflake·Databricks·AWS·GCP·Azure 통합). 온프레미스는 제한적.
- **URL**: [immuta.com/product/data-security-ai](https://www.immuta.com/product/data-security-ai/)

#### Privacera (Trust3 AI by Privacera)
- **특징**: Apache Ranger 기반 + 클라우드 SaaS. 50개 이상 데이터소스 지원. 2024년 Vector DB/RAG 접근 통제·데이터 필터링 기능 추가. 역할/그룹 단위 VectorDB 정책 적용.
- **AI 특화**: PAIG(Privacera AI Governance) — 학습 데이터, RAG, 사용자 인터랙션, 모델 출력 전 단계 보안. Confluence·SharePoint·DB·티켓 시스템의 원본 접근 정책을 VectorDB에도 그대로 반영.
- **배포**: 하이브리드·멀티클라우드. 온프레미스+클라우드 일관 정책.
- **URL**: [privacera.com/platform](https://privacera.com/platform/), [PR Newswire 2024](https://www.prnewswire.com/news-releases/privacera-enhances-ai-governance-solution-with-new-access-control-and-data-filtering-functionality-for-vector-dbrag-302116010.html)

#### Apache Ranger
- **특징**: 오픈소스. Hadoop 생태계(HDFS·Hive·Kafka 등) 중심. RBAC 기반. 대규모 정책 수가 필요해 복잡도↑.
- **AI 특화**: 기본 기능에는 AI 파이프라인 특화 기능 없음. Privacera가 Ranger를 클라우드·AI 환경으로 확장.
- **배포**: 온프레미스. 제조 폐쇄망 환경에 적합.
- **URL**: [ranger.apache.org](https://ranger.apache.org/)

#### Databricks Unity Catalog
- **특징**: Databricks 플랫폼 내장. 데이터+AI 자산(모델·피처·노트북) 통합 거버넌스. 열·행 수준 접근 제어. Delta Sharing.
- **AI 특화**: AI 모델, 피처 스토어, 학습 데이터를 하나의 거버넌스 체계에서 관리.
- **배포**: Databricks 클라우드(AWS·Azure·GCP). 온프레미스는 Databricks on prem 필요.
- **URL**: [databricks.com/product/unity-catalog](https://www.databricks.com/product/unity-catalog)

#### Snowflake Horizon
- **특징**: Snowflake 내장 거버넌스. 동적 데이터 마스킹(DDM)·행 수준 보안·태그 기반 분류·데이터 공유 거버넌스.
- **배포**: Snowflake 클라우드 전용.
- **URL**: [snowflake.com/en/data-cloud/horizon](https://www.snowflake.com/en/data-cloud/horizon/)

---

### 8-2. 민감정보 탐지·발견 솔루션

#### BigID
- **특징**: AI 기반 분류기 1,000개+ / 100개+ 언어. 정형·비정형·클라우드·온프레미스·SaaS·메인프레임 통합 커버. Forrester Wave 2026 Q2 리더(3개 벤더 중 하나).
- **AI 특화**: DSPM(Data Security Posture Management). AI 학습 데이터 발견·분류·태깅 자동화. SAP HANA 포함 엔터프라이즈 DB 커버.
- **배포**: 하이브리드(클라우드+온프레미스). 제조 환경 SAP 연동 가능.
- **URL**: [bigid.com/discovery-classification](https://bigid.com/discovery-classification/)

#### Amazon Macie
- **특징**: AWS S3 전용. ML + 패턴 매칭으로 개인정보 자동 발견·분류. 실시간 추적·이상 알림.
- **배포**: AWS 클라우드 전용.
- **URL**: [aws.amazon.com/macie](https://aws.amazon.com/macie/)

#### Google Sensitive Data Protection (구 Cloud DLP)
- **특징**: 텍스트·이미지 내 민감정보 검사·분류·마스킹. Cloud SQL 포함 다양한 스토리지 지원(2024-2025 확장). GCP 환경 통합.
- **배포**: GCP 클라우드. 온프레미스 데이터는 API 호출 방식(데이터 외부 전송 필요 — 폐쇄망 주의).
- **URL**: [cloud.google.com/sensitive-data-protection](https://cloud.google.com/sensitive-data-protection)

---

### 8-3. 비식별 변환 솔루션 (마스킹·가명화·토큰화)

#### Microsoft Presidio (오픈소스)
- **특징**: 텍스트·이미지 대상. NER + 정규식 + 체크섬. Anonymizer 모듈: 마스킹·교체·삭제·가명화·암호화 선택 가능. Python 패키지로 파이프라인 통합 용이.
- **공식 한계**: *"no guarantee that Presidio will find all sensitive information"* — 자동 탐지 100% 신뢰 불가. 사람 검수 필수.
- **배포**: 온프레미스(폐쇄망 제조 환경에서 자체 배포 가능). 오픈소스.
- **URL**: [github.com/microsoft/presidio](https://github.com/microsoft/presidio), [presidio.dataprivacystack.org](https://presidio.dataprivacystack.org/)

#### Protegrity
- **특징**: 필드 수준 보호(토큰화·암호화·마스킹·FPE). 볼트리스(Vaultless) 토큰화. 클라우드·온프레미스·메인프레임 전체 배포. 2025년 9월 Developer Edition 출시(Python 패키지, AI 파이프라인용 Semantic Guardrails — Prompt·출력 PII 검사).
- **AI 특화**: AI 파이프라인에 직접 통합 가능. 학습 데이터·추론 인풋/아웃풋 모두 커버.
- **배포**: 온프레미스+클라우드. 제조 폐쇄망 환경에 적합.
- **URL**: [protegrity.com/product](https://www.protegrity.com/product), [protegrity.com/product/methods-of-protection](https://www.protegrity.com/product/methods-of-protection)

#### Tonic.ai
- **특징**: 구조적 데이터(Tonic Structural) + 비정형 텍스트(Tonic Textual) 비식별·합성. 개발/테스트 환경용 안전 데이터 생성에 강점. 2025년 Fabricate Data Agent 출시(자연어로 합성 데이터 생성).
- **AI 특화**: AI 학습 데이터 합성 + 비식별 통합 플로우. AWS Marketplace 제공.
- **배포**: SaaS(클라우드 중심). 온프레미스 옵션 제한적.
- **URL**: [tonic.ai](https://www.tonic.ai/)

#### Gretel.ai (NVIDIA 인수, 2025년 3월)
- **특징**: 합성 데이터 생성 + 차분 프라이버시(Differential Privacy) 학습 + PII 교체. NVIDIA 인수 후 GPU 기반 대규모 합성 데이터 생성 방향.
- **배포**: 클라우드(SaaS). NVIDIA 인프라.
- **URL**: [gretel.ai](https://gretel.ai/)

#### Skyflow
- **특징**: 데이터 프라이버시 볼트. 폴리모픽 암호화(Polymorphic Encryption) + 토큰화. LLM Privacy & Security 기능(AI에 토큰 전달, 응답 복원). 제로트러스트 아키텍처.
- **배포**: SaaS(멀티테넌트·싱글테넌트). 온프레미스 지원 미확인.
- **URL**: [skyflow.com](https://www.skyflow.com/)

---

### 8-4. 국내 솔루션

#### 파수 (Fasoo)
- **주요 제품**: Fasoo Data Radar(FDR) — 비정형 데이터(파일서버·PC·모바일) 대상 민감정보 탐지·분류·태깅·처리. Fasoo AI-R Privacy — AI 기반 개인정보 검출·마스킹. OCR 마스킹(PDF·이미지 내 개인정보 포함).
- **특징**: 온프레미스·클라우드 모두 지원. 한국어 개인정보 유형(주민번호·전화·계좌 등) 특화. GDPR·HIPAA·PCI·국내 개인정보보호법 대응.
- **URL**: [fasoo.ai/products/fasoo-data-radar](https://www.fasoo.ai/products/fasoo-data-radar)

#### 이지서티 (EasyCerti)
- **주요 제품**: IDENTITY SHIELD v3.0 — 가명정보 비식별화·결합 솔루션. 비정형 데이터 내 개인정보 탐지 지원. 4개 이상 DB 자동 가명처리.
- **특징**: 국내 개인정보보호 원천 특허 34개. 비식별화 신청→위험성 검토→가명처리→적정성 평가→사후관리 전 과정 표준 프로세스 제공. 한국 개인정보보호위원회 AI 프라이버시 리스크 관리 모델(2025.02) 대응.
- **URL**: [easycerti.com](https://www.easycerti.com/)

#### 신시웨이 / 기타 국내 제품
- 신시웨이는 DB 접근 통제·감사 분야(Petra, 등) 전문. 비식별 전용 제품 정보 미확인.
- 기타 국내 비식별 제품: 지란지교데이터 IDFILTER(가명처리), 펜타시스템 DataEye PIDI(정형·비정형 통합, sLLM 기반 텍스트 탐지), 에이씨엔에스 Docu AD(문서 실시간 마스킹), 앤트랩(CCTV 영상 얼굴·번호판 마스킹).
- **출처**: [보안뉴스 2026 비식별화 솔루션 리포트](https://m.boannews.com/html/detail.html?idx=143580)

---

### 8-5. 선정 기준 요약표 (제조 현업 관점)

| 기준 | 중요도 | 설명 |
|------|--------|------|
| 정형+비정형 탐지 커버리지 | ★★★ | DB 컬럼 + 문서/이미지/로그 통합 탐지 |
| 온프레미스/폐쇄망 지원 | ★★★ | 제조 보안망(인터넷 미연결) 환경 필수 |
| 한국어 민감정보 특화 | ★★★ | 주민번호·전화·계좌 등 국내 포맷 지원 |
| AI 파이프라인 통합(RAG·학습) | ★★★ | AI 워크플로우에 직접 연결 |
| 활용성 보존(업무 맥락 유지) | ★★ | 제품명·결함유형 보존하며 개인정보만 제거 |
| 역할 기반 정책 세분도 | ★★ | 역할·목적별 차등 정책 적용 |
| 클라우드 내장 vs 전용 제품 | ★ | 기존 클라우드 환경 있으면 내장 활용 가능 |

---

## 9. 참고 출처 목록

- [Immuta — Data Security for AI](https://www.immuta.com/product/data-security-ai/)
- [Immuta — RAG GenAI Governance 발표](https://www.immuta.com/news/immuta-announces-multi-layered-data-governance-and-audit-for-rag-based-genai-applications/)
- [Privacera — RAG Vector DB 접근 통제 2024-04](https://www.prnewswire.com/news-releases/privacera-enhances-ai-governance-solution-with-new-access-control-and-data-filtering-functionality-for-vector-dbrag-302116010.html)
- [Privacera Platform](https://privacera.com/platform/)
- [Microsoft Presidio 공식 사이트](https://presidio.dataprivacystack.org/)
- [Microsoft Presidio GitHub](https://github.com/microsoft/presidio)
- [BigID — Discovery & Classification](https://bigid.com/discovery-classification/)
- [BigID — Forrester Wave 2026 Q2 리더](https://bigid.com/blog/bigid-forrester-wave-leader-sensitive-data-discovery-classification-2026/)
- [Protegrity — 데이터 보호 방법](https://www.protegrity.com/product/methods-of-protection)
- [Protegrity Developer Edition (AI 파이프라인용)](https://www.protegrity.com/blog/secure-your-ai-pipeline-introducing-protegrity-developer-edition)
- [Tonic.ai](https://www.tonic.ai/)
- [Gretel.ai 블로그](https://gretel.ai/blog/2025-the-year-synthetic-data-goes-mainstream)
- [Skyflow — PII 데이터 프라이버시 볼트](https://www.skyflow.com/product/pii-data-privacy-vault)
- [OWASP GenAI LLM02:2025 민감정보 노출](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)
- [Protecto.ai — AI 데이터 프라이버시 위험 2024](https://www.protecto.ai/blog/ai-data-privacy-concerns-risk-breaches/)
- [RiskTemplate — AI 데이터 유출 방지 실무 가이드 2026](https://risktemplate.com/blog/2026-03-28-ai-data-leakage-prevention-llm-sensitive-data/)
- [Analytics Vidhya — RAG 파이프라인 PII 탐지·마스킹 2024](https://www.analyticsvidhya.com/blog/2024/03/pii-detection-and-masking-in-rag-pipelines/)
- [PrivacyForge.ai — 가명화 vs 익명화 2025](https://www.privacyforge.ai/blog/pseudonymization-vs-anonymization-when-to-use-what-complete-guide-2025)
- [Privacy Analytics — 비식별화·AI 통합 정리](https://privacy-analytics.com/resources/articles/data-privacy-ai-de-identification-anonymization-roundup)
- [파수 Fasoo Data Radar](https://www.fasoo.ai/products/fasoo-data-radar)
- [이지서티 IDENTITY SHIELD](https://www.easycerti.com/)
- [보안뉴스 2026 비식별화 솔루션 리포트](https://m.boannews.com/html/detail.html?idx=143580)
- [KAIST CSRC — 국내 가명처리 솔루션 비교 2023](https://csrc.kaist.ac.kr/blog/2023/06/16/%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4-%EA%B0%80%EB%AA%85-%EC%B2%98%EB%A6%AC%EB%B9%84%EC%8B%9D%EB%B3%84-%EC%86%94%EB%A3%A8%EC%85%98-%EA%B8%B0%EB%8A%A5-%EB%B0%8F-%EC%84%B1%EB%8A%A5-%EB%B6%84%EC%84%9D/)
- [GigaOm — Immuta vs Apache Ranger 비교](https://www.immuta.com/resources/gigaom-report-immuta-vs-apache-ranger/)
