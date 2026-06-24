# C-2 데이터 품질 관리 — 리서치(개념·기준·KPI)

> 리서치 원자료. 가이드 본문이 아니라 작성용 재료다.
> 관점 고정: "AI를 만드는 법"이 아니라 "그 AI가 쓸 **데이터를 준비·정비·판정하는 법**"으로 정리한다.
> 주제 MECE 경계: **"쓸 수 있는가(품질)" 판정만**. 접근 권한·보안 처리는 F-4, 실시간 이상 감지는 C-1, 사후 이력 추적은 C-3.
> 가격·버전 등 변동 정보는 단정하지 않는다.

---

## 0. 품질의 출발 개념 — "용도 적합성(Fitness for Use)"

데이터 품질의 고전적 정의는 Joseph Juran의 **"용도 적합성(fitness for use)"** — 데이터가 운영·의사결정·계획 등 **의도한 용도에 적합하면** 고품질이다. 사양(spec)을 맞추는 것이 전부가 아니라 **실제 쓰임에 맞는가**가 핵심이다.
- 출처: First San Francisco Partners — Fundamental Concepts of Data Quality <https://www.firstsanfranciscopartners.com/blog/fundamental-concepts-data-quality/>
- (개념 보조) LambdaTest — Managing for Quality with Dr. Joseph Juran <https://www.lambdatest.com/blog/managing-for-quality-with-dr-joseph-juran/>

C-2에 주는 함의: 품질은 절대 기준이 아니라 **"이 AI 용도에 쓸 수 있는가"라는 상대 판정**이다. → 차원별 허용 기준(threshold)을 업무·용도별로 정해야 한다(아래 §1·§2와 연결).

---

## 1. 데이터 품질 차원(Data Quality Dimensions)

### 1-1. 정본 6개 차원 — 확정

표준·실무가 가장 널리 쓰는 **6개 차원**으로 가이드 정본을 잡는다(요청대로 6개 확정).

| 차원 | 영문 | 한 줄 뜻 | 제조 데이터 예시 |
|---|---|---|---|
| 완전성 | Completeness | 있어야 할 값이 다 채워져 있는가(결측 없음) | 설비 검사 로그에서 측정값·판정·시각 칸이 비지 않았는가 |
| 정확성 | Accuracy | 값이 실제(참값)를 올바르게 나타내는가 | 두께 측정값이 실제 두께와 일치(센서 오차·오기 없음) |
| 일관성 | Consistency | 시스템·소스 간 값이 서로 모순되지 않는가 | MES의 LOT 결과와 QMS의 동일 LOT 결과가 어긋나지 않음 |
| 최신성 | Timeliness | 필요한 시점에 최신 상태로 쓸 수 있는가 | 라인 상태 데이터가 분 단위로 갱신되어 늦지 않음 |
| 유효성 | Validity | 정해진 형식·범위·코드 규칙을 따르는가 | 불량코드가 코드표에 있는 값, 온도가 허용범위(0~300℃) 내 |
| 유일성 | Uniqueness | 같은 대상이 중복 없이 한 번만 들어가는가 | 동일 타임스탬프·동일 LOT가 두 번 적재되지 않음 |

출처:
- DAMA International / DAMA-NL — Dimensions of Data Quality(DDQ) Research Paper v1.2 (DAMA가 정의한 6개 핵심 차원: Accuracy, Completeness, Consistency, Timeliness, Uniqueness, Validity) <https://dama-nl.org/wp-content/uploads/2020/09/DDQ-Dimensions-of-Data-Quality-Research-Paper-version-1.2-d.d.-3-Sept-2020.pdf>
- Clever Republic — The six most used Data Quality dimensions (accuracy·completeness·consistency·timeliness·validity·uniqueness, DAMA-DMBOK 기반) <https://www.cleverrepublic.com/resources/blog/the-six-most-used-data-quality-dimensions/>
- Metaplane — Data Quality Metrics(6개 차원 매핑) <https://www.metaplane.dev/blog/data-quality-metrics-for-data-warehouses>

