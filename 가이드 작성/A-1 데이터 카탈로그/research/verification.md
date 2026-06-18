# A-1 데이터 카탈로그 — 출처 검증 리포트

- **검증 일자:** 2026-06-18
- **검증자:** Claude Code (출처 검증 에이전트)
- **대상 파일:** `가이드 작성/A-1 데이터 카탈로그/A-1 데이터 카탈로그.md`
- **판정 기준:** OK / MISMATCH / BROKEN / 확인불가

---

## 1. 정량 주장 검증 (6개)

---

### [1] "데이터 전문가들은 프로젝트 시간의 약 20%를 데이터 찾기에 낭비"
- **본문 위치:** §2.1 Pain Point, footnote [src-KPI-005]
- **출처 URL:** https://atlan.com/modern-data-catalog/
- **판정:** ✅ OK
- **확인 내용:** 페이지에서 다음 인용 확인됨.
  > "data professionals waste 20% of their project time (one full day per week) simply trying to figure out what data to use" (출처: 2024–2025 Modern Data Survey)
- **비고:** 수치와 표현 모두 본문과 일치. 인용 출처가 Atlan 자체 서베이(Modern Data Survey)임을 참고자료 각주에 명시하면 신뢰도가 높아짐.

---

### [2] "조직이 평균 400개 이상의 서로 다른 데이터 소스를 사용"
- **본문 위치:** §2.1 Pain Point, footnote [src-KPI-004]
- **출처 URL:** https://www.decube.io/post/data-catalog-roi
- **판정:** ⚠️ MISMATCH
- **확인 내용:**
  - decube.io 페이지에 "400개 이상 데이터 소스" 수치 **없음**.
  - atlan.com/modern-data-catalog/ 페이지에도 해당 수치 **없음**.
  - decube.io에서 확인된 수치: "10,000+ 데이터 테이블" (지역 은행 사례), "60% 검색 시간 단축"
- **실제 상황:** "400개 이상 데이터 소스" 수치의 원출처가 특정되지 않음. 이 수치는 Stitch Data (2019), Fivetran, 또는 Gartner 보고서에서 자주 인용되지만, 기재된 두 URL 어디에도 이 수치가 없음.
- **권장 수정안:**
  - **옵션 A (삭제):** 출처가 불명확하므로 해당 수치 주장을 본문에서 삭제.
  - **옵션 B (수치 교체):** 실제 decube.io 페이지 내용을 반영해 "대규모 조직은 수천 개 이상의 데이터 테이블을 보유하나 전체를 아우르는 목록이 없는 경우가 많다"로 서술 방식 변경, footnote도 해당 내용 확인 가능한 URL로 교체.
  - **출처 각주 교체 대상:** [src-KPI-004]를 decube.io에서 실제 확인 가능한 수치(60% 검색 시간 단축)로 용도를 변경하거나 삭제.

---

### [3] "데이터 탐색 시간 60~65% 단축"
- **본문 위치:** §2.2 기대 효과, footnote [src-KPI-004], [src-KPI-005]
- **출처 URL:**
  - https://www.decube.io/post/data-catalog-roi
  - https://atlan.com/modern-data-catalog/
- **판정:** ⚠️ MISMATCH (부분)
- **확인 내용:**
  - **decube.io:** "60% 감소" 확인 (검색 시간 5h/주 → 2h/주). **수치 60%는 일치**, 표현은 "단축"이 아니라 ROI 계산 내 비용 절감 사례로 제시됨.
  - **atlan.com:** "automated discovery reduce initial cataloging time by 65%" — 이것은 "탐색(discovery) 시간" 단축이 아니라 **"초기 카탈로깅(cataloging) 시간"** 단축임. 맥락이 다름.
  - atlan.com의 다른 수치: "data discovery time from 4.2 hours to 12 minutes" (~95% 단축, UC Berkeley 출처)도 있으나, 본문의 "60~65%" 범위와 다름.
- **권장 수정안:**
  - "데이터 탐색 시간 60~65% 단축"을 두 수치를 혼합한 표현이므로, 각 수치를 출처별로 분리 표기하는 것이 정확함.
    - decube.io 인용 시: "데이터 검색 시간 **60% 단축** (주당 5시간→2시간)" [src-KPI-004]
    - atlan.com 인용 시: "자동 수집 도입 시 초기 카탈로깅 시간 **65% 단축**" [src-KPI-005]
  - 또는, 각 출처에서 실제 확인되는 수치만 사용해 "카탈로그 도입 조직에서 데이터 검색 시간 **60% 이상 단축** 사례가 보고된다"로 보수적으로 표현.

---

