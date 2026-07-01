# HighByte Intelligence Hub — OT/IoT 수집 솔루션

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | HighByte, Inc. (2019 설립, 미국 포틀랜드) → 2024년 Siemens 생태계 공식 파트너 |
| 라이선스 | 상용 (노드/사이트 라이선스) |
| 배포 형태 | On-premises Edge (임베디드~서버급 하드웨어), Siemens Industrial Edge 포함 |
| 최신 동향 | Siemens + HighByte 공식 파트너십(2024~2025); Intelligence Hub v3.1 출시 — OT 데이터 접근·스케일·거버넌스 확장; Industrial AI 인프라 포지셔닝 강화 |

## 한 줄 포지셔닝

> **OT/IT 데이터 컨텍스트화 전문 Industrial DataOps 플랫폼**. 코드 없이 다양한 OT·IT 소스를 연결하고 데이터 모델을 적용해 AI·분석 시스템이 즉시 소비할 수 있는 품질 높은 산업 데이터를 생산한다.

---

## 주요 기능

### OT/IT 연결 (Connections)
- **OT 프로토콜**: OPC UA, Modbus TCP/RTU, MQTT, EtherNet/IP, PROFINET, BACnet, EtherCAT, DNP3 — 주요 산업 프로토콜 기본 지원
- **IT 시스템**: REST API, SQL DB, SAP (RFC/OData), OSIsoft PI, 파일시스템(CSV, JSON, XML) — OT·IT 데이터를 동일 플랫폼에서 통합
- **Ignition 연동**: HighByte와 Ignition의 상호 보완 아키텍처 지원 — Ignition이 수집, HighByte가 컨텍스트화

### 데이터 모델링·컨텍스트화 (핵심 차별점)
- **코드리스 데이터 모델**: GUI 기반 드래그앤드롭으로 설비 계층(Equipment Model) 정의. 수천 개 태그를 설비·공장·기능 계층으로 매핑
- **유닛·명명 표준화**: 태그명 변환(snake_case→CamelCase, 약어 통일), 단위(UoM) 표준화, 스케일 변환 규칙 일괄 적용
- **메타데이터 병합**: IT 시스템(ERP 설비 마스터, MES 공정 파라미터)의 비즈니스 컨텍스트를 OT 데이터에 자동 결합
- **Unified Namespace(UNS) 제공자**: 컨텍스트화된 데이터를 MQTT 토픽 계층(UNS)으로 발행 — 전사 데이터 메시(Data Mesh) 구현

### 데이터 파이프라인·거버넌스
- **변환 규칙 엔진**: 필터링·집계·계산 로직을 파이프라인 형태로 구성. IF/THEN 규칙, 통계 계산, 품질 코드 처리
- **데이터 거버넌스**: 데이터 모델 버전 관리, 변경 이력 추적, 다중 사이트 모델 일관성 관리
- **v3.1 신기능 (2024~2025)**: OT 데이터 접근 확장(멀티소스), 스케일 개선(수천 동시 태그), 거버넌스 기능 강화

### 멀티 대상 배포
- **MQTT/Kafka 브로커**: 컨텍스트화된 데이터를 MQTT Broker(HiveMQ, EMQX) 또는 Kafka 토픽으로 발행
- **데이터베이스 싱크**: InfluxDB, TimescaleDB, MS SQL, PostgreSQL 직접 쓰기
- **클라우드 연결**: AWS IoT Core, Azure IoT Hub, Google Cloud IoT, Snowflake, Azure ADX

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 매핑 방식 |
|---|---|
| D-1 Physical 데이터 수집 | 다중 OT 프로토콜 연결로 원시 태그 수집 |
| 시계열 표준화 | 단위·명명·스케일 표준화 규칙 엔진 |
| 컨텍스트화 (핵심) | 설비 계층 모델 + IT 메타데이터 병합 → AI 학습 즉시 가능 데이터 |
| 데이터 품질 | 품질 코드 필터링, 이상값 처리 규칙 |
| 데이터 거버넌스 | 모델 버전 관리, 다사이트 표준 적용 |
| Unified Namespace | MQTT UNS 발행으로 전사 데이터 메시 구현 |

---

## 강점

- **컨텍스트화 전문성**: 원시 태그 → AI-Ready 데이터 변환에 특화. AVEVA AF, AWS Asset Model과 동급이지만 에이전틱·코드리스 접근 방식
- **플랫폼 중립성**: 특정 클라우드·이력 관리 시스템에 종속되지 않음. 기존 Ignition, AVEVA, Kafka 환경에 삽입 가능
- **Siemens 에코시스템**: Siemens Industrial Edge 통합으로 지멘스 장비 환경에서 즉시 활용
- **다계열사 표준화**: 동일 데이터 모델을 다수 공장 사이트에 복제·적용하여 그룹 수준 데이터 표준화 효율적

---

## 약점·주의점

- **시계열 저장 없음**: HighByte는 데이터 전달(파이프라인)에 집중. 시계열 Historian은 InfluxDB, AVEVA PI, TimescaleDB 등 별도 필요
- **스트리밍 고성능 한계**: Kafka 수준 초당 수백만 메시지 처리보다 컨텍스트화 정확도에 최적화
- **인지도·레퍼런스**: AVEVA, Ignition 대비 브랜드 인지도와 국내 레퍼런스 부족. 파일럿 PoC 권장
- **단독 완결성 부족**: OT 수집~시계열 저장~분석을 완결하려면 타 솔루션 조합 필수

---

## 가격 모델

| 모델 | 내용 |
|---|---|
| 노드 라이선스 | 배포 노드(Edge 장치) 수 기반; 소규모 사이트부터 엔터프라이즈까지 티어 구성 |
| 엔터프라이즈 계약 | 다사이트·그룹 단위 볼륨 라이선스; 문의 기반 |
| 평가판 | 30일 무료 평가판 제공 |

---

## 연동 생태계

- **OT 플랫폼**: Ignition (Inductive Automation), AVEVA PI System, Siemens TIA Portal/Industrial Edge
- **메시징**: MQTT (HiveMQ, EMQX, Mosquitto), Apache Kafka (Confluent)
- **시계열 DB**: InfluxDB, TimescaleDB, AVEVA PI Server
- **클라우드**: AWS IoT Core/SiteWise, Azure IoT Hub/ADX, Google Cloud IoT, Snowflake
- **분석/AI**: Databricks, Power BI, Grafana, Python ML 파이프라인

---

## 출처

- [HighByte Intelligence Hub 공식 페이지](https://www.highbyte.com/intelligence-hub)
- [Intelligence Hub v3.1 출시](https://www.highbyte.com/blog/intelligence-hub-version-3-1-expanding-ot-data-access-scale-and-governance)
- [Siemens + HighByte 파트너십](https://www.automation.com/article/siemens-highbyte-partner-industrial-data-operations-scale-industrial-ai)
- [Siemens Industrial Edge HighByte](https://www.siemens.com/en-us/products/highbyte-intelligence-hub/)
- [HighByte + Ignition 연동 사례](https://www.highbyte.com/blog/highbyte-and-ignition-two-powerful-solutions-in-your-modern-data-architecture)
- [컨텍스트화 데이터 블로그](https://www.highbyte.com/blog/contextualized-data-where-it-matters)
