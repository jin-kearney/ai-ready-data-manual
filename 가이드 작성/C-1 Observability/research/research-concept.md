# C-1 데이터 Observability — 개념 리서치

> 작성일: 2026-06-24  
> 관점 고정: AI가 쓸 데이터를 **운영 중 지켜보고 이상을 잡아내는** 법. 데이터 파이프라인·데이터셋 모니터링 관점.  
> 독자: 제조 현업·데이터 조직

---

## 1. 데이터 Observability의 관측 축 (5 Pillars)

Monte Carlo가 정의한 "5 Pillars of Data Observability"는 데이터 다운타임(data downtime) — 데이터가 누락되거나 부정확하거나 지연되는 상태 — 을 방지하기 위한 5가지 관측 차원이다. DevOps 모니터링 개념을 데이터 파이프라인에 적용한 프레임워크다.

### 1-1. Freshness (신선도)
- **무엇을 보나**: 데이터가 얼마나 최신인가. 테이블이 얼마나 자주 갱신되는가.
- **이상 신호**: 갱신이 멈추거나 주기가 틀어짐. 파이프라인이 중단된 첫 번째 증거.
- **제조 예시**: 설비 센서 데이터가 1분마다 들어와야 하는데 10분째 새 레코드가 없을 때. 결함 분류 AI의 학습 데이터가 어제 기준으로 멈춰 있을 때.

### 1-2. Volume (양·건수)
- **무엇을 보나**: 데이터 저장소의 레코드 수·용량이 기대 범위 안에 있는가.
- **이상 신호**: "2억 건이 갑자기 500만 건으로 줄면 알아야 한다"(Monte Carlo). 급격한 양 감소는 파이프라인 중단·누락의 직접 지표.
- **제조 예시**: 라인별 품질검사 결과 레코드가 평소 하루 5만 건인데 오늘 200건만 적재됨 → 수집 어댑터 장애 또는 라인 다운.

### 1-3. Schema (스키마)
- **무엇을 보나**: 테이블 구조(필드 추가·삭제·타입 변경·테이블 제거)가 바뀌었는가.
- **이상 신호**: 스키마 변경은 데이터 다운타임 사고의 주요 원인. 예: 센서 단위 필드가 °C → °F로 바뀌는 경우.
- **제조 예시**: PLC(공장제어시스템) 업그레이드 후 "pressure_kpa" 컬럼이 "pressure_mpa"로 이름이 바뀌어 하위 AI 모델 입력값이 100배로 스케일 오류.

### 1-4. Lineage (계보)
- **무엇을 보나**: 데이터가 어디서 와서 어디로 흘러가는가. 어떤 상위(upstream) 소스와 하위(downstream) 소비자가 연결돼 있는가.
- **이상 신호**: 어떤 팀이 데이터를 생성하고 누가 읽는지 파악 → 문제 발생 시 영향 범위 즉시 파악.
- **제조 예시**: 용접 공정 데이터 파이프라인에 문제 발생 → Lineage로 "이 파이프를 쓰는 AI 모델 3개, 보고서 2개"를 즉시 파악하여 알림 대상 결정.

### 1-5. Distribution / Quality (분포·품질)
- **무엇을 보나**: 필드 수준의 값 분포 — null 비율, 고유값 비율, 값 범위 이탈, 이상치.
- **이상 신호**: "평소 null 비율이 2%인데 갑자기 40%로 치솟음"(Monte Carlo). 값이 허용 범위를 벗어남.
- **제조 예시**: 온도 센서 값이 갑자기 -999(오류 코드)로 채워지거나, 두께 측정값이 물리적으로 불가능한 음수로 기록되는 경우.

**참고**: 일부 벤더는 Lineage를 별도 플랫폼(C-3 데이터 계통)으로 분리하고 Observability는 나머지 4개 축에 집중하기도 한다.

---

## 2. 이상 판단 방식 — 고정 임계값 vs ML 자동 베이스라인

### 2-1. 고정 임계값(Rule/Threshold) 방식
- **작동 방식**: 사전에 "volume < 1,000건이면 알림" 같은 규칙을 직접 작성.
- **적합한 경우**:
  - 값이 물리적 한계나 비즈니스 규칙으로 명확히 정해질 때 (예: 온도 > 150°C = 이상, 디스크 > 90% = 위험).
  - 법적·컴플라이언스 기준이 고정값으로 정의될 때.
  - 단순하고 예측 가능한 패턴(분산 적음).
- **한계**: 계절성·주기성을 고려하지 못함. 정상 변동에도 알림 → 알림 피로(alert fatigue).