> 차원별 정확한 정의(ISO/IEC 25012 원문 표현, 가이드 인용용):
> - 정확성(Accuracy): "data has attributes that correctly represent the true value of the intended attribute of a concept or event in a specific context of use."
> - 완전성(Completeness): "subject data associated with an entity has values for all expected attributes and related entity instances in a specific context of use."
> - 일관성(Consistency): "data has attributes that are free from contradiction and are coherent with other data in a specific context of use."
> 출처: ISO 25000 portal — ISO/IEC 25012 <https://iso25000.com/index.php/en/iso-25000-standards/iso-25012>

### 1-2. 표준별 차원 개수 차이(메모 — 정본은 위 6개)

| 표준/프레임워크 | 차원 처리 | 비고 | 출처 |
|---|---|---|---|
| DAMA DDQ(2020) | **핵심 6개** (Accuracy·Completeness·Consistency·Timeliness·Uniqueness·Validity) | 실무 정본의 근거 | DAMA-NL DDQ paper(위 링크) |
| DAMA DMBOK2 | 8개 (위 6 + Integrity, Reasonability; Currency 추가 언급) | 무결성·합리성 등 확장 | DMBOK 2.0 Revisions <https://www.damadmbok.org/dmbok2-revisions> |
| ISO/IEC 25012 | **15개** (관점 2분류: 고유/시스템 의존) | 아래 §1-3 | ISO 25000 portal(위 링크), ISO 표준 페이지 <https://www.iso.org/standard/35736.html> |
| ISO 8000 | 차원 나열형이 아니라 **구문/의미/실용 품질** 3축 + 검증·교환 요건 | 마스터·참조 데이터 중심, 컴퓨터로 검증 가능한 요건 | arc42 — ISO 8000 <https://quality.arc42.org/standards/iso-8000>, ISO 8000-1:2022 <https://www.iso.org/obp/ui/#iso:std:iso:8000:-1:ed-1:v1:en> |

가이드 처리 방침: **정본은 6개 차원**으로 일관 사용. 표준 차이는 별첨/각주에 한 줄로만("DMBOK은 8개, ISO 25012는 15개로 더 세분") 언급하고 본문은 6개로 고정한다(절대 원칙 "정본 모델 하나").

### 1-3. ISO/IEC 25012 — AI 신뢰성과 직접 연결되는 표준 (메모)

ISO/IEC 25012는 SQuaRE(ISO/IEC 25000) 계열의 **데이터 품질 모델**로, 15개 특성을 **2개 관점**으로 나눈다.
- **고유 품질(Inherent)**: 데이터 자체에서 평가 가능 — 정확성(Accuracy)·완전성(Completeness)·일관성(Consistency)·신뢰성(Credibility)·최신성(Currentness) 등.
- **시스템 의존 품질(System-dependent)**: 저장·처리·접근 환경에 좌우 — 가용성(Availability)·이식성(Portability)·복구성(Recoverability)·접근성(Accessibility)·준수성(Compliance)·기밀성(Confidentiality)·효율성(Efficiency)·정밀성(Precision)·추적성(Traceability)·이해가능성(Understandability) 등.
- 출처: ISO 25000 portal <https://iso25000.com/index.php/en/iso-25000-standards/iso-25012>, arc42 — ISO/IEC 25012 <https://quality.arc42.org/standards/iso-iec-25012>
- AI 맥락: ISO/IEC 25012가 "신뢰할 수 있는 AI(Trustworthy AI)"의 데이터 품질 근거로 인용됨 — Nemko Digital 해설 <https://digital.nemko.com/standards/iso-iec-25012>

