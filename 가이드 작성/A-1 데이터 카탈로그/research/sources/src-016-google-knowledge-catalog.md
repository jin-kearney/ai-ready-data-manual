# src-016 — Google Knowledge Catalog (구 Dataplex Universal Catalog)

- **URL**: https://docs.cloud.google.com/dataplex/docs/catalog-overview
- **제목**: About metadata management in Knowledge Catalog | Google Cloud Documentation
- **접속일**: 2026-06-18

---

## 주요 내용 (WebFetch 수집)

Knowledge Catalog은 2026년 4월 10일 Dataplex Universal Catalog에서 리브랜딩됨. API·CLI·IAM 이름은 유지.

### 지원 데이터 소스 (자동 메타데이터 수집)

**Analytics**: BigQuery(데이터셋·테이블·뷰·모델), Dataform, Dataproc Metastore, Iceberg REST Catalog

**AI/ML**: Vertex AI(모델·데이터셋·피처 그룹)

**Databases**: Bigtable, Spanner, AlloyDB for PostgreSQL, Cloud SQL

**Streaming**: Pub/Sub 토픽

**Unstructured**: Cloud Storage, PDF 등 비정형 데이터 프로파일 스캔 (Preview)

**BI**: Looker(Preview)

**서드파티**: 관리형 연결 파이프라인(Managed Connectivity Pipeline)으로 통합

### 검색 기능
- 자연어 시맨틱 검색
- 검색 API 무료 제공

### 메타데이터 관리 핵심
- Entry Type: 커스텀 항목의 최소 메타데이터 표준 강제
- Aspect: 메타데이터 보강 (중첩 구조 list·map·array 지원)
- Entry Links: 자산 간 관계 정의
- 메타데이터 변경 피드 → Pub/Sub 스트리밍 → 자동화 워크플로

### AI 기능
- Gemini 기반 카탈로그
- 정형·비정형 데이터에서 의미 자동 추출 → 동적 컨텍스트 그래프
- AI 에이전트 할루시네이션 저감을 위해 MCP 표준으로 인증된 컨텍스트 제공

### 리브랜딩 이력
- Data Catalog 서비스: 2026년 6월 1일부터 단계적 종료 (Knowledge Catalog으로 마이그레이션)
- Dataplex Universal Catalog → Knowledge Catalog: 2026년 4월 10일