### 2-2. ML 자동 베이스라인(Adaptive Baseline) 방식
- **작동 방식**: 과거 추세·계절성·요일 패턴을 학습해 "이 시간대의 정상 범위"를 동적으로 계산. 그 범위를 벗어날 때만 알림.
- **적합한 경우**:
  - 데이터 량·분포가 계절·주기에 따라 변하는 경우 (예: 주말 생산 감소, 분기 말 데이터 급증).
  - 임계값을 직접 정하기 어려운 복잡한 파이프라인.
  - 대규모 파이프라인으로 수동 임계값 관리가 불가능할 때.
- **한계**: 학습 초기 정확도 낮음. 설명 가능성이 낮아 현업 신뢰 확보가 어려울 수 있음.

### 2-3. 알림 피로(Alert Fatigue)와 완화법
**문제**: 고정 임계값 기반 알림은 "정상 오토스케일, 주말 배치, 시간대 변화"에도 발화 → 팀이 알림을 무시하기 시작 → 진짜 이상을 놓침. CNCF 2024 조사에 따르면 63%의 조직이 알림 피로를 유효한 인시던트 대응의 주요 장벽으로 꼽음.

**완화 방법**:
| 방법 | 설명 |
|------|------|
| 심각도 등급 조정 | 모든 알림을 같은 채널로 보내지 않고, 심각도에 따라 채널 분리 |
| 중복 묶기(Grouping) | 동일 원인 파이프라인의 연속 알림을 하나의 인시던트로 집계 |
| 억제 윈도우(Suppression Window) | 계획된 배치 작업·유지보수 중에는 알림 억제 |
| 적응형 학습(Adaptive Learning) | ML이 해결 피드백을 받아 베이스라인 지속 정제 |
| 임팩트 기반 우선순위 | 비즈니스 영향 큰 파이프라인 알림을 우선, 저위험은 로그만 |

---

## 3. 알림·심각도(Severity) 운영

### 3-1. 인시던트 심각도 등급 (데이터 파이프라인 적용)

| 등급 | 상황 | 알림 대상 | 채널 | 응답 시간 |
|------|------|-----------|------|-----------|
| **SEV1** (Critical) | 핵심 데이터 파이프라인 완전 중단, 데이터 손실, AI 서비스 즉각 영향 | 온콜 담당 + 백업 + DataOps 리드 + 데이터 오너 + AI 서비스 운영자 | PagerDuty 즉시 호출 + Slack #incidents | 5분 내 확인 |
| **SEV2** (Major) | 핵심 데이터 흐름 손상·지연, 주요 AI 피처 결함, 부분 우회 가능 | 온콜 담당 + DataOps 팀 리드 | PagerDuty + Slack 채널 생성 | 30분 내 확인 |
| **SEV3** (Minor) | 특정 서브셋 품질 이상, 우회로 있음, AI 서비스 즉각 영향 없음 | DataOps 팀 | Slack 알림 (업무시간) | 당일 처리 |
| **SEV4** (Info) | 스키마 경고, 소수 필드 이상, 리포팅 지연 (사용자 비영향) | 담당자 | 로그 기록 / 티켓 생성 | 정기 검토 |

### 3-2. 알림 대상과 역할
- **데이터 오너(Data Owner)**: 해당 데이터 도메인의 비즈니스 책임자. SEV1·SEV2에서 필수 통보.
- **DataOps 팀**: 파이프라인 운영·수리 담당. SEV1~SEV3 모두 포함.
- **AI 서비스 운영자**: 해당 데이터를 쓰는 AI 모델·서비스 팀. Lineage 정보로 영향 범위 파악 후 선별 통보.

### 3-3. 에스컬레이션
- SEV1: 10분 내 확인 없으면 엔지니어링 매니저 자동 에스컬레이션.
- SEV2: 30분 내 미해결 시 팀 리드로 에스컬레이션.
- 심각도(Severity)와 우선순위(Priority)는 별개: 스테이징 환경 스키마 오류는 심각도 높으나 우선순위 낮음(프로덕션 미영향).

---

## 4. AI 결과 이상 — 데이터 문제 vs 모델/Prompt 문제 구분

### 4-1. 핵심 개념: 전체 스택 책임 (Full-Stack Observability)

AI 모델 성능이 떨어졌을 때 "모델이 잘못된 건지, 데이터가 잘못된 건지, Prompt가 바뀐 건지"를 구분하려면 **각 레이어의 버전과 상태를 함께 기록**해야 한다.

```
[입력 데이터 버전] → [전처리 파이프라인 버전] → [피처스토어 버전]
        ↓
[모델 체크포인트 버전] → [Prompt 버전] → [AI 결과]
```

