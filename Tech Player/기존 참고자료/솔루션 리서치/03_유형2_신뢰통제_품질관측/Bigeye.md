# Bigeye — Lineage 기반 데이터 Observability & AI Trust 플랫폼

> 작성일: 2026-06-10 | 카테고리: 유형② 신뢰 통제

---

## 기본 정보

| 항목 | 내용 |
|---|---|
| 개발사 | Toro Data Labs (샌프란시스코, 2019년 설립) |
| 라이선스 | 상용 SaaS |
| 배포 형태 | SaaS / 프라이빗 클라우드 배포 |
| 최신 동향 | 2025~2026: "AI Trust Platform"으로 포지셔닝 전환, PII/PHI/PCI 자동 탐지 강화, Lineage 기반 영향 분석 고도화, AWS/Azure Marketplace 등재 |

---

## 한 줄 포지셔닝

**"70가지 이상 품질 메트릭과 Lineage 기반 RCA를 결합해 AI 프로젝트 데이터 신뢰를 보장하는 Observability 플랫폼"**

---

## 주요 기능

### 1. 자동화 데이터 품질 모니터링
- 70개 이상의 사전 빌드 데이터 품질 모니터링 메트릭 라이브러리
- ML 기반 이상탐지 + 커스텀 룰 병행 운영
- UI 또는 YAML 기반 프로그래밍 방식 설정 (두 방법 모두 지원)
- 분 단위 신선도(Freshness) 모니터링부터 복잡한 분포 비교까지

### 2. Lineage 기반 RCA & 영향 분석
- 필드 수준(Field-level) 데이터 Lineage 자동 수집
- 이상 탐지 시 Lineage를 따라 상위(upstream) 원인 자동 추적
- 하위(downstream) 영향 자산 즉시 식별 — 영향 범위 분석 자동화

### 3. 민감 데이터 자동 탐지
- PII(개인정보), PHI(건강정보), PCI(결제정보) 등 민감 데이터 자동 스캔
- 규제 리스크 감소 및 AI 프로젝트 데이터 안전성 사전 검증
- 숨겨진 민감 데이터 탐지로 데이터 거버넌스 강화

### 4. AI Trust Platform (2025 리포지셔닝)
- AI 이니셔티브 규모화를 위한 데이터 품질·리스크·정책 통합 플랫폼
- AI 학습 데이터의 품질·민감도·정책 준수 여부 통합 관리
- 데이터 엔지니어·분석가·데이터 과학자·이해관계자 협업 환경

### 5. YAML 기반 구성 자동화
- UI 없이 YAML로 모니터링 설정 → 코드화·버전관리 가능
- 대규모 테이블 집합에 대한 일괄 설정 지원

---

## AI-Ready Data 주제 매핑

| 주제 코드 | 주제명 | 지원 수준 |
|---|---|---|
| C-1 | 데이터 Observability | ○ 핵심 기능 |
| C-2 | 품질관리 | ○ 70+ 메트릭 |
| C-3 | 데이터 Lineage | ○ 필드 수준 Lineage |

---

## 강점

- **Lineage + Observability 통합**: 탐지→Lineage→RCA를 하나의 플로우로 연결 — 조사 시간 최소화
- **민감 데이터 자동 탐지**: PII/PHI/PCI 스캔이 품질 모니터링과 통합 — 규제 환경에 강점
- **AI Trust 포지셔닝**: AI 프로젝트 데이터 신뢰 보장에 특화된 명확한 가치 제안
- **유연한 설정**: UI와 YAML 모두 지원 — 다양한 팀 역량에 적응
- **Marketplace 접근성**: AWS, Azure, Microsoft Marketplace 등재

---

## 약점 및 주의점

- **비투명 가격**: 완전 커스텀 견적, 공개 가격표 없음
- **데이터 계약 약함**: Soda 수준의 Contract 엔진 없음
- **AI 에이전트 미흡**: Monte Carlo·Anomalo 수준의 자율 에이전트 기능 부재
- **중소규모 한계**: 대규모 다계열사 환경에서의 확장성 레퍼런스 제한적
- **오픈소스 없음**: 완전 상용, 커뮤니티 OSS 생태계 없음

---

## 가격 모델

- **완전 커스텀 견적**: hello@bigeye.com으로 문의
- AWS Marketplace에서 프라이빗 오퍼 요청 가능
- 조직 규모·소스 수·기능 레벨에 따라 차등

---

## 연동 생태계

| 카테고리 | 연동 도구 |
|---|---|
| 데이터 웨어하우스 | Snowflake, BigQuery, Redshift, Databricks |
| 파이프라인 | Airflow, dbt |
| 마켓플레이스 | AWS Marketplace, Azure Marketplace, Microsoft Marketplace |
| 알림 | Slack, PagerDuty, Jira |
| API | REST API, YAML 구성 |
| 보안 | 민감 데이터 스캐너 (PII/PHI/PCI) |

---

## 출처

- https://www.bigeye.com/
- https://www.g2.com/products/bigeye/reviews
- https://www.gartner.com/reviews/market/data-observability-tools/vendor/bigeye/product/bigeye
- https://aws.amazon.com/marketplace/pp/prodview-w4yis4dzpm4u2
- https://www.trustradius.com/products/bigeye-data-observability-platform/pricing
- https://marketplace.microsoft.com/en-us/product/saas/torodatalabsinc1699291779936.bigeye
