# AWS IoT SiteWise — OT/IoT 수집 솔루션

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Amazon Web Services (AWS) |
| 라이선스 | 종량과금(Pay-as-you-go) |
| 배포 형태 | AWS Cloud + SiteWise Edge Gateway(On-prem/Edge) |
| 최신 동향 | SiteWise Assistant(자연어 쿼리, 2025); Edge 이상 탐지 모델 로컬 재학습; Litmus Edge 공식 통합(250+ 프로토콜); AWS re:Invent 2025 "산업 클라우드의 물리 세계 진입" |

## 한 줄 포지셔닝

> **AWS 기반 완전 관리형 산업 IoT 플랫폼**. 에셋 모델(Asset Model)로 설비 계층을 표준화하고 Edge에서 클라우드까지 시계열 데이터를 관리하며, SiteWise Assistant로 현장 작업자가 자연어로 운영 데이터를 조회할 수 있다.

---

## 주요 기능

### 데이터 수집 (Edge Gateway)
- **OPC UA 직접 지원**: SiteWise Edge Gateway가 OPC UA 서버에 직접 연결. 인증서 기반 보안 통신
- **Modbus TCP/RTU**: Edge Gateway를 통해 Modbus 디바이스 데이터 수집
- **MQTT**: AWS IoT Core와 연계하여 MQTT 디바이스 데이터 수집
- **Litmus Edge 통합**: 250+ 산업 프로토콜(Siemens S7, Allen-Bradley, Fanuc 등 레거시 PLC 포함) 연결로 프로토콜 폭 대폭 확장
- **오프라인 내성**: 인터넷 단절 시 최대 30일 로컬 저장 후 재연결 시 자동 동기화

### 에셋 모델링 (Asset Model)
- **계층적 에셋 정의**: 설비→라인→공장 계층 구조 정의. 각 에셋에 속성(온도, 압력 등) 연결
- **측정값 자동 매핑**: OPC UA 태그 → 에셋 속성 자동 매핑
- **지표 계산**: 에셋 수준에서 KPI(OEE, 가동률) 로컬 또는 클라우드 계산
- **디지털 트윈 기반**: SiteWise 에셋 모델이 디지털 트윈의 물리적 계층 역할

### 시계열 저장·분석
- **SiteWise 시계열 DB**: 완전 관리형 시계열 저장. 원시값 및 집계값(분/시/일 평균·최대·최소) 자동 생성
- **SiteWise Monitor**: 웹 기반 운영 대시보드. 코드 없이 실시간 트렌드·알람 구성
- **데이터 내보내기**: S3, Amazon Timestream, AWS Lake Formation으로 자동 내보내기 → Athena/SageMaker 연결

### AI 통합 (2025~2026)
- **SiteWise Assistant**: 자연어 쿼리 ("Pump A 진동 원인은?") — 현장 작업자 대상 운영 데이터 민주화
- **Edge ML 모델 재학습**: 이상 탐지 모델을 로컬 Edge에서 재학습 → 인터넷 없이 AI 추론 가능
- **SageMaker 통합**: SiteWise 시계열 → SageMaker Feature Store → ML 모델 학습·배포

---

## AI-Ready Data 주제 매핑

| AI-Ready Data 주제 | 매핑 방식 |
|---|---|
| D-1 Physical 데이터 수집 | Edge Gateway(OPC UA/Modbus) + Litmus 250+ 프로토콜 |
| 시계열 표준화 | 에셋 모델 속성으로 단위·계층 표준화 |
| 컨텍스트화 | Asset Model 계층이 AI 학습 데이터의 컨텍스트 레이블 |
| 데이터 품질 | 집계 이상 탐지, Edge ML 모델 |
| AI-Ready 파이프라인 | SiteWise→S3→SageMaker 원클릭 파이프라인 |

---

## 강점

- **완전 관리형**: 서버 관리·패치·스케일링 불필요. 제조업 IT 역량이 제한적인 사이트에 적합
- **에셋 모델 표준화**: 설비 계층 정의 → AI 모델이 소비하는 컨텍스트 일관성 보장
- **AWS 생태계 통합**: S3, Athena, SageMaker, QuickSight와 원클릭 연결
- **SiteWise Assistant**: 자연어 쿼리로 현장 엔지니어·생산관리자의 데이터 접근성 향상
- **Litmus 파트너십**: 레거시 PLC 250+ 프로토콜 지원으로 OT 프로토콜 폭 보완

---

## 약점·주의점

- **AWS 벤더 락인**: 다클라우드·온프레미스 전용 환경에서 유연성 낮음
- **쿼리 비용**: 데이터 포인트 조회 수 기반 과금 — 고빈도 실시간 분석 시 비용 급증
- **복잡 이벤트 처리 한계**: Kafka/Flink 수준의 스트리밍 CEP(Complex Event Processing) 기능은 AWS IoT Events·Lambda 조합으로 별도 구성 필요
- **대용량 고빈도 데이터**: 초당 수십만 포인트 이상 고해상도 진동 데이터는 비용 구조 재검토 필요

---

## 가격 모델

| 항목 | 내용 |
|---|---|
| 데이터 포인트 | 수집 포인트당 과금 ($0.05/10만 포인트) |
| 데이터 조회 | 조회 포인트당 과금 ($0.001/1만 포인트) |
| Edge Gateway | Edge 처리당 과금 + EC2/Greengrass 비용 |
| 스토리지 | S3 표준 스토리지 + SiteWise 시계열 스토리지 분리 과금 |

---

## 연동 생태계

- **OT 프로토콜 확장**: Litmus Edge (250+ 프로토콜), Kepware, OSIsoft PI Connector
- **AI/ML**: Amazon SageMaker, Lookout for Equipment (이상 탐지 전용 서비스)
- **데이터 레이크**: Amazon S3, AWS Lake Formation, AWS Glue, Amazon Timestream
- **시각화**: Amazon QuickSight, Grafana (Amazon Managed Grafana)
- **산업 파트너**: Siemens (OT-IT 통합 솔루션), Rockwell Automation

---

## 출처

- [AWS IoT SiteWise 공식 기능](https://www.amazonaws.cn/en/iot-sitewise/features/)
- [AWS IoT SiteWise + Litmus 통합](https://aws.amazon.com/blogs/industries/unlocking-industrial-data-potential-with-aws-iot-sitewise-edge-and-litmus/)
- [AWS re:Invent 2025 산업 클라우드](https://www.arcweb.com/blog/aws-reinvent-2025-how-industrial-cloud-becoming-physical)
- [Siemens OT-IT AWS 통합](https://www.siemens.com/en-us/company/insights/industrial-operations-x/architecture-hub/aws-ot-it-integration/)
- [AWS IoT SiteWise 보안 아키텍처](https://docs.aws.amazon.com/whitepapers/latest/securing-iot-with-aws/aws-iot-sitewise-edge-and-cloud-processing-for-industrial-data.html)
- [Top 10 IIoT Platforms 2026](https://iiotblog.com/2025/12/12/top-10-iiot-platforms-to-watch-in-2026/)