### 4-2. 데이터 드리프트 vs 개념 드리프트

| 구분 | 정의 | 탐지 신호 | 원인 후보 |
|------|------|-----------|-----------|
| **데이터 드리프트 (Data Drift)** | 모델에 입력되는 데이터의 분포가 학습 시점과 달라짐 | 입력 피처 통계값(평균·분산·null율) 변화, PSI(Population Stability Index) > 0.2 | 센서 교체·보정 변경, 스키마 변경, 수집 파이프라인 오류 |
| **개념 드리프트 (Concept Drift)** | 입력-출력 관계(모델이 학습한 패턴)가 현실과 달라짐 | 입력 분포는 안정적인데 예측 정확도 하락 | 제품 설계 변경, 공정 파라미터 변경, 계절 패턴 변화 |

**제조 예시**:
- **데이터 드리프트**: 새 설비로 교체 후 진동 센서 측정 단위가 mm/s → g로 바뀜 → 모델 입력값 분포가 갑자기 변함.
- **개념 드리프트**: 부품 재질이 바뀜 → 같은 온도값이지만 불량 발생 패턴이 달라짐 → 모델 학습 시점의 "정상" 기준이 유효하지 않음.

### 4-3. 원인 후보 분리 방법 (Lineage 기반)

원인 후보를 분리하기 위해 기록해야 할 항목:

| 기록 항목 | 내용 | 확인 포인트 |
|-----------|------|-------------|
| 데이터 버전 | 학습·추론에 쓰인 데이터 스냅샷 | 이 시점 데이터에 스키마/분포 변화 있었나? |
| 전처리 버전 | 전처리 코드·파이프라인 커밋 | 정규화 로직·필터 조건이 바뀌었나? |
| 피처스토어 버전 | 어떤 피처 집합을 사용했나 | 피처 정의가 변경되었나? |
| 모델 체크포인트 | 추론에 사용된 모델 가중치 버전 | 재학습·배포 이력 |
| Prompt 버전 | LLM 기반 AI의 경우 Prompt 텍스트 버전 | Prompt 문구 변경 이력 |

**절차**: 모델 성능 하락 감지 → Lineage로 상위 파이프라인 추적 → 각 버전 비교로 변경점 확인 → "입력 분포가 변했으면 데이터 드리프트, 분포는 안정적인데 성능만 하락하면 개념 드리프트 또는 모델 문제"로 분기.

Galileo AI의 프레임워크는 "PSI > 0.2 = 데이터 드리프트 의심, 예측 엔트로피 상승 = 개념 드리프트 의심"으로 신호를 구분한다.

---

## 5. 운영 수준 KPI

### 5-1. 핵심 지표 정의

| KPI | 영문 | 정의 | 방향 |
|-----|------|------|------|
| **이상 감지 시간** | MTTD (Mean Time to Detect) | 이상이 발생한 시점부터 탐지될 때까지의 평균 시간 | ↓ 낮을수록 좋음 |
| **해결 시간** | MTTR (Mean Time to Resolve) | 탐지 후 완전 해결까지의 평균 시간 | ↓ 낮을수록 좋음 |
| **놓친 건수** | Missed Incidents | 모니터링이 감지하지 못하고 다른 경로(사용자 신고 등)로 발견된 이상 건수 | ↓ 낮을수록 좋음 |
| **오탐률** | False Positive Rate | 전체 알림 중 실제 이상이 아닌 알림의 비율 | ↓ 낮을수록 좋음 |
| **관측 커버리지** | Monitored Pipeline Coverage | 전체 데이터 파이프라인 중 Observability 모니터링이 적용된 비율 | ↑ 높을수록 좋음 |

### 5-2. 업계 참고 기준값

| 지표 | 현황 평균 | 성숙 조직 목표 | 출처 |
|------|-----------|----------------|------|
| MTTD | 수 시간~수 일 | < 5분 (2026 목표) | GrayCella (2026) |
| MTTR | 수 일 | 수 시간 수준 | Pantomath, Databand |
| False Positive Rate | 30% 이상이면 위험 신호 | 가능한 최소화 | CNCF 2024 조사 |
| 알림 노이즈 감소 (ML 도입 시) | — | 30~50% 감소 | Gartner 2024 |

> **주의**: MTTD/MTTR 벤치마크는 보안 SOC 영역에서 많이 연구되었으며 데이터 파이프라인 전용 벤치마크는 조직마다 다르게 정의한다. 내부 SLA 기준을 먼저 설정하고 그것과 비교하는 방식을 권장.

### 5-3. 지표 측정 방법 예시

