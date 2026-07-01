# Microsoft Presidio — AI 데이터 보안 솔루션

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Microsoft (오픈소스 프로젝트, GitHub microsoft/presidio) |
| 라이선스 | MIT 라이선스 (완전 오픈소스) |
| 배포 형태 | 셀프 호스팅(Docker, Kubernetes, Python 라이브러리), Azure PaaS 통합 |
| 최신 동향 | PII Shield (Azure PII 프록시, 2025) 발표; ONNX/HuggingFace Transformer 백엔드 지원; LLM 입출력 PII 필터링 사용 사례 확산 (2025~2026) |

## 한 줄 포지셔닝

> **LLM·AI 파이프라인에 삽입 가능한 오픈소스 PII 탐지·익명화 엔진**. 텍스트·이미지에서 맥락 인식 NER로 개인정보를 식별하고, 마스킹·가명화·합성 대체를 적용하여 GenAI 서비스와 ML 파이프라인의 프라이버시를 보호한다.

---

## 주요 기능

### PII 탐지 (Presidio Analyzer)
- **다중 NLP 백엔드**: spaCy(기본), ONNX, Stanza, HuggingFace Transformers — 고정밀 NER 모델 교체 가능
- **내장 인식기(Recognizer)**: 50+ 엔티티 타입 기본 지원 — 이름, 이메일, 전화번호, 신용카드, 주민등록번호, 여권번호, IBAN, IP 주소 등
- **커스텀 인식기**: 정규식, 체크섬(Luhn 알고리즘), NER 모델 기반 커스텀 엔티티 추가. 한국 주민번호·사업자번호·계좌번호 등 커스텀 가능
- **맥락 인식(Context-Aware)**: "환자 이름:" 같은 맥락 단서로 PII 탐지 신뢰도 향상
- **이미지 PII 탐지**: Presidio Image Redactor로 이미지·PDF의 텍스트 레이어 PII 탐지·블러 처리

### 익명화·가명화 (Presidio Anonymizer)
- **다양한 연산자**:
  - `replace`: 엔티티를 `<PERSON>` 같은 플레이스홀더로 대체
  - `mask`: 부분 마스킹 (`홍*동`)
  - `hash`: SHA256/MD5 해시 (가명화)
  - `encrypt/decrypt`: AES 암호화·복호화 (재식별 가능 가명화)
  - `custom`: 커스텀 Python 함수로 대체 값 생성
- **역익명화(De-anonymize)**: 암호화 키로 원본 복원 지원 — 가명처리 후 재식별 가능 파이프라인

### LLM/GenAI 특화 (2024~2026)
- **Prompt 전처리**: LLM API 호출 전 사용자 Prompt에서 PII 제거 후 전달
- **응답 후처리**: LLM 응답에서 PII 재탐지 → 사용자에게 노출 전 필터링
- **PII Shield (Azure, 2025)**: 모든 LLM API 호출을 경유하는 Azure PaaS 프록시. 기업 LLM 사용 시 Prompt/응답 자동 스캔
- **RAG 파이프라인**: 벡터 DB 인덱싱 전 문서 PII 제거 → 검색 결과 PII 비노출

### 서비스 배포
- **REST API 서버**: FastAPI 기반 /analyze, /anonymize 엔드포인트 → 마이크로서비스 통합 용이
- **Python 라이브러리**: `pip install presidio-analyzer presidio-anonymizer` 직접 임포트
- **Kubernetes 배포**: Helm Chart 제공. 고가용성 스케일 아웃 가능

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 매핑 방식 |
|---|---|
| F-4 AI 데이터 보안 | 핵심 솔루션 — 학습 데이터·Prompt·Agent 로그 PII 탐지·익명화 |
| 비정형 PII 탐지 | 텍스트·이미지·PDF PII 식별 (비정형 데이터 전문) |
| 가명처리 (PIPA) | hash/encrypt 연산자로 가명화; 재식별 가능 가명 파이프라인 지원 |
| LLM 보안 | Prompt 입력·출력 PII 필터링 |
| ML 학습 데이터 품질 | 학습셋 PII 사전 제거로 모델 오염 방지 |

---

## 강점

- **완전 무료(MIT)**: 라이선스 비용 없음. 기업 규모와 무관하게 도입 장벽 최소
- **LLM 파이프라인 통합 용이**: Python 라이브러리로 LangChain, LlamaIndex, Azure OpenAI 파이프라인에 몇 줄 코드로 삽입
- **커스터마이징**: 한국 개인정보 식별자(주민번호, 계좌번호) 등 국내 규제 대응 커스텀 인식기 직접 개발 가능
- **커뮤니티 활발**: GitHub Star 3,500+. 엔터프라이즈 사례(은행·의료·GenAI 서비스) 지속 증가

---

## 약점·주의점

- **엔터프라이즈 기능 없음**: 중앙 정책 관리 UI, RBAC, 감사 로그, 대시보드 없음 → 조직 수준 거버넌스는 별도 구현 필요
- **정형 DB 보호 미지원**: 데이터베이스 컬럼 마스킹·토큰화는 기능 범위 밖. BigID, Protegrity 등 보완 필요
- **탐지 정확도 한계**: 한국어 NER 모델 품질이 영어 대비 낮을 수 있음. 한국어 특화 모델 별도 파인튜닝 권장
- **운영 부담**: OSS이므로 버전 관리·보안 패치·성능 튜닝 모두 자체 책임

---

## 가격 모델

| 모델 | 내용 |
|---|---|
| Presidio OSS | 완전 무료 (MIT 라이선스) |
| Azure PII Shield | Azure 서비스 비용만 발생 (API 호출 기반) |
| 상용 지원 | Microsoft는 별도 상용 지원 패키지 미제공; 커뮤니티 지원 또는 SI 파트너 활용 |

---

## 연동 생태계

- **LLM/GenAI**: Azure OpenAI, OpenAI API, LangChain, LlamaIndex, Semantic Kernel
- **데이터 플랫폼**: Apache Spark (PySpark + Presidio), Databricks, pandas DataFrame
- **ML Ops**: MLflow 학습 데이터 전처리, Kubeflow 파이프라인
- **언어/런타임**: Python(핵심), .NET 클라이언트 지원
- **컨테이너**: Docker, Kubernetes(Helm), Azure Container Apps

---

## 출처

- [Microsoft Presidio GitHub](https://github.com/microsoft/presidio)
- [Presidio로 LLM PII 보호 (Ploomber 블로그)](https://ploomber.io/blog/presidio/)
- [PII Shield: Azure LLM 프록시 (Microsoft Community Hub)](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/introducing-pii-shield-a-privacy-proxy-for-every-llm-call/4514726)
- [Presidio AI 에이전트 PII 보호 (Medium)](https://laxmikumars.medium.com/llms-protecting-sensitive-data-with-microsoft-presidio-33265c887f95)
- [Enterprise-Scale PII De-Identification 논문](https://ijaibdcms.org/index.php/ijaibdcms/article/view/339)
- [LLMOps PII Detection 실전 (OneUptime 블로그)](https://oneuptime.com/blog/post/2026-01-30-llmops-pii-detection/view)
