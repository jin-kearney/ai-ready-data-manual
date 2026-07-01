# Google BigQuery + Dataplex (Knowledge Catalog)

> 작성일: 2026-06-10 | 조사 기준: 2025~2026년 최신 릴리스

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Google LLC (Alphabet Inc.) |
| 라이선스 | 상용 |
| 배포 형태 | SaaS — Google Cloud Platform (GCP, 35+ 리전) |
| 최신 주요 릴리스 | 2026-04: Dataplex Universal Catalog → **Knowledge Catalog** 이름 변경 |
| 관련 제품 | BigQuery, Dataplex (Knowledge Catalog), BigLake, Looker, Vertex AI |

---

## 한 줄 포지셔닝

**GCP 네이티브 서버리스 데이터 웨어하우스와 Knowledge Catalog를 결합한 멀티모달 AI 분석 플랫폼 — Gemini와 Vertex AI의 최전선 통합.**

---

## 주요 기능

### 1. BigQuery — 서버리스 분석 엔진
- **서버리스 아키텍처**: 인프라 관리 없음, 수 TB~PB 쿼리를 수 초 내 처리
- **BigLake**: 데이터 레이크(GCS)와 데이터 웨어하우스(BigQuery) 통합 스토리지 레이어
- **Omni**: AWS·Azure 데이터에 대한 BigQuery 연합 쿼리 (멀티클라우드 지원)
- **Biglake Metastore**: Apache Iceberg 테이블 관리, Hive·Spark 호환

### 2. Knowledge Catalog (구 Dataplex Universal Catalog)
- **2026-04 명칭 변경**: Dataplex Universal Catalog → Knowledge Catalog (API·IAM 이름 유지)
- **전사 데이터 발견**: BigQuery·GCS·외부 소스(BigLake 포함) 자산 자동 카탈로그화
- **태그 템플릿**: 비즈니스 메타데이터 구조화 태그 지정
- **Business Glossary**: 비즈니스 용어 정의 + BigQuery 에이전트와 연동 (대화형 분석에 Glossary 컨텍스트 주입)
- **자동 데이터 인사이트**: 쿼리 추천·테이블·컬럼 자동 설명을 Dataplex에 발행(Preview)
- **메타데이터 변경 피드**: Pub/Sub 기반 실시간 메타데이터 변경 알림

### 3. 데이터 리니지
- **BigQuery 리니지 자동 캡처**: BigQuery→BigQuery 쿼리 리니지 자동 수집 (Preview)
- **Looker 메타데이터 리니지**: Looker (Google Cloud core) 카탈로그 자동화·리니지 수집(Preview)
- **OpenLineage 수집**: 외부 Airflow, Spark, dbt 파이프라인 리니지 통합
- **Impact Analysis**: 업스트림 변경이 다운스트림 리포트에 미치는 영향 분석

### 4. 데이터 품질
- **Data Profile Scans**: 열 수준 통계 자동 생성 (null 비율, 분포, 중앙값 등)
- **Lightweight Profiling Mode (Preview)**: 초 단위 저지연 프로파일 — AI 에이전트 응답 기반 데이터에 적합
- **Data Quality Scans**: 커스텀 SQL 기반 품질 규칙 정의 및 스케줄 실행
- **Custom 실행 ID**: 서비스 계정·EUC 기반 최소 권한 원칙 적용

### 5. 접근 제어
- **IAM + VPC Service Controls**: GCP IAM과 연동한 열·행 수준 데이터 접근 제어
- **BigQuery Row-level Security**: 행 수준 필터 정책
- **Column-level Security**: 열 레이블(데이터 분류) 기반 마스킹 정책
- **Dataplex Zones**: 논리적 데이터 영역(Raw/Curated/Product)으로 접근 정책 분리

### 6. AI 기능 (2025~2026)
- **Gemini 통합**: BigQuery Gemini 어시스턴트로 자연어 SQL 생성, 쿼리 최적화, 문서 생성
- **Vertex AI 네이티브 통합**: BigQuery ML → Vertex AI 모델 배포 파이프라인 직결
- **Cortex Framework**: 산업별(제조, 소매, 금융) 사전 구축 분석 템플릿
- **Conversational Analytics Agent**: BigQuery용 대화형 분석 에이전트 + Glossary 연동

### 7. DataOps & 생애주기
- **Dataform**: 버전 관리·테스트·문서화가 내장된 SQL 변환 파이프라인
- **Cloud Composer (Airflow)**: 워크플로우 오케스트레이션
- **Time Travel**: 최대 7일 (BigQuery 기본), CLONE·SNAPSHOT으로 장기 보존