C-2 활용 메모: 가이드 본문은 **고유 품질 5개 + 유일성/유효성**으로 6개 정본을 구성하고, "기밀성·접근성·추적성"은 **F-4(보안)·C-3(계통)·C-1로 넘어간다**고 경계 표시하면 ISO 25012 분류와도 깔끔히 맞물린다(시스템 의존 특성 = 인접 주제 영역).

---

## 2. AI에서 품질이 더 중요한 이유 + AI 사용 금지/제한 데이터 기준

### 2-1. 왜 AI에서 품질이 더 치명적인가 (Garbage In, Garbage Out)

- **GIGO 원리**: 학습 데이터의 편향·오류·공백은 **그대로 모델 출력에 반영**된다. → 오답·환각·차별적 결과로 증폭. 출처: Sama — Garbage In, Garbage Out <https://www.sama.com/blog/garbage-in-garbage-out-why-data-accuracy-matters-for-ai-models>
- **증폭 위험(전통 BI 대비 차이)**: 사람이 보는 리포트는 이상값을 사람이 거를 수 있으나, AI는 나쁜 데이터를 그대로 **학습/추론에 흡수**해 대규모로 재생산한다. 출처: Leverture — Data Quality for AI <https://www.leverture.com/post/data-quality-for-ai-why-garbage-in-still-means-garbage-out>, Saifr — Why data quality is critical to AI <https://saifr.ai/blog/garbage-in-garbage-out-why-data-quality-is-critical-to-ai>
- **정량 신호(인용용, 출처 명시 필요 — 단정 회피)**: 라벨 오류가 AI 데이터셋에 광범위(주요 ML 데이터셋 평균 약 3.4% 라벨 오류, ImageNet 검증셋 2,900건+ 오류 보고). 출처: aimultiple — AI Data Quality <https://research.aimultiple.com/data-quality-ai/> (수치는 출처 인용 형태로만 사용, 본문 단정 금지)
- 위험 유형 3종 정리(가이드 Why용): ① **오답·환각**(부정확·불완전 데이터) ② **편향**(대표성 없는·치우친 데이터) ③ **재현 불가/신뢰 붕괴**(출처·이력 불명 데이터). 출처: 위 Sama·aimultiple, Medium(Dickson Lukose) — Strategies to Prevent GIGO <https://medium.com/@dickson.lukose/garbage-in-garbage-out-why-data-quality-is-the-key-to-trustworthy-ai-e506f4001433>

### 2-2. AI 학습·추론에 쓰면 안 되는(제한해야 하는) 데이터 기준

KQ② "어떤 데이터는 AI에 쓰면 안 되는가"에 대한 권위 근거. **EU AI Act Article 10(데이터 거버넌스)**이 가장 구체적이다 — 학습·검증·테스트 데이터는 거버넌스 대상이며 ① 용도 적합(relevant) ② 수집 과정·동의 여부·필터링 기준·**무엇을 왜 제외했는지** 문서화가 요구된다.
- 출처: HighRiskAudit.EU — EU AI Act Data Governance: Article 10 <https://highriskaudit.eu/blog/eu-ai-act-data-governance-article-10>

AI 사용 제한 데이터 유형(주제 정의의 5종을 외부 근거로 보강):

| 제한 사유 | 설명 | 제조 맥락 예시 | 근거 |
|---|---|---|---|
| 품질 기준 미달 | 완전성·정확성 등 차원 임계값 미달 | 결측 과다한 검사 로그, 범위 벗어난 센서값 | 거버넌스가 품질 임계값으로 결과에서 제외 — aimultiple, TechTarget(아래) |
| 미승인/출처 불명(provenance) | 출처·수집 경위가 문서화되지 않음 | 누가 언제 만든지 모르는 엑셀, 외부 반입 파일 | 동의/출처 미확보 데이터는 학습 부적합 — Living Library <https://thelivinglib.org/data-authenticity-consent-and-provenance-for-ai-are-all-broken-what-will-it-take-to-fix-them/>, JCOTS AI Training Data Brief <https://dls.virginia.gov/commissions/jcots/Materials/Policy%20Briefs/2025-AI-Training-DataBrief.pdf> |
| 최신성 미보장 | 갱신이 멈춰 현재를 반영 못함 | 단종 공정·옛 규격 기준의 과거 데이터 | 최신성 차원(§1·§4 freshness) |
| 목적 외 사용 제한 | 수집 목적과 다른 용도 사용 금지 | 특정 고객 계약상 분석 외 사용 불가 데이터 | 용도 적합(relevant)·거버넌스 — EU AI Act Art.10 |
| 대표성 결여(편향) | 특정 집단·조건을 과소/과대 표현 | 특정 라인·특정 제품만 편중된 학습셋 | 치우친 데이터는 학습 부적합 — JCOTS Brief(위), Sama |

