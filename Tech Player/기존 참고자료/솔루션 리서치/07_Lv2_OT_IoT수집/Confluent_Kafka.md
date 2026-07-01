# Confluent (Apache Kafka) — OT/IoT 수집 솔루션

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Confluent, Inc. (2026년 3월 IBM 인수 완료) |
| 라이선스 | Apache Kafka: Apache 2.0 OSS / Confluent Platform: 상용 |
| 배포 형태 | Confluent Cloud(SaaS), Confluent Platform(Self-managed), IBM-Confluent 통합 예정 |
| 최신 버전/동향 | IBM 인수(2026.03) 후 IBM watsonx, OpenShift와 통합 로드맵 발표; Confluent Streaming Agents(2025), Confluent Intelligence 출시 |

## 한 줄 포지셔닝

> **OT 엣지에서 클라우드까지 실시간 데이터 스트리밍 백본**. Kafka 토픽을 Unified Namespace의 메시지 버스로 활용하여 공장 데이터를 AI/분석 시스템에 밀리초 단위로 전달한다.

---

## 주요 기능

### 프로토콜 및 OT 연결
- **MQTT 브리지**: Kafka와 MQTT 브로커(HiveMQ, EMQX 등)를 연결하는 공식 커넥터 지원. 센서·게이트웨이 데이터를 Kafka 토픽으로 실시간 수집
- **OPC UA 연결**: MES/SCADA에서 OPC UA 서버 데이터를 Kafka Connector(Kepware, HighByte, Cogent DataHub 등 파트너 경유)로 수집
- **Modbus/기타 산업 프로토콜**: Kafka Connect 에코시스템의 커뮤니티 커넥터 또는 HighByte·Litmus 같은 OT 게이트웨이를 경유해 연결
- **Sparkplug B 지원**: Eclipse Sparkplug B 페이로드를 MQTT 위에서 처리하여 ERP/SCADA 간 표준 IIoT 통신 지원 (2025 현재 용 발표)

### 스트림 처리 (Edge·클라우드)
- **Apache Flink 통합**: Confluent Cloud 내 완전 관리형 Flink 엔진으로 실시간 필터링·집계·이상 탐지, CEP(Complex Event Processing)
- **Shift Left 아키텍처**: Siemens 사례(2025)처럼 처리 로직을 가능한 한 소스 가까이 배치해 클라우드 비용·지연 감소
- **Kafka Streams / ksqlDB**: 경량 스트림 처리 라이브러리, SQL 방언으로 실시간 집계

### 데이터 관리
- **Schema Registry**: Avro, JSON Schema, Protobuf 스키마 강제·버전 관리 → 시계열 포맷 표준화에 활용
- **Tiered Storage**: 오래된 토픽 데이터를 저비용 객체 스토리지(S3, Azure Blob)로 자동 계층화
- **데이터 품질 파이프라인**: Data Quality Rules(2024+)로 스키마 위반·null 비율 실시간 감지

### AI/LLM 통합 (2025~2026)
- **Confluent Streaming Agents**: AI 에이전트가 Kafka 스트림 데이터를 실시간으로 소비·행동 트리거
- **Vector DB 스트리밍**: Kafka→Pinecone, Weaviate, OpenSearch 벡터 인덱스 실시간 동기화

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 매핑 방식 |
|---|---|
| D-1 Physical 데이터 수집 | Kafka 토픽이 센서·PLC 스트림의 표준 수집 채널 |
| 데이터 리니지 | Schema Registry + Connect 커넥터 메타데이터로 토픽 수준 리니지 추적 |
| 실시간 데이터 품질 | Data Quality Rules, Flink 이상 탐지 |
| 스트리밍 컨텍스트화 | Flink/ksqlDB에서 설비 계층 테이블과 JOIN하여 컨텍스트 부여 |

---

## 강점

- **처리량 최강**: 초당 수백만 메시지 처리, 제조업 대규모 태그 스트림에 적합
- **생태계 풍부**: 200+ 공식 커넥터, HighByte·Litmus·AVEVA PI Connector 등 OT 파트너
- **Flink 통합**: 복잡한 이벤트 처리·머신러닝 파이프라인을 동일 플랫폼에서 처리
- **IBM 통합 시너지**: IBM MQ, watsonx, OpenShift와 통합으로 엔터프라이즈 AI 파이프라인 강화 예정

---

## 약점·주의점

- **시계열 저장 없음**: Kafka 자체는 영구 시계열 저장 DB가 아님. InfluxDB, TimescaleDB, ADX 등 별도 싱크 필요
- **OT 프로토콜 직접 지원 한계**: OPC UA·Modbus 직접 드라이버 없음 → HighByte, Litmus 등 OT 게이트웨이 선행 필요
- **운영 복잡도**: 클러스터 관리(ZooKeeper → KRaft 전환), 파티션 설계 등 Kafka 전문 지식 요구
- **IBM 인수 전환기 불확실성**: 제품 로드맵·가격 정책 변동 가능성 모니터링 필요

---

## 가격 모델

| 모델 | 내용 |
|---|---|
| Confluent Cloud | CKU(Confluent Kafka Unit) 기반 종량. 기본 클러스터 시간당 ~$0.11~ 시작; 데이터 처리량·커넥터 수에 따라 변동 |
| Confluent Platform | 연간 구독; 코어 수 또는 엔터프라이즈 계약 기반 |
| Apache Kafka OSS | 무료; 인프라·운영 비용은 자체 부담 |
| IBM 통합 이후 | IBM 엔터프라이즈 계약 형태로 통합 가능성 (2026~) |

---

## 연동 생태계

- **OT 게이트웨이**: HighByte Intelligence Hub, Litmus Edge, Cogent DataHub, MQTT X
- **시계열 저장**: InfluxDB, TimescaleDB, Apache Druid, Azure Data Explorer
- **AI/ML**: Databricks, Snowflake, Apache Spark, Flink ML, IBM watsonx
- **시각화**: Grafana, Apache Superset, Power BI (Kafka Source)
- **클라우드**: AWS MSK(관리형 Kafka), Azure Event Hubs(Kafka API 호환), Confluent Cloud

---

## 출처

- [Confluent Manufacturing IoT Solutions](https://www.confluent.io/industry-solutions/manufacturing/)
- [Kafka for IoT: 4 key capabilities and top use cases in 2026](https://www.instaclustr.com/education/apache-kafka/kafka-for-iot-4-key-capabilities-and-top-use-cases-in-2026/)
- [IBM Acquires Confluent 2026](https://www.scalytics.io/en-us/blog/ibm-confluent-acquisition-kafka-architecture-2026)
- [Siemens Shift Left Architecture with Confluent](https://www.kai-waehner.de/blog/2025/04/11/shift-left-architecture-at-siemens-real-time-innovation-in-manufacturing-and-logistics-with-data-streaming/)
- [Towards Manufacturing 5.0 with Sparkplug and Kafka](https://current.confluent.io/post-conference-videos-2025/towards-manufacturing-5-0---edge-iot-platform-with-sparkplug-and-apache-kafka-bng25)
- [Confluent MQTT IoT Use Cases](https://www.confluent.io/blog/iot-streaming-use-cases-with-kafka-mqtt-confluent-and-waterstream/)