- **MTTD**: 이상 발생 타임스탬프(파이프라인 로그)와 알림 발송 타임스탬프 차이를 집계.
- **MTTR**: 인시던트 오픈 시각과 클로즈 시각 차이. 인시던트 관리 도구(예: PagerDuty, OpsGenie) 자동 집계.
- **오탐률**: (알림 전체 건수 - 실제 이상으로 확인된 건수) / 알림 전체 건수 × 100.
- **커버리지**: 모니터링 등록된 파이프라인 수 / 전체 운영 파이프라인 수 × 100.

---

## 6. 제조 현업 적용 시나리오

### 설비 텔레메트리 수집 파이프라인이 멈추는 경우
1. 용접 설비의 전류·전압 센서 데이터가 1분 주기로 데이터 레이크에 적재되어야 함.
2. **Freshness 축 알림**: 15분째 신규 레코드 없음 → SEV2 알림.
3. DataOps 팀 확인: 네트워크 어댑터 재시작 후 복구.
4. **Volume 축 알림**: 복구 후 30분간 누락분 재적재 → 갑작스런 volume 급증을 정상으로 분류(억제 윈도우 적용).

### 단위가 바뀌는 경우
1. PLC 펌웨어 업그레이드 후 압력 단위가 kPa → MPa로 변경됨.
2. **Schema 축**: 컬럼명 변경 감지 → 알림.
3. **Distribution 축**: 값 범위가 1,000배 변동 → 이상 탐지.
4. Lineage로 이 데이터를 쓰는 AI 모델 확인 → 해당 AI 서비스 팀에 즉시 통보.
5. 원인: 데이터 드리프트(스키마·단위 변경). 모델 문제 아님.

---

## 출처 URL 목록

1. **Monte Carlo — 5 Pillars of Data Observability (정본)**  
   https://montecarlo.ai/blog-introducing-the-5-pillars-of-data-observability/

2. **Monte Carlo — What Is Data Observability? (2026)**  
   https://montecarlo.ai/blog-what-is-data-observability/

3. **Monte Carlo — AI Data Drift**  
   https://montecarlo.ai/blog-ai-data-drift/

4. **Acceldata — Data Observability with Automated Anomaly Detection**  
   https://www.acceldata.io/blog/data-observability-with-automated-anomaly-detection-explained

5. **Edge Delta — Anomaly Detection in Observability (2025)**  
   https://edgedelta.com/company/knowledge-center/anomaly-detection

6. **DevHelm — Incident Severity Levels: Sev1, Sev2, Sev3, Sev4**  
   https://devhelm.io/blog/incident-severity-levels

7. **Pantomath — Data Observability Guide**  
   https://www.pantomath.com/guide-data-observability

8. **Galileo AI — ML Observability Framework**  
   https://galileo.ai/blog/ml-observability-framework

9. **Evidently AI — Model Monitoring for ML in Production**  
   https://www.evidentlyai.com/ml-in-production/model-monitoring

10. **dqlabs — Data Observability Explained (5 Pillars & AI Shift)**  
    https://www.dqlabs.ai/blog/data-observability-explained/

11. **Estuary — Data Observability in the Modern Data Stack (Part 1)**  
    https://estuary.dev/blog/data-observability-modern-data-stack-part-1/

12. **GrayCella America — Data Observability in 2026**  
    https://graycellamerica.com/data-observability-in-2026-from-reactive-monitoring-to-autonomous-trust/

13. **RisingWave — 5 Crucial Pillars of Data Observability**  
    https://risingwave.com/blog/5-crucial-pillars-of-data-observability-for-modern-data-management/

14. **TechTarget — 5 Pillars of Data Observability Bolster Data Pipeline**  
    https://www.techtarget.com/searchdatamanagement/tip/Pillars-of-data-observability-bolster-data-pipeline

15. **First Eigen — Data Observability: Everything You Need to Know**  
    https://firsteigen.com/blog/data-observability-everything-you-need-to-know/

16. **Atlan — Top 14 Data Observability Tools in 2026**  
    https://atlan.com/know/data-observability-tools/

17. **SYNQ — 10 Best Data Observability Tools in 2025**  
    https://www.synq.io/blog/the-10-best-data-observability-tools-in-2025

18. **Superwise — Data and Model Drift: A Strategic Business Risk**  
    https://superwise.ai/blog/data-model-drift-a-strategic-business-risk-2/

19. **Fiddler — ML Observability Documentation**  
    https://docs.fiddler.ai/reference/glossary/ml-observability

20. **OvalEdge — Data Observability Tools for Pipeline Health**  
    https://www.ovaledge.com/blog/data-observability-tools/
