# src-009 — DataHub: Open-Source Data Catalog

**URL (공식 문서):** https://docs.datahub.com/docs/introduction  
**URL (블로그):** https://datahub.com/blog/what-is-data-catalog/  
**제목:** DataHub — Open-Source Metadata Platform  
**접속일:** 2026-06-18

---

## 개요

DataHub는 LinkedIn에서 구축한 메타데이터 플랫폼 — 데이터 카탈로깅, 발견(discovery), 관찰(observability), 거버넌스 지원. 2020년 오픈소스 공개.

아키텍처: Kafka, Elasticsearch, GraphQL 기반 마이크로서비스. 3개 계층:
1. **소싱(Sourcing)** — 원천 시스템에서 메타데이터 pull/push
2. **서빙(Serving)** — 메타데이터 처리·저장
3. **소비(Consumption)** — 사용자 인터페이스·API

## 메타데이터 수집

- **80+ 프로덕션급 커넥터**: 컬럼 리니지, 사용 통계, 프로파일링, 품질 지표 포함 심층 메타데이터 추출
- **Push/Pull 이중 방식**: 직접 API 호출 또는 Kafka 스트림을 통한 수집
- **자동화 메타데이터 캡처**: 웨어하우스·BI 도구에 연결하여 메타데이터·쿼리 이력 자동 수집
- **컬럼 수준 리니지**: SQL 쿼리 파싱으로 업스트림·다운스트림 의존관계 표시

## API·SDK

- GraphQL API, OpenAPI, Python·Java SDK, CLI 도구
- 3,000+ 조직이 프로덕션에서 운영 (오픈소스 + DataHub Cloud)

## 라이선스

Apache License 2.0 (오픈소스)

## 레거시 시스템 연동

- JDBC 기반 커넥터로 온프레미스 DB 연결 가능
- 커넥터가 없는 레거시 시스템은 API/SDK를 통한 커스텀 수집 파이프라인 구현 가능
- 수동 메타데이터 업로드 지원
