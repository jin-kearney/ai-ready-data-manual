# Cloudera Data Platform (CDP)

> 작성일: 2026-06-10 | 조사 기준: 2025~2026년 최신 릴리스

---

## 기본 정보

| 항목 | 내용 |
|------|------|
| 개발사 | Cloudera, Inc. (미국, 산타클라라) — KKR·CD&R 사모펀드 소유 |
| 라이선스 | 상용 (기반 오픈소스: Apache Hadoop, Spark, Iceberg, Hive 등) |
| 배포 형태 | 퍼블릭 클라우드(AWS/Azure/GCP) + 온프레미스(Private Cloud Base) + 하이브리드 |
| 최신 주요 릴리스 | 2025-09: Iceberg REST Catalog GA, Lakehouse Optimizer 출시; 2026: 쿼리 성능 38% 향상 |
| SDX | Shared Data Experience — CDP 전체를 관통하는 통합 보안·거버넌스 레이어 |

---

## 한 줄 포지셔닝

**하이브리드·온프레미스 환경에서 엔터프라이즈급 보안·거버넌스를 갖춘 오픈 데이터 레이크하우스 — Hadoop 레거시 조직의 현대화 경로.**

---

## 주요 기능

### 1. Cloudera Data Platform 아키텍처
- **CDP Public Cloud**: AWS·Azure·GCP에서 동일한 데이터 레이어·거버넌스 정책 제공
- **CDP Private Cloud Base**: 온프레미스 하둡 클러스터 현대화 (HDFS → Ozone + Iceberg)
- **CDP Hybrid**: 온프레미스와 클라우드에서 동일 SDX 정책 일관 적용 — 데이터 주권 규제 환경에 유리

### 2. SDX (Shared Data Experience) — 통합 보안·거버넌스
- **Apache Ranger**: 중앙화된 RBAC/ABAC 접근 제어, 세분화된 열·행 수준 보안
- **Apache Atlas**: 데이터 카탈로그, 메타데이터 관리, 데이터 리니지
- **Apache Knox**: API 게이트웨이 및 통합 인증 레이어
- **정책 일관성**: 어느 워크로드(Spark, Hive, HBase, Impala)에서도 동일한 보안·거버넌스 정책 적용

### 3. 데이터 카탈로그 (Apache Atlas 기반)
- **자동 메타데이터 수집**: Hive, Spark, HDFS, Kafka 등 클러스터 내 자산 자동 카탈로그화
- **분류(Classification)**: 민감 데이터 분류 태그 자동 전파 (리니지 따라 하위 자산으로 전파)
- **비즈니스 용어 사전**: Glossary 기능 (Apache Atlas 기본, 제한적 수준)
- **검색·탐색**: 전문 검색(Full-text), 필터, 관계 그래프 탐색

### 4. 데이터 리니지
- **Apache Atlas 리니지**: Hive, Spark 쿼리 자동 리니지 캡처
- **테이블 레벨 리니지 주력**: 컬럼 레벨 리니지는 제한적 (Databricks·Snowflake 대비 약점)
- **AI 리니지**: ML 워크로드(CDSW/CML)에서 모델 학습 데이터 추적

### 5. Cloudera Iceberg REST Catalog (2025 GA)
- **개방형 Iceberg 카탈로그**: 모든 Iceberg 호환 엔진(Spark, Flink, Trino, Databricks)이 연결 가능
- **상호운용성**: Delta Sharing, Polaris 등 외부 카탈로그와 페더레이션 지원
- **무결성 보장**: 다중 엔진 동시 읽기·쓰기 시 ACID 트랜잭션 보장

### 6. Cloudera Lakehouse Optimizer (2025 신기능)
- **Apache Iceberg 테이블 자동 최적화**: 쿼리 성능 38% 향상, 저장소 오버헤드 36% 절감
- **자동 Compaction**: 소형 파일 병합, 데이터 정렬 자동화
- **수동 튜닝 불필요**: 데이터 엔지니어 개입 없이 지속 최적화

### 7. AI·ML 워크로드
- **Cloudera Machine Learning (CML)**: Spark와 통합된 MLOps 플랫폼 (모델 배포·모니터링)
- **RAG 파이프라인 지원**: 구조화·비정형·반정형 데이터 통합으로 RAG 기반 AI 애플리케이션 구축
- **AI Feature Store**: 실시간 ML 피처 서빙 지원
- **에이전트 AI 컨텍스트 레이어 (2026 방향)**: 자율 에이전트가 데이터 레이크하우스를 컨텍스트 소스로 활용하는 아키텍처로 진화 중

