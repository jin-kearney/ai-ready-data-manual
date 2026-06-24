# C-1 출처 검증 메모 (2026-06-24)

본문 참고자료 URL을 web_fetch로 실제 확인한 결과와 반영 내용.

## 정정 반영(본문 수정 완료)

| 항목 | 기존 | 반영 | 근거 |
|---|---|---|---|
| Monte Carlo 공식·블로그 | montecarlodata.com | **montecarlo.ai** | 301 영구 리다이렉트(도메인 이전). 블로그 글 생존 확인 |
| Databricks | /product/machine-learning/lakehouse-monitoring | **/product/data-quality-monitoring** | 제품명·URL 변경(Lakehouse Monitoring → Data Quality Monitoring) |
| AWS Glue Data Quality | /glue/features/data-quality/ | **/glue/data-quality/** | 경로 단축(구 URL도 접속되나 정식으로 교체) |
| Metaplane | (주석 없음) | **(Datadog 인수) 주석 추가** | 인수 사실 명시 |

## 생존 확인(정상, 수정 없음)
Anomalo · Bigeye · Soda · Acceldata · Sifflet · Snowflake Docs · dbt Docs · Great Expectations · soda-core(GitHub) · Elementary · Deequ(GitHub) · Evidently — 모두 정상.

## 판단 보류·유지

- **5 Pillars 4번째 축 명칭**: Monte Carlo 현행 표기는 Freshness·Volume·Schema·Lineage·**Quality**. 본 가이드는 4번째 축을 "값 분포(Distribution)"로 표기. "품질(Quality)"은 C-2 품질 관리(쓸 수 있는가 판정)와 용어가 겹쳐 MECE 경계를 흐리므로, 값의 결측·범위·분포를 가리키는 "값 분포(Distribution)"가 더 정확하다고 판단해 유지. (Distribution도 업계 다수가 쓰는 표현.)
- **Lineage 제외**: 5 Pillars 중 계보(Lineage)는 C-3 소관이라 관측 4축에서 제외하고, "알림 대상 찾기"에 활용한다고만 명시 — MECE 경계와 일치.
- evidentlyai.com은 www 유무 모두 접속됨 — 현행 표기 유지.

## 변동 수치 단정 회피 확인
가격·기능 세부는 본문에서 단정하지 않고 "공식 문서·PoC 확인"으로 명시(§5.2 + References 머리말). 통과.
