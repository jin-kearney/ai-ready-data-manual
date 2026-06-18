# src-001 — 오픈소스 데이터 거버넌스 프레임워크 비교

- **URL**: https://thedataguy.pro/blog/2025/08/open-source-data-governance-frameworks/
- **제목**: Open-Source Data Governance Frameworks: A Strategic Analysis of OpenMetadata, DataHub, Apache Atlas, and Amundsen
- **접속일**: 2026-06-18
- **상태**: 403 Forbidden — 본문 직접 수집 불가. 검색 결과 스니펫 기반 정리.

---

## 수집된 핵심 사실 (검색 스니펫 기반)

### DataHub
- LinkedIn 개발, AcrylData 관리. 오픈소스화: 2020년
- 2025년 1월 DataHub 1.0 출시(5주년 기념)
- v1.4.0: Context Documents, 재설계된 계보 네비게이터, Google Dataplex·Azure Data Factory·IBM Db2 커넥터 추가
- 아키텍처: 관계형 DB + Elasticsearch + JanusGraph/Neo4j + Kafka — 강력하지만 인프라 복잡도 높음
- 데이터 메시(Data Mesh) 아키텍처에 특히 적합

### OpenMetadata
- 2021년 출시. Apache Atlas·Uber Databook 팀 출신
- "단일 진실 공급원(Single Source of Truth)" 접근
- 2025년 6월 v1.8: 데이터 계약(Data Contract) 도입
- 아키텍처: MySQL/PostgreSQL + Elasticsearch — 단순 스택, 운영 복잡도 낮음

### Apache Atlas
- Hadoop 생태계의 정통 거버넌스 솔루션
- 2025년 초 기준 GitHub 이슈 대응 느림 (수개월 미해결)
- 신규 도입 비추천 (Hadoop 운영 조직 제외)

### Amundsen
- Lyft 개발, Linux Foundation 이전
- 로드맵 불명확, 문서 노후화
- 기존 수년 사용 조직 외 신규 도입 비추천

### 운영 비용
- 오픈소스 공통: 0.5~1 FTE 지속 필요 (배포·통합·운영)
- DataHub 분산 아키텍처: 인프라·모니터링 비용 높음
- OpenMetadata 단일 설계: 운영 복잡도 낮음