### [4] 커버리지 기준 "80% 이상 우수 / 60% 미만 즉시 조치"
- **본문 위치:** §10.1 성과 지표, footnote [src-KPI-003]
- **출처 URL:** https://kpidepot.com/kpi/data-catalog-coverage
- **판정:** ✅ OK
- **확인 내용:** 페이지 "Data Catalog Coverage Interpretation" 섹션에서 다음이 명시됨.
  > "80% and above – Strong data governance and accessibility"
  > "60%–79% – Moderate coverage; consider targeted improvements"
  > "Below 60% – Significant gaps; immediate action required"
- **비고:** 본문 표현("60~79% = 개선 필요"를 "60% 미만 = 즉시 조치"로 단순화)은 출처 취지와 일치. 수치 정확히 일치함.

---

### [5] "SAP 테이블 문서화 6주 → 약 15분"
- **본문 위치:** §10.2 고도화 로드맵 (3단계 예시), footnote [src-구축-005]
- **출처 URL:** https://www.collibra.com/products/data-catalog
- **판정:** 🔴 MISMATCH (출처 불일치)
- **확인 내용:**
  - Collibra 제품 페이지(https://www.collibra.com/products/data-catalog): "SAP 테이블 문서화 6주→15분" 수치 **전혀 없음**.
  - Collibra 블로그 대체 URL(https://www.collibra.com/blog/data-catalog-use-cases): **404 Not Found**.
  - Collibra AI 카탈로그 블로그(https://www.collibra.com/blog/ai-powered-data-catalog): **404 Not Found**.
  - 현재까지 이 수치를 담은 Collibra 공식 URL **미발견**.
- **실제 상황:** 이 수치는 Collibra 고객 사례(customer story) 또는 블로그 포스트에 있을 가능성이 있으나, 기재된 URL에는 없음. "6주→15분"은 업계에서 AI 메타데이터 자동생성 효과 설명 시 사용되는 수치로 여러 벤더에서 유사 표현이 등장하지만 원출처 특정 불가.
- **권장 수정안 (우선순위 순):**
  1. **출처 교체 시도:** Collibra Customer Stories 페이지(https://www.collibra.com/customers) 또는 Atlan/Alation 고객 사례에서 동일·유사 수치 확인 후 교체.
  2. **출처 불명 표기:** 확인되는 출처를 찾지 못한 경우, 수치 뒤에 각주 없애고 "업계 사례 보고 기준"으로만 서술하거나 수치 자체를 삭제.
  3. **대체 표현:** "AI 메타데이터 자동 생성 도입 시 수작업 대비 등록 시간을 수십 배 단축한 사례가 보고된다"로 수치 없이 서술 가능.
- **추가 확인 필요 URL 후보:**
  - https://www.collibra.com/customers (Collibra 고객 사례 인덱스)
  - https://atlan.com/data-catalog-automation/ (Atlan 자동화 사례)

---

### [6] "Level 1→3 달성에 통상 12~18개월"
- **본문 위치:** §10.2 고도화 로드맵 하단 "공통 원칙", footnote [src-KPI-007]
- **출처 URL:** https://atlan.com/know/gartner/data-governance-maturity-model/
- **판정:** ✅ OK
- **확인 내용:** 페이지 "Timeline and resource expectations" 섹션에서 다음 인용 확인됨.
  > "Moving from level 1 to level 3 typically requires 12-18 months with dedicated resources and executive sponsorship."
- **비고:** 수치 정확히 일치. 이후 "Level 4까지 추가 18-24개월"도 명시되어 있어 로드맵 작성 시 참고 가능.

---

## 2. References 절 솔루션 URL 무작위 6개 생존 확인

| # | URL | 대상 | 판정 | 비고 |
|---|-----|------|------|------|
| 1 | https://www.alation.com/product/data-catalog/ | Alation 제품 페이지 | ✅ OK | 정상 접근. 페이지 제목 "Alation Data Catalog \| AI-Powered Data Discovery & Governance" |
| 2 | https://datahubproject.io/ | DataHub 공식 사이트 | ⚠️ 리다이렉트 | 301 → http://datahub.com/ 으로 영구 이동. datahub.com은 정상 접근(Acryl Data 운영 DataHub 상용 클라우드 사이트). 오픈소스 커뮤니티 사이트(datahubproject.io)에 연결되던 URL이 상용 사이트로 이동했으므로, **본문 링크 텍스트("DataHub (Acryl Data)")와 URL을 https://datahub.com/ 으로 교체 권장** |
| 3 | https://open-metadata.org/ | OpenMetadata 공식 사이트 | ✅ OK | 정상 접근. "#1 Open Source Context Layer" |
| 4 | https://www.databricks.com/product/unity-catalog | Databricks Unity Catalog | ✅ OK | 정상 접근. "Unity Catalog \| Databricks" |
| 5 | https://thedataguy.pro/blog/2025/08/open-source-data-governance-frameworks/ | TheDataGuy 블로그 | 🔴 확인불가(차단) | HTTP 403 Forbidden. 서버 접근 차단. 본문 인용 내용("오픈소스 0.5~1 FTE 운영 부담") 확인 불가. |
| 6 | https://www.collibra.com/blog/evaluating-your-data-catalogs-success | Collibra KPI 블로그 | ✅ OK | 정상 접근. Enablement / Adoption / Business Value 3분류 내용 확인됨. |

### References 절 추가 확인: Collibra 제품 페이지 (본문에서 2회 인용)

| URL | 본문 인용 목적 | 판정 |
|-----|---------------|------|
| https://www.collibra.com/products/data-catalog | [src-구축-005]: "수동 메타데이터 60~70% 정확도" + "SAP 6주→15분" | ⚠️ MISMATCH — 두 주장 모두 해당 페이지에 없음 |

---

## 3. 추가 발견 사항

### 3.1 "수동 문서화 정확도 60~70%" 주장 (§4.6, §10.2)
- **본문:** `"수동 문서화 기반 메타데이터의 정확도는 60~70%에 불과하고, 생성 직후부터 빠르게 노후화된다."` — footnote [src-구축-005] (Collibra 제품 페이지)
- **확인 결과:** Collibra 제품 페이지에 해당 수치 없음. Satori Cyber 블로그(src-구축-010)에도 없음.
- **그러나,** atlan.com/modern-data-catalog/ 에서 유사 수치 발견:
  > "Modern catalogs use active metadata that updates continuously, achieving **90%+ accuracy vs 60–70% in passive systems**"
- **판정:** MISMATCH (출처 오기재). Collibra URL이 아닌 Atlan URL에서 이 수치가 확인됨.
- **권장 수정안:** footnote를 [src-구축-005](Collibra)에서 [src-KPI-005](https://atlan.com/modern-data-catalog/)로 교체.

### 3.2 DataHub URL 리다이렉트
- `https://datahubproject.io/`가 `http://datahub.com/`으로 영구 리다이렉트됨.
- 본문 References 절 및 §6.1 본문 링크 모두 `https://datahubproject.io`로 기재되어 있음.
- **권장:** `https://datahub.com/` 으로 URL 교체. (내용 동일, Acryl Data 운영 확인됨)

---

## 4. 판정 요약

| 구분 | 건수 | 해당 항목 |
|------|------|-----------|
| ✅ OK | 4건 | [1] 20% 낭비 / [4] 커버리지 80%·60% 기준 / [6] 12~18개월 / References 4개 URL |
| ⚠️ MISMATCH | 4건 | [2] 400개 데이터 소스 / [3] 60~65% 단축(출처 맥락 불일치) / [5] SAP 6주→15분 / 수동 60~70% 정확도 출처 오기재 |
| 🔴 BROKEN | 0건 | — |
| 확인불가(차단) | 1건 | thedataguy.pro (HTTP 403) |
| ⚠️ 리다이렉트 | 1건 | datahubproject.io → datahub.com |

---

## 5. 오케스트레이터 반영 권고 (우선순위 순)

### 우선순위 1 — [2] "400개 이상 데이터 소스" 수치 삭제 또는 교체
- 기재된 두 URL(decube.io, atlan.com) 어디에도 이 수치가 없음. 출처 불명.
- **가장 간단한 조치:** §2.1의 해당 문장에서 `[src-KPI-004]` footnote를 삭제하고, "400개 이상"이라는 수치도 제거. 대신 "수천 개 이상의 데이터 자산이 여러 시스템에 분산되어 있으나 전체 목록이 없는 경우가 많다"로 서술 변경.

### 우선순위 2 — [5] "SAP 6주→15분" 출처 교체 또는 수치 삭제
- Collibra 제품 페이지에 해당 수치 없음. 올바른 Collibra URL 미발견.
- **조치 옵션:** ① Collibra 고객 사례 페이지에서 출처 확인 후 URL 교체 ② 출처 확인 불가 시 수치 제거 및 "수작업 대비 수십 배 단축"으로 대체 서술.

### 우선순위 3 — "수동 메타데이터 60~70% 정확도" 출처 교체
- §4.6의 footnote [src-구축-005](Collibra 제품 페이지)를 [src-KPI-005](https://atlan.com/modern-data-catalog/)로 교체.
- Atlan 페이지에서 동일 수치("60–70% in passive systems") 확인됨.

### 참고 — datahubproject.io 리다이렉트
- 시급성 낮음. §6.1 및 References 절의 DataHub URL을 `https://datahub.com/`으로 업데이트.

---

*검증 완료: 2026-06-18. 본 리포트는 판정 및 권고만 담으며, 가이드 본문 직접 수정은 오케스트레이터가 수행한다.*
