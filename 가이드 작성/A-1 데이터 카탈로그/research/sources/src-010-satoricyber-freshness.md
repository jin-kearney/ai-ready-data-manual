# src-010 — Satori Cyber / Elementary Data: Stale Metadata & Freshness

**URL (Satori):** https://blog.satoricyber.com/how-stale-metadata-causes-data-projects-to-fail/  
**URL (Elementary):** https://www.elementary-data.com/post/data-freshness-best-practices-and-key-metrics-to-measure-success  
**제목:** How Stale Metadata Causes Data Projects To Fail | Data Freshness Best Practices  
**접속일:** 2026-06-18

---

## 오래된 메타데이터가 프로젝트를 망치는 방법

- 오래된 오너 필드·오래된 비즈니스 설명이 있는 자산은 사람들을 적극적으로 오도함
- 데이터 소비자는 노후화된 문서에 의존할 수 있으며, 분석가들이 데이터를 수동으로 검증하거나 작업을 중복 수행하는 데 시간을 낭비
- **오래된 또는 불완전한 메타데이터 = 데이터 불신의 주요 원인**

## 자동화 메타데이터 관리가 최신성 유지에 기여

자동화된 메타데이터 관리는 다음을 지속적으로 수집하여 최신 상태를 유지:
- 갱신 일정(refresh schedules)
- 스키마 변경
- 쿼리 패턴

스키마 변경, 품질 이슈 발생, 신규 원천 등장 시 카탈로그가 리니지·품질 점수·거버넌스 메타데이터를 실시간 자동 업데이트.

## 데이터 신선도(Data Freshness) 모니터링

**운영 메타데이터에 포함되어야 할 항목:**
- 갱신 빈도
- 최종 업데이트 타임스탬프
- 사용 패턴·쿼리 통계
- 성능 지표

이 항목들로 사용자가 데이터의 신선도·신뢰성을 판단할 수 있음.

**기계학습 기반 신선도 탐지 (Elementary):**
- 테이블 커밋 이력을 분석하여 테이블별 모델 구축
- 다음 커밋 시점 예측
- ML 모델로 신선도 이상 탐지 → 테이블의 업데이트 빈도를 학습하고 현재 신선한지 지속 확인

## data.world 메타데이터 신선도 검토 자동화

**URL:** https://docs.data.world/en/160043-metadata-freshness-review-automation.html

- 데이터 스튜어드가 정기적 메타데이터 검토 일정 설정 가능
- **Refreshed On 필드** 모니터링: 리소스가 마지막으로 갱신된 시점
- **shelf life(유효 기간)** 설정: 갱신 유효 기간(일 단위)
- **Refresh Due 필드**: 리소스가 더 이상 신선하지 않아 주의가 필요한지 표시
- 임계값 초과 시 스튜어드에게 자동 알림