> 가이드 작성 메모: 위 표는 **F-4(권한·동의·민감정보)와 경계**가 닿는다. C-2는 "**품질로 쓸 수 있는가**"(미달·출처불명·최신성)만 판정하고, **동의·반출 권한·개인정보**는 F-4로 넘긴다고 명시할 것(MECE 유지). EU AI Act는 양쪽에 걸치므로 "거버넌스 요건"으로만 한 번 언급.

---

## 3. Quality Gate / Data Contract 개념 (KQ③)

데이터가 AI(학습·RAG·자동화)에 **투입되기 전 품질 기준 통과를 강제하는 관문**. 핵심 패턴 4종:

### 3-1. Quality Gate(품질 관문)
배포 전 검증 게이트 — 스키마·필수 필드·기본 분포 규칙을 통과하지 못한 데이터는 운영(프로덕션)으로 못 넘어가고 **격리(quarantine)**된다. 통과해야만 승격(promote).
- 출처: Data Engineering Weekly — An Engineering Guide to Data Quality (Data Contract Perspective) <https://www.dataengineeringweekly.com/p/an-engineering-guide-to-data-quality>

### 3-2. Write-Audit-Publish(WAP) 패턴
데이터 흐름을 3단계로 분리: **Write(스테이징에 적재) → Audit(규칙·제약·스키마 검증) → Publish(통과분만 운영/하류로 승격)**. Audit 단계에서 스키마 호환성·데이터 제약·데이터 계약을 점검한다. C-2의 "AI 투입 전 게이트"를 구현하는 대표 절차.
- 출처: Medium(Sathish Kumar) — WAP Pattern in Data Pipelines <https://medium.com/@sathishdba/write-audit-publish-wap-pattern-in-data-pipelines-19defcfe73a8>, Dagster — Write-Audit-Publish <https://dagster.io/blog/python-write-audit-publish>, pipeline2insights — Data Quality Design patterns (WAP/AWAP) <https://pipeline2insights.substack.com/p/data-quality-design-patterns-wap-awap>

### 3-3. Circuit Breaker(회로 차단기) 패턴
실행 중 데이터 품질 지표가 안전 임계값을 넘으면 **"회로를 열어" 파이프라인을 물리적으로 정지**, 저품질 데이터가 하류(=AI/소비자)로 못 가게 막는다. 철학: **가용성보다 신뢰성 우선** — "품질 낮은 구간은 리포트에 빠질 수 있으나, 존재하는 데이터는 옳음이 보장된다." 잘못된 데이터를 내보내 사후에 불 끄는 비용을 없앤다.
- 출처: Modern CDO(Sandeep Uttamchandani) — Taming Data Quality with Circuit Breakers <https://modern-cdo.medium.com/taming-data-quality-with-circuit-breakers-dbe550d3ca78>, apxml — Circuit Breakers in Pipelines <https://apxml.com/courses/data-governance-quality-observability-production/chapter-5-automated-reliability-ci-pipelines/circuit-breakers-pipelines>

