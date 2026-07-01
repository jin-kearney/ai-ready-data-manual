# Ignition (Inductive Automation) — OT/IoT 수집 솔루션

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Inductive Automation (캘리포니아 기반 민간 기업) |
| 라이선스 | 상용 (서버 단위 영구 라이선스; 태그 수 무제한) |
| 배포 형태 | On-premises, Ignition Edge, Ignition Cloud (클라우드 모듈) |
| 최신 동향 | Ignition 8.3 출시 — 강화된 보안, 스트림 데이터 관리, 고급 시각화, OT-IT 통합 기능; Cloud Hybrid Architecture 지원 |

## 한 줄 포지셔닝

> **태그 수 무제한 라이선스의 통합 산업 플랫폼(SCADA+MES+IIoT+Historian)**. 다양한 PLC 드라이버와 OPC UA를 기본 내장하고, 온프레미스·엣지·클라우드 하이브리드 구성이 가능한 제조업 현장의 실질적 선택지다.

---

## 주요 기능

### 데이터 수집
- **OPC UA 내장**: 표준 OPC UA 클라이언트·서버 기능 기본 포함. 모든 OPC UA 호환 PLC/SCADA 직접 연결
- **드라이버 내장**: Modbus TCP/RTU, Allen-Bradley (EtherNet/IP, DF1, DH+), Siemens S7, Mitsubishi, DNP3, BACnet 등 주요 PLC 브랜드 드라이버 포함 (별도 비용 없음)
- **MQTT (Cirrus Link 모듈)**: Sparkplug B 기반 MQTT 게이트웨이 모듈. Ignition Edge가 현장에서 Sparkplug 페이로드 발행, 중앙 Ignition 서버 수신
- **SQL 데이터베이스 연결**: MySQL, MS SQL, PostgreSQL, Oracle 등 직접 연결로 ERP·MES 데이터 통합

### Edge 처리 (Ignition Edge)
- **경량 Edge 에이전트**: 임베디드 하드웨어, 산업용 PC에 설치. 단방향 게이트웨이로 로컬 OT 데이터 수집 후 중앙 서버로 전달 (OT/IT 망분리 환경 적합)
- **로컬 캐싱**: 연결 단절 시 로컬 태그 값 버퍼링 후 재연결 시 동기화
- **로컬 HMI**: Edge에서 기본 HMI/대시보드 운영 가능

### Historian (시계열 저장)
- **내장 Historian**: SQL 데이터베이스를 Historian으로 활용. 태그 이력 압축·저장. 고해상도(ms 단위) 시계열 보존
- **스토어 앤 포워드**: 네트워크 장애 시 데이터 로컬 보관 후 전송
- **태그 히스토리 쿼리**: Vision/Perspective에서 트렌드 시각화, 커스텀 리포트 생성

### SCADA/MES/IIoT 통합
- **UDT (User Defined Types)**: 설비 유형별 표준 태그 구조 정의 → 동일 유형 설비에 일괄 적용. 컨텍스트화·표준화 핵심
- **Perspective (웹 SCADA)**: 반응형 웹 UI로 PC/모바일/태블릿 운영 현황 모니터링
- **Reporting Module**: PDF/Excel 보고서 자동 생성 — 생산 실적·품질·에너지 보고서
- **OEE Module**: 가용성·성능·품질 KPI 자동 계산 및 대시보드

### AI/클라우드 통합 (2025~2026)
- **Cloud Hybrid Architecture**: AI 분석을 위해 클라우드 서비스(Azure, AWS)와 연계 확장 가능
- **MQTT/Kafka 브리지**: Cirrus Link 모듈로 Kafka 토픽 또는 MQTT 클라우드로 데이터 스트리밍
- **Python 스크립팅**: Ignition 내 Python 스크립트로 전처리·ML 모델 호출 가능

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 매핑 방식 |
|---|---|
| D-1 Physical 데이터 수집 | 내장 드라이버(OPC UA, Modbus, EtherNet/IP 등)로 폭넓은 PLC 수집 |
| 시계열 표준화 | UDT 기반 태그 구조 표준화, Historian 압축 저장 |
| 컨텍스트화 | UDT + 설비 계층 태그 명명 규칙으로 컨텍스트 부여 |
| 데이터 품질 | 태그 이상 알람, Historian 품질 코드(Good/Bad/Uncertain) |
| 엣지 처리 | Ignition Edge 로컬 전처리·캐싱 |

---

## 강점

- **태그 수 무제한 라이선스**: 수십만 태그 환경에서도 라이선스 추가 비용 없음 — 타 솔루션 대비 명확한 TCO 우위
- **통합 플랫폼**: SCADA+MES+Historian+IIoT를 하나의 플랫폼으로 구성 가능. 벤더 복잡도 최소화
- **PLC 드라이버 포괄성**: 주요 PLC 브랜드 내장 드라이버로 레거시 장비 즉시 연결
- **제조업 레퍼런스**: 전 세계 9,000+ 조직, 식음료·제약·자동차·에너지 다양한 산업 구축 사례
- **망분리 친화**: Ignition Edge 단방향 게이트웨이로 OT/IT 분리 환경 안전한 데이터 수집

---

## 약점·주의점

- **클라우드 네이티브 부족**: Azure/AWS 수준의 완전 관리형 클라우드 기능은 별도 모듈 또는 외부 서비스 조합 필요
- **고속 스트리밍 한계**: Kafka 수준의 고성능 이벤트 스트리밍이나 복잡한 실시간 스트림 처리는 적합하지 않음
- **스케일 아웃 복잡도**: 수백 개 공장 규모 멀티사이트 배포 시 아키텍처 설계·운영 복잡도 증가
- **DB 병목**: Historian이 SQL 기반이라 초대용량·초고빈도 데이터(ms 단위 진동 등)에서 성능 한계 가능

---

## 가격 모델

| 모델 | 내용 |
|---|---|
| Ignition 서버 라이선스 | 서버당 영구 라이선스 ($~$7,500~$14,000/서버, 버전·모듈에 따라 변동); 태그 수 무제한 |
| Ignition Edge | Edge 노드당 라이선스 ($~$1,000~$2,500) |
| 추가 모듈 | OEE, Reporting, BACnet 등 기능 모듈별 추가 구매 |
| 연간 유지보수 | 라이선스의 20~25% 수준 |

---

## 연동 생태계

- **클라우드**: Cirrus Link MQTT 모듈 → AWS IoT, Azure IoT Hub, Google Cloud IoT; InfluxDB, Timescale Cloud
- **ERP/MES**: SAP (OPC UA), Oracle, Infor, custom SQL 연결
- **AI/분석**: Python 스크립팅, HighByte Intelligence Hub(OT 데이터 정제 후 AI 플랫폼), Power BI
- **시각화**: Ignition Perspective (웹 내장), Tableau, Grafana
- **산업 표준**: ISA-95, ISA-88, OPC UA, Sparkplug B

---

## 출처

- [Ignition 공식 플랫폼 페이지](https://inductiveautomation.com/ignition/)
- [Ignition SCADA 제조업 페이지](https://page.inductiveautomation.com/industry/manufacturing)
- [Ignition과 SCADA: 산업 자동화의 미래 (2025)](https://iotechcontrols.com/2025/02/14/ignition-and-scada-the-future-of-industrial-automation/)
- [Gartner Peer Insights: Ignition 2026](https://www.gartner.com/reviews/product/ignition)
- [Inductive Automation 공식 홈페이지](https://inductiveautomation.com/)
