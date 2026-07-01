# InfluxDB + Telegraf — OT/IoT 수집 솔루션

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | InfluxData (샌프란시스코 기반) |
| 라이선스 | InfluxDB OSS: MIT 라이선스 / InfluxDB Cloud: 상용 SaaS / InfluxDB Enterprise: 상용 |
| 배포 형태 | OSS(자체 운영), InfluxDB Cloud(SaaS), InfluxDB Enterprise(온프레미스 고가용성) |
| 최신 동향 | InfluxDB 3.0 (Apache Arrow 기반, SQL 지원 강화, 성능 대폭 향상); Telegraf Enterprise 출시 (컨트롤 플레인 + UI 중앙 관리); TimescaleDB와 시장 경쟁 심화 |

## 한 줄 포지셔닝

> **오픈소스 기반 목적형 시계열 DB + 유연한 에이전트(Telegraf)**. MIT 라이선스 OSS부터 엔터프라이즈까지 다양한 배포 옵션을 제공하며, 400+ Telegraf 플러그인으로 OT 센서부터 클라우드 메트릭까지 단일 파이프라인으로 수집한다.

---

## 주요 기능

### Telegraf (데이터 수집 에이전트)
- **400+ 플러그인**: 입력(Input), 출력(Output), 처리(Processor), 집계(Aggregator) 플러그인 생태계
- **OT/IoT 주요 플러그인**:
  - **OPC UA** (`inputs.opcua`): OPC UA 서버 태그 폴링·구독
  - **Modbus** (`inputs.modbus`): Modbus TCP/RTU 레지스터 직접 폴링
  - **MQTT Consumer** (`inputs.mqtt_consumer`): MQTT 토픽 구독 → InfluxDB 라인 프로토콜 변환
  - **SNMP, HTTP, Kafka, AMQP** 등 다수 IT·IoT 프로토콜 지원
- **경량 설계**: Go 언어 단일 바이너리, 외부 의존성 없음 → 산업용 임베디드 PC 배포 가능
- **Telegraf Enterprise (2025)**: 중앙 컨트롤러 UI로 수백 개 Telegraf 에이전트 상태 모니터링·설정 배포

### InfluxDB 3.0 시계열 저장
- **Apache Arrow 기반 컬럼형 스토리지**: 기존 TSM 포맷 대비 쿼리 성능 대폭 향상 (집계·스캔 워크로드)
- **SQL 지원**: InfluxQL과 함께 표준 SQL 쿼리 지원 — 데이터 분석가 접근성 향상
- **시계열 최적화**: 자동 시간 기반 파티셔닝, 다운샘플링(Downsampling), 데이터 보존 정책(Retention Policy)
- **Flux 쿼리 언어**: 시계열 특화 함수(이동 평균, 결측값 보간, 이상 탐지)

### Edge 복제·클라우드 통합
- **Edge Replication**: InfluxDB Edge 인스턴스 데이터를 InfluxDB Cloud로 자동 복제 → 엣지+클라우드 이중 저장
- **InfluxDB Cloud Serverless**: 용량 계획 없이 자동 스케일링; Pay-per-use
- **AWS 통합**: InfluxDB Edge → Amazon Timestream Edge Replication (AWS 공식 지원)

### AI/ML 통합
- **Python 클라이언트**: influxdb-client-python으로 ML 파이프라인 직접 연결
- **예측 유지보수**: 진동·온도 시계열을 AI 이상 탐지 모델 입력으로 직접 사용
- **Grafana 연동**: InfluxDB Data Source 플러그인으로 실시간 대시보드

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 매핑 방식 |
|---|---|
| D-1 Physical 데이터 수집 | Telegraf OPC UA/Modbus/MQTT 플러그인으로 센서·PLC 직접 수집 |
| 시계열 저장·표준화 | InfluxDB 3.0 시계열 최적화 저장 + 자동 다운샘플링 |
| 데이터 품질 | Telegraf Processor 플러그인으로 이상값 필터링·변환 |
| AI 학습 데이터 | Python 클라이언트로 시계열 데이터 직접 ML 파이프라인 연결 |
| 엣지-클라우드 복제 | Edge Replication 기능으로 로컬+클라우드 이중 보관 |

