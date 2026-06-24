# D-1 Physical 데이터 — 리서치 자료: 표준·연결·정제
> 작성일: 2026-06-24 | 작성자: 리서치 에이전트 | 후속 가이드 작성용 내부 자료

---

## 목차
1. [산업용 통신 프로토콜 / 표준](#1-산업용-통신-프로토콜--표준)
2. [자산·설비 식별 / 데이터 구조 표준 (ISA-95)](#2-자산설비-식별--데이터-구조-표준-isa-95)
3. [시간 동기화 표준 (NTP / PTP)](#3-시간-동기화-표준-ntp--ptp)
4. [단위·태그 표준화](#4-단위태그-표준화)
5. [물리 데이터 기초 정제 개념](#5-물리-데이터-기초-정제-개념)
6. [실시간 처리 vs 배치 처리 구분](#6-실시간-처리-vs-배치-처리-구분)
7. [출처 목록](#출처-목록)

---

## 1. 산업용 통신 프로토콜 / 표준

설비 → 상위 시스템(MES·ERP·AI)으로 데이터를 전달하는 연결 계층. 세 프로토콜이 현장에서 계층별로 역할이 나뉜다.

### 1-1. OPC UA (OPC Unified Architecture)

- **공식 기관**: [OPC Foundation](https://opcfoundation.org/)
- **사양서(Specification) 공식 URL**: [https://opcfoundation.org/developer-tools/documents/?type=Specification](https://opcfoundation.org/developer-tools/documents/?type=Specification)
- **레퍼런스 사이트**: [https://reference.opcfoundation.org](https://reference.opcfoundation.org)
- IEC 62541로 표준화된 플랫폼 독립 산업 통신 규격. 2008년 1판 발표, 현재 1.05 계열.
- 한 줄 설명: **설비와 상위 시스템이 맥락·보안까지 담아 데이터를 주고받는 국제 표준 방식.**
- 핵심 특징:
  - 클라이언트-서버 + 발행-구독(Pub/Sub) 두 통신 방식 모두 지원
  - 150개 이상의 산업별 동반 사양(Companion Specification) — 공정·에너지·로봇 등 분야별 데이터 모델 표준
  - X.509 인증서 기반 보안·암호화·감사 추적 내장
  - 계층적 주소 공간(Address Space): 설비 → 라인 → 공장까지 계층 구조로 태그 배치
- 언제 쓰는가:
  - PLC/DCS → SCADA/MES → ERP 수직 통신 (설비 내부 M2M 포함)
  - 데이터에 의미(컨텍스트·단위·계층 위치)까지 실어야 할 때
  - 보안·인증이 엄격히 요구되는 환경 (발전, 반도체, 화학)
- 제조 현장 예시: 두산에너빌리티 가스터빈 PLC가 OPC UA 서버로 구동, MES가 클라이언트로 터빈 속도·진동·온도를 구독 → AI 예지보전 입력

### 1-2. MQTT + Sparkplug B

- **공식 기관**: [Eclipse Foundation — Sparkplug Working Group](https://sparkplug.eclipse.org/)
- **사양서 공식 URL**: [https://sparkplug.eclipse.org/specification/](https://sparkplug.eclipse.org/specification/)
- **PDF 직접 다운로드 (v3.0)**: [https://sparkplug.eclipse.org/specification/version/3.0/documents/sparkplug-specification-3.0.0.pdf](https://sparkplug.eclipse.org/specification/version/3.0/documents/sparkplug-specification-3.0.0.pdf)
- MQTT: 경량 발행-구독 메시징 프로토콜. 불안정한 네트워크·저사양 기기에 적합.
- Sparkplug B → v3.0(2022년 11월 출시): MQTT만으로는 부족한 세 가지를 추가
  1. **표준화된 토픽 네임스페이스** — spBv1.0/그룹ID/노드ID/디바이스ID 체계
  2. **강형식 Protobuf 페이로드** — 데이터 타입·단위 내장
  3. **디바이스 생애주기 관리** — Birth/Death 메시지로 설비 온·오프라인 추적
- 한 줄 설명: **센서·기기가 네트워크를 통해 가볍고 표준화된 방식으로 데이터를 내보내는 IIoT 메시징 규격.**
- 언제 쓰는가:
  - 에지 게이트웨이 → 클라우드/브로커로 데이터를 올릴 때
  - 다수의 저전력·저사양 센서·기기가 분산된 환경
  - SCADA/HMI의 실시간 데이터 시각화용 스트리밍
- 제조 현장 예시: 두산밥캣 공장 에지 게이트웨이가 각 용접 셀의 전류·전압을 Sparkplug B 포맷으로 MQTT 브로커에 발행 → 클라우드 AI가 구독해 용접 불량 예측

### 1-3. Modbus

- **공식 기관**: [Modbus Organization](https://modbus.org/)
- **사양서 위치**: modbus.org → Resources → Specifications (URL 직접 접속 시 403 — 사이트 내 탐색 필요)
- 1979년 Modicon(現 Schneider Electric)이 개발, 2004년 공개 표준으로 이전.
- 변종: Modbus RTU(직렬), Modbus TCP/IP(이더넷), Modbus ASCII. 현행 사양 버전 1.1b3.
- 한 줄 설명: **40년 이상 산업 현장에서 쓰여온 설비-컨트롤러 간 가장 단순한 데이터 교환 방식.**
- 언제 쓰는가:
  - 레거시 PLC·온도 조절기·전력계 등 단순 필드 기기 연결
  - OPC UA/MQTT를 구동할 컴퓨팅 자원이 없는 기기에서 데이터를 읽어낼 때
  - 기존 설비를 현대 네트워크에 신속 편입(레거시 통합)
- 주의: 보안(암호화·인증) 기능 없음. 현대 환경에서는 게이트웨이를 통해 OPC UA/MQTT로 변환해 상위 시스템에 전달하는 방식이 일반적.
- 제조 현장 예시: 두산산업차량 창고 충전기 컨트롤러(Modbus RTU) → IoT 게이트웨이가 Modbus 폴링 → OPC UA로 변환 → MES 적재

### 1-4. 프로토콜 계층별 역할 요약

| 계층 | 프로토콜 | 역할 |
|------|----------|------|
| 필드 기기 ↔ PLC | Modbus | 단순 읽기/쓰기, 레거시 기기 |
| PLC/DCS ↔ SCADA/MES | OPC UA | 의미 있는 구조화 데이터, 보안 |
| 에지 ↔ 클라우드/브로커 | MQTT + Sparkplug B | 경량·실시간 스트리밍 |

---

## 2. 자산·설비 식별 / 데이터 구조 표준 (ISA-95)

### 2-1. ISA-95 표준 개요

- **공식 기관**: [ISA (International Society of Automation)](https://www.isa.org/)
- **공식 URL**: [https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard](https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard)
- 국제 표준명: ANSI/ISA-95 = IEC 62264. 총 8개 파트.
  - Part 1: 모델·용어 / Part 2: 개체·속성 / Part 3: 제조 운영 활동 모델 / 이하 통합·트랜잭션·메시징·별칭·정보교환 프로파일
- 한 줄 설명: **공장의 설비·공정·데이터가 계층적으로 어디에 속하는지 정의해 IT와 OT를 연결하는 국제 통합 표준.**

### 2-2. 5계층 설비 계층 모델

```
기업(Enterprise) — 전사
  └ 사이트(Site) — 공장/사업장
      └ 영역(Area) — 공정 구역
          └ 작업 센터(Work Center) — 라인/셀
              └ 작업 단위(Work Unit) — 개별 설비/기기
                  └ Level 0: 실제 물리 공정 (센서·밸브·액추에이터)
```

- Level 0: 물리 공정 (실제 기계·센서)
- Level 1: 감지·제어 (스마트 센서·밸브)
- Level 2: 감시·제어 (PLC·DCS)
- Level 3: 제조 운영 관리 (MES·SCADA)
- Level 4: 사업 계획·물류 (ERP)

### 2-3. 설비 ID / 태그 명명의 필요성

- ISA-95 Part 6: 전역 네임스페이스(Global Namespace) 정의 — 로컬 태그명을 전역 표준명으로 변환하는 명명 규칙
- ISA 5.1 계측 태그 체계: `영역번호 + 기능 문자 + 루프 번호` 조합으로 설비 내 유일 식별
  - 예: `T-101-TI-001` = 구역 T, 라인 101, 온도계기(TI), 001번째
- **명명 일관성이 없으면 발생하는 문제:**
  - 같은 설비에서 나온 데이터가 시스템마다 다른 이름 → 조인 불가
  - AI 모델이 같은 센서를 두 개의 다른 신호로 학습
  - 설비 이전·교체 시 태그 추적 불가
- 현장 적용: 두산에너빌리티 계열 발전 설비라면 `E-SEO-GAS01-PLC01-T001` 처럼 사이트코드-공정코드-설비코드-태그번호 체계를 사전 정의해야 AI 적재 시 자동 매핑 가능.

---

## 3. 시간 동기화 표준 (NTP / PTP)

### 3-1. NTP vs PTP 비교

| 항목 | NTP | IEEE 1588 PTP |
|------|-----|----------------|
| 공식 표준 | RFC 5905 ([https://www.ntp.org](https://www.ntp.org)) | IEEE 1588-2008 (PTPv2) |
| 정밀도 | 밀리초(ms) 수준 | 나노초(ns) ~ 수백 나노초 수준 |
| 동작 방식 | 인터넷 전반 범용 시간 동기 | 전용 이더넷 LAN에서 하드웨어 타임스탬프 |
- **PTP 공식 참고**: [https://www.ntp.org/reflib/ptp/](https://www.ntp.org/reflib/ptp/)
- PTP의 핵심 구조: **Grandmaster 클락** → 모든 하위 기기에 기준 시각 배포. 왕복 지연 계산으로 전파·처리 지연 보정.

### 3-2. 왜 시각 동기화가 시계열 분석의 전제인가

- 진동 센서(1kHz 샘플링)와 온도 센서(1분 간격)를 동시에 분석하려면 공통 시간 기준이 필수
- 시각이 설비마다 수십 ms 어긋나면 **이상 발생 순서(선행·후행)를 뒤바꾸는 분석 오류** 발생
- 발전터빈 예시: 진동 급증(설비 A 시각 기준) → 압력 강하(설비 B 시각 기준) 순서가 맞아야 원인 특정 가능 — 시각이 어긋나면 인과 관계 역전

### 3-3. 타임스탬프 기준 문제 (수집 시각 vs 측정 시각)

- **측정 시각(Event Time)**: 센서가 실제로 물리량을 측정한 시점
- **수집 시각(Ingestion Time)**: 상위 시스템(SCADA·Historian)이 값을 받아 기록한 시점
- 두 시각 차이가 수십 ms ~ 수 초 발생 가능 (네트워크 지연·폴링 주기·버퍼)
- AI 입력 전에 반드시 어느 시각 기준인지 명시하고 통일해야 함.

### 3-4. 타임존·UTC 기록 원칙

- 여러 사이트(국내 공장 + 해외 법인)의 데이터를 합칠 때: **UTC로 저장, 표시는 로컬**
- 일광절약시간(Daylight Saving Time) 경계에서 로컬 시각만 저장하면 중복 타임스탬프 발생 → UTC + 오프셋으로 명시해야 유일성 보장

---

## 4. 단위·태그 표준화

### 4-1. 엔지니어링 단위 혼재 문제

- 제조 현장에서 자주 발생하는 혼재:
  - 온도: ℃(섭씨) / °F(화씨) 혼용 → 같은 공정 데이터가 두 단위로 적재
  - 압력: bar / MPa / psi 혼용 → 설비 세대·원산지마다 다름
  - 길이: mm / inch 혼용 → 수입 설비(두산밥캣 북미 기기)와 국내 기기 혼재
  - 유량: L/min / m³/h 혼용
- AI 모델 학습 전에 **단일 단위 체계로 변환하지 않으면** 모델이 단위 차이를 물리적 변화로 오인

### 4-2. 단위 표준 참고

- **ISO/IEC 80000** 시리즈: 국제 표준 물리량·단위 체계 ([https://www.iso.org/standard/76921.html](https://www.iso.org/standard/76921.html) — ISO 80000-1:2022)
  - Part 3: 공간·시간 / Part 4: 역학 / Part 5: 열역학 / Part 6: 전자기
  - SI 단위계(국제단위계)의 기술 분야별 확장 정의
- 현장 적용: SI 단위를 정본 단위로 지정하고, 비SI 단위(bar·inch·psi)로 들어오는 값은 적재 파이프라인에서 자동 변환 처리

### 4-3. 태그 명명 일관성 원칙

- 동일 물리량이라도 설비·PLC·SCADA·Historian에서 태그명이 달라지는 현상이 빈번
  - PLC: `T_101_01` / SCADA: `TEMP-LINE1-MACHINE01` / Historian: `SiteA.TempSensor.Loop01`
- **태그 명명 표준 수립 필요 요소**:
  1. 설비 위치 코드 (사이트·공정·라인)
  2. 물리량 종류 (온도·압력·진동·전류)
  3. 측정 위치 (입구·출구·중간)
  4. 단위 (기록 단위 명시)
- ISA 5.1 계측 기기 식별 및 기호 표준이 계측 태그 문자 체계의 기준으로 많이 사용됨

---

## 5. 물리 데이터 기초 정제 개념

AI 입력 전 1차 정리 단계. 최종 품질 판정(이 배치를 써도 되는가)은 C-2 데이터 품질 영역이지만, 센서 신호를 다룰 수 있는 형태로 만드는 기초 정제는 D-1 범위.

### 5-1. 센서 노이즈 / 스무딩

- **현상**: 측정 환경의 전기적 간섭·기계적 진동으로 순간적인 무작위 변동이 신호에 섞임
- **대표 정제 기법**:
  - 이동 평균(Moving Average): 창(window) 내 값의 평균으로 노이즈 희석
  - 지수 평활(Exponential Smoothing): 최근 값에 가중치를 더 줘 추세 보존하며 노이즈 감소
- **제조 예시**: CCL 라미네이터 압력 센서가 전기 노이즈로 1분에 수십 회 ±0.2bar 진동 → 이동 평균 적용 후 실제 압력 추세만 추출

### 5-2. 결측(Gap) · 신호 끊김(Dropout) 처리

- **현상**: 통신 장애·센서 교체·설비 정지 등으로 시계열에 구멍이 생김
- **대표 처리 방식**:
  - 선형 보간(Linear Interpolation): 전후 값을 직선으로 연결해 채움. 변화가 완만한 신호에 적합.
  - 전진 채움(Forward Fill): 직전 유효 값을 그대로 복사. 값이 거의 변하지 않는 설비 상태 코드에 적합.
  - 결측 표시(Flag): 보간이 불확실하면 채우지 않고 결측 플래그 컬럼을 별도로 추가
- **제조 예시**: 건설기계 굴삭기 엔진 RPM 센서가 30분간 통신 장애 → 장애 전후 정상 구간만 학습, 결측 구간은 플래그 처리
- 주의: 장시간 결측을 기계적으로 보간하면 AI가 허구 데이터로 학습 — 결측 구간 길이 기준 수립 필요

### 5-3. 이상값 / 스파이크(Spike) 탐지

- **현상**: 센서 오작동·케이블 노이즈·기계적 충격으로 순간적으로 비정상적인 값이 찍힘
- 스파이크: 주변 값 대비 극단적으로 크거나 작은 단일 포인트 → 센서 오류일 가능성 높음
- 스파이크 ≠ 실제 이상: 실제 공정 이상은 여러 타임스텝에 걸쳐 지속됨
- **대표 탐지 기법**:
  - IQR(사분위 범위) 기반 임계치: 중앙값에서 일정 배수 이상 벗어나면 스파이크로 표시
  - 표준편차 기반 Z-score: 평균에서 3σ 이상 이탈 시 이상치 판정
- **제조 예시**: 발전 터빈 베어링 온도 센서가 1초 만에 300℃ 급등 후 정상 복귀 → 센서 오류 스파이크, 보간으로 대체

### 5-4. 리샘플링 · 정렬(Resampling / Alignment)

- **현상**: 여러 센서가 서로 다른 주기(진동 1kHz · 온도 10Hz · 공정 조건 1Hz)로 수집됨. AI 모델은 동일 시간 간격의 정렬된 데이터를 요구.
- **리샘플링 방향**:
  - 업샘플링: 낮은 주파수 신호를 높은 주파수로 늘림 (보간 필요)
  - 다운샘플링: 높은 주파수 신호를 낮은 주파수로 줄임 (집계·평균)
- **정렬**: 이종 신호를 공통 타임스텝(예: 1초 격자)에 매핑
- **제조 예시**: 반도체 테스트 장비의 RF 파워(100Hz)·챔버 온도(1Hz)를 동시에 AI에 입력하려면 온도를 100Hz로 업샘플하거나 RF 파워를 1Hz로 다운샘플해 정렬

### 5-5. Historian의 Deadband / 압축이 만드는 불균일 간격 문제

- **Historian(히스토리안)**: 공정 데이터 시계열을 장기 저장하는 전용 소프트웨어 (OSIsoft PI, AVEVA, Ignition 등)
- **Deadband(데드밴드) / 예외 기반 보고(Exception-based Reporting)**:
  - 값이 직전 저장값 대비 설정 임계치 이상 변할 때만 기록 (예: 0.5bar 이상 변할 때만 저장)
  - 목적: 저장 공간 절약. 전압 신호가 임계치 없을 때 8,640개/일 → 데드밴드 적용 시 3개/일로 줄어드는 사례도 있음
- **Swinging Door 압축**: 보간으로 재현 가능한 중간 포인트를 삭제하는 알고리즘. 오차 범위 내에서 최소한의 포인트만 저장.
- **AI 입력 시 문제**: 압축·데드밴드 처리된 데이터는 **타임스탬프 간격이 불규칙** → ML 모델(특히 LSTM 등 시계열 모델)이 등간격 가정을 위반
- **해결 방법**: Historian에서 데이터를 꺼낼 때 **균일 간격 재보간(interpolated retrieval)**으로 요청하거나, AI 파이프라인 전처리 단계에서 등간격 리샘플링

### 5-6. 중복 · 시간 역전(Duplicate / Time Inversion)

- **중복**: 네트워크 재전송 등으로 동일 타임스탬프에 두 값이 기록됨
- **시간 역전**: 클락 드리프트·프로토콜 버퍼링으로 나중에 측정된 값이 더 이른 타임스탬프를 가짐
- 두 경우 모두 시계열 정렬 전에 제거하지 않으면 AI 모델 학습 오류 유발
- **처리**: 중복 제거(deduplication) → 타임스탬프 오름차순 정렬 확인 → 역전 포인트 플래그 처리

---

## 6. 실시간 처리 vs 배치 처리 구분

### 6-1. 핵심 구분 기준

| 기준 | 실시간(스트리밍) 처리 | 배치 처리 |
|------|----------------------|-----------|
| 지연 허용 | 밀리초(ms) ~ 수백 ms | 분 ~ 시간 |
| 대표 사용 | 설비 이상·안전·품질 즉시 대응 | 분석·리포팅·모델 재학습 |
| 데이터 준비 특성 | 경량·실시간 정제, 에지 처리 | 대용량 이력, 클라우드/온프레미스 데이터레이크 |
| 예시 | 프레스 스트로크 불량 즉시 배출 | 주간 공정 수율 분석, 모델 재훈련 |

### 6-2. 실시간 처리가 필요한 경우 (데이터 준비 함의)

- **안전 임계**: 설비 과열·과부하 → 즉각 정지 신호. 지연 200~800ms도 허용 불가.
- **품질 즉시 배출**: 600 스트로크/분 프레스에서 불량품 판정 → 5ms 내 AI 판단 필요.
- **데이터 준비 관점**: 에지에서 최소 정제(스파이크 제거·단위 변환)만 하고 즉시 추론. 과도한 전처리는 지연 초래.
- 두산 예시: 두산테스나 반도체 테스트 장비에서 실시간 불량 신호 탐지 — 테스트 완료 후 수 ms 내 판정 필요

### 6-3. 배치 처리가 적합한 경우 (데이터 준비 함의)

- 수개월치 이력 기반 예지보전 모델 학습
- 일간·주간·월간 생산성·품질 리포트
- 데이터 품질 점검·이상 패턴 소급 분석
- **데이터 준비 관점**: 철저한 정제(결측 보간·단위 통일·리샘플링·중복 제거) 후 Historian/데이터레이크에서 일괄 추출. 시간이 허용되므로 정제 품질을 높일 수 있음.

### 6-4. 권장 하이브리드 아키텍처

```
설비 센서
  ↓ (Modbus/OPC UA)
에지 게이트웨이
  ├─ 실시간 경로: 경량 정제 → 즉시 AI 추론 → 경보·제어
  └─ 이력 경로:  Historian 적재 → 배치 정제 → 데이터레이크 → 모델 학습/분석
```

- 실시간 경로: 즉각 판단이 필요한 안전·품질 신호
- 이력 경로: 예지보전·수율 분석·AI 모델 재학습용 데이터 준비

---

## 출처 목록

| # | 출처명 | URL | 접속일 | 성격 |
|---|--------|-----|--------|------|
| 1 | OPC Foundation — OPC UA 공식 소개 | https://opcfoundation.org/about/opc-technologies/opc-ua/ | 2026-06-24 | 공식 표준기구 |
| 2 | OPC Foundation — Specifications (사양서 목록) | https://opcfoundation.org/developer-tools/documents/?type=Specification | 2026-06-24 | 공식 표준기구 (사양서) |
| 3 | OPC Foundation — Reference Site | https://reference.opcfoundation.org | 2026-06-24 | 공식 표준기구 (레퍼런스) |
| 4 | Eclipse Foundation — Sparkplug Working Group 공식 | https://sparkplug.eclipse.org/ | 2026-06-24 | 공식 표준기구 |
| 5 | Eclipse Foundation — Sparkplug Specification v3.0 | https://sparkplug.eclipse.org/specification/ | 2026-06-24 | 공식 사양서 |
| 6 | Sparkplug 3.0 PDF 직접 다운로드 | https://sparkplug.eclipse.org/specification/version/3.0/documents/sparkplug-specification-3.0.0.pdf | 2026-06-24 | 공식 사양서 PDF |
| 7 | Modbus Organization — 공식 사이트 | https://modbus.org/ | 2026-06-24 | 공식 표준기구 |
| 8 | ISA — ISA-95 표준 공식 | https://www.isa.org/standards-and-publications/isa-standards/isa-95-standard | 2026-06-24 | 공식 표준기구 |
| 9 | NTP.org — IEEE 1588 PTP 레퍼런스 | https://www.ntp.org/reflib/ptp/ | 2026-06-24 | 공식 기술 참고문서 |
| 10 | ISO — ISO 80000-1:2022 (물리량·단위) | https://www.iso.org/standard/76921.html | 2026-06-24 | 공식 표준기구 |
| 11 | OPC UA Wikipedia (기술 개요) | https://en.wikipedia.org/wiki/OPC_Unified_Architecture | 2026-06-24 | 참고 백과 |
| 12 | AVEVA/OSIsoft — Deadband·압축 영향 발표자료 | https://cdn.osisoft.com/osi/presentations/2023-AVEVA-San-Francisco/UC23NA-3PGK04-AVEVA_Bregenzer_Brent-Exception-Compression-and-their-Impacts-On-PI-System-Performance.pdf | 2026-06-24 | 산업 컨퍼런스 발표 |
| 13 | scadaprotocols.com — OPC UA vs MQTT vs Modbus 비교 | https://scadaprotocols.com/opc-ua-vs-mqtt-vs-modbus/ | 2026-06-24 | 기술 해설 |
| 14 | Cirrus Link — IIoT 프로토콜 효율 비교 | https://cirrus-link.com/efficient-iiot-communications-a-comparison-of-mqtt-opc-ua-http-and-modbus/ | 2026-06-24 | 산업 기술 블로그 |
| 15 | EMQ — ISA-95 표준 해설 | https://www.emqx.com/en/blog/exploring-isa95-standards-in-manufacturing | 2026-06-24 | 기술 해설 |
| 16 | TigerData — SCADA 히스토리안 아키텍처 | https://www.tigerdata.com/learn/scada-data-management-at-scale-architecture-historians-and-the-modern-database | 2026-06-24 | 산업 기술 참고 |
| 17 | Springer — 예측 노이즈 보정 방법론 | https://journalofbigdata.springeropen.com/articles/10.1186/s40537-020-00367-w | 2026-06-24 | 학술 논문 |
| 18 | ScienceDirect — 시계열 전처리 서베이 | https://www.sciencedirect.com/science/article/pii/S2307187724000452 | 2026-06-24 | 학술 논문 |
| 19 | Confluence.io — 실시간 AI 스트림 처리 vs 배치 ETL | https://www.confluent.io/blog/real-time-ai-stream-processing/ | 2026-06-24 | 산업 기술 블로그 |
| 20 | Edge Computing Manufacturing (ARM Newsroom) | https://newsroom.arm.com/blog/ai-at-the-edge-manufacturing-quality | 2026-06-24 | 산업 기술 참고 |
| 21 | HPE — Precision Time Protocol 해설 | https://www.hpe.com/us/en/what-is/precision-time-protocol.html | 2026-06-24 | 기술 해설 |
| 22 | Wikipedia — Modbus | https://en.wikipedia.org/wiki/Modbus | 2026-06-24 | 참고 백과 |