### 3-4. Data Contract(데이터 계약)
데이터 **생산자-소비자 간 합의를 문서화·자동 강제**하는 협약. 스키마 정의·소유자·SLO(서비스 수준 목표)·허용 변경·폐기 규칙을 담는다. 계약 위반 시 회로 차단/실패로 연결. 2021년 Andrew Jones(GoCardless)가 정식 제안 — 상류 변경이 예고 없이 하류 파이프라인을 깨는 문제 해결이 출발점.
- 출처: Atlan — Data Contracts Explained <https://atlan.com/data-contracts/>, DataHub — The What, Why, and How of Data Contracts <https://datahub.com/blog/the-what-why-and-how-of-data-contracts/>, Select Star — A Guide to Data Contracts with Andrew Jones <https://www.selectstar.com/resources/data-contracts>, Wikipedia — Data contract <https://en.wikipedia.org/wiki/Data_contract>

> 가이드 작성 메모(현업 눈높이): 이 4종을 다 나열하지 말고 **"AI 투입 전 품질 관문(Quality Gate) = 통과해야만 들어간다"** 한 모델로 설명하고, WAP·회로차단기·데이터 계약은 "이를 구현하는 방식"으로 한 줄씩만 풀이. 약어·구현 디테일은 줄인다(절대 원칙). 다이어그램 후보: "Write→Audit(게이트)→Publish, 실패 시 격리/차단" 흐름도(분기·게이트가 있어 그림이 유효).

---

## 4. 품질 규칙(Rule) 유형 — 규칙 기반 자동 점검 (KQ③ 구현, §3과 연결)

자동 Quality Gate가 돌리는 점검 규칙의 표준 유형. 각 차원(§1)과 매핑된다.

| 규칙 유형 | 영문 | 한 줄 설명 | 제조 예시 | 연결 차원 |
|---|---|---|---|---|
| 결측 체크 | Null / Completeness | 필수 칸이 비었는지(공백·whitespace 포함) | 검사 결과의 판정값이 비어 있으면 실패 | 완전성 |
| 범위 체크 | Range | 수치·날짜가 허용 범위 안인지 | 경화 온도 0~300℃ 밖이면 실패, 미래 날짜 금지 | 유효성/정확성 |
| 형식·패턴 | Format / Regex | 정해진 형식·코드값을 따르는지 | LOT 번호 형식, 불량코드가 코드표(enum) 내인지 | 유효성 |
| 참조 무결성 | Referential Integrity | 외래키가 실제 존재하는 기준값을 가리키는지 | MES의 설비ID가 설비마스터에 실제 존재 | 일관성 |
| 유일성/중복 | Uniqueness | 같은 키가 중복되지 않는지 | 동일 타임스탬프+동일 LOT 중복 적재 차단 | 유일성 |
| 최신성/SLA | Freshness | 마지막 갱신이 기준 시간 내인지 | 라인 데이터가 N분 내 갱신, 초과 시 경보 | 최신성 |
| 분포·이상치 | Distribution / Anomaly | 값 분포·통계가 평소 범위를 벗어났는지 | 불량률이 평소 분포를 크게 이탈(스턱값 의심) | (정확성, C-1과 경계) |

출처:
- Microsoft Purview — Create Data Quality Rules(Completeness/Conformity/Uniqueness/Freshness 등 규칙 분류) <https://learn.microsoft.com/en-us/purview/unified-catalog-data-quality-rules>
- Profisee — Data Quality Rules: Examples and Best Practices <https://profisee.com/blog/data-quality-rules/>
- Start Data Engineering — Types of data quality checks <https://www.startdataengineering.com/post/types-of-dq-checks/>
- Google Cloud Dataplex — Auto data quality overview(null/range/regex/uniqueness/freshness/row condition) <https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview>
- dbt Labs — Build reliable data pipelines with data quality checks <https://www.getdbt.com/blog/data-pipeline-quality-checks>