---

## 강점

- **오픈소스 최소 비용**: OSS 버전 무료 사용. 소규모 사이트·PoC에 즉시 도입 가능
- **플러그인 풍부성**: 400+ Telegraf 플러그인으로 거의 모든 소스 커버. 커스텀 플러그인 개발도 단순
- **SQL 지원 (3.0)**: 시계열 데이터에 표준 SQL을 사용할 수 있어 데이터 팀 진입 장벽 낮음
- **경량 배포**: Telegraf 단일 바이너리 + InfluxDB 단일 프로세스 → 낮은 시스템 요구사항
- **TimescaleDB 보완**: InfluxDB가 순수 시계열에 집중한다면, 관계형 JOIN이 필요한 경우 Telegraf→TimescaleDB 조합 활용

---

## 약점·주의점

- **컨텍스트화 없음**: 태그 기반 원시 시계열 저장. 설비 계층 컨텍스트화는 HighByte, AVEVA AF 등 별도 솔루션 필요
- **엔터프라이즈 기능 부족**: 멀티테넌시, RBAC, 감사 로그 등 엔터프라이즈 기능은 상용 버전 필요
- **고가용성 구성 복잡**: OSS 단일 노드 기준. HA 클러스터는 Enterprise 버전(고비용) 또는 별도 아키텍처 필요
- **3.0 전환 혼선**: InfluxDB 1.x/2.x → 3.0 API 일부 비호환. 기존 Flux 코드 마이그레이션 필요

---

## 가격 모델

| 모델 | 내용 |
|---|---|
| InfluxDB OSS | 무료 (MIT 라이선스); 단일 노드, HA 미지원 |
| InfluxDB Cloud (Serverless) | 무료 플랜 (제한적) + 종량: 쓰기 ~$0.002/MB, 쿼리 ~$0.01/GB |
| InfluxDB Cloud Dedicated | 전용 클러스터; 연간 계약 기반 |
| InfluxDB Enterprise | 온프레미스 고가용성; 서버 수 기반 연간 계약 |
| Telegraf Enterprise | 에이전트 관리 플랫폼; 별도 구독 |

---

## 연동 생태계

- **OT 수집**: Telegraf OPC UA/Modbus/MQTT 플러그인 (직접), Litmus Edge, Kepware (Telegraf HTTP 연동)
- **시각화**: Grafana (공식 데이터 소스), Chronograf (InfluxData 자체), Kibana
- **AI/ML**: Python (influxdb-client), Jupyter Notebook, MLflow
- **클라우드**: AWS (Timestream Edge Replication), Azure Event Hub → Telegraf, Google Cloud
- **데이터 파이프라인**: Apache Kafka (Telegraf Kafka Output), Telegraf→TimescaleDB

---

## 출처

- [InfluxDB Trends 2025-2026](https://calmops.com/database/influxdb/influxdb-trends/)
- [Telegraf 공식 문서](https://docs.influxdata.com/telegraf/v1/)
- [InfluxDB Cloud IoT](https://www.influxdata.com/influxdb-cloud-iot/)
- [InfluxDB Edge → AWS Timestream 통합](https://aws.amazon.com/blogs/database/simplify-industrial-iot-use-influxdb-edge-replication-for-centralized-time-series-analytics-with-amazon-timestream/)
- [Gartner: InfluxData Telegraf 2025](https://www.gartner.com/reviews/market/global-industrial-iot-platforms/vendor/influxdata/product/telegraf)
- [InfluxDB Industrial IoT + AWS](https://www.iiot-world.com/industrial-iot/connected-industry/optimize-industrial-iot-data-with-influxdb-and-aws/)
