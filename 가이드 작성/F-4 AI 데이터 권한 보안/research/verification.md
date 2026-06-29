# F-4 AI 데이터 권한 보안 — 출처 URL 검증 결과

검증일: 2026-06-29  
검증 방법: WebFetch로 각 URL 직접 접근 시도  
범례: ✅ 정상 / ⚠️ 리다이렉트·내용 불일치 / ❌ 접근 불가

---

## 검증 결과 요약 테이블

| 번호 | 원 URL | 상태 | 대체 URL | 비고 |
|---|---|---|---|---|
| [1] | https://promethium.ai/guides/rbac-vs-abac-pbac-access-control-comparison/ | ✅ | — | RBAC·ABAC·PBAC 비교 내용 정상 |
| [2] | https://www.velotix.ai/data-access-control/rbac-vs-abac-vs-fgac/ | ✅ | — | RBAC·ABAC·FGAC 비교 내용 정상 |
| [4] | https://www.nextlabs.com/products/data-access-enforcer/what-is-dynamic-data-masking/ | ✅ | — | Dynamic Data Masking 내용 정상 |
| [5] | https://www.tonic.ai/guides/data-anonymization-vs-data-masking-is-there-a-difference | ✅ | — | 익명화 vs 마스킹 비교 내용 정상 |
| [6] | https://www.k2view.com/blog/pseudonymization-vs-tokenization/ | ✅ | — | 가명화 vs 토큰화 내용 정상 |
| [7] | https://www.iri.com/solutions/data-masking/static-data-masking/encrypt/format-preserving-encryption | ✅ | — | Format-Preserving Encryption 내용 정상 |
| [8] | https://www.kisa.or.kr/2060301/form?postSeq=24&lang_type=KO | ❌ | https://www.kisa.or.kr/20603/form (목록 페이지) | HTTP 500 Internal Server Error. KISA URL 구조가 변경된 것으로 추정. 목록 페이지도 500 오류. 하단 대체 URL 참고 |
| [9] | https://www.shinkim.com/kor/media/newsletter/2342 | ✅ | — | 비정형데이터 가명처리 가이드라인 개정(2024) 내용 정상 |
| [10] | https://www.pipc.go.kr/np/cop/bbs/selectBoardList.do?bbsId=BS074&mCode=C020010000 | ⚠️ | https://www.pipc.go.kr/np/cop/bbs/selectBoardList.do?bbsId=BS217&mCode=D010030000 | 원 URL은 보도자료 게시판(HTTP 200, 접근은 되나 생성형 AI 안내서 없음). 실제 안내서는 별도 「안내서」 게시판에 있음 |
| [11] | https://gdprlocal.com/data-pseudonymisation-vs-anonymisation/ | ✅ | — | GDPR 가명화·익명화 내용 정상 |
| [12] | https://openredaction.com/blog/pii-detection-for-ai | ✅ | — | PII Detection for AI 내용 정상 |
| [13] | https://www.protecto.ai/blog/ner-models-pii-detection-llm-workflows/ | ✅ | — | NER PII Detection LLM Workflows 내용 정상 |
| [14] | https://github.com/microsoft/presidio | ✅ | — | GitHub 레포 정상. 단, 레포가 data-privacy-stack/presidio로 이동 중 안내 있음 (현재는 접근 가능) |
| [15] | https://microsoft.github.io/presidio/ | ⚠️ | https://presidio.dataprivacystack.org/ | 원 URL은 301 리다이렉트 발생(→ presidio.dataprivacystack.org). 리다이렉트 목적지에서 "no guarantee that Presidio will find all sensitive information" 문구 정상 확인 |
| [16] | https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/ | ✅ | — | OWASP LLM02:2025 Sensitive Information Disclosure 내용 정상 |
| [17] | https://intuitionlabs.ai/articles/ai-data-classification-chatgpt-copilot-gemini-policies | ✅ | — | AI 데이터 분류·외부 LLM 정책 내용 정상 |
| [18] | https://utrechtuniversity.github.io/dataprivacyhandbook/k-l-t-anonymity.html | ✅ | — | k-익명성·l-다양성·t-근접성 내용 정상 |
| [20] | https://www.analyticsvidhya.com/blog/2024/03/pii-detection-and-masking-in-rag-pipelines/ | ✅ | — | RAG 파이프라인 PII 탐지·마스킹 내용 정상 |
| [21] | https://www.immuta.com/product/data-security-ai/ | ✅ | — | Immuta Data Security for AI 내용 정상 |
| [22] (본문 링크) | https://privacera.com/platform/ | ✅ | — | Privacera Platform 내용 정상 |
| [22] (ref22) | https://www.prnewswire.com/news-releases/privacera-enhances-ai-governance-solution-with-new-access-control-and-data-filtering-functionality-for-vector-dbrag-302116010.html | ✅ | — | Privacera RAG/VectorDB 접근 통제 보도자료 정상 |
| [23] | https://ranger.apache.org/ | ✅ | — | Apache Ranger 공식 사이트 정상 |
| [24] | https://www.databricks.com/product/unity-catalog | ✅ | — | Databricks Unity Catalog 내용 정상 |
| [25] | https://www.snowflake.com/en/data-cloud/horizon/ | ✅ | — | Snowflake Horizon 내용 정상 |
| [26] | https://aws.amazon.com/macie/ | ✅ | — | Amazon Macie 내용 정상 |
| [27] | https://cloud.google.com/sensitive-data-protection | ✅ | — | Google Sensitive Data Protection 페이지 접근됨(내용 길어 일부 truncated, 페이지 자체는 정상) |
| [28] | https://www.protegrity.com/product | ✅ | — | Protegrity 제품 내용 정상 |
| [29] | https://www.tonic.ai/ | ✅ | — | Tonic.ai 홈페이지 정상 |
| [30] | https://www.skyflow.com/ | ✅ | — | Skyflow 홈페이지 정상 |
| [31] | https://www.fasoo.ai/products/fasoo-data-radar | ✅ | — | Fasoo Data Radar 내용 정상 |
| [32] | https://www.easycerti.com/ | ✅ | — | 이지서티 홈페이지 및 IDENTITY SHIELD 제품 정상 |
| [33] | https://m.boannews.com/html/detail.html?idx=143580 | ✅ | — | 보안뉴스 비식별화 솔루션 리포트 기사 정상 |

