# src-013 — Microsoft Purview Unified Catalog

- **URL**: https://learn.microsoft.com/en-us/purview/unified-catalog
- **제목**: Learn about Microsoft Purview Unified Catalog | Microsoft Learn
- **접속일**: 2026-06-18

---

## 주요 내용 (WebFetch 수집)

Microsoft Purview Unified Catalog는 데이터 거버넌스를 위한 단일 통합 SaaS 프레임워크를 제공한다. 데이터 소비자·스튜어드·CxO 모두를 위한 도구를 하나의 경험에서 제공한다.

### 핵심 기능 테이블 (출처 문서 직접 인용)

| 거버넌스 원칙 | 카탈로그 솔루션 |
|-------------|--------------|
| 데이터 접근 | Unified Catalog 접근 정책, 중요 데이터 요소, 용어집 |
| 데이터 큐레이션 | 거버넌스 도메인, 데이터 제품, Health Actions |
| 데이터 발견 | 검색·탐색, 셀프서비스 접근 요청 |
| 데이터 건강 | 품질 규칙·점수, Health Controls, OKR |
| 데이터 이해 | 데이터 제품, 용어집, OKR 연동 |

### 거버넌스 도메인(Governance Domains)
비즈니스 개념(예: Marketing, Finance)으로 데이터 자산을 구조화. 미니 카탈로그 역할.

### 데이터 제품(Data Products)
관련 데이터 자산(테이블·파일·Power BI 보고서 등)을 묶어 쉽게 발견·접근 가능하도록 패키징.

### AI 시대 거버넌스
"연합 거버넌스(Federated Governance)" 접근 — 중앙 표준·정책 + 팀별 셀프서비스 관리.

---

## 지원 데이터 소스 (src-014에서 수집)

**Azure**: Blob Storage, ADLS Gen2, Azure SQL DB, Azure Synapse, Azure Databricks, Cosmos DB, ADF, Data Share, Files, Machine Learning, SQL Managed Instance 등 약 20개

**Database**: Amazon RDS, Amazon Redshift, Cassandra, Db2, Google BigQuery, Hive Metastore, MongoDB, MySQL, Oracle, PostgreSQL, SAP BW, SAP HANA, Snowflake, SQL Server, Teradata

**File**: Amazon S3, HDFS

**Services & Apps**: Airflow, Dataverse, Erwin, Fabric, Looker, Power BI, Qlik Sense, Salesforce, SAP ECC, SAP S/4HANA, Tableau

**스캔 레벨**: L1(기본 메타데이터), L2(스키마), L3(분류 규칙 적용)

**지원 파일 형식**: AVRO, CSV, JSON, ORC, PARQUET, XML, PDF, XLSX, PPTX 등 30개 이상