### 8. DataOps & 생애주기
- **Cloudera DataFlow (NiFi 기반)**: 실시간 데이터 수집·변환 파이프라인
- **Cloudera Data Engineering (Spark 기반)**: 배치·스트리밍 ETL 파이프라인
- **데이터 보존 정책**: HDFS→Ozone 계층화 저장, 아카이빙 정책 관리

---

## AI-Ready Data 주제 매핑

| 주제코드 | 주제명 | 커버 수준 | 비고 |
|---------|--------|-----------|------|
| A-1 | 데이터 카탈로그 | ○ 완전 | Apache Atlas 기반 |
| A-2 | 메타데이터 관리 | ○ 완전 | SDX 통합, 분류 전파 |
| A-3 | 데이터 리니지 | △ 부분 | 테이블 레벨 강함, 컬럼 레벨 미흡 |
| C-3 | Business Glossary | △ 부분 | Atlas 기본 Glossary, 전용 거버넌스 도구 대비 제한적 |
| E-1 | 데이터 품질 | △ 부분 | 별도 Cloudera DQ 모듈 또는 Spark 기반 커스텀 구현 |
| C-1 | 접근 제어 | ○ 완전 | Apache Ranger RBAC/ABAC |
| C-2 | 데이터 분류 | ○ 완전 | Atlas 분류 태그 자동 전파 |
| F-1 | DataOps | ○ 완전 | DataFlow, Data Engineering |
| F-2 | 데이터 생애주기 | ○ 완전 | HDFS/Ozone 계층화, Iceberg Time Travel |

---

## 강점

1. **하이브리드·온프레미스 최강**: 동일한 SDX 보안 정책을 온프레미스와 클라우드에 일관 적용
2. **데이터 주권·규제 대응**: 데이터를 퍼블릭 클라우드로 내보내지 않아도 되는 환경(금융·방산·공공) 적합
3. **Hadoop 레거시 마이그레이션**: 기존 HDP/CDH 환경에서 CDP로 현대화하는 검증된 경로
4. **대규모 스트리밍**: Apache Kafka + NiFi + Flink 기반 실시간 데이터 처리 성숙도 높음
5. **오픈소스 기반 투명성**: 벤더 종속 위험 최소화

---

## 약점·주의점

1. **운영 복잡도**: 하이브리드 배포는 관리 인력·전문성 요구 — SaaS 대비 운영 부담 큼
2. **컬럼 레벨 리니지**: Databricks·Snowflake 대비 컬럼 레벨 리니지 자동화 미흡
3. **UI/UX**: 비즈니스 사용자 친화적 인터페이스가 경쟁사 대비 약함
4. **AI 기능 성숙도**: CoWork·Genie 같은 자연어 AI 인터페이스 미제공
5. **비용 불투명**: 온프레미스 노드 기반 라이선스로 소규모 시작 비용이 높음

---

## 가격 모델

- **구독 기반**: 노드 수 또는 워크로드 용량 기준 (연간 계약 일반적)
- **CDP Public Cloud**: 클라우드 리소스 소비 기반
- **CDP Private Cloud Base**: 노드/코어 기반 구독 라이선스
- 기본 $100,000~$500,000+/년 수준 (규모·에디션에 따라 크게 차이)
- 참고: https://www.cloudera.com/products/cloudera-data-platform.html

---

## 연동 생태계

- **커넥터**: Apache Kafka, NiFi, Sqoop, HDFS, RDBMS 커넥터 다수
- **BI**: Cloudera Data Visualization, Tableau, Power BI (JDBC/ODBC)
- **AI/ML**: CML (Cloudera ML), CDSW, SparkML, TensorFlow on Spark
- **오픈 표준**: Apache Iceberg, Apache Parquet, Apache ORC, Apache Avro
- **API**: Ranger REST API, Atlas REST API
- **MCP**: 공식 MCP 서버 미제공 (2026 기준); 파트너 통합 통해 간접 지원
- **외부 카탈로그**: Iceberg REST Catalog 표준으로 Databricks·Spark 연동

---

## 출처

- https://www.cloudera.com/about/news-and-blogs/press-releases/2025-09-25-cloudera-accelerates-ai-and-analytics-projects-with-a-unified-platform-for-secure-governed-and-performant-data.html
- https://www.cloudera.com/blog/business/data-lakehouse-in-the-agentic-ai-era.html
- https://www.cloudera.com/blog/business/2026-predictions-the-architecture-governance-and-ai-trends-every-enterprise-must-prepare-for.html
- https://www.hpcwire.com/bigdatawire/this-just-in/cloudera-advances-hybrid-data-platform-with-long-term-stability-elastic-scale-and-open-data-interoperability/
- https://www.cloudera.com/products/open-data-lakehouse.html
