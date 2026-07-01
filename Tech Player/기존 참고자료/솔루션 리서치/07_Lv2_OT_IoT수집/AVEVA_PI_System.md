# AVEVA PI System (PI Data Infrastructure) — OT/IoT 수집 솔루션

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | AVEVA (Schneider Electric 계열, Cambridge UK 본사) |
| 라이선스 | 상용 (구독 모델 전환 중) |
| 배포 형태 | On-premises(PI Server) + 클라우드(AVEVA CONNECT) 하이브리드 |
| 최신 동향 | AVEVA World 2026: CONNECT Flows(Q2 2026, 800+ 커넥터), AI 기능 내장 발표; PI Data Infrastructure = PI Server + CONNECT 통합 브랜드 |

## 한 줄 포지셔닝

> **제조·에너지 산업 OT 데이터 역사(Historian)의 사실상 표준**. 수십 년의 제조업 레퍼런스와 컨텍스트화 기능(Asset Framework)을 기반으로 온프레미스부터 AI 클라우드까지 하이브리드 운영을 지원한다.

---

## 주요 기능

### 데이터 수집 (PI Interface / Adapters)
- **450+ 인터페이스**: OPC DA/UA, Modbus TCP/RTU, DNP3, IEC 61850, EtherNet/IP, PROFIBUS, 각종 DCS/PLC 벤더 전용 드라이버 등 산업 프로토콜 광범위 지원
- **PI Interface (레거시)**: 수십 년간 검증된 단방향 수집 에이전트. 망분리(Air-gapped) OT 환경에서도 안정적으로 동작
- **AVEVA Adapters (신세대)**: 웹 기반 관리 UI로 구성·확장 단순화. CONNECT와 직접 연동 지원 (2026 업데이트)
- **PI to PI / PI Replicator**: 다수 현장 PI Server → 중앙 PI Server 복제·집계. 다계열사 데이터 통합에 활용

### 시계열 저장 (PI Server)
- **PI Data Archive**: 최적화된 압축 알고리즘(Swinging Door Compression)으로 수십억 개 태그의 시계열 데이터를 저비용으로 장기 보관
- **PI Asset Framework (AF)**: 태그를 설비 계층(공장→라인→설비→센서 등)으로 컨텍스트화. 속성(Attribute)에 단위·한계값·설명 부여
- **Event Frames**: 배치(Batch) 프로세스나 이벤트 기간 데이터를 구조화하여 AI 학습 데이터 생성에 직접 활용 가능

### 클라우드 전환 (AVEVA CONNECT)
- **PI Server → CONNECT 연동**: 현장 PI Server 데이터를 CONNECT 클라우드 플랫폼으로 스트리밍. 벌크 데이터 전송·엔터프라이즈 관리 기능 강화(2026)
- **CONNECT Flows (Q2 2026)**: 800+ 커넥터 지원 데이터 파이프라인 구성. 실시간 정제·필터링·변환 기능. DataOps 워크플로 자동화
- **Operations Data Lake**: CONNECT 내 Analytics 기능으로 BI 도구·AI 플랫폼과 직접 연동

### AI 통합 (2025~2026)
- **AVEVA World 2026 발표**: AI 기능 내재화 — 자연어 쿼리, 이상 탐지 자동화, LLM 기반 운영 데이터 분석 어시스턴트
- **외부 AI 플랫폼 연동**: PI Web API, PI OLEDB를 통해 Python/ML 프레임워크, Azure ML, AWS SageMaker 직접 연결

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 매핑 방식 |
|---|---|
| D-1 Physical 데이터 수집 | PI Interface/Adapters로 현장 프로토콜 수집 |
| 시계열 표준화 | PI Data Archive + AF 속성(단위·계층)으로 정규화 |
| 컨텍스트화 | PI AF 설비 계층 + Event Frame으로 AI 학습용 구조화 |
| 데이터 리니지 | CONNECT Flows에서 데이터 파이프라인 추적 |
| 데이터 품질 | 압축 비율·태그 이상 알람, CONNECT 실시간 정제 |

---

## 강점

- **산업 표준 Historian**: 정유·화학·전력·철강·반도체 등 중공업·제조업에서 30년+ 검증된 사실상 표준
- **컨텍스트화 깊이**: AF를 통한 설비 계층·속성·이벤트 구조는 AI 학습 데이터 레이블링에 직접 활용 가능
- **망분리 환경 신뢰성**: 단방향 인터페이스 에이전트, VLAN 분리 환경에서 안정적인 데이터 수집
- **레거시 통합**: 수십 년 전 DCS/PLC도 벤더 전용 인터페이스로 연결 가능

---

## 약점·주의점

- **비용**: 구독 요금이 태그 수 기반으로 수십만 태그 환경에서 상당. TCO 분석 필수
- **클라우드 전환기 혼선**: PI Server(온프레미스)와 CONNECT(클라우드) 간 기능 경계·데이터 동기화 정책이 지속 변화 중
- **모던 스트리밍 한계**: Kafka 수준의 고속 스트리밍·이벤트 아키텍처에는 부적합. 히스토리안 패러다임에 최적화
- **학습 곡선**: AF 모델 설계, PI Vision 구성 등 전문 인력 필요

---

## 가격 모델

| 모델 | 내용 |
|---|---|
| PI Server 라이선스 | 태그 수 기반 영구 라이선스 + 유지보수; 수천~수십만 태그 규모에 따라 수억원대 |
| AVEVA CONNECT 구독 | 온프레미스+클라우드 혼합 구독 모델로 전환 중; 태그·데이터 전송량 기반 |
| PI Developer Edition | 무료(비상업, 태그 제한); 개발·테스트 목적 |

---

## 연동 생태계

- **SCADA/DCS**: Honeywell Experion, Emerson DeltaV, Siemens PCS 7, Yokogawa CENTUM 등 전용 인터페이스
- **엔터프라이즈 분석**: Microsoft Power BI, Tableau, SAP (PI SAP Connector)
- **AI/ML**: Azure ML (PI Connector for Azure), AWS IoT SiteWise (AVEVA + AWS 통합), Python PI Web API
- **데이터 플랫폼**: Snowflake, Databricks (CONNECT 경유)
- **OT 생태계**: OSIsoft (흡수합병), Aspentech

---

## 출처

- [AVEVA PI Data Infrastructure 공식 페이지](https://www.aveva.com/en/products/pi-data-infrastructure/)
- [AVEVA World 2026 AI 발표](https://www.aveva.com/en/about/news/press-releases/2026/aveva-announces-new-capabilities-to-embed-ai-across-industrial-organizations-and-data-infrastructure-at-aveva-world-2026/)
- [AVEVA PI System 로드맵 2025](https://www.aveva.com/en/perspectives/presentations/2025/aveva--pi-system--and-aveva--pi-data-infrastructure-roadmap/)
- [AVEVA CONNECT 클라우드 통합](https://blog.softwaretoolbox.com/datahub-aveva-pi-and-connect-data-services)
- [AVEVA 하이브리드 데이터 인프라 블로그](https://www.aveva.com/en/perspectives/blog/aveva-s-new-hybrid-data-infrastructure-has-the-flexibility-industrial-enterprises-need-to-thrive-in-increasingly-connected-data-driven-environments/)
- [Gartner Peer Insights: AVEVA PI System](https://www.gartner.com/reviews/product/aveva-pi-system)
