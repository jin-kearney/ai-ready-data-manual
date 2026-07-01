# Azure IoT (IoT Hub + Azure IoT Operations + Fabric RTI) — OT/IoT 수집 솔루션

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Microsoft |
| 라이선스 | 종량과금(Pay-as-you-go) |
| 배포 형태 | Azure Cloud + Azure IoT Operations(Edge, Arc 기반) |
| 최신 동향 | Azure IoT Operations GA(2024); Hannover Messe 2026에서 AI Agent + OT 통합 발표; Fabric Real-Time Intelligence(RTI) = 구 Azure Data Explorer(ADX) 기반 강화 |

## 한 줄 포지셔닝

> **Microsoft Azure 기반 공장 데이터의 엣지-투-클라우드 일관 파이프라인**. Azure IoT Operations가 OT 엣지에서 OPC UA 데이터를 수집·처리하고, Microsoft Fabric Real-Time Intelligence에서 AI 기반 실시간 분석을 제공한다.

---

## 주요 기능

### Azure IoT Hub
- **디바이스 등록·보안**: 수백만 디바이스 인증서 기반 양방향 통신(MQTT, AMQP, HTTPS)
- **메시지 라우팅**: 규칙 기반 조건 라우팅 → Azure Stream Analytics, Event Hubs, Storage, Service Bus
- **디바이스 트윈(Device Twin)**: 디바이스 상태·설정의 클라우드 미러 유지. 원격 구성·펌웨어 업데이트 지원
- **한계**: 직접 OPC UA/Modbus 수집 기능 없음 → Azure IoT Operations로 보완

### Azure IoT Operations (Edge — Arc 기반)
- **OPC UA Broker 내장**: OPC UA 서버 직접 연결, OPC UA over MQTT 변환
- **MQTT Broker**: 엣지 MQTT 브로커로 센서·게이트웨이 데이터 수집; Sparkplug B 지원
- **데이터 파이프라인(Dataflow)**: 엣지에서 필터링·변환·라우팅 후 IoT Hub·Event Hub·Fabric로 전송
- **Arc 기반 관리**: Kubernetes 클러스터(온프레미스/엣지)를 Azure Arc로 중앙 관리·배포
- **보안**: X.509 인증서, TLS 1.3, OT/IT 망분리 지원

### Azure Data Explorer (ADX) / Fabric Real-Time Intelligence (RTI)
- **KQL(Kusto Query Language)**: 수십억 행 시계열 데이터의 초 단위 쿼리
- **Eventstream**: Fabric 내 IoT Hub 스트림을 실시간 수집, 자동 파싱·변환 후 KQL Database로 적재
- **Real-Time Dashboard**: 초 단위 갱신 운영 현황판
- **EventHouse**: Fabric RTI의 시계열 저장소 — 압축·파티셔닝 최적화

### AI 통합 (2025~2026)
- **Hannover Messe 2026**: 공장 데이터+Copilot AI Agent — 이상 탐지 자동화, 자연어 운영 쿼리
- **Azure OpenAI + Fabric**: Eventstream 데이터를 RAG(Retrieval-Augmented Generation) 파이프라인에 연결
- **Predictive Maintenance**: 진동·온도 데이터를 엣지에서 전처리 후 Azure ML 이상 탐지 모델 연동 — 45% 다운타임 감소 사례

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 매핑 방식 |
|---|---|
| D-1 Physical 데이터 수집 | IoT Operations OPC UA Broker + IoT Hub MQTT |
| 시계열 표준화 | ADX/RTI EventHouse에 시계열 스키마 강제 |
| 실시간 컨텍스트화 | Dataflow에서 설비 메타데이터 JOIN |
| 데이터 품질 | KQL 기반 이상 탐지, Eventstream 데이터 정합성 규칙 |
| AI-Ready 파이프라인 | Fabric RTI→ML/OpenAI 직접 연결 |

---

## 강점

- **풀스택 일관성**: 엣지(IoT Ops)→클라우드(IoT Hub)→분석(Fabric RTI)→AI(Azure OpenAI) 단일 벤더 일관 파이프라인
- **Fabric 통합**: Power BI, Synapse, ML, OpenAI가 모두 Fabric 내 원클릭 연결
- **Arc 중앙 관리**: 다공장·다계열사 엣지 Kubernetes를 Azure Arc로 단일 콘솔 관리
- **ADX 쿼리 성능**: 수십억 행 시계열 KQL 쿼리 성능 업계 최고 수준

---

## 약점·주의점

- **벤더 락인**: Azure 생태계 의존도 높음. 멀티클라우드 전략 시 별도 추상화 레이어 필요
- **온프레미스 완전 배포 한계**: IoT Hub는 클라우드 필수. Arc 없이 완전 오프라인 환경 지원 불가
- **Modbus 직접 지원 제한**: IoT Operations에서 Modbus 직접 드라이버 없음 → OT 게이트웨이 경유 필요
- **비용 복잡성**: IoT Hub 메시지 수 + Arc + ADX CU + Fabric CU 등 복합 과금; 대규모 공장에서 비용 추정 어려움

---

## 가격 모델

| 컴포넌트 | 내용 |
|---|---|
| Azure IoT Hub | 메시지 수 기반 종량 (무료 8,000/일; 기본 ~$10/월/50만 메시지) |
| Azure IoT Operations | Arc-enabled K8s 클러스터당 과금 |
| Azure Data Explorer | CU(Compute Unit) + 스토리지 기반 |
| Microsoft Fabric RTI | Fabric CU(F-SKU) 기반 구독 |

---

## 연동 생태계

- **OT 게이트웨이**: Kepware (PTC), Cogent DataHub, Litmus Edge, HighByte (IoT Ops 경유)
- **AI/ML**: Azure Machine Learning, Azure OpenAI, Databricks on Azure
- **시각화**: Power BI, Grafana (ADX 데이터 소스)
- **엔터프라이즈**: SAP 통합(Azure + SAP), Microsoft 365 Copilot
- **OT 보안**: Microsoft Defender for IoT (OT 네트워크 NDR)

---

## 출처

- [Azure IoT Operations + Microsoft Fabric 블로그](https://www.btelligent.com/en/blog/real-time-intelligence-azure-iot-microsoft-fabric)
- [Microsoft Hannover Messe 2026](https://www.microsoft.com/en-us/microsoft-cloud/blog/manufacturing/2026/04/16/industrial-intelligence-unlocked-microsoft-at-hannover-messe-2026/)
- [Azure IoT + ADX 아키텍처](https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/iot-azure-data-explorer)
- [Azure IoT Hub + IoT Operations 브리징](https://techcommunity.microsoft.com/blog/iotblog/bridging-the-digital-and-physical-worlds-with-azure-iot-hub-and-azure-iot-operat/4469774)
- [Azure IoT Manufacturing Guide 2026](https://artificial-intelligence-wiki.com/industry-ai/manufacturing-and-industrial-automation/azure-iot-manufacturing-guide/)
- [Automotive Fabric RTI 마이그레이션 사례](https://www.tcs.com/what-we-do/industries/manufacturing/case-study/automotive-supplier-migrates-to-fabric-real-time-intelligence)
