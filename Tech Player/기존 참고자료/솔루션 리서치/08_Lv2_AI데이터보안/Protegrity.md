# Protegrity — AI 데이터 보안 솔루션

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Protegrity (스웨덴·미국 이중 본사; 1996 설립) |
| 라이선스 | 상용 |
| 배포 형태 | On-premises / Hybrid / Cloud (AWS, Azure, GCP) |
| 최신 동향 | **AI Team Edition** 출시 (2025.11) — AI 개발자·Agent 워크플로 전용 보안 패키지; **Developer Edition** GA (2025.09) — GitHub 무료 제공, GenAI 프라이버시 혁신 목적; Semantic Guardrails(Prompt 보안 검사) 추가 |

## 한 줄 포지셔닝

> **필드 수준 vaultless 토큰화의 업계 최강 전문 솔루션**. 정형 데이터베이스·데이터 웨어하우스·BI 도구에서 원본 데이터 관계(JOIN·집계)를 유지하면서 최고 성능의 토큰화·암호화·마스킹을 적용하며, AI 파이프라인용 Semantic Guardrails로 GenAI 보안까지 확장한다.

---

## 주요 기능

### 데이터 보호 방법 (Protection Methods)
- **Vaultless 토큰화**: 토큰 저장 vault 없이 수학적 변환으로 토큰 생성·역변환. 초고속(초당 수천만 건), 데이터 관계(외래 키) 보존
- **FPE(Format-Preserving Encryption)**: 원본 포맷 유지 암호화 — 신용카드 번호 16자리 → 16자리 암호문. 시스템 변경 없이 적용
- **마스킹(Static/Dynamic)**: 컬럼 수준 마스킹. 비프로덕션 환경 데이터 마스킹(Test Data Management)
- **K-익명성·차분 프라이버시**: 통계 프라이버시 보호 기법 지원 — ML 학습 데이터 익명화에 활용
- **중앙 정책 엔진(Policy Server)**: 단일 정책 정의 → 모든 데이터 소스에 일관 적용. 보호 정책 버전 관리·감사

### AI 파이프라인 보안 (2025~2026 신기능)

#### Developer Edition (2025.09)
- Python 패키지 형태로 AI 개발 워크플로에 토큰화·마스킹 직접 적용
- `protegrity.tokenize()`, `protegrity.mask()` API로 Pandas DataFrame, Spark DataFrame 처리

#### AI Team Edition (2025.11)
- AI 개발팀 전용 — 모델·파이프라인·에이전트 시스템 보호 통합 패키지
- **Semantic Guardrails**: 런타임 Prompt·응답 검사 — 민감 엔티티 탐지 후 토큰화/마스킹/차단 적용
- Agentic 워크플로 데이터 보호 — AI Agent 호출 사이에 데이터 토큰화 미들웨어 삽입 가능

#### AI Enterprise Edition
- 데이터 웨어하우스·BI 도구(Tableau, Power BI, Looker)에서 end-to-end 고속 vaultless 토큰화
- 분석가가 토큰화된 데이터로 JOIN·집계 실행 → 원본 노출 없이 분석 가능

### 비정형 데이터 보호
- 문서·이메일·로그에서 PII 탐지 후 토큰화 적용 (Presidio 수준보다 정형 특화, 비정형은 보조적)
- 구조화 로그(JSON, CSV)의 특정 필드 선택적 토큰화

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 매핑 방식 |
|---|---|
| F-4 AI 데이터 보안 | 필드 수준 토큰화·마스킹 + Semantic Guardrails |
| AI 학습 데이터 보호 | 학습셋 PII 토큰화로 모델 오염 방지, 재식별 가능 가명화 |
| LLM/Agent 보안 | Semantic Guardrails로 Prompt·응답 민감 정보 실시간 차단 |
| 분석 유용성 보전 | Vaultless 토큰화로 JOIN·집계 관계 유지 |
| 규제 준수 | GDPR, HIPAA, PCI-DSS, PIPA 가명처리 기술적 수단 |

---

## 강점

- **토큰화 성능·안전성 최강**: 검증된 vaultless 토큰화 기술 — vault 해킹 위험 없이 초고속 처리
- **데이터 관계 보전**: 토큰화 후에도 동일 원본 값 → 동일 토큰 보장 → AI 모델이 JOIN·집계 정상 학습 가능
- **중앙 정책 일관성**: 단일 Policy Server로 DB, 웨어하우스, BI, AI 파이프라인 전체에 동일 정책 적용
- **AI 파이프라인 Python 통합**: Developer/AI Team Edition으로 AI 개발팀이 직접 소비 가능한 SDK 제공

---

## 약점·주의점

- **고비용**: 엔터프라이즈 수준 가격. 중소 규모 조직에는 부담
- **비정형 탐지 한계**: 이미지·PDF·자연어 문서의 PII 탐지 기능은 Presidio, BigID 대비 약함
- **초기 구축 복잡도**: Policy Server 설계, 프로텍터(Protector) 배포, 데이터 소스 연결에 전문 인력·시간 필요
- **중앙화 단일 실패점**: Policy Server 장애 시 전체 데이터 접근 영향 → HA 구성 필수

---

## 가격 모델

| 모델 | 내용 |
|---|---|
| Developer Edition | 무료 (GitHub 공개; 비상업·개발 목적) |
| AI Team Edition | 팀 단위 구독; AI 개발 조직 대상 |
| Enterprise Edition | 데이터 볼륨·노드·프로텍터 수 기반 연간 계약 |
| 온프레미스 구축 | 별도 구현 비용; SI 파트너 활용 |

---

## 연동 생태계

- **데이터 소스**: Oracle, SQL Server, MySQL, PostgreSQL, Snowflake, Teradata, Hadoop/HDFS
- **빅데이터**: Apache Spark (Protegrity Spark 프로텍터), Databricks
- **BI/분석**: Tableau, Power BI, MicroStrategy (토큰화 데이터 직접 분석)
- **AI/ML**: Python SDK, Jupyter Notebook, MLflow
- **클라우드**: AWS (RDS, Redshift, S3), Azure (SQL Database, Synapse), GCP (BigQuery)
- **ERP**: SAP HANA 토큰화 연동

---

## 출처

- [Protegrity 공식 보호 방법](https://www.protegrity.com/product/methods-of-protection)
- [AI Team Edition 출시 (2025.11)](https://www.protegrity.com/news/protegrity-ai-team-edition-to-secure-agentic-workflows)
- [Developer Edition 출시 (2025.09)](https://www.protegrity.com/news/correcting-and-replacing-protegrity-releases-free-developer-edition-on-github-for-genai-privacy-innovation)
- [AI 파이프라인 보안 블로그](https://www.protegrity.com/resources/blog/secure-your-ai-pipeline-introducing-protegrity-developer-edition)
- [Gartner Peer Insights: Protegrity 2026](https://www.gartner.com/reviews/market/data-masking/vendor/protegrity/product/protegrity-data-security-platform)
- [AI 사기 탐지와 데이터 보안 2026](https://www.protegrity.com/blog/ai-fraud-detection-in-2026-what-leaders-must-know)