---

## AI-Ready Data 주제 매핑

| 주제코드 | 주제명 | 커버 수준 | 비고 |
|---------|--------|-----------|------|
| A-1 | 데이터 카탈로그 | ○ 완전 | Knowledge Catalog (구 Dataplex Universal Catalog) |
| A-2 | 메타데이터 관리 | ○ 완전 | 자동 카탈로그화, 태그 템플릿 |
| A-3 | 데이터 리니지 | △ 부분 | BigQuery 리니지 Preview, OpenLineage 수집 |
| C-3 | Business Glossary | △ 부분 | 기본 Glossary 있음, 전용 거버넌스 도구 대비 미흡 |
| E-1 | 데이터 품질 | ○ 완전 | Data Profile·Quality Scans |
| C-1 | 접근 제어 | ○ 완전 | IAM + 행·열 보안 |
| C-2 | 데이터 분류 | ○ 완전 | 열 레이블, 자동 민감정보 분류 |
| F-1 | DataOps | ○ 완전 | Dataform, Cloud Composer |
| F-2 | 데이터 생애주기 | △ 부분 | Time Travel 7일, SNAPSHOT으로 보완 |

---

## 강점

1. **서버리스·무관리**: 인프라 관리 부담 제로, 수 PB 쿼리를 즉각 처리
2. **Gemini·Vertex AI 최전선 통합**: 멀티모달(텍스트·이미지·영상·오디오) AI 분석에서 경쟁사 대비 선도
3. **글로벌 데이터 가용성**: 지역 간 데이터 복제·다중 리전 분석 기본 지원
4. **비용 효율**: 쿼리당 과금(온디맨드) 또는 예약 슬롯 선택, 소규모 시작에 유연
5. **Cortex 산업 템플릿**: 제조·소매 등 산업별 사전 구축 분석으로 빠른 PoC 가능

---

## 약점·주의점

1. **GCP 종속성**: 멀티클라우드 지원(Omni)이 있지만 핵심 거버넌스는 GCP 중심
2. **Business Glossary 성숙도**: 전용 데이터 거버넌스 플랫폼(Collibra, Informatica) 대비 Glossary 워크플로우 약함
3. **리니지 완성도**: BigQuery 내 리니지는 강하나 외부 소스 통합 리니지는 Preview 단계
4. **온프레미스 지원 없음**: 완전 클라우드 전용 — 하이브리드 환경은 Anthos 활용 필요하나 복잡
5. **에코시스템 락인**: BigQuery ML, Vertex AI, Looker 조합은 강력하지만 GCP 의존도 심화

---

## 가격 모델

- **BigQuery 쿼리**: 온디맨드($6.25/TB) 또는 예약 슬롯(Editions: Standard/Enterprise/Enterprise+)
- **BigQuery 저장소**: 활성($0.02/GB/월), 장기($0.01/GB/월)
- **Dataplex/Knowledge Catalog**: 메타데이터 저장·스캔 기준 과금 (소규모 무료 포함)
- **Data Quality Scans**: 스캔 처리 바이트 기준 과금
- 참고: https://cloud.google.com/bigquery/pricing

---

## 연동 생태계

- **커넥터**: 300+ (Datastream, BigQuery Data Transfer Service, Fivetran, dbt)
- **BI**: Looker(Google 소유, 가장 깊은 통합), Data Studio, Tableau, Power BI
- **AI/ML**: Vertex AI (AutoML, Custom Training, Model Registry), Gemini API
- **오픈 표준**: Apache Iceberg, Apache Parquet, Apache Arrow, Delta Lake(읽기)
- **API**: BigQuery REST API, Storage Read/Write API, Dataplex API
- **MCP**: 자체 MCP 서버 공식 없음; 파트너(Atlan 등)를 통한 간접 지원
- **OpenLineage**: Cloud Composer(Airflow) 기반 외부 리니지 수집

---

## 출처

- https://docs.cloud.google.com/dataplex/docs/introduction
- https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog
- https://docs.cloud.google.com/bigquery/docs/release-notes
- https://docs.cloud.google.com/dataplex/docs/release-notes
- https://siliconangle.com/2025/05/28/google-cloud-rolls-new-biglake-bigquery-features-ease-analytics-projects/
- https://pawait.africa/google-cloud-update-july-25-data-catalog-migration/
