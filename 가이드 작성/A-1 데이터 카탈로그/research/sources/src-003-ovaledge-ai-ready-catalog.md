# src-003: AI-Ready Data Catalog — OvalEdge Blog

- URL: https://www.ovaledge.com/blog/ai-ready-data-catalog
- 제목: What Does It Actually Take to Build an AI-Ready Data Catalog?
- 접속일: 2026-06-18

## 핵심 메타데이터 필드 분류

### 기술 메타데이터 (Technical Metadata)
- 스키마 구조 및 컬럼 정의
- 데이터 소스 연결 정보(커넥터)
- 필드 레벨 리니지 추적
- 사용 패턴 및 쿼리 이력
- 최신성 신호(freshness signals) 및 최종 갱신 타임스탬프
- 오너십(ownership) 및 스튜어드십 정보

### 거버넌스·컴플라이언스 필드
- 역할 기반 접근 제어(RBAC) 정책
- PII 분류 및 민감도 태그
- 규제 컴플라이언스 마커(GDPR, CCPA, HIPAA)
- 데이터 마스킹 규칙
- 인증 상태(certification status) 및 검증 타임스탬프

## AI 특화 메타데이터 차원

### 능동 메타데이터(Active Metadata) 속성
- 지속적 실시간 수집 및 업데이트 (수동 유지 불필요)
- 실시간 스키마 변경 감지
- 품질 점수: 완전성(completeness), 정확성(accuracy), 일관성(consistency), 최신성(freshness)
- 신뢰 신호(trust signals) 및 신뢰도 지표

### 의미론(Semantic)·비즈니스 컨텍스트
- 비즈니스 용어 매핑 및 글로서리 링크
- 도메인별 정의 및 엔터티 관계
- 지식 그래프(knowledge graph) 연결
- 사업부 간 동의어 해소

### 리니지(Lineage)·설명 가능성
- 엔드-투-엔드 데이터 변환 경로
- 파이프라인 전반 필드 레벨 리니지
- 다운스트림 소비 이벤트
- 감사 추적(audit trail)을 위한 원천-결과 추적

## 분류 프레임워크

- **품질 차원**: 완전성, 최신성, 정확성, 일관성
- **접근 분류**: Public / Restricted / Confidential / PII-bearing
- **신뢰 속성**: 인증 상태, 품질 점수, 거버넌스 컴플라이언스 상태