> 제조 데이터 품질·이상 사례(가이드 예시용, 매우 유효): "**열전대(thermocouple)가 고장나 마지막 값을 무한 반복** 반환 → 히스토리언이 72시간 동안 동일 측정값으로 채움" — 범위는 통과하지만 **최신성/이상치 규칙**으로 잡아야 하는 전형적 케이스. 또 센서 시계열의 **결측·중복 타임스탬프(같은 값 DTS / 다른 값 DTD)**가 흔하다.
> 출처: Lasso — What Data Quality Actually Looks Like in Manufacturing <https://lassosupplychain.com/resources/blog/what-data-quality-actually-looks-like-in-a-manufacturing-environment-and-how-to-measure-it/>, Springer — Identifying Missing Sensor Values in IoT Time Series (Smart Manufacturing) <https://link.springer.com/chapter/10.1007/978-3-031-63646-2_16>

> 경계 메모: **분포·이상치 실시간 감지**는 C-1(Observability) 영역과 닿는다. C-2는 "AI 투입 전 합격 판정 규칙"으로, C-1은 "운영 중 이상 실시간 감지"로 구분(가이드에 한 줄 경계).

---

## 5. 품질 KPI 후보 (KQ⑤)

### 5-1. 핵심 KPI 정의·방향·계산식

| # | KPI | 측정 목적 | 방향 | 계산식 |
|---|---|---|---|---|
| 1 | 품질 기준 통과율(Data Quality Score / Pass Rate) | AI 투입 대상 데이터가 품질 기준을 얼마나 통과하는가(체계의 종합 건강도) | ↑ | (통과 점검 수 ÷ 전체 실행 점검 수) × 100. 또는 (통과 레코드 ÷ 전체 레코드) × 100 |
| 2 | 품질 미달 차단 건수(Blocked/Quarantined records) | Quality Gate가 실제로 막은 저품질 데이터량(게이트가 작동하는가) | ↓(개선될수록 감소) / 모니터 | 일·월 단위 게이트 실패로 격리·차단된 레코드/데이터셋 수 |
| 3 | 품질 개선 리드타임(Mean Time to Resolve, MTTR) | 품질 이슈 발생→해결까지 걸린 시간(고치는 속도) | ↓ | 이슈별 (해결 완료 시각 − 발생/탐지 시각) 평균 |
| 4 | 정확성/오류율(Accuracy Rate / Error Rate) | 값이 참값과 얼마나 일치하는가 | 정확성↑/오류율↓ | (정확 레코드 ÷ 전체) × 100 ; 오류율 = (오류 레코드 ÷ 전체) × 100 |
| 5 | 최신성 SLA 준수율(Freshness SLA adherence) | 데이터가 기한 내 갱신된 비율 | ↑ | (SLA 내 갱신된 데이터셋 수 ÷ 전체) × 100 |
| (보조) | 데이터 다운타임(Data Downtime) | 품질 이상으로 데이터를 못 믿은 총 시간 | ↓ | 이슈 건수 × (평균 탐지시간 + 평균 해결시간) |
| (보조) | 중복 레코드율(Duplicate rate) | 유일성 위반 비율 | ↓ | (중복 레코드 ÷ 전체) × 100 |

출처:
- DQOps — Definition of Data Quality KPIs (KPI = 통과 점검 비율(0~100%); KPI = (Valid + Warning) ÷ Total × 100) <https://dqops.com/docs/dqo-concepts/definition-of-data-quality-kpis/>
- KPI Depot — Quality Assurance Pass Rate (pass rate = 통과 ÷ 전체 × 100) <https://kpidepot.com/kpi/quality-assurance-pass-rate>
- Metaplane — Data Quality Metrics(정확성율·오류율·데이터 다운타임 계산식) <https://www.metaplane.dev/blog/data-quality-metrics-for-data-warehouses>
- Uvik — Data Quality Metrics & KPIs(파이프라인 완전성·freshness SLA·스키마 검증 통과율·중복율·정확성·MTTD/MTTR 등 8개 셋) <https://uvik.net/blog/data-quality-metrics-kpis/>
- TechTarget — Evaluating data quality requires clear and measurable KPIs <https://www.techtarget.com/searchdatamanagement/tip/Evaluating-data-quality-requires-clear-and-measurable-KPIs>
- Monte Carlo — 12 Data Quality Metrics That Actually Matter <https://www.montecarlodata.com/blog-data-quality-metrics/>

