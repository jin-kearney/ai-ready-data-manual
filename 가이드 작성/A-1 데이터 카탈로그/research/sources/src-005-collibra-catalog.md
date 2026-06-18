# src-005 — Collibra: Data Catalog Product & Workflows

**URL (제품 페이지):** https://www.collibra.com/products/data-catalog  
**URL (워크플로우):** https://productresources.collibra.com/docs/collibra/latest/Content/Catalog/CatalogWorkflows/ref_catalog-workflows.htm  
**URL (커넥터 개요):** https://productresources.collibra.com/docs/collibra/latest/Content/Edge/JDBCConnections/ref_catalog-connector-overview.htm  
**제목:** Collibra Data Catalog — Product Capabilities & Workflows  
**접속일:** 2026-06-18

---

## 자동 메타데이터 수집(Automated Metadata Harvesting)

- **100+ 네이티브 커넥터**: 클라우드 데이터 플랫폼(Snowflake, Databricks, Redshift, BigQuery), 온프레미스 DB(Oracle, SQL Server, PostgreSQL, MySQL), 데이터 레이크(S3, ADLS, HDFS), BI 도구(Tableau, Power BI, Looker, Qlik), ETL 도구(Informatica, Talend, SSIS, DataStage), 데이터 사이언스 플랫폼(SageMaker, Azure ML)
- **Collibra Edge**: 방화벽 뒤 제한된 네트워크 환경에서 내부 인프라를 외부에 노출하지 않고 메타데이터를 안전하게 수집
- **자동 스캔**: 수집 과정에서 스키마 발견, 파일 스캐닝, 프로파일링, 민감 필드 분류, 시간 경과에 따른 스키마 변경 감지 자동 실행

## 처리·저장

수집 후 Collibra가 거버넌스 로직 적용:
- 규칙·패턴 기반 자산 자동 분류 (PII, 재무, 운영 등)
- 처리된 메타데이터, 비즈니스 정의, 리니지 그래프, 거버넌스 산출물, 감사 추적을 플랫폼 DB에 저장

## 리니지 하베스터(Lineage Harvester) 컴포넌트

- 리니지 하베스터는 데이터 원천 가까이에서 실행, SQL 스크립트·ETL 스크립트 등 변환 로직 수집
- Collibra REST API로 수집 데이터를 Collibra Data Lineage 서버에 전송
- 서버에서 파싱·분석 후 리니지 그래프 생성

## REST API·SDK 통합

- 메타데이터, 리니지, 용어집, 워크플로우를 프로그래밍 방식으로 접근
- 신규 데이터 원천 자동 등록, 메타데이터 보강, 인증 프로세스 트리거 스크립트/워크플로우 구축 가능

## 카탈로그 워크플로우 (11개 기본 제공)

1. **Assign Owner To Data Set** — 신규 데이터셋 생성 시 오너 배정 자동화
2. **Post Data Ingestion Workflow** — 새로 등록된 스키마에 오너·기술 스튜어드 배정 관리
3. **Propose New Business/Data/Technology Assets** — 데이터 거버넌스 커뮤니티에서 자산 생성 촉진
4. **Request Assets Access** — 데이터 바스켓을 통한 데이터 접근 요청
5. **Simple Approval** — 단일 단계 자산 승인 프로세스
6. **Cancel Process** — 워크플로우 취소 시 사용자 알림
7. **Escalation Process** — 사용자 작업 에스컬레이션 기본 메커니즘
8. **Voting Sub-Process** — 투표 필요 시 다른 워크플로우에서 호출

## 메타데이터 변경·승인 프로세스

- **접근 요청**: "Request Assets Access" 워크플로우로 사용자가 자산(데이터셋, 보고서 등)을 바스켓에 추가하고 접근 요청 제출
- **승인 요건**: "자산에 접근하기 전 모든 데이터 오너가 요청을 승인해야 한다"
- **Post Ingestion 흐름**: 오너가 기술 스튜어드 배정 → 스튜어드가 보안 분류 및 PII 플래그를 올바르게 설정

## 운영 기능
- 인터랙티브 데이터 리니지 시각화
- 컴플라이언스를 위한 민감 데이터 탐지·자동 분류
- 신뢰할 수 있는 데이터 인증·관련 지표 표시
- AI Copilot 기반 직관적 데이터 발견
- 큐레이션된 데이터 제품 게시를 위한 데이터 마켓플레이스