---

## 수정 필요 항목 상세

### [8] KISA 가명정보 처리 가이드라인 — ❌ HTTP 500

**원 URL:** `https://www.kisa.or.kr/2060301/form?postSeq=24&lang_type=KO`  
**문제:** HTTP 500 Internal Server Error. URL 경로 구조(2060301)가 KISA 사이트 개편으로 변경된 것으로 추정. 다수 경로 패턴 시도에서 전부 500 오류 반환.  
**권장 대체:** KISA 가명정보 처리 가이드라인 페이지를 직접 찾는 것을 권장. KISA 가이드라인 자료실 목록 URL(`https://www.kisa.or.kr/2060205/form`) 도 500 오류. KISA 홈페이지(`https://www.kisa.or.kr`) 접속 후 검색을 통해 최신 가이드라인 게시물 확인 필요. 또는 피드백을 통해 실제 접근 가능한 직접 링크로 교체 권장.

### [10] 개인정보보호위원회 생성형 AI 안내서 — ⚠️ 내용 불일치

**원 URL:** `https://www.pipc.go.kr/np/cop/bbs/selectBoardList.do?bbsId=BS074&mCode=C020010000`  
**문제:** URL 자체는 HTTP 200 접근 가능하나, 이 게시판은 **보도자료(1,263건)** 게시판이며 "생성형 AI 개발·활용을 위한 개인정보 처리 안내서"가 없음.  
**실제 안내서 위치:** 개인정보보호위원회 **안내서 게시판** — `https://www.pipc.go.kr/np/cop/bbs/selectBoardList.do?bbsId=BS217&mCode=D010030000`  
이 게시판에서 "생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.)" 확인됨.

### [15] Presidio 공식 문서 — ⚠️ 리다이렉트

**원 URL:** `https://microsoft.github.io/presidio/`  
**문제:** 301 Moved Permanently로 `https://presidio.dataprivacystack.org/` 으로 리다이렉트.  
**리다이렉트 목적지 상태:** 정상 접근 가능. "no guarantee that Presidio will find all sensitive information" 문구 확인됨.  
**권장 조치:** 대체 URL `https://presidio.dataprivacystack.org/` 로 교체. 단, 현재 리다이렉트가 자동으로 되므로 독자 접근에는 문제없음 — 단순 URL 정리 차원에서 교체 권장.

---

## 추가 참고사항

- **[14] GitHub microsoft/presidio:** 레포 내부에 "Presidio is moving to a new home" 안내가 있음. 현재는 접근 가능하나 장기적으로 `data-privacy-stack/presidio` 로 이전 예정. 당장 수정 필요는 없으나 추후 모니터링 필요.
- **[22] ref22 vs 본문 링크:** 본문 5.1 솔루션 표에서 Privacera 링크는 `privacera.com/platform/`을 쓰고, References의 [22]는 prnewswire 보도자료를 쓴다. 두 URL 모두 정상이나 역할이 다르다(제품 설명 vs 기능 발표 보도자료). 현행 유지가 적절.
- **[3] [19]:** 본문에서 참조([3][19])되지 않아 References 절에도 없음. 번호 공백으로 확인됨.