> 가이드 작성 메모: 주제 정의가 명시한 3개(**통과율·미달 차단 건수·개선 리드타임**)를 정본 KPI로 쓰고, 정확성율·최신성 SLA 준수율을 보조로 둔다(3~5개 범위). KPI마다 "왜 보나·방향·식" 한 줄씩. **MTTD(탐지시간)는 C-1(이상감지) 쪽**과 겹치므로 C-2 KPI에서는 MTTR(해결)·통과율·차단 건수 중심으로 잡고, 탐지 지표는 C-1로 넘긴다고 경계 표시.

---

## 6. 인접 주제 경계 정리 (MECE — 가이드 "다른 주제와의 관계" 섹션 재료)

| 인접 주제 | C-2와의 경계 |
|---|---|
| C-1 Observability | C-1은 **운영 중 실시간 이상 감지·탐지(MTTD)**. C-2는 **AI 투입 전 합격/불합격 판정**. 분포·이상치 규칙이 닿는 부분이 접점. |
| C-3 데이터 계통(Lineage) | C-3은 **출처·이동·변환의 사후 이력 추적**. C-2는 "쓸 수 있는가" 현시점 판정. 단 출처 불명 데이터 판정 시 C-3 정보 참조. |
| F-4 AI 데이터 권한·보안 | F-4는 **접근 권한·동의·민감정보 마스킹**. C-2는 품질만. EU AI Act 거버넌스 요건은 양쪽에 걸침(C-2는 품질·출처·목적 적합, F-4는 권한·동의·개인정보). |
| B-1 데이터 전처리 | 전처리 적재 후 **품질 통과 여부 판정이 C-2**(최종 주제 정의 B-1 KQ5에 "적재 후 품질 통과는 C2"로 명시). |
| A-2 메타데이터 | 품질 기준·차원 임계값은 메타데이터로 기록·관리. C-2가 그 기준으로 판정. |

---

## 7. 가이드 작성용 핵심 정리(요약)

1. **품질 차원 정본 = 6개**: 완전성·정확성·일관성·최신성·유효성·유일성. (DAMA DDQ 근거, ISO 25012는 15개·DMBOK은 8개로 더 세분 — 각주로만)
2. **품질 = 용도 적합성(Juran)**: 절대 기준이 아니라 "이 AI 용도에 쓸 수 있는가" 상대 판정 → 차원별 임계값을 업무·용도별로.
3. **AI에서 더 치명적**: GIGO — 나쁜 데이터가 오답·환각·편향으로 **증폭·대규모 재생산**. (사람 리포트와 달리 AI는 그대로 흡수)
4. **사용 제한 데이터 5종**: 품질 미달·미승인/출처불명·최신성 미보장·목적 외 제한·대표성 결여(편향). EU AI Act Art.10이 "제외 사유 문서화" 요구.
5. **Quality Gate**: AI 투입 전 통과 강제 관문. 구현 = WAP(Write-Audit-Publish)·Circuit Breaker(임계 초과 시 파이프라인 정지)·Data Contract(생산자-소비자 합의 자동 강제).
6. **규칙 7종**: 결측·범위·형식/패턴·참조무결성·유일성·최신성·분포/이상치. 제조 예시(열전대 스턱값=최신성/이상치, 중복 타임스탬프=유일성)가 강력.
7. **KPI 정본 3 + 보조 2**: ①품질 기준 통과율 ②품질 미달 차단 건수 ③품질 개선 리드타임(MTTR) + 정확성/오류율·최신성 SLA 준수율. (MTTD 탐지지표는 C-1로)
