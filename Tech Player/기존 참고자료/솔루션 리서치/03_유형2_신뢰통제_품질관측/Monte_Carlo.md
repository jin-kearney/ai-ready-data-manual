# Monte Carlo — 데이터·AI Observability 플랫폼

> 작성일: 2026-06-10 | 카테고리: 유형② 신뢰 통제

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Monte Carlo Data (샌프란시스코, 2019년 설립) |
| 라이선스 | 상용 SaaS |
| 배포 형태 | 완전 관리형 SaaS (멀티클라우드) |
| 최신 동향 | 2025~2026: Agentic Observability 레이어 출시, AI 모델 출력·피처 스토어 모니터링 추가, $236M+ 펀딩(기업가치 $1.6B) |

---

## 한 줄 포지셔닝

**"ML 자동 이상탐지 + 컬럼 수준 Lineage + Agentic 인시던트 대응을 통합한 데이터·AI Observability 업계 1위"**

---

## 주요 기능

### 1. ML 기반 자동 이상탐지 (Anomaly Detection)
- 룰·임계값 설정 없이 데이터 패턴을 학습해 신선도(Freshness), 볼륨, 분포(Distribution), 스키마 변화를 자동 감지
- 데이터 소스별 시즌성·트렌드를 학습하여 노이즈 알림을 최소화

### 2. 컬럼 수준 데이터 Lineage
- 단방향/양방향 계보 UI로 테이블·컬럼 간 데이터 흐름 시각화
- 크로스 시스템 Lineage: 트랜잭셔널 DB, 분석 플랫폼, Kafka 토픽, 벡터 DB, BI 도구까지 커버
- 인시던트 발생 시 영향받는 하위 자산 즉시 식별

### 3. 자동 근본 원인 분석 (RCA)
- Lineage와 이상 탐지를 연결해 SQL 잡 오류·스키마 변경·업스트림 파이프라인 실패를 자동으로 연결
- 조사 시간 수 시간 → 수 분으로 단축

### 4. Agentic Observability (2025 신기능)
- First Responder Agent: 알림 수신 → 자동 조사 → 런북 기반 조치 실행
- 인간 의사결정을 대체하지 않고 탐지-해결 갭을 자율 보조
- AI 모델 출력 및 피처 스토어 모니터링으로 커버리지 확장

### 5. 50+ 사전 빌드 커넥터
- Snowflake, Redshift, BigQuery, Databricks, Looker, Power BI, dbt, Airflow, Fivetran 등
- 2025 전략: dbt, Airflow, Fivetran 심층 통합으로 엔드투엔드 파이프라인 관측 강화

### 6. AI 관측 (AI Observability)
- AWS Marketplace에 "Monte Carlo Data + AI Observability Platform"으로 등재
- LLM 파이프라인용 벡터 DB 모니터링, 피처 스토어 신선도 추적

---

## AI-Ready Data 주제 매핑

| 주제 코드 | 주제명 | 지원 수준 |
|---|---|---|
| C-1 | 데이터 Observability | ○ 핵심 기능 |
| C-2 | 품질관리 | ○ ML 자동탐지 |
| C-3 | 데이터 Lineage | ○ 컬럼 수준 |

---

## 강점

- **ML-first 철학**: 룰 작성 없이 즉시 이상탐지 시작 — 운영 부담 최소
- **업계 최다 배포**: Snowflake·Databricks 대규모 환경에서 검증된 레퍼런스 다수
- **통합 인시던트 워크플로우**: 탐지→Lineage→RCA→티켓팅(Jira·PagerDuty)까지 단일 플로우
- **AI 시대 확장성**: AI 모델 출력, 피처 스토어 등 AI 데이터 파이프라인 감시까지 커버

---

## 약점 및 주의점

- **비용 급등 위험**: 관측 볼륨·소스 수 증가 시 warehouse compute 비용 포함 급등 가능
- **룰 기반 테스트 약함**: SLA 명세·데이터 계약(Contract) 집행 기능은 Soda 대비 제한적
- **온프레미스 미지원**: 완전 SaaS 구조로 레거시 온프레미스 환경 적용 불가
- **투명 가격 부재**: 공개 가격표 없음, 개별 협상 필요

---

## 가격 모델

- **과금 기준**: 관측 데이터 볼륨 + 연결 소스 수 + 모니터링 수준
- **참고 범위**: 30~100 테이블 / 2~3 소스 기준 연간 $25,000~$50,000
- **대기업**: 복잡한 스택 기준 $100,000~$500,000+/년 보고됨
- **결제 옵션**: Pay-as-you-go 또는 약정 할인

---

## 연동 생태계

| 카테고리 | 연동 도구 |
|---|---|
| 데이터 웨어하우스 | Snowflake, BigQuery, Redshift, Databricks |
| 파이프라인 | dbt, Airflow, Fivetran, Glue |
| BI | Looker, Tableau, Power BI, Mode |
| 스트리밍 | Kafka |
| 벡터 DB | Pinecone, Weaviate 등 |
| 알림/티켓 | Slack, PagerDuty, Jira, OpsGenie |
| API | REST API, Python SDK |
| LLM/AI | 피처 스토어 모니터링, AI Observability 레이어 |

---

## 출처

- https://www.montecarlodata.com/
- https://www.montecarlodata.com/product/resolve/
- https://www.montecarlodata.com/platform/data-lineage-impact/
- https://aws.amazon.com/marketplace/pp/prodview-hikicsfohm3gg
- https://www.modern-datatools.com/tools/monte-carlo
- https://www.vendr.com/marketplace/monte-carlo
- https://www.siffletdata.com/blog/monte-carlo-data-review
